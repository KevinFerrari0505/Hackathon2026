# Gestione Conservazione

## Premessa

Tale funzione è da intendersi come il cruscotto centrale del sistema di versamento dei documenti presso l'ente conservatore. Da qui è possibile avere le informazioni relative al numero di documenti versati, al loro stato di conservazione, ad eventuali anomalie in relazione alla conservazione ecc. È inoltre possibile eseguire alcune operazioni manuali sui documenti versati.

La predisposizione dei pacchetti di versamento, il versamento degli stessi presso l'ente conservatore e il controllo degli esiti di conservazione, è configurabile tramite processo automatico direttamente all'interno dell'applicativo CWOL.

## Accesso al menu

Per accedere al menu di gestione della conservazione documentale, dal menu principale occorre seguire il percorso:

**20.Protocollo → 10.Protocollo → 50.Conservazione → 20.Gestione Conservazione**

[Immagine: Screenshot del percorso di menu nell'applicativo Academy Suite CWOL, con i sottomenu espansi che mostrano il percorso 20.Protocollo → 10.Protocollo → 50.Conservazione → 20.Gestione Conservazione]

## Maschera di ricerca e filtri

Si apre una maschera dalla quale è possibile inserire alcuni filtri così da restringere il campo di ricerca. Essendo una maschera dinamica, selezionando un valore all'interno del campo **"Tipo documento"**, verranno messi a disposizione dei campi di ricerca differenziati in base al tipo di documento di interesse. È possibile altrimenti eseguire una ricerca che coinvolga tutti i documenti predisposti per la conservazione.

I campi disponibili sono:

- **Tipo Documento** – seleziona il tipo di documento (es. "Tutti", "Atti Amministrativi", ecc.)
- **Anno** – già compilato con l'anno corrente
- **Da Numero Atto / A Numero Atto** – intervallo di numeri di protocollo
- **Da N. Generale / A N. Generale** – intervallo di numeri generali
- **Tipo Atto** – tipo specifico dell'atto
- **Dalla Data Atto / Alla Data Atto** – intervallo di date
- **Titolario** – con versione (es. "2 - 2013/12/19")
- **Descrizione Titolario**
- **Stato Versamenti** – filtro per stato di versamento (default: "Tutti")
- **Stato Conservazione** – filtro per stato di conservazione (default: "Tutti")

[Immagine: Screenshot della maschera di ricerca con filtri – vista "Tutti tipi documento" e vista "Atti amministrativi" con campi aggiuntivi]

> **Nota:** Si consiglia di non impostare intervalli di tempo molto estesi, così da evitare che la richiesta di una mole di dati troppo elevata possa richiedere un tempo conseguentemente più lungo.

Dopo aver impostato i filtri necessari, cliccare il bottone **"Elenca"**.

## Risultati della ricerca

Verranno estratti i dati sulla base dei filtri precedentemente impostati. In corrispondenza di ogni documento, viene indicato il dettaglio in merito allo **stato di versamento** e allo **stato di conservazione**:

- **Stato Versamento**: esprime l'esito dell'invio all'ente conservatore e relativa accettazione del pacchetto di versamento.
- **Stato Conservazione**: esprime l'esito finale di conservazione da parte dell'ente conservatore.

Nella parte destra della schermata è possibile consultare la **legenda dei vari stati di versamento e conservazione**, così da avere sempre una visione chiara in merito alla conservazione di ogni singolo documento.

[Immagine: Screenshot della tabella "Elenco Conservazioni" con colonne: Tipo Documento, Tipo, Anno, Numero, Oggetto, Fascicolo, Data Registrazione, Data Ultima Trasmissione, Ora Ultima Trasmissione, Tentativi, Stato Versamento, Stato Conservazione. A destra è visibile la "Legenda Stato Esiti".]

## Il processo di conservazione in due passaggi

La conservazione dei documenti avviene in due passaggi:

### 1. Versamento al Polo di conservazione

È un processo automatizzabile che permette l'invio dei documenti dall'applicativo CWOL all'ente conservatore. In questa fase si riceve l'accettazione dei pacchetti da parte dell'ente conservatore, che ne verifica il rispetto dei requisiti minimi di composizione.

### 2. Conservazione dei documenti versati

L'ente conservatore tratta i pacchetti inviati e li predispone per la conservazione presso il proprio sistema certificato e restituisce l'esito dell'operazione all'applicativo CWOL, che lo associa in automatico allo specifico documento. In questa fase si riceve quindi l'esito definitivo della conservazione vera e propria del documento.

## Versamento manuale di un documento

Se si ha la necessità di procedere manualmente al versamento di un documento non ancora versato in conservazione (entrambi i bollini blu), operare come segue:

1. Selezionare un documento dalla lista con un clic;
2. Cliccare il bottone **Menu Funzioni**;
3. Cliccare **Riversa in Conservazione**.

[Immagine: Screenshot del pannello "Menu Funzioni" con le opzioni: "Riversa in Conservazione", "Controllo Allegati", "Blocca Conservazione Protocollo"]

Nella colonna **"Stato Versamento"** verrà aggiornato il colore del bollino in base all'esito del versamento.

### Legenda colori – Stato Versamento

| Colore bollino | Significato |
|---|---|
| 🟢 Verde | Versato correttamente (nessuna anomalia) |
| 🔵 Blu | Non versato |
| 🔴 Rosso | Errore in versamento |
| 🟡 Giallo | Versato con anomalie |
| 🟠 Arancione | Protocollo variato |
| 🔵 Blu chiaro | Protocollo non conservabile |
| 🟣 Viola | Protocollo bloccato |

## Aggiornamento dello Stato Conservazione

Dopo aver versato il protocollo manualmente, per aggiornare lo **"Stato Conservazione"**:

1. Cliccare sul simbolo della **lente** in corrispondenza del documento appena versato.
2. Si aprirà una nuova finestra ("Dettaglio Elemento Conservato").
3. Cliccare il tasto in corrispondenza della voce **RDV** per ricevere l'esito della conservazione.

[Immagine: Screenshot della finestra "Dettaglio Elemento Conservato" per il Protocollo P - 2024/063326, con tabella Conservazioni (Data, Ora, Esito Versamento, Esito Conservazione, UUID, File Esito, File Richiesta, RDV). Il pulsante RDV è evidenziato con un riquadro rosso.]

Nella schermata compaiono data, ora e esito di tutti i tentativi di invio fatti.

Chiudendo la finestra e tornando alla schermata precedente, avendo avuto esito positivo in relazione alla conservazione, il bollino nella colonna **"Stato Conservazione"** in corrispondenza del documento per il quale si è richiesto lo stato di conservazione, assumerà il colore **verde**.

### Legenda colori – Stato Conservazione

| Colore bollino | Significato |
|---|---|
| 🟢 Verde | Conservato correttamente |
| 🔴 Rosso | Errore in fase di conservazione |
| 🔵 Blu | Il protocollo non è stato ancora verificato |