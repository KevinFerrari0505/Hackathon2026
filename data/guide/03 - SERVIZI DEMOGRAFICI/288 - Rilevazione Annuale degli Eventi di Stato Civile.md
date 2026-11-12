# Rilevazione Annuale degli Eventi di Stato Civile

La Rilevazione annuale degli eventi demografici di stato civile è effettuata attraverso il modello **D.7.A** e riguarda il conteggio dei seguenti atti relativi alla popolazione presente:

- Nascite (distinte per vitalità, filiazione e genere del parto)
- Morti
- Matrimoni
- Accordi extra-giudiziali di negoziazione assistita dagli avvocati ex art. 6
- Accordi extra-giudiziali conclusi e confermati direttamente di fronte all'Ufficiale di Stato civile ex art. 12
- Unioni civili
- Provvedimenti delle autorità giudiziarie

## Novità a partire dalla rilevazione dell'anno 2024

A partire dalla rilevazione dell'anno 2024, il modello di rilevazione Istat D.7.a annuale presenta le seguenti novità:

1. **Non vengono più richieste** le variazioni delle condizioni degli accordi ex art. 6 ed ex art. 12 (punti 6.3 e 7.3).
2. Ai punti 6.3 e 7.3 vanno indicati, invece, gli **scioglimenti di unione civile** (ex art. 6 ed ex art. 12).
3. È stata aggiunta la **sezione 9** relativa ai Provvedimenti delle autorità giudiziarie.

Nella sezione 9 vanno riportati:

- **Punto 9.1** – Provvedimenti di separazione
- **Punto 9.2** – Divorzio
- **Punto 9.3** – Scioglimento di unione civile

emessi dalle autorità giudiziarie italiane e da queste trasmessi al Comune per le annotazioni sull'atto di matrimonio o di unione civile.

> **Nota:** Le sentenze ecclesiastiche di nullità di matrimonio pronunciate dal Tribunale Ecclesiastico, per il riconoscimento civile nello Stato italiano devono essere delibate dalla Corte d'Appello competente e pertanto vanno conteggiate nel punto 9.2.

## Schema di riferimento degli eventi

Nello schema seguente si riassumono le date di riferimento degli eventi da conteggiare nel modello.

| Evento | Data di riferimento per il conteggio nel modello |
|--------|--------------------------------------------------|
| Nascita | Nascite avvenute dal 1° gennaio al 31 dicembre |
| Decesso | Decessi avvenuti dal 1° gennaio al 31 dicembre |
| Matrimonio | Matrimoni celebrati dal 1° gennaio al 31 dicembre |
| Unione civile | Unioni civili costituite dal 1° gennaio al 31 dicembre |
| Accordi extragiudiziali ex art. 6 | Accordi trascritti dal 1° gennaio al 31 dicembre |
| Accordi extragiudiziali ex art. 12 | Accordi registrati per la conferma definitiva dal 1° gennaio al 31 dicembre |
| Provvedimenti delle autorità giudiziarie italiane | Provvedimenti annotati dal 1° gennaio al 31 dicembre |

## Estrazione delle statistiche D7A

È possibile estrarre le statistiche del D7A annuali dal punto di menù:

**Servizi Demografici → Stato Civile → Altre operazioni → Statistiche → Rilevazione annuale degli eventi di Stato Civile (Istat D7A)**

L'unica cosa che richiede la finestra è l'**anno di estrazione**, quindi → **Esporta**

[Schermata: finestra "Rilevazione annuale degli eventi di Stato Civile (Istat D7A)" con campo "Anno*" (es. 2024) e pulsante "Esporta"]

Il programma esporterà in un file `.csv` (file da **NON APRIRE** e da importare poi su **GINO**) i dati dando il seguente messaggio:

> ⚠️ Attenzione: il file D7A_2024.csv verra' scaricato nella cartella Download.

E allo stesso tempo eseguirà un'**anteprima in Excel** dei dati estratti.

## Lettura dei dati nella piattaforma GINO

Come vengono letti questi dati dalla piattaforma GINO? Ecco un file di esempio:

[Anteprima Excel: "Comune di Potenza Picena – Rilevazione annuale degli eventi di Stato Civile – D7A Annuale – Anno 2024" con colonne MASCHI, FEMMINE, TOTALE e righe da 1. Nati vivi a 5. Matrimoni]

Il **punto 1.1** è la somma dei punti **1.1.1** e **1.1.2**, mentre il **punto 1.2** viene conteggiato a parte, quindi poi si dovrà controllare che al **punto 3** corrispondano gli stessi numeri.

### Struttura del file di esempio (sezioni principali)

| Rif. | Descrizione | MASCHI | FEMMINE | TOTALE |
|------|-------------|--------|---------|--------|
| 1. | Nati vivi | | | |
| 1.1 | dichiarati direttamente all'Uff. di stato civile (1.1.1+1.1.2) | | | |
| 1.1.1 | di cui nati nel territorio del Comune | 0 | 0 | 0 |
| 1.1.2 | di cui nati nel territorio di un altro Comune | 7 | 9 | 16 |
| 1.2 | dichiarati alla Direzione sanitaria del centro di nascita | 1 | 2 | 3 |
| 1.3.1 | di cui da genitori almeno uno dei quali straniero | 0 | 0 | 0 |
| 2. | Nati morti | | | |
| 2.1 | all'interno del matrimonio | 1 | 0 | 1 |
| 2.2 | al di fuori del matrimonio o filiaz. ignota | 1 | 1 | 2 |
| 2.3.1 | di cui da genitori almeno uno dei quali straniero | 0 | 0 | 0 |
| 3. | Nati vivi all'interno o fuori matrimonio/Nati da parti plurimi | | | |
| 3.1 | Nati vivi all'interno del matrimonio | 4 | 6 | 10 |
| 3.2 | Nati vivi al di fuori del matrimonio o filiazione ignota | 1 | 5 | 6 |
| 3.3 | Nati (sia vivi sia morti) da parti plurimi | 0 | 0 | 0 |
| 4. | Morti | | | |
| 4.1 | Nel 1° anno di vita | 0 | 0 | 0 |
| 4.2 | Oltre il 1° anno di vita | 8 | 6 | 14 |
| 4.3.1 | di cui di cittadinanza straniera | 0 | 1 | 1 |
| 5. | Matrimoni | | | |

> **Verifica:** controllare che la somma dei punti 3.1 + 3.2 + 3.3 corrisponda ai totali del punto 1.1 (somma di 1.1.1 e 1.1.2) più il punto 1.2.