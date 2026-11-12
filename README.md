# ORIENTO

**Assistenza e formazione per gli operatori comunali**

Prototipo sviluppato per l'*Hackathon Responsible – Palitalsoft × UNICAM* (11–12 novembre 2026).

ORIENTO integra in un'unica piattaforma l'assistenza di primo livello e la formazione continua. Ogni richiesta di supporto viene risolta tramite retrieval sulla documentazione ufficiale e, quando indica una possibile lacuna di competenza, viene convertita in un percorso formativo mirato. L'obiettivo è aumentare progressivamente l'autonomia degli operatori e ridurre il carico sull'assistenza tecnica.

---

## Indice

1. [Caratteristiche](#caratteristiche)
2. [Architettura](#architettura)
3. [Requisiti e avvio](#requisiti-e-avvio)
4. [Configurazione](#configurazione)
5. [Ingestione della normativa](#ingestione-della-normativa)
6. [Componenti funzionali](#componenti-funzionali)
7. [Scenario dimostrativo](#scenario-dimostrativo)
8. [Struttura del repository](#struttura-del-repository)
9. [Limiti noti](#limiti-noti)
10. [Dichiarazione sull'uso di strumenti di IA](#dichiarazione-sulluso-di-strumenti-di-ia)

---

## Caratteristiche

- **Zero dipendenze**: solo libreria standard di Python (`http.server`, `sqlite3`, `urllib`).
- **Retrieval ibrido e tracciabile**: ricerca BM25 per sezione sulle guide Palitalsoft; ogni risposta cita le fonti utilizzate.
- **Gestione esplicita dell'incertezza**: in assenza di copertura documentale l'assistente non inventa, dichiara il limite ed esegue l'escalation con un ticket completo.
- **Degrado controllato**: funzionamento in modalità offline senza chiave API e coda di emergenza in caso di indisponibilità dell'AI.
- **Profilazione trasparente**: regola deterministica e ispezionabile, senza punteggi opachi.
- **Separazione tra guide e normativa**: indici distinti, pesi differenti e citazione in un riquadro dedicato.

## Architettura

```
                +-------------------------+
                |  Interfaccia web (SPA)  |
                |  HTML / CSS / JS        |
                +-----------+-------------+
                            | HTTP / JSON
                +-----------v-------------+
                |  app.py                 |
                |  Server HTTP + API      |
                +----+------+------+------+
                     |      |      |
        +------------+      |      +--------------+
        |                   |                     |
+-------v--------+  +-------v--------+   +--------v---------+
| core/agent.py  |  | core/profiling |   | core/db.py       |
| Orchestrazione |  | Regola         |   | SQLite + seed    |
| e ticket       |  | competenze     |   | dati fittizi     |
+---+--------+---+  +----------------+   +------------------+
    |        |
+---v----+ +-v-----------+
|core/   | |core/llm.py  |
|search  | |OpenAI Chat  |
|BM25    | |Completions  |
+---+----+ +-------------+
    |
+---v---------------------------+
| data/guide/  (guide + norme)  |
| data/content.json (corsi/quiz)|
+-------------------------------+
```

### Flusso di una richiesta

1. L'operatore invia una richiesta in linguaggio naturale.
2. `core/search.py` recupera le sezioni più pertinenti dalle guide; la normativa è interrogata in un indice separato con peso inferiore, salvo domande su leggi, obblighi o termini.
3. `core/agent.py` decide tra: **risposta con fonti**, **domanda di chiarimento** o **escalation** con generazione del ticket.
4. `core/profiling.py` valuta se la richiesta costituisce un indizio di lacuna e, in caso, propone il percorso formativo collegato.

Il motore dell'agente è selezionabile a runtime: **OpenAI** se `OPENAI_API_KEY` è presente, **offline** in caso contrario.

## Requisiti e avvio

**Requisiti:** Python 3.9 o superiore. Nessuna libreria da installare.

```bash
python app.py
```

L'applicazione è disponibile su `http://localhost:8000`.

### Con l'assistente basato su OpenAI

```bash
# macOS / Linux
export OPENAI_API_KEY="sk-..."
python app.py
```

```powershell
# Windows (PowerShell)
$env:OPENAI_API_KEY="sk-..."
python app.py
```

> **Sicurezza:** la chiave API non deve mai essere inserita nel codice sorgente né nel repository.

### Modalità offline

In assenza di `OPENAI_API_KEY` l'applicazione si avvia in modalità offline: risposte predefinite per i casi dimostrativi (`data/scenari_offline.json`) e ricerca della guida più pertinente per tutte le altre richieste.

## Configurazione

| Variabile        | Obbligatoria | Predefinito   | Descrizione                          |
|------------------|:------------:|---------------|--------------------------------------|
| `OPENAI_API_KEY` | No           | —             | Abilita il motore basato su OpenAI   |
| `OPENAI_MODEL`   | No           | `gpt-4o-mini` | Modello utilizzato per le chiamate   |
| `PORT`           | No           | `8000`        | Porta di ascolto del server HTTP     |

## Ingestione della normativa

Gli atti normativi vengono importati da raccolte zip di Normattiva in formato XML **Akoma Ntoso**. Lo zip **non va scompattato** né versionato nel repository.

```bash
python importa_normativa.py "C:\percorso\Normativa.zip"
```

Gli atti importati sono quelli elencati nella costante `SELEZIONE`, in testa a `importa_normativa.py`:

- DPR 445/2000
- Codice dell'Amministrazione Digitale (CAD)
- DPR 223/1989
- DPR 642/1972
- L. 241/1990

Lo script:

- seleziona la **versione vigente** più recente di ciascun atto;
- genera un file Markdown per atto in `data/guide/Normativa/`, con un titolo per ciascun articolo e senza note redazionali;
- segnala gli atti non trovati nello zip.

Al termine è necessario riavviare `python app.py` per reindicizzare i contenuti.

### Ricerca di ulteriori atti

```bash
python importa_normativa.py "C:\percorso\Normativa.zip" --cerca protocollo
```

La ricerca opera per parola chiave sul titolo e stampa le righe già formattate per essere aggiunte a `SELEZIONE`.

### Utilizzo della normativa da parte dell'assistente

- Interrogazione **separata** dalle guide, con peso inferiore, tranne che per domande su leggi, obblighi o termini.
- Citazione come **riferimento normativo**, in un riquadro distinto dalle fonti operative.
- La normativa da sola non è considerata sufficiente per spiegare una procedura nel software.
- Per i dubbi interpretativi l'assistente rimanda al responsabile del servizio o al segretario comunale.

## Componenti funzionali

### Modulo A – Assistenza

| Componente | Descrizione |
|---|---|
| **Assistente** | Interpreta la richiesta, cerca nelle guide (BM25 per sezione) e risponde con passi operativi e fonti. Pone domande di chiarimento quando la richiesta è ambigua; esegue l'escalation dichiarando esplicitamente che la documentazione non copre il caso. |
| **Ticket per il tecnico** | Contiene: operatore, modulo, descrizione originale, riepilogo tecnico, domande e risposte della diagnosi, tentativi già effettuati, guide consultate, motivo dell'inoltro. Il formato è conforme alla *Comunicazione Palitalsoft 01/2024* sulle richieste di assistenza. |
| **Ticket manuale** | Sempre disponibile, mai bloccato dall'AI. Durante la scrittura vengono suggerite le guide più pertinenti tramite sola ricerca, quindi anche con l'AI ferma. Dopo l'invio l'AI classifica argomento e tipo, alimentando anche con i ticket manuali il profilo. Se l'AI non è disponibile il ticket resta "da classificare" e viene classificato dal tecnico. |
| **Coda di emergenza** | In caso di indisponibilità dell'AI le richieste vengono accodate e gestite manualmente dai tecnici. Al ripristino l'AI elabora esclusivamente quelle ancora aperte. Manuali, ticket tradizionali e formazione restano sempre accessibili. |

### Modulo B – Formazione

| Componente | Descrizione |
|---|---|
| **Corsi** | Percorsi brevi costruiti su guide e videoguide (trascrizioni), con quiz in cui ogni domanda riporta la propria fonte. |
| **Profilo competenze** | Regola esplicita: le richieste di *supporto operativo* indicano una possibile lacuna, che il quiz conferma o esclude; le *anomalie software* non incidono sul profilo. Verifiche periodiche a 2, 7 e 30 giorni. |
| **Dashboard responsabile** | Argomenti critici, mappa delle competenze (operatori × argomenti), andamento mensile, percorsi completati. |

## Scenario dimostrativo

Durata indicativa: 5 minuti. Prima di ogni prova usare **Ripristina dati demo** dall'icona ⚙ in alto a destra.

| # | Ruolo | Azione | Risultato atteso |
|---|---|---|---|
| 1 | Laura Bianchi (operatrice) | Home → *"Le PEC arrivano ma gli allegati non finiscono nel protocollo"*; al chiarimento rispondere *"è un pdf molto pesante, circa 30 mega"* | Soluzione con fonte (FAQ Protocollo) e scheda **Dall'assistenza alla formazione**: seconda richiesta sulla PEC, quindi segnalata una *possibile lacuna* |
| 2 | Laura Bianchi | Ripasso e quiz | Profilo da *Possibile lacuna* a *Competente*, con verifica periodica programmata |
| 3 | Laura Bianchi | Nuova richiesta → *"Errore interno: impossibile generare la segnatura XML"*; alla diagnosi rispondere che i campi obbligatori sono compilati | L'assistente non inventa e genera il ticket completo; la nota chiarisce che un'anomalia non pesa sul profilo formativo |
| 4 | Help desk | *Simula un guasto dell'AI*; come due operatori diversi inviare due richieste; come help desk risolverne una a mano; *Ripristina il servizio AI* | Le richieste finiscono in coda; l'AI elabora solo quella rimasta aperta, che l'operatore trova in Home come "risposta differita" |
| 5 | Sara Galli (responsabile) | Dashboard | Argomenti critici, mappa delle competenze (con dettaglio per operatore), percorsi completati |

## Struttura del repository

```
.
├── app.py                      # Server HTTP e API (libreria standard)
├── importa_normativa.py        # Importazione atti Normattiva (Akoma Ntoso) da zip
├── core/
│   ├── search.py               # Indicizzazione per sezione + ricerca BM25
│   ├── agent.py                # Agente (motori OpenAI e offline) e costruzione ticket
│   ├── llm.py                  # Client OpenAI Chat Completions (urllib)
│   ├── profiling.py            # Regola di profilazione delle competenze
│   └── db.py                   # Schema SQLite e dati di esempio (fittizi)
├── data/
│   ├── guide/                  # Guide Palitalsoft (Informazioni generali, Protocollo,
│   │                           #   Servizi Demografici) e normativa importata
│   ├── content.json            # Argomenti, corsi e quiz con fonti (da rivedere a cura del team)
│   └── scenari_offline.json    # Risposte predefinite per la modalità offline
└── static/                     # Interfaccia web (HTML, CSS, JavaScript senza dipendenze)
```

## Limiti noti

- Tutti i dati relativi a operatori, ente, richieste e quiz sono **fittizi**, come previsto dal regolamento.
- Le cartelle `video/` della documentazione contengono le **trascrizioni** dei videotutorial, non i video: nella demo il lettore video è un segnaposto dichiarato.
- Le guide non contengono immagini: le schermate sono descritte a testo e mostrate come riquadri descrittivi.
- La demo copre tre aree documentali. Per estenderla è sufficiente copiare ulteriori cartelle in `data/guide/` e aggiungere argomenti e corsi in `data/content.json`.
- Il contenuto di `data/content.json` (corsi e quiz) richiede revisione da parte del team prima di un uso reale.

## Dichiarazione sull'uso di strumenti di IA

Come richiesto dal regolamento dell'hackathon:

- **OpenAI API**: motore dell'assistente a runtime.
- **Claude (Anthropic)**: supporto allo sviluppo del codice e dei contenuti.
