# Interrogazione elettorale

**Altre guide collegate:** [Variazione elettorale](#)

Per consultare i dati presenti nell'archivio elettorale andare nel menù **Servizi Demografici→Elettorale→Manutenzione→Interrogazione Elettorale**.

La consultazione può essere effettuata utilizzando i campi proposti e premendo **Elenca**.

[Schermata di Interrogazione Elettorale con campi: Cognome, Nome, Sesso, Sezione Elettorale, Num. Lista Sezionale, Data di nascita, Num. Lista Generale, Tipo Lista, Matricola, Fascicolo. Pulsanti: F4 - Elenca, Carica, Salva, Reset. Filtri "Voglio vedere": Elettori, Sospesi, Cancellati, Non iscritti.]

## Criteri di ricerca per il campo COGNOME

La ricerca utilizzando il campo **COGNOME** segue il criterio mostrato nei seguenti esempi con una lista di nominativi:

| Contenuto campo selezione | Risultato in lista | Criterio |
|---|---|---|
| `ro` | Ronconi, Rosi, Rossi, Rossini | Quelli che iniziano per 'ro' |
| `ro%` | Ronconi, Rosi, Rossi, Rossini | Quelli che iniziano per 'ro' |
| `rossi` | Rossi, Rossini | Quelli che iniziano per 'rossi' |
| `rossi%` | Rossi, Rossini | Quelli che iniziano per 'rossi' |
| `%ro%` | De Rosa, De Rossi, Ronconi, Rosi, Rossi, Rossini | Quelli che contengono 'ro' |
| `%rossi%` | De Rossi, Rossi, Rossini | Quelli che contengono 'rossi' |
| `%rossi` | De Rossi, Rossi | Quelli che finiscono con 'rossi' |
| VUOTO | TUTTI | |

## Filtri di visualizzazione

E' possibile, inoltre, modificare i filtri su quali dati si vogliono vedere nell'archivio elettorale togliendo o inserendo le spunte su **Elettori**, **Sospesi**, **Cancellati**, **Non iscritti**.

## Funzionalità disponibili nell'elenco elettori

Una volta eseguita la ricerca si arriverà alla schermata con l'elenco degli elettori, nella quale è possibile utilizzare varie funzionalità selezionando con un solo click l'elettore e cliccando poi uno dei seguenti bottoni:

[Schermata elenco elettori con colonne: Tipo Lista, Stato, Cognome e Nome, Sesso, Data nascita, Luogo nascita, Sezione, Lista generale, Fascicolo, Note, Tessera. Pulsanti a destra: Visualizza Anagrafe, Tessere, Generazione 3D XML, Stampa comunicazioni (pdf), Stampa comunicazioni (docx), Fascicolo Elettorale, Altra Ricerca.]

### Interrogazione anagrafe

Permette di visualizzare la situazione all'interno dell'archivio anagrafico.

### Tessere

Visualizza lo storico di tutte le tessere dell'elettore, con la possibilità di svolgere funzioni nella tessera attraverso i vari bottoni (per comprendere le funzioni consultare la guida: **Tessere Elettorali**).

[Schermata Gestione Tessere Elettorali con colonne: Tessera, Se, Cognome e nome, Data di nasc, Data rilascio, No Annullamento, Motivo Annullamento, Tipo tess, Utente mod., Data mod. Pulsanti a destra: Altra Ricerca, Assegna data Notifica, Aggiungi, Duplicato, Completa di timbri, Ristampa, Etichetta, Stampa Notifica.]

### Generazione_3D-XML

Verranno generati i files richiesti (sotto forma di zip se cumulativo) nella cartella download del browser.

### Stampa comunicazioni elettorale

Guida consultabile al link **Stampa Comunicazioni Elettorale**.

### Fascicolo elettorale

Consultare il fascicolo elettorale dell'elettore se presente, oppure crearlo tramite il bottone **'nuovo'** inserendo gli allegati.

[Schermata Fascicolo Elettorale con colonne: Categoria, Descrizione, Nome, UUID. Pulsanti a destra: Nuovo, Altra Ricerca, Esporta cartella, Download.]

## Note elettorali

Inserire, modificare o cancellare note elettorali.

### Inserimento nuova nota

1. Selezionare l'elettore e premere **Note** sulla destra.

[Schermata elenco elettori con il pulsante "Note" evidenziato sulla barra laterale destra.]

2. Premere **Aggiungi** per inserire una nuova nota.

[Schermata Gestione Note con colonne: Tipo Nota, Evidenza, Testo. Pulsante "Aggiungi" evidenziato.]

3. Nel campo **Annotazione** inserire il testo della nota e poi premere **Conferma** per salvare.

[Schermata di inserimento nota con campi: Annotazione (testo libero), Tipo Nota, Gruppo Nota, Natura Nota, In evidenza, Urgente, Progressivo Nota, Riga Nota. Pulsanti: Conferma, Annulla.]

4. La nota inserita sarà visualizzabile direttamente dall'elenco degli elettori. Nella colonna **Note** comparirà una nuova icona e posizionandovi il cursore sopra verrà mostrato un tooltip con le note inserite.

[Schermata elenco elettori con icona nota nella colonna "Note" e tooltip "QUESTA È UNA NOTA" visualizzato al passaggio del mouse.]

### Modifica/cancellazione della nota

- **Modifica:** Per modificare una nota eseguire un **doppio click sulla riga** o cliccare sulla **matita**.
- **Cancellazione:** Per cancellare una nota occorre selezionarla e poi premere il pulsante **cestino** in basso.

[Schermata Gestione Note con indicazione "Modifica della nota" (icona matita) e "Cancellazione della nota" (icona cestino in basso).]

## Scheda dettaglio elettore

Mentre per entrare nel dettaglio della scheda dell'elettore premere **due volte il tasto sinistro del mouse** nell'elettore desiderato.

[Schermata dettaglio elettore con campi: Nome, Sesso, Nato il, Tipo lista, Stato, Sezione, Num. Lista Sezionale, Fascicolo, Matricola, Tessera. Tab disponibili: Dati Elettore, Cittadino, Controllo dati correnti in anagrafe.]

### Tab Cittadino

Selezionando il tab **cittadino** è possibile vedere i dati legati ad:

- Atto di nascita
- Stato civile
- Cittadinanza
- Indirizzo dell'elettore
- Professione
- Titolo di studio

Se dovessero essere presenti delle differenze tra i dati di elettorale e anagrafe saranno evidenziati in **rosso**.

[Schermata tab Cittadino con sezioni: Atto Nascita (Luogo, Numero, Parte, Serie, Delegazione, Volume, Anno Atto), Stato Civile, Cittadinanza, Num civico, Progr. interno, Località estera, Professione, Titolo di Studio.]

### Tab Controllo dati correnti in anagrafe

Dal tab **Controllo dati correnti in anagrafe** verranno evidenziati le singole differenze tra anagrafe e elettorale. Per bonificarle seguire il richiamo alla guida **Variazione elettorale**.

[Schermata Controllo dati correnti in anagrafe con esempio di differenza evidenziata: "Stato Civile: Elettorale: CG / Anagrafe: (vuoto)".]