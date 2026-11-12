# Estrazione da Anagrafe per Invio Messaggio tramite AppIO

> **PRIMA** di utilizzare questo servizio accertarsi di aver configurato in maniera corretta nel menù **Amministrazione del Sistema ⇒ App.Io ⇒ Gestione Servizi** tutti i parametri necessari al corretto funzionamento.

[Schermata: Configurazione Servizi di Notifica Digitali con campi UID Servizio, Nome Servizio, Dati Principali, Dati Avanzati, Agente Trasmissione, ID Servizio App.IO, Chiave primaria]

---

## Descrizione del programma

Attraverso questo programma è possibile estrarre dei nominativi selezionando specifici parametri.

È possibile estrarre i singoli cittadini oppure lo stato di famiglia dei cittadini selezionati al fine di inoltrare un messaggio attraverso l'AppIO come ad esempio:

- un avviso di inizio lavori in una via
- un'interruzione di servizio idrico per un intero quartiere
- comunicazioni ai genitori di bambini di un plesso scolastico
- ecc…

---

## Filtri predefiniti

All'apertura del programma sono già selezionati due filtri, ovvero **Residenti** e **Attivi**.

[Schermata: Sezione "Scegli il tipo di estrazione" con due opzioni radio: "Voglio estrarre i cittadini corrispondenti a questa selezione" e "Voglio estrarre lo stato di famiglia dei cittadini corrispondenti a questa selezione". Sotto, la sezione "Filtri disponibili per impostare la tua estrazione" con i filtri "Residenti" e "Attivi" già attivi nella colonna di destra "Verranno estratti i cittadini con queste caratteristiche"]

Tali filtri possono essere:

- **modificati**, con il doppio click
- **eliminati**, con l'icona del cestino
- **aggiunti**, selezionando il triangolo a sinistra della videata per aprire nuovi filtri

[Schermata: Pannello "Verranno estratti i cittadini con queste caratteristiche" con i filtri "Residenti" e "Attivi" ciascuno con icona cestino per l'eliminazione]

---

## Aggiunta di nuovi filtri

Facendo doppio click su un filtro da aggiungere (es. **Età**):

[Schermata: Albero "Filtri disponibili per impostare la tua estrazione" con struttura: Filtri Anagrafe → Residenti o Aire o Temporanei, Attivi o cancellati, Nascita (Data di Nascita, **Età** [evidenziato], Regione Nascita, Comune Nascita, Stato Nascita, Raggruppamento Stati (continente)), Indirizzo, Matricole precaricate, Sesso]

Si aprirà una finestra che permetterà di inserire la selezione richiesta.

[Schermata: Finestra "Scelta dati per Estrazione Anagrafe in Excel: indicare i dati della richiesta" con campo "Scegli Età", campi "Inserisci Età da estrarre" con valori da 18 a 21, e pulsanti "Conferma" e "Annulla"]

Nello stesso modo può essere fatto per tutti gli altri filtri.

---

## Calcolo dei soggetti estratti

Una volta effettuata la selezione di tutti i filtri, premendo il tasto **Quanti sono?** verrà fatto il calcolo dei soggetti che saranno estratti.

[Schermata: Pulsante "Quanti sono?" evidenziato a destra, con popup "Estrazione da Anagrafe in Excel" che mostra "La selezione corrisponde a 194 cittadini"]

---

## Preparazione del messaggio per AppIO

Nell'ultima videata, premendo infine il tasto **"Prepara messaggio per AppIO"** viene aperta una maschera con i cod. fiscali dei soggetti selezionati e la generazione del messaggio che si vuole inoltrare.

[Schermata: Maschera di composizione messaggio con elenco di codici fiscali in alto, campi "Oggetto" e "Contenuto" con editor di testo formattato, e pulsanti di invio sulla destra]