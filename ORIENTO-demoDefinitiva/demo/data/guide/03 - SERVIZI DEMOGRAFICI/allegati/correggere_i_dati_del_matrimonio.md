# Correzione Dati del Matrimonio

Alcune volte capita che in Cityware e di conseguenza in ANPR non vengano aggiornati i dati del matrimonio nella maschera dell'anagrafe.

Se il matrimonio è stato caricato nel DB locale come in figura sotto:

[Schermata: Maschera "Stato Civile" → "Matrimonio" con tab "Matrimonio" attivo. Visualizza: Data Matrimonio 02/06/1991, Cognome/Nome Coniuge GABRIELLI EVA. In basso, dettagli dell'evento: Data Evento 02/06/1991, Luogo Evento 151 316 FOSSOMBRONE (PS), Coniuge GABRIELLI EVA 9410. Atto Originale: Comune 151 316 FOSSOMBRONE (PS), Num. 15, Parte 2, Serie A, Anno 1991.]

ma interrogando il soggetto in anagrafe la situazione del matrimonio dovesse risultare così:

[Schermata: Scheda attuale del soggetto con Stato Civile evidenziato in giallo come "Coniugato/a ()" — campo coniuge vuoto, indicando che il dato non è stato aggiornato correttamente.]

## Procedura di correzione

Occorre seguire queste indicazioni:

### 1. Aprire Correzione Eventi

Percorso menu: **MENU → 150. Servizi Demografici → 10. Anagrafe → 30. Variazioni → 20. Eventi → 20. Correzione Eventi**

[Schermata: Menu a cascata con il percorso evidenziato in rosso fino a "20. Correzione Eventi"]

### 2. Ricostruzione situazione persona

Richiamare il soggetto ed effettuare una **ricostruzione situazione persona**.

[Schermata: Maschera "Correzione Eventi" con sezione "quale apportare modifiche". Tra le opzioni disponibili (Storico Generalità, Dati Personali, Variazioni Famiglia, Storico Iscriz/Canc. Temporanei, Variazioni di Domicilio, Modifica stato civile persona, Convivenza di Fatto, Immigrazione, Emigrazione, Iscrizioni AIRE, Movimenti AIRE, Variazioni di Domicilio AIRE), è selezionato il radio button **"Ricostruzione situaz. persona"** evidenziato in giallo.]

Deve presentare una situazione di questo genere: valore prima **NULLA** (o NC su stato civile), valore dopo i dati del coniuge e del matrimonio.

[Schermata: Tabella con colonne "descrizione campo modificato", "valore prima", "Valore Dopo". Righe: Identificativo soggetto coniuge (0 → 40616), Coniuge (Cognome) [VARCHAR] (vuoto → AB...), Coniuge (Nome) [VARCHAR] (vuoto → HMED EL... AYE), Data Matrimonio (vuoto → 17).]

> **Nota:** La medesima operazione deve essere eseguita sul nominativo del coniuge.

### 3. Verifica in interrogazione anagrafe

Tornando in interrogazione anagrafe la maschera deve presentarsi così:

[Schermata: Scheda attuale del soggetto con Stato Civile evidenziato in giallo: "Coniugato/a con ABDELHAY AHMED ELSAYED ELSAYED il 17-01-2013 a EGITTO (ET)" — ora il dato è correttamente popolato.]

## Riversamento in ANPR

Nel DB locale i dati sono aggiornati ma vanno riversati in ANPR seguendo la procedura sottostante.

### 4. Correzione eventi da CWOL

Da **CWOL** andare in **correzione eventi**.

Percorso menu: **MENU → 150. Servizi Demografici → 10. Anagrafe → 30. Variazioni → 20. Eventi → 20. Correzione Eventi**

[Schermata: Menu a cascata con percorso evidenziato fino a "20. Correzione Eventi"]

### 5. Selezionare il matrimonio

Richiamare la persona e mettere il pallino su **Matrimonio** lasciando la data del giorno.

[Schermata: Maschera "Correzione eventi" con "Dati soggetto" (Cognome AI, Nome MA, Data Deco. Anpr 03/11/2021). Sezione "Seleziona la tabella alla quale apportare modifiche" con radio button "Matrimonio" selezionato ed evidenziato in giallo.]

E premere il tasto **F2 - Avanti**.

### 6. Attivare e verificare i dati

Nella maschera che si presenta:

1. Cliccare la **matita**, in alto a sinistra, in modo da attivare tutti i dati.
2. Verificare che tutti i dati siano corretti, facendo attenzione anche ad eventuali dati degli atti (non sempre presenti se il matrimonio è avvenuto all'estero e non è stato mai trascritto in Italia), altrimenti modificarli.
3. Premere poi **F2 = Avanti**.

[Schermata: Maschera di correzione matrimonio con icona matita evidenziata in alto a sinistra. Campi visibili: Data Evento 17/01/2013, Luogo Evento 999 904 EGITTO (ET), Coniuge AHD... 40616. Atto Originale e Atto Trascritto con campi Comune, Num., Parte, Serie, Del., Vol., Anno. In basso: Stato Civile alla data CG Coniugato/a, Num.Variazione 71867, Data Var. 03/11/2021, Progr. Indice 0.]

> **Attenzione:** Controllare anche che lo **stato civile** sia valorizzato.

[Schermata: Dettaglio del campo "Stato Civile alla data" con valore "CG Coniugato/a" evidenziato in giallo con freccia nera indicante il campo.]

### 7. Ripetere per l'altro coniuge

Questo stesso passaggio va ripetuto da pag. 2 anche per l'altro coniuge se residente nello stesso comune.

### 8. Verifica finale in ANPR

Controllare in **Interrogazione ANPR** che i dati siano passati per entrambi i coniugi.

[Schermata: Maschera "ANPR Consultazione" con sezione "Generalità". Campi: Codice Fiscale, Id ANPR, Cognome ROSSI, Nome MARIO, Sesso M/F, Data nascita, Ricerca Nazionale (spuntato), Mostra solo gli AIRE, Dt Rif. scheda. Nota in giallo: "non si riferisce alla certificazione storica, ma alla data aggiornamento ca..."]