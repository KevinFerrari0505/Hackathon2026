# Statistica per età e sesso

## Parametri di configurazione

### Tipo

È possibile effettuare una statistica della popolazione:

- **Apr** – Residente (APR)
- **Aire** – Anagrafe Italiani Residenti all'Estero
- **Temporanei** – Temporaneamente iscritti in anagrafe per massimo un anno per la richiesta del medico

### Includi

Selezionando o deselezionando le checkbox è possibile includere o escludere:

- Italiani
- Extracomunitari
- Comunitari

### Alla data

La statistica può essere riferita a:

- **Odierna** – data corrente
- **Richiesta** – una data specifica (di solito molto utilizzata per la popolazione a fine anno)

### Controlla eventuali anomalie statistiche e le riporta su file excel

Se selezionata, eventuali anomalie riscontrate su alcuni soggetti verranno scaricate in un file Excel.

## Esecuzione della statistica

Premendo il tasto **ELABORA** verrà prodotto il grafico e sulla destra apparirà il tasto **Apri Estrazioni** con il quale verranno prodotti 2 file da scaricare:

1. **StatisticheEtaSesso.xlsx** – contenente la statistica richiesta suddivisa per età e sesso
2. **Anomalie.xlsx** – contenente le anomalie da sanare

## Output generato

### StatisticheEtaSesso.xlsx

Il file contiene una tabella con le seguenti colonne:

| Colonna | Descrizione |
|---------|-------------|
| ETA | Età del soggetto |
| Femmine | Numero di femmine per età |
| Maschi | Numero di maschi per età |
| Totale | Somma di femmine e maschi |

Nella riga di intestazione (riga 1) viene riportata la selezione effettuata, ad esempio:

> Selezione: Tipo: Apr - Include: italiani, extracomunitari, comunitari alla data odierna 28-02-2022

### Anomalie.xlsx

Il file contiene un elenco dei soggetti che presentano anomalie da sanare, con le seguenti colonne:

| Colonna | Descrizione |
|---------|-------------|
| Anomalie | Descrizione dell'anomalia |
| Sesso | Sesso del soggetto |
| Cognome | Cognome |
| Nome | Nome |
| Data Nascita | Data di nascita |
| Tipo | Tipo di anomalia |
| Famiglia | Numero di famiglia |
| Stato | Stato civile |
| Anomalia | Dettaglio dell'anomalia (es. "Famiglie attive su DAN_FAMI e invece cancellate in anag") |

## Interfaccia

[Schermata della finestra "Statistiche per età e sesso" con i campi: Tipo (Apr/Aire/Temporanei), Includi (Italiani/Extracomunitari/Comunitari), Alla data (Odierna/Richiesta) e la checkbox "Controlla eventuali anomalie statistiche e le riporta su file excel"]

[Schermata del risultato: grafico a barre con distribuzione per età e sesso (Femmine/Maschi) e pulsanti "Elabora", "Chiudi" e "Apri Estrazioni" sulla destra]

[Schermata del pannello "Files" con i due file generati: StatisticheEtaSesso.xlsx e Anomalie.xlsx]