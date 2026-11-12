# Estrazione soggetti aggiunti per TELELEVA

Questa funzione permette di creare il file **TELELEVA** riguardo i soggetti aggiunti, che vengono estratti in precedenza con causale **"Acquisto Cittadinanza Italiana"**.

## Percorso di navigazione

Il percorso da seguire è il seguente:

**Servizi Demografici ⇒ Leva Militare ⇒ Conferma Lista di Leva ⇒ Estrazione soggetti aggiunti per TELELEVA**

[Schermata del menu a cascata del software: Servizi Demografici → Leva Militare → Conferma Lista di Leva → 40. Estrazione soggetti aggiunti per Teleleva]

## Parametri di compilazione

Entrando all'interno, bisognerà indicare l'**anno di competenza**.

L'anno da indicare fa riferimento a ciò che è stato indicato nel precedente programma, utilizzato per effettuare l'estrazione di coloro che hanno acquistato la cittadinanza italiana.

Quindi se ho estratto tutti i soggetti che nel 2024 hanno acquistato la cittadinanza, nella creazione del file TELELEVA indicherò l'anno **2007**.

### Tabella di conversione anno estrazione → anno di competenza

| Anno estrazione cittadinanza | Anno di competenza da indicare |
|------------------------------|-------------------------------|
| 2025                         | 2008                          |
| 2024                         | 2007                          |
| 2023                         | 2006                          |
| 2022                         | 2005                          |
| ...                          | ...                           |

### Campi del modulo

[Schermata del modulo "Estrazione soggetti aggiunti per Teleleva" con i seguenti campi:]

- **Anno di competenza**: campo di testo (es. `2007`)
- **Solo attivi**: checkbox
- **Nominativo referente**: campo di testo

## Conferma ed esito

Una volta compilati i campi, premere sulla destra **"Conferma"** e verrà prodotto il file TELELEVA in un formato **txt**.

Esempio di file generato: `TeleLeva20250217172414.txt`