# Configurazione delle Comunicazioni per Ufficio

## Introduzione

Sono delle stampe legate a delle causali anagrafiche, per esempio le comunicazioni di aggiornamento all'anagrafe sanitaria ASL, le comunicazioni dall'ufficio anagrafe a quello elettorale oppure alla leva militare.

Queste sono gestite, modificabili e personalizzabili attraverso **2 programmi**:

- **STAMPA COMUNICAZIONI**, che permette di selezionare un ufficio/destinatario e stampare degli elenchi a seconda delle causali anagrafiche.

  Percorsi:

  - `Servizi Demografici; Anagrafe; Variazioni; STAMPA COMUNICAZIONI`
  - `Servizi Demografici, Elettorale; Manutenzione; Stampe; STAMPA COMUNICAZIONI`

- **DESTINATARI COMUNICAZIONI**, serve a collegare una variazione anagrafica ad un testo da stampare. È necessario configurarle in questa tabella per poi stamparle.

  Percorso:

  - `Servizi Demografici; Anagrafe; Tabelle; per Variazioni Anagrafiche; DESTINATARI COMUNICAZIONI`

---

## Procedura di configurazione

### 1) Creare la testata della comunicazione

Accedere al programma **DESTINATARI COMUNICAZIONI** dal percorso indicato sopra e all'accesso cliccare **NUOVO** sulla destra.

Compilare i seguenti campi:

- **Id**: numeri maggiori di 10
- **Descrizione**: ASL, Questura, Segretariato ecc. (oppure il titolo desiderato)
- **Primo periodo di variazione dell'estrazione**: data da – data al

[Schermata: finestra "Comunicazioni da Variazioni Anagrafiche" con campi Id*, Descrizione*, Data Comunicazione iniziale, Data Comunicazione finale e pulsanti Aggiungi / Torna Elenco / Comunicazioni]

---

### 2) Configurare la comunicazione

Una volta creata la testata, è necessario configurarla associando alla comunicazione appena creata le **causali di estrazione** ed i **testi di stampa**.

Da lì cliccare su **Nuovo** e aggiungere le variazioni anagrafiche collegandole al testo da stampare.

Compilare:

a) **Scegliete la variazione anagrafica** [Rosso]: dalla lentina selezionare le variazioni anagrafiche per la quale viene fatta l'estrazione
b) **Scegliete il testo**
c) **Indicate il numero di copie da stampare**

[Schermata: finestra "Comunicazioni ai Destinatari" con campi Codice Dest., Causale Variazione*, Codice Testo, Copie, Tipo Ufficio (Anagrafe) e pulsanti Aggiungi / Torna Elenco]

---

## Esempi di configurazione

### Esempio ASL

Di seguito un esempio che si può riprodurre:

[Schermata: tabella "Comunicazioni ai destinatari" con Codice Dest. = 1, Descrizione Dest. = ASL]

| Causale | Desc.Causale | Descrizione Testo | Copie | Tipo Ufficio | Codice Testo |
|---------|-------------|-------------------|-------|--------------|--------------|
| 1.7.5 | Riconsegna Accertata (entro 45gg) | Elenco Immigrati Da Anagrafe per ASL | 1 | Anagrafe | owd_elencimmigratidaAnagrafeASL |
| 1.7.9 | Iscrizione per Altri Motivi Accertata (entro 45gg) | Elenco Immigrati Da Anagrafe per ASL | 1 | Anagrafe | owd_elencimmigratidaAnagrafeASL |
| 1.7.10 | Ripristino Iscriz.per Altri Motivi registrata (entro 45gg) | Elenco Immigrati Da Anagrafe per ASL | 1 | Anagrafe | owd_elencimmigratidaAnagrafeASL |
| 1.4.2 | Immigrazione | Elenco Immigrati Da Anagrafe per ASL | 1 | Anagrafe | owd_elencimmigratidaAnagrafeASL |
| 1.4.3 | Iscrizione d'Ufficio | Elenco Immigrati Da Anagrafe per ASL | 1 | Anagrafe | owd_elencimmigratidaAnagrafeASL |
| 1.4.4 | Riconsegna | Elenco Immigrati Da Anagrafe per ASL | 1 | Anagrafe | owd_elencimmigratidaAnagrafeASL |
| 1.4.7 | Iscrizione per altri motivi | Elenco Immigrati Da Anagrafe per ASL | 1 | Anagrafe | owd_elencimmigratidaAnagrafeASL |
| 1.8.6 | Canc.per Altri Motivi Confermata | Elenco Immigrati Da Anagrafe per ASL | 1 | Anagrafe | owd_elencimmigratidaAnagrafeASL |
| 1.6.3 | Emigrazione | Elenco Emigrati Da Anagrafe ASL | 1 | Anagrafe | owd_elencimmigratidaAnagrafeASL |
| 1.6.4 | Irreperibilità | Elenco Emigrati Da Anagrafe ASL | 1 | Anagrafe | owd_elencimmigratidaAnagrafeASL |
| 1.6.5 | Cancellazione d'ufficio | Elenco Emigrati Da Anagrafe ASL | 1 | Anagrafe | owd_elencimmigratidaAnagrafeASL |
| 1.6.7 | Cancellazione per altri motivi | Elenco Emigrati Da Anagrafe ASL | 1 | Anagrafe | owd_elencimmigratidaAnagrafeASL |
| 1.9.2 | Emigrazione Confermata (apri da altro comune O chiusa pratica dopo inc.) | Elenco Emigrati Da Anagrafe ASL | 1 | Anagrafe | owd_elencimmigratidaAnagrafeASL |
| 1.7.2 | Immigrazione Accertata (entro 45gg) | Comunicazione Anagrafe Elenco cambi Indirizzo ASL | 1 | Anagrafe | owd_elencambiIndirizzo |
| 1.6.1 | Morte | Elenco Cambi Indirizzi Da Anagrafe per ASL | 1 | Anagrafe | owd_elencambiIndirizzoASL |
| 1.6.6 | Impossibilità di Censimento | Elenco Cambi Indirizzi Da Anagrafe per ASL | 1 | Anagrafe | owd_elencambiIndirizzoASL |
| 1.5.2 | Variazione Residenza Accertata (entro 45gg) | Elenco Cambi Indirizzi Da Anagrafe per ASL | 1 | Anagrafe | owd_elencambiIndirizzoASL |
| 1.5.4 | Scissione di Famiglia Accertata (entro 45gg) | Elenco Cambi Indirizzi Da Anagrafe per ASL | 1 | Anagrafe | owd_elencambiIndirizzoASL |
| 1.5.1 | Morte | Elenco Cambi Indirizzi Da Anagrafe per ASL | 1 | Anagrafe | owd_elencambiIndirizzoASL |
| 1.5.3 | Morte | Elenco Cambi Indirizzi Da Anagrafe per ASL | 1 | Anagrafe | owd_elencambiIndirizzoASL |
| 1.5.19 | Variazione numero civico d'ufficio (o famiglia) | Elenco Cambi Indirizzi Da Anagrafe per ASL | 1 | Anagrafe | owd_elencambiIndirizzoASL |
| 1.5.20 | Variazione residenza d'ufficio | Elenco Cambi Indirizzi Da Anagrafe per ASL | 1 | Anagrafe | owd_elencambiIndirizzoASL |
| 1.5.29 | Cambio denominazione Via (cumulativo) | Elenco Cambi Indirizzi Da Anagrafe per ASL | 1 | Anagrafe | owd_elencambiIndirizzoASL |
| 3.5.1 | Atto di Morte | Comunicazione di Morte per Stato Civile | 1 | Stato Civile | owd_ComunicazioneDecessoStatoCivile |
| 1.6.2 | Morte presunta | Comunicazione di Morte generica_X | 1 | Anagrafe | owd_comunicazionemorteemergenza |

---

### Esempio Elettorale

#### Cancellazioni

[Schermata: tabella "Comunicazioni ai destinatari" con Codice Dest. vuoto, Descrizione Dest. = Elettorale Cancellazioni]

| Causale | Desc.Causale | Descrizione Testo | Copie | Tipo Ufficio | Codice Testo |
|---------|-------------|-------------------|-------|--------------|--------------|
| 1.9.2 | Emigrazione Confermata (apri da altro comune O chiusa pratica dopo Acquisizione Cittadinanza Italiana per Elett | | 1 | Anagrafe | owd_acqCittadItalianaEle |
| 1.6.1 | Morte | Comunicazione di Morte per Elettorale | 1 | Anagrafe | owd_ComunicazioneDeces |
| 3.5.1 | Atto di Morte | Comunicazione di Morte per Elettorale | 1 | Stato Civile | owd_ComunicazioneDeces |

#### Iscrizioni

[Schermata: tabella "Comunicazioni ai destinatari" con Codice Dest. vuoto, Descrizione Dest. = Elettorali Iscrizioni]

| Causale | Desc.Causale | Descrizione Testo | Copie | Tipo Ufficio | Codice Testo |
|---------|-------------|-------------------|-------|--------------|--------------|
| 1.7.2 | Immigrazione Accertata (entro 45gg) | | 1 | Anagrafe | |
| 1.7.5 | Riconsegna Accertata (entro 45gg) | | 1 | Anagrafe | |
| 1.7.9 | Iscrizione per Altri Motivi Accertata (entro 45gg) | | 1 | Anagrafe | |
| 1.7.10 | Ripristino Iscriz.per Altri Motivi registrata (entro 45gg) | | 1 | Anagrafe | |
| 1.4.2 | Immigrazione | | 1 | Anagrafe | |
| 1.4.3 | Iscrizione d'Ufficio | | 1 | Anagrafe | |
| 1.4.4 | Riconsegna | | 1 | Anagrafe | |
| 1.4.7 | Iscrizione per altri motivi | | 1 | Anagrafe | |
| 1.5.16 | Acquisto cittadinanza Italiana | | 1 | Anagrafe | |
| 3.4.1 | Acquisto cittadinanza Italiana da registrare in Anagrafe | | 1 | Stato Civile | |

---

## Personalizzazione dei testi

I testi proposti possono essere personalizzati rendendoli propri. Per la guida sui testi, consultare la documentazione dedicata (link "guide sui testi" a fondo pagina).