"""Agente di assistenza di primo livello.

Due motori con la stessa interfaccia:
  - LLM (OpenAI): recupera i brani pertinenti dalle guide e chiede al modello di rispondere
    SOLO su quei brani, oppure di chiedere un chiarimento, oppure di fare escalation.
  - OFFLINE: risposte preparate per i casi dimostrativi + suggerimento della guida piu' pertinente.

Ogni turno restituisce un dizionario con:
  esito: risolto | chiarimento | escalation | guida_suggerita
  testo, fonti, argomento, tipo, (ticket_info per l'escalation)
"""
import json
import re

from . import llm
from .search import NORMATIVA, detect_modules, is_legal, strip_accents

MAX_CHIARIMENTI = 2
TIPI_TICKET = {
    "anomalia": "Richiesta assistenza per errore/anomalia",
    "supporto_operativo": "Richiesta assistenza per supporto operativo",
    "formazione": "Richiesta formazione/consulenza",
    "da_classificare": "Da classificare",
}


def norm(s):
    return strip_accents((s or "").lower())


class Agent:
    def __init__(self, index, content, scenari):
        self.index = index
        self.content = content
        self.scenari = scenari["scenari"]
        self.argomenti = content["argomenti"]
        # path della guida -> argomento (dalle fonti di corsi e quiz)
        self.path_arg = {}
        for c in content["corsi"]:
            for u in c["unita"]:
                self.path_arg.setdefault(u["path"], c["argomento"])

    # ------------------------------------------------------------------ utilita'
    def _fonte(self, path, anchor=None, sezione=None):
        d = self.index.doc(path) or {"titolo": path, "modulo": ""}
        return {"path": path, "anchor": anchor, "guida": d["titolo"], "modulo": d["modulo"],
                "sezione": sezione or d["titolo"]}

    @staticmethod
    def operator_messages(conv):
        return [m["testo"] for m in conv["messaggi"] if m["ruolo"] == "operatore"]

    @staticmethod
    def diagnosi(conv):
        """Coppie domanda dell'agente / risposta dell'operatore."""
        out, msgs = [], conv["messaggi"]
        for i, m in enumerate(msgs):
            if m["ruolo"] == "agente" and m.get("esito") == "chiarimento":
                ans = next((x["testo"] for x in msgs[i + 1:] if x["ruolo"] == "operatore"), None)
                out.append({"domanda": m["testo"], "risposta": ans or "(nessuna risposta)"})
        return out

    def retrieve(self, conv, operatore, k=6):
        """Guide Palitalsoft prima; la normativa (se importata) e' cercata a parte, con un peso minore,
        cosi' una raccolta di leggi molto grande non sommerge le guide operative."""
        q = " ".join(self.operator_messages(conv))
        mods = detect_modules(q) or [operatore["modulo"]]
        guide_mods = [m for m in {c.module for c in self.index.chunks} if m != NORMATIVA]
        hits = self.index.search(q, k=k, modules=guide_mods, boost_modules=mods)
        if any(c.module == NORMATIVA for c in self.index.chunks):
            legale = is_legal(q)
            soglia = 6 if legale else 14
            norme = [(c, s) for c, s in self.index.search(q, k=3 if legale else 2, modules=[NORMATIVA]) if s >= soglia]
            hits = hits + norme
        return hits

    # ------------------------------------------------------------------ motore LLM
    def _system_prompt(self, single_turn=False):
        args = "\n".join(f"- {k}: {v['nome']} ({v['modulo']})" for k, v in self.argomenti.items())
        extra = ("\nIn questa modalità NON puoi porre domande all'operatore: se le informazioni non bastano, "
                 "usa esito \"escalation\".") if single_turn else ""
        return f"""Sei l'assistente di primo livello per gli operatori comunali che usano i software Palitalsoft.
Il tuo obiettivo è risolvere i problemi semplici e documentati, evitando ticket inutili, ma SENZA mai inventare.

REGOLE OBBLIGATORIE
1. Usa SOLO le informazioni contenute nei BRANI DI DOCUMENTAZIONE forniti. Non inventare menu, bottoni, percorsi o procedure.
2. Se i brani descrivono chiaramente la soluzione: esito "risolto". Scrivi una risposta chiara in italiano, con passi numerati, nomi di menu e bottoni in **grassetto**, e indica in "fonti" gli identificativi dei brani usati (es. ["B1","B3"]). Senza fonti non puoi rispondere "risolto".
3. Se il problema ha più cause documentate e serve sapere quale si applica, o la richiesta è troppo vaga: esito "chiarimento" con UNA sola domanda breve e concreta. Hai già posto {{n_chiarimenti}} domande: se sono {MAX_CHIARIMENTI} o più, non puoi chiederne altre.
4. Se il caso non è documentato nei brani, è un probabile errore del software, richiede un intervento tecnico di Palitalsoft o non sei sicuro: esito "escalation". Dichiara onestamente che la documentazione non copre il caso.
5. Classifica la richiesta in "tipo_richiesta": "anomalia" (errore o malfunzionamento del software), "supporto_operativo" (come si fa / errore d'uso o di configurazione), "formazione" (richiesta esplicita di formazione).
6. Classifica l'"argomento" scegliendo UNO di questi codici:
{args}
7. In caso di escalation compila anche: "oggetto_ticket" (specifico, mai generico come "Richiesta assistenza" o "Errore"), "riassunto_tecnico" (2-4 frasi per il tecnico), "tentativi" (elenco di verifiche già fatte dall'operatore o suggerite durante la conversazione), "motivo_escalation".
8. I brani di Tipo NORMATIVA (leggi e regolamenti) servono per obblighi, termini e fondamento giuridico. Usali per rispondere a domande sulla legge citando atto e articolo, oppure per aggiungere in fondo a una risposta operativa una breve riga "Riferimento normativo: …". Da soli NON bastano a spiegare come si fa un'operazione nel software: se servono i passi nel programma e nessun brano di Tipo GUIDA li descrive, non usare esito "risolto". Non dare interpretazioni giuridiche: per i dubbi interpretativi rimanda al responsabile del servizio o al segretario comunale.{extra}

Rispondi SOLO con un oggetto JSON con queste chiavi:
{{"esito": "risolto|chiarimento|escalation", "argomento": "CODICE", "tipo_richiesta": "...", "risposta": "testo markdown (vuoto se chiarimento)", "domanda": "testo (solo se chiarimento)", "fonti": ["B1"], "oggetto_ticket": "", "riassunto_tecnico": "", "tentativi": [], "motivo_escalation": ""}}"""

    def llm_turn(self, conv, operatore, single_turn=False):
        hits = self.retrieve(conv, operatore)
        brani, idmap = [], {}
        for i, (c, score) in enumerate(hits, 1):
            bid = f"B{i}"
            idmap[bid] = c
            if c.module == NORMATIVA:
                brani.append(f"[{bid}] Tipo: NORMATIVA | Atto: {c.doc_title} | {c.section}\n{c.text[:1800]}")
            else:
                brani.append(f"[{bid}] Tipo: GUIDA | Modulo: {c.module} | Guida: {c.doc_title} | Sezione: {c.section}\n{c.text[:1800]}")
        storia = "\n".join(
            f"{'OPERATORE' if m['ruolo'] == 'operatore' else 'ASSISTENTE'}: {m['testo']}" for m in conv["messaggi"])
        user = (f"OPERATORE: {operatore['nome']} – {operatore['ufficio']} – modulo principale: {operatore['modulo']}\n\n"
                f"CONVERSAZIONE:\n{storia}\n\nBRANI DI DOCUMENTAZIONE:\n\n" + "\n\n---\n\n".join(brani))
        system = self._system_prompt(single_turn).replace("{n_chiarimenti}", str(conv.get("chiarimenti", 0)))
        out = llm.chat_json(system, [{"role": "user", "content": user}])

        esito = out.get("esito")
        if esito not in ("risolto", "chiarimento", "escalation"):
            esito = "escalation"
        arg = out.get("argomento") if out.get("argomento") in self.argomenti else "ALTRO"
        tipo = out.get("tipo_richiesta") if out.get("tipo_richiesta") in TIPI_TICKET else "supporto_operativo"
        fonti_ids = [f for f in (out.get("fonti") or []) if f in idmap]
        fonti = [self._fonte(idmap[f].path, idmap[f].anchor, idmap[f].section) for f in fonti_ids]
        consultate = [self._fonte(c.path, c.anchor, c.section) for c, _ in hits]

        if esito == "risolto" and not fonti:
            esito = "escalation"
            out["motivo_escalation"] = "La risposta generata non era supportata da nessuna guida: per prudenza il caso passa a un tecnico."
        if esito == "chiarimento" and (single_turn or conv.get("chiarimenti", 0) >= MAX_CHIARIMENTI):
            esito = "escalation"
            out.setdefault("motivo_escalation", "Dopo le domande di chiarimento il caso non risulta risolvibile con la documentazione.")

        res = {"esito": esito, "argomento": arg, "tipo": tipo, "motore": "openai", "consultate": consultate}
        if esito == "risolto":
            res.update(testo=out.get("risposta") or "", fonti=fonti)
        elif esito == "chiarimento":
            res.update(testo=out.get("domanda") or out.get("risposta") or "Puoi darmi qualche dettaglio in più?", fonti=[])
        else:
            res.update(
                testo=self._testo_escalation(out.get("motivo_escalation")),
                fonti=fonti or consultate[:3],
                ticket_info={
                    "oggetto": out.get("oggetto_ticket") or "",
                    "riassunto_tecnico": out.get("riassunto_tecnico") or "",
                    "tentativi": out.get("tentativi") or [],
                    "motivo": out.get("motivo_escalation") or "Caso non coperto dalla documentazione disponibile.",
                })
        return res

    def llm_ticket(self, conv, operatore, motivo_operatore):
        """Riassunto per il tecnico quando l'operatore dice che la soluzione non ha funzionato."""
        storia = "\n".join(f"{'OPERATORE' if m['ruolo'] == 'operatore' else 'ASSISTENTE'}: {m['testo']}" for m in conv["messaggi"])
        system = ("Prepari ticket di assistenza per i tecnici Palitalsoft. Usa solo le informazioni della conversazione. "
                  "Rispondi in JSON con chiavi: oggetto_ticket (specifico, mai generico), riassunto_tecnico (2-4 frasi), "
                  "tentativi (elenco delle soluzioni già provate), motivo_escalation, tipo_richiesta "
                  "(anomalia|supporto_operativo|formazione).")
        out = llm.chat_json(system, [{"role": "user", "content": f"{storia}\n\nL'operatore segnala: {motivo_operatore}"}])
        return {
            "oggetto": out.get("oggetto_ticket") or "",
            "riassunto_tecnico": out.get("riassunto_tecnico") or "",
            "tentativi": out.get("tentativi") or [],
            "motivo": out.get("motivo_escalation") or motivo_operatore,
            "tipo": out.get("tipo_richiesta") if out.get("tipo_richiesta") in TIPI_TICKET else None,
        }

    @staticmethod
    def _testo_escalation(motivo):
        return ("Non ho trovato nella documentazione una soluzione affidabile per questo caso, quindi **non provo a indovinare**. "
                "Ho preparato una segnalazione per il tecnico con tutto quello che mi hai detto, così non dovrai rispiegare il problema."
                + (f"\n\n*Motivo:* {motivo}" if motivo else ""))

    # ------------------------------------------------------------------ motore OFFLINE
    @staticmethod
    def _match_groups(text, groups):
        return all(any(k in text for k in g) for g in groups)

    def _scenario(self, sid):
        return next((s for s in self.scenari if s["id"] == sid), None)

    def offline_turn(self, conv, operatore, single_turn=False):
        msgs = conv["messaggi"]
        last = norm(self.operator_messages(conv)[-1])
        prev_agent = next((m for m in reversed(msgs[:-1]) if m["ruolo"] == "agente"), None)

        # 1) risposta a una domanda di chiarimento di uno scenario
        if prev_agent and prev_agent.get("esito") == "chiarimento" and prev_agent.get("scenario"):
            sc = self._scenario(prev_agent["scenario"])
            if sc and sc["id"] != "_generico":
                return self._risolvi_scenario(sc, last, operatore, after_question=True)
        if prev_agent and prev_agent.get("esito") == "chiarimento" and prev_agent.get("scenario") == "_generico":
            # seconda descrizione: riprovo con tutto il testo, altrimenti escalation
            full = norm(" ".join(self.operator_messages(conv)))
            sc = next((s for s in self.scenari if self._match_groups(full, s["match"])), None)
            if sc:
                return self._risolvi_scenario(sc, full, operatore, after_question=False, single_turn=True)
            return self._guida_o_escalation(conv, operatore, allow_question=False)

        # 2) primo messaggio: cerco uno scenario preparato
        sc = next((s for s in self.scenari if self._match_groups(last, s["match"])), None)
        if sc:
            return self._risolvi_scenario(sc, last, operatore, after_question=False, single_turn=single_turn)
        return self._guida_o_escalation(conv, operatore, allow_question=not single_turn)

    def _risolvi_scenario(self, sc, text, operatore, after_question, single_turn=False):
        fonti = [self._fonte(f["path"], f.get("anchor"), f.get("sezione")) for f in sc["fonti"]]
        base = {"argomento": sc["argomento"], "tipo": sc["tipo"], "motore": "offline", "scenario": sc["id"],
                "consultate": fonti}
        ch = sc.get("chiarimento")
        if ch:
            ramo = next((r for r in ch["rami"] if any(k in text for k in r["match"])), None)
            if ramo:
                return {**base, "esito": "risolto", "testo": ramo["risposta"], "fonti": fonti}
            if not after_question and not single_turn:
                return {**base, "esito": "chiarimento", "testo": ch["domanda"], "fonti": []}
            if ch.get("default"):
                return {**base, "esito": "risolto", "testo": ch["default"], "fonti": fonti}
        if sc.get("escalation"):
            e = sc["escalation"]
            return {**base, "esito": "escalation", "testo": self._testo_escalation(e["motivo"]), "fonti": fonti,
                    "ticket_info": {"oggetto": e["oggetto"], "riassunto_tecnico": "", "tentativi": list(e["tentativi"]),
                                    "motivo": e["motivo"]}}
        return {**base, "esito": "risolto", "testo": sc["risposta"], "fonti": fonti}

    def _guida_o_escalation(self, conv, operatore, allow_question):
        hits = self.retrieve(conv, operatore, k=3)
        consultate = [self._fonte(c.path, c.anchor, c.section) for c, _ in hits]
        if hits and hits[0][1] >= 16:
            c = hits[0][0]
            estratto = re.sub(r"\[Schermata[^\]]*\]", "", c.text).strip()
            estratto = estratto[:700] + ("…" if len(estratto) > 700 else "")
            return {
                "esito": "guida_suggerita", "motore": "offline", "scenario": None,
                # in modalita' offline la classificazione non e' affidabile: non alimenta il profilo
                "argomento": "ALTRO", "tipo": "supporto_operativo",
                "testo": (f"Ho cercato nella documentazione: la sezione più pertinente è **{c.doc_title} › {c.section}**.\n\n"
                          f"> {estratto.replace(chr(10), chr(10) + '> ')}\n\nApri la guida completa dal riquadro delle fonti. "
                          "Se non risolve, posso inoltrare la richiesta a un tecnico."),
                "fonti": [self._fonte(c.path, c.anchor, c.section)], "consultate": consultate,
            }
        if allow_question:
            return {"esito": "chiarimento", "motore": "offline", "scenario": "_generico", "argomento": "ALTRO",
                    "tipo": "da_classificare", "fonti": [], "consultate": consultate,
                    "testo": "Non sono sicuro di aver capito il problema. Puoi indicarmi in quale funzione ti trovi, "
                             "cosa stai cercando di fare e, se compare, il testo esatto del messaggio?"}
        motivo = "La richiesta non corrisponde a nessuna procedura presente nella documentazione consultata."
        return {"esito": "escalation", "motore": "offline", "scenario": None, "argomento": "ALTRO",
                "tipo": "da_classificare", "testo": self._testo_escalation(motivo), "fonti": consultate,
                "consultate": consultate,
                "ticket_info": {"oggetto": "", "riassunto_tecnico": "", "tentativi": [], "motivo": motivo}}

    # ------------------------------------------------------------------ ticket
    def build_ticket(self, conv, operatore, res, motore):
        info = res.get("ticket_info") or {}
        op_msgs = self.operator_messages(conv)
        originale = op_msgs[0] if op_msgs else ""
        diag = self.diagnosi(conv)
        modulo = self.argomenti.get(res.get("argomento"), {}).get("modulo")
        if not modulo or modulo == "-":
            modulo = operatore["modulo"]
        oggetto = info.get("oggetto") or f"{modulo.upper()} – {originale[:70]}"
        riassunto = info.get("riassunto_tecnico") or (
            f"L'operatore segnala: \"{originale}\". "
            + (" ".join(f"Alla domanda di diagnosi ha risposto: \"{d['risposta']}\"." for d in diag))
            + " La documentazione consultata non descrive il caso. " + (info.get("motivo") or ""))
        tentativi = list(info.get("tentativi") or [])
        for m in conv["messaggi"]:
            if m["ruolo"] == "agente" and m.get("esito") in ("risolto", "guida_suggerita"):
                prima_riga = re.sub(r"[*>#]", "", m["testo"]).strip().split("\n")[0][:160]
                tentativi.append(f"Soluzione proposta dall'assistente AI e provata dall'operatore: {prima_riga}")
        consultate = res.get("consultate") or res.get("fonti") or []
        tipo = res.get("tipo") or "da_classificare"
        return {
            "oggetto": oggetto,
            "tipo_ticket": TIPI_TICKET.get(tipo, tipo),
            "modulo": modulo,
            "destinatario": f"Indirizzo ticket del modulo {modulo} (elenco ufficiale: palitalsoft.it/indirizzi-per-ticket)",
            "operatore": {k: operatore[k] for k in ("id", "nome", "ufficio", "ente", "telefono", "email")},
            "descrizione_originale": originale,
            "riassunto_tecnico": riassunto,
            "diagnosi": diag,
            "tentativi": tentativi or ["Nessuna soluzione applicabile trovata nella documentazione"],
            "guide_consultate": [{"guida": f["guida"], "sezione": f["sezione"], "path": f["path"], "anchor": f.get("anchor"), "modulo": f.get("modulo")}
                                 for f in consultate],
            "motivo_escalation": info.get("motivo") or "",
            "generato_da": "Assistente AI (OpenAI)" if motore == "openai" else "Assistente (modalità offline)",
            "conformita": [
                "Oggetto specifico (non generico)",
                "Descrizione dettagliata del problema",
                "Firma e recapiti dell'operatore",
                "Una richiesta per ogni problema",
            ],
        }


def classifica_ticket(agent, testo, motore):
    """Classifica argomento e tipo di un ticket aperto a mano (per il profilo competenze).

    Ritorna None se il servizio AI non e' disponibile: il ticket resta da classificare
    e lo classifichera' il tecnico.
    """
    if motore == "down":
        return None
    if motore == "openai":
        args = "\n".join(f"- {k}: {v['nome']} ({v['modulo']})" for k, v in agent.argomenti.items())
        system = ("Classifichi ticket di assistenza degli operatori comunali sui software Palitalsoft. "
                  "Scegli l'argomento tra questi codici:\n" + args +
                  "\nScegli il tipo: \"anomalia\" (errore o malfunzionamento del software), \"supporto_operativo\" "
                  "(come si fa, errore d'uso o di configurazione), \"formazione\" (richiesta esplicita di formazione). "
                  "Se non sei sicuro dell'argomento usa ALTRO. Rispondi in JSON: "
                  "{\"argomento\": \"CODICE\", \"tipo\": \"...\", \"motivazione\": \"una frase\"}")
        out = llm.chat_json(system, [{"role": "user", "content": testo}])   # puo' sollevare LLMUnavailable
        arg = out.get("argomento") if out.get("argomento") in agent.argomenti else "ALTRO"
        tipo = out.get("tipo") if out.get("tipo") in ("anomalia", "supporto_operativo", "formazione") else "supporto_operativo"
        return {"argomento": arg, "tipo": tipo, "motivazione": out.get("motivazione") or "", "da": "Assistente AI (OpenAI)"}
    # motore offline: stesse regole a parole chiave dei casi preparati
    t = norm(testo)
    sc = next((s for s in agent.scenari if Agent._match_groups(t, s["match"])), None)
    if not sc:
        return {"argomento": "ALTRO", "tipo": "da_classificare", "motivazione": "Nessuna corrispondenza con i casi noti",
                "da": "Assistente (modalità offline)"}
    return {"argomento": sc["argomento"], "tipo": sc["tipo"], "motivazione": "Corrispondenza con un caso documentato",
            "da": "Assistente (modalità offline)"}
