# Novità Agid

## Sigillo elettronico qualificato

Il sigillo elettronico è una firma automatica del server apposta sul file `Segnatura.xml`, generato dal programma per i protocolli in partenza via posta elettronica.

Il sigillo garantisce l'origine e quindi l'autenticità e l'integrità dei documenti inviati.

Il sigillo elettronico qualificato è un sigillo rilasciato da un prestatore di servizi fiduciari qualificato.

## Nuovi metadati di conservazione: il tipo soggetto (per segnatura di protocollo e conservazione)

Per ogni soggetto mittente/destinatario è possibile indicare, facoltativamente, se si tratta di:

- Persona fisica
- Persona giuridica
- Pubblica Amministrazione Italiana
- Pubblica Amministrazione Estera

[Schermata: campo "Tipo soggetto" nel form di inserimento destinatario e mittente, con menu a tendina che mostra le opzioni: Indefinito, Persona fisica, Persona giuridica, Pubblica Amministrazione Italiana, Pubblica Amministrazione estera]

Nel caso in cui si tratti di una Pubblica Amministrazione Italiana, va indicato anche il **Codice IPA**.

[Schermata: form con campo "Tipo soggetto" impostato su "Pubblica Amministrazione Italiana" e campo "Cod. IPA" evidenziato]

Se il soggetto mittente/destinatario viene scelto dalla **Ricerca IPA**, verrà riconosciuto come Pubblica Amministrazione Italiana e il Codice IPA sarà inserito automaticamente.

[Schermata: esempio di mittente "COMUNE DI ANCONA" con Tipo soggetto "Pubblica Amministrazione Italiana" e Cod. IPA "c_a271" popolato automaticamente]

Nell'**anagrafica dei soggetti mittenti/destinatari**, si può specificare il tipo soggetto.

[Schermata: form "Archivio Soggetti/Mittenti/Destinatari" con campo "Tipo soggetto" evidenziato e menu a tendina aperto]

Il dato **Tipo Soggetto** viene riportato all'interno della `Segnatura.xml`. Se ci sono più destinatari, vengono riportate solo le Pubbliche Amministrazioni Italiane. Tutti gli altri soggetti sono omessi per evitare che, in caso di gara, siano visibili i nomi degli altri destinatari.

## Nuovi metadati di conservazione: modalità di formazione del documento informatico (solo per conservazione)

Nella tabella degli **Allegati** è possibile specificare, facoltativamente, la modalità con cui è stato creato il documento principale protocollato.

Le opzioni disponibili sono:

a) da editor;
b) scansione;
c) da portali;
d) da raggruppamento di dati di origine eterogenea.

[Schermata: tabella Allegati con menu a tendina "Seleziona Modalità di formazione" che mostra le opzioni dettagliate:
- a) creazione tramite utilizzo di strumenti software (strumenti di office automation personali)
- b) acquisizione di un documento informatico per via telematica o su supporto informatico (scansione o mail/PEC)
- c) memorizzazione su supporto informatico in formato digitale delle informazioni risultanti da transazioni (transazioni da portali esterni)
- d) generazione o raggruppamento anche in via automatica di un insieme di dati o registrazioni, provenienti da una o più banche dati, anche appartenenti a più soggetti interoperanti]

L'informazione, se presente, viene riportata nei dati di conservazione, ma **non** nella `Segnatura.xml`.

## Tempi di conservazione

Si possono impostare i tempi di conservazione per ciascun **fascicolo**.

[Schermata: form "Gestione Fascicolo" con campo "Tempo di Conservazione" evidenziato, contenente un campo numerico e una checkbox "Perenne"]

Si può decidere di indicare più genericamente dei tempi di conservazione a livello di **titolario**, quindi tutti i documenti all'interno di uno stesso titolo e classe, erediteranno i tempi di conservazione direttamente dalla classificazione.

[Schermata: struttura ad albero del titolario con colonna "Tempo Cons." e form "Gestione Categorie" con campo "Tempo di Conservazione" evidenziato]

Più genericamente ancora, si possono impostare le tempistiche nei **parametri generali**.

[Schermata: tab "Conservazione" nei parametri generali con campo "Tempo di Conservazione Predefinito" e menu a tendina che mostra le opzioni: Indefinito, 5 Anni, 10 Anni, 15 Anni, 20 Anni, 25 Anni, 30 Anni, 35 Anni, 40 Anni, 45 Anni, 50 Anni, Perenne]

L'informazione dei tempi di conservazione viene cercata **a scalare**, dal fascicolo, al titolario, ai dati generali.

## Nuovi metadati di conservazione per il fascicolo informatico

In fase di creazione di un nuovo fascicolo, ne andrà specificata la **tipologia**:

- **per affare**: comprende documenti di un affare specifico, di durata circoscritta (es. costruzione di un edificio, organizzazione di un evento culturale, un bando di selezione del personale), da chiudere alla conclusione dell'affare;

- **per attività**: comprende i documenti prodotti nello svolgimento di un'attività amministrativa semplice, non discrezionale e ripetitiva, che si esaurisce in risposte obbligate o meri adempimenti (es. richieste di permessi di accesso alla ztl, elenco dei nati). Ha durata annuale;

- **per persona fisica**: comprende tutti i documenti, anche con classifiche diverse, che si riferiscono a una persona fisica (es. i fascicoli personali dei dipendenti). Questi fascicoli rimangono aperti finché è in corso il rapporto tra l'ente e la persona;

- **per persona giuridica**: comprende tutti i documenti, anche con classifiche diverse, che si riferiscono a una persona giuridica (es. i fascicoli dei fornitori). Questi fascicoli rimangono aperti finché è in corso il rapporto tra l'ente e il soggetto;

- **per procedimento amministrativo**: comprende una pluralità di documenti che rappresentano azioni amministrative omogenee e destinate a concludersi con un provvedimento amministrativo.

[Schermata: form di creazione fascicolo con campo "Tipologia Fascicolo" e menu a tendina che mostra le opzioni: Affare, Attività, Persona Fisica, Persona Giuridica, Procedimento Amministrativo]