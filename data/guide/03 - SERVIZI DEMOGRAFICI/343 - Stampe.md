# Stampe

## Stampa suddivisione territorio in sezioni

Dal menù **Servizi Demografici→Elettorale→Elettorale→Stampe→Stampa suddivisione territorio in sezioni** è possibile generare una stampa della ripartizione del territorio in sezioni elettorali.

Questa funzione genera un elenco diviso per sezione elettorale con la suddivisione delle varie vie del territorio.

La suddivisione del territorio in sezioni viene definita tramite gli elementi del Viario.
Il codice elemento (fisso) delle sezioni elettorali è il **5**.

E' qui permesso di cambiare questo codice, perché può essere utile durante la fase di risuddivisione del territorio in sezioni, andare a stampare la nuova suddivisione del territorio. Suddivisione che si sta ancora definendo, e che quindi temporaneamente è caricata su un codice diverso dal 5.

E' possibile cambiare le due **intestazioni** per la stampa e scegliere anche il **metodo di conteggio** da utilizzare.

- Si può ottenere la stampa **senza nessun conteggio** del numero di elettori.
- Si può scegliere **"Elettori"**, nell'elenco delle vie associate ad ogni sezione ci sarà anche il numero di elettori presenti in quella via.
- Se si sceglie invece **"Da copia elettorale"**, il conteggio avverrà non dall'Elettorale, ma dalla copia di lavoro usata per la ricompilazione delle liste.

> Questa scelta deve essere indicata solamente nel menù della ricompilazione liste.

Dopo aver impostato i vari parametri premere **Stampa** per generare il report.

[Schermata: Finestra "Stampa Suddivisione Territorio" con campo Elemento impostato su "5 - SEZIONI ELETTORALI", campi Intestazione 1 e Intestazione 2, sezione "Conteggio" con dropdown "Seleziona il conteggio da utilizzare" che mostra le opzioni: Nessun conteggio, Elettori, Da copia elettorale. Pulsante Stampa a destra.]

### Esempio di report

Esempio di report con codice elemento default. Sono stati compilati entrambi i campi delle intestazioni ed è stato scelto il conteggio "Elettori".

**Suddivisione territorio in Sezioni** — Comune di [Comune] — 22-11-2022
*Intestazione 2*

**SEZIONE 1**

| Via | Pari/Dis | Da | A | Tot M | Tot F | Tot M F |
|-----|----------|----|----|-------|-------|---------|
| [Via] | | | | | | |
| 125 via a. fogazzaro | T | | 999999 | 41 | 46 | 87 |
| [Via] | | | | | | |
| 30 via belluno | T | | 999999 | 29 | 35 | 64 |
| 50 via brescia | T | | 999999 | 26 | 31 | 57 |
| 10 via d. alighieri | T | | 999999 | 28 | 24 | 52 |

---

## Stampe residenti estero

Dal menù **Servizi Demografici→Elettorale→Elettorale→Stampe→Stampa residenti estero** è possibile generare una stampa degli elettori residenti all'estero filtrando per zona di residenza.

- E' possibile scegliere come zona di residenza **CEE**, **EXTRACEE**, **TUTTI** o una **nazione precisa**.
- Si può indicare un **ordinamento** per la stampa.
- E' obbligatorio indicare un **testo** (es. "Residenti estero").
- Il formato di output può essere un **DOCX (editabile a video)** o un **PDF (non editabile)**.

Premere **Stampa** per generare il testo scelto.

[Schermata: Finestra "Stampe residenti estero" con campi: Tipo lista (1 - Liste Elettorali), Zona residenza (Seleziona: CEE), Nazione estera (campo con ricerca), Ordina per (Stato estero residenza / Sesso / Nome), Codice testo (campo obbligatorio evidenziato in rosso), Formato di output (Documento in formato DOCX). Pulsanti: Salva Parametri, Stampa.]

---

## Stampa parametrica

Dal menù **Servizi Demografici→Elettorale→Elettorale→Stampe→Stampa parametrica** è possibile generare delle stampe in formato testo o excel utilizzando un'ampia scelta di filtri.

### Passaggio 1 – Destinazione della stampa

Come primo passaggio occorre scegliere la **destinazione della stampa**, che può essere un **testo** o una **stampa fissa** (con colonne preimpostate) in excel.

- Se si è scelto **testo** occorre selezionare un testo dall'elenco e proseguire cliccando su **Avanti**.

[Schermata: Finestra "Stampa Parametrica" con campo "Destinazione della stampa" impostato su "Testo", campo Documento con ricerca, checkbox "Stampa in formato PDF". Pulsante Avanti.]

- Se si è scelto **Stampa fissa** occorre indicare anche il tracciato excel da generare, il nome del foglio e se si vogliono stampare solo i totali (verranno stampati solo i numeri totali e non i singoli nominativi). Dopo di che cliccare su **Avanti**.

[Schermata: Finestra "Stampa Parametrica" con campo "Destinazione della stampa" impostato su "Stampa Fissa", campo "Scegli il tracciato excel da generare" (Sintetico (Fascicolo, sezione, sesso, Cognome, Nome, Data Nascita, Luogo nascita)), campo "Indica nome del foglio" (Estrazione personalizzata), checkbox "Stampa solo totali". Pulsante Avanti.]

### Passaggio 2 – Tipo lista e tipologia elettore

Indicare il **tipo lista** e selezionare il filtro sulla tipologia di elettore, di default sarà indicato **Attivo**. Cliccare su **Avanti** per proseguire.

[Schermata: Finestra "Stampa Parametrica" con campo "Tipo Lista" (1 - Liste Elettorali), sezione "L'elettore è..." con checkbox: Attivo (selezionato), Cancellati, Non iscritti, Sospesi. Sezione "Somo..." con checkbox: Residenti, Aire. Sezione "Seleziona da matricole precaricate" con campo Matricole. Pulsanti: Avanti, Indietro.]

### Passaggio 3 – Filtri di estrazione

Nella schermata successiva è possibile utilizzare molti filtri per eseguire un'estrazione precisa.

Nell'esempio è stata indicata una via per verificare quali sono gli elettori in tale indirizzo.

Cliccare su **Avanti** per proseguire.

[Schermata: Finestra "Stampa Parametrica" con numerosi campi di filtro: Regione di Nascita, Provincia o Comune, Dalla data di Nascita / Alla, Nominativo, Sesso, Cittadinanza, Titolo di studio, Professione, Sezione, Anno iscrizione, checkbox "solo elettori voto assistito" e "solo elettori con blocco sezione elettorale", Stato civile, campo "Via e num civ" (es. 15 - asiago, da 0 a 9999), Verbale nr., Verbale data da, Tipologia, Data Evento da. Pulsanti: Avanti, Indietro.]

### Passaggio 4 – Titolo e ordinamento

Nella schermata finale occorre indicare un **Titolo** e scegliere l'**ordinamento**.

Premere **Stampa** per generare l'estrazione richiesta.

[Schermata: Finestra "Stampa Parametrica" con campo "Titolo" (es. "Elettori in Via Asiago"), campo "Ordinamento" con dropdown che mostra le opzioni: Alfabetico, Sesso / Alfabetico, Sesso / Sezione / Numero Lista Sezionale, Sesso / Sezione / Alfabetico, Sesso / Lista generale, Fascicolo, Sesso / Data di nascita, Indirizzo. Pulsanti: Stampa, Indietro.]