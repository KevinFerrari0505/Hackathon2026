# Notifiche Anpr

Vengono visualizzate le notifiche di **Mutazioni/Ripristino soggetti N010-N014-N015** degli ultimi 7 giorni scaricate.

## Stato normale: apertura notifiche senza anomalie

Questo è il normale caso di apertura delle notifiche senza anomalie riscontrate a livello di scarico notturno.

[Schermata: finestra "Notifiche ricevute Anpr" con indicatore "Stato del Demone **In esecuzione**" (icona verde), data ultima iterazione demone, pulsante "Aggiorna Stato" e tabella "Consultazione Registro Notifiche" con colonne: Id operaz., A. Dl. Decis., Operazione, Persona, Stato Notif., Note, Comune Richiesta, Verif., Id Anpr, Matricola, Dl. Ricezione. Esempi di righe: N010 Mutazione residi, N010 Mutazione residi, N012 variante grado parentela, N010 Mutazione residi. Stato Notif: "elaborato" o "da elaborare".]

## Anomalie di esecuzione o di controllo

Nel caso in cui non ci sono notifiche scaricate, segnala eventuali anomalie di esecuzione o di controllo.

### Demone fermo (errore)

In questo caso per esempio il **Demone si è fermato e non è attivo**, quindi occorre contattare assistenza.

[Schermata: finestra "Notifiche ricevute Anpr" con indicatore "Stato del Demone **Fermo in errore - contattare assistenza**" (icona rossa), messaggio di errore in rosso: "Demone non attivo oppure in crash o in errore - contattare l'assistenza per verificare il problema", data ultima iterazione demone, pulsante "Aggiorna Stato" e tabella "Consultazione Registro Notifiche" vuota (nessuna riga).]

### Demone in warning

In questo caso significa che il **demone è in warning**, ma **non è una anomalia**: significa che è stato eseguito più di 10 minuti fa. Solo nel caso di fermo significa che ci sono problemi.

[Schermata: finestra "Notifiche ricevute Anpr" con indicatore "Stato del Demone **In esecuzione**" (icona gialla/warning), data ultima iterazione demone, pulsante "Aggiorna Stato" e tabella "Consultazione Registro Notifiche" con righe di notifiche elaborate/da elaborare.]