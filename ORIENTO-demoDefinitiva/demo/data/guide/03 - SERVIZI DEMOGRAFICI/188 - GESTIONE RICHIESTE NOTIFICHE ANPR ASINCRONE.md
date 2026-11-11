# Gestione Richieste Notifiche ANPR Asincrone

Permette di gestire le richieste Notifiche ANPR.

[Schermata principale della Gestione Richieste Notifiche ANPR Asincrone: mostra un pannello informativo con messaggi di stato sulle richieste elaborate, un elenco di "Ultime elaborazioni effettuate" con dettagli su tipo richiesta e data, e sulla destra un pannello "Azioni Disponibili" con i pulsanti: Elabora Richieste in Sospeso, Invia Nuova Richiesta, Vedi Log]

## Funzioni disponibili

Le funzioni disponibili sono le seguenti:

### Elabora Richieste in Sospeso

Permette di elaborare le richieste in sospeso che si vedono sulla schermata alla voce *"Ci sono ancora da elaborare le seguenti richieste"*.

### Invia Nuova Richiesta

Permette di effettuare una nuova richiesta di notifiche. Cliccando comparirà la schermata di invio:

[Schermata "Invio Richiesta Notifiche ANPR: indicare i dati della richiesta" con i seguenti campi:
- **Richiesta Notifiche Dalla Data** (campo data, es. 08/07/2020)
- **alla Data** (campo data, es. 15/07/2020)
- **Numero Notifica ANPR** (campo numerico, es. 0)
- **Tipo Notifica** (menu a tendina, es. "Mutazioni/Ripristini soggetti N010-N014-N015")
- Pulsanti: **Conferma** e **Annulla**]

Per eseguire la richiesta di una sola notifica non scaricata, basta indicare:

- Il **numero di Notifica ANPR**
- La **data richiesta notifica** (Dalla Data corretta)
- Il **tipo Notifica**

e cliccare su **Conferma**.

Comparirà un Log in base all'esito della richiesta effettuata.

[Schermata "Elaborazione richieste in sospeso" con messaggio di esito: "ERRORE ANPR - La richiesta effettuata non produce alcun risultato"]

### Vedi Log

Permette di visualizzare il Log delle richieste.

[Schermata "Consultazione Richieste ANPR" con una griglia di record contenente colonne: ID, Tipo, Data, Ora, Data Notifica, Ora Data Notifica, Tipo Richiesta, Esito, Data Elaborazione, Ora Elaborazione, e altre. Sulla destra il pannello "Azioni Disponibili" con i pulsanti: Elabora Richieste in Sospeso, Invia Nuova Richiesta, Vedi Log, Cambia Stato Richiesta]

#### Pulsante Cambia Stato Richiesta

Il pulsante **Cambia Stato Richiesta**, scegliendo il record sulla griglia, permette di rieseguire l'elaborazione della Request.

[Schermata di conferma "Gestione Notifiche Anpr" con messaggio: "Sei sicuro di voler rielaborare la richiesta delle notifiche già eseguite? Premi cambia per confermare" e pulsanti: **cambia** / **Non Cambiare**]

Premendo **Cambia**, rimette la Request da elaborare per la prossima esecuzione di elaborazione Richieste in Sospeso.