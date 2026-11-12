# NUOVA Modifica Testi DOCX

Con questa nuova modalità di modifica testi è possibile personalizzare qualsiasi testo fornito da noi come **Testo Standard**, e far sì che quest'ultimo venga disabilitato, in modo da non visualizzarlo più all'interno di CWOL, e di sostituirlo con il testo modificato.

## Procedura

### 1. Accedere alla tabella dei testi DOCX

Andare nell'apposita tabella per scegliere il testo desiderato, ovvero:

- Dai **tre puntini dell'icona menù** → scrivere la parola **docx** e scegliere la voce del tipo di testo che occorre modificare, cioè se testi di:
  - Anagrafe
  - Elettorale
  - Stato Civile

[Immagine: finestra di ricerca applicazioni con query "docx" e tre risultati: Servizi Demografici>Anagrafe>Tabelli>Progressivi/Personalizzazione>Testi Docx, Servizi Demografici>Elettorale>Tabelli>Progressivi/Personalizzazione>Testi Docx, Servizi Demografici>Stato Civile>Tabelli>Personalizzazione>Testi Docx]

### 2. Selezionare il testo da modificare

Dopodiché selezionare con il **doppio click del mouse** il testo desiderato cercandolo tramite **codice testo** o **descrizione**, in modo da vederlo nel dettaglio e cliccare poi il bottone **'RENDI MIO'**.

[Immagine: tabella "Documenti base" con colonne Classe, Funzione, Codice, Codice Num, Descrizione. Esempio di testo selezionato: Classe "Elettorale", Funzione "COMUNICAZIONI", Codice "cwd_RichiestaRinnovoTesseraElettorale", Codice Num "0383", Descrizione "Richiesta Rinnovo Tessera Elettorale"]

### 3. Confermare l'operazione "Rendi Mio"

Cliccare il pulsante **Rendi Mio** per bloccare i futuri aggiornamenti del testo standard e creare allo stesso momento un nuovo testo personalizzato. Dare → **conferma** all'uscita del messaggio:

> **Rendi Mio**
> L'operazione bloccherà i futuri aggiornamenti del testo e creerà un nuovo testo personalizzato. Procedere?
> [F5-Conferma] [F8-Annulla]

### 4. Inserire il nuovo codice

Una volta confermato il passaggio, il programma chiederà con un ulteriore messaggio di inserire il codice per il nuovo testo personalizzato, mettendo già di default il **codice istat** del cliente.

Quindi immettere il nuovo codice del testo **SENZA inserire spazi o caratteri particolari (&,%,/…)** al suo interno → **conferma**

> **Rendi Mio**
> Inserisci il codice per il nuovo testo personalizzato.
> [___________]_RinnovoTesseraElettorale
> [Conferma] [Annulla]

### 5. Confermare la sostituzione sulle tabelle

Infine, con un ultimo messaggio il programma chiede se deve procedere a sostituire il vecchio testo con il nuovo sulle tabelle dove è utilizzato, quindi → **conferma**

> **Rendi Mio**
> Sostituire il codice testo nelle tabelle di composizione da cwd_RichiestaRinnovoTesseraElettorale a 042048_RinnovoTesseraElettorale?
> [F5-Conferma]

### 6. Verifica del risultato

Al termine della sostituzione viene restituito il messaggio di **"Codice sostituito"**.

> **Sostituzione codice**
> Codice sostituito

In questo modo:

- Il **vecchio codice** verrà visualizzato con il flag **scaduto** nella tabella dei testi (per vederlo, nella finestra principale di ricerca della tabella selezionare anche il flag **"includi testi scaduti"**)
- Il **nuovo testo** pronto ad ogni modifica verrà visualizzato come **testo principale**

[Immagine: tabella "Documenti base" con colonna "Scaduti" evidenziata. Il vecchio testo "cwd_RichiestaRinnovoTesseraElettorale" appare con flag scaduto. Il nuovo testo "042048_RinnovoTesseraElettorale" appare come testo principale attivo.]

---

## Esempio pratico: modifica/sostituzione del testo standard

### Testo collegato a 3 differenti tipi di atto

[Immagine: "Tabella Comunicazioni da Atti" con colonne Tipo Atto, Parte, Serie, Descrizione, Causale, Codice Testo, ID Com. Il testo "cwd_ComunicazioneNascitaASL" è collegato a 3 righe: Nascita Parte 1 Serie A (ID 529), Nascita Parte 1 Serie B (ID 560), Nascita Parte 2 Serie B (ID 561)]

### Utilizzo del bottone 'Rendi Mio'

[Immagine: dettaglio documento "cwd_ComunicazioneNascitaASL" - Cod. Numerico 0038 - Descrizione "Comunicazione Nascita alla ASL". Banner giallo: "Si sta modificando un documento standard." Pulsante "Rendi Mio" evidenziato con freccia rossa.]

### Inserimento nuovo codice

[Immagine: dialog "Rendi Mio" con campo per il nuovo codice personalizzato. Il prefisso istat "042048" è già presente di default, seguito da "_NascitaPerASL". Pulsanti Conferma/Annulla.]

### Sostituzione del vecchio testo con il nuovo

[Immagine: dialog "Rendi Mio" con messaggio: "Sostituire il codice testo nelle tabelle di composizione da cwd_ComunicazioneNascitaASL a 042048_NascitaPerASL?" Pulsante F5-Conferma.]

### Messaggio di sostituzione avvenuta correttamente

> **Sostituzione codice**
> Codice sostituito in 3 righe.

### Il nuovo testo viene agganciato in automatico ai 3 differenti tipi di atto

[Immagine: "Tabella Comunicazioni da Atti" aggiornata. Il campo "Codice Testo" mostra ora "042048_NascitaPerASL" in tutte e 3 le righe (ID Com: 529, 560, 561), confermando che la sostituzione è stata applicata automaticamente a tutti i collegamenti.]