# ANPR - Allineamento elettori AIRE

Ogni anno il Ministero degli Affari Esteri invia una circolare con scadenza **31.12.0000** di ogni anno.

[Immagine: Circolare del Ministero degli Affari Esteri e della Cooperazione Internazionale - D.G.I.E.P.M. / D.G.A.I. Ufficio IV / Direzione Centrale dei Servizi Elettorali - Oggetto: AIRE – Attività di verifica dei dati – Aggiornamento al 31 dicembre dell'Elenco unico dei cittadini residenti all'estero]

I Comuni devono controllare gli indirizzi AIRE, il campo **"TIPO ELETTORE"** e risolvere le anomalie segnalate sulla web app se presenti.

## Procedura di aggiornamento del campo tipo elettore

Per poter aggiornare il campo tipo elettore per gli AIRE procedere come segue:

**Servizi Demografici** ⇒ **Anagrafe** ⇒ **ANPR - Funzioni di Servizio** ⇒ **ANPR - Allineamento Elettori Aire**

Non cambiare nessun valore e confermare la videata che si presenta.

[Immagine: Videata "ANPR: allinea elettori AIRE" con messaggio "Verrà allineato su ANPR il dato di elettore sì/no, per gli iscritti Aire. Attenzione: chiudere il messaggio a video non terminerà l'elaborazione sul server." Campi: "A partire dalla matricola: 0" e "per numero di soggetti: 99999". Pulsanti: "Conferma" e "Apri log"]

> ⚠️ Il programma può impiegare parecchi minuti, dipende da quanti AIRE deve aggiornare.

Al termine può comparire un file con le anomalie riscontrate da aggiornare a mano.

## Risoluzione delle Anomalie

Si vedranno punto per punto le anomalie consigliando i programmi e le azioni utili alla risoluzione:

### AIRE Elenchi Anomalie – Soggetti con codice territorio di nascita valorizzato ma senza luogo di nascita

- Avete inserito il codice del territorio senza inserire poi il luogo di nascita, provvedere a correggere tramite **Nuovi Eventi → Causale rettificà generalità senza cambio sesso**. Se non avete il luogo inserito dovete inserirlo. **ATTENZIONE ALLA TABELLA LOCALITÀ**

### AIRE Elenchi Anomalie – Soggetti con codice territorio di nascita valorizzato e luogo nascita uguale alla denominazione di un comune italiano

- Simile al precedente, è valorizzato un codice territorio estero associato ad un comune italiano di nascita, intervenire con **rettifica generalità senza cambio sesso**

### AIRE Elenchi Anomalie – Soggetti con tipo elettore non valorizzato

- Agite da **web app**

### AIRE Elenchi Anomalie – Soggetti indirizzo o località che riportano il nome di uno stato estero

- Dovete specificare l'indirizzo o la località, potete intervenire con **Correzione Eventi → Causale Indirizzo AIRE**

### AIRE Elenchi Anomalie – Soggetti SOLO MIN che non vengono aggiornati da almeno 4 anni

- Aggiornare, può essere minorenni di cui non si hanno atti

### AIRE Elenchi Anomalie – Soggetti con luogo nascita composto da soli caratteri speciali o numeri

- Correggere come al punto 1

### AIRE Elenchi Anomalie – Soggetti con cognome, nome, o cognome coniuge composto da soli caratteri speciali o numeri

- Specificare Nome e cognome con una **rettifica generalità** se si tratta del soggetto, correggere il matrimonio se si tratta di un coniuge

### AIRE Elenchi Anomalie – Soggetti con codice ISTAT comune di nascita inesistente

- Correggere il codice ISTAT tenendo conto della documentazione tecnica fornita da ANPR. Controllare che il soggetto sia stato caricato nel modo corretto

### AIRE Elenchi Anomalie – Soggetti con territorio di nascita errato

- Sono i casi di extraterritorio, come i nati su imbarcazione, inserire **codice 998** per ANPR

### AIRE Elenchi Anomalie – Soggetti nati a Fiume, Pola, Zara dopo il 15/09/1947

- Non esistono più, controllare la tabella di decodifica stati su ANPR

### AIRE Elenchi Anomalie – Posizioni senza indicazione del comune o dello stato estero di nascita

- Inserire questi dati attraverso una **correzione eventi** o una **rettifica generalità senza cambio sesso**

### AIRE Elenchi Anomalie – Soggetti con luogo nascita contenente parole non valide

- Correggere il luogo di nascita come nel punto 1

### AIRE Elenchi Anomalie – Soggetti con luogo di residenza contenente parole non valide

- Correggere l'indirizzo immettendo caratteri che ANPR accetta, **no caratteri diacritici**

### AIRE Elenchi Anomalie – Soggetti con toponimo di residenza non valorizzato

- Inserire con **correzioni eventi indirizzo AIRE**

### AIRE Elenchi Anomalie – Soggetti con residenza non individuabile

- Adeguare l'indirizzo specificandolo o reperendolo

### AIRE Elenchi Anomalie – Data arrivo circoscrizione consolare non valida

- Va modificata la data riprendendo i documenti inviati dal consolato, attenzione alle variazioni già eseguite, anch'esse vanno tenute in conto. **ACCORDANZA TRA LE DATE DI DECORRENZA**

### AIRE Elenchi Anomalie – Codici fiscali duplicati – posizioni duplicate (cittadini iscritti contemporaneamente sia in APR che in AIRE o in due Comuni AIRE)

- Bisogna sanare la posizione cancellando il soggetto che non è AIRE, assicurandosi della coerenza e veridicità dei dati.

### AIRE Elenco Unico – Soggetti scartati nell'elenco unico

- Consultare l'archivio e sanare le posizioni che non andavano cancellate.