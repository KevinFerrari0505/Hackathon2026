# Consultazione notifiche ricevute da ANPR

Viene utilizzato per la consultazione delle notifiche ricevute da ANPR.

Cityware.online scarica ogni notte le notifiche ricevute da ANPR. Per consultarle indicate il periodo desiderato.

> **NB:** Precisiamo che la data di notifica non viene restituita da ANPR, quindi la "data di ricezione" è la data in cui cityware.online le ha scaricate (spesso, ma non sempre coincide con la data di notifica).

## Schermata di ricerca

La schermata si presenta con le date preimpostate di caricamento delle notifiche dell'ultima settimana.

[Schermata di ricerca notifiche ANPR con campi: Data di ricezione notifiche dal/a, Numero Notifica ANPR, Matricola, Solo notifiche non elaborate, Tipo Notifica (es. Mutazioni/Ripristini soggetti N010-N014-N015), e sezione "Ultimo allineamento effettuato" con elenco delle notifiche scaricate]

**Ultimo Allineamento effettuato** indica l'ultima volta che il Demone ha girato correttamente.

## Visualizzazione delle notifiche

Con **Elenca** vengono visualizzate le notifiche in base ai parametri indicati nella schermata di ricerca.

### Interpretazione dello stato

- Se lo stato della Notifica è **elaborato** senza nessun triangolo nella colonna verifica, vuol dire che è andato tutto a buon fine.

- Se invece lo stato della notifica è **elaborato** ma nella colonna verifica vi è un **triangolo giallo**, posizionandosi sopra (senza nessun click, solo semplicemente passando con il mouse sopra) appare un tooltip con la spiegazione dell'errore.

[Schermata elenco notifiche con colonna "Verif." che mostra triangoli gialli di avviso; tooltip esemplificativo: "CW: SOGGETTO AIRE ATTIVO / ANPR: NON COMPETENZA DEL MIO COMUNE MA NOVI DI MODENA (MO)"]

## Procedura di risoluzione errori

In questo caso, occorre operare come segue:

1. Selezionare la riga (che diventa gialla) e premere il tasto **cambia stato**.

2. Nella videata che compare, lasciare **da elaborare** e premere **conferma**.

[Finestra di dialogo "Scegli Cambio stato" con campo "Cambio stato" impostato su "0 - da elaborare", campo "Nota risoluzione" vuoto, e pulsanti "Conferma" e "Annulla"]

3. La riga quindi cambierà stato e diventerà **"da elaborare"**.

4. Effettuare lo stesso procedimento con le altre righe in cui sono evidenziati i triangoli. Quando tutte le righe sono da elaborare, alla notte verranno elaborate automaticamente.

## Notifiche mancanti

Se non ci fossero notifiche su Cwol da più di **5 giorni**, controllare la sezione notifiche sulla web app del Ministero dell'Interno. Se qui, invece, fossero presenti notifiche recenti di **MUTAZIONE DI RESIDENZA** o **AVVENUTO SUBENTRO DEL COMUNE** che su Cwol non vedete, è possibile mandare una email per richiedere assistenza.

> **Attenzione:** Tutte le segnalazioni riguardo a notifiche non visibili da meno di 5 giorni verranno ignorate.