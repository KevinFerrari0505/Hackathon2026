# Rinumerazione Civica

## (o problemi di numerazione)

**Riferimenti utili:** Regolamento anagrafe DPR 30 maggio 1989, n.223 Articoli 38 – 45:

- Obbligo di nome univoco per ogni area di circolazione
- Obbligo di numerazione civica esterna sull'area di circolazione
- Obbligo di numerazione civica interna per gli accessi alle abitazioni/attività
- Obbligo di domanda del proprietario, di avere il civico prima che sia finita la costruzione
- Obbligo di seguire le indicazioni ISTAT

L'ISTAT ha indicato in un volume *"Anagrafe della popolazione – metodi e norme – serie B n.29 – edizione 1992"* ISSN 0075-1847, un capitolo *"Istruzioni per l'ordinamento ecografico"* con le indicazioni metodologiche.

---

## CASO 1: Cambio Denominazione Via

**Esempio:** L'attuale "Via Azzurra" diventa "Viale Azzurro"

### Ecco come modificare:

Aprire la tabella delle vie dal punto di menù:

```
Servizi Economici > Modulo Base > Tabelle Generali > Viario > Vie
```

Nella finestra sarà possibile ricercare direttamente la via desiderata oppure cliccare **→ Elenca** per vederle tutte, e cercare poi nel campo 'descrizione'.

[Screenshot: Finestra di ricerca "Vie" con campi Descrizione, Toponimo, Codice da/a, Codice Ente e pulsanti Nuovo, Elenca, Carica, Salva, Reset]

Una volta individuata la via, vado in modifica tramite l'apposita 'matitina' ed inserisco la data della delibera di modifica come **data di fine** su "Via Azzurra" → **Aggiorna**

[Screenshot: Tabella vie con la riga "Potenza Picena-VIA AZZURRA" evidenziata e l'icona matita cerchiata in rosso]

Il programma cessa automaticamente alla stessa data tutti i civici e interni collegati che risultavano attivi. Per sincerarsi del fatto, basta cliccare il bottone **Civici**, che aprirà una finestra con tutti i civici collegati a quella via.

[Screenshot: Scheda di modifica via con campo "Data fine" impostato a 10/04/2024 e pulsante "Aggiorna" evidenziato]

[Screenshot: Finestra "Numeri civici" con elenco dei civici collegati alla via (codice via 13, VIA AZZURRA) con data fine 10/04/2024]

Dopo di ché, passo ad inserire la nuova via (**→ Nuovo**), prestando attenzione alla data di inizio e al collegamento storico (campo "codice via originale") → **Aggiungi**

[Screenshot: Scheda di nuova via con Codice via 900022, Toponimo "viale", Descrizione "Azzurro", Data inizio 10/04/2024, Codice Via Originale 13 VIA AZZURRA, pulsante "Aggiungi" evidenziato]

> **Nota:** Non esiste invece automatismo per la duplicazione dei civici dato che sono spesso soggetti a diversa numerazione.

### Inserimento dei nuovi numeri civici

Il procedimento corretto è quindi quello di entrare nella tabella dei Civici tramite il punto di menu:

```
Servizi Demografici → Modulo Base → Tabelle Generali → Viario → Numeri Civici → Nuovo
```

[Screenshot: Finestra "Numeri civici" con campi di ricerca e pulsante "Nuovo" evidenziato]

Nel nostro esempio "Via Azzurra" parte dal numero 1. Decidiamo di farlo diventare il numero 2 di "Viale Azzurro" per cui compileremo la videata così → **Aggiungi**

[Screenshot: Scheda nuovo numero civico con Codice via 900022 Viale Azzurro, Numero civico 2, Tipo 3 Abitazione, Agibilità 1-Agibile, Data inizio 20/04/2024, Progressivo originale 1 con riferimento VIA AZZURRA 1, pulsante "Aggiungi" evidenziato]

L'effetto di queste operazioni sul viario è che la vecchia denominazione di "Via Azzurra 1" la vedo cessata sul viario, mentre vedo attiva al nuovo indirizzo di "Viale Azzurro 2" (e così via per tutti gli altri numeri civici):

[Screenshot: Tabella Numeri civici con ricerca "azzur" che mostra le righe VIA AZZURRA con data fine 10/04/2024 (evidenziate in giallo) e la nuova riga Viale Azzurro n.2 con data inizio 20/04/2024]

### Aggiornamento in anagrafe locale

Si dovrà, prima, effettuare un **Interrogazione Anagrafica** per il codice della vecchia via, estrapolando tutte le famiglie presenti, e predisporre poi la pratica di **Variazione Domicilio Intero Nucleo Familiare** dalla data della delibera, ed inviare poi le comunicazioni del cambio effettuato.

---

## CASO 2: Ubicazione errata, erroneamente dichiarata

**Esempio:** è presente in tabella l'indirizzo "via verdi 3 bis", che però non esiste, il corretto è "via verdi 3/b".

### Ecco come modificare

Se il 3 bis è inesistente, va **cessato** nella tabella dei civici. (Inserendo anche una nota con la spiegazione di quello che è successo).

Questo perché, si può fare una correzione che non storicizza nulla, ma in genere si preferisce invece storicizzare in quanto potrebbero essere stati effettuati dei certificati al 3bis anche se errato; in questo modo, dal punto di vista storico l'indirizzo errato resta memorizzato sino alla data della correzione. (Se ho delle pratiche in corso a 3bis, le cambio d'ufficio al 5).

In elettorale, l'indirizzo viene corretto normalmente o con **extrarevisione** o con **revisione**, a seconda che cambi o meno la sezione.