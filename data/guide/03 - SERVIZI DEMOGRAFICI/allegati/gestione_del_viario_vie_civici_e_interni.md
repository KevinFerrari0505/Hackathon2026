# Gestione dei civici

La gestione degli indirizzi e dei civici su CWOL – cityware online si effettua dal gruppo programmi del modulo base ed è strettamente collegata all'anagrafe e all'elettorale. Importante quindi è qualora sopprimiate o create nuovi civici e interni con schede famiglie all'interno di controllare che siano associati alle rispettive sezioni di riferimento.

> **IMPORTANTE:** la gestione delle vie è come una matriosca, come visto nella guida per le sezioni, quindi oltre che essere inserite dentro dei macro elementi: sezioni, comitati di quartiere, frazioni ecc. le vie contengono i civici a loro volta suddivisi in interni.

## Struttura gerarchica

La scala dal contenitore più grande al più piccolo è:

**ELEMENTI ---> ASSOCIAZIONI ---> CIVICI ---> INTERNI**

Dove per ognuna si intende:

- **ELEMENTI:** sono i contenitori più grandi usati da altri programmi, contengono delle VOCI, per esempio: l'elemento SEZIONI conterrà come voci tutte le sezioni numerate, a loro volta ogni VOCE avrà una serie di ASSOCIAZIONI, che sono le VIE divise per pari o dispari e/o intere e spezzate nei civici.
- **ASSOCIAZIONI:** sono le VIE connesse ad un ELEMENTO del territorio.
- **CIVICI:** sono contenuti nelle VIE
- **INTERNI:** sono contenuti nei CIVICI

In questa guida vedremo la parte relativa alla gestione delle VIE e dei loro sottogruppi, CIVICI e INTERNI.

## Accedere alla gestione degli indirizzi

Seguire il percorso sotto indicato in giallo e arriverete al programma VIE:

Potete cercare "Vie" nella barra di ricerca o utilizzare l'App center.

[Schermata: percorso di navigazione nel menu CWOL: Modulo base → 100. Servizi Demografici → 10. Impostazioni generali → 10. Toponimi → 30. Vie e CAP Grandi Comuni → 30. Vie]

## Ricerca delle vie

Il programma che si apre presenta due modalità di ricerca:

1. Quella per filtri, quindi compilando la maschera in primo piano
2. Quella massiva, quindi facendo elenca e restituendo l'elenco di tutti gli elementi

[Schermata: finestra "Vie" con maschera di ricerca per filtri (Descrizione, Toponimo, Codice da/a, Codice Ente) e pulsanti a destra: Nuovo, Elenca, Carica, Salva, Reset]

## Gestione dei CIVICI

Una volta cercata la Via che vogliamo modificare possiamo agire prima sui CIVICI poi sugli INTERNI, infatti selezionandola possiamo poi modificare i vari sottogruppi:

[Schermata: elenco delle Vie con colonne Id, Descrizione, Data inizio, Data fine, Ubicazione, Utente mod., Data mod., Abilitato. Pulsanti a destra: Nuovo, Altra Ricerca, Associaz., Relazioni, Entità, Civici, Mappa]

Selezioniamo il record e clicchiamo su **CIVICI**:

> **NB:** con **Nuovo** potete inserire un indirizzo

[Schermata: finestra "Numeri civici" con colonne Codice via, Descrizione via, N.civ., Sub.num., Tipo, Data inizio, Data fine. Pulsanti a destra: Nuovo, Altra Ricerca, Interni, Mappa, Note]

### Creazione di un nuovo civico

Nel caso nella Via non fossero presenti dei civici li aggiungerete da **nuovo** compilando i seguenti campi:

[Schermata: form di creazione civico con campi: Progressivo, Codice via*, Numero civico*, Sottounumero, Compon.1, Compon.2, Compon.3, Tipo*, Agibilità, Senza fissa dimora, Data inizio*, Data fine, Prog. originale, Cod.immobile, Verifica/Verificato in data]

I campi colorati sono **obbligatori** per la creazione del civico.

## Gestione degli INTERNI

Una volta creato il civico o selezionato uno già esistente possiamo gestire gli interni, quindi, selezioniamo il civico e clicchiamo su **INTERNI**:

[Schermata: finestra "Numeri civici" con record selezionato (Codice via 276, Descrizione via PIAZZA GIARDINO DELLA MUSICA, N.civ. 15, Tipo Abitazione, Data inizio 01/01/1900). Pulsante "Interni" evidenziato a destra]

Si apre una videata che riassume i dati del percorso in alto e permette l'aggiunta degli interni sulla destra:

[Schermata: finestra "Numeri civici Interni" con riepilogo percorso in alto (Via: 276 PIAZZA GIARDINO DELLA MUSICA, Civico: 15, Tipo: Abitazione, Data inizio: 01/01/1900). Tabella con colonne: Progr. #, Tipo, Scala, Piano, Interno, Data inizio, Data fine, Verif., Utente mod., Data mod. Pulsante "Nuovo" a destra]

Su **NUOVO** poi andate a compilare i campi che vi servono, l'interno se non presente nella lista lo potete creare sempre con lentina **+ nuovo**:

[Schermata: form di creazione interno con campi: Progressivo n.civico, Scala, Interno*, Piano, Tipo, Agibilità, Cod.immobile, Data inizio, Data fine, Verifica/Verificato in data]

## Suggerimenti

- Se aggiungete un civico o un interno questo essendo già associato ad una via esistente si assocerà anche alla sezione elettorale nel caso le vie siano inserite nell'elemento sezione come **"tutta la via pari/tutta la via dispari"**. In caso di vie spezzate: come dal civico 15 al 24, se aggiungiamo il civico 14 dovremo associarlo alla sezione.