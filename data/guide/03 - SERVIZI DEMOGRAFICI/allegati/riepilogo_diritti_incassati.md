# RIEPILOGO DI CASSA

Di seguito le estrazioni effettuabili da CWOL - Cityware Online per il controllo degli introiti da sportello: certificati, Cie/C.I. e altri documenti.

## Accesso al programma e informazioni generali

Seguire il percorso: **Servizi Demografici → Anagrafe → Sportello → Riepilogo Diritti Incassati**

All'accesso del programma dovete immettere i dati per effettuare l'estrazione, che può essere in formato di stampa oppure Excel:

[Schermata del form "Riepilogo diritti incassati" con i campi: Data emissione (da/a), Ora Emissione, Tipo Stampa, Canale Pagamento, Tipo Emissione, Utente, Terminale che ha emesso il certificato, Selezionare tipo Carte di Indentità/Doc. Riconoscimento (Cartacce, CIE, Doc. Riconoscimento)]

### Parametri di estrazione

- **Il periodo di emissione:** da una data gg/mm/aaaa ad un'altra gg/mm/aaaa

- **Il tipo di stampa:**
  1. **Dettagliato:** produce un dettaglio giornaliero dei documenti emessi
  2. **Totale di giornata:** crea una voce per ogni giornata riassumendo in totali le emissioni
  3. **Totale di periodo:** somma le emissioni in un dato periodo senza dividerle in giornate
  4. **Totale per terminale:** divide le emissioni a seconda del terminale che le emette
  5. **Totale per Utente:** divide le emissioni per l'utente che le ha confermate, si può filtrare per singolo utente indicando il codice fiscale di questo.

### Tipo di rendicontazione

Sempre nella sezione del tipo di stampa trovate il tipo di rendicontazione:

- **Unica:** riporta i totali dividendoli solo per il tipo di diritto che viene incassato e riportando il totale finale
- **Separata:** divide gli incassi per il metodo di pagamento effettuato: cassa, bancomat, pagopa ecc.

### Tipo documento da estrarre

- Se seleziono **CIE, C.I. e altri documenti** estraggo tutto quello che è stato emesso allo sportello compresi i certificati.
- Se tolgo **CIE**, non estrarrò le CIE e così dicendo per le altre opzioni.
- Se voglio estrarre **solo le CIE** seleziono solo quel valore, stessa cosa per le altre opzioni.
- Se **non seleziono niente**, estrarrà solamente i certificati.

## Esempi di estrazione

### Tipo di Stampa: Dettagliato

Si noti come vi è il dettaglio delle emissioni per giornata:

| Data | Tipo Certificato | Certificati Emissi (Ann. / Esem. / Norm. / Bollo / On. / Auto) | Diritti Segreteria | Diritti Stato Civile | Carta di Identità | Quota Ministero CIE | Totali Certif. | Incassat | TOTALE GENERALE |
|------|-----------------|--------------------------------------------------------------|-------------------|---------------------|-------------------|--------------------|--------------|----------|----------------|
| 02-01-2025 | | | | | | | | | |
| | | 1 / 2 | 0,26 | 5,16 | | | 3 | 5,42 | 5,42 |
| **Totale della Giornata:** | | 1 / 2 | 0,26 | 5,16 | | | 3 | 5,42 | 5,42 |
| 08-01-2025 | | | | | | | | | |
| | Cie Emissione | 2 | 0,52 | | 10,32 | 32,00 | 2 | 42,84 | 42,84 |
| | STORICO DI RESIDENZA | 2 | | | | | 2 | | |
| **Totale della Giornata:** | | 2 / 2 | 0,52 | | 10,32 | 32,00 | 4 | 42,84 | 42,84 |
| 15-01-2025 | | | | | | | | | |
| | CIE | 1 | 5,42 | 16,78 | | | 1 | 22,20 | 22,20 |
| **Totale della Giornata:** | | 1 | 5,42 | 16,78 | | | 1 | 22,20 | 22,20 |
| **Totale** | | 0 / 3 / 5 | 6,20 | 21,94 | 10,32 | 32,00 | 8 | 70,46 | **70,46** |

### Tipo Stampa: Totale di giornata

Produce la stampa mostrando i totali per ogni giornata in un dato periodo di tempo.

**Riepilogo Periodico Diritti**
dal 01-01-2025 al 31-01-2025

| Data | Tipo Certificato | Certificati Emissi (Ann. / Esem. / Norm. / Bollo / On. / Auto) | Diritti Segreteria | Diritti Stato Civile | Carta di Identità | Quota Ministero CIE | Totali Certif. | Incassat | TOTALE GENERALE |
|------|-----------------|--------------------------------------------------------------|-------------------|---------------------|-------------------|--------------------|--------------|----------|----------------|
| 02-01-2025 | | | | | | | | | |
| **Totale della Giornata:** | | 1 / 2 | 0,26 | 5,16 | | | 3 | 5,42 | 5,42 |
| 08-01-2025 | | | | | | | | | |
| **Totale della Giornata:** | | 2 / 2 | 0,52 | | 10,32 | 32,00 | 4 | 42,84 | 42,84 |
| 15-01-2025 | | | | | | | | | |
| **Totale della Giornata:** | | 1 | 5,42 | 16,78 | | | 1 | 22,20 | 22,20 |
| **Totale** | | 0 / 3 / 5 | 6,20 | 21,94 | 10,32 | 32,00 | 8 | 70,46 | **70,46** |

### Tipo Stampa: Totale di Periodo

Il totale di periodo propone le emissioni in un dato periodo di tempo senza riassumerle per giornata.

**Riepilogo Periodico Diritti**
dal 01-01-2025 al 31-01-2025

| Data | Tipo Certificato | Certificati Emissi (Ann. / Esem. / Norm. / Bollo / On. / Auto) | Diritti Segreteria | Diritti Stato Civile | Carta di Identità | Quota Ministero CIE | Totali Certif. | Incassat | TOTALE GENERALE |
|------|-----------------|--------------------------------------------------------------|-------------------|---------------------|-------------------|--------------------|--------------|----------|----------------|
| | | 1 / 2 | 0,26 | 5,16 | | | 3 | 5,42 | 5,42 |
| | | 1 | 5,42 | 16,78 | | | 1 | 22,20 | 22,20 |
| | Cie Emissione | 2 | 0,52 | | 10,32 | 32,00 | 2 | 42,84 | 42,84 |
| | STORICO DI RESIDENZA | 2 | | | | | 2 | | |
| **Totale** | | 0 / 3 / 5 | 6,20 | 21,94 | 10,32 | 32,00 | 8 | 70,46 | **70,46** |

### Tipo Stampa: Totale per Utente

In questo riepilogo vedete che le emissioni sono suddivise per utente e poi viene fatto il totale.

**Riepilogo Periodico Diritti**
dal 17-02-2025 al 17-02-2025

| UTENTE | Certificati Emissi (Ann. / Esem. / Norm. / Bollo / On. / Auto) | Diritti Segreteria | Diritti Stato Civile | Acconto Stato Civile | Rimborsi stampati | Diritti Carta di Identità | Diritti d'Archivio | Totali Certif. | Incassat | Diritti CIE Stato | TOTALE GENERALE |
|--------|--------------------------------------------------------------|-------------------|---------------------|---------------------|-------------------|--------------------------|-------------------|--------------|----------|-------------------|----------------|
| | 5 / 1 | 0,52 | | | | | | 6 | 0,52 | | 0,52 |
| | 4 | | | | | | | 4 | | | |
| | 3 | 1,56 | | | | | | 3 | 1,56 | | 1,56 |
| | 6 | 1,56 | | | 30,96 | | | 6 | 32,52 | 83,95 | 116,47 |
| | 11 | | | | | | | 11 | | | |
| | 7 | 1,82 | | | 36,12 | | | 7 | 37,94 | 117,53 | 155,47 |
| | 2 / 3 | 1,56 | | | | | | 5 | 1,56 | | 1,56 |
| | 17 | | | | | | | 17 | | | |
| | 7 | 1,82 | | | 36,12 | | | 7 | 37,94 | 117,53 | 155,47 |
| | 2 | | | | | | | 2 | | | |
| **Totale** | 0 / 41 / 20 / 7 | 8,84 | | | 103,20 | | | 68 | 112,04 | 319,01 | **431,05** |

Nel caso volessi sapere le emissioni per singolo utente allora dovete inserire il codice fiscale di quest'ultimo.

[Schermata del form "Tipo stampa" con i campi: Tipo Stampa (Dettagliato), Canale Pagamento (Rendicontazione separata), Tipo Emissione (Emessi allo sportello), Utente (campo con codice fiscale evidenziato in rosso), sezione "Terminale che ha emesso il certificato" con opzione "Tutti" selezionata e "Lista terminali" deselezionata]

## Consigli

È possibile poi creare delle combinazioni: per esempio inserendo il codice fiscale di un soggetto ma mantenendo il tipo stampa a **Dettagliato** potete vedere tutte le emissioni per singolo utente e così dicendo.