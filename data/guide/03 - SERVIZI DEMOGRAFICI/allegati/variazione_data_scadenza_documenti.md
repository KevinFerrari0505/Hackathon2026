# VARIAZIONE DATA SCADENZA DOCUMENTI

Questo programma permette convertire una data fissa impostata in un'altra.

Quindi: viene fatta una ricerca nei dati per i documenti che hanno la data di scadenza impostata, una volta trovati sostituisce la data di scadenza calcolandola come la data di emissione del documento sommata al periodo che imposteremo noi a video (10 anni, 7 mesi, 5 giorni ecc.)

Ma vediamolo nello specifico.

## Accesso al programma

Seguire il percorso indicato per effettuare l'accesso o in alternativa digitare il nome del programma nella barra di ricerca applicazioni.

[Schermata: percorso di accesso al programma tramite menu a cascata: Gestione Documenti → 10. Gestione Documentale → 20. Archivio → 90. Gestione temporanei → 60. Variazione data scadenza documenti. Il percorso completo è: Gestione Documentale > Gestione Documentale > Archivio > Gestione temporanei > Variazione data scadenza documenti]

## Utilizzo del programma

Come da immagine procedere compilando la sezione di sinistra per poi eseguire il programma:

[Schermata: interfaccia del programma "Variazione data documenti" con i campi: Tipo documento (con campo PERIODO), Scadenza, Periodo. A destra il pulsante "ESEGUI" con indicazione "SELEZIONARE IL TIPO DOCUMENTO, DALLA LISTA CHE PROPONE" e "SELEZIONARE SUCCESSO PER PROCEDERE ALLE MODIFICHE". Note esplicative: LA DATA DI SCADENZA CHE VIENE USATA COME FILTRO PER SELEZIONARE DAI DATI TUTTI I DOCUMENTI CHE PER UN TIPO DEFINITO HANNO QUELLA DATA DI SCADENZA. PERIODO: INSIEME DI TEMPO CHE VIENE AGGIUNTO ALLA DATA DI EMISSIONE QUINDI PERIODO = DATA DI EMISSIONE PER I DOCUMENTI CHE SARANNO SELEZIONATI. VIENE ESPRESSO IN GIORNI, MESI, ANNI E NEL PRIMO CAMPO SI IMMETTE IL VALORE NUMERICO, COME ES. 20, 50 (ANNO/GIORNO/MESI)]

Intanto vediamo l'esempio eseguito su un ambiente di test con dati fittizi:

Scelgo il tipo documento, vedo la data di scadenza, che per esempio era impostata nel 1811 ed è come se dicessi al programma che: "Per ogni documento con questa data di scadenza, prendi la data di rilascio e somma il periodo che ti ho indicato, in questo caso 200 anni"

> **Attenzione:** i dati che uso non sono reali quindi i risultati possono essere dissimili da quelli che avrete voi nell'utilizzo.

[Schermata: esempio di compilazione con Tipo documento: 6 - Permesso di Soggiorno, Scadenza: 11/11/1811, Periodo: 200 anni]

Una volta lanciato il programma vi troverete il messaggio che chiede la conferma della modifica:

[Schermata: finestra di dialogo "Attenzione" con messaggio: "Sono stati trovati 113 documenti. La nuova data di scadenza verrà calcolata come la data di rilascio + 200 anni. Si desidera confermare l'operazione?" con pulsanti FS-Conferma e FS-Annulla]

Mi dice che ha trovato 113 documenti con la data di scadenza da me impostata, indica il calcolo che viene fatto in base ai dati da me immessi e procedo con la conferma dell'operazione.

Vedrete una fase di elaborazione che ha durata in base alla mole di dati che andrete a modificare e di seguito un messaggio di avvenuta modifica:

[Schermata: finestra di dialogo "Attenzione" con messaggio: "Operazione conclusa con successo. Sono stati aggiornati con successo 113 documenti"]

L'aggiornamento interessa i dati dei documenti che sono visualizzati nei programmi di CWOL - cityware online, quindi aggiornando i documenti e poi interrogando i soggetti vedrete i dati nuovi.