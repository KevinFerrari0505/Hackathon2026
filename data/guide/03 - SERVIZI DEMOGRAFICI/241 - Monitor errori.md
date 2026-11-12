# Monitor errori

Questo programma serve a tenere sotto controllo eventuali errori che possono verificarsi durante la normale attività lavorativa. Può capitare che durante il lavoro alcune variazioni non passino in ANPR segnalando un errore; questo monitor ha la funzione di salvare questi errori per essere corretti e non rischiare di perdere alcuni aggiornamenti in ANPR.

## Apertura del programma

Aprendo il programma la maschera si presenta così:

[Schermata del Monitor errori: interfaccia principale con barra degli strumenti in alto, sezione "Errore Variazione" con campi di ricerca (data, causale), tabella centrale con colonne per Movimentazione, Gruppo, Num. rif., Data Ocorr., Data Inv. ANPR, Causale, Cognome Nome, Utente, ID Num., e pannello laterale destro "Note variazione" con pulsanti di azione (Correzione dati, da verificare, da chiudere, con Cityware, scarta, scartare, scarta, scartare, scartare, scartare, Variazione). In alto è evidenziato un tooltip che mostra "CAUSALE N. 1.1.37 - TIPOLOGIA: RETTIFICA GENERALITÀ SENZA CAMBIO SESSO".]

## Decodifica della causale di variazione

Posizionando il cursore sopra la causale di variazione viene decodificato il tipo di variazione.

## Visualizzazione della descrizione dell'errore

Cliccando due volte sulla riga in basso a destra comparirà la descrizione dell'errore.

[Schermata dettagliata: in alto la tabella "Errore Variazione" con i dati della variazione; in basso la tabella "ANPR - Monitor errori" con colonne ID, Tipo Var., Famiglia, Annulla, Metodo, Stato, Provvedimento, Data, CF, ID Numero, Comune ID, ANPR ID Oper, Cat. ID, Stato, Messaggio. Le righe evidenziate in rosso mostrano errori di tipo "Errore" con messaggio "ANPR: individuate due posizioni in A7 non unificate".]

## Correzione dell'errore

Tale errore deve essere corretto. Nell'esempio riportato, l'anomalia va corretta collegandosi alla **webapp** nella sezione **funzioni di servizio** e **risoluzione disallineamenti con l'A.E.**

## Chiusura dell'errore

Dopo aver corretto l'errore (verificando che la situazione in ANPR sia identica a quella locale in Cityware):

1. Si torna nel **Monitor errori**
2. Si seleziona il soggetto
3. Si preme **Risolto Manualmente**

[Schermata: pannello laterale destro con il pulsante "Risolto Manualmente" evidenziato in rosso, sotto la sezione "Note variazione".]