# ELENCHI PREPARATORI

Attraverso questo programma è possibile effettuare la stampa degli elenchi di coloro che devono essere iscritti nella leva militare e coloro che, invece, **NON** devono essere iscritti.

## Percorso di accesso

**Servizi demografici ⇒ Leva militare ⇒ Preparazione lista di leva ⇒ Elenchi preparatori**

[Schermata del menu di navigazione: dal menu principale si seleziona "150. Servizi Demografici" → "40. Leva Militare" → "10. Preparazione Lista di leva" → "40. Elenchi preparatori"]

## Videata di configurazione

Aprendo il programma, si presenterà una videata con i seguenti campi:

[Schermata del form "Elenchi leva" con i campi: Anno di competenza, Causale di iscrizione / Codice testo, Causale di cancellazione / Codice testo, Ordine, e pulsante Stampa]

## Campi da valorizzare

I campi che devono essere valorizzati sono:

- **Anno di competenza**;

- **Codice testo** (il testo da utilizzare è il seguente ⇒ `cwd_LevaElencoPreparatorio`);

  > **N.B.** Se si vuole effettuare un unico elenco per tutti gli attivi, o per tutti coloro che hanno una causale di cancellazione, basterà indicare solamente il testo (senza l'indicazione delle causali)……..mentre se si vogliono effettuare più elenchi bisognerà indicare, oltre al codice testo, anche le varie causali (per capire di quali causali ho bisogno posso andare a consultare la tabella **"Gestione Iscritti"** dove sono presenti tutti i soggetti estratti con le varie causali.

- **Ordine** ⇒ permette di ordinare la stampa per **causale**, **cognome e nome** o **data di nascita**.

[Schermata del menu a tendina "Ordine" con le opzioni: Cognome e nome, Data di nascita, Causale/Cognome e nome]

## Esempio di compilazione

[Schermata del form compilato con esempio:
- **Causale di iscrizione** → Codice testo: `cwd_LevaElencoPrep` → LEVA ELENCO PREPARATORIO → *Per avere un elenco di soli attivi*
- **Causale di cancellazione** → Codice testo: `cwd_LevaElencoPrep` → LEVA ELENCO PREPARATORIO → *Per avere un elenco di solo coloro che NON dovranno essere iscritti*
- **Ordine**: Cognome e nome]

## Risultato della stampa

Dopo aver valorizzato i campi e premuto il pulsante **Stampa**, il sistema genera un documento Word contenente l'elenco preparatorio della lista di leva.

[Schermata dell'anteprima del documento generato: "COMUNE DI POTENZA PICENA – ELENCO PREPARATORIO LISTA DI LEVA – CLASSE DI LEVA 2008" con tabella contenente le colonne: N.° Prog., Cognome Nome, Data Nascita, Cognome Nascita, Note/Note]