# Statistiche per Fasce di Età

Permette di ottenere la statistica divisa per età (anno corrente - anno di nascita) e sesso, degli iscritti APR, oppure dei soli stranieri iscritti APR, oppure degli AIRE, ecc…

[Schermata dell'interfaccia "Statistiche per fasce di età" con i campi: Tipo (Apr, Aire, Temporanei), Includi (Italiani, Extracomunitari, Comunitari), Alla data (Odierna, Richiesta) e la tabella Fascia di età con righe da 0-14, 15-29, 30-44, 45-64, 65-90, 91-999 e ulteriori righe personalizzabili]

## Tipo

Selezionare il Tipo Anagrafe da elaborare.

## Includi

E' attivo solo se selezionato **Apr**. Permette di includere nella statistica, solo la categoria desiderata:

- **tutti** (selezionare tutti e 3 i checkbox)
- italiani
- stranieri (comunitari + extracomunitari)
- comunitari (la statistica si basa sul gruppo nazionalità indicato ai cittadini)
- extracomunitari (la statistica si basa sul gruppo nazionalità indicato ai cittadini)

## Richiesta

- Se indicata la **data odierna**, ottenete la situazione attuale dell'Anagrafe selezionata.
- Se viceversa richiesta una **specifica data**, il programma risale alla situazione storica alla data richiesta, basandosi sugli eventi (data evento e non data perfezionamento) registrati.

## Fascie di età

Vengono proposte quelle memorizzate nella **Tabella Personalizzazione CITY-PEOPLE**.

Si possono modificare, e in questo caso, la selezione corrente non sostituisce quella pre-impostata sulla tabella di personalizzazione.

## Elaborazione

Premendo il tasto **ELABORA** verrà prodotto il grafico e sulla destra apparirà il tasto **Apri Estrazioni** con il quale verrà prodotto 1 file da scaricare (`StatisticheFasceEta.xlsx`) contenente quanto richiesto.

[Bar chart a raggruppamento con legenda "Femmine" (viola) e "Maschi" (azzurro) che mostra la distribuzione della popolazione per fascia di età]

## Esempio di output (StatisticheFasceEta.xlsx)

| | A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|---|
| **1** | | | | | | | |
| **2** | Fasce d'età | Femmine | Maschi | Totale | Perc M. | Perc F. | Perc Tot. |
| **3** | 0 - 14 | 234 | 241 | 475 | 12,18 | 10,86 | 11,50 |
| **4** | 15 - 29 | 278 | 248 | 526 | 12,54 | 12,91 | 12,73 |
| **5** | 30 - 44 | 369 | 326 | 695 | 16,48 | 17,13 | 16,82 |
| **6** | 45 - 64 | 664 | 654 | 1318 | 33,06 | 30,83 | 31,90 |
| **7** | 65 - 90 | 556 | 495 | 1051 | 25,03 | 25,81 | 25,44 |
| **8** | 91 - 999 | 53 | 14 | 67 | 0,71 | 2,46 | 1,62 |
| **9** | **Tot. Popolaz.** | **2154** | **1978** | **4132** | | | |

> **Nota:** L'intestazione dell'estrazione riporta: *Estrazione Tipo: Apr - Include: italiani,extracomunitari,comunitari alla data 28-02-2022*