# Come personalizzare il Formulario

Il Formulario di Stato Civile viene fornito già precaricato. Allineato al formulario del 2002, con le integrazioni del 2014 (divorzi brevi) e 2016 (unione civile).

Tutti i dati del formulario, che hanno il campo **ID minore di 1.000** sono precaricati, e ne viene impedita la modifica da parte del cliente. Questo allo scopo di accentrare eventuali futuri aggiornamenti.

Nulla vieta però che il cliente aggiunga formule di suo interesse. Queste verranno registrate con campo **ID maggiore di 1.000**, che indica la formula personalizzata. Non sono soggette a nessun controllo o aggiornamento.

Le formule possono utilizzare le variabili previste per il formulario.

## Indicazioni per la redazione del corpo della Formula

### Corpo della Formula: variabili per reperire dati da CWOL

Tra parentesi quadre, vengono indicate le variabili che riportano dati presenti in CWOL. Naturalmente si possono usare solo le variabili previste da CWOL, il cui elenco è disponibile nella documentazione "variabili previste per il formulario".

```
Madre: [PROGDETIND1.MATER_C] [PROGDETIND1.MATER_N] nata in [MATER_LUONAS] il
[MATER_DATANAS] cittadina [MATER_CITTAD] residente in [MATER_RESID] moglie del
dichiarante, cittadino [PATER_CITTAD]
```

> **NB:** a video quando si registra il testo dell'annotazione, o dell'atto, si vedrà questo stesso testo senza la formattazione di corsivo e grassetto, qui usata per spiegare meglio il concetto.

### Corpo della Formula: campi mancanti & commenti

Come standard nel caricare il corpo della formula utilizziamo `…` per indicare all'operatore che deve scrivere manualmente un dato, non presente in CWOL. Quando nel formulario sono presenti commenti atti ad aiutare l'operatore con indicazioni, li riportiamo tra doppia parentesi angolare `«»`. Ecco un esempio:

```
Mi ha dichiarato, inoltre, che il bambino è stato trovato il giorno … «indicare anche il mese e l'anno»
```

> **NB:** a video quando si registra il testo dell'annotazione, o dell'atto, si vedrà questo stesso testo senza la formattazione di corsivo e grassetto, qui usata per spiegare meglio il concetto.

### Corpo della Formula: domande per formula che prevede più casistiche

Quando nella formula il testo ministeriale prevede di riportare cose diverse a seconda delle condizioni che si verificano, usiamo le **graffe**.

Riportiamo qui un esempio dove il dichiarante può essere il Padre, oppure la Madre. La formula è unica, ma a seconda di chi sia il dichiarante, cambia il testo da indicare. Testo che può avere o meno delle variabili.

In questo esempio, generiamo una formula che quando utilizzata dall'operatore, genererà una domanda a video. Domanda che prevede 2 possibili risposte.

```
dopo avermi prodotto l'atto ... <<indicare i dati essenziali dell'atto
pubblico>> con cui
{1*dichiarante Padre* [PROGDETIND1.MATER_C] [PROGDETIND1.MATER_N]  madre del
neonato }
{1*dichiarante Madre* [PROGDETIND1.PATER_C] [PROGDETIND1.PATER_N] padre del
neonato  }
```

La sintassi prevede:

- `{` = apertura domanda
- `codice` = progressivo che identifica la domanda
- `*` = asterisco di separazione tra codice e titolo
- `titolo` = la domanda che apparirà all'operatore a video, quando usa la formula
- `*` = asterisco di separazione tra codice e titolo
- `corpo` = il testo da riportare quando tra le domande a video, viene scelta questa risposta. Il testo può includere variabili
- `}` = chiusura domanda

Il **codice** è importante in quanto a identici numeri (si usa numerazione progressiva) corrisponde una unica domanda a video. Nell'esempio siccome sono indicati due codici `1`, apparirà una unica form a video, con due possibili risposte, la prima intitolata *"dichiarante Padre"*, la seconda *"dichiarante Madre"*.

### Corpo della Formula: domande annidate

È possibile utilizzare la sintassi della domanda anche per fare casistiche complicate che ricorrono come da esempio:

```
dopo avermi prodotto l'atto ... <<indicare i dati essenziali dell'atto
pubblico>> con cui
{1*dichiarante Padre* [PROGDETIND1.MATER_C] [PROGDETIND1.MATER_N]  madre del
neonato
  {1.1*madre straniera* di cittadinanza [MATER_CITTAD] di cui mi presenta il
passaporto}
  {1.1*madre italiana* cittadina italiana}
}
{1*dichiarante Madre* [PROGDETIND1.PATER_C] [PROGDETIND1.PATER_N] padre del
neonato  }
```

L'esempio produce una prima videata con due domande: *dichiarante padre o madre?* Qualora venga scelto padre, propone una seconda videata con due domande: *madre straniera o italiana?* Se invece viene scelto dichiarante madre, non ci sono ulteriori videate.

## Caricamento di una formula

Per caricare una nuova formula andare nel menù **Servizi Demografici → Stato Civile → Tabelle → Definizione Formulario**.

Cliccando sulla freccia nera a fianco di ogni titolo/capo è possibile aprire la sezione sulla quale caricare una nuova formula. Selezionare una formula all'interno della sezione e poi premere **Nuovo**.

[Screenshot: interfaccia "Formulario Stato Civile" con struttura ad albero dei titoli/capi e pulsanti "Nuovo" e "Mostra Tutto" evidenziati in alto a destra]

Il primo dato da modificare sarà l'**ordinamento** della nuova formula all'interno del formulario.

Il campo **Id P** corrisponde alla sezione dove ci si è posizionati. Nel caso in esempio ci troviamo al *"CAPO I - TRASCRIZIONE DI ATTI (FATTA ECCEZIONE PER QUELLI DI CUI AI MODULI E, M, N E Q)"*. Se ci si è posizionati nel punto giusto non va modificato.

Il campo **Ordinamento formulario** serve per ordinare la nuova formula all'interno della sezione. È possibile utilizzare un numero o un altro carattere per un massimo di **40 caratteri**.

Modificare esclusivamente i dati dopo l'ultimo punto. Non è possibile utilizzare un numero già assegnato ad un'altra formula.

Nell'esempio verrà inserito `MORTE_ESTERO` dopo l'ultimo punto perché la formula è la trascrizione di un atto di morte ricevuto da Consolato.

[Screenshot: form "Inserimento Titolo" con campi ID (1000), Id P (48), Ordinamento Formulario (40.10.10.19308 evidenziato in rosso), Descrizione]

Compilare la **descrizione** della formula (max 255 caratteri) e spuntare la casella **Questa riga è una formula?**.

Ora dovrà essere compilata la parte relativa alla formula indicando:

- **numero formula** (max 15 caratteri)
- **corpo della formula** (max 4000 caratteri)
- **riservatezza formula sulle annotazioni** (solo per le annotazioni)
- **formula per redigere atto in bianco?** (solo per atti in bianco)

Il **corpo della formula** può essere scritto direttamente nel campo di testo presente su Cityware.online o copiato da un blocco note utilizzando le variabili previste per il formulario.

> ⚠️ **Sconsigliamo fortemente** di copiare un modello preparato su altri editor di testo come Microsoft Word o Libre Office.

Premere **Aggiungi** per salvare la formula.

[Screenshot: form completo "Inserimento Titolo" e "Inserimento Formula" con campi compilati: Ordinamento Formulario "40.10.10.MORTE_ESTERO", Descrizione "Trascrizione atto di morte da Consolato", "Questa riga è una formula?" spuntato, Numero Formula "MORTE_ESTERO", Corpo della formula con testo di esempio, Riservatezza formula sulle annotazioni "0 - Pubblica", "Formula per redigere atto in bianco?" spuntato, pulsante "Aggiungi" evidenziato]

Le formule aggiuntive/personalizzate possono essere caricate nelle sezioni specifiche o direttamente nella sezione **PERSONALIZZATE** in base alla preferenza.

Posizionarsi sulla sezione **PERSONALIZZATE**, cliccare su **Nuovo** e poi compilare i restanti campi come descritto in precedenza.

[Screenshot: interfaccia "Formulario Stato Civile" con sezione "PERSONALIZZATE" evidenziata in basso e pulsante "Nuovo" in alto a destra]