# Controllo PEC nell'Indice Nazionale dei Domicili Digitali (INAD)

È ora disponibile un controllo nel campo **Codice Fiscale**, che verifica se il soggetto destinatario è registrato nell'anagrafica dei domicili digitali delle persone fisiche.

[Schermata: campo "Cod. Fiscale" con icona di controllo INAD evidenziata in un form di protocollo, con campi Tipo soggetto, Destinatario, PEC/Mail, Spedizione]

---

## a) Richiesta di fruizione del servizio INAD

Per poter utilizzare il servizio di verifica del codice fiscale è necessario che l'ente effettui l'attività di richiesta di Fruizione presso il portale INAD riservato agli enti: [https://selfcare.pagopa.it](https://selfcare.pagopa.it)

## b) Richiesta di attivazione del servizio INAD

Dopo aver ricevuto approvazione della richiesta di fruizione su portale INAD dovete effettuare una richiesta di attivazione a Palitalsoft. Siamo a disposizione anche per il supporto alla richiesta di fruizione.

> **ATTENZIONE:** per l'attivazione occorre contattare il commerciale di riferimento.

## c) Funzioni applicative

A partire dal Codice Fiscale, viene controllata la correttezza della PEC inserita. Se riscontra delle differenze, propone di aggiornare il campo **"PEC/Mail"** con la PEC estratta dall'INAD.

- Se **non viene confermata**, viene lasciata la PEC inserita dall'operatore.
- Se il **Codice Fiscale non è formalmente corretto**, il controllo non può essere effettuato.

[Schermata: finestra di dialogo "Controllo INAD" che avvisa: "PEC inserita non corrispondente con PEC estratta e valida su archivio INAD. Vuoi aggiornare il campo PEC con la MAIL estratta (test@pec.it)?" con pulsanti F5-Conferma e F8-Annulla]

[Schermata: finestra di dialogo "Attenzione" con messaggio: "Codice Fiscale errato, impossibile effettuare il controllo"]

---

## Controllo massivo al momento della registrazione

Se il controllo non viene fatto singolarmente per ciascun soggetto destinatario, viene fatto **massivamente su tutti i soggetti al momento del Registra**.

- Dove manca il Codice Fiscale o la PEC non corrisponde a quella presente in INAD, lo stato viene indicato come **"Da Verificare"** e nella colonna **"Messaggio"** è indicato il motivo.
- In caso di PEC non corrispondente, si può scegliere dalle opzioni se lasciare il valore inserito o se utilizzare l'indirizzo estrapolato dall'INAD.

[Schermata: finestra "Controllo INAD" con tabella contenente colonne: Descrizione, Codice Fiscale, PEC/Mail, Messaggio, Opzioni, Stato. Esempi di messaggi: "PEC inserita non corrispondente con...", "Codice Fiscale non inserito, impossibile...". Stato: "Da Verificare". Pulsante "Prosegui" in basso]

[Schermata: finestra "Controllo INAD" con menu a tendina nella colonna "Opzioni" che mostra le scelte: "Da Verificare", "Utilizza valore inserito", "Utilizza valore estratto"]

- Se il campo **Codice Fiscale non è stato compilato**, è possibile lasciarlo vuoto o inserirlo in questa fase. Di nuovo sarà ripetuto il controllo sulla correttezza formale del Codice Fiscale.

Dopo la registrazione del protocollo, nella maschera riepilogativa, comparirà il **numero di controlli fatti**.

[Schermata: maschera riepilogativa "Registrato" con "Registrazione protocollo N. 000044", Segnatura, Data, Titolare e indicatore "Controllo INAD: 3 / 3"]

---

## Configurazione e ambito di attivazione

Il controllo è attivo per:

- **Tipi Soggetto:** "Persona fisica" e "Indefinito"
- **Tipologie Spedizione** che hanno il flag **"Attiva Controllo Massivo INAD"**

[Schermata: menu a tendina "Tipo soggetto" con opzioni: Indefinito, Persona fisica, Persona giuridica, Pubblica Amministrazione Italiana, Pubblica Amministrazione estera]

[Schermata: finestra "Tipologia Spedizione" con campi Codice (EML), Descrizione (EMAIL), Tipologia (Analogica), e checkbox "Attiva Controllo Massivo INAD" spuntata]