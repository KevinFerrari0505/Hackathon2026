# Personalizzazione Stato Civile

Il punto di menù è raggiungibile tramite il percorso:

**Servizi Demografici → Stato Civile → Tabelle → Personalizzazione → Personalizzazione Stato Civile**

Da questo punto è possibile gestire vari aspetti per lo Stato Civile, ovvero:

---

## 1. Stampa degli Atti

Scegliere ad esempio quante stampe effettuare per atto, se eseguire o meno dei controlli sulla data dell'atto oppure se numerare l'atto all'inizio o una volta finito, e così via.

[Schermata: Tab "Stampa Atti" della finestra Personalizzazione Stato Civile, con i seguenti campi:]

- **Numero Copie per la Stampa dell'Atto**: campo numerico (es. 3)
- **Gestire campo "Volume" per Atti emessi**: checkbox
- **Controlli sulla data dell'Atto**: checkbox (attivo)
- **Obbligatoria Delegazione**: checkbox
- **Abilito l'emissione di un solo atto originale alla volta per tipo parte e serie**: checkbox (attivo)
- **Numerazione Atto solo alla fine**: checkbox (attivo)
- **Abilito l'emissione di un solo atto trascritto alla volta per tipo parte e serie**: checkbox (attivo)
- **Codice Cittadinanza da proporre**: campo con ricerca
- **Cod. Rel. Par. da proporre (nascita)**: campo con ricerca
- **Luogo Nas. da proporre (Atto nascita)**: campo con ricerca
- **Testo Trasm. atto a altro Comune per trascrizione**: campo con ricerca (es. `cwd_comunicazioneNasci` → "Trasmissione Atto Nascita al Comune di Residenza")
- **Codice Categoria itaDrive allegati atti**: campo con ricerca (es. `ALLEG_ATTI_STACIV` → "Allegati atti di Stato Civile")

---

## 2. Registrazione Anagrafica dopo l'atto

Scegliere se registrare immediatamente l'atto anche in anagrafe, o se apportare correzioni anche lì.

[Schermata: Tab "Registrazione Anagrafe" – sezione "Info Registrazione Anagrafica", con i seguenti campi:]

- **Registrazione immediata in Anagrafe dell'atto?**: checkbox (attivo)
- **Correzione Dati Atto varia Anagrafe?**: checkbox (attivo)
- **Proporre Var. Rel. Par. dopo atto morte?**: checkbox (attivo)

---

## 3. Pubblicazioni di Matrimonio

Impostare i vari testi relativi alle pubblicazioni, impostare causale e il tipo di diritto da emettere.

[Schermata: Tab "Pubbl. Matrimonio" – sezione "Pubblicazione Matrimonio", con i seguenti campi:]

- **Testo per Pubblicazione Matrimonio**: campo con ricerca (es. `cwd_VerbalePubblicazion` → "Verbale di Pubblicazione di Matrimonio")
- **Testo per Atto Pubblicazione Matrimonio**: campo con ricerca (es. `cwd_AttoPubblicazione` → "Atto di Pubblicazione")
- **Causale Verbale Processo Matrimonio**: campi numerici (es. 3 / 5 / 1) → "Processo Verbale Pubblicazione Matrimonio"
- **Tipo Diritti per Atto**: menu a tendina (es. E)
- **Testo Pubblicazione per Albo Online**: campo con ricerca (es. `cwd_AttoPubblicazione` → "Atto di Pubblicazione")
- **Tipo pubblicazione Albo Online**: campo (es. 01) → "(STC) PUBBLICAZIONI DI MATRIMONIO"
- **Firma digitale su atto pubbl. matrimonio**: checkbox (attivo)
- **Metodo conteggio periodo esposizione**: checkbox

### Metodo conteggio periodo esposizione

- Se il flag **"metodo conteggio periodo esposizione"** è **attivo**, conteggia la durata di **8 giorni**, **senza** tener conto del giorno stesso della pubblicazione.
- Se il flag è **disattivo**, conteggia la durata di **8 giorni**, **tenendo conto** del giorno stesso della pubblicazione.

[Schermata: Sezione "Dati Pubblicazione" con esempio di flag attivo – Data Pubbl. 30/03/2026, Periodo esposizione dal 30/03/2026 al 07/04/2026, Durata Complessiva Giorni 8]

[Schermata: Sezione "Dati Pubblicazione" con esempio di flag disattivo – Data Pubbl. 30/03/2026, Periodo esposizione dal 30/03/2026 al 06/04/2026, Durata Complessiva Giorni 8]

---

## 4. Varie

Impostare il tipo diritti per le certificazioni, se inserire un atto con persona senza matricola, ecc.

[Schermata: Tab "Varie", con i seguenti campi:]

- **Tipo Diritti per certificazione Stato Civile**: menu a tendina (es. E)
- **Permettere inserimento persona su atto senza matricola**: checkbox
- **Ambiente CWOL**: checkbox (attivo)
- **UUID Servizio stato civile**: campo con ricerca
- **UUID Servizio Permessi Seppellimento**: campo con ricerca

---

## 5. Causali

Impostare le causali relative agli AIRE.

[Schermata: Tab "Causali", con i seguenti campi:]

- **Causale Atto di Nascita AIRE**: campi numerici (es. 3 / 1 / 6) → "Atto di Nascita di persona AIRE senza registraz. Anagr."
- **Causale Atto di Morte AIRE**: campi numerici (es. 3 / 3 / 3) → "Atto di Morte di persona Aire senza registraz. Anagr."
- **Causale Acquisto Cittadinanza italiana**: campi numerici (es. 3 / 4 / 5) → "Acquisto Cittadinanza italiana di soggetto da iscrivere AIRE"
- **Causale Perdita Cittadinanza italiana**: campi numerici (es. 3 / 4 / 4) → "Perdita cittadinanza di soggetto AIRE senza registraz. Anag."

---

## 6. Permessi Seppellimento

Impostare la videata che apparirà all'inserimento di un permesso e altre informazioni.

[Schermata: Tab "Permessi di Seppellimento", con due sezioni:]

**Sezione "Permessi" – Righi personalizzabili:**

| Riga | Etichetta |
|------|-----------|
| Riga 1 p. s. | NOME DITTA |
| Riga 2 p. s. | TIPO SEPOLTURA |
| Riga 3 p. s. | OGGETTO SEP/CREM |
| Riga 4 p. s. | TIPO TRASPORTO |
| Riga 5 p. s. | OGGETTO TRASPORTO |
| Riga 6 p. s. | DATA TRASPORTO |
| Riga 7 p. s. | ORA PARTENZA |
| Riga 8 p. s. | INCARICATO AL TRASPORTO |
| Riga 9 p. s. | TARGA AUTOVEICOLO |
| Riga 10 p. s. | LUOGO PARTENZA |
| Riga 11 p. s. | LUOGO SOSTA |
| Riga 12 p. s. | NUL. OSTA AUT.GIUDIZIARIA |
| Riga 13 p. s. | NUL. OSTA AUT.SANITARIA |
| Riga 14 p. s. | LUOGO CREMAZIONE |

**Sezione "Info":**

- **Numerazione per tipologia**: checkbox
- **Presenta videata perm. sepp. dopo atto morte 1 o 2B**: checkbox (attivo)
- **Codice servizio emittente**: campo (es. 0)
- **Codice Categoria itaDrive**: campo con ricerca (es. `ALLEG_PERM_SEP`)
- **Allegati Permessi di Seppellimento**: campo

---

## 7. Richiesta Unione Civile

Impostare testo del verbale e la causale.

[Schermata: Tab "Rich. Unione Civile" – sezione "Richiesta Unione Civile", con i seguenti campi:]

- **Testo Verbale Richiesta Unione Civile**: campo con ricerca (es. `cwd_VerbaleRichiesta` → "VERBALE RICHIESTA UNIONE CIVILE")
- **Causale Verbale Richiesta Unione Civile**: campi numerici (es. 3 / 11 / 1) → "Processo Verbale Richiesta Unione Civile"