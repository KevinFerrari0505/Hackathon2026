"""Profilazione delle competenze: regola trasparente e spiegabile.

Segnali usati per ogni operatore e argomento:
  - richieste di SUPPORTO OPERATIVO ("come si fa") degli ultimi 90 giorni.
    Le segnalazioni di ANOMALIA (errori del software) NON contano: non indicano una lacuna.
  - esito dell'ultimo quiz sull'argomento.

Stati:
  lacuna        -> ultimo quiz sotto il 60%
  da_verificare -> 2+ richieste di supporto senza un quiz che le smentisca (quiz assente o
                   precedente alle richieste): si propone ripasso + quiz per confermare o escludere
  competente    -> ultimo quiz >= 75% e meno di 2 richieste successive al quiz.
                   Se le richieste erano ricorrenti ma il quiz e' superato, lo si dice esplicitamente:
                   la causa probabile non e' una lacuna (caso raro, configurazione...)
  in_crescita   -> quiz tra 60% e 74%
  segnale_debole-> una sola richiesta, nessun quiz
"""
from datetime import datetime, timedelta

FINESTRA_GIORNI = 90
SOGLIA_RICHIESTE = 2
SOGLIA_SUPERATO = 75
SOGLIA_LACUNA = 60

STATI = {
    "lacuna": "Lacuna confermata",
    "da_verificare": "Possibile lacuna",
    "in_crescita": "In consolidamento",
    "competente": "Competente",
    "segnale_debole": "Segnale debole",
}


def _dt(s):
    return datetime.fromisoformat(s)


def profilo(conn, content, op_id, ref_time=None):
    now = ref_time or datetime.now()
    da = now - timedelta(days=FINESTRA_GIORNI)
    req = conn.execute(
        "SELECT * FROM richieste WHERE operatore_id=? AND argomento IS NOT NULL ORDER BY creata", (op_id,)
    ).fetchall()
    quiz = conn.execute(
        "SELECT * FROM quiz_risultati WHERE operatore_id=? ORDER BY data", (op_id,)
    ).fetchall()
    completati = {r["corso_id"] for r in conn.execute(
        "SELECT corso_id FROM corsi_completati WHERE operatore_id=?", (op_id,))}

    argomenti = content["argomenti"]
    corsi = {c["id"]: c for c in content["corsi"]}
    out = []
    for code, meta in argomenti.items():
        if code == "ALTRO":
            continue
        r_arg = [r for r in req if r["argomento"] == code and _dt(r["creata"]) >= da]
        sup = [r for r in r_arg if r["tipo"] == "supporto_operativo"]
        anom = [r for r in r_arg if r["tipo"] == "anomalia"]
        q_arg = [q for q in quiz if q["argomento"] == code]
        last_q = q_arg[-1] if q_arg else None
        sup_dopo_quiz = [r for r in sup if not last_q or _dt(r["creata"]) > _dt(last_q["data"])]

        stato, motivo = None, []
        if sup:
            motivo.append(f"{len(sup)} richiest{'a' if len(sup) == 1 else 'e'} di supporto operativo negli ultimi {FINESTRA_GIORNI} giorni")
        if anom:
            motivo.append(f"{len(anom)} segnalazion{'e' if len(anom) == 1 else 'i'} di anomalia software (non conteggiate come lacuna)")
        if last_q:
            motivo.append(f"ultimo quiz: {last_q['punteggio']}% ({_dt(last_q['data']).strftime('%d/%m/%Y')})")
        else:
            motivo.append("nessun quiz svolto")

        if last_q and last_q["punteggio"] < SOGLIA_LACUNA:
            stato = "lacuna"
        elif len(sup_dopo_quiz) >= SOGLIA_RICHIESTE:
            stato = "da_verificare"
        elif last_q and last_q["punteggio"] >= SOGLIA_SUPERATO:
            stato = "competente"
            if len(sup) >= SOGLIA_RICHIESTE:
                motivo.append("le richieste ricorrenti non sembrano dovute a una lacuna (quiz superato): "
                              "probabile caso raro o problema di configurazione")
        elif last_q:
            stato = "in_crescita"
        elif len(sup) == 1:
            stato = "segnale_debole"
        if not stato:
            continue

        # competenza numerica (per grafici): dal quiz, penalizzata dalle richieste successive;
        # senza quiz e' solo una stima dalle richieste
        if last_q:
            comp = max(0, last_q["punteggio"] - 10 * len(sup_dopo_quiz))
            stimata = False
        else:
            comp = max(20, 70 - 15 * len(sup))
            stimata = True

        # verifica periodica (ripetizione dilazionata)
        prossima = None
        if last_q:
            superati = [q for q in q_arg if q["punteggio"] >= SOGLIA_SUPERATO]
            giorni = 2 if last_q["punteggio"] < SOGLIA_SUPERATO else (7 if len(superati) <= 1 else 30)
            prossima = _dt(last_q["data"]) + timedelta(days=giorni)

        corso_id = meta.get("corso")
        out.append({
            "argomento": code, "nome": meta["nome"], "modulo": meta["modulo"],
            "stato": stato, "stato_label": STATI[stato], "competenza": comp, "stimata": stimata,
            "motivo": motivo,
            "n_supporto": len(sup), "n_anomalie": len(anom),
            "ultimo_quiz": dict(last_q) if last_q else None,
            "storico_quiz": [{"data": q["data"], "punteggio": q["punteggio"]} for q in q_arg],
            "evidenze": [{"data": r["creata"], "testo": r["testo"], "tipo": r["tipo"], "esito": r["esito"]} for r in r_arg][-5:],
            "corso": corso_id, "corso_titolo": corsi[corso_id]["titolo"] if corso_id in corsi else None,
            "corso_completato": corso_id in completati,
            "verifica_periodica": prossima.isoformat() if prossima else None,
            "verifica_scaduta": bool(prossima and prossima <= now),
        })
    ordine = {"lacuna": 0, "da_verificare": 1, "in_crescita": 2, "segnale_debole": 3, "competente": 4}
    out.sort(key=lambda x: (ordine[x["stato"]], -x["n_supporto"]))
    suggerimenti = [p for p in out if p["stato"] in ("lacuna", "da_verificare") and p["corso"]]
    verifiche = [p for p in out if p["verifica_scaduta"] and p["stato"] not in ("lacuna", "da_verificare") and p["corso"]]
    return {"argomenti": out, "suggerimenti": suggerimenti, "verifiche": verifiche}


def stato_argomento(conn, content, op_id, argomento):
    for p in profilo(conn, content, op_id)["argomenti"]:
        if p["argomento"] == argomento:
            return p
    return None
