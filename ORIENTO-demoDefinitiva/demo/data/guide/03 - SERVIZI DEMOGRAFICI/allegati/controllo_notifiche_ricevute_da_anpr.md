# Controllo Notifiche Ricevute da ANPR

Per aggiornare automaticamente la propria base dati locale, necessaria per lo svolgimento dei propri compiti istituzionali diversi da quelli di natura propriamente anagrafica, vengono utilizzati i servizi che ANPR rende disponibili a questo scopo. In particolare, la WA integrata prevede un servizio di notifica che consente all'ente locale di effettuare l'integrazione e l'allineamento delle basi dati eventualmente conservate localmente.

- L'ANPR restituisce al Comune, mediante un servizio di notifica, i dati di ciascuna registrazione anagrafica effettuata tramite WA dal Comune stesso;
- Il Software locale del Comune, che dovrà disporre di un servizio di ricezione delle notifiche, elabora le notifiche trasmesse da ANPR e le utilizza per allineare le basi dati locali.

In **cityware_online** questo compito è lasciato a questo programma che va consultato giornalmente.

[Schermata: percorso menu Servizi Demografici > Anagrafe > ANPR - Funzioni di Servizio > Consultazione notifiche ricevute da ANPR]

Nella maschera il programma imposta automaticamente l'intervallo di date della ricezione ma è possibile anche variarle per ampliare la forbice. In tale schermata controllare anche che la data richiesta sia sempre il **giorno prima** rispetto al giorno attuale.

[Schermata: maschera "Consultazione Registro Notifiche" con campi: Data di ricezione notifiche dal / alla Data, Numero Notifica ANPR, Matricola CW, Solo notifiche non elaborate, Tipo Notifica (Mutazioni/Ripristini soggetti N010-N014-N015). In basso a destra il pulsante F4 - Elenca. In basso a sinistra la sezione "Ultimo allineamento effettuato" con log delle richieste.]

Premere poi **F4 = Elenca**.

Vengono elencate tutte le persone che hanno cambiato residenza trasferendosi in un altro comune (**N010 Mutazione residenza**) ed eventuali ripristini di immigrazioni (**N015 Ripristino, da registrazione immigrazione**).

- Nel caso in cui **stato notifica** sia **elaborato** vuol dire che è andato tutto a buon fine e che il soggetto è emigrato nel nuovo comune anche nell'applicativo locale cityware.
- Nel caso in cui sia segnalato l'errore ma poi per la stessa persona viene elaborata la notifica vuol dire che è andato tutto a buon fine.

[Schermata: tabella "Consultazione Registro Notifiche" con colonne: Id Notifica A, Dt. Decorrenza, Operazione, Persona, Stato Notif, Note, Comune Richiesta. Esempi di righe con stato "elaborato" e righe con errore "errore con d'Attenzione: il soggetto selezionato non può essere sc...".]

Se invece nella colonna **verif.** compare un **triangolo giallo** allora vuol dire che la variazione **non è passata in locale**.

[Schermata: tabella con colonna "Verif" evidenziata con triangoli gialli di attenzione su alcune righe.]

In questo caso se si ha l'autorizzazione si può provare a rieseguire la notifica altrimenti occorre chiamare l'assistenza.

## Rieseguire una notifica andata in errore

1. Selezionare la riga andata in errore e premere **CAMBIO STATO**.

[Schermata: riga selezionata con pulsante "CambioStato" evidenziato in alto a destra.]

2. La riga tornerà in stato **da elaborare**. A questo punto appuntarsi il **numero della notifica** e la **data Ricezione**.

[Schermata: riga con stato "da elaborar", Id Notifica "19065842" e Data Ricezione "19-02-2020" evidenziati.]

3. Aprire il programma:

   **Servizi Demografici > Anagrafe > ANPR - Funzioni di Servizio > Gestione richieste Notifiche ANPR asincrone**

[Schermata: percorso menu con "40. Gestione richieste Notifiche ANPR asincrone" evidenziato.]

4. Premere **Invia Nuova Richiesta**.

[Schermata: pulsante "Invia Nuova Richiesta" evidenziato nella schermata "Parametri Gestione".]

5. Nella videata che compare inserire la **data di ricezione** e il **numero della notifica** appuntati in precedenza e premere **Conferma**.

[Schermata: finestra "Invio Richiesta Notifiche ANPR: indicare i dati della richiesta" con campi: Richiesta Notifiche Dalla Data, alla Data, Numero Notifica ANPR, Tipo Notifica (Mutazioni/Ripristini soggetti N010-N014-N015). Pulsanti Conferma e Annulla.]

6. Attendere fino alla comparsa dell'esito **Positivo**. Chiudere il programma e verificare in cityware locale che la persona sia effettivamente emigrata.