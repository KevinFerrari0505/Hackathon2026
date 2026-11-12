# Allineamento cittadinanza, carta d'identità o permesso di soggiorno

Nel caso in cui si dovesse creare un disallineamento tra il DataBase locale ed ANPR riguardante i dati relativi a: **Permesso di soggiorno**, **carta di identità**, **cittadinanza**, e **codice fiscale** nel DB locale.

## Procedura

### 1. Interrogazione anagrafe

Da **Cityware.online** eseguire un'interrogazione anagrafe Cityware.

[Schermata: finestra "Interrogazione anagrafe" con campi di ricerca: Cognome, Nome, Parentela, Data nascita, Via, Num. Civico, Famiglia, Matricola, Codice Fiscale, Cittadinanza, ANPR ID. Opzioni di visualizzazione: Apr, Aire.]

### 2. Selezione della persona e avvio allineamento

Ricercare la persona, selezionarla con un click e premere sulla destra:

> **ANPR → Allinea posizione cittadino**

[Schermata: elenco risultati ricerca con la persona selezionata in evidenza. Pannello laterale destro con menu "Funzioni" → "ANPR" → "Allinea posiz. Cittad." evidenziato in rosso.]

### 3. Verifica dei campi disallineati

Dovreste vedere una schermata simile dove i campi non allineati sono scritti in **rosso**.

[Schermata: "Controllo dati correnti in ANPR" con sezioni:
- **Permesso di Soggiorno**: dati ANPR vs dati CW (es. "ANPR: Permesso nr. IT46569 rilasciato il 06-05-2021 scade il...")
- **Carta d'identità**: dati ANPR vs dati CW (es. "ANPR: Carta nr. A2... rilasciata il 1-1-2021 scade il 19-02-2027 comune di...")
- **Cittadinanza**: "Dati allineati"
- **Indice Fiscale (allineamento su Anagrafe Locale)**: "ANPR: Codice Fiscale ML... A validazione: D - Definitivo" vs "CW: - Codice Fiscale ML... A validazione: D - Definitivo"
- **Dati generali**: confronto tra dati ANPR e CW (Sesso, Data nascita, Luogo Nascita, Matricola, Famiglia)

Annotazioni in rosso:
- "Questi dati saranno allineati in ANPR"
- "Questi dati saranno allineati localmente"
- "Questi dati non saranno allineati"]

### 4. Aggiornamento

Premendo il tasto **Aggiorna ANPR** i dati che si trovano in CW verranno riportati in ANPR.

## Nota

Questo tipo di allineamento funziona anche per allineare **nuovi permessi di soggiorno** o **carte d'identità**.