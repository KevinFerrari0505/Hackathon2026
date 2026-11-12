"""Database SQLite della demo: schema e dati di esempio (TUTTI FITTIZI)."""
import json
import random
import sqlite3
import threading
from datetime import datetime, timedelta

_lock = threading.RLock()

SCHEMA = """
CREATE TABLE IF NOT EXISTS operatori (
  id TEXT PRIMARY KEY, nome TEXT, ruolo TEXT, ufficio TEXT, ente TEXT,
  telefono TEXT, email TEXT, modulo TEXT
);
CREATE TABLE IF NOT EXISTS conversazioni (
  id INTEGER PRIMARY KEY AUTOINCREMENT, operatore_id TEXT, creata TEXT,
  messaggi TEXT, chiarimenti INTEGER DEFAULT 0, stato TEXT, argomento TEXT, tipo TEXT,
  fonti TEXT DEFAULT '[]', richiesta_id INTEGER, ticket_id INTEGER
);
CREATE TABLE IF NOT EXISTS richieste (
  id INTEGER PRIMARY KEY AUTOINCREMENT, operatore_id TEXT, creata TEXT, testo TEXT,
  argomento TEXT, tipo TEXT, esito TEXT, conversazione_id INTEGER, risposta TEXT
);
CREATE TABLE IF NOT EXISTS ticket (
  id INTEGER PRIMARY KEY AUTOINCREMENT, codice TEXT, creato TEXT, operatore_id TEXT,
  modulo TEXT, origine TEXT, stato TEXT, dati TEXT
);
CREATE TABLE IF NOT EXISTS coda_emergenza (
  id INTEGER PRIMARY KEY AUTOINCREMENT, creata TEXT, operatore_id TEXT, testo TEXT,
  stato TEXT, risolta_da TEXT, nota TEXT, argomento TEXT, tipo TEXT,
  esito_ai TEXT, conversazione_id INTEGER, chiusa TEXT
);
CREATE TABLE IF NOT EXISTS quiz_risultati (
  id INTEGER PRIMARY KEY AUTOINCREMENT, operatore_id TEXT, corso_id TEXT, argomento TEXT,
  data TEXT, punteggio INTEGER, errori TEXT
);
CREATE TABLE IF NOT EXISTS corsi_completati (
  operatore_id TEXT, corso_id TEXT, data TEXT, PRIMARY KEY (operatore_id, corso_id)
);
CREATE TABLE IF NOT EXISTS config (k TEXT PRIMARY KEY, v TEXT);
"""

ENTE = "Comune di Valfiorita (ente fittizio)"

OPERATORI = [
    # id, nome, ruolo, ufficio, telefono, modulo principale
    ("op1", "Laura Bianchi", "operatore", "Ufficio Protocollo", "0733 000 101", "Protocollo"),
    ("op2", "Marco Rossi", "operatore", "Ufficio Protocollo", "0733 000 102", "Protocollo"),
    ("op3", "Giulia Ferri", "operatore", "Servizi Demografici", "0733 000 103", "Servizi Demografici"),
    ("op4", "Paolo Neri", "operatore", "Segreteria Generale", "0733 000 104", "Protocollo"),
    ("op5", "Anna Conti", "operatore", "Ufficio Ragioneria", "0733 000 105", "Protocollo"),
    ("op6", "Luca Marini", "operatore", "Servizi Demografici", "0733 000 106", "Servizi Demografici"),
    ("op7", "Elena Fabbri", "operatore", "Ufficio Protocollo", "0733 000 107", "Protocollo"),
    ("op8", "Davide Greco", "operatore", "Polizia Locale", "0733 000 108", "Protocollo"),
    ("op9", "Chiara Lombardi", "operatore", "Servizi Demografici", "0733 000 109", "Servizi Demografici"),
    ("op10", "Stefano Ricci", "operatore", "Ufficio Tecnico", "0733 000 110", "Protocollo"),
    ("op11", "Marta Sala", "operatore", "Servizi Sociali", "0733 000 111", "Protocollo"),
    ("op12", "Andrea Villa", "operatore", "Servizi Demografici", "0733 000 112", "Servizi Demografici"),
    ("tec1", "Help desk (tecnico)", "tecnico", "Assistenza Palitalsoft", "-", "Protocollo"),
    ("resp1", "Sara Galli", "responsabile", "Responsabile formazione", "0733 000 199", "Protocollo"),
]

# Testi di esempio delle richieste storiche, per argomento e tipo
TESTI = {
    ("PROT_PEC", "supporto_operativo"): [
        "Una PEC arrivata stamattina non ha l'allegato nel protocollo",
        "Non trovo più alcune mail nell'elenco da protocollare",
        "Come scarto una mail che non va protocollata?",
    ],
    ("PROT_PARTENZA", "supporto_operativo"): [
        "La mail del protocollo in partenza non è partita",
        "Devo correggere un protocollo già inviato, come faccio?",
        "Ho inviato a 40 destinatari ma solo alcuni l'hanno ricevuta",
    ],
    ("PROT_PARTENZA", "anomalia"): ["Errore imprevisto in fase di invio PEC, il programma si blocca"],
    ("PROT_FATTURE", "supporto_operativo"): [
        "Come rifiuto una fattura elettronica ricevuta?",
        "Non capisco come protocollare una fattura in partenza",
    ],
    ("PROT_ARRIVO", "supporto_operativo"): ["Quali campi sono obbligatori per protocollare in arrivo?"],
    ("PROT_RICERCA", "supporto_operativo"): [
        "Non vedo alcuni protocolli del mio ufficio nella ricerca",
        "Come verifico se un collega ha preso in carico un protocollo?",
    ],
    ("PROT_ASSEGNAZIONI", "supporto_operativo"): ["Come trasmetto un protocollo solo in visione?"],
    ("PROT_ACCESSO", "supporto_operativo"): ["Non riesco ad entrare: numero massimo di accessi raggiunto"],
    ("DEMO_CERTIFICATI", "supporto_operativo"): [
        "Come faccio un certificato ANPR per un non residente?",
        "Ho stampato per sbaglio un certificato e mi ha memorizzato i diritti",
        "Come si fa un certificato cumulativo?",
    ],
    ("PROT_CONSERVAZIONE", "supporto_operativo"): ["Il registro giornaliero di ieri risulta non versato?"],
}


def connect(path):
    conn = sqlite3.connect(path, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.executescript(SCHEMA)
    return conn


def now():
    return datetime.now().replace(microsecond=0)


def iso(dt):
    return dt.replace(microsecond=0).isoformat()


def reset(conn):
    with _lock:
        for t in ["operatori", "conversazioni", "richieste", "ticket", "coda_emergenza",
                  "quiz_risultati", "corsi_completati"]:
            conn.execute(f"DELETE FROM {t}")
        conn.execute("DELETE FROM sqlite_sequence")
        seed(conn)
        conn.commit()


def seed(conn):
    rnd = random.Random(42)
    t0 = now()
    for (oid, nome, ruolo, uff, tel, mod) in OPERATORI:
        email = nome.lower().split(" (")[0].replace(" ", ".") + "@valfiorita.example"
        conn.execute("INSERT INTO operatori VALUES (?,?,?,?,?,?,?,?)",
                     (oid, nome, ruolo, uff, ENTE, tel, email, mod))

    def req(op, days_ago, arg, tipo, esito="risolta_ai", testo=None):
        txt = testo or rnd.choice(TESTI.get((arg, tipo), ["Richiesta di supporto"]))
        d = t0 - timedelta(days=days_ago, hours=rnd.randint(0, 6), minutes=rnd.randint(0, 59))
        conn.execute("INSERT INTO richieste (operatore_id, creata, testo, argomento, tipo, esito) VALUES (?,?,?,?,?,?)",
                     (op, iso(d), txt, arg, tipo, esito))

    def quiz(op, days_ago, corso, arg, score, completed=True):
        d = t0 - timedelta(days=days_ago)
        conn.execute("INSERT INTO quiz_risultati (operatore_id, corso_id, argomento, data, punteggio, errori) VALUES (?,?,?,?,?,?)",
                     (op, corso, arg, iso(d), score, "[]"))
        if completed:
            conn.execute("INSERT OR REPLACE INTO corsi_completati VALUES (?,?,?)", (op, corso, iso(d)))

    # --- Laura Bianchi (protagonista della demo) ---
    req("op1", 21, "PROT_PEC", "supporto_operativo", testo="Una PEC arrivata stamattina non ha l'allegato nel protocollo")
    req("op1", 55, "PROT_FATTURE", "supporto_operativo")
    req("op1", 40, "PROT_FATTURE", "supporto_operativo", esito="escalation")
    req("op1", 33, "PROT_PARTENZA", "anomalia", esito="escalation")   # anomalia: NON conta come lacuna
    quiz("op1", 70, "C_ARRIVO", "PROT_ARRIVO", 100)
    quiz("op1", 30, "C_FATTURE", "PROT_FATTURE", 50)

    # --- Marco Rossi: richieste ricorrenti MA quiz superato -> non e' una lacuna ---
    req("op2", 60, "PROT_PARTENZA", "supporto_operativo")
    req("op2", 45, "PROT_PARTENZA", "supporto_operativo")
    req("op2", 12, "PROT_PARTENZA", "supporto_operativo", esito="escalation",
        testo="Ho inviato a 40 destinatari ma solo alcuni l'hanno ricevuta")
    quiz("op2", 35, "C_PARTENZA", "PROT_PARTENZA", 100)
    quiz("op2", 80, "C_PEC", "PROT_PEC", 75)
    quiz("op2", 20, "C_PEC", "PROT_PEC", 100)

    # --- Giulia Ferri: lacuna sui certificati, poi in miglioramento ---
    req("op3", 85, "DEMO_CERTIFICATI", "supporto_operativo")
    req("op3", 70, "DEMO_CERTIFICATI", "supporto_operativo")
    req("op3", 62, "DEMO_CERTIFICATI", "supporto_operativo", esito="escalation")
    quiz("op3", 58, "C_CERTIFICATI", "DEMO_CERTIFICATI", 25, completed=False)
    quiz("op3", 30, "C_CERTIFICATI", "DEMO_CERTIFICATI", 50)
    quiz("op3", 5, "C_CERTIFICATI", "DEMO_CERTIFICATI", 75)

    # --- Paolo Neri: segnali dalle richieste, nessun quiz -> da verificare ---
    req("op4", 28, "PROT_RICERCA", "supporto_operativo")
    req("op4", 9, "PROT_RICERCA", "supporto_operativo", esito="escalation")
    req("op4", 50, "PROT_ASSEGNAZIONI", "supporto_operativo")
    req("op4", 15, "PROT_PEC", "supporto_operativo")
    req("op4", 4, "PROT_PEC", "supporto_operativo")

    # --- Anna Conti: fatture ---
    req("op5", 66, "PROT_FATTURE", "supporto_operativo")
    req("op5", 18, "PROT_FATTURE", "supporto_operativo")
    req("op5", 7, "PROT_ACCESSO", "supporto_operativo")
    quiz("op5", 10, "C_FATTURE", "PROT_FATTURE", 50)

    # --- Luca Marini: competente ---
    req("op6", 75, "DEMO_CERTIFICATI", "supporto_operativo")
    quiz("op6", 50, "C_CERTIFICATI", "DEMO_CERTIFICATI", 100)
    quiz("op6", 40, "C_ARRIVO", "PROT_ARRIVO", 75)

    # --- Storico generale (ultimi 6 mesi) per i grafici della dashboard ---
    # (operatori "di sfondo", cosi' i profili usati nella demo restano controllati)
    ops = ["op7", "op8", "op9", "op10", "op11", "op12"]
    pesi = [("PROT_PEC", 6), ("PROT_PARTENZA", 5), ("PROT_FATTURE", 4), ("DEMO_CERTIFICATI", 4),
            ("PROT_RICERCA", 3), ("PROT_ARRIVO", 2), ("PROT_ASSEGNAZIONI", 2), ("PROT_ACCESSO", 2),
            ("PROT_CONSERVAZIONE", 1)]
    args = [a for a, w in pesi for _ in range(w)]
    for month in range(6, 0, -1):         # da 6 mesi fa fino al mese scorso
        n = 14 + (month * 2)              # meno richieste nei mesi recenti
        for _ in range(n):
            days = month * 30 + rnd.randint(0, 29)
            a = rnd.choice(args)
            tipo = "anomalia" if rnd.random() < 0.18 else "supporto_operativo"
            if (a, tipo) not in TESTI:
                tipo = "supporto_operativo"
            # quota risolta dall'AI cresce nel tempo (piattaforma piu' matura)
            p_ai = 0.45 + (6 - month) * 0.06
            esito = "risolta_ai" if (tipo == "supporto_operativo" and rnd.random() < p_ai) else "escalation"
            req(rnd.choice(ops), days, a, tipo, esito=esito)
    # quiz degli operatori di sfondo, per la dashboard
    for op in ops:
        for corso, arg in [("C_PEC", "PROT_PEC"), ("C_PARTENZA", "PROT_PARTENZA"), ("C_FATTURE", "PROT_FATTURE"),
                           ("C_CERTIFICATI", "DEMO_CERTIFICATI"), ("C_RICERCA", "PROT_RICERCA"), ("C_ARRIVO", "PROT_ARRIVO")]:
            if rnd.random() < 0.6:
                first = rnd.choice([25, 50, 50, 75, 75, 100])
                d1 = rnd.randint(60, 150)
                quiz(op, d1, corso, arg, first)
                if first < 75 and rnd.random() < 0.7:
                    quiz(op, rnd.randint(5, d1 - 10), corso, arg, min(100, first + rnd.choice([25, 25, 50])))
    conn.commit()


def ensure_seed(conn, default_engine):
    with _lock:
        if conn.execute("SELECT COUNT(*) FROM operatori").fetchone()[0] == 0:
            seed(conn)
            conn.execute("INSERT OR REPLACE INTO config VALUES ('engine', ?)", (default_engine,))
            conn.commit()


def get_config(conn, k, default=None):
    r = conn.execute("SELECT v FROM config WHERE k=?", (k,)).fetchone()
    return r["v"] if r else default


def set_config(conn, k, v):
    with _lock:
        conn.execute("INSERT OR REPLACE INTO config VALUES (?,?)", (k, v))
        conn.commit()


def rows(cur):
    return [dict(r) for r in cur.fetchall()]


def jload(s, default=None):
    try:
        return json.loads(s) if s else default
    except Exception:
        return default
