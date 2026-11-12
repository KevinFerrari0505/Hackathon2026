# Estrazione da Anagrafe per Invio Messaggio tramite AppIO

Attraverso questo programma è possibile estrarre dei nominativi selezionando specifici parametri.

È possibile estrarre i singoli cittadini oppure lo stato di famiglia dei cittadini selezionati al fine di inoltrare un messaggio nell'AppIO, es. la scadenza della carta di identità, avviso di inizio lavori in una via, ecc.

## Selezione del tipo di estrazione

[Schermata: finestra "Estrazione da anagrafe in excel" con due opzioni radio: "Voglio estrarre i cittadini corrispondenti a questa selezione" e "Voglio estrarre lo stato di famiglia dei cittadini corrispondenti a questa selezione". A destra, pannello "Verranno estratti i cittadini con queste caratteristiche" con i filtri "Residenti" e "Attivi" già selezionati.]

All'apertura del programma sono già selezionati due filtri, ovvero **Residenti** e **Attivi**.

## Gestione dei filtri

Tali filtri possono essere modificati, eliminati o anche aggiunti degli altri selezionando il triangolo per aprire i filtri.

[Schermata: pannello "Filtri disponibili per impostare la tua estrazione" con la sezione "Filtri Anagrafe" espansa, che mostra le opzioni: Residenti o Aire o Temporanei, Attivi o cancellati, Nascita, Indirizzo, Matricole precaricate, Sesso.]

### Aggiunta di un filtro

Facendo doppio click su un filtro da voler aggiungere, es. **Età**:

[Schermata: sezione "Filtri Anagrafe" con sotto-sezione "Nascita" espansa, che mostra: Data di Nascita, Età (evidenziato in giallo), Regione Nascita, Comune Nascita, Stato Nascita, Raggruppamento Stati (continente), Indirizzo.]

Si aprirà una finestra che permetterà di inserire la selezione richiesta.

[Schermata: finestra "Scelta dati per Estrazione Anagrafe in Excel: indicare i dati della richiesta" con titolo "Scegli Età" e campi "Inserisci Età da estrarre" con valori da **18** a **21**, e pulsanti "Conferma" e "Annulla".]

Nello stesso modo può essere fatto per tutti gli altri filtri.

## Calcolo dei soggetti estratti

Una volta effettuata la selezione di tutti i filtri, premendo il tasto **Quanti sono?** verrà fatto il calcolo dei soggetti che saranno estratti.

[Schermata: finestra "Estrazione da Anagrafe in Excel" con messaggio "La selezione corrisponde a 194 cittadini" e pulsante "Quanti sono?" evidenziato a destra.]

## Configurazione dell'output

Proseguendo con l'**Avanti**, nell'output è già selezionato il campo dell'indirizzo ma possono essere anche aggiunti gli altri campi che si vedono nella finestra.

[Schermata: finestra "Output per impostare campi della tua estrazione" con tabella contenente le colonne "Sel." e "Tipo informazione". Campi disponibili: frazione, indirizzo (selezionato con spunta), operazione (evidenziato in giallo), famiglia, codici. In basso: "Visualizzati 1 - 5 di 5".]

## Titolo di stampa e ordinamento

Nell'ultima videata viene riportata una parte del titolo di stampa che può essere modificato e si può scegliere l'ordinamento preferito per l'output.

[Schermata: campo "Titolo della stampa*" con valore "COMUNE DI" e sottotitolo "- Elenco Cittadini Residenti Attivi Et? da 18 a 21". Sotto, sezione "Scegli uno dei seguenti tipi di ordinamento" con opzioni radio: Alfabetico (selezionato), Alfabetico per sesso, Indirizzo e famiglia, Sesso e data di nascita, Cittadinanza, alfabetico.]

## Preparazione del messaggio per AppIO

Premendo infine il tasto **"Prepara messaggio per AppIO"** viene aperta una maschera con i cod. fiscali dei soggetti selezionati e la generazione del messaggio che si vuole inoltrare, es. (scadenza carta di identità, ecc.).

[Schermata: finestra con elenco di codici fiscali dei soggetti estratti (in formato testo giallo su sfondo chiaro) e, a destra, pannello con pulsanti "Invia Messaggio", "Torna Indietro", "Quanti sono?" e "Prepara messaggio per AppIO". In basso, form di composizione messaggio con campi: Servizio, Stato, Oggetto, Contenuto (con barra di formattazione testo) e Allegato.]