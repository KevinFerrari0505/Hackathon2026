# Controllo Albo per Creazione Proposte di Cancellazione

Questo programma permette il lancio di un controllo sulla lista degli scrutatori dalla quale vengono estratti quelli che devono essere cancellati per perdita dei requisiti. Si suggerisce di stampare l'elenco e creare un archivio in modo da mantenere i dati: l'elenco riporta anche le causali di cancellazione come prospetto Excel come mostrato dalle videate sottostanti.

## Interfaccia del programma

[Schermata: Finestra "Controllo Albo per Creazione Proposte di Cancellazione" con sezione "Tipo Elaborazione" contenente due checkbox: "Stampa Elenco" (selezionata) e "Creazione Archivio" (selezionata)]

## Formato del prospetto Excel

Il prospetto Excel ha il seguente formato:

| Matricola | Cognome Nome | Data Nascita | In Elettorale | In Anagrafe | Cancellazione SCRUTATORI |
|-----------|--------------|--------------|---------------|-------------|--------------------------|
| 23877 | *(cognome oscurato)* | 06/01/1943 | Annullato | Canc. Aire | Emigrazione |
| 25745 | *(cognome oscurato)* | 19/04/1985 | | Aire | Cancellazione Aire |
| 25472 | *(cognome oscurato)* | 26/02/1989 | | Emigrato | Emigrazione |
| 24894 | *(cognome oscurato)* | 29/01/1975 | Annullato | Emigrato | Emigrazione |
| 24850 | *(cognome oscurato)* | 05/10/1971 | Annullato | Emigrato | Emigrazione |
| **NUMERO SCRUTATORI PRESENTI NELL'ALBO** | | **735** | **TOTALE LIMITE ETA'** | | **0** |
| **TOTALE SCRUTATORI DA CANCELLARE** | | **5** | **TOTALE MORTI** | | **0** |
| **NUOVO ALBO, TOTALE SCRUTATORI:** | | **730** | **TOTALE EMIGRATI** | | **4** |
| | | | **TOTALE PERDITA DIRITTO VOTO** | | **0** |
| | | | **TOTALE AIRE** | | **1** |

### Spiegazione delle colonne

- **Matricola**: codice identificativo dello scrutatore
- **Cognome Nome**: dati anagrafici dello scrutatore
- **Data Nascita**: data di nascita
- **In Elettorale**: stato nella lista elettorale (es. "Annullato")
- **In Anagrafe**: stato anagrafico (es. "Canc. Aire", "Aire", "Emigrato")
- **Cancellazione SCRUTATORI**: causale di cancellazione (es. "Emigrazione", "Cancellazione Aire")

### Riepilogo statistico (righe di riepilogo)

Il prospetto include in basso un riepilogo con:

- **Numero scrutatori presenti nell'albo**: totale iniziale
- **Totale scrutatori da cancellare**: numero di soggetti da rimuovere
- **Nuovo albo, totale scrutatori**: totale dopo la cancellazione
- **Totale Limite Età**: cancellati per superamento limite di età
- **Totale Morti**: cancellati per decesso
- **Totale Emigrati**: cancellati per emigrazione
- **Totale Perdita Diritto Voto**: cancellati per perdita del diritto di voto
- **Totale AIRE**: cancellati per iscrizione AIRE