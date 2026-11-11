# Attribuzione Numero a Famiglia Eliminata

Questo programma permette di avere un elenco di tutte quelle **scheda famiglia** che sono state eliminate in un dato periodo di tempo ed inoltre di poterle numerare sulla tabella di riferimento, quindi conferire un **progressivo di eliminazione**.

## Contenuto dell'elenco prodotto

L'elenco che viene prodotto riporta:

- Il **tipo famiglia** (AN, FE, CV, TE)
- Il **codice famiglia**, quindi il progressivo, che assieme al tipo forma la combo che identifica nella vostra anagrafe la famiglia
- Le **date di istituzione e di cessazione** della famiglia
- Il **nominativo dell'intestatario scheda**

## Percorso di accesso

Il programma si trova all'interno del gruppo anagrafe dei servizi demografici ed è raggiungibile seguendo il percorso:

- **150-10-30-140**
- **Servizi Demografici** → **Anagrafe** → **Variazioni** → **Attribuzione numero a famiglia eliminata**

[Schermata del menu di navigazione: 150. Servizi Demografici → 30. Anagrafe → 30. Variazioni → 140. Attribuzione numero a famiglia eliminata]

## Interfaccia del programma

Una volta selezionato il programma si apre con una videata semplice: permette l'inserimento del **periodo di tempo** che viene usato come parametro per estrarre tutte quelle scheda famiglia istituite e cessate. Premendo su **Stampa** si procede alla creazione del file.

[Schermata del programma: campo "Data inizio" (es. 01/01/2023), campo "Data fine" (es. 31/12/2023), pulsanti "Stampa" e "Annulla"]

## Output: file Excel

Il file Excel prodotto riporta i dati come mostrato di seguito.

### Esempio di output

| TIPO FAMIGLIA | CODICE FAMIGLIA | DATA ISTITUZIONE FAMIGLIA | DATA ELIMINAZIONE FAMIGLIA | INTESTATARIO FAMIGLIA |
|---|---|---|---|---|
| AN | *(progressivo)* | 1928-01-19 | 2023-01-03 | *(nominativo)* |
| *(tipo)* | 1302 | 1928-04-27 | 2023-07-21 | *(nominativo)* MARIA |
| *(tipo)* | *(codice)* | 1955-02-01 | 2023-01-02 | *(nominativo)* ROBERTO |
| *(tipo)* | *(codice)* | *(data)* | 2023-07-21 | *(nominativo)* INES |

> **Nota:** I dati nell'esempio sono stati oscurati per motivi di privacy. Le colonne riportano: tipo famiglia, codice/progressivo, data di istituzione, data di eliminazione e nominativo dell'intestatario.