# Tabella delle diciture

La tabella delle diciture gestisce i nominativi stampati nelle firme di Anagrafe, Stato Civile ed Elettorale: la sua compilazione è in carico al cliente che conoscendo l'organizzazione interna del proprio settore può gestirle in autonomia.

## Accesso al programma

Per accedere al programma seguite questo percorso:

**150. Servizi Demografici - 10. Anagrafe - 80. Tabelle - 10. Generiche - 60. Tabella Diciture**

Una volta effettuato l'accesso vi verranno rese a video tutte le diciture standard inserite nell'applicativo: i codici dicitura maggiori di 1000 sono standard, forniti dalla ditta, per i quali è sconsigliata la modifica dell'intestazione, potete modificare il nome dell'incaricato. I nuovi codici, creati da voi, avranno valori inferiori a 1000.

[Schermata: Tabella Diciture con elenco di codici standard (1001 Il Sindaco, 1002 Il Segretario Generale, 1003 Il Responsabile Servizi Demografici, 1004 Il Responsabile Uff. Anagrafe, 1005 Il Responsabile Uff. Elettorale, 1006 Il Responsabile Uff. Stato Civile, 1007 L'Ufficiale d'Anagrafe) con colonne Codice, Etichetta, Valore e pulsanti di modifica/annullamento]

## Compilare un codice esistente

Per compilare un codice esistente fate click sul pulsante di modifica a sinistra della riga che volete modificare e vi si aprirà la funzione di modifica della dicitura. Modificate in corrispondenza del campo **valore** e cliccate su **aggiungi** per registrare la modifica. Se modificate una dicitura questa sarà aggiornata in automatico sui testi che la contengono, controlla le informazioni di tutta la guida per gestire i testi DOCX.

> **NB:** per i codici maggiori di 1000 si sconsiglia di modificare l'etichetta, ossia l'intestazione della firma.

[Schermata: Funzione di modifica della dicitura con campi Codice (1003), Etichetta (Il Responsabile Servizi Demografici), Valore (Inserire il valore), Annullata, e pulsanti Aggiorna, Altra Ricerca, Cancella, Torna Elenco. Sezione Audit con Ultima modifica e Effettuata da]

## Creare un nuovo codice

Per creare un nuovo codice, partendo dalla videata che ripropone tutte le diciture, spostatevi a destra e cliccate sul pulsante **NUOVO** compilate come segue:

1. **Etichetta** è l'intestazione che troverete stampata sui testi, potete intestarlo a qualsiasi soggetto interno all'ente o esterno; per esempio: Direttore Azienda Ospedaliera Universitaria, Ordine degli Avvocati e altre.
2. **Valore** inserite il Cognome + Nome della persona che ricopre l'incarico che avete messo nell'etichetta, può anche essere vuoto se non volete venga stampato nulla

procedete cliccando su **AGGIUNGI** a destra per inserire il dato

[Schermata: Procedura di creazione nuovo codice - 1) Click sul pulsante "Nuovo" nella tabella diciture; 2) Compilazione campi Etichetta e Valore; 3) Click sul pulsante "Aggiungi"]

## Inserire e gestire la variabile sui testi DOCX

Una volta che avete creato una nuova dicitura per un **Testo personalizzato dal cliente** è possibile inserirla all'interno di quel testo: di seguito le indicazioni sulla gestione dei testi standard, che sono del fornitore, e testi personalizzati di proprietà del cliente.

### Inserire in testo Standard

La modifica di un testo standard è consentita solo dal fornitore quindi potete:

1. Segnalarci qualora un testo pensiate necessiti di modifiche
2. Personalizzare il testo copiandolo e creandone uno ad uso cliente oppure usando la funzione di **RENDI MIO**

L'applicativo CWOL - Servizi Demografici consente un alto grado di personalizzazione della gestione testi e di molte altre funzionalità che permettono all'utente finale, attraverso guide e formazione, di diventare autonomo nel plasmare l'applicativo sulle proprie esigenze.

### Inserire in testo Personalizzato

Se avete personalizzato un testo, usando **RENDI MIO** o **NUOVO+COPIA DA** potete aggiungere la dicitura all'interno del testo per farlo seguite questi passaggi:

Aprite il menu e nella barra di ricerca digitate **DOCX**, vi verranno proposti 3 programmi di gestione testi divisi per area di lavoro, Anagrafe, Elettorale e Stato Civile:

- Servizi Demografici>Anagrafe>Tabelle>Progressivi/Personalizzazione>Testi Docx
- Servizi Demografici>Elettorale>Tabelle>Progressivi/Personalizzazione>Testi Docx
- Servizi Demografici>Stato Civile>Tabelle>Personalizzazione>Testi Docx

[Schermata: Menu applicazioni con ricerca "docx" che mostra i 3 programmi di gestione testi per Anagrafe, Elettorale e Stato Civile]

cliccate sul programma che contiene il testo nel quale volete aggiungere le diciture, è necessario creare prima il testo personalizzato con le funzioni citate in precedenza, e ricercate il testo. Per ricercarlo usate il campo **descrizione** inserendo una parola chiave:

[Schermata: Ricerca documenti base con campo Descrizione per inserire parola chiave e pulsante F4-Elenco]

Vi verranno resi i testi che corrispondono (contengono) la parola chiave che avete inserito, selezionate quello da modificare con doppio clic e poi cliccate su **apri e visualizza**:

[Schermata: Elenco documenti base con campi Codice, Descrizione, Cod. Numerico e pulsanti F6-Aggiorna, Apri / Visualizza]

vi si aprirà in un'altra tab del browser (google, firefox...) l'ONLYOFFICE per la modifica del documento, posizionatevi in corrispondenza delle variabili legate alla dicitura che sono:

1. **Variabile per Etichetta:** `@{$DICITURE→campo('etichetta(codice-etichetta)')}@` esempio pratico `@{$DICITURE→campo('etichetta(1016)')}@`
2. **Variabile per Valore:** `@{$DICITURE→campo('valore(codice-etichetta)')}@` esempio pratico `@{$DICITURE→campo('valore(1016)')}@`

Una volta che vi siete posizionati dove volete inserire o modificare la dicitura:

- se la volete **modificare**, cambiate solo il codice numerico che trovate tra parentesi, questo identifica la dicitura contenuta nella tabella; quindi se avete creato un nuovo codice che ha valore 1 andrete a sostituirlo al codice esistente:

### Esempio

| COSA VEDO NEL TESTO | PRIMA DELLA MODIFICA | DOPO LA MODIFICA |
|---|---|---|
| Intestazione dicitura | `@{$DICITURE→campo('etichetta(1016)')}@` | `@{$DICITURE→campo('etichetta(1001)')}@` |
| Valore dicitura | `@{$DICITURE→campo('valore(1016)')}@` | `@{$DICITURE→campo('valore(1001)')}@` |

- Se invece nel testo personalizzato non vi era una dicitura e la volete **aggiungere** posizionatevi nella parte del testo dove volete che questa sia presente e scrivete/incollate le variabili che trovate in questa guida, scrivendo già il codice al quale fanno riferimento.

Chiudete l'ONLYOFFICE in modo che le modifiche vengano registrate e rilanciate in stampa il testo per controllare il posizionamento e la corretta sintassi delle variabili.