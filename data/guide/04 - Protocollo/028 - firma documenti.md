# Firma uno o più documenti in carico

Il firmatario troverà il documento nel portlet **Documenti in Carico**, indicato dalla lettera **I**, dal simbolo verde e dalla coccarda rossa, che indica la richiesta di firma.

[Schermata: Portlet "Protocolli in carico" con elenco di documenti. Ogni riga mostra la lettera "I", il simbolo verde, la coccarda rossa, il numero di protocollo, la data di trasmissione e l'oggetto. In basso sono presenti i filtri: In Carico, Vedi Chiusi, Scaduti, Rifiutati, Vedi Inviati, Da Firmare.]

Per visualizzare solo i *Documenti alla Firma* tra i propri protocolli in carico, si può utilizzare il menù a tendina e selezionare **"Documento"**.

[Schermata: Menù a tendina del filtro con opzioni: ---TUTTI---, Arrivo, Partenza, Doc. Formale, Documento (selezionato), Passo.]

## Firma di un singolo documento

Una volta aperto il documento è sufficiente cliccare **Vai alla Firma** per aprire la finestra di firma remota. Inserire nome utente e password della firma, il codice OTP e cliccare *Conferma*.

[Schermata: Dettaglio documento con barra laterale destra contenente i pulsanti: Visualizza Documento, Firma gli allegati, Chiudi Iter, Rifiuta, Vai Alla Firma. In basso a destra è indicato lo stato "ITER APERTO / Iot.Giorn I".]

Al momento della firma, il programma assegna al documento un numero di protocollo e lo identifica come una **partenza (P)** o come un **documento formale (C)**.

### Documento in partenza

Se si tratta di una **partenza** e se è presente almeno un indirizzo di posta elettronica, il programma predispone il protocollo per l'invio. Gli allegati firmati sono caricati automaticamente; l'oggetto e il corpo della mail sono compilati con i dati del protocollo, ma possono essere modificati. Con il tasto *Conferma* il protocollo viene inviato a tutti gli indirizzi indicati. L'operazione è conclusa e l'iter è chiuso automaticamente.

[Schermata: Finestra "Gestione Mail" con tabella indirizzi (es. dev.italsoft@pec.it), campo Oggetto precompilato con il numero di protocollo, editor di testo per il corpo della mail, e tabella allegati firmati con nome file, descrizione, provenienza e dimensione. Pulsante F5-Conferma in alto a destra.]

### Documento interno formale

Se si tratta di un **documento interno formale**, dopo la firma il protocollo viene inviato a tutti gli *assegnatari* indicati. L'iter **non** viene chiuso automaticamente. Se il lavoro sul documento è concluso, cliccare **Chiudi Iter**.

## Firma massiva di più documenti

Se i documenti da firmare sono più di uno, è possibile firmarli **massivamente**.

Nella scrivania dei **Documenti in Carico**, selezionare il filtro *Da Firmare*.

In basso a destra è presente una finestra per le operazioni massive.

[Schermata: Scrivania "Documenti in carico" con elenco di protocolli da firmare. In basso a destra è visibile la finestra "Operazioni massive" con campi "Dal:" e "Al:" per l'intervallo di date e il pulsante "Firma Massiva".]

Si può impostare un intervallo di date per filtrare i protocolli da firmare oppure, se non si impostano date, verranno proposti tutti i protocolli da firmare presenti sulla scrivania, indipendentemente dalla data di trasmissione.

Cliccando il tasto **Firma Massiva**, si apre una finestra con l'elenco dei protocolli da firmare.

Cliccando la **graffetta**, è possibile visionare l'allegato che si andrà a firmare.

[Schermata: Finestra "Risultato Ricerca" con messaggio "I protocolli selezionati verranno Firmati Digitalmente." Tabella con colonne: Numero, Data, Oggetto, Provenienza, Gestione, Prot. Colli, e icona graffetta per "Vedi Allegati". In basso il pulsante "F2-Conferma Selezione".]

Selezionare i protocolli da firmare.

- Per selezionarli **tutti**, spuntare il primo quadratino in alto a sinistra.
- Altrimenti spuntare **singolarmente** i protocolli.

Infine confermare la scelta con il tasto *Conferma Selezione*.

Si aprirà la schermata per la firma remota. Inserire le credenziali della firma, il codice OTP e confermare.

[Schermata: Finestra "Autenticazione Firma Remota" con campi: Tipo di Firma (Firma Digitale remota in standard CAdES (p7m)), Dominio Autenticazione (firma), Nome Utente, Password, OTP (One Time Pass). Pulsante Conferma.]

## Esito della firma massiva

Un messaggio avvisa che la firma è andata a buon fine e che i documenti sono stati protocollati.

In caso di protocolli in partenza via pec/mail, il programma avvierà automaticamente la spedizione.

Eventuali anomalie in fase di firma o di invio saranno segnalate.

[Schermata: Finestra "Firma massiva" con messaggio: "Firma massiva completata. Sono stati firmati 2 su 2 elementi da firmare. Altre Informazioni: Documentale 9751: firmato e trasformato nel protocollo 15 / 2020 P; Documentale 9752: firmato e trasformato nel protocollo 16 / 2020 P."]