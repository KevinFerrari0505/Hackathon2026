# Codice fiscale in ANPR

**Premessa:** la documentazione fornita da ANPR è limitata. Quanto scriviamo qui come *indicazioni generali* è il frutto di esperienza, e di alcuni chiarimenti forniti da Sogei nel tempo. Resta inteso che le scelte su come comportarsi sulla gestione del codice fiscale, vengono fatte dagli enti centrali, e *potrebbero cambiare senza preavviso in qualsiasi momento*.

## Tre banche dati

1) Quello che siete abituati a consultare con **Punto Fisco**, e che chiamiamo **Anagrafe Tributaria** (abbreviato AT), oppure **Agenzia delle Entrate** (abbreviato AE), è la vera anagrafe dei codici fiscali, nata negli anni '70.

2) Il codice fiscale è anche presente in **ANPR**, e dovrebbe (ma non è sempre vero) corrispondere con quello presente in anagrafe tributaria.

3) Il codice fiscale è memorizzato ovviamente anche in **Cityware.online**, e deve corrispondere con quello memorizzato in ANPR, altrimenti è stata sbagliata una qualche operazione.

## Corrispondenza delle operazioni sul c.f. tra Cityware.online e ANPR

In qualsiasi operazione sulla web application ANPR vi viene richiesto di indicare il campo "gestione cf" che ha questo significato.

| CWOL | ANPR | significa |
|------|------|-----------|
| *validare il c.f.* | | fare una operazione che va a buon fine solo se il CF è validato in ANPR. In caso di rettifica generalità, potrebbe portare alla generazione di un nuovo codice fiscale |
| *richiesta attribuzione* | | solo per soggetti NON presenti in AE. Se il cf che si deve generare esiste già in AE, l'operazione fallirà. |
| *richiesta omocodice* | | solo per soggetti il cui cf generato automaticamente, esiste già in AE per un altro cittadino |
| *iscrizione/variazione senza validazione CF* | | operazione ammessa da ANPR solo in alcuni casi molto particolari |

In cityware.online viene richiesto esplicitamente solo durante la rettifica di generalità. Negli altri casi CWOL usa un automatismo prefissato.

## Chi crea il codice fiscale per un nuovo soggetto?

Per quanto ci risulta, anche consultando il sito dell'Agenzia Entrate, da vari enti.

- i Comuni con le iscrizioni e le variazioni registrate in ANPR
- gli sportelli dell'Agenzia delle Entrate
- le Questure nel rilascio del permesso di soggiorno

E' sottointeso che possono creare un c.f. solo se questo non esiste già.

Se due persone diverse, vengono ad avere la stessa codifica del codice fiscale, la seconda attribuzione si dice *omocodice*, e vede un ricalcolo manuale da parte dell'AE del codice.

## Chi può modificare il codice fiscale o le sue generalità?

Quando nelle due banche dati:

- in ANPR il c.f. è **validato**
- in AE il c.f. è **marcato ANPR**

In questa condizione, solo le anagrafi possono modificare i dati. Inoltre in questa condizione, l'indirizzo di residenza di ANPR viene automaticamente registrato in AE.

Se non sussistono queste condizioni, anche gli sportelli delle Agenzie Entrate possono intervenire.

## Vecchio codice fiscale o "collegato"

Quando per qualsiasi motivo un c.f. esistente in AE, viene cessato perchè con una operazione di rettifica generalità, è stato assegnato un nuovo c.f. , il "vecchio" è collegato al nuovo.

Il "vecchio" c.f. rimane presente in AE, e non può essere assegnato a un altro cittadino.

Cercando in AE per uno qualsiasi dei c.f. che nel tempo ha avuto il soggetto, si viene ricondotti al c.f. attuale.

## Per quali motivi il codice fiscale in ANPR non è validato?

tra i principali motivi:

- il codice fiscale è nato nel 1970, quindi soggetti emigrati all'estero prima di quella data
- cittadini aire a cui non è mai stato assegnato (magari non hanno mai abitato in Italia)
- cittadini residenti con generalità differenti da quelle registrate in AE
- il c.f. che verrebbe generato automaticamente, corrisponde a un altro soggetto già presente in AE

## Limiti nella gestione del codice fiscale

Sono diversi, i principali sono:

- nel variare le generalità di una persona già iscritta in AE, non si possono modificare più di 3 elementi in una unica operazione¹
- quando si fa una operazione sul codice fiscale da ANPR che determina una operazione su AE, non si può intervenire una seconda volta nello stesso giorno

## Richiesta codice fiscale omocodice

Se c'è un altro soggetto già presente in AE, con lo stesso c.f. del mio cittadino, occorre indagare per cercare di verificare se si tratta della stessa persona.

Supponiamo di determinare che sono due persone diverse. In ANPR posso effettuare una operazione:

- occorre fare una variazione, indicando "richiesta omocodice"
- se la variazione va a buon fine, viene attibuito un cf numerico provvisorio (come ai richiedenti asilo)
- la pratica va in gestione alla Direzione Centrale dell'Agenzia delle Entrate, che verifica se sono veramente due persone diverse
- in seguito l'ufficio centrale assegna il cf omocodice, che ha la caratteristica di avere una lettera al posto delle ultime 3 cifre

Da indicazioni di Sogei, la Direzione Centrale dell'Agenzia delle Entrate è contattabile alla email entrate.archivioanagrafico@agenziaentrate.it

**PS:** nel caso si renda successivamente necessario modificare i dati di un cf omocodice, occorre sempre contattare lo stesso ufficio, inviando la documentazione necessaria²

## Consultazioni codici fiscali in Anagrafe Tributaria

Se non avete sul vostro pc Punto Fisco, potete comunque usare la web application per consultare l'Anagrafe Tributaria.

Aprite la web application, e selezionate il menù:

> Consultazione e estrazione > Consultazione AE

Al contrario di Punto Fisco, tramite la WA potete ricercare esclusivamente per codice fiscale.

Se il codice fiscale ricercato esiste, appare una videata suddivisa in tre sezioni:

1. Generalità
2. Data Residenza
3. Indirizzo, a seconda dei casi
   1. Indirizzo in Italia
   2. Indirizzo estero

Qualora il codice fiscale NON sia marcato ANPR, l'indirizzo è quello che risulta alla Agenzia delle Entrate, e non centra niente con l'indirizzo di residenza anagrafico.

## Elenco Normativa e documentazione utile

**DECRETO DEL PRESIDENTE DELLA REPUBBLICA 29 settembre 1973, n. 605**

Disposizioni relative all'anagrafe tributaria e al codice fiscale dei contribuenti.

**DECRETO MINISTRO FINANZE 23 dicembre 1976**

Sistemi di codificazione dei soggetti da iscrivere all'anagrafe tributaria in *Gazzetta Ufficiale n.345 del 29-12-1976 S.O.*

**AGENZIA ENTRATE: COME SI CHIEDE IL CODICE FISCALE**

vedi https://www.agenziaentrate.gov.it/portale/web/guest/schede/istanze/richiesta-ts_cf/come-si-chiede-il-codice-fiscale

---

¹ forum sogei rif #142 o #2288

² forum sogei rif #3371