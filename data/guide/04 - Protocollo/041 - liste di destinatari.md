# Liste di destinatari

Se si ha bisogno di avere a disposizione diversi gruppi di destinatari a cui inviare comunicazioni, è necessario creare un file Excel con determinate caratteristiche.

## Creazione del file Excel

1. Aprire un nuovo file Excel e selezionare una qualsiasi cella; cliccare il tasto destro e scegliere **Formato celle…**.

2. Nella tab *Numero*, in *Categoria* selezionare **Testo** e confermare cliccando **OK**.

## Struttura delle colonne

Nelle colonne del foglio di calcolo inserire i dati secondo la seguente struttura:

| Colonna | Dato | Obbligo |
|---------|------|---------|
| A | Nome del destinatario (Ente, privato, nome e cognome, ecc.) | **OBBLIGATORIO** |
| B | Indirizzo | FACOLTATIVO |
| C | Nome della città | FACOLTATIVO |
| D | Provincia | FACOLTATIVO |
| E | CAP | FACOLTATIVO |
| F | Indirizzo mail/PEC | **OBBLIGATORIO** |

### Controlli automatici del programma

Il programma effettuerà un controllo sui dati inseriti:

- La **provincia** (campo D) deve essere di **due lettere**.
- La **mail** (campo F) deve contenere la **@** e un **dominio valido**.

### Esempio di dati inseriti

| A | B | C | D | E | F |
|---|---|---|---|---|---|
| Italsoft | via Paganini, 57 | Potenza Picena | MC | 62018 | certificata@pec.italsoft-mc.it |
| Chiara Cognigni | via Paganini, 57 | Potenza Picena | MC | 62018 | chiara.cognigni@italsoft.it |
| Alessandro Mucci | via Paganini, 57 | Potenza Picena | MC | 62018 | alessandro.mucci@italsoft.eu |

## Salvataggio del file in formato CSV

1. Dopo aver inserito tutti i destinatari della lista, scegliere **Salva con nome**.

2. Scegliere dove salvare il file (è consigliabile salvarlo in una **cartella condivisa**, così che anche gli altri utenti possano utilizzarla); rinominarlo e in *Salva come:* selezionare **CSV**.

3. Alla domanda di Excel, rispondere **Sì**.

La lista è stata creata.

### Salvataggio con LibreOffice

Per chi utilizza **LibreOffice**, in fase di salvataggio del file come CSV, va anche spuntata la voce **"Modifica impostazioni filtro"**.

Successivamente, nella finestra *Esportazione file di testo*, configurare le seguenti opzioni:

- **Separatore di campo:** punto e virgola (`;`)
- **Delimitatore di stringa:** virgolette (`"`)
- Spuntare la voce **"Virgolette su tutte le celle di testo"**

## Caricamento della lista nel protocollo

Per caricare una lista di destinatari nel protocollo in partenza, spostarsi nella tabella **Altri Dest.** e cliccare l'icona **Importa CSV**.

1. Cliccare sull'icona di acquisizione file per poter scegliere il file da caricare.

2. Scegliere il file `.csv`.

3. La lista verrà caricata nella tabella *Altri Dest.* con le colonne: Descrizione, Email-PEC, Indirizzo, Città, Cc, Mail, Acc., Cons., Not. P, Sbl.