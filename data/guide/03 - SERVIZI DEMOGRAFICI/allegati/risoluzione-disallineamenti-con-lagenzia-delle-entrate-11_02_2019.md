# APPENDICE - VALIDAZIONE DEL CODICE FISCALE E DEI DATI ANAGRAFICI E RISOLUZIONE DEI DISALLINEAMENTI CON L'AGENZIA DELLE ENTRATE

## 1. PREMESSA

Con il subentro, le persone sono inserite in ANPR sulla base dei dati trasmessi da ciascun comune; i dati sono trasmessi all'Agenzia delle Entrate (AE nel seguito del documento) che li verifica rispetto all'Anagrafe Tributaria (AT nel seguito del documento), restituendo gli esiti di tale verifica.

Gli esiti della verifica vengono utilizzati per aggiornare in ANPR lo stato di validazione del codice fiscale, così come riepilogato nella tabella che segue:

| Anomalia | Descrizione | Stato del codice fiscale in ANPR (cfr Tabella 22) | Note |
|----------|-------------|--------------------------------------------------|------|
| — | Soggetto validato (cf e dati anagrafici del comune perfettamente coincidenti con quelli AT) | VALIDATO | Dati anagrafici validati (soggetto presente in A.T. con CF e dati anagrafici uguali a quelli indicati dal Comune) |
| EA001 | Codice fiscale di lunghezza errata | NON VALIDATO | Posizione inesistente (soggetto NON presente in A.T.) |
| EA002 | Soggetto presente in AT con dati anagrafici uguali a quelli del comune ma CF del comune assente | VALIDATO | Dati anagrafici validati (soggetto presente in A.T. con dati anagrafici uguali a quelli indicati dal Comune ma CF diverso). Anpr registra il codice fiscale restituito dall'Agenzia delle Entrate; il comune deve aggiornare le proprie basi dati |
| EA003 | Soggetto presente in AT con dati anagrafici uguali a quelli del comune ma CF diverso | VALIDATO | Dati anagrafici validati (soggetto presente in A.T. con dati anagrafici uguali a quelli indicati dal Comune ma CF diverso). Anpr registra il codice fiscale restituito dall'Agenzia delle Entrate; il comune deve aggiornare le proprie basi dati |
| EA029 | Codice fiscale calcolato dai dati anagrafici del comune non presente in AT | NON VALIDATO | Posizione inesistente (soggetto NON presente in A.T.) |
| EA036 | Soggetto registrato più volte sia con il CF base che con quello che risolve l'omocodia | NON VALIDATO | Posizione con più omocodici collegati (soggetto presente in A.T., ma non individuato con il codice fiscale omocodice) |
| EA038 | Soggetto con data di nascita non coincidente con quella presente nel CF | NON VALIDATO | Posizione inesistente (soggetto NON presente in A.T.) |
| EA040 | Soggetto registrato più volte sia con il CF collegato che con l'ultimo | NON VALIDATO | Posizione con codice fiscale collegato (più recente) (soggetto presente in A.T., individuato con il codice fiscale collegato) |
| EA042 | Soggetto con sesso non coincidente con quello presente nel CF | NON VALIDATO | Posizione inesistente (soggetto NON presente in A.T.) |
| EA048 | Codice fiscale formalmente errato | NON VALIDATO | Posizione inesistente (soggetto NON presente in A.T.) |
| EAA30 | Soggetto presente in AT con dati anagrafici diversi | NON VALIDATO | Dati anagrafici diversi (soggetto presente in A.T. con dati anagrafici diversi da quelli indicati dal Comune; la differenza non produce un diverso codice fiscale) |
| EAA31 | Soggetto presente in AT con dati anagrafici diversi | NON VALIDATO | Dati anagrafici diversi (soggetto presente in A.T. con dati anagrafici diversi da quelli indicati dal Comune; la differenza non produce un diverso codice fiscale) |
| EAA40 | Soggetto presente in AT con altri codici fiscali più recenti | NON VALIDATO | Posizione con codice fiscale collegato (più recente) (soggetto presente in A.T., individuato con il codice fiscale collegato) |
| EAA41 | Soggetto presente in AT con altri codici fiscali più recenti | NON VALIDATO | Posizione con codice fiscale collegato (più recente) (soggetto presente in A.T., individuato con il codice fiscale collegato) |
| EAA50 | Codice fiscale base di omocodice | NON VALIDATO | Posizione con più omocodici collegati (soggetto presente in A.T., ma non individuato con il codice fiscale omocodice) |
| EAA51 | Codice fiscale base di omocodice | NON VALIDATO | Posizione con più omocodici collegati (soggetto presente in A.T., ma non individuato con il codice fiscale omocodice) |

Esclusi i soggetti validati, tutti gli altri sono inseriti in appositi elenchi che il comune può scaricare dalla Web Application successivamente al subentro.

Occorre prestare particolare attenzione alle persone con stato del codice fiscale = validato e segnalate con le anomalie **EA002** e **EA003**: si tratta, infatti, schede individuali che ANPR aggiorna sulla base di quanto restituito da AE. Il comune, partendo dall'elenco che li contiene (**Soggetti con cf diverso, dati anagrafici diversi, collegato, omocodice, cf errato**), deve aggiornare la propria base dati locale.

I soggetti con codice fiscale validato sono marcati da AE come "soggetti ANPR" e questo blocca qualsiasi aggiornamento effettuato dagli uffici della stessa Agenzia.

Per tutte le altre persone, il comune utilizzando le funzionalità di ANPR, provvederà a rimuovere l'errore che determina il disallineamento, in modo che AE marchi anche questi soggetti come "soggetti ANPR" ed elabori correttamente le notifiche che li riguardano: le notifiche, infatti, sono acquisite da AE soltanto per le posizioni marcate ANPR.

Successivamente al subentro, durante le normali operazioni di registrazione che effettua il comune, possono essere segnalati errori restituiti da AE che non consentono la prosecuzione degli operazioni; in casi del tutto eccezionali (ad esempio sussistono condizioni di particolare urgenza che non consentono di rinviare l'operazione dopo aver chiarito le cause del disallineamento), è possibile completare comunque la registrazione anche in assenza della validazione da parte dell'Agenzia dell'Entrate (valore 3 nel campo gestioneCF per chi utilizza i WS, Iscrizione/modifica senza validazione CF per chi utilizza la WA).

Tale opzione, al momento, non è permessa quando il soggetto è già marcato da AE come "soggetto ANPR".

Il soggetto, al termine dell'operazione, risulterà non validato in ANPR (anomalia EN141).

Per quanto sopra esposto in merito alle notifiche, anche tali anomalie vanno risolte tempestivamente.

I disallineamenti "da subentro" o quelli che si creano successivamente con i servizi di registrazione possono essere risolti dal comune con due modalità:

- mutazione dei dati generali;
- funzione di "Risoluzione disallineamenti con Agenzia Entrate" disponibile nella sezione Utilità e Notifiche della WA.

Le due modalità sono in alternativa tra loro: si può utilizzare la prima quando il soggetto è sprovvisto di codice fiscale; in tutti gli altri casi è obbligatorio utilizzare la seconda.

Per risolvere un disallineamento, è necessaria una istruttoria preventiva per individuare:

- quali dati conosce AE per un iscritto con codice fiscale non validato, utilizzando gli strumenti resi disponibili dalla stessa Agenzia o dalla funzione di Consultazione AE presente tra le funzioni di consultazione del sito Web ANPR
- l'effettiva validità dei dati anagrafici del comune rispetto a quelli noti in AE.

Si ricorda infine che nell'ipotesi in cui la soluzione del disallineamento comporti l'attribuzione di un nuovo codice fiscale, è necessario avvertire il cittadino.

Nei paragrafi che seguono, sono descritti:

- modalità da adottare per tipologia di disallineamento;
- strumenti da utilizzare durante l'istruttoria preventiva;
- modalità operative di funzionamento della "Risoluzione disallineamenti con Agenzia Entrate" della WA.

Nell'ultimo paragrafo, infine, sono indicati alcuni esempi di soluzioni da adottare quando effettuando un'operazione di registrazione si ottiene un errore bloccante.

## 2. MODALITÀ DA ADOTTARE PER TIPOLOGIA DI DISALLINEAMENTO

### 2.1 SOGGETTI NON VALIDATI AL SUBENTRO

#### 2.1.1 PERSONE CON DATI ANAGRAFICI DIVERSI

Si tratta di persone presenti sia in ANPR che in AT, ma registrate con dati anagrafici differenti, senza che questa differenza dia origine a un diverso codice fiscale.

Di seguito le anomalie segnalate:

| Anomalia | Descrizione | Stato del codice fiscale in ANPR (cfr Tabella 22) |
|----------|-------------|--------------------------------------------------|
| EAA30 | Soggetto presente in AT con dati anagrafici diversi | 3 - Dati anagrafici diversi (soggetto presente in A.T. con dati anagrafici diversi da quelli indicati dal Comune; la differenza non produce un diverso codice fiscale) |
| EAA31 | Soggetto presente in AT con dati anagrafici diversi | 3 - Dati anagrafici diversi (soggetto presente in A.T. con dati anagrafici diversi da quelli indicati dal Comune; la differenza non produce un diverso codice fiscale) |

Le persone interessate sono presenti nell'elenco delle anomalie "Soggetti con cf diverso, **dati anagrafici diversi**, collegato, omocodice, cf errato", che indica che i dati in possesso di AE sono diversi da quelli del comune; questa differenza non dà origine ad un diverso codice fiscale (ad esempio: Cognome del comune = **Rossi**; Cognome AE = **Rassi**).

Occorre in tal caso utilizzare la funzionalità di "Risoluzione disallineamenti con Agenzia Entrate" confermando i dati di AE oppure quelli di ANPR in funzione dell'esito dell'attività di verifica volta ad individuare quali siano i dati anagrafici corretti.

#### 2.1.2 PERSONE REGISTRATE IN ANPR CON CODICE FISCALE COLLEGATO

Si tratta di persone che possiedono più di un codice fiscale; tra questi, quello indicato dal comune non è l'ultimo attribuito da AE.

Di seguito le anomalie segnalate:

| Anomalia | Descrizione | Stato del codice fiscale in ANPR (cfr Tabella 22) |
|----------|-------------|--------------------------------------------------|
| EAA40 | Soggetto presente in AT con altri codici fiscali più recenti | 4 - Posizione con codice fiscale collegato (più recente) (soggetto presente in A.T., individuato con il codice fiscale collegato) |
| EAA41 | Soggetto presente in AT con altri codici fiscali più recenti | 4 - Posizione con codice fiscale collegato (più recente) (soggetto presente in A.T., individuato con il codice fiscale collegato) |

Le persone interessate sono presenti nell'elenco delle anomalie "**Soggetti con cf diverso, dati anagrafici diversi, collegato**, omocodice, cf errato".

Anche in questo caso è necessario effettuare delle indagini preventive utilizzando gli strumenti di interrogazione resi disponibili da ANPR o da Agenzia Entrate.

In base alle risultanze di tali indagini, tramite la funzione di risoluzione anomalie è possibile confermare i dati dell'Agenzia delle Entrate o di ANPR.

Da notare che, se il soggetto è presente in ANPR con il suo codice fiscale collegato e si confermano i dati di ANPR, si effettua quella che tecnicamente AE definisca come "inversione di link" ossia il CF collegato diventa il principale e viceversa.

Confermando invece i dati di AE sarà aggiornato ANPR la scheda individuale, registrando i dati anagrafici modificati ed il corrispondente codice fiscale.

L'operazione che viene effettuata in automatico è una mutazione dei dati generali interrogabile dal comune per l'aggiornamento delle basi dati locali.

#### 2.1.3 OMOCODICI

Si tratta di persone diverse con gli stessi dati anagrafici.

Di seguito le anomalie segnalate:

| Anomalia | Descrizione | Stato del codice fiscale in ANPR (cfr Tabella 22) |
|----------|-------------|--------------------------------------------------|
| EAA50 | Codice fiscale base di omocodice | 5 - Posizione con più omocodici collegati (soggetto presente in A.T., ma non individuato con il codice fiscale omocodice) |
| EAA51 | Codice fiscale base di omocodice | 5 - Posizione con più omocodici collegati (soggetto presente in A.T., ma non individuato con il codice fiscale omocodice) |

Le anomalie EAA50 e EAA51 indicano che il comune utilizza il codice fiscale "base" di omocodice, cioè quello attribuito per primo da AT.

Le persone interessate sono presenti nell'elenco delle anomalie "**Soggetti con cf diverso, dati anagrafici diversi, collegato, omocodice**, cf errato".

Per entrambe le anomalie, il comune deve verificare se tra tutti i soggetti con gli stessi dati anagrafici individua il proprio cittadino; a tal fine occorre utilizzare Siatel – Punto Fisco (cfr paragrafo 3.1).

Una volta individuato il codice fiscale corretto il comune dovrà utilizzare la funzione di risoluzione anomalie confermando i dati presenti in Agenzia delle Entrate.

Non sarà infatti possibile rettificare i dati di Agenzia Entrate con un codice fiscale base di omocodice.

Se nessun codice fiscale registrato in AT corrisponde a quanto risulta al comune, occorre effettuare una mutazione di dati generali confermando che si tratta di una omocodia (gestione CF = 2 per chi utilizza i WS; ....per chi utilizza la WA)

#### 2.1.4 PERSONE NON PRESENTI IN AT

Si tratta di persone che non risultano in AT (ricalcolando il codice fiscale dai dati anagrafici).

Di seguito le anomalie segnalate:

| Anomalia | Descrizione | Stato del codice fiscale in ANPR (cfr Tabella 22) |
|----------|-------------|--------------------------------------------------|
| EA001 | Codice fiscale di lunghezza errata | 9 - Posizione inesistente (soggetto NON presente in A.T.) |
| EA029 | Codice fiscale calcolato dai dati anagrafici del comune non presente in AT | 9 - Posizione inesistente (soggetto NON presente in A.T.) |
| EA038 | Soggetto con data di nascita non coincidente con quella presente nel CF | 9 - Posizione inesistente (soggetto NON presente in A.T.) |
| EA042 | Soggetto con sesso non coincidente con quello presente nel CF | 9 - Posizione inesistente (soggetto NON presente in A.T.) |

Le persone interessate sono presenti negli elenchi delle anomalie:

- "Soggetti con codici fiscali formalmente errati o incongruenti con i dati anagrafici" (EA001, EA038, EA042);
- "Soggetti non presenti in agenzia delle entrate" (EA029).

Tali anomalie indicano che i dati anagrafici del comune non sono conosciuti in AT; è questo il caso, ad esempio, di una persona registrata in AE come ROSSI ALBERTO che il comune ha conferito in ANPR come ROSSI ALBERTO MARIA oppure di una persona realmente sprovvista di codice fiscale (iscritto AIRE ad esempio), registrata in ANPR con un codice fiscale calcolato dal sw anagrafico del comune.

A parte quanto segnalato direttamente con le anomalie (EA001, EA038, EA042), è necessario effettuare un'istruttoria per capire il motivo della mancata validazione, a valle della quale:

- se la persona fosse realmente priva di codice fiscale, occorre chiedere l'attribuzione con una mutazione, specificando il valore 1 nel campo gestioneCF;
- se si tratta di una differenza sui dati anagrafici che determina un codice fiscale diverso, con la funzionalità di "Risoluzione disallineamenti con Agenzia Entrate", indicando entrambi i codici fiscali (quello del comune e quello di AE) e, sulla pagina che si ottiene in risposta, confermando i dati di AE oppure quelli di ANPR.

### 2.2 POSIZIONI NON ALLINEATE A SEGUITO DI OPERAZIONI DI REGISTRAZIONE

È il caso di una persona iscritta in ANPR senza richiedere la validazione del codice fiscale (gestioneCF = 3).

Occorre utilizzare le funzioni di Risoluzione disallineamenti con Agenzia Entrate.

Nel caso si confermino i dati ANPR è possibile che AE attribuisca un nuovo codice fiscale, il precedente risulterà collegato al nuovo. L'operazione che viene effettuata in automatico è una mutazione dei dati generali interrogabile dal comune per l'aggiornamento delle basi dati locali.

## 3. STRUMENTI DISPONIBILI

### 3.1 SIATEL-PUNTO FISCO

Il sistema, reso disponibile da AE, consente di ricercare un soggetto in AT secondo vari criteri di ricerca:

- Codice fiscale
- Dati anagrafici completi
- Cognome, Casella senza cognome, Nome, Casella senza nome, Sesso, Data di Nascita, Casella senza giorno, Casella senza giorno e mese
- Cognome, Casella senza cognome, Nome, Casella senza nome, —, Data di Nascita, Casella senza giorno, Casella senza giorno e mese
- Cognome, Casella senza cognome, Nome, Casella senza nome, Sesso, —, Intervallo Anni
- Cognome, Casella senza cognome, Nome, Casella senza nome, Sesso, —, Comune e Prov. di Nascita
- Cognome, Casella senza cognome, Nome, Casella senza nome, —, —, Comune e Prov. di Nascita
- Cognome, Casella senza cognome, —, Casella senza nome, Sesso, Data di Nascita, Casella senza giorno, Casella senza giorno e mese, Comune e Prov. di Nascita
- —, Nome, Casella senza nome, Sesso, Data di Nascita, Casella senza giorno, Casella senza giorno e mese, Comune e Prov. di Nascita

Occorre effettuare le ricerche sfruttando i diversi criteri disponibili per verificare "al di là di ogni ragionevole dubbio" che la persona sia effettivamente sprovvista di codice fiscale, per evitare di creare posizioni riferite allo stesso soggetto, registrato più volte negli archivi AT con dati anagrafici diversi.

### 3.2 CONSULTAZIONE DEI DATI AE DALLA WA

È possibile verificare la posizione di un cittadino in Agenzia Entrate utilizzando la funzionalità "Consultazione AE" presente nella sezione "consultazione ed estrazione" del sito web di ANPR.

La ricerca può essere effettuata esclusivamente per codice fiscale: alla conferma sono visualizzati i dati anagrafici e l'indirizzo del cittadino così come risultano in Agenzia Entrate. La consultazione evidenzia nel campo "esito" se il soggetto è transitato o meno in ANPR.

Vengono altresì riportati eventuali codici fiscali collegati: il codice fiscale visualizzato nella sezione "Generalità" è sempre l'ultimo codice fiscale attribuito da AE al cittadino, quelli collegati sono evidenziati nella sezione "codici fiscali collegati". Se la richiesta di consultazione è avvenuta tramite un collegato viene evidenziato nel campo "esito".

Se la consultazione AE restituisce il messaggio di errore "Non sono stati trovati soggetti corrispondenti ai criteri di ricerca" occorre utilizzare le funzioni di ricerca che la stessa Agenzia rende disponibili ai comuni nel sistema Siatel PuntoFisco.

## 4. MODALITÀ OPERATIVE DI FUNZIONAMENTO DI "RISOLUZIONE DISALLINEAMENTI CON AGENZIA ENTRATE"

La funzionalità è disponibile nell'area Utilità e Notifiche della WA.

La persona da allineare deve essere registrata in ANPR con un codice fiscale.

Laddove il codice fiscale non sia presente l'utente dovrà richiederne l'attribuzione/validazione con l'operazione di Mutazione tutti i dati del Servizio di Registrazione.

Selezionando la funzione in esame, si ottiene in risposta la pagina seguente:

[Schermata: pagina "Risoluzione disallineamenti con Agenzia Entrate" con criteri di ricerca per Codice fiscale, Codice fiscale AE (con check "coincidenti"), Cognome (con check "Senza cognome"), Nome (con check "Senza nome"), Sesso, Data di nascita (con opzioni Completa/Solo mese e anno/Solo anno), Provincia di nascita, Stato estero, Comune di nascita, e pulsanti CERCA e RIPULISCI]

La ricerca può essere effettuata su ANPR anche per dati anagrafici, oltre che per codice fiscale.

Nella pagina che si ottiene in risposta, sono riportati i dati ANPR e quelli dell'Agenzia delle Entrate, con evidenza delle eventuali differenze.

[Schermata: tabella "Dati aggiornabili" con colonne DATI AGENZIA ENTRATE e DATI ANPR, campi: Codice fiscale, Cognome, Senza cognome, Nome, Senza nome, Sesso, Data di nascita (con evidenza in giallo della differenza), Provincia di nascita, Comune di nascita, Stato estero di nascita, Luogo di nascita eccezionale, e pulsanti CONFERMA AE e CONFERMA ANPR]

In presenza di differenze tra ANPR e AE, è possibile:

- confermare i dati anagrafici presenti in ANPR; in tal caso i dati dell'Agenzia delle Entrate saranno rettificati sulla base di quanto presente in ANPR;
- confermare i dati anagrafici presenti nel sistema dell'Agenzia delle Entrate: in tal caso i dati di ANPR saranno modificati per allineamento con quelli dell'Agenzia delle Entrate.

Occorre precisare che anche nel caso di conferma dati di Agenzia delle Entrate fa comunque fede l'indirizzo presente in ANPR che va ad aggiornare quello di AE.

È possibile che nel caso siano confermati i dati di ANPR, il codice fiscale venga riassegnato in base alle nuove informazioni. In tal caso il nuovo codice fiscale viene restituito ad ANPR ed aggiornato sia sull'archivio di ANPR che su quello di Agenzia Entrate.

È prevista la realizzazione di una nuova notifica da utilizzare per recepire nella propria base dati le nuove generalità (compreso il nuovo codice fiscale).

Il buon esito dell'operazione renderà validato il soggetto che non sarà più modificabile dall'Agenzia delle Entrate.

[Schermata: messaggio verde "Mutazione dei dati del soggetto eseguita correttamente. Nuovo codice fiscale attribuito BCCCML75S58F839O" e messaggio giallo "Codice fiscale presente in AT come collegato"]

Nel caso in cui i dati del comune, registrati in ANPR coincidano con quelli dell'Agenzia delle Entrate, sarà presente solo il pulsante "Allineamento dati AE".

Cliccando su tale pulsante il sistema richiederà una conferma della richiesta in corso come riportato nella figura seguente:

[Schermata: finestra di dialogo "Attenzione" con testo "Conferma AE: I dati di ANPR verranno sostituiti con quelli presenti in AE. Sei sicuro di voler continuare?" e pulsanti SI e Annulla]

Alla conferma, il sistema invia un messaggio che segnala l'avvenuto allineamento del codice fiscale:

[Schermata: messaggio verde "Esito AE: Codice fiscale allineato (Codice 00)"]

### 4.1 COLLEGAMENTO CODICI FISCALI

È possibile con la stessa funzione di Risoluzione disallineamenti con Agenzia Entrate collegare due codici fiscali appartenenti alla stessa persona ma non collegati tra di loro.

Per effettuare questa operazione è necessario indicare nella pagina di ricerca i due CF: sul primo quello presente in ANPR (selezionando il check includi validati)

[Schermata: pagina di ricerca con campo "Codice fiscale" compilato (es. BCCGRG94M50F158B), check "Includi validati" selezionato, campo "Codice fiscale AE" compilato (es. BCCGRG94M50F158U), check "coincidenti" deselezionato]

Sul secondo campo l'altro CF da collegare presente solo sul sistema di Agenzia Entrate (deselezionando il check coincidenti)

[Schermata: elenco soggetti ricerca con un risultato: CODICE FISCALE BCCGRG94M50F158B, COGNOME BUCCERI, NOME GIORGIA, SESSO F, DATA NASCITA 10/09/94, LUOGO DI NASCITA MESSINA (ME)]

Si seleziona il soggetto della lista che verrà mostrato nella pagina successiva con l'evidenza delle differenze tra i due sistemi.

[Schermata: pagina "Dati aggiornabili" con colonne DATI AGENZIA ENTRATE e DATI ANPR, differenze evidenziate in arancione (Nome: GIOVANNA vs GIORGIA), campo "Collega Codici Fiscali" e pulsante CONFERMA]

Si seleziona il check **Collega Codici Fiscali** e si seleziona il tasto **CONFERMA**.

Questa operazione collega i due codici fiscali e aggiorna il soggetto presente in ANPR con il codice fiscale e i dati anagrafici presenti in AE.

### 4.2 AGGIORNAMENTO CODICE FISCALE DEFINITIVO

Un soggetto con codice fiscale provvisorio per risoluzione omocodia, al quale è stato assegnato il definitivo, può essere aggiornato in ANPR utilizzando il servizio 5008 – mutazione tutti i dati, tipo mutazione 1 o tramite l'utilizzo dell'applicazione Web.

In quest'ultimo caso è necessario utilizzare la funzione di **Mutazione tutti i dati** presente sotto la voce: **Registrazioni**.

Si ricerca il soggetto, si seleziona dalla lista tramite la lente, si seleziona come dato di controllo **Dati anagrafici/codice fiscale** lasciando non selezionata la lista gestione Codice Fiscale.

[Schermata: sezione "Dati di controllo" con checkbox "Dati anagrafici / Codice fiscale" selezionata e altre opzioni non selezionate; sezione "Gestione Codice fiscale" con campo vuoto; pulsanti CONFERMA, RIPULISCI, ANNULLA OPERAZIONE]

Nella pagina successiva si seleziona la sezione delle **Generalità** (nella lista sulla sinistra) e si sostituisce il codice fiscale presente con quello definitivo comunicato (tramite notifica, contatto diretto o email).

Si confermano i dati della pagina delle generalità, si seleziona l'ultima sezione **Completa l'operazione** e si preme il tasto **salva e chiudi**.

## 5. COME EVITARE I DISALLINEAMENTI

Di seguito alcune indicazioni per la soluzione di casi specifici segnalati dai comuni subentrati.

### 5.1 ERRORE BLOCCANTE IN ISCRIZIONE

La persona è già censita in AT con dati diversi da quelli del comune (caso frequente per gli stranieri – cognome e nome invertiti tra comune e AT).

Premesso che occorre in ogni caso una verifica per controllare quali siano i dati corretti (quelli di iscrizione o quelli dell'Agenzia), assumendo che quelli validi siano quelli di iscrizione, ci sono due modi per procedere:

- si effettua l'iscrizione con i dati dell'Agenzia senza specificare nulla nel campo gestioneCf e successivamente si esegue una mutazione con i dati corretti; con il primo passaggio AE marca il soggetto ANPR e con il secondo rettifica i propri dati (con eventuale attribuzione di un nuovo CF);
- si effettua l'iscrizione con gestioneCF = 3 e successivamente con la funzione di Risoluzione dei disallineamenti della WA (area Utilità e notifiche) si confermano i dati del comune.

### 5.2 POSIZIONI DUPLICATE

Effettuando una mutazione dei dati anagrafici, AE restituisce l'errore **AEM9C**: individuate due posizioni non collegate in AT. Questo errore indica che il codice fiscale presente in ANPR prima della mutazione e quello che si otterrebbe a mutazione avvenuta esistono entrambi in AT ma non sono collegati tra di loro.

Di seguito un esempio: in ANPR è stato iscritto erroneamente il soggetto A con nome e cognome invertiti tra loro; il comune effettua la mutazione mettendo il nome al posto del cognome ed ottiene l'errore sopra descritto, in quanto il soggetto A è registrato in AT con entrambi i codici fiscali.

Sono in corso di modifica la mutazione dei dati generali (tramite WA) e la funzione di risoluzione dei disallineamenti per consentire al comune di chiedere il collegamento.