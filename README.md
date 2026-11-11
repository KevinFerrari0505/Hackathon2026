# ORIENTO – assistenza e formazione per gli operatori comunali

Prototipo per l'**Hackathon Responsible – Palitalsoft × UNICAM (11–12 novembre 2026)**.

> Non ci limitiamo a risolvere i problemi degli operatori: trasformiamo ogni difficoltà in un'opportunità di apprendimento, aumentando progressivamente la loro autonomia e riducendo il carico di lavoro dell'assistenza.

## Avvio

Serve solo **Python 3.9 o superiore**: nessuna libreria da installare.

```bash
python app.py
# poi apri http://localhost:8000
```

Con l'assistente basato su OpenAI:

```bash
# macOS / Linux
export OPENAI_API_KEY="sk-..."
python app.py

# Windows (PowerShell)
$env:OPENAI_API_KEY="sk-..."
python app.py
```

Variabili facoltative: `OPENAI_MODEL` (predefinito `gpt-4o-mini`), `PORT` (predefinito `8000`).
**Non inserire mai la chiave nel codice o nel repository.**

Senza chiave la demo parte in **modalità offline**: risposte preparate per i casi dimostrativi, più la ricerca della guida più pertinente per tutto il resto.

## Aggiungere la normativa (Normattiva, formato XML Akoma Ntoso)

Lo zip di Normattiva **non va scompattato** e non va messo nel repository. Lo script prende solo gli atti utili:

```bash
python importa_normativa.py "C:\percorso\Normativa.zip"
```

Gli atti importati sono quelli elencati in `SELEZIONE`, in cima a `importa_normativa.py`: DPR 445/2000, CAD, DPR 223/1989, DPR 642/1972 e L. 241/1990. Lo script:
- sceglie la versione **vigente** più recente;
- crea un file Markdown per atto in `data/guide/Normativa/`, con un titolo per ogni articolo e senza le note redazionali;
- segnala gli atti che non trova.

Poi basta riavviare `python app.py`.

Per trovare altri atti da aggiungere, cerca per parola nel titolo:

```bash
python importa_normativa.py "C:\percorso\Normativa.zip" --cerca protocollo
```

Lo script stampa le righe pronte da copiare nella `SELEZIONE`.

Come l'assistente usa la normativa:
- la cerca **separatamente** dalle guide e con un peso minore, salvo quando la domanda riguarda leggi, obblighi o termini;
- la cita come **riferimento normativo**, in un riquadro distinto;
- da sola non la considera sufficiente per spiegare una procedura nel software;
- per i dubbi interpretativi rimanda al responsabile del servizio o al segretario comunale.

## Cosa fa

| Area | Funzione |
|---|---|
| **Assistente (Modulo A)** | Comprende la richiesta, cerca nelle guide Palitalsoft (ricerca BM25 per sezione), risponde con passi e fonti, pone domande di chiarimento oppure fa escalation dichiarando che la documentazione non copre il caso. |
| **Ticket per il tecnico** | Operatore, modulo, descrizione originale, riassunto tecnico, domande e risposte della diagnosi, tentativi già fatti, guide consultate, motivo dell'inoltro. Il formato rispetta la *Comunicazione Palitalsoft 01/2024* sulle richieste di assistenza. |
| **Ticket manuale** | Sempre disponibile e mai bloccato dall'AI. Mentre l'operatore scrive, compaiono le guide più pertinenti, trovate con la sola ricerca e quindi disponibili anche con l'AI ferma. Dopo l'invio, l'AI classifica argomento e tipo, così anche i ticket manuali alimentano il profilo. Se l'AI è ferma, il ticket resta "da classificare" e lo classifica il tecnico dalla lista dei ticket. |
| **Coda di emergenza** | Se l'AI non è disponibile, le richieste finiscono in coda. I tecnici le risolvono a mano; al ripristino l'AI riprende solo quelle ancora aperte. Manuali, ticket tradizionali e formazione restano sempre disponibili. |
| **Formazione (Modulo B)** | Corsi brevi costruiti sulle guide e sulle videoguide (trascrizioni), con quiz in cui ogni domanda cita la propria fonte. |
| **Profilo competenze** | Regola trasparente: le richieste di *supporto operativo* indicano una possibile lacuna, che il quiz conferma o esclude. Le *anomalie software* non contano. Verifiche periodiche a 2, 7 e 30 giorni. |
| **Dashboard responsabile** | Argomenti critici, mappa delle competenze operatori × argomenti, andamento mensile, percorsi completati. |

## Copione della demo (circa 5 minuti)

Dall'icona ⚙ in alto a destra: **Ripristina dati demo** prima di ogni prova.

1. **Laura Bianchi (operatrice)**, Home → esempio *“Le PEC arrivano ma gli allegati non finiscono nel protocollo”*.
   L'assistente chiede un chiarimento. Rispondere: *“è un pdf molto pesante, circa 30 mega”*. Arriva la soluzione con la fonte (FAQ Protocollo) e la scheda **Dall'assistenza alla formazione**: è la seconda richiesta sulla PEC, quindi viene segnalata una *possibile lacuna*.
2. Si apre il ripasso, poi il quiz. Il profilo passa da *Possibile lacuna* a *Competente*, con la verifica periodica programmata.
3. **Nuova richiesta** → esempio *“Errore interno: impossibile generare la segnatura XML”*. Alla domanda di diagnosi rispondere che i campi obbligatori sono compilati: l'assistente **non inventa** e genera il ticket completo. La nota spiega che un'anomalia non pesa sul profilo formativo.
4. **Help desk** → *Simula un guasto dell'AI*. Come operatori diversi, fare due richieste: finiscono in coda. Come help desk, risolverne una a mano e poi *Ripristina il servizio AI*. L'AI elabora solo quella rimasta aperta; l'operatore la trova in Home come “risposta differita”.
5. **Sara Galli (responsabile)** → dashboard: argomenti critici, mappa delle competenze (cliccare su un operatore) e percorsi completati.

## Struttura

```
app.py                  server HTTP e API (libreria standard)
core/search.py          indicizzazione delle guide per sezione + ricerca BM25
core/agent.py           agente: motore OpenAI e motore offline, costruzione del ticket
importa_normativa.py    importazione degli atti di Normattiva (XML Akoma Ntoso) dalle raccolte zip
core/llm.py             chiamata a OpenAI Chat Completions (urllib)
core/profiling.py       regola di profilazione delle competenze
core/db.py              schema SQLite e dati di esempio (fittizi)
data/guide/             guide Palitalsoft usate (Informazioni generali, Protocollo, Servizi Demografici)
data/content.json       argomenti, corsi e quiz (con le fonti) – da rivedere a cura del team
data/scenari_offline.json  risposte preparate per la modalità offline
static/                 interfaccia web (HTML, CSS e JavaScript senza dipendenze)
```

## Note e limiti

- Tutti i dati di operatori, ente, richieste e quiz sono **fittizi**, come richiesto dal regolamento.
- Le cartelle `video/` della documentazione contengono le **trascrizioni** dei videotutorial, non i video: nella demo il lettore video è un segnaposto dichiarato.
- Le guide non contengono immagini: le schermate sono descritte a testo e vengono mostrate come riquadri descrittivi.
- La demo usa le guide di tre aree; per estenderla basta copiare altre cartelle in `data/guide/` e aggiungere argomenti e corsi in `content.json`.
- **Strumenti di IA usati (dichiarazione richiesta dal regolamento):** OpenAI API nell'assistente; Claude (Anthropic) come supporto allo sviluppo del codice e dei contenuti.
