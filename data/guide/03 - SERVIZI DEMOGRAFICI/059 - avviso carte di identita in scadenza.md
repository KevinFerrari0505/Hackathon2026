# Avviso Carte di Identità in scadenza tramite AppIO

Questo programma consente di estrarre l'elenco dei cittadini con carte in scadenza esportando i dati in Excel e/o inviare notifiche tramite l'App IO o stampare le relative comunicazioni in docx.

**Punto menù:** Servizi Demografici → Anagrafe → Stampe → Avviso Carte di Identità in Scadenza tramite app IO

## Parametri di configurazione

All'apertura della form, il programma chiede l'impostazione di alcuni dati, di seguito le spiegazioni:

- **Scadenza dal…al:** è il periodo di scadenza da indicare, delle carte da analizzare

- **Flag:**
  - `'cartacee'` o `'CIE'`: selezionare almeno uno dei due tipi di carte, in modo da vedere poi l'elenco
  - `'elenco cittadini'`: abilita l'esportazione in Excel che estrae i cittadini con carte in scadenza nel periodo indicato

- **Testo per stampa lettera avviso:** scegliere il modello di documento per stampare la comunicazione in docx, una volta scelto il testo il programma recupera i cittadini selezionati e crea delle lettere per la stampa massiva

- **Invio avviso tramite App IO:** attiva l'invio delle notifiche digitali, se il servizio App IO è configurato nel sistema, i cittadini che hanno l'app IO installata riceveranno il messaggio (il riconoscimento avviene per Codice Fiscale)
  - **Oggetto per invio app IO** → titolo del messaggio da inviare
  - **Messaggio per invio app IO** → testo della comunicazione (obbligatorio se si invia via App IO)

- **Flag Reinoltro avviso app.io:** se attivo, include cittadini già avvisati (è consigliato apporre il flag solo per i solleciti)

> **Nota:** Qualora un cittadino abbia già ricevuto l'avviso di scadenza tramite app IO dal nostro Comune, non lo riceverà di nuovo anche se la scadenza rientra nel periodo indicato ora a video. Spuntare REINOLTRO se si desidera forzare l'invio anche ai già avvisati della scadenza.

## Procedura operativa

Una volta impostati i dati cliccare il bottone **'Elabora'**.

[Schermata della form "Elenco Carte identità in scadenza": mostra i campi Scadenza dal/al con date, i checkbox Cartacee/CIE/Elenco cittadini (excel), il campo Testo per stampa lettera avviso, la sezione Invio avviso tramite app.IO con Oggetto e Messaggio per invio app.IO (editor di testo con formattazione), il checkbox Reinoltro avviso app.io, e i pulsanti laterali Elabora, Parametri ricerca, Carica, Salva, Reset]