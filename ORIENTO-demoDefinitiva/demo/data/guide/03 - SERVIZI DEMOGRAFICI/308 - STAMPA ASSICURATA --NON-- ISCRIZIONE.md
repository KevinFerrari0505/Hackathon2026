# STAMPA ASSICURATA **NON** ISCRIZIONE

Il programma permette di generare e stampare l'**assicurata NON iscrizione** da inviare al comune nel quale il soggetto è **EMIGRATO**.

## Percorso di navigazione

**Servizi demografici** ⇒ **Leva militare** ⇒ **Preparazione lista di leva** ⇒ **Stampa assicurata NON iscrizione**

[Schermata del menu di navigazione: dal menu principale si seleziona "150. Servizi Demografici" → "40. Leva Militare" → "10. Preparazione Lista di leva" → "60. Stampa assicurata NON iscrizione"]

## Compilazione dei campi

Per procedere alla stampa bisogna compilare i campi nel seguente modo:

- **Anno di competenza**;
- **Causale di cancellazione** ⇒ Che posso **sempre** andare a consultare nel programma di Gestione (*Gestione Iscritti*);
- Inserire il relativo testo (il testo da utilizzare è il seguente `cwd_LevaAssicuratanoniscrizione`).

[Schermata del form "Stampa assicurata non iscrizione": campo "ANNO DI COMPETENZA" con valore 2006, campo "CAUSALE DI CANCELLAZIONE" con valore "Emigrat", campo "CODICE TESTO" con valore "cwd_LevaAssicurata", pulsante "Stampa" e pulsante "Protocolla"]

## Output

Una volta compilati i campi e premuto il bottone **"Stampa"**, il programma effettua l'estrazione e carica i file all'interno di una cartella `.zip` (dove all'interno saranno presenti tutti i file che devono essere inviati ai comuni in formato **DOCX**).

Mentre se si preme il bottone **"Protocolla"**, quest'ultimi verranno trasformati in **PDF**.