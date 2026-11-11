# Guida operativa alla Gestione degli adempimenti elettorali con ANPR

Tutti i comuni dal 30 novembre 2023, prorogato poi al 31 dicembre 2023 sono subentrati con i dati elettorali in ANPR e questo ha comportato l'adeguamento dei nostri programmi alla comunicazione di tali dati verso la piattaforma ministeriale.

L'adeguamento è continuo in quanto siamo ancora in una fase di transizione e adattamento come avete potuto notare dalle GIT aperte da vari soggetti e attori (comuni, software house e SOGEI).

Questa guida ha l'obiettivo di accompagnarvi nella gestione degli adempimenti spiegandovi l'utilizzo delle nuove funzionalità introdotte.

---

## Introduzione e informazioni utili

La comunicazione con ANPR è assicurata da funzionalità interne ai programmi esistenti e da altri aggiunti di recente; infatti, la chiusura delle revisioni vi permette l'invio degli elettori, immediato o differito che sia, verso ANPR, la Gestione Invii consente varie azioni sugli elettori nonché le variazioni di certificabilità.

Tuttavia, prima di addentrarci nella guida è bene dare qualche informazione:

- L'azione di mutazione dei dati elettorali da Web App è tendenzialmente istantanea e permette di cancellare, iscrivere o mutare i dati elettorali.
- L'invio degli elettori differito o istantaneo può richiedere dalle 4 alle 6 ore per essere correttamente gestito da ANPR.
- La chiusura della revisione in errore, caso raro, non comporta la perdita di dati come vedremo successivamente.

---

## La conferma revisione e l'invio dati verso ANPR

Al termine delle procedure di revisione, previo controllo che vedremo dopo, i dati vengono comunicati ad ANPR e potete sempre scegliere il tipo di invio attraverso il flag mostrato nella videata sottostante:

- **Tipo Invio Anpr Immediato** ☑️ — Il FLAG permette l'invio immediato dei dati che verranno elaborati da ANPR, si consiglia di utilizzarlo qualora le variazioni da comunicare, iscrizioni, cancellazioni e cambi sezione, non siano troppe. In caso contrario potreste trovarvi nella situazione di dovere attendere il termine degli invii per utilizzare il programma.

- **Tipo Invio Anpr Differito** ☐ — L'assenza del FLAG comporta l'invio differito che avviene in seguito attraverso una schedulazione notturna; questo è consigliato quando avete numerose variazioni da comunicare o qualora non vogliate attendere la fine dell'elaborazione per riprendere le mansioni della giornata.

La videata nella quale potete fare questa scelta è quella di **conferma revisione** presente al termine di ogni revisione:

[Schermata: videata di Conferma Revisione Semestrale con menu laterale "Programma Elettorale" e campo "Tipo Invio Anpr Immediato" con checkbox selezionata]

> **NB:** Nel caso la revisione andasse in errore al momento della chiusura o prima di questa, viene sempre creato un backup con iscrivendi/cancellandi/cambi sezione, che può essere ripreso per la generazione dei file da inviare al ministero.

---

## La Gestione dell'invio dati ad ANPR: la Gestione Invii

Il programma che permette di agire sugli invii degli elettori è **Gestione Invii** raggiungibile attraverso il percorso:

- `150 – 20 – 60 – 10`
- `Servizi Demografici ---> Elettorale ---> ANPR – Funzioni di Servizio ---> Gestione Invii`

[Schermata: percorso di navigazione menu con Servizi Demografici > Elettorale > ANPR - Funzioni di Servizio > Gestione Invii]

All'apertura del programma vi troverete una videata con i dati degli invii, relativi alle varie revisioni e una serie di bottoni sulla destra, quelli che interessano a voi sono:

### Inserisci Elettore

Permette di inserire come invio un elettore pescando i dati dall'elettorale, questa funzione è utilizzabile qualora per l'elettore non sia già stato creato un invio.

[Schermata: videata Gestione invii ad ANPR con tabella e pulsanti a destra: Inserisci Elettore, Inserisci Sezioni, Modifica e Reinoltro]

Cliccato il bottone di **Invio singolo elettore** si apre una videata di interrogazione elettorale che permette di ricercare l'elettore e selezionarlo con un doppio click e vi verrà ridata una videata gialla di conferma inserimento, o se già presente una rossa di errore.

[Schermata: videata Interrogazione Elettorale con campi: Sezione Elettorale, Cognome, Nome, Sesso, Data di nascita, Num. Lista Elettorale, Tipo Lista, Matricola, e filtri Iscritti/Cancellati/Non iscritti]

### Inserisci Sezioni

Come per l'inserimento dell'elettore singolo questo bottone permette di inserire le sezioni: nello specifico, qualora vi troverete nella situazione di risuddividere il territorio e creare nuove sezioni, queste vanno inviate assieme agli elettori quindi:

1. Confermate la revisione creando i dati elettorali in differito (togliere il flag)
2. Nella gestione invii create la sezione
3. Selezionate la sezione con un doppio click e la inserite

[Schermata: videata Gestione invii ad ANPR con tabella Sezioni Elettorali contenente colonne: Cod, Descrizione Breve, Descrizione Sezione Estesa, Sede Elettorale, Elettori, e pulsanti Inserisci, Elimina, Aggiungi, Annulla]

### Modifica e Reinoltro

Questo pulsante permette il reinvio del dato su ANPR, per utilizzarlo selezionate il singolo record (sezione o elettore) e poi premendo questo pulsante lo modificate con la dicitura **"Modifica e Reinoltrato – Modificati dati e Reinoltrato"**.

Inoltre, l'aggiornamento del dato non va fatto in modo indiscriminato in quanto ulteriori invii di dati già presenti mandano l'invio in errore, il che non vuol dire che l'elettore non sia passato ma che ANPR non accetta un secondo invio.

---

## Controlli pre-conferma: Il controllo dei soggetti in revisione

Prima della conferma della revisione è bene, al fine di creare correttamente tutti i file, eseguire questo controllo che vi permette di sapere se ci sono errori possibili e presenti sui soggetti in revisione.

Il programma è nello stesso gruppo di gestione Invii con la voce: **Controllo soggetti in Revisione ANPR**.

Il controllo produce un file Excel, dopo aver elaborato tutti gli elettori in revisione, mostrandovi per i vostri **ISCRIVENDI** e **CANCELLANDI**, il motivo di cancellazione ANPR dal vostro comune o da altro, di quest'ultimo viene indicato il nome.

Di conseguenza c'è corrispondenza tra causali di iscrizione elettorale e causali di cancellazione per ANPR, questo perché vi permette di conoscere qualora un elettore sia iscrivibile e il file di invio accettabile da parte di ANPR.

Esempio di output del file Excel:

| PROGSOGG | NOMINATIVO | ANPR_ID | CAUSALE_RI | COMUNE_CANCELLAZIONE | DATA_CANC | MOTIVO_CANCELLAZIONE |
|----------|------------|---------|------------|----------------------|-----------|----------------------|
| | | | 12 - Cambi di sezione | | | |
| | | | 12 - Cambi di sezione | | | |
| | | | 4 - Acquisto cittadinanza italiana | | | |
| | | | 12 - Cambi di sezione | | | |
| | | | 12 - Cambi di sezione | | | |
| | | | 2 - Immigraz. MODENA (MO) | | | Trasferimento residenza |
| | | | 4 - Acquisto cittadinanza italiana | | | |

I dati delle prime colonne sono stati cancellati ma li troverete sempre, sono la matricola interna, nome e cognome e l'id_anpr dei cittadini in revisione.

### Casi da ricordare per controllare ed usare il file:

- Se il motivo cancellazione e il comune non sono presenti spesso è perché il soggetto non è ancora cancellato, dovete assicurarvi che venga fatto.

- Il caso dell'Immigrazione da estero quando è riconducibile ad un movimento da un AIRE ad un'altra va gestito con la causale **2 – Immigrazione da altro comune**.

- Nel caso mancasse l'ID_ANPR questo va associato alla matricola da apposita funzione che trovate al percorso sotto indicato e per la quale è presente l'omonima guida sulle guide rapide.

  Percorso: `Servizi Demografici > Elettorale > ANPR - Funzioni di Servizio > Corrispondenza ID ANPR e Cityware`

  [Schermata: percorso menu con Corrispondenza ID ANPR e Cityware evidenziato]

  Riferimento guida rapida: https://wiki.nuvolaitalsoft.it/doku.php?id=guide:demografici:corrispondenza_id_anpr_e_cityware

---

## Capire se la variazione è passata in ANPR

Per capire se la variazione è passata in ANPR possiamo eseguire un doppio controllo:

### Controllo 1: Stato in Gestione Invii

Nella gestione invii, controllando i soggetti, troverete questo stato in **Tipo Operazione**, significa che l'invio è andato a buon fine.

[Schermata: Tabella Invii ad ANPR con colonne Data Invio, Matricola, Nominativo, Data nascita, Sezione, Tipo Invio, Tipo Operazione. Il Tipo Operazione mostra "Reinoltro - Reinoltrato Movimento ANPR" in verde]

### Controllo 2: Stato ERRORE

Lo Stato **ERRORE**, permette una volta posizionatosi sopra col mouse di vedere la risposta di ANPR all'invio e quindi provvedere alle correzioni del caso e reinoltrare nuovamente la variazione:

[Schermata: Tabella Invii ad ANPR con record in stato ERRORE e tooltip che mostra "ERR: 1-ANPR.ENG04-ANPR - OPERAZIONE NON EFFETTUABILE, COMUNE NON COMPETENTE"]

> **NB:** non si reinoltra l'errore di non competenza del comune inviante.

### Situazioni particolari per le cancellazioni

Tenete conto che per le cancellazioni potreste trovarvi queste situazioni:

#### ELETTORE CANCELLATO MA NON ANCORA ISCRITTO IN ALTRO COMUNE

I dati elettorali sono visibili e anche il motivo cancellazione.

[Schermata: Dati Elettorale con campi: Certificabilità: Soggetto con certificabilità completa; Cancellato per Motivo: Trasferimento residenza; Su ANPR risulta elettore: SI; Lista Generale - del Comune di...; sezione n., Indirizzo: SCUOLE ELEMENTARI...; Referendum nazionali: SI; Elezione dei membri del Parlamento spettanti all'Italia: SI; Senato della Repubblica: SI; Camera dei Deputati: SI; Regionali: SI; Comunali: SI; Circoscrizionali: NO]

#### ELETTORE CANCELLATO E ATTUALMENTE ISCRITTO IN ALTRO COMUNE

Non troverete il motivo cancellazione ma direttamente i dati del comune iscrivente.

[Schermata: Dati Elettorale con campi: Certificabilità: Soggetto con certificabilità completa; Su ANPR risulta elettore: SI; Lista Generale - del Comune di...; sezione n., Indirizzo: CENTRO SPORTIVO...; Referendum nazionali: SI; Elezione dei membri del Parlamento spettanti all'Italia: SI; Senato della Repubblica: SI; Camera dei Deputati: SI; Regionali: SI; Comunali: SI; Circoscrizionali: SI]