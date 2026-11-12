# ANPR - Cambio data decorrenza residenza

In ANPR **non è possibile** modificare la data di residenza.

## WA (da WebApp ANPR) – Annullamento operazione

Occorre recuperare **id operazione** e **data decorrenza**.

### Passaggio 1 – Consultazione

Da **Consultazione** cercare la persona e cliccare **"Elenco Operazioni"** (sulla sinistra).

[Schermata: Elenco operazioni con colonne ID OPERAZIONE ANPR, OPERAZIONE, EFFETTUATA IN DATA, DATA DI DECORRENZA, DATA DI DEFINIZIONE, ESITO DELLA REGISTRAZIONE, DATI DELL'OPERAZIONE, DATI DELLA RISPOSTA. Esempio di riga evidenziata: ID 19121064 – MUTAZIONE FAMIGLIA CONVIVENZA – 08-04-2019 – 19-10-2018 – 08-04-2019 – Completata con esito positivo]

### Passaggio 2 – Registrazione - Annullamento Mutazione

Percorso: **HOME > REGISTRAZIONE > SERVIZI DI REGISTRAZIONE**

**Scegli operazione:**

| Campo | Valore |
|-------|--------|
| Tipo operazione | Annullamento mutazione |
| Iniziativa* | Operazione d'ufficio |

**Ricerca la persona:**

| Campo | Descrizione |
|-------|-------------|
| Codice fiscale | (campo di ricerca) |
| Cognome | (campo di ricerca, con opzione "Senza cognome") |

Ricercare la persona e selezionarla.

### Passaggio 3 – Compilazione dati

**Dati principali:**

| Campo | Valore / Istruzione |
|-------|---------------------|
| Data protocollo del comune | (GG / MM / AAAA) |
| Data di decorrenza* | Indicare quella presente nell'elenco operazioni (es. 19/10/2018) |
| Data di definizione della pratica | (GG / MM / AAAA) |
| Note | (campo libero) |

**Altri dati:**

| Campo | Valore / Istruzione |
|-------|---------------------|
| Tipo scheda* | **Scheda Famiglia** se riguarda una variazione sull'intera famiglia; **Scheda Soggetto** se va annullato solo il singolo soggetto |
| Ripristino posizione anagrafica | NO |

**Dati dell'operazione da annullare:**

| Campo | Valore / Istruzione |
|-------|---------------------|
| Operazione richiesta* | Indicare lo **stesso tipo** presente nell'elenco operazioni (es. MUTAZIONE FAMIGLIA CONVIVENZA) |
| Id operazione comune | (campo di testo) |
| Protocollo del comune | (campo di testo) |
| Data protocollo del comune | (GG / MM / AAAA) |
| ID operazione ANPR* | ID recuperato dall'elenco operazioni (es. 191121064) |
| Data operazione | (GG / MM / AAAA) |
| Motivo richiesta | (campo di testo) |

> **Note importanti:**
> - **Data decorrenza**: indicare quella presente nell'elenco operazioni.
> - **Tipo scheda**: *Scheda famiglia* se riguarda una variazione sull'intera famiglia; *Scheda soggetto* se va annullato solo il singolo soggetto.
> - **Annullamento attribuzione codice fiscale** = NO (presente solo se scheda soggetto).
> - **Operazione richiesta**: indicare lo stesso tipo presente nell'elenco operazioni.

### Passaggio 4 – Conferma

Cliccare **CONFERMA**, poi **SALVA** e **CHIUDI**.

[Schermata: Pulsanti CONFERMA, RIPULISCI e ANNULLA OPERAZIONE]