# Stampa Residenti Estero per Elezioni

Questo programma vi permette di estrarre l'elenco dei votanti AIRE, sia in documento che in Excel, stampare le etichette/cartoline di avviso e calcolare i fabbisogni da comunicare al ministero nonché la composizione dell'elettorato AIRE per paese di residenza.

Per utilizzare in modo corretto questo programma è necessario che abbiate **prima** eseguito queste operazioni:

1. Apertura di un codice elezione → *Aprire un codice elezione*
2. Creazione dell'archivio votanti AIRE → *Creazione Archivio AIRE*

---

## Accesso al programma

Accedete al programma seguendo questo percorso:

**150. Servizi Demografici - 20. Elettorale - 40. Elezioni - 30. Gestione Votanti AIRE - 30. Stampa Residenti Estero per elezioni**

---

## Stampa Elenchi/Estrazione in Excel

Per estrarre gli elenchi, sia in documento che in EXCEL, dovrete compilare l'intera videata andando a configurare i parametri di estrazione:

1. **Tipo Lista:** selezionate **Liste Elettorali**
2. **Zona di residenza:** permette di estrarre i votanti AIRE in base alla zona di residenza. La dicitura **CEE** sta per UE. Potete anche inserire una nazione se volete estrarre per singolo stato.

   [Screenshot: campo "Zona residenza" con menu a tendina che mostra le opzioni: TUTTI, CEE, EXTRACEE, TEMPORANEI]

3. **Votanti in:** selezionate se volete estrarre gli AIRE che votano in Italia o all'estero; tenete conto di come avete creato l'archivio
4. **Sesso:** potete estrarre per sesso o senza distinzione
5. **Codice elezione:** inserite il codice della consultazione elettorale per la quale state facendo le operazioni pre-elettorali
6. **Codice testo e formato di output:** nel codice testo, con la lente potete ricercare i testi per gli elenchi e le etichette:

   [Screenshot: finestra "Risultato Ricerca" con Elenco Documenti. Filtri: Codice vuoto, Descrizione "estero", Tipo vuoto. Risultati:
   - 0041 – Verbale Elettori Votanti Estero per corrispondenza – DOCX
   - 0352 – Elenco Residenti estero per elezioni x Pubblicazione – DOCX
   - 0042 – Elenco Residenti estero per elezioni - voto – DOCX]

Cliccate a destra su **CONFERMA** per elaborare le stampe o su **ESPORTA EXCEL** per esportare i dati in un foglio lavoro di EXCEL.

---

## Esempio di estrazione

Ecco un esempio di estrazione: le votanti all'estero residenti in paesi UE per le elezioni politiche:

[Screenshot: videata "Stampa residenti all'estero per elezioni" con i seguenti parametri impostati:
- Tipo lista: 1 - Liste Elettorali
- Zona residenza – Seleziona: CEE
- Votanti in – Seleziona: Estero
- Sesso – Seleziona: Femmina
- Cod. Elezione: 5 – ELEZIONI POLITICHE
- Ordina per: Stato estero residenza/Sesso/Nome
- Codice testo: cwd_ElezVotoEstero – Elenco Residenti estero per elezioni - voto
- Formato di output: Documento in formato PDF]

Selezionando l'estrazione in EXCEL verrà scaricato il file dal quale poter estrarre quanti residenti per singolo paese → *Gestire un estrazione in EXCEL*

---

## Calcolo del fabbisogno

Per calcolare i fabbisogni di etichette e cartoline, nel caso li comunichiate ad una ditta esterna o al ministero, potete usare le funzioni sopra descritte oppure lanciare un'estrazione generica stampando l'elenco:

1. **Zona di residenza:** **tutti**, oppure scegliete una **zona** a seconda del tipo di consultazione elettorale
2. **Votanti in:** **tutti**, oppure scegliete tra **Italia/estero** a seconda del tipo di consultazione elettorale
3. **Sesso:** **tutti**

[Screenshot: videata "Stampa residenti all'estero per elezioni" con parametri:
- Tipo lista: 1 - Liste Elettorali
- Zona residenza – Seleziona: TUTTI
- Votanti in – Seleziona: Tutti
- Sesso – Seleziona: Tutti
- Cod. Elezione: 5 – ELEZIONI POLITICHE
- Ordina per: Stato estero residenza/Sesso/Nome
- Codice testo: cwd_ElezVotoEstero – Elenco Residenti estero per elezioni - voto
- Formato di output: Documento in formato DOCX]

Cliccate su **CONFERMA** per stampare l'elenco e scorretelo fino al numero finale.

---

## Stampa delle etichette

Per la stampa delle etichette impostate i filtri secondo le indicazioni generali spiegate in precedenza, andando a selezionare la parte di votanti AIRE per i quali le volete stampare e selezionate il testo **"cartoline"** attraverso la lente di ricerca (mantenete il formato output **docx**):

[Screenshot: finestra "Risultato Ricerca" con Elenco Documenti. Filtri: Codice vuoto, Descrizione "cart", Tipo vuoto. Risultati:
- 9338 – Cartoline Aire 2 X 8 – DOCX
- 9347 – Cartoline Aire 2 X 6 – DOCX
- 0268 – Cartoline AIRE 2 colonne – DOCX]

Per la formattazione della stampante in base al formato etichette che avete acquistato, prendete appuntamento con anticipo scrivendo una mail a **citypeople@palitalsoft.it**.