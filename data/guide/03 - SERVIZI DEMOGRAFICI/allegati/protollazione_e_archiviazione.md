# Guida alla Protocollazione Diretta dei Documenti dai Servizi Demografici

In CWOL – Cityware Online, nelle schermate di stampa dei documenti, sono presenti una serie di bottoni che permettono, oltre alla consueta modifica del documento (corpo testo e nome file), scaricare/convertire il file o stamparlo, una serie di bottoni che vi danno la possibilità di:

- Protocollare direttamente il documento
- Allegare il documento nello spazio di archiviazione relativo (atto di S. Civile, pratiche anagrafiche, fascicolo elettorale o pratica funeraria)
- Protocollare e allegare per la conservazione con un solo click, mantenendo i metadati del protocollo.

## Cosa sono i metadati?

Sono le informazioni identificative legate alla registrazione di un protocollo. Queste accompagnano l'allegato nell'archiviazione; quindi, oltre al documento informatizzato avrete anche, per esempio, i dati del protocollo di quel documento (tipo protocollo, data e numero).

---

## 1) Pulsanti "Allega" e "Protocolla e Allega"

Ecco un esempio dei pulsanti che troverete:

[Schermata "Visualizzatore Documenti" con barra dei pulsanti: Protocolla, Scarica, Salva in file-box, Modifica Documento, Allega alla pratica, Protocolla e allega alla pratica]

### A) Allega alla pratica

Vi permette di allegare il documento alla pratica del soggetto. Lo stesso vale per gli atti di S. Civile, le pratiche funerarie e il fascicolo elettorale nonché tutte le stampe legate alle revisioni elettorali.

> **NB:** rispettare le regole di sintassi quando si salvano i file e non inserire caratteri che potrebbero dare problemi (questi sono indicati a fine guida).

### B) Protocolla e Allega

Compie la medesima funzione aggiungendovi l'apertura del protocollo:

[Schermata "Gestione Pratiche" con sezione "Sezione Protocollo" contenente campi: Segnatura, N.Protocollo, Data, Ora, Ultima modifica, Ufficio (PALC1 - UFFICIO 1) e sezione "Dettaglio Protocollo" con campi: Prot.Collegato, Tipo Doc, Oggetto, Prog. dell'Oggetto, Documenti Pratica n. 2025/2, Inviato il, Mitt./Firmatario]

Una volta protocollato vengono salvati i metadati sull'allegato:

[Schermata "Documenti pratica n. 2025/2" con tab "Metadati" selezionata]

| Chiave | Descrizione | Valore |
|--------|-------------|--------|
| PROT_TIPO | Tipo protocollo | P |
| PROT_ANNO | Anno protocollo | 2025 |
| PROT_NUM | Numero protocollo | 1 |
| PROT_DATA | Data protocollo | 2025-02-14 |
| PROT_SORG | Sorgente protocollo | itals |

A destra con il pulsante **VEDI PROTOCOLLO**, potete visualizzare il protocollo che avete registrato.

---

## Riferimento per il modulo Elettorale

Le medesime funzioni le ritrova in elettorale, dove vi lascio come riferimento il programma:

- **ELENCO VERBALI ELETTORALE**, che trovate al percorso:
  `Servizi Demografici → Elettorale → Manutenzione → Elenco Verbali Elettorali`

  Dove troverete i documenti della revisione che avete allegato. **Attenzione a scegliere sempre lo stesso verbale.**

Per gli atti di Stato Civile ed i permessi di seppellimento vale quanto detto in precedenza.

---

## Regole di sintassi per il rinomina file

### Caratteri che possono causare problemi

Questi caratteri sono consentiti, ma possono creare difficoltà in terminali, script o programmazione:

- **Spazio** (` `) → Rende il file difficile da usare nei comandi senza escape (`\ `) o virgolette (`"file con spazi"`).
- **Asterisco** (`*`) → Interpretabile come carattere jolly nei comandi shell.
- **Punto interrogativo** (`?`) → Usato come wildcard per un singolo carattere.
- **Backslash** (`\`) → Necessita escape (`\\`) in alcuni contesti.
- **Virgolette** (`"` `'`) → Possono interferire con la sintassi degli script.
- **Backtick** (`` ` ``) → Interpretato come comando da eseguire nella shell.
- **Pipe** (`|`) → Usato per concatenare comandi in shell.
- **Maggiore e minore** (`>` `<`) → Interpretati come redirezioni di output.
- **E commerciale** (`&`) → Usato per eseguire comandi in background.
- **Parentesi tonde** (`(` `)`) → Necessitano escape o virgolette in alcuni contesti.
- **Parentesi quadre** (`[` `]`) → Interpretate come espressioni regolari o test condizionali.
- **Accenti** (`~ ! $`) → Interpretati dalla shell con significati speciali.

### Consigli per nomi di file sicuri in Linux

- ✅ Usa solo caratteri alfanumerici (`a-z`, `A-Z`, `0-9`) e underscore (`_`) o trattino (`-`).
- ✅ Evita spazi e caratteri speciali per evitare problemi negli script.