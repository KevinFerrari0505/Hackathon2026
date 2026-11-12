# Archiviazione delle PEC scartate

Può capitare che giungano al protocollo alcune e-mail/PEC che non devono essere protocollate (Spam ecc.), è possibile procedere tramite apposita funzione, allo scarto dalla lista delle e-mail/PEC da protocollare. Questi elementi però, seppur scartati e non visibili all'interno della lista di protocollazione, occupano uno spazio fisico all'interno del sistema. Tramite la funzione di archiviazione delle PEC scartate, è possibile archiviare in maniera massiva, tutte le e-mail/PEC scartate dal protocollo, così da liberare spazio.

Per utilizzare questa funzionalità occorre operare come segue con un utente abilitato alle funzioni di **Amministrazione del sistema**.

## Definizione del percorso di archiviazione

Il primo step è quello di definire un percorso all'interno del server, nel quale archiviare le e-mail/PEC:

1. Cliccare il bottone raffigurante l'omino, posto in alto a destra nella schermata:

   [Screenshot: barra strumenti in alto a destra con icone, il bottone "omino" (profilo utente) è evidenziato con un riquadro rosso]

2. Selezionare dalla schermata che si apre, il bottone **"Gestione Parametri"**;

3. Dalla schermata che si apre, digitare all'interno del campo filtro, la dicitura **"PARAMETRI ARCHIVIAZIONE MAIL"** e digitare invio da tastiera;

4. Accedere con doppio clic alla voce descritta al punto precedente;

5. Si apre la maschera dedicata all'inserimento del percorso di archiviazione delle PEC, dove è possibile appunto indicare un path valido all'interno del server:

   [Screenshot: finestra "Configurazione Parametri - ARCHIVIAZIONEMAIL" con campo "PATH PER COPIA MAIL" contenente il valore "tmp/" e pulsante "F5-Conferma"]

   Il percorso nell'esempio è puramente indicativo.

6. Cliccare il bottone **"Conferma"** per salvare il percorso di archiviazione.

## Avvio dell'archiviazione delle PEC scartate

1. Accedere alla funzione **Amministrazione del sistema / Webmail / Archiviazione mail**;

2. Si apre la schermata di ricerca dei dati:

   [Screenshot: finestra "Lista archivio mail" con campi: Account (menu a tendina), Classe (menu a tendina con opzione "Scartate del protocollo"), Da Data, A Data, Path copia (campo di testo con valore "tmp/"), e pulsanti "F4 - Elenca" e "F2 - Seconda Ricerca"]

   - Nel primo campo **"Account"**, è possibile selezionare l'account per il quale si vuole procedere all'archiviazione delle PEC scartate;
   - Nel campo **"Classe"** è possibile specificare se si intende estrarre le PEC scartate dal protocollo, quelle scartate dal SUAP o entrambe;
   - Impostare un **range di date** entro il quale eseguire l'estrazione;
   - Cliccare il bottone **"Elenca"** per estrarre i dati;

3. Si apre la lista degli elementi estratti:

   [Screenshot: tabella "Lista archivio mail" con colonne: Certificazione, Oggetto, Data e Ora, Data Invio, Ora Invio, Giorni, Mittente, Mittente Posta Mail, Destinatario, Account, Classe. Sono visibili circa 22 righe di elementi estratti. Pulsanti a destra: "F3 - Altra Ricerca", "Simula archiviazione", "Archivia mail"]

   - E' possibile tornare alla ricerca tramite il bottone **"Altra Ricerca"**;

   - Tramite il bottone **"Simula Archiviazione"**, viene visualizzato un calcolo di spazio che verrebbe liberato archiviando le PEC estratte:

     [Screenshot: finestra "Check Mail Scartate" con messaggio informativo: "Totale Mail: 1308" e "Totale dimensioni occupate mail scartate: 32,27 MB"]

   - Tramite il bottone **"Archivia mail"** si procede alla vera e propria archiviazione all'interno del percorso indicato.

## Risultato dell'archiviazione

Tutti gli elementi archiviati, vengono inseriti all'interno di un **archivio .zip**, corredate da un **file Excel** che indica per ogni elemento i suoi dati principali, così da rendere agevole la ricerca in caso di necessità futura.

Completata l'archiviazione, queste PEC non saranno più presenti all'interno del sistema, liberando spazio, e saranno consultabili all'interno del percorso di archiviazione impostato.