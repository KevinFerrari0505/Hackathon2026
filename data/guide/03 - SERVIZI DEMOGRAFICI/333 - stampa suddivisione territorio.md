# Stampa suddivisione territorio in sezioni

Dal menù **Servizi Demografici → Elettorale → Elettorale → Stampe → Stampa suddivisione territorio** in sezioni è possibile generare una stampa della ripartizione del territorio in sezioni elettorali.

Questa funzione genera un elenco diviso per sezione elettorale con la suddivisione delle varie vie del territorio.

## Definizione della suddivisione

La suddivisione del territorio in sezioni viene definita tramite gli elementi del **Viario**.

Il codice elemento (fisso) delle sezioni elettorali è il **5**.

È qui permesso di cambiare questo codice, perché può essere utile durante la fase di risuddivisione del territorio in sezioni, andare a stampare la nuova suddivisione del territorio. Suddivisione che si sta ancora definendo, e che quindi temporaneamente è caricata su un codice diverso dal 5.

## Parametri di stampa

È possibile cambiare le due **intestazioni** per la stampa e scegliere anche il **metodo di conteggio** da utilizzare.

### Opzioni di conteggio

- **Senza nessun conteggio**: si ottiene la stampa senza nessun conteggio del numero di elettori.
- **Elettori**: nell'elenco delle vie associate ad ogni sezione ci sarà anche il numero di elettori presenti in quella via.
- **Da copia elettorale**: il conteggio avverrà non dall'Elettorale, ma dalla copia di lavoro usata per la ricompilazione delle liste.

> ⚠️ La scelta "Da copia elettorale" deve essere indicata solamente nel menù della ricompilazione liste.

## Generazione del report

Dopo aver impostato i vari parametri premere **Stampa** per generare il report.

[Interfaccia "Stampa Suddivisione Territorio": campo Elemento con dropdown "5 - SEZIONI ELETTORALI", campo Intestazione 1 (es. "Suddivisione territorio in Sezioni"), campo Intestazione 2, sezione "Conteggio" con dropdown "Seleziona il conteggio da utilizzare" con opzioni: Nessun conteggio / Elettori / Da copia elettorale, pulsante Stampa]

## Esempio di report

Esempio di report con codice elemento default. Sono stati compilati entrambi i campi delle intestazioni ed è stato scelto il conteggio "Elettori".

### Suddivisione territorio in Sezioni — Intestazione 2

**Comune di** [nome comune] — 22-11-2022

#### SEZIONE 1

| Via | Pari/Dis | Da | A | Tot M | Tot F | Tot M F |
|-----|----------|----|----|-------|-------|---------|
| 125 via a. fogazzaro | T | | 999999 | 41 | 46 | 87 |
| [via] | | | | | | |
| 30 via belluno | T | | 999999 | 29 | 35 | 64 |
| 50 via brescia | T | | 999999 | 26 | 31 | 57 |
| 10 via d. alighieri | T | | 999999 | 28 | 24 | 52 |