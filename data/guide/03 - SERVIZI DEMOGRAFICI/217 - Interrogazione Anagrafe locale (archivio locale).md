# Interrogazione Anagrafe locale (archivio locale)

**Autorizzazione richiesta:** DAN\1 (anagrafe semplificata) o DAN\2 (anagrafe completa)

Permette la ricerca e consultazione dei cittadini iscritti all'APR o AIRE, all'anagrafe dei temporanei oppure dei soggetti non residenti i cui dati sono disponibili perché sono state emesse carte d'identità o atti di Stato Civile a loro nome.

## Criteri di ricerca parziale

Quando viene visualizzata la paginazione di vari elementi di una tabella, è generalmente possibile effettuare la loro selezione parziale in base al codice e/o alla descrizione. Il risultato della selezione segue, in generale, le seguenti regole:

- Se la ricerca è per **codice**, vengono visualizzati gli elementi con codice maggiore o uguale a quello specificato. **Attenzione:** se si indica un codice e questo non è presente in tabella, esso non sarà ovviamente visualizzato, ma l'elenco inizierà dal codice immediatamente superiore.
- Se la ricerca è per **descrizione**, viene seguito il criterio mostrato nei seguenti esempi con una lista di nominativi:

| Contenuto campo selezione | Risultato in lista | Criterio |
|---|---|---|
| ro | Ronconi, Rosi, Rossi, Rossini | Quelli che iniziano per 'ro' |
| ro% | Ronconi, Rosi, Rossi, Rossini | Quelli che iniziano per 'ro' |
| rossi | Rossi, Rossini | Quelli che iniziano per 'rossi' |
| rossi% | Rossi, Rossini | Quelli che iniziano per 'rossi' |
| %ro% | De Rosa, De Rossi, Ronconi, Rosi, Rossi, Rossini | Quelli che contengono 'ro' |
| %rossi% | De Rossi, Rossi, Rossini | Quelli che contengono 'rossi' |
| %rossi | De Rossi, Rossi | Quelli che finiscono con 'rossi' |
| VUOTO | TUTTI | |

## Criteri di ricerca

È possibile ricercare per varie combinazioni i soggetti. La ricerca più comune è senz'altro quella per nome, ma sono anche possibili ricerche combinate, come ad esempio:

- Per **data di nascita** (volendo è anche possibile indicare solo mese e anno, oppure solo giorno e mese…)

  [Screenshot: form di ricerca con campo "Data nascita" compilato con 10/12/1976 evidenziato in rosso]

- Per **nome e anno di nascita** (volendo è anche possibile indicare solo mese e anno, oppure solo giorno e mese…)

  [Screenshot: form di ricerca con campo "Cognome" = ROSSI e "Data nascita" = 0/0/1976 evidenziati in rosso]

- Per **indirizzo** (a partire da un certo numero civico della via)

  [Screenshot: form di ricerca con campo "Via" = 41 CAVOUR e "Num. Civico" = 10 evidenziati in rosso]

- Per **nome e indirizzo**

  [Screenshot: form di ricerca con campo "Cognome" = ROSSI e "Via" = 41 CAVOUR evidenziati in rosso]

### Ricerca per famiglia ANPR / ID famiglia ANPR

È possibile ricercare una famiglia con corrispondenza ANPR sull'anagrafe locale utilizzando l'ID ANPR della famiglia, impostare il campo evidenziato in giallo:

[Screenshot: interfaccia "Interrogazione anagrafe" con il campo "Famiglia ANPR" evidenziato in giallo e i checkbox "Apr", "Aire", "Temporanei", "Non residenti", "Vedi anche Cancellati" selezionati]

## Criteri di esclusione/inclusione

**Attenzione** anche a scegliere correttamente la ricerca, utilizzando il significato dei vari flag anagrafe. I Flag (tipo famiglia, motivo iscrizione e motivo cancellazione), individuano il tipo di posizione anagrafica del soggetto, e lo stato della persona.

### Motivo iscrizione / Motivo cancellazione

| Motivo iscrizione | Motivo Cancellazione |
|---|---|
| N - Nascita (Apr-Aire) | E - emigrato (Apr) |
| I - Immigrazione (Apr) | I - irreperibile (Apr-Aire) |
| U - d'ufficio (Apr-Aire-temporanei) | M - morto (Apr-Aire) |
| C - Cittadinanza (Aire) | C - cittadinanza (Aire) |
| R - Ricomparsa (Apr-Aire) | R - rimpatrio (Aire) (nel comune o in altro comune) |
| E - Espatrio (Aire) | T - trasferito (Aire) |
| T - Trasferito (Aire) | D - domanda (temporanei) |
| D - Domanda (temporanei) | U - d'ufficio (temporanei) |

### Tipo famiglia

Individua il tipo di posizione anagrafica della persona. Il codice significa:

**Iscritti APR (Anagrafe Popolazione Residente):**

- Tipo Famiglia = **AN** Famiglie "normali" (non Convivenze)
- Tipo Famiglia = **CV** Convivenze

**Pratica APR** (viene utilizzato un codice diverso, provvisorio, per assegnare il vero numero di famiglia solo alla conferma) di creazione famiglia in corso (al termine si trasformeranno in AN o CV):

- Tipo Famiglia = **PA** Famiglie "normali" (non Convivenze)
- Tipo Famiglia = **PV** Convivenze

**Iscritti AIRE (Anagrafe Italiani Residenti Estero):**

- Tipo Famiglia = **FE** il numero di famiglia in questo caso, corrisponde a quello indicato sul modello AIRE/01

**Pratica AIRE (Anagrafe Italiani Residenti Estero):**

- Tipo Famiglia = **PI** nuova famiglia Aire, numero provvisorio.

**Iscritti nell'anagrafe dei Temporanei:**

- Tipo Famiglia = **TE**

**Non residenti.** Presenti perché sono stati emesse carte d'identità o atti di stato civile a loro nome:

- Tipo Famiglia = **vuoto**

## Ricerca Anagrafe - Paginazione

Una volta eseguita la ricerca si avrà l'elenco con il risultato della consultazione. Cliccando sul simbolo **"+"** si aprirà la finestra con l'elenco dei componenti della famiglia.

[Screenshot: tabella di risultati "Interrogazione Anagrafe" con colonne Stato, Famiglia, Cognome Nome, Sesso, Data Nascita, Luogo Nascita, Sc., Rel Par, Isc., Canc., Atto, Prat., Note, Allegati, Verif. e pannello funzioni a destra]

### Significato delle colonne nella paginazione:

- **Famiglia** → vedi [Tipo famiglia](#tipo-famiglia)
- **Isc.** → vedi [Motivo iscrizione](#motivo-iscrizione--motivo-cancellazione)
- **Canc.** → vedi [Motivo cancellazione](#motivo-iscrizione--motivo-cancellazione)
- **Atto** → Evidenzia se sono stati redatti degli Atti di Stato Civile, successivamente alla cancellazione anagrafica o come non residente.
- **Prat.** → Evidenzia se sono aperte delle pratiche relative al soggetto.
- **Note** → Evidenzia se sono state inserite delle note relative al soggetto.
- **Allegati** → Evidenzia se sono stati caricati documenti relativi a tale cittadino.
- **Verif.** → Famiglia Ospitata coabitante con altra nella stessa abitazione

## Funzioni

Dopo aver selezionato il cittadino è possibile selezionare alcune funzioni presenti nell'elenco sulla destra della videata:

### Funzioni locali

- **Soggetto** → Permette di consultare il Dettaglio scheda soggetto.
- **Recapiti** → Permette l'aggiunta di un recapito telefonico o di un indirizzo email.
- **Note** → Permette l'inserimento di una o più note su un soggetto.
- **Comunicazioni** → Permette la stampa di comunicazioni anagrafiche per il soggetto scelto.
- **Pratiche** → Permette di consultare lo storico delle pratiche legate al soggetto.
- **Storico Variazioni** → Permette di consultare lo storico variazioni.
- **Allegati** → in evoluzione
- **Scheda Famiglia** → Permette la consultazione dello storico delle scheda di famiglia.

### Funzioni ANPR

- **Allinea posiz. Cittad.** → Permette di allineare alcuni dati tra banca dati locale e ANPR.160 visualizzazioni.