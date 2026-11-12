# Configurazione delle Comunicazioni per Ufficio

Di cosa parliamo? Sono delle stampe legate a delle causali anagrafiche, per esempio le comunicazioni di aggiornamento all'anagrafe sanitaria ASL, le comunicazioni dall'ufficio anagrafe a quello elettorale oppure alla leva militare.

Queste sono gestite, modificabili e personalizzabili attraverso 2 programmi:

- **STAMPA COMUNICAZIONI**, che vi permette di selezionare un ufficio/destinatario e stampare degli elenchi a seconda delle causali anagrafiche. Questo programma lo trovate al percorso:

  - *Servizi Demografici; Anagrafe; Variazioni; STAMPA COMUNICAZIONI*
  - *Servizi Demografici, Elettorale; Manutenzione; Stampe; STAMPA COMUNICAZIONI*

- **DESTINATARI COMUNICAZIONI**, serve a collegare una variazione anagrafica ad un testo da stampare. È necessario configurarle in questa tabella per poi stamparle. Il programma lo trovate a questo percorso:

  - *Servizi Demografici; Anagrafe; Tabelle; per Variazioni Anagrafiche; DESTINATARI COMUNICAZIONI*

---

## Procedura di configurazione

### 1) Creare la testata della comunicazione

Accedere al programma **STAMPA COMUNICAZIONI** dal percorso indicato sopra e all'accesso cliccate **NUOVO** sulla destra:

[Schermata: finestra "Stampa Comunicazioni" con elenco vuoto e pulsante "Nuovo" evidenziato in alto a destra]

Compilate poi il destinatario (ASL, Questura, Segretariato ecc.) o dategli il titolo che volete e selezionate il primo periodo di variazione dell'estrazione (data da – data al).

[Schermata: form di compilazione con campi: Destinatario comunicazione, Periodo di variazione comunicazioni (Data Iniziale / Data Finale), Periodo di variazione da comunicare (Data Iniziale* / Data Finale*), Tipo Ufficio (Tutti), checkbox "Simulare Variazioni Sospese", campo NOTE]

---

### 2) Configurare le causali e i testi di stampa

Una volta fatto questo dovete configurarla e per farlo accedete al programma **DESTINATARI COMUNICAZIONI**, dove assocerete alla comunicazione appena creata le causali di estrazione ed i testi di stampa.

Quindi accedete a **DESTINATARI COMUNICAZIONI** e selezionate la comunicazione che avete creato poco fa (diventa gialla), e selezionate il pulsante **Comunicazioni** sulla destra:

[Schermata: finestra "Destinatari Comunicazioni" con elenco, riga "Elettorale Cancellazioni" evidenziata in giallo e pulsante "Comunicazioni" evidenziato a destra]

Da lì cliccate su **Nuovo** e aggiungete le variazioni anagrafiche collegandole al testo da stampare.

[Schermata: finestra "Comunicazioni ai Destinatari" con campi: Codice Dest., Descrizione Dest., tabella vuota con colonne Causali, Desc.Causale, Descrizione Testo, Copie, Tipo Ufficio, Codice Testo, e pulsante "Nuovo" a destra]

Compilate:

a) **Scegliete la variazione anagrafica** [Rosso]: dalla lente di ingrandimento selezionare le variazioni anagrafiche per la quale viene fatta l'estrazione

b) **Scegliete il testo**

c) **Indicate il numero di copie da stampare**

[Schermata: form "Comunicazioni ai Destinatari" con campi: Codice Dest. (1), Causale Variazione* (campo evidenziato in rosso), Codice Testo, Copie (1), Tipo Ufficio (Anagrafe), pulsanti "Aggiungi" e "Torna Elenco"]

---

## Esempi di configurazione

### Esempio ASL

[Schermata: finestra "Comunicazioni ai Destinatari" – Codice Dest. 2, Descrizione Dest. "ASL"]

| Causale | Desc. Causale | Descrizione Testo | Copie | Tipo Ufficio | Codice Testo |
|---------|---------------|-------------------|-------|--------------|--------------|
| 1.3.5 | Ricomparsa Accertata (entro 45gg) | Elenco Immigrati Da Anagrafe ASL | 1 | Anagrafe | owd_elencoimmigratidaAnagrafeASL |
| 1.7.9 | Iscrizione per Altri Motivi Accertata (entro 45gg) | Elenco Immigrati Da Anagrafe ASL | 1 | Anagrafe | owd_elencoimmigratidaAnagrafeASL |
| 1.7.10 | Ripristino Iscriz. per Altri Motivi registrata (entro 45gg) | Elenco Immigrati Da Anagrafe ASL | 1 | Anagrafe | owd_elencoimmigratidaAnagrafeASL |
| 1.4.2 | Immigrazione | Elenco Immigrati Da Anagrafe ASL | 1 | Anagrafe | owd_elencoimmigratidaAnagrafeASL |
| 1.4.3 | Iscrizione d'Ufficio | Elenco Immigrati Da Anagrafe ASL | 1 | Anagrafe | owd_elencoimmigratidaAnagrafeASL |
| 1.4.4 | Ricomparsa | Elenco Immigrati Da Anagrafe ASL | 1 | Anagrafe | owd_elencoimmigratidaAnagrafeASL |
| 1.4.7 | Iscrizione per altri motivi | Elenco Immigrati Da Anagrafe ASL | 1 | Anagrafe | owd_elencoimmigratidaAnagrafeASL |
| 1.8.6 | Canc. per Altri Motivi Confermata | Elenco Emigrati Da Anagrafe ASL | 1 | Anagrafe | owd_elencoimmigratidaAnagrafeASL |
| 1.6.3 | Emigrazione | Elenco Emigrati Da Anagrafe ASL | 1 | Anagrafe | owd_elencoimmigratidaAnagrafeASL |
| 1.6.4 | Imperitabilità | Elenco Emigrati Da Anagrafe ASL | 1 | Anagrafe | owd_elencoimmigratidaAnagrafeASL |
| 1.6.5 | Cancellazione d'Ufficio | Elenco Emigrati Da Anagrafe ASL | 1 | Anagrafe | owd_elencoimmigratidaAnagrafeASL |
| 1.6.7 | Cancellazione per altri motivi | Elenco Emigrati Da Anagrafe ASL | 1 | Anagrafe | owd_elencoimmigratidaAnagrafeASL |
| 1.9.2 | Emigrazione Confermata (apri da altro comune O chiusa pratica dopo inc.) | Elenco Emigrati Da Anagrafe ASL | 1 | Anagrafe | owd_elencoimmigratidaAnagrafeASL |
| 1.7.2 | Immigrazione Accertata (entro 45gg) | Comunicazione Anagrafe Elenco cambi indirizzo ASL | 1 | Anagrafe | OWL_elencocambiaindirizzoASL |
| 1.6.1 | Morte | Elenco Cambi Indirizzi Da Anagrafe per ASL | 1 | Anagrafe | OWL_elencocambiaindirizzoASL |
| 1.6.6 | Imperitabilità o Cessamento | Elenco Emigrati Da Anagrafe ASL | 1 | Anagrafe | owd_elencoimmigratidaAnagrafeASL |
| 1.9.3 | Variazione Residenza Accertata (entro 45gg) | Elenco Cambi Indirizzi Da Anagrafe per ASL | 1 | Anagrafe | owd_elencocambiaindirizzoASL |
| 1.9.4 | Scissione di Famiglia Accertata (entro 45gg) | Elenco Cambi Indirizzi Da Anagrafe per ASL | 1 | Anagrafe | owd_elencocambiaindirizzoASL |
| 1.5.1 | — | Elenco Cambi Indirizzi Da Anagrafe per ASL | 1 | Anagrafe | owd_elencocambiaindirizzoASL |
| 1.5.3 | — | Elenco Cambi Indirizzi Da Anagrafe per ASL | 1 | Anagrafe | owd_elencocambiaindirizzoASL |
| 1.5.19 | Variazione numero civico (ufficio o famiglia) | Elenco Cambi Indirizzi Da Anagrafe per ASL | 1 | Anagrafe | owd_elencocambiaindirizzoASL |
| 1.5.20 | Variazione residenza d'ufficio | Elenco Cambi Indirizzi Da Anagrafe per ASL | 1 | Anagrafe | owd_elencocambiaindirizzoASL |
| 1.5.23 | — | Elenco Cambi Indirizzi Da Anagrafe per ASL | 1 | Anagrafe | owd_elencocambiaindirizzoASL |
| 1.5.27 | Cambio denominazione Via (cumulativo) | Elenco Cambi Indirizzi Da Anagrafe per ASL | 1 | Anagrafe | owd_elencocambiaindirizzoASL |
| 3.3.1 | Atto di Morte | Comunicazione di Morte per Stato Civile | 1 | Stato Civile | owd_ComunicazioneMorteStatoCivile |
| 1.6.2 | Morte presunta | Comunicazione di Morte generica_X | 1 | Anagrafe | owd_ComunicazioneMorteEmergenza |

---

### Esempio Elettorale

#### Elettorale Cancellazioni

[Schermata: finestra "Comunicazioni ai Destinatari" – Codice Dest. vuoto, Descrizione Dest. "Elettorale Cancellazioni"]

| Causale | Desc. Causale | Descrizione Testo | Copie | Tipo Ufficio | Codice Testo |
|---------|---------------|-------------------|-------|--------------|--------------|
| 1.9.2 | Emigrazione Confermata (apri da altro comune O chiusa pratica dopo inc.) | Acquisizione Cittadinanza Italiana per Eletti | 1 | Anagrafe | owd_acqCittadItalianaElett |
| 1.6.1 | Morte | Comunicazione di Morte per Elettorale | 1 | Anagrafe | owd_ComunicazioneDeced |
| 3.3.1 | Atto di Morte | Comunicazione di Morte per Elettorale | 1 | Stato Civile | owd_ComunicazioneDeced |

#### Elettorali Iscrizioni

[Schermata: finestra "Comunicazioni ai Destinatari" – Codice Dest. vuoto, Descrizione Dest. "Elettorali Iscrizioni"]

| Causale | Desc. Causale | Descrizione Testo | Copie | Tipo Ufficio | Codice Testo |
|---------|---------------|-------------------|-------|--------------|--------------|
| 1.7.2 | Immigrazione Accertata (entro 45gg) | — | 1 | Anagrafe | — |
| 1.7.5 | Ricomparsa Accertata (entro 45gg) | — | 1 | Anagrafe | — |
| 1.7.9 | Iscrizione per Altri Motivi Accertata (entro 45gg) | — | 1 | Anagrafe | — |
| 1.7.10 | Ripristino Iscriz. per Altri Motivi registrata (entro 45gg) | — | 1 | Anagrafe | — |
| 1.4.2 | Immigrazione | — | 1 | Anagrafe | — |
| 1.4.3 | Iscrizione d'Ufficio | — | 1 | Anagrafe | — |
| 1.4.4 | Ricomparsa | — | 1 | Anagrafe | — |
| 1.4.7 | Iscrizione per altri motivi | — | 1 | Anagrafe | — |
| 1.5.16 | Acquisto cittadinanza Italiana | — | 1 | Anagrafe | — |
| 3.4.1 | Acquisto cittadinanza Italiana da registrare in Anagrafe | — | 1 | Stato Civile | — |

---

## Personalizzazione dei testi

I testi che vengono proposti possono essere personalizzati rendendoli propri. Per la guida sui testi, consultare la documentazione dedicata.