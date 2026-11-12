# Gestione soggetti AIRE e Sezioni

I programmi che gestiscono le Revisioni Elettorali, nello specifico il **CONTROLLO ELETTORI SENZA SEZIONE ELETTORALE** della **SECONDA TORNATA** eseguono un controllo sugli iscrivendi, che di norma sono associati alle sezioni in automatico attraverso la combo **VIA → SEZIONE**, che non hanno vie collegabili a sezioni.

In particolare gli AIRE possono risultare senza sezione, e si hanno 2 possibili metodi di gestione.

## Introduzione

L'assegnazione automatica degli AIRE è modificabile attraverso le **Tabelle Elettorali** in particolare **Progressivi e Personalizzazioni** nella parte delle **Attribuzioni** (potete ricercare *Personalizzazione Elettorale* nella barra di ricerca e trovare il programma).

Nella sezione attribuzione trovate i primi due campi sugli AIRE:

[Schermata: Personalizzazione Elettorale - tab "Attribuzioni" con i campi "Attribuzione Sezione agli Aire" e "Sezione per Aire (se fissa)" evidenziati in rosso]

### ATTRIBUZIONE SEZIONE AGLI AIRE

Contiene due opzioni:

1. **Assegnare agli AIRE sezione 0** — il che vuol dire gestirli manualmente e smistarli nelle varie sezioni
2. **Assegnarli tutti ad un'unica sezione** — selezionando sotto la sezione di destinazione nel campo **Sezione Aire (se fissa)**

## Assegnare una sezione di default

Può succedere che qualcuno gestisca gli AIRE dedicando una sezione elettorale esclusivamente ad essi e quindi, invece che smistarli nelle varie sezioni, è possibile assegnarli automaticamente ad una sezione, come mostrato nello screen precedente.

> ⚠️ **Va fatto prima della revisione!!!**

## Gestione Manuale degli AIRE

La gestione Manuale prevede l'assegnazione della sezione all'elettore all'interno della revisione stessa: quindi utilizzando il programma **Gestione Elettori in Revisione**:

1. Dopo aver estratto gli elettori senza sezione, dall'omonimo programma della revisione, abbiamo un elenco di soggetti con **sezione=0**

[Schermata: "Controllo Sezione Elettorale" – Comune di Potenza Picena, con elenco di elettori nella colonna "Sezione" con valore 0]

2. Dopo aver fatto i controlli del caso (interrogazione anagrafe e altri), procediamo alla gestione del soggetto, quindi inserimento della sezione.

Usiamo il programma **GESTIONE ELETTORI IN REVISIONE**:

[Schermata: Menu revisioni – sezione "ISCRIZIONI" con l'opzione "Gestione Elettori in Revisione" selezionata]

Ci troviamo una videata dove cerchiamo i nostri elettori ai quali assegnare la sezione:

[Schermata: "Gestione Elettori in Revisione" – campo Revisione "2 - DINAMICA 2° TORNATA", con campi di ricerca: Cognome, Nome, Sesso, Sezione, Matricola, Data nascita, Causale elettorale in revisione]

Ricerchiamo per **nome, cognome, sesso** o altri dati rilevanti, dopo aver cliccato su **ELENCA** a destra della videata, ci porta ad una schermata dove selezioniamo il soggetto e con **doppio click su di esso** accediamo alla **MODIFICA DATI**.

[Schermata: "Interrogazione Elettorale" – elenco risultati con colonne: Tipo lista, Stato, Cognome e Nome, Sesso, Data nascita, Luogo nascita, Sezione (evidenziata in rosso con valore 0), Lista generale, Fascicolo, Note, Tessera. Pulsanti a destra: Nuovo, Visualizza Anagrafe, Tessere, Generazione 3D XML, Stampa comunicazioni, Fascicolo Elettorale, Note]

Compiliamo il campo rosso nei dati elettorali per assegnare la sezione: si ricerca con la **lentina** la sezione da assegnare e si clicca su **Aggiorna** a destra.

[Schermata: "Gestione elettori in revisione" – scheda "Dati Elettorali" con campo "Sezione Elettorale" evidenziato in rosso (valore 0), e pulsante "Conferma" evidenziato in rosso a destra]

Una volta aggiornato il dato, rilanciamo la stampa di controllo che cerca gli elettori senza sezione:

[Schermata: Menu revisioni – sezione "ISCRIZIONI" con "Controllo Elettori senza Sezione Elettorale" selezionato. Messaggio di informazione: "Per la selezione richiesta non c'è nessun dato da elaborare."]