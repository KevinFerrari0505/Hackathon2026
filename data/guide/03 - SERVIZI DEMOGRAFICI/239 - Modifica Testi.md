# Modifica Testi

## Modifica diretta (utente autorizzato)

Se si ha l'autorizzazione a poter modificare dei testi base, è sufficiente un **doppio click** nel testo e poi premere il bottone **Apri/Visualizza** e procedere nella modifica.

## Creazione di un nuovo testo (utente non abilitato)

Se invece non si è abilitati, procedere andando in:

- **Servizi Demografici > Anagrafe > Tabelle > Progressivi > Personalizzazione > Testi Docx**
- **Servizi Demografici > Elettorale > Tabelle > Progressivi > Personalizzazione > Testi Docx**
- **Servizi Demografici > Stato Civile > Tabelle > Personalizzazione > Testi Docx**

Scegliere l'opzione in base a se si vuole modificare testi relativi all'**anagrafe**, all'**elettorale** o allo **Stato Civile**.

### Procedura passo-passo

1. Utilizzare il tasto → **Nuovo**

   [Screenshot: pulsante "Nuovo" evidenziato nella barra laterale destra della schermata di gestione testi]

2. Si aprirà la schermata con i dati del nuovo testo. Alla voce **"Codice"** il programma inserisce in automatico il **codice ISTAT** del proprio comune. Questo **VA LASCIATO** come si presenta, perché vi permetterà poi di distinguere il testo standard già presente nel programma da quello da voi modificato.

3. Selezionare → **Copia da...**

   [Screenshot: campo "Codice" con il CODICE ISTAT e l'underscore dopo il codice (es. `c_`), pulsante "Copia da..." evidenziato]

4. A questo punto si apre una finestra di ricerca dove è possibile prendere con il **doppio click** il testo già presente in Cityware che si desidera modificare.

   [Screenshot: finestra "Risultato Ricerca" con tabella "Documenti" contenente colonne: Codice, Descrizione, Tipo. Esempi di documenti: `cwd_AssicurataTrascrizioneM...`, `cwd_SoggConsComunicazione...`, `cwd_Tessere_RegistroPerCon...`, tutti di tipo DOCX]

5. La schermata che apparirà sarà quella vista in precedenza con i dati del testo:
   - Alla voce **"Codice"** (lasciando il codice ISTAT con l'underscore che viene messo in automatico) è possibile nominare il codice a piacimento **SENZA USARE SPAZI O CARATTERI SPECIALI o PUNTI**.
   - Alla voce **"Descrizione"** dare un "Titolo" al testo con la possibilità di usare spaziature ma sempre **SENZA CARATTERI SPECIALI**.

   → **Aggiungi**

   [Screenshot: form con campo Codice (es. `c_SoggConsComunicazioneAIRE`), Descrizione (es. "Soggetto Consolato Comunicazione Iscrizione AIRE"), Classificazione (Anagrafe), Tipo (DOCX), Funzione (COMUNICAZIONI), pulsante "Aggiungi" evidenziato]

6. Dopo aver aggiunto il testo, la schermata si presenterà con i relativi dati del testo più il bottone → **Apri/Visualizza**

   [Screenshot: schermata con i dati del testo salvato e pulsante "Apri / Visualizza" evidenziato nella barra laterale]

7. Cliccandolo si aprirà una nuova scheda con il testo in **ONLYOFFICE** dove sarà possibile apporre le modifiche desiderate.

## Variabili nel testo

Il testo contiene variabili dinamiche racchiuse tra `@{...}@`. Esempi di variabili presenti nei template:

- `@{SANA::ana_cognome}@` — Cognome anagrafico
- `@{SANA::ana_nome}@` — Nome anagrafico
- `@{SANA::ana_indestero1}@` — Intestazione indirizzo
- `@{SANA::ana_indestero_cap}@` — CAP indirizzo
- `@{SANA::ana_indestero_luogo}@` — Luogo indirizzo
- `@{SANA::ana_nascita_data}@` — Data di nascita
- `@{SANA::ana_nascita_atto}@` — Atto di nascita
- `@{SANA::ana_staciv}@` — Stato civile
- `@{SANA::ana_sciv_coniuge}@` — Sciv coniuge
- `@{SANA::ana_aire_dataiscrizione}@` — Data iscrizione AIRE
- `@{SANA::ana_aire_aireiscr1}@` — Pratica AIRE 1
- `@{SANA::ana_famiglia}@` — Famiglia
- `@{SANA::ana_aire_caumovare_dec}@` — Causa movimento
- `@{SANA::ana_aire_luogo_iscr_canc}@` — Luogo iscrizione/cancellazione
- `@{SANA::ana_indestero1upper}@` — Intestazione maiuscolo
- `@{SANA::ana_indestero2upper}@` — Intestazione 2 maiuscolo
- `@{SANA::ana_indestero2_cap}@` — CAP indirizzo 2
- `@{SANA::ana_indestero2_luogo}@` — Luogo indirizzo 2
- `@{SANA::ana_indestero_consolato}@` — Consolato
- `@{SANA::ana_indestero_consolato_ind1}@` — Consolato indirizzo 1
- `@{SANA::ana_indestero_consolato_ind2}@` — Consolato indirizzo 2
- `@{SANA::ana_indestero_consolato_ind2}@` — Consolato indirizzo 2
- `@{SANAELE::ele_lista_gen}@` — Lista elettorale generale
- `@{SANAELE::ele_fascicolo}@` — Fascicolo elettorale
- `@{SANAELE::ele_sezione}@` — Sezione elettorale
- `@{SBASE.CLIENT_DESLOCAL}@` — Denominazione ente locale
- `@{Samarty.now|date_format="%d/%m/%Y"}@` — Data corrente
- `@{SINCLUDE.CWD_intestaCertificat}@` — Intestazione certificato
- `@{SINCLUDE.CWD_fondoAnagrafe}@` — Fondo anagrafe
- `@{while $ANA->readRecord()}@` — Ciclo lettura record anagrafe
- `@{while $MOVIM->readRecord()}@` — Ciclo lettura movimento
- `@{while $ANAELE->readRecord()}@` — Ciclo lettura elettorale
- `@{while}@` — Fine ciclo

### Struttura di un ciclo nel template

```
@{while $ANA->readRecord()}@
  ... contenuto con variabili @{SANA::...}@ ...
@{/while}@

@{while $MOVIM = $ANA->listaGuida('dai_movim')}@
  ... contenuto con variabili @{SANA::...}@ ...
@{/while}@

@{while $ANAELE = $ANA->listaGuida('anavelettore')}@
  ... contenuto con variabili @{SANAELE::...}@ ...
@{/while}@
```

### Tabelle nei template

| Nr. Lista Generale | Nr. Fascicolo |
|---|---|
| `@{SANAELE::ele_lista_gen}@` | `@{SANAELE::ele_fascicolo}@` |

### Plugin per variabili aggiuntive

Eventuali altre variabili possono essere prelevate tramite il pulsante **Plugin** nella barra degli strumenti di ONLYOFFICE.

[Screenshot: barra strumenti ONLYOFFICE con il pulsante "Plugin" evidenziato in alto a destra]

---

> **N.B.** Il programma esegue il **salvataggio automatico ogni 3 secondi**, perciò una volta modificato tutto il testo sarà sufficiente **chiudere la scheda**. (Per il momento non andare in modifica delle variabili ma solo del testo scritto.)