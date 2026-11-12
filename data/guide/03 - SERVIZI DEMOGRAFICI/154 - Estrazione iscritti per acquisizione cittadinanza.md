# Estrazione iscritti per acquisizione cittadinanza

Questo programma permette di effettuare l'estrazione degli "Aggiunti", richiesti dal distretto militare, per acquisizione della cittadinanza italiana.

## Percorso di navigazione

**Servizi Demografici ⇒ Leva Militare ⇒ Preparazione Lista di Leva ⇒ Estrazione Iscritti per Acquisizione Cittadinanza**

## Interfaccia del programma

Entrando all'interno, il programma si presenterà come sotto riportato:

[Screenshot: Schermata del modulo "Aggiorna lista di leva" con i campi "Anno di Acquisizione Cittadinanza" (campo vuoto) e "Causale di Iscrizione" (precompilato con codice 209 - Acquisto Cittadinanza Italiana)]

## Campi da compilare

I campi da compilare sono i seguenti:

1. Anno di competenza;
2. Causale;

### 1) Anno di competenza

Per quanto riguarda l'anno di competenza, **bisognerà inserire l'anno di acquisizione della cittadinanza italiana**.

> **ESEMPIO:** *"Il distretto militare mi richiede gli "Aggiunti" di tutti coloro che, nel 2024, hanno acquistato la cittadinanza italiana".*

Quindi nel campo "Anno di competenza" andrò ad inserire **"2024"**, che fa riferimento alla classe di leva **"2007"**.

Corrispondenza anno acquisizione → classe di leva:

| Anno di acquisizione | Classe di leva |
|---|---|
| 2024 | 2007 |
| 2025 | 2008 |
| 2026 | 2009 |
| ... | ... |

### 2) Causale

Riguardo la causale, di default troverete già impostato **codice 209 = Acquisto Cittadinanza Italiana**.

Nel caso questa causale non dovesse essere presente, potete seguire la wiki **"Tabella Casuali Leva Militare"** che vi spiegherà come aggiungerla.

## Conferma dell'estrazione

Una volta compilati i campi come sopra riportato, e sulla base delle informazioni richieste dal distretto, procedere con il tasto **"Conferma"**.

[Screenshot: Modulo compilato con Anno di Acquisizione Cittadinanza = 2024, Causale di Iscrizione = 209 Acquisto Cittadinanza Italiana, e pulsante "Conferma" evidenziato in rosso]

## Esito dell'operazione

Effettuata l'estrazione, l'operazione si concluderà con questo messaggio:

[Screenshot: Finestra di dialogo "Attenzione" con messaggio "Operazione conclusa con successo - Sono stati numerati 4 soggetti"]

Tutti i soggetti estratti verranno inseriti all'interno della tabella **Gestione Iscritti (Gestione ruoli matricolari)** con:

- **"Classe di Leva"** riferita all'anno di estrazione indicato in precedenza (2024 ⇒ 2007, 2023 ⇒ 2006, 2022 ⇒ 2005 ecc…)
- **Numerazione "1/A - 2/A - 3/A"** dove la **"A"** sta ad indicare **"Aggiunti"**
- **Causale di iscrizione "Acquisto Cittadinanza Italiana"**

[Screenshot: Tabella "Gestione Iscritti" con colonne Leva Militare, Cognome/Nome, Sesso, Data di nascita, Iscrizione (Acquisto Cittadinanza Italiana), Cancellazione, Classe di leva (2007)]

[Screenshot: Dettaglio del ruolo matricolare con Classe leva = 2007, Num. lista di leva = 0, Num. agg. lista di leva = 1/A, sezione Iscrizione con Causale 209 Acquisto Cittadinanza Italiana, Luogo immigrazione ALATRI (FR), Data immigrazione 08/07/2003, e sezione Cancellazione vuota]

## Passaggio successivo

Effettuata l'estrazione degli aggiunti, si procede con la creazione del **File TELELEVA** da dare al distretto militare ⇒ **Estrazione soggetti aggiunti per TELELEVA**