# SECONDA TORNATA

La revisione dinamica seconda tornata viene effettuata due volte l'anno, entro il 31 gennaio e 31 luglio.

In questa fase devono essere apportate alle liste elettorali le seguenti variazioni:

## Iscrizioni

- immigrazioni da altro Comune
- acquisti di cittadinanza italiana
- ripristini di residenza effettuati da altro Comune
- ricomparsi
- iscritti all'AIRE
- riacquisto capacità elettorale

## Cancellazioni

- Cancellazioni per motivi diversi dall'emigrazione (es. perdita della cittadinanza italiana)

## Variazioni

- Variazioni per trasferimento di abitazione nella circoscrizione di altra sezione del Comune

---

## Apertura della Revisione Dinamica

Attivare la revisione dinamica dal menù **Servizi demografici → Elettorale → Menù revisioni**

Eseguire un doppio click sulla voce **Apertura revisione** per scegliere la revisione da attivare.

[Schermata: Menù revisioni con voce "Apertura revisione" evidenziata]

Selezionare **DINAMICA 2° TORNATA** dal menù a tendina e premere **Conferma**.

In questo modo si andrà a lavorare sulla Lista elettorale ordinaria.

Se si vuole eseguire una revisione straordinaria per elezioni è possibile spuntare la casella a fianco di **Revisione straordinaria?**, indicando anche l'elezione in corso dal menù a tendina.

[Schermata: Finestra "Apertura Revisione" con dropdown "DINAMICA 2° TORNATA" selezionato, checkbox "Revisione Straordinaria?" e campo "Cod. elez."]

---

## Fasi della seconda tornata

E' possibile entrare all'interno delle varie funzioni della revisione eseguendo un doppio click sulle rispettive voci.

---

# ISCRIZIONI

## Estrazione iscrivendi

In questa finestra vengono presentate le causali (preimpostate) di estrazione degli iscrivendi per la revisione.

Di default il programma genera solo una stampa degli estratti in formato excel.

Se si vuole procedere con la generazione dell'archivio sul quale lavorare per la revisione occorre spuntare la casella **Creazione archivio**.

Premere **conferma** per estrarre le proposte di iscrizione nel corpo elettorale.

[Schermata: Finestra "Programma Elettorale" con Revisione "2 - DINAMICA 2^ TORNATA", elenco causali (Immigrazione da altro Comune, Immigrazione dall'Estero, Ricomparsa, Acquisto cittadinanza Italiana, Riacquisto capacità elettorale, Iscrizione Aire, Ripristino Cancellazione, Iscrizione Per Altri Motivi), checkbox "Creazione Archivio" e "Stampa estratti"]

## Gestione Elettori in Revisione

E' possibile modificare o aggiungere manualmente dei nominativi alle proposte di iscrizione generate con l'estrazione automatica.

[Schermata: Finestra "Programma Elettorale" con combo "Gestione elettori in revisione" e filtri di ricerca (Cognome, Nome, Sesso, Sezione, Matricola, Data nascita, Causale elettorale in revisione)]

### Modificare iscrivendi

Selezionare dalla combo **Gestione elettori in revisione** ed eseguire la ricerca utilizzando i filtri presenti premendo **Elenca**.

Fare doppio click sul nominativo per entrare in modifica dei suoi dati.

Modificare i dati relativi all'ultima revisione se necessario (es. causale o luogo revisione) e premere **Conferma** per salvare la modifica.

[Schermata: Finestra "Ultima Revisione" con campi Revisione elettorale, Causale Revisione, Località, Irreperibilità, Data evento, Ricomparsa, Vecchia Sez. Ele., Vecchia Lista Sez., Num civico, Progr. interno]

### Aggiungere iscrivendi

E' possibile aggiungere degli iscrivendi alla revisione scegliendo dalla combo la voce **Aggiunta iscrivendi** ed indicando il nominativo del soggetto da aggiungere e premere il bottone →**Elenca**

il programma eseguirà la ricerca nell'archivio unico dei soggetti quindi, selezionare l'elettore con un doppio click e passare poi alla compilazione dei campi legati all'aggiunta del nuovo iscrivendo (dati minimi sono località, data evento e causale) e poi premere **Conferma**.

[Schermata: Finestra "Anagrafica Soggetti" con elenco risultati e finestra "Ultima Revisione" con campi Causale Revisione, Località, Data evento evidenziati]

### Eliminare iscrivendi

E' possibile eliminare un iscrivendo entrando in modifica dei suoi dati e poi premendo **Cancella**.

[Schermata: Finestra "Programma Elettorale" con profilo elettore e pulsante "Cancella" evidenziato]

## Controllo elettori senza Sezione Elettorale

Per eseguire un controllo degli elettori senza sezione elettorale selezionare **Stampa solo iscrivendi con sezione a 0**, modificare l'intestazione in caso di necessità e premere **Conferma**.

[Schermata: Finestra con dropdown "Stampa solo iscrivendi con sezione a 0" e campi intestazione]

Nel caso di elettori con sezione a 0 potete consultare questa guida, vale sia per AIRE che non AIRE: *Gestione elettori a con sezione a 0*

## Controllo soggetti non iscritti

Premendo **Conferma** verrà generata una stampa dei soggetti NON iscritti in elettorale e NON presenti in revisione.

[Schermata: Finestra "Programma Elettorale" con descrizione "stampa i soggetti NON iscritti in elettorale e NON iscritti in revisione"]

## Elenco preparatorio iscrivendi

In questa fase è possibile stampare l'elenco preparatorio delle proposte di iscrizione nel corpo elettorale utile anche per il controllo con le comunicazioni Anagrafe/Elettorale.

Modificare l'intestazione in caso di necessità, selezionare i filtri di interesse e premere **Conferma** per generare la stampa dell'elenco preparatorio degli iscrivendi.

[Schermata: Finestra con campi Intestazione 1, Intestazione 2, Seleziona il filtro (Iscrivendi), Filtro per sesso (Tutti), Ordinamento (Sezione / Alfabetico), Solo la causale (non filtrare per causale), Crea stampa per ogni Comune]

## Importazione 3D xml e stampa di controllo

Per importare i 3D xml consultare la guida *3D XML e certificati Penali*

La stampa di controllo fornisce delle indicazioni sui 3d xml mancanti rispetto al numero degli iscrivendi in revisione e se le generalità o atto di nascita di questi sono diverse.

AD Esempio nella stampa sotto:

1. **In Arancione 3D da elaborare** = Significa che sono arrivati dei 3Dxml relativi a quei soggetti ma che tali persone non sono state caricate nella revisione di iscrizione. Questo è un messaggio di **STOP**

2. **In Verde 3D di soggetti iscritti non per immigrazione** = Significa che i 3D arrivati sono relativi a soggetti la cui causale di iscrizione è diversa da immigrazione da altro comune ovvero potrebbe essere per rimpatrio dall'estero o per ripristino pratica di emigrazione ecc.. questo messaggio è **solo di avviso**

3. **In Rosso MANCA 3D** = Significa che ci sono dei soggetti in revisione di iscrizione a cui manca il 3D. Messaggio di **STOP**, in questo caso occorre assicurarsi con l'altro comune che non siano stati cancellati e toglierli dalla revisione

[Schermata: Esempio di stampa di controllo con tre sezioni colorate: "3D da Elaborare - Soggetti non iscritti in Revisione" (arancione), "3D da Elaborare à Soggetti iscritti in Revisione non per Immigrazione da" (verde), "Manca 3D - Soggetti iscritti in Revisione per Immigrazione da altro Comune" (rosso)]

**N.B.** *Qualora il comune non avesse ricevuto il 3d, ma è stata accertata la cancellazione del soggetto, sarà piena responsabilità dell'ufficiale elettorale iscrivere il soggetto.*

## CONTROLLO SOGGETTI IN REVISIONE ANPR

Una volta inseriti e verificati i 3dxml per essere pienamente sicuri che i soggetti iscritti siano stati effettivamente cancellati dal comune di provenienza o che in anpr siano correttamente inseriti, pronti per l'iscrizione elettorale, andare al punto di menu: **Servizi Demografici → Elettorale → ANPR - Funzioni di servizio → Controllo soggetti in revisione**

[Schermata: Percorso menu a cascata: 150. Servizi Demografici → 20. Elettorale → 70. ANPR - Funzioni di Servizio → 20. Controllo Soggetti in Revisione ANPR]

cliccare nel bottone **'Download'**, così da far iniziare la ricerca per ogni soggetto presente nella revisione, al termine, nel caso in cui ci siano soggetti non allineati uscirà un elenco in excel

[Schermata: Finestra "Controllo soggetti revisione ANPR" con barra di avanzamento "Elaborazione in corso - 30/575" e pulsante "Download"]

## Assegnazione verbale iscrizione

assegna a tutti gli iscrivendi numero e la data del verbale di iscrizione.

Cliccare sulla lente per aprire l'elenco dei verbali già caricati.

Cliccare su **Nuovo** per inserire un nuovo verbale.

[Schermata: Finestra "Verbali Elettorali" con elenco e pulsante "Nuovo"]

Compilare i campi **Verbale numero**, **data verbale** e **Descrizione**.

Premere →**Aggiungi** per salvare i dati inseriti, selezionare il verbale appena creato con il doppio click e →**Conferma**

[Schermata: Finestra "Verbali Elettorali" con campi Id, Verbale numero, Data verbale, Descrizione e pulsante "Aggiungi"]

## Assegnazione numero fascicolo

Verificare che il numero di fascicolo presente a video sia il successivo all'ultimo elettore aggiunto con la precedente revisione elettorale.

Premere **Conferma** per assegnare un numero di fascicolo a tutti i nuovi iscrivendi.

[Schermata: Finestra con campo "Aggiorna n° fascicolo a: Tutti gli iscrivendi" e "Numero fascicolo iniziale: 40973"]

## Richiesta documenti

### Richiesta certificato penale

Utilizzare questa funzione solo dopo aver importato tutti i 3D Xml per gli iscrivendi.

Premendo →**Conferma** verrà generato un file txt contenente solo gli iscrivendi di cui manca il 3D Xml.

Tale file dovrà essere caricato sul programma ministeriale per l'invio delle Massive, per procedere con la richiesta dei certificati penali al Casellario Giudiziale.

[Schermata: Finestra con campo "Nome file: richiesta_penale.txt" e "Elaborare: Solo gli iscrivendi di cui manca il 3D-XML"]

### Certificato cumulativo di residenza e cittadinanza

Utilizzare questa funzione solo dopo aver importato tutti i 3D Xml per gli iscrivendi.

il testo viene indicato di default dal programma quindi, indicare l'uso del certificato ed il firmatario.

Per quanto riguarda il flag di inserimento automatico nel fascicolo elettronico, lasciare attiva la spunta su **Inserimento automatico nel Fascicolo Elettronico (NON viene eseguita la stampa)** se si vogliono inserire direttamente i certificati all'interno del fascicolo dell'elettore, oppure togliere il flag, in questo modo i certificati non verranno caricati nel fascicolo ma sarà possibile visualizzare l'anteprima a video.

e nel campo **elaborare** scegliere la voce **Solo gli iscrivendi di cui manca il 3D Xml** →**Conferma**

[Schermata: Finestra "Certificato cumulativo residenza e cittadinanza" con campi Testo, Uso, Firmatario, checkbox "Inserimento automatico nel Fascicolo Elettronico (NON viene eseguita la stampa)" e "Elaborare: Solo gli iscrivendi di cui manca il 3D-XML"]

### Estratto di nascita

Utilizzare questa funzione solo dopo aver importato tutti i 3D Xml per gli iscrivendi.

Situazione analoga alla precedente, i testi vengono indicati per default, il primo testo si riferisce all'estratto di nascita degli elettori i cui atti sono presenti nel comune, il secondo crea la richiesta degli estratti di nascita che sono di altri comuni; quindi, indicare l'uso del certificato, il firmatario, scegliere se lasciare attiva o meno la spunta su **Inserimento automatico nel Fascicolo Elettronico (NON viene eseguita la stampa)** e la voce da elaborare impostata su **Solo gli iscrivendi di cui manca il 3D Xml** → **Conferma**

[Schermata: Finestra "Estratto di Nascita per atti in mio Possesso" e "Richiesta estratto di nascita per gli altri soggetti" con campi Testo, Uso, Firmatario, checkbox inserimento automatico e "Elaborare: Solo gli iscrivendi di cui manca il 3D-XML"]

## Controllo progressivi sezionali e generali

Premere **Conferma** per generare una stampa di controllo dei progressivi sezionali e generali tra la situazione che si trova nella tabella dei progressivi e quella che si trova in elettorale.

Nella colonna **Situazione in tabella** viene mostrato il primo numero disponibile da assegnare, se il controllo è andato a buon fine si vedranno delle semplici spunte verdi che stanno ad indicare che entrambe le situazioni nelle tabelle corrispondono, se invece dovessero esserci delle incongruenze numeriche queste verranno segnalate come nell'immagine di esempio

[Schermata: Tabella "Liste Elettorali" con sezioni "Lista Generale" (Situazione in tabella: 15173, Situazione in Elettorale: V), "Fascicolo" (Situazione in tabella: 40973) e "Lista Sezionale" con colonne Sezione, Situazione in tabella, Situazione in Elettorale. Sezione 3 mostra incongruenza: 1067 vs 1062 in rosso]

## Assegnazione numero lista generale

Utilizzare questa funzione solo dopo aver verificato la correttezza dei progressivi sezionali e generali impostati sul programma (passaggio precedente).

Premere **Conferma** per assegnare il numero di lista generale a tutti gli iscrivendi.

## Allegato al verbale

E' possibile stampare l'allegato al verbale distinto per sesso e ordinato o per lista sezionale o generale.

---

# CANCELLAZIONI

## Estrazione cancellandi

In questa finestra vengono presentate le causali (preimpostate) di estrazione dei cancellandi per la revisione. Di default il programma genera solo una stampa degli estratti in formato excel. Se si vuole procedere con la generazione dell'archivio sul quale lavorare per la revisione occorre spuntare la casella **Creazione archivio** → **Conferma**

[Schermata: Finestra con elenco causali cancellandi (Causale Emigrazione Italia, Causale Emigrazione Estero, Causale Irreperibilità, Causale Morte: 16-Morte, Causale perdita Cittadinanza: 17-Perdita cittadinanza italiana, Causale Morte, Causale canc. AIRE per irreperibilità, Causale canc. AIRE per Rimpatrio in altro Comune, Causale canc. AIRE perTrasf. ad AIRE altro Comune, Causale cancellazione AIRE, Ripristino Iscrizione, Causale Cancellazione per altri Motivi, Causale avvenuta Scadenza) e checkbox "Creazione Archivio" e "Stampa estratti"]

Proseguire in ordine con i successivi passi (dall'alto verso il basso), spiegati già nella fase delle iscrizioni.

- **Gestione elettori in revisione** può essere utilizzato per gestire manualmente i singoli cancellandi all'interno della revisione
- Generare l'elenco preparatorio, assegnare data e numero verbale e infine stampare gli allegati al verbale per i cancellandi

[Schermata: Albero di navigazione "2^ DINAMICA TORNATA" → "CANCELLAZIONI" con voci: Estrazione Cancellandi, Gestione Elettori in Revisione, Elenco preparatorio Cancellandi, Assegna Verbale Cancellazione, Allegato al Verbale Sezionale, Allegato al Verbale Alfabetico, Stampa Modelli 6D]

---

# CAMBI DI SEZIONE

## Estrazione cambi di sezione

Questo punto della revisione viene eseguito solamente se qualche elettore ha variato la sezione, altrimenti il passaggio può essere saltato.

In questa finestra vengono estratti per la causale (preimpostata) gli elettori che sono soggetti a cambio di sezione.

Di default il programma genera solo una stampa degli estratti in formato excel, se si vuole procedere con la generazione dell'archivio sul quale lavorare per la revisione occorre spuntare la casella **Creazione archivio** →**Conferma**

[Schermata: Finestra con campo "Cambi sez per indirizzo: 12 - Cambi di sezione", checkbox "Creazione Archivio" e "Stampa estratti"]

Proseguire in ordine con i successivi passi (dall'alto verso il basso).

- **Gestione cambi di sezione** può essere utilizzato per gestire manualmente i singoli cambi di sezione all'interno della revisione
- Generare l'elenco di controllo dei cambi di sezione, assegnare data e numero verbale e infine stampare gli allegati al verbale.

[Schermata: Albero di navigazione "CAMBI DI SEZIONE" con voci: Estrazione Cambi di sezione, Gestione Cambi di Sezione, Elenco Cambi di Sezione per Controllo, Assegna Nr. e Data Verbale Cambi Sezione, Allegato al Verbale in ordine di Vecchia Sezione, Allegato al Verbale in ordine di Nuova Sezione, Allegato al Verbale in Ordine Alfabetico]

---

# FASI FINALI

## Situazione progressivi

viene posto un controllo maggiore nei progressivi, soprattutto in caso di cambi di sezione

## Controllo tessere

Questa funzione controlla che i CANCELLANDI (o CAMBI DI SEZIONE) presenti in revisione abbiano una tessera elettorale e che gli ISCRIVENDI, invece, non abbiano una tessera elettorale.

Premere → **Conferma** per generare la stampa di controllo.

[Schermata: Finestra con descrizione controlli: "i CANCELLANDI (o CAMBI DI SEZIONE) presenti in revisione devono avere una tessera" e "gli ISCRIVENDI presenti in revisione non devono avere una tessera"]

## Assegna numero lista Generale a iscrivendi

al → **Conferma** il programma assegna in automatico il numero di lista generale a tutti gli iscrivendi presenti in revisione.

## Assegnazione nr. Lista Sezionale a iscrivendi e cambi di sezione

Utilizzare questa funzione solo dopo aver verificato la correttezza dei progressivi sezionali impostati sul programma (passaggio precedente).

Premere → **Conferma** e il programma assegnerà automaticamente per ogni iscrivendo e per ogni elettore che ha effettuato un cambio di sezione in revisione il corrispondente numero di lista sezionale.

## Stampa code Liste Generali e sezionali

questa funzione permette di stampare le code delle liste generali e sezionali, nel caso in cui l'ente non fosse ancora passato alle liste digitali. (nel caso delle liste digitalizzate, questi due punti possono essere saltati)

la finestra di stampa va impostata come nell'immagine di esempio, dove, se si desidera, è anche possibile suddividere la stampa in ordine alfabetico, prima dalla lettere A fino alla lettera M e poi dalla lettera L alla lettera Z. E nel box dedicato al tibro è possibile modificarlo o cancellarlo qualora non fosse necessario.

[Schermata: Finestra con campi Sesso (Tutti), Num. lista generale da 0 a 99999, Intestazione Cognome compreso tra M-Z, Timbro finale con testo di certificazione e campo M-Z evidenziato]

## Creazione Tessere Elettorali per Iscrivendi

Questa funzione assegna un numero di tessera elettorale agli iscrivendi nelle revisione.

Di default il programma assegna una sola tessera per persona, Aire compresi.

Per non assegnare una tessera agli Aire è sufficiente togliere la spunta su **Assegn. Tessera ad Aire**.

la finestra indica il carico in corso, dal numero al numero, con anche l'ultimo numero di tessera emesso.

Premere → **Conferma** per assegnare le tessere elettorali agli iscrivendi.

[Schermata: Finestra con campi Operatore, Carico in corso (150691201 al 150693200, Ultimo 150691949), Sesso (Tutti), checkbox "1 sola tessera x persona" e "Assegn. Tessera ad Aire", Sezione da 0 a 23, Escludere nati dopo il, Dt. creaz. Tessera, Ordinamento per (Alfabetico)]

## Stampe tessere elettorali

Questa funzione permette di stampare le tessera elettorale agli iscrivendi nelle revisione.

E' fondamentale aver già assegnato un numero di tessera ai singoli iscrivendi utilizzando il programma indicato al passo precedente (Creazione Tessere Elettorali per Iscrivendi).

Controllare il numero della prima e l'ultima tessera da stampare, che il programma assegna già in automatico, la modalità di stampa, che viene inserita di default in quanto viene configurata precedentemente, e scegliere un ordinamento e premere **Conferma** per generare l'anteprima di stampa.

[Schermata: Finestra con Carico in corso (150691201 al 150693200, Ultimo 150691949), Ristampare dal n° (150691949 al 150691949), sezione "Scegli il testo docx o la modalità di stampa" con Codice Testo e Modalità di Stampa (Stampante report cod 2), Ordinamento (Numero Tessera)]

## CREA e Stampa Etichette Tessera per Cambi di Sezione

Questa funzione permette di creare e stampare le etichette alle tessere elettorali per i cambi di sezione.

Anche qui il programma imposta tutto in automatico, quindi controllare la modalità di stampa, sempre assegnata di default e scegliere l'ordinamento.

Il funzionamento ha i seguenti valori:

- **Stampa e memorizza**: se lanciato questo punto per la prima volta, avendo dei cambi di sezioni il funzionamento è impostato su stampa e memorizza, in quanto *salva il nuovo dato riguardante sezione e indirizzo*, dovuto al cambio, e poi genera l'anteprima di stampa delle etichette
- **Ristampa**: genera l'anteprima di stampa delle etichette già memorizzate

Premere **Conferma** per generare l'anteprima di stampa.

[Schermata: Finestra con campi Sesso (Tutti), Sezione da 0 a, Ordinamento per (Sezione / Numero di lista), Funzionamento (Stampa e Memorizza), Codice Testo, Modalità di Stampa (stampante Laser HP Lasjet E60155)]

## Gestione Tessere Elettorali

Permette di gestire manualmente le tessere elettorali assegnate agli iscrivendi durante la revisione.

## Stampa notifica/invito ritiro Tessera Elettorale

Questa funzione permette di stampare le notifiche di ritiro della tessera elettorale.

Utilizzare uno dei filtri proposti tra sezione, data rilascio o numero tessera per generare l'anteprima di stampa della notifica.

Nel caso l'Ente abbia attivato i servizi per l'app.IO spuntare **Invio avviso tramite app.IO**, indicare oggetto, messaggio.

Premere **Conferma** per generare l'anteprima di stampa (o inviare il messaggio tramite app.IO).

## Registro Consegna Tessere Elettorali

Questa funzione permette di stampare il registro delle tessere elettorali rilasciate.

Utilizzare uno dei filtri proposti tra sezione, data rilascio o numero tessera, premere conferma per generare l'anteprima di stampa del registro tessere.

## Stampa prospetti

E' possibile generare 4 prospetti per la revisione in corso: motivo cancellazione, iscrizione, generale e sezionale per controllare a livello numerico le variazioni che saranno apportate al corpo elettorale.

## Stampa verbale

E' possibile stampare il verbale relativo alla seconda tornata.

Scegliere il tipo di output tra DOCX e PDF (DOCX è modificabile a video, PDF non è modificabile).

Indicare data e numero verbale.

Premere **Conferma** per generare il file.

Copia del verbale è trasmesso al Prefetto, al procuratore della Repubblica presso il Tribunale competente per territorio ed al presidente della Commissione elettorale circondariale.

## Conferma Dinamica 2° Tornata

Questa è la fase conclusiva della revisione dinamica seconda tornata, nella quale è possibile scegliere se confermare la revisione o annullarla.