# Digitalizzazione Liste Elettorali CWOL

Dopo aver ricevuto l'autorizzazione a poter digitalizzare le Liste elettorali procedere come segue:

## 1. Aggiornamento Elettorale da Anagrafe

A Dicembre di ogni anno, dopo la conferma della revisione semestrale e dopo aver lanciato le variazioni ExtraRevisione (senza aggiornare professione e titolo di studio), vedi maschera:

[Schermata: Maschera "Aggiorna Elettorale da Anagrafe" con avviso ATTENZIONE: "Non eseguire questo programma durante una revisione dinamica: l'aggiornamento effettivo potrebbe essere sovrascritto dalla revisione...". Tipo Lista: "1 - Liste Elettorali". Sezione "Segnala le differenze tra Anagrafe e Elettorale per:" con checkbox: Variazione indirizzo italiano ✓, Variazione indirizzo estero ✓, Professione ☐, Titolo di studio ☐, Stato Civile e nome coniuge (solo per femmine) ✓, Nominativo ☐, Luogo e data di Nascita ✓, Atto di Nascita ✓. In basso: Creazione Archivio ✓, Stampa estratti ✓, Considera civico interno ☐, variare elettore solo se non cambiata sezione ☐]

## 2. Apertura della Revisione di Ricompilazione Liste

Aprire la revisione di ricompilazione liste.

> **TALE REVISIONE NON VA' APERTA LO STESSO GIORNO DELLA CHIUSURA DELLA SEMESTRALE MA DAL GIORNO DOPO**

ES.: chiusura semestrale e lancio variazioni extrarevisione il 20.12.20xx → La ricompilazione **VA' FATTA dal giorno 21.12.20xx a seguire**

[Schermata: Maschera "Apertura Revisione" con dropdown "Revisione da aprire:" che mostra le opzioni: Selezionare..., BLOCCO LISTE, Blocco Liste LISTE AGGIUNTE, DINAMICA ALTRI MOTIVI ISCRIZ. 30° GIORNO, Dinamica 1° Tornata LISTE AGGIUNTE, Dinamica 2° Tornata LISTE AGGIUNTE, **RICOMPILAZIONE LISTE ELETTORALI** (evidenziato), Ricompilazione LISTE AGGIUNTE, Semestrale LISTE AGGIUNTE]

## 3. Lanciare i Punti Evidenziati

- Rinumerare le liste Generali **SOLO** se si è avuta l'autorizzazione, altrimenti limitarsi alle liste sezionali

[Schermata: Albero "RICOMPILAZIONE LISTE ELETTORALI" con i punti da eseguire evidenziati in rosso:
- ○ Copia Elettorale per Ricompilazione
- ○ Aggiunta modifiche da Semestrale
- ○ Variazione Elettori in archivio di Copia
- ○ Azzeramento numero Lista Generale per iscritti da Semestrale
- ○ **Rinumerazione Liste Sezionali**
- ○ **Rinumerazione Liste Generali**
- ○ Stampa Liste Sezionali rinumerate
- ○ Stampa Liste Generali rinumerate
- ○ Recupero numero Lista Generale da iscrivendi Semestrale
- ○ **Conteggio elettori per verifica**
- ○ **Stampa Verbale**
- ○ **CONFERMA ricompilazione**]

> ⚠️ **ATTENZIONE** – prima di confermare la revisione controllare con stampa prospetti che i numeri siano corrispondenti con il prospetto finale della semestrale.

## 4. Maschera di Conferma

Nella maschera di conferma selezionare **entrambe** solo se avete avuto l'autorizzazione a rinumerare anche le generali, altrimenti solo le **sezionali**.

[Schermata: Maschera "Programma Elettorale" con Revisione "6 - RICOMPILAZIONE LISTE ELETTORALI". La revisione deve essere: Confermata. Ricompilate liste: dropdown con opzioni "Entrambe", "Sezionali", "Generali". Data e Nr. Verbale. Codice rev. semestrale da chiudere. ATTENZIONE! "Per motivi tecnici si raccomanda di non eseguire revisioni nella stessa data della conferma ricompilazione!"]

## 5. Verifica Tabella di Personalizzazione City-People Elettorale

Dopo aver chiuso la revisione di ricompilazione verificare che nella tabella di personalizzazione City-People Elettorale sia presente la data della ricompilazione liste sezionali e se autorizzati anche delle generali.

Percorso menu: `150. Servizi Demografici` → `10. Anagrafe` → `20. Elettorale` → `20. Tabelle` → `20. Progressivi` → `40. Personalizzazione Elettorale`

[Schermata: Maschera "Personalizzazione" con tab "Attribuzioni" attiva. Campi evidenziati in rosso: "Data ricomp. liste sezionali: 30/06/2018" e "Data ricomp. liste generali: (vuoto)". Altri campi visibili: Attribuzione Sezione agli Aire, Sezione per Aire (se fissa), Uso dei fascicoli liberi?, Tipo Diritti per certificazione Elettorale: E - Esente, Impostare data Notifica Tessera? ✓, 3D-XML = Tessera Consegnata ✓, Ambiente CWOL: 2 - Attivato]

## 6. Generazione dei PDF

Per la generazione dei PDF procedere come segue:

Percorso menu: `150. Servizi Demografici` → `10. Anagrafe` → `20. Elettorale` → `20. Manutenzione` → `80. Stampe` → Selezionare:
- **50. Liste sezionali digitali, dopo revisione**
- **60. Liste generali digitali, dopo revisione**
- **70. Liste sezionali digitali ricompilate**
- **80. Liste generali digitali ricompilate**

## 7. Compilazione della Videata di Stampa

Nella videata compilare come segue inserendo il tipo lista, il codice del testo da stampare e le sezioni:

[Schermata: Maschera "Stampa Liste Sezionali Digitali" con campi:
- Tipo Lista: **1 - Liste Elettorali**
- Data Ricompilazione Liste: 30/06/2018
- Testo: **Avd ListeSezionali Digitali** / **QL Liste Sezionali digitali**
- Sesso: Maschi
- Sezione elettorale da: **1** a **17**
- Num. lista sez. da: 0 a 0
- Timbro finale: (anteprima del testo del verbale con data e firma del Responsabile dell'Ufficio Elettorale)]

> ⚠️ **Attenzione**: prima di utilizzare questa funzione deve essere stato sistemato lo storico elettorale dall'assistenza PAL. Produce la ristampa della lista sezionale dalla data ricompilazione, con i salti pagina ad ogni revisione.

Accertati che i dati del verbale e tutto il timbro siano corretti prima di confermare. In fase di stampa la scritta `@elettori@` verrà sostituita con il numero degli elettori.

### Stampa in PDF

Una volta generato il file ed aperto occorre andare in stampa e come stampante selezionare **PDF Creator** e premere **OK**.

[Schermata: Finestra di stampa con "Destinazione: PDFCreator", Pagine: Tutti, Copie: 1, A colori: A colori]

### Configurazione PDF/A

A questo punto, seleziona la voce **PDF/A (conservazione a lungo termine)** dal menu a tendina **Profilo** annesso alla nuova finestra che si apre a schermo, digita, se lo desideri, le informazioni su **Titolo**, **Autore**, **Soggetto** e **Parola chiave** del documento, imposta se necessario il percorso di salvataggio dello stesso pigiando sul pulsante **[...]** e finalizza l'esportazione cliccando sul pulsante **Salva**.

[Schermata: Finestra "PDFCREATOR FREE 5.1.2" con:
- Profilo: **PDF/A (conservazione a lungo termine)**
- Nomefile: Liste Sezionali Digitali Maschili
- Cartella: C:\Users\v.angeletti\Documents
- Titolo: CWOL - Dev
- Autore: v.angeletti
- Soggetto: (vuoto)
- Parola chiave: (vuoto)
- Pulsanti: Annulla, Unisci, Email, **Salva**]

## 8. Verifica del PDF Generato

Per una verifica se tutto è andato a buon fine, aprendo il file PDF in alto deve comparire la dicitura:

> ℹ️ Il file è conforme allo **standard PDF/A ed è stato aperto in sola lettura per evitare modifiche.**

## 9. Revisioni Dinamiche Successive

Da questo momento in poi per ogni revisione Dinamica **non devono più essere stampate le code** ma la revisione deve essere eseguita fino alla conferma finale e poi si torna nel programma stampe e vengono stampate nuovamente le liste digitali dopo revisione.

Percorso: `80. Stampe` → **50. Liste sezionali digitali, dopo revisione** / **60. Liste generali digitali, dopo revisione**

Le liste digitali conterranno:

- I **cancellati con sfondo grigio** e gli estremi della cancellazione (es. "Cancellato con verbale 1 del 05/01/2021 per Emigrazione")
- I **nuovi aggiunti in coda**

## 10. Liste Aggiunte

L'operazione di Ricompilazione liste deve essere eseguita anche per tutte le **liste aggiunte attive** presenti nel comune.

Percorso: `Apertura Revisione` → Revisione da aprire: **Ricompilazione LISTE AGGIUNTE** → Tipo Lista: selezionare tra:
- 7 - provincia di Bolzano
- 2 - provincia di Trento
- 4 - Regione Valle d'Aosta
- 5 - UE Comunali
- 3 - UE Parlamento Europee

## 11. Ciclo Annuale

A dicembre di ogni anno viene rieseguita l'operazione di ricompilazione delle Liste e si ripete l'intero ciclo.