"""Demo hackathon Palitalsoft x UNICAM – piattaforma di assistenza e formazione.

Avvio:   python app.py            (poi apri http://localhost:8000)
OpenAI:  impostare la variabile d'ambiente OPENAI_API_KEY prima dell'avvio (facoltativo).
Solo libreria standard di Python 3.9+: nessuna installazione necessaria.
"""
import json
import mimetypes
import os
import re
import sys
import threading
import traceback
from datetime import datetime, timedelta
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

from core import db, llm, profiling
from core.agent import Agent, classifica_ticket
from core.search import GuideIndex, extract_section

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "data")
STATIC = os.path.join(BASE, "static")
PORT = int(os.environ.get("PORT", "8000"))

print("Indicizzazione delle guide…", flush=True)
INDEX = GuideIndex(os.path.join(DATA, "guide"))
CONTENT = json.load(open(os.path.join(DATA, "content.json"), encoding="utf-8"))
SCENARI = json.load(open(os.path.join(DATA, "scenari_offline.json"), encoding="utf-8"))
AGENT = Agent(INDEX, CONTENT, SCENARI)
CORSI = {c["id"]: c for c in CONTENT["corsi"]}
CONN = db.connect(os.path.join(DATA, "demo.sqlite3"))
db.ensure_seed(CONN, "openai" if llm.has_key() else "offline")
LOCK = db._lock
print(f"{len(INDEX.docs)} guide, {len(INDEX.chunks)} sezioni indicizzate.", flush=True)

QUEUE_JOB = {"attivo": False, "elaborate": 0, "totale": 0, "log": []}


# ---------------------------------------------------------------- helper dati
def q(sql, args=()):
    return db.rows(CONN.execute(sql, args))


def q1(sql, args=()):
    r = CONN.execute(sql, args).fetchone()
    return dict(r) if r else None


def operatore(op_id):
    return q1("SELECT * FROM operatori WHERE id=?", (op_id,))


def engine():
    return db.get_config(CONN, "engine", "offline")


def load_conv(cid):
    c = q1("SELECT * FROM conversazioni WHERE id=?", (cid,))
    if c:
        c["messaggi"] = db.jload(c["messaggi"], [])
    return c


def save_conv(c):
    CONN.execute("UPDATE conversazioni SET messaggi=?, chiarimenti=?, stato=?, argomento=?, tipo=?, richiesta_id=?, ticket_id=? WHERE id=?",
                 (json.dumps(c["messaggi"], ensure_ascii=False), c["chiarimenti"], c["stato"], c.get("argomento"),
                  c.get("tipo"), c.get("richiesta_id"), c.get("ticket_id"), c["id"]))


def new_ticket(op_id, modulo, origine, dati):
    cur = CONN.execute("INSERT INTO ticket (creato, operatore_id, modulo, origine, stato, dati) VALUES (?,?,?,?,?,?)",
                       (db.iso(db.now()), op_id, modulo, origine, "aperto", json.dumps(dati, ensure_ascii=False)))
    tid = cur.lastrowid
    codice = f"TCK-{datetime.now().year}-{tid:04d}"
    CONN.execute("UPDATE ticket SET codice=? WHERE id=?", (codice, tid))
    return tid, codice


def record_richiesta(op_id, testo, argomento, tipo, esito, conv_id=None, risposta=None, when=None):
    cur = CONN.execute(
        "INSERT INTO richieste (operatore_id, creata, testo, argomento, tipo, esito, conversazione_id, risposta) VALUES (?,?,?,?,?,?,?,?)",
        (op_id, when or db.iso(db.now()), testo, argomento, tipo, esito, conv_id, risposta))
    return cur.lastrowid


def formazione_suggerita(op_id, argomento, prima):
    """Il ponte assistenza -> formazione: dopo ogni richiesta ricalcola il profilo sull'argomento."""
    dopo = profiling.stato_argomento(CONN, CONTENT, op_id, argomento) if argomento else None
    if not dopo or dopo["stato"] not in ("lacuna", "da_verificare") or not dopo["corso"]:
        return None
    corso = CORSI[dopo["corso"]]
    return {
        "argomento": argomento, "nome": dopo["nome"], "stato": dopo["stato"], "stato_label": dopo["stato_label"],
        "nuovo": not prima or prima["stato"] != dopo["stato"],
        "motivo": dopo["motivo"], "corso_id": corso["id"], "corso_titolo": corso["titolo"],
        "durata_min": corso["durata_min"], "n_domande": len(corso["quiz"]),
    }


def ticket_view(t):
    t = dict(t)
    t["dati"] = db.jload(t["dati"], {})
    return t


# ---------------------------------------------------------------- assistenza
def enqueue(op, conv, testo, errore=None):
    cur = CONN.execute("INSERT INTO coda_emergenza (creata, operatore_id, testo, stato, conversazione_id, nota) VALUES (?,?,?,?,?,?)",
                       (db.iso(db.now()), op["id"], testo, "in_attesa", conv["id"], errore))
    pos = CONN.execute("SELECT COUNT(*) FROM coda_emergenza WHERE stato='in_attesa'").fetchone()[0]
    conv["stato"] = "in_coda"
    return {
        "esito": "coda", "motore": "nessuno", "coda_id": cur.lastrowid, "posizione": pos, "fonti": [],
        "testo": ("Il servizio di assistenza AI al momento **non è disponibile**. La tua richiesta è stata registrata "
                  f"nella **coda di emergenza** (n. {cur.lastrowid}, posizione {pos}): un tecnico la gestirà manualmente oppure, "
                  "se nel frattempo il servizio torna attivo, verrà elaborata automaticamente.\n\n"
                  "Nel frattempo puoi **consultare i manuali** o **aprire un ticket tradizionale**."),
    }


def run_engine(conv, op, single_turn=False):
    mode = engine()
    if mode == "openai":
        return AGENT.llm_turn(conv, op, single_turn=single_turn)   # puo' sollevare LLMUnavailable
    return AGENT.offline_turn(conv, op, single_turn=single_turn)


def chat(body):
    op = operatore(body.get("operatore_id"))
    if not op:
        raise ValueError("Operatore non valido")
    testo = (body.get("messaggio") or "").strip()
    if not testo:
        raise ValueError("Messaggio vuoto")
    with LOCK:
        conv = load_conv(body["conversazione_id"]) if body.get("conversazione_id") else None
        if not conv or conv["stato"] not in ("aperta",):
            cur = CONN.execute("INSERT INTO conversazioni (operatore_id, creata, messaggi, chiarimenti, stato) VALUES (?,?,?,?,?)",
                               (op["id"], db.iso(db.now()), "[]", 0, "aperta"))
            conv = load_conv(cur.lastrowid)
        conv["messaggi"].append({"ruolo": "operatore", "testo": testo, "ora": db.iso(db.now())})
        CONN.commit()

    if engine() == "down":
        res = None
        err = "Servizio AI non disponibile (guasto simulato)"
    else:
        try:
            res = run_engine(conv, op)
            err = None
        except llm.LLMUnavailable as e:
            res, err = None, f"Servizio AI non raggiungibile: {e}"

    with LOCK:
        if res is None:
            res = enqueue(op, conv, " / ".join(AGENT.operator_messages(conv)), err)
        else:
            res = finalize(conv, op, res)
        msg = {"ruolo": "agente", "testo": res["testo"], "esito": res["esito"], "fonti": res.get("fonti", []),
               "scenario": res.get("scenario"), "ora": db.iso(db.now())}
        for k in ("ticket", "formazione", "nota_profilo", "coda_id"):
            if res.get(k):
                msg[k] = res[k]
        conv["messaggi"].append(msg)
        save_conv(conv)
        CONN.commit()
    res["conversazione_id"] = conv["id"]
    res["stato_conversazione"] = conv["stato"]
    res.pop("consultate", None)
    res.pop("ticket_info", None)
    return res


def finalize(conv, op, res):
    """Registra la richiesta, apre il ticket se serve e calcola il suggerimento formativo."""
    if res["esito"] == "chiarimento":
        conv["chiarimenti"] += 1
        return res
    prima = profiling.stato_argomento(CONN, CONTENT, op["id"], res.get("argomento"))
    testo_orig = AGENT.operator_messages(conv)[0]
    conv["argomento"], conv["tipo"] = res.get("argomento"), res.get("tipo")
    if res["esito"] in ("risolto", "guida_suggerita"):
        conv["stato"] = "risolta"
        conv["richiesta_id"] = record_richiesta(op["id"], testo_orig, res.get("argomento"), res.get("tipo"),
                                                "risolta_ai", conv["id"], res["testo"])
    elif res["esito"] == "escalation":
        conv["stato"] = "escalation"
        dati = AGENT.build_ticket(conv, op, res, res.get("motore"))
        tid, codice = new_ticket(op["id"], dati["modulo"], "agente", dati)
        conv["ticket_id"] = tid
        conv["richiesta_id"] = record_richiesta(op["id"], testo_orig, res.get("argomento"), res.get("tipo"),
                                                "escalation", conv["id"])
        res["ticket"] = {"id": tid, "codice": codice, **dati}
    if res.get("tipo") == "anomalia":
        res["nota_profilo"] = "Segnalazione di anomalia del software: non viene conteggiata come lacuna formativa nel tuo profilo."
    else:
        res["formazione"] = formazione_suggerita(op["id"], res.get("argomento"), prima)
    return res


def escalate(body):
    """L'operatore dice che la soluzione proposta non ha funzionato: si genera il ticket per il tecnico."""
    with LOCK:
        conv = load_conv(body.get("conversazione_id"))
        if not conv:
            raise ValueError("Conversazione non trovata")
        op = operatore(conv["operatore_id"])
        motivo = (body.get("motivo") or "La soluzione proposta non ha risolto il problema").strip()
        conv["messaggi"].append({"ruolo": "operatore", "testo": f"Non ha funzionato: {motivo}", "ora": db.iso(db.now())})
    info = None
    if engine() == "openai":
        try:
            info = AGENT.llm_ticket(conv, op, motivo)
        except llm.LLMUnavailable:
            info = None
    with LOCK:
        last_agent = next((m for m in reversed(conv["messaggi"]) if m["ruolo"] == "agente"), {})
        res = {"esito": "escalation", "argomento": conv.get("argomento"), "tipo": (info or {}).get("tipo") or conv.get("tipo"),
               "fonti": last_agent.get("fonti", []), "consultate": last_agent.get("fonti", []),
               "ticket_info": info or {"oggetto": "", "riassunto_tecnico": "", "tentativi": [],
                                       "motivo": f"L'operatore segnala che la soluzione proposta non ha risolto: {motivo}"}}
        dati = AGENT.build_ticket(conv, op, res, engine())
        tid, codice = new_ticket(op["id"], dati["modulo"], "agente", dati)
        if conv.get("richiesta_id"):
            CONN.execute("UPDATE richieste SET esito='escalation' WHERE id=?", (conv["richiesta_id"],))
        conv["stato"], conv["ticket_id"] = "escalation", tid
        testo = "Capito. Ho inoltrato il caso a un tecnico con il riepilogo completo, compresa la soluzione già provata."
        ticket = {"id": tid, "codice": codice, **dati}
        conv["messaggi"].append({"ruolo": "agente", "testo": testo, "esito": "escalation", "ticket": ticket, "fonti": []})
        save_conv(conv)
        CONN.commit()
    return {"esito": "escalation", "testo": testo, "ticket": ticket, "conversazione_id": conv["id"], "stato_conversazione": "escalation"}


def manual_ticket(body):
    op = operatore(body.get("operatore_id"))
    if not op:
        raise ValueError("Operatore non valido")
    oggetto, descr = (body.get("oggetto") or "").strip(), (body.get("descrizione") or "").strip()
    if len(oggetto) < 5 or len(descr) < 10:
        raise ValueError("Inserisci un oggetto specifico e una descrizione dettagliata")
    modulo = body.get("modulo") or op["modulo"]
    dati = {
        "oggetto": oggetto, "tipo_ticket": body.get("tipo_ticket") or "Richiesta assistenza per supporto operativo",
        "modulo": modulo, "destinatario": f"Indirizzo ticket del modulo {modulo} (elenco ufficiale: palitalsoft.it/indirizzi-per-ticket)",
        "operatore": {k: op[k] for k in ("id", "nome", "ufficio", "ente", "telefono", "email")},
        "descrizione_originale": descr, "riassunto_tecnico": "", "diagnosi": [], "tentativi": [], "guide_consultate": [],
        "motivo_escalation": "Ticket aperto manualmente dall'operatore", "generato_da": "Modulo manuale",
        "conformita": ["Oggetto specifico (non generico)", "Descrizione dettagliata del problema", "Firma e recapiti dell'operatore"],
    }
    # classificazione per il profilo competenze (non blocca mai l'invio del ticket)
    try:
        cls = classifica_ticket(AGENT, f"{oggetto}\n{descr}", engine())
    except llm.LLMUnavailable:
        cls = None
    arg = cls["argomento"] if cls else None
    tipo = cls["tipo"] if cls else None
    with LOCK:
        prima = profiling.stato_argomento(CONN, CONTENT, op["id"], arg) if arg else None
        rid = record_richiesta(op["id"], descr, arg, tipo, "ticket_manuale")
        dati["richiesta_id"] = rid
        dati["classificazione"] = cls
        tid, codice = new_ticket(op["id"], modulo, "manuale", dati)
        CONN.commit()
        form = formazione_suggerita(op["id"], arg, prima) if cls and tipo == "supporto_operativo" else None
    return {"id": tid, "codice": codice, **dati, "formazione": form}


def classify_ticket(tid, body):
    """Classificazione manuale da parte del tecnico (es. ticket aperti mentre l'AI era ferma)."""
    arg = body.get("argomento") if body.get("argomento") in CONTENT["argomenti"] else None
    tipo = body.get("tipo") if body.get("tipo") in ("supporto_operativo", "anomalia", "formazione") else None
    if not arg or not tipo:
        raise ValueError("Indica argomento e tipo")
    with LOCK:
        t = q1("SELECT * FROM ticket WHERE id=?", (tid,))
        if not t:
            raise ValueError("Ticket non trovato")
        dati = db.jload(t["dati"], {})
        dati["classificazione"] = {"argomento": arg, "tipo": tipo, "motivazione": "", "da": body.get("tecnico") or "Tecnico"}
        if dati.get("richiesta_id"):
            CONN.execute("UPDATE richieste SET argomento=?, tipo=? WHERE id=?", (arg, tipo, dati["richiesta_id"]))
        CONN.execute("UPDATE ticket SET dati=? WHERE id=?", (json.dumps(dati, ensure_ascii=False), tid))
        CONN.commit()
    return ticket_view(q1("SELECT * FROM ticket WHERE id=?", (tid,)))


# ---------------------------------------------------------------- coda di emergenza
def resolve_queue_item(item_id, body):
    with LOCK:
        it = q1("SELECT * FROM coda_emergenza WHERE id=?", (item_id,))
        if not it or it["stato"] != "in_attesa":
            raise ValueError("Elemento non in attesa")
        arg = body.get("argomento") if body.get("argomento") in CONTENT["argomenti"] else "ALTRO"
        tipo = body.get("tipo") if body.get("tipo") in ("supporto_operativo", "anomalia", "formazione") else "supporto_operativo"
        nota = (body.get("nota") or "").strip() or "Risolta manualmente dal tecnico"
        CONN.execute("UPDATE coda_emergenza SET stato='risolta_manuale', risolta_da=?, nota=?, argomento=?, tipo=?, chiusa=? WHERE id=?",
                     (body.get("tecnico") or "Help desk", nota, arg, tipo, db.iso(db.now()), item_id))
        record_richiesta(it["operatore_id"], it["testo"], arg, tipo, "risolta_manuale", it["conversazione_id"], nota)
        if it["conversazione_id"]:
            conv = load_conv(it["conversazione_id"])
            if conv:
                conv["stato"] = "risolta"
                conv["messaggi"].append({"ruolo": "agente", "testo": f"**Risposta del tecnico (gestione manuale):** {nota}",
                                         "esito": "risolto", "fonti": []})
                save_conv(conv)
        CONN.commit()
    return {"ok": True}


def process_queue():
    """Quando l'AI torna disponibile riparte dalle richieste ancora in attesa (saltando quelle chiuse a mano)."""
    with LOCK:
        if QUEUE_JOB["attivo"]:
            return
        items = q("SELECT * FROM coda_emergenza WHERE stato='in_attesa' ORDER BY id")
        QUEUE_JOB.update(attivo=True, elaborate=0, totale=len(items), log=[])
        saltate = CONN.execute("SELECT COUNT(*) FROM coda_emergenza WHERE stato='risolta_manuale'").fetchone()[0]
        if saltate:
            QUEUE_JOB["log"].append(f"{saltate} richieste già risolte manualmente dai tecnici: saltate.")
    try:
        for it in items:
            if engine() == "down":
                QUEUE_JOB["log"].append("Servizio di nuovo non disponibile: elaborazione sospesa.")
                break
            with LOCK:
                cur = q1("SELECT stato FROM coda_emergenza WHERE id=?", (it["id"],))
                if cur["stato"] != "in_attesa":     # chiusa a mano nel frattempo
                    QUEUE_JOB["log"].append(f"#{it['id']} chiusa nel frattempo da un tecnico: saltata.")
                    continue
                op = operatore(it["operatore_id"])
                conv = load_conv(it["conversazione_id"])
            try:
                res = run_engine(conv, op, single_turn=True)
            except llm.LLMUnavailable as e:
                QUEUE_JOB["log"].append(f"#{it['id']}: servizio non raggiungibile ({e}). Elaborazione sospesa.")
                break
            with LOCK:
                if res["esito"] == "chiarimento":
                    res["esito"] = "escalation"
                    res.setdefault("ticket_info", {"motivo": "Servono altre informazioni dall'operatore."})
                res = finalize(conv, op, res)
                conv["messaggi"].append({"ruolo": "agente", "testo": res["testo"], "esito": res["esito"],
                                         "fonti": res.get("fonti", []), "ticket": res.get("ticket"),
                                         "formazione": res.get("formazione"), "differita": True})
                save_conv(conv)
                CONN.execute("UPDATE coda_emergenza SET stato='elaborata_ai', esito_ai=?, argomento=?, tipo=?, chiusa=? WHERE id=?",
                             (res["esito"], res.get("argomento"), res.get("tipo"), db.iso(db.now()), it["id"]))
                CONN.commit()
                QUEUE_JOB["elaborate"] += 1
                esito = "risolta dall'AI" if res["esito"] in ("risolto", "guida_suggerita") else f"ticket {res['ticket']['codice']}"
                QUEUE_JOB["log"].append(f"#{it['id']} ({op['nome']}): {esito}.")
    except Exception:
        traceback.print_exc()
        QUEUE_JOB["log"].append("Errore durante l'elaborazione della coda.")
    finally:
        QUEUE_JOB["attivo"] = False


def set_engine(body):
    mode = body.get("motore")
    if mode not in ("openai", "offline", "down"):
        raise ValueError("Motore non valido")
    if mode == "openai" and not llm.has_key():
        raise ValueError("OPENAI_API_KEY non impostata: avvia il server con la chiave per usare OpenAI")
    prev = engine()
    db.set_config(CONN, "engine", mode)
    pending = CONN.execute("SELECT COUNT(*) FROM coda_emergenza WHERE stato='in_attesa'").fetchone()[0]
    if prev == "down" and mode != "down" and pending:
        threading.Thread(target=process_queue, daemon=True).start()
    return state()


def state():
    return {
        "motore": engine(), "openai_disponibile": llm.has_key(), "modello": llm.MODEL,
        "coda_in_attesa": CONN.execute("SELECT COUNT(*) FROM coda_emergenza WHERE stato='in_attesa'").fetchone()[0],
        "job_coda": QUEUE_JOB,
    }


# ---------------------------------------------------------------- formazione
def course_detail(cid, op_id):
    c = CORSI.get(cid)
    if not c:
        raise ValueError("Corso non trovato")
    unita = []
    for u in c["unita"]:
        md = INDEX.read(u["path"]) or ""
        unita.append({**u, "testo": extract_section(md, u["anchor"]) or "", "guida": (INDEX.doc(u["path"]) or {}).get("titolo")})
    quiz = [{k: v for k, v in qq.items() if k not in ("corretta", "spiegazione")} for qq in c["quiz"]]
    storico = q("SELECT data, punteggio FROM quiz_risultati WHERE operatore_id=? AND corso_id=? ORDER BY data", (op_id, cid))
    return {**{k: c[k] for k in ("id", "argomento", "titolo", "durata_min")},
            "argomento_nome": CONTENT["argomenti"][c["argomento"]]["nome"],
            "modulo": CONTENT["argomenti"][c["argomento"]]["modulo"],
            "unita": unita, "quiz": quiz, "storico": storico}


def submit_quiz(cid, body):
    c = CORSI.get(cid)
    op = operatore(body.get("operatore_id"))
    if not c or not op:
        raise ValueError("Dati non validi")
    risposte = body.get("risposte") or []
    dettaglio, corrette = [], 0
    for i, qq in enumerate(c["quiz"]):
        r = risposte[i] if i < len(risposte) else None
        ok = r == qq["corretta"]
        corrette += ok
        dettaglio.append({"ok": ok, "data": r, "corretta": qq["corretta"], "spiegazione": qq["spiegazione"], "fonte": qq["fonte"]})
    score = round(100 * corrette / len(c["quiz"]))
    with LOCK:
        prima = profiling.stato_argomento(CONN, CONTENT, op["id"], c["argomento"])
        CONN.execute("INSERT INTO quiz_risultati (operatore_id, corso_id, argomento, data, punteggio, errori) VALUES (?,?,?,?,?,?)",
                     (op["id"], cid, c["argomento"], db.iso(db.now()), score,
                      json.dumps([i for i, d in enumerate(dettaglio) if not d["ok"]])))
        if score >= profiling.SOGLIA_SUPERATO:
            CONN.execute("INSERT OR REPLACE INTO corsi_completati VALUES (?,?,?)", (op["id"], cid, db.iso(db.now())))
        CONN.commit()
        dopo = profiling.stato_argomento(CONN, CONTENT, op["id"], c["argomento"])
    return {"punteggio": score, "corrette": corrette, "totale": len(c["quiz"]), "dettaglio": dettaglio,
            "superato": score >= profiling.SOGLIA_SUPERATO, "prima": prima, "dopo": dopo}


# ---------------------------------------------------------------- viste
def home(op_id):
    op = operatore(op_id)
    prof = profiling.profilo(CONN, CONTENT, op_id)
    convs = q("SELECT * FROM conversazioni WHERE operatore_id=? ORDER BY id DESC LIMIT 8", (op_id,))
    recenti = []
    for c in convs:
        msgs = db.jload(c["messaggi"], [])
        first = next((m["testo"] for m in msgs if m["ruolo"] == "operatore"), "")
        last = next((m for m in reversed(msgs) if m["ruolo"] == "agente"), {})
        recenti.append({"id": c["id"], "creata": c["creata"], "testo": first, "stato": c["stato"],
                        "ultima_risposta": last.get("testo", ""), "differita": last.get("differita", False),
                        "ticket": (last.get("ticket") or {}).get("codice")})
    storico = q("SELECT creata, testo, argomento, tipo, esito FROM richieste WHERE operatore_id=? ORDER BY creata DESC LIMIT 6", (op_id,))
    return {"operatore": op, "profilo": prof, "conversazioni": recenti, "storico": storico, "stato": state()}


def dashboard():
    now = datetime.now()
    req = q("SELECT * FROM richieste WHERE argomento IS NOT NULL")
    ops = q("SELECT * FROM operatori WHERE ruolo='operatore' ORDER BY id")
    # andamento mensile
    mesi = []
    for i in range(5, -1, -1):
        y, m = now.year, now.month - i
        while m <= 0:
            m += 12
            y -= 1
        mesi.append((y, m))
    nomi_mesi = ["gen", "feb", "mar", "apr", "mag", "giu", "lug", "ago", "set", "ott", "nov", "dic"]
    trend = []
    for (y, m) in mesi:
        rr = [r for r in req if datetime.fromisoformat(r["creata"]).year == y and datetime.fromisoformat(r["creata"]).month == m]
        ai = sum(1 for r in rr if r["esito"] == "risolta_ai")
        qq = q("SELECT punteggio FROM quiz_risultati WHERE substr(data,1,7)=?", (f"{y}-{m:02d}",))
        trend.append({"mese": f"{nomi_mesi[m - 1]} {str(y)[2:]}", "richieste": len(rr), "risolte_ai": ai,
                      "ticket": len(rr) - ai,
                      "media_quiz": round(sum(x["punteggio"] for x in qq) / len(qq)) if qq else None})
    # argomenti critici (ultimi 90 giorni)
    da = now - timedelta(days=90)
    per_arg = []
    profili = {o["id"]: profiling.profilo(CONN, CONTENT, o["id"]) for o in ops}
    for code, meta in CONTENT["argomenti"].items():
        if code == "ALTRO":
            continue
        rr = [r for r in req if r["argomento"] == code and datetime.fromisoformat(r["creata"]) >= da]
        sup = sum(1 for r in rr if r["tipo"] == "supporto_operativo")
        quiz = q("SELECT punteggio FROM quiz_risultati WHERE argomento=?", (code,))
        lac = sum(1 for p in profili.values() for a in p["argomenti"] if a["argomento"] == code and a["stato"] == "lacuna")
        ver = sum(1 for p in profili.values() for a in p["argomenti"] if a["argomento"] == code and a["stato"] == "da_verificare")
        per_arg.append({"argomento": code, "nome": meta["nome"], "modulo": meta["modulo"], "supporto": sup,
                        "anomalie": sum(1 for r in rr if r["tipo"] == "anomalia"),
                        "media_quiz": round(sum(x["punteggio"] for x in quiz) / len(quiz)) if quiz else None,
                        "n_quiz": len(quiz), "lacune": lac, "da_verificare": ver})
    per_arg.sort(key=lambda a: -(a["lacune"] * 3 + a["da_verificare"] * 2 + a["supporto"]))
    # matrice operatori x argomenti
    matrice = []
    for o in ops:
        stati = {a["argomento"]: {"stato": a["stato"], "competenza": a["competenza"]} for a in profili[o["id"]]["argomenti"]}
        comp = q("SELECT COUNT(*) n FROM corsi_completati WHERE operatore_id=?", (o["id"],))[0]["n"]
        matrice.append({"id": o["id"], "nome": o["nome"], "ufficio": o["ufficio"], "stati": stati, "corsi_completati": comp})
    tot90 = [r for r in req if datetime.fromisoformat(r["creata"]) >= da]
    kpi = {
        "richieste_90": len(tot90),
        "risolte_ai_90": sum(1 for r in tot90 if r["esito"] == "risolta_ai"),
        "ticket_90": sum(1 for r in tot90 if r["esito"] in ("escalation", "ticket_manuale")),
        "lacune_aperte": sum(a["lacune"] for a in per_arg),
        "da_verificare": sum(a["da_verificare"] for a in per_arg),
        "corsi_completati": q("SELECT COUNT(*) n FROM corsi_completati")[0]["n"],
        "quiz_svolti": q("SELECT COUNT(*) n FROM quiz_risultati")[0]["n"],
    }
    corsi = []
    for c in CONTENT["corsi"]:
        n = q("SELECT COUNT(*) n FROM corsi_completati WHERE corso_id=?", (c["id"],))[0]["n"]
        corsi.append({"id": c["id"], "titolo": c["titolo"], "completati": n})
    return {"kpi": kpi, "trend": trend, "argomenti": per_arg, "matrice": matrice, "corsi": corsi,
            "colonne": [{"code": k, "nome": v["nome"]} for k, v in CONTENT["argomenti"].items() if k != "ALTRO"]}


def tickets():
    return [ticket_view(t) | {"operatore_nome": (operatore(t["operatore_id"]) or {}).get("nome")}
            for t in q("SELECT * FROM ticket ORDER BY id DESC")]


def queue():
    items = q("SELECT c.*, o.nome AS operatore_nome, o.ufficio FROM coda_emergenza c JOIN operatori o ON o.id=c.operatore_id ORDER BY c.id")
    return {"elementi": items, "stato": state()}


def reset_demo(_body):
    mode = engine()
    with LOCK:
        QUEUE_JOB.update(attivo=False, elaborate=0, totale=0, log=[])
        db.reset(CONN)
        db.set_config(CONN, "engine", mode if (mode != "openai" or llm.has_key()) else "offline")
    return state()


# ---------------------------------------------------------------- HTTP
ROUTES_GET = [
    (r"^/api/stato$", lambda m, qs: state()),
    (r"^/api/operatori$", lambda m, qs: q("SELECT * FROM operatori ORDER BY ruolo DESC, id")),
    (r"^/api/home/(\w+)$", lambda m, qs: home(m.group(1))),
    (r"^/api/profilo/(\w+)$", lambda m, qs: {"operatore": operatore(m.group(1)),
                                            **profiling.profilo(CONN, CONTENT, m.group(1))}),
    (r"^/api/conversazione/(\d+)$", lambda m, qs: load_conv(int(m.group(1)))),
    (r"^/api/guide$", lambda m, qs: INDEX.docs),
    (r"^/api/guida$", lambda m, qs: {"doc": INDEX.doc(qs.get("path", [""])[0]), "testo": INDEX.read(qs.get("path", [""])[0])}),
    (r"^/api/cerca$", lambda m, qs: [dict(c.ref(400), punteggio=round(s, 1)) for c, s in INDEX.search(qs.get("q", [""])[0], k=12)]),
    (r"^/api/corsi$", lambda m, qs: [{**{k: c[k] for k in ("id", "argomento", "titolo", "durata_min")},
                                     "argomento_nome": CONTENT["argomenti"][c["argomento"]]["nome"],
                                     "modulo": CONTENT["argomenti"][c["argomento"]]["modulo"],
                                     "n_unita": len(c["unita"]), "n_domande": len(c["quiz"])} for c in CONTENT["corsi"]]),
    (r"^/api/corso/(\w+)$", lambda m, qs: course_detail(m.group(1), qs.get("op", [""])[0])),
    (r"^/api/ticket$", lambda m, qs: tickets()),
    (r"^/api/coda$", lambda m, qs: queue()),
    (r"^/api/dashboard$", lambda m, qs: dashboard()),
    (r"^/api/argomenti$", lambda m, qs: CONTENT["argomenti"]),
]
ROUTES_POST = [
    (r"^/api/chat$", lambda m, b: chat(b)),
    (r"^/api/chat/escalation$", lambda m, b: escalate(b)),
    (r"^/api/ticket$", lambda m, b: manual_ticket(b)),
    (r"^/api/ticket/(\d+)/classifica$", lambda m, b: classify_ticket(int(m.group(1)), b)),
    (r"^/api/coda/(\d+)/risolvi$", lambda m, b: resolve_queue_item(int(m.group(1)), b)),
    (r"^/api/motore$", lambda m, b: set_engine(b)),
    (r"^/api/quiz/(\w+)$", lambda m, b: submit_quiz(m.group(1), b)),
    (r"^/api/reset$", lambda m, b: reset_demo(b)),
]


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        if "/api/" in (args[0] if args else ""):
            sys.stderr.write("%s\n" % (fmt % args))

    def _send(self, code, payload, ctype="application/json; charset=utf-8"):
        data = payload if isinstance(payload, bytes) else json.dumps(payload, ensure_ascii=False, default=str).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def _dispatch(self, routes, arg):
        path = urlparse(self.path).path
        for rx, fn in routes:
            m = re.match(rx, path)
            if m:
                try:
                    self._send(200, fn(m, arg))
                except ValueError as e:
                    self._send(400, {"errore": str(e)})
                except Exception as e:
                    traceback.print_exc()
                    self._send(500, {"errore": f"Errore interno: {e}"})
                return True
        return False

    def do_GET(self):
        u = urlparse(self.path)
        if u.path.startswith("/api/"):
            if not self._dispatch(ROUTES_GET, parse_qs(u.query)):
                self._send(404, {"errore": "Non trovato"})
            return
        rel = "index.html" if u.path in ("/", "") else u.path.lstrip("/")
        full = os.path.normpath(os.path.join(STATIC, rel))
        if not full.startswith(STATIC) or not os.path.isfile(full):
            full = os.path.join(STATIC, "index.html")
        with open(full, "rb") as f:
            ctype = mimetypes.guess_type(full)[0] or "application/octet-stream"
            if ctype.startswith("text/") or ctype.endswith("javascript"):
                ctype += "; charset=utf-8"
            self._send(200, f.read(), ctype)

    def do_POST(self):
        n = int(self.headers.get("Content-Length") or 0)
        try:
            body = json.loads(self.rfile.read(n) or b"{}")
        except Exception:
            body = {}
        if not self._dispatch(ROUTES_POST, body):
            self._send(404, {"errore": "Non trovato"})


if __name__ == "__main__":
    print(f"Motore AI: {engine()}  |  OpenAI configurato: {'sì' if llm.has_key() else 'no'}  |  modello: {llm.MODEL}")
    print(f"Demo pronta su http://localhost:{PORT}")
    ThreadingHTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
