# Statistiche per Cittadinanza e Fasce di Età

Permette di ottenere la statistica divisa per età (anno corrente - anno di nascita) e sesso, degli stranieri iscritti APR suddivisi per cittadinanza.

## Interfaccia di richiesta

[Schermata del modulo "Statistiche stranieri per cittadinanza e sesso" con sezione "Alla data" (opzioni: Odierana / Richiesta con campo data) e sezione "Fasce Età" con i seguenti intervalli:]

| Fascia | Da | A |
|--------|----|----|
| Età da | 0 | 14 |
| Età da | 15 | 29 |
| Età da | 30 | 44 |
| Età da | 45 | 64 |
| Età da | 65 | 90 |
| Età da | 91 | 999 |
| Età da | 0 | 0 |
| Età da | 0 | 0 |
| Età da | 0 | 0 |
| Età da | 0 | 0 |

## Richiesta

La statistica può essere riferita alla **data odierna** oppure ad una **data richiesta** (di solito molto utilizzata per la popolazione a fine anno).

Premendo il tasto **ELABORA** verrà prodotto il grafico e sulla destra apparirà il tasto **Apri Estrazioni** con il quale verrà prodotto il file da scaricare.

[Schermata del Visualizzatore Documenti con il file generato e i pulsanti "Protocolla" e "Scarica"]

## Output

Il file generato (es. `StatisticheCittadinanzaFasceEta_28_02_2022.xlsx`) contiene:

- La statistica richiesta suddivisa per **Cittadinanza** e **sesso**
- Un Excel con il **riepilogo** e il **dettaglio per ogni continente**

[Schermata del foglio Excel di output: "Popolazione stranieri suddivisi per età e sesso al 28_02_2022" con colonne: Nazioni, Femmine, Maschi, Totale, e colonne per fascia d'età (da 0 a 14, da 15 a 29, da 30 a 44, da 45 a 64, da 65 a 90, da 91 a 999). Righe per: UNIONE EUROPEA, ALTRI PAESI EUROPEI, AFRICA, AMERICA, ASIA, OCEANIA, Totale.]

I fogli del file Excel sono organizzati per continente:

- **RIEPILOGO**
- **UNIONE EUROPEA**
- **ALTRI PAESI EUROPEI**
- **AFRICA**
- **AMERICA**
- **ASIA**
- **OCEANIA**