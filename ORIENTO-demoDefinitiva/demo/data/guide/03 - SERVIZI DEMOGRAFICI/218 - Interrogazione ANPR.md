# Interrogazione ANPR

L'interrogazione ANPR permette di consultare l'Anagrafe Nazionale della Popolazione Residente. La consultazione è permessa ai soli Ufficiali d'Anagrafe che sono stati censiti nella WebApp ANPR.

## Criteri di ricerca

La ricerca del soggetto può essere effettuata tramite uno o più dei seguenti criteri:

- **Codice Fiscale**
- **Id Soggetto ANPR**
- **Id ANPR Univoco**
- **Id ANSC**
- **Cognome**
- **Nome**
- **Sesso**
- **Data di nascita**
- **Comune di nascita**
- **Tipo Famiglia**
- **Numero Famiglia**

Per ottenere risultati più precisi è consigliabile compilare il maggior numero possibile di informazioni disponibili.

## Dettagli sui campi di ricerca

- Le caselle con dicitura **senza** a fianco dei campi **Cognome** e **Nome** consentono la ricerca di soggetti privi del relativo dato anagrafico.

- Il campo **Comune di nascita** consente la ricerca sia di cittadini italiani sia di cittadini stranieri.

- Qualora venga valorizzato uno degli identificativi univoci (**Id Soggetto ANPR**, **Id ANPR Univoco** o **Id ANSC**), la ricerca viene eseguita utilizzando prioritariamente il dato inserito. Eventuali ulteriori criteri di ricerca valorizzati potrebbero non essere considerati.

- L'opzione **Ricerca Nazionale** consente di estendere la consultazione all'intera banca dati ANPR.

- L'opzione **Mostra solo gli AIRE** limita la ricerca ai soli cittadini iscritti all'Anagrafe degli Italiani Residenti all'Estero.

- I campi **Tipo Famiglia** e **Numero Famiglia** consentono di limitare la ricerca ai soggetti appartenenti ad una specifica famiglia anagrafica.

- Il campo **Dt Rif. scheda** può essere utilizzato per effettuare una consultazione riferita ad una specifica data di aggiornamento del cartellino individuale. Se non valorizzato, la ricerca viene eseguita con riferimento alla situazione corrente.

> **Nota:** Il campo Dt Rif. scheda non si riferisce alla certificazione storica, ma alla data aggiornamento cartellino individuale (data decorrenza anpr).

## Pulsanti della schermata di ricerca

| Pulsante | Funzione |
|----------|----------|
| **F4 - Elenca** | Avvia la consultazione una volta compilati i filtri |
| **Pulisci** | Elimina tutti i valori inseriti nei campi di ricerca |
| **F6 - Chiudi** | Consente di uscire dalla funzione |

[Schermata del form di ricerca ANPR con i campi: Codice Fiscale, Id Soggetto ANPR, Cognome (con checkbox "senza"), Nome (con checkbox "senza"), Sesso (M/F), Data nascita, Comune di Nascita, Ricerca Nazionale (checkbox), Mostra solo gli AIRE (checkbox), Tipo Famiglia, Numero Famiglia, Id ANPR Univoco, Id ANSC, Dt Rif. scheda. A destra i pulsanti F4-Elenca, Pulisci, F6-Chiudi.]

## Elenco cittadini da ANPR

Dopo aver premuto **F4-ELENCA** verrà presentato l'elenco dei cittadini risultante dalla ricerca in ANPR.

Se ad esempio la consultazione fosse fatta indicando solo **COGNOME** e **NOME** potrebbero esserci vari nominativi nell'elenco.

Nell'elenco vengono mostrate le generalità dei cittadini, la loro residenza e se risultano AIRE.

[Schermata dell'elenco risultati con colonne: Codice Fiscale, Nominativo, Sesso, Data nascita, Luogo nascita, Residenza, Aire. A destra i pulsanti: F2 - Altra Ricerca, Dettaglio ANPR, Rendi Soggetto, Verifica procedimento aperto, F6 - Chiudi.]

### Interazione con i risultati

- **Aprire il dettaglio del cittadino:** fare doppio click sul soggetto di interesse oppure selezionare il nominativo (un click sulla riga) e poi premere **DETTAGLIO ANPR** sulla destra.

- **Composizione familiare:** il simbolo **"+"** a fianco del nominativo permette di vedere la sua composizione famigliare.

- **Rendi Soggetto:** il pulsante **RENDI SOGGETTO** permette di salvare nell'archivio unico soggetti i dati di un non residente. Verranno salvate le generalità del soggetto e l'atto di nascita. Utile ad esempio per avere i dati di un non residente completi per la registrazione di un atto di Stato Civile per tale nominativo.

- **Verifica procedimento aperto:** il pulsante **VERIFICA PROCEDIMENTO APERTO** permette di verificare la presenza di un procedimento in corso su ANPR per il soggetto selezionato.