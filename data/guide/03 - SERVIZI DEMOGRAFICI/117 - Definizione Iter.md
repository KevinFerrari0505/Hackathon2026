# Definizione Iter

Un **ITER** rappresenta il flusso operativo di una pratica: definisce i passi, gli esiti, gli utenti o uffici coinvolti e le regole di avanzamento fino alla chiusura.

## Accesso al modulo

All'apertura del punto di menu: **Servizi Demografici → Modulo Base → Iter → Definizione iter**

Appare la schermata di tutti gli Iter presenti per le pratiche all'interno del programma.

- Dal codice **100000 in avanti** sono gli **iter standard** forniti dalla softwarehouse.
- **Sotto al 100000** invece, sono **iter personalizzati** direttamente dal cliente.

## Creazione di un nuovo iter

È possibile creare un nuovo iter personalizzato partendo da zero, cliccando il bottone → **Nuovo**, oppure duplicare un iter standard e poi personalizzarlo.

### Duplicazione di un iter standard

Per la spiegazione di come personalizzare un iter e collegare i testi ai suoi passi o esiti, partiremo ad esempio con la duplicazione dell'iter di una pratica di immigrazione:

1. Selezionare con un click l'iter desiderato.
2. Cliccare il bottone → **Duplica**.

[Schermata "Definizione Iter" con elenco iter e pulsante "Duplica" evidenziato]

Apparirà una finestra pop-up che indica:
- Il **codice iter attribuito** (codice assegnato direttamente dal programma, non modificabile)
- Il campo per la **descrizione del nuovo iter**

Premere poi il bottone → **Conferma**.

[Finestra pop-up "Duplicazione Iter" con campi "Codice Iter Attribuito" e "Descrizione Nuovo Iter"]

## Visualizzazione della struttura

A questo punto, selezionare con un click l'iter appena duplicato e cliccare nel bottone → **Struttura** per poter vedere tutte le sequenze dei passi con i relativi esiti e gli eventuali passi successivi.

[Schermata "Definizione Struttura Iter" con tabella: seq. Passi, Esiti, Passo Successivo, Chiude]

Nella struttura sono presenti:
- L'icona dell'**occhio** per visualizzare quel passo
- L'icona della **matita** per modificare quel passo
- Un **check** se quel passo chiude l'intero iter della pratica
- Il bottone **Nuovo** per aggiungere ulteriori passi

## Modifica di un passo

Cliccando la **matita** su un passo è possibile modificarne l'esito ed il passo successivo, ed agganciare i testi a quel passo o all'esito.

**Esempio:** prendendo il passo *domanda*, i possibili esiti possono essere:

| Esito | Passo Successivo |
|-------|-----------------|
| Domanda Accolta | Avvio Procedimento |
| Irricevibile | Pratica annullata |

[Schermata "Struttura Iter" con passi: Domanda → Domanda Accolta → Avvio Procedimento; Domanda → Irricevibile → Pratica annullata]

### Tab "Definizione"

Aprendo la finestra in modifica, il primo tab che il programma mostra è la **definizione** di quel passo (es. il passo *domanda*), con i relativi testi già associati, con possibilità di:
- Inserire nuovi testi tramite il bottone **Inserisci Doc**
- Eliminare testi esistenti tramite il bottone **Elimina Doc**

[Schermata tab "Definizione" con campi: Sequenza passi, Giorni previsti, Giorni da non visualizzare, e sezione "Testi associati"]

### Tab "Autorizzazione"

Spostandosi nel tab **Autorizzazione** è possibile decidere il tipo di autorizzazione in consultazione della pratica:

- **Pubblica**: chiunque può consultare la pratica in tutti i suoi passi.
- **Elenco uffici o utenti**: occorre specificare (in una finestra che appare solo quando è selezionata questa opzione) i singoli utenti autorizzati a consultare la pratica. A tutti gli altri, la consultazione sarà impedita.

[Schermata tab "Autorizzazione" con opzioni radio "Elenco Ufficio o Utenti" e "Pubblica", e sezione "Audit"]

### Tab "Esiti"

Spostandosi nell'ultimo tab **Esiti**, si vedono gli esiti già previsti per quel passo, con la possibilità di:
- Inserire nuovi esiti tramite il bottone **Inserisci**
- Modificare esiti esistenti tramite il bottone **Modifica**
- Eliminare esiti tramite il bottone **Elimina**

**Esempio:** se il passo è la *domanda* ricevuta, gli esiti possibili potrebbero essere *irricevibile* o *domanda accolta*.

Andando in modifica di un esito, il programma aprirà una finestra dove sarà possibile gestire quell'esito, ovvero:

- Decidere se è l'ultimo esito, che quindi chiude tutto l'iter, ponendo il check in **Chiude iter**
- Definire il **passo successivo**
- Associare o cancellare i **testi associati** all'esito tramite i bottoni **Inserisci** e **Elimina**

[Schermata "Assegnazione Esiti al Passo di Iter" con campi: Iter, Passo, Esito, Chiude iter, Disabilitato, Passo successivo (Codice iter, Passo), Nome metodo, Testi associati]

Una volta definito, aggiornare tramite il bottone → **Aggiorna**.