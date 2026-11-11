# AIRE Iscrizione

[Diagramma: Schema circolare che mostra il flusso tra "Cittadini all'estero", "Anagrafe dei Comuni AIRE" e "Rappresentanze e Uffici Consolari", con frecce che indicano il flusso di comunicazione tra i tre soggetti.]

## ISCRIZIONE

### Chi deve iscriversi

Iscriversi all'AIRE è un obbligo prescritto dalla legge istitutiva dell'AIRE nei seguenti casi:

- se si è cittadini italiani e si intende spostare la propria residenza all'estero per un periodo superiore ai dodici mesi. Ai sensi dell'art 43 del Codice Civile, la residenza è il luogo di abituale dimora, cioè il luogo dove solitamente si svolge la vita familiare, lavorativa e sociale;
- se si è cittadini italiani nati all'estero e da sempre residenti al di fuori del territorio italiano;
- se si acquisisce la cittadinanza italiana all'estero.

L'iscrizione all'AIRE dei cittadini italiani nati all'estero o degli stranieri che hanno acquisito all'estero la cittadinanza italiana, può essere effettuata solo a seguito della trascrizione, negli appositi registri di Stato Civile, dell'atto di nascita o del decreto di concessione della cittadinanza. L'accertamento del possesso/mantenimento della cittadinanza italiana spetta all'Ufficio consolare di residenza.

La trascrizione dell'atto di nascita per i cittadini nati e residenti all'estero deve essere effettuata, tramite l'Autorità diplomatico-consolare, presso i Registri di ovvero dell'avo materno o paterno. Nell'impossibilità di utilizzare i precedenti criteri, l'interessato dovrà indicare, su espresso invito dell'Autorità diplomatico consolare, un comune di sua scelta (art. 17 DPR n. 396/2000).

## Iscrizione all'AIRE per Espatrio all'Estero

### Percorso nel software

**Servizi Demografici > Anagrafe > Variazioni > Eventi > Nuovi Eventi**

### Selezionare l'innesco e la causale di iscrizione

[Screenshot: Maschera "Dati famiglia" con i campi Innesco impostato su "Operazione d'ufficio", Causale Variazione, Data Decorrenza, Data Variazione/Perfezionamento e i campi Cognome/Nome.]

Le causali per l'iscrizione possono essere **in famiglia (AIRE) esistente** oppure **creando una nuova famiglia**.

[Screenshot: Elenco delle causali disponibili sotto la voce "2.2.0 - ISCRIZIONE":]

- ○ 2.2.1 - Iscr. AIRE per Nascita in famiglia esistente
- ○ 2.2.2 - Iscr. AIRE per acquisizione Citt. italiana in famiglia esistente
- ○ 2.2.3 - Iscr. AIRE per Ricomparsa in famiglia esistente
- ○ **2.2.4 - Iscr. AIRE per Espatrio/Res. estero in famiglia esistente**
- ○ 2.2.5 - Iscr. AIRE per Trasferimento da altra AIRE in famiglia esistente
- ○ 2.2.7 - Iscr. AIRE per Nascita con Creazione Nuova Famiglia
- ○ 2.2.8 - Iscr. Aire per acquis. Cittad. italiana in Nuova famiglia
- ○ 2.2.9 - Iscr. Aire per Ricomparsa con Creazione Nuova Famiglia
- ○ **2.2.10 - Iscr. Aire per Espatrio/Residenza Estero in Nuova Famiglia**
- ○ 2.2.11 - Iscr. Aire per Trasferimento da altra AIRE n Nuova Famiglia

La differenza tra una causale e l'altra, nel primo caso, sta nella ricerca di una famiglia AIRE già esistente.

[Screenshot: Maschera con causale "Iscr. AIRE per Espatrio/Res. estero in famiglia esistente" selezionata e box "Inserisci l'intestatario scheda della famiglia di destinazione" con campi Cognome e Nome.]

Mentre nel secondo caso andranno caricati tutti i dati di nuova residenza.

[Screenshot: Maschera con causale "Iscr. Aire per Espatrio/Residenza Estero in Nuova Famiglia" e sezione "Luogo residenza estera" con campi Nazione, Residente in, Dt arrivo Circoscriz., Consolato, Codice avv. postale ente.]

### Note sulla compilazione

- La **data di arrivo nella circoscrizione consolare** non è obbligatoria e onde evitare di scrivere una data sbagliata che poi potrebbe bloccare il passaggio in ANPR è preferibile non indicarla.
- La **Data decorrenza** è quella indicata nel CONS01.

### Procedura operativa

Dopo aver compilato la prima videata proseguire con il tasto **AVANTI**.

Nella parte in alto viene proposta la famiglia AIRE se si è scelto **in famiglia esistente**, altrimenti, nel caso si sia scelto **in nuova famiglia** il box sarà vuoto.

Nella parte sotto invece sarà possibile ricercare il o i soggetti da iscrivere all'AIRE. Automaticamente il programma creerà anche la pratica di emigrazione nel Data Base locale.

[Screenshot: Maschera "Componenti interessati alla Pratica" con tabella contenente colonne: Cognome Nome, Fan, Sesso, Data Nascita, Luogo Nascita, St.Civ., Rel.Par., Ord., Can., N. Ord. I nuovi soggetti sono evidenziati in verde.]

I nuovi soggetti della famiglia vengono evidenziati in **verde** e prima di proseguire occorre caricare la **relazione di parentela** e il **numero d'ordine** all'interno della famiglia.

### Eliminazione di un soggetto errato

Nel caso in cui si commetta un errore nel prendere una persona piuttosto che un'altra è possibile eliminare il soggetto selezionandolo (viene evidenziato in **giallo**) e premendo poi il tasto del **cestino**.

[Screenshot: Tabella con un soggetto evidenziato in giallo e il tasto cestino in basso a sinistra.]

### Riepilogo e conferma

Proseguendo con **Avanti** il programma mostra un riepilogo con le operazioni eseguite e che proseguendo verranno confermate sia nel DB locale che in ANPR.

> **N.B.** Se la maschera dovesse essere vuota senza nessuna riga che evidenzia l'operazione appena eseguita vuol dire che qualcosa non è andato a buon fine, in questo caso contattare l'assistenza.

[Screenshot: Maschera di riepilogo con messaggio "Operazione completata, ma non registrata. Verificare l'elenco delle persone interessate e premere CONFERMA per registrare" e tabella riepilogativa.]

## Iscrizione per altre causali

Allo stesso modo si può iscrivere per le altre causali dopo aver trascritto l'atto di stato civile.

L'unica differenza riguarda l'iscrizione per **trasferimento da altra AIRE**.

[Screenshot: Elenco causali con ricerca "trasfer" che mostra: 2.2.5 - Iscr. AIRE per Trasferimento da altra AIRE in famiglia esistente e 2.2.11 - Iscr. Aire per Trasferimento da altra AIRE n Nuova Famiglia.]

Perché in questo caso il soggetto deve essere ricercato in **ANPR** con lo specifico tasto dedicato.

[Screenshot: Maschera di ricerca soggetto con campi Cognome, Nome, Nascita il, Sesso, Stato civile, Rel.Par., Cittadinanza, C.F., N. Ord Aire e un pulsante specifico per la ricerca in ANPR evidenziato in rosso.]