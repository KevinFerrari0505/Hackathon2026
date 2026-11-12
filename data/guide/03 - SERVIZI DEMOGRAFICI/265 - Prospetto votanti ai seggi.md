# Prospetto votanti ai seggi

Si tratta di un'estrazione che genera un prospetto Excel della forza votante relativamente ad una specifica elezione che deve essere precedentemente inserita tramite **APERTURA ELEZIONI**. La videata che si apre richiede la compilazione del campo *Cod.elezione* attraverso il quale, cliccando sulla lente, è possibile selezionare un'elezione e di conseguenza ottenere un conteggio del corpo elettorale in relazione alla tabella **tipi elezioni**:

[Schermata della videata "Prospetto forza votante" con i campi: Cod.elezione (es. 13 - Elezioni Comunali 14-15 maggio 2023), Data Elezione (14-05-2023), Prospetto 1 (Forza votante), e pulsanti "Salva Parametri Default" e "Conferma"]

Cliccando su **Conferma** a destra della videata viene scaricato il file Excel contenente il prospetto:

[Schermata del download del file Excel "prospetto_16_1696860185268.xlsx" dal browser]

Inoltre, il prospetto può essere lanciato più volte nel corso delle operazioni precedenti all'elezione e confrontato con gli elenchi e verbali della gestione votanti AIRE, dei Minorenni e delle varie revisioni.

Il prospetto che ne esce mostra sottrazioni e addizioni di elettori che, partendo dal totale degli elettori interessati da una tornata elettorale, sottrae o aggiunge elettori per arrivare alla composizione finale.

---

## Note importanti sul prospetto

> **IMPORTANTE:** la seconda tabella sulla sinistra, dopo le sezioni, è l'ultima situazione della lista a seguito di revisione, quindi prima dell'inizio delle operazioni elettorali i totali devono combaciare con quelli risultanti dall'ultima revisione effettuata → questi poi si modificano ad ogni revisione, anche quelle che farete per preparare il corpo elettorale: si consiglia di controllare che i totali combacino.

Questa è poi quella che vi ritroverete nell'estratto liste sezionali da stampare e consegnare ai seggi.

---

## Variazioni in base al tipo di elezione

**NB:** il prospetto forza votante cambia a seconda del tipo di elezione (vedi **Tipo Elezioni**), quindi le variazioni possono riguardare:

- La gestione degli AIRE (UE, EXTRAUE) se votano o meno in Italia
- La presenza di liste aggiunte europee o nazionali (Val d'Aosta, Trento, Bolzano)
- La gestione degli elettori che non avranno compiuto il 18esimo anno di età alla data delle elezioni

---

## Esempio: Elezioni Europee

[Schermata del prospetto forza votante per Elezioni Europee (Mod. XVI) con colonne: Sezione, Liste elettorali (M/F/T), Minorenni (M/F/T), AIRE voto estero (M/F/T), UE Parlamento Europee (M/F/T), Forza votante (M/F/T)]

- In **VERDE** e **ROSSO**, le liste elettorali interessate dall'elezione che formano il **TOTALE CORPO ELETTORALE** come indicato nella tabella tipi elezioni per il tipo EUROPEE.
- In **BLU** gli AIRE ed i Minorenni, che nel tipo elezioni corrispondono ai FLAG della composizione prospetto (verde):

[Schermata della "Tabella Tipo Elezioni" per Elezioni Europee (ID 5, Età da 18, Età a 999) con:
- Corpo elettorale: 1 - Liste Elettorali, tipo lista 2: 3 - UE Parlamento Europee
- Composizione prospetto: Liste elettorali ✓, AIRE vota estero ✓, Totale lista aggiunta ✓, Senato + Camera ✓, Minorenni ✓, Totale elettori ✓, Ogni lista aggiunta ✓, Forza votante ✓]

---

## Esempio: Elezioni Amministrative

Lo stesso ragionamento, con dati diversi, vale per le **amministrative**:

[Schermata della "Tabella Tipo Elezioni" per Amministrative (ID 6, Età da 18, Età a 999) con:
- Corpo elettorale: 1 - Liste Elettorali, tipo lista 2: 5 - UE Comunali, tipo lista 3: 7 - provincia di Bolzano, tipo lista 4: 4 - Regione Valle d'Aosta
- Composizione prospetto: Liste elettorali ✓, AIRE vota estero ☐, Totale lista aggiunta ✓, Senato + Camera ☐, Minorenni ✓, Totale elettori ✓, Ogni lista aggiunta ✓, Forza votante ✓]

Il suo prospetto forza votante sarà:

[Schermata del prospetto forza votante per Amministrative (Mod. XVI) con colonne: Sezione, Liste elettorali (M/F/T), Minorenni (M/F/T), UE Comunali (M/F/T), provincia di Bolzano (M/F/T), Regione Valle d'Aosta (M/F/T), Forza votante (M/F/T)]

Le liste in **giallo** combaciano col corpo elettorale in tabella e rimane la gestione minorenni. Non è presente la gestione degli AIRE in quanto per le amministrative devono venire in Italia a votare.