# Documenti di identità e scadenze

Questa sezione descrive la gestione dei documenti di identità dei cittadini: carta d'identità, passaporto, permesso di soggiorno e altri documenti rilasciati o registrati dall'ufficio anagrafe.

Il modulo è accessibile dal menu **Anagrafe → Gestione Documenti**.

## Struttura dati

I dati sono distribuiti su due tabelle collegate:

| Tabella | Descrizione |
|---------|-------------|
| **DAN_DOCUM** | Testata del documento: tipo, numero, data rilascio, stato, ente rilasciante |
| **DAN_DOCUMR** | Rinnovi e scadenze: data inizio, data scadenza, protocollazione, tipo comunicazione |

Ogni documento è identificato dalla coppia **(PROGDOC, PROGSOGG)**, dove PROGSOGG è il progressivo del soggetto in anagrafe.

## Tipi di documento

I tipi documento sono configurati nella tabella **DTA_TIPDOC** (menu Tabelle → Tipi Documento). Ogni tipo documento ha un codice numerico (campo TIPDOC) e una descrizione (DESDOCUM).

Il tipo documento **2** (Permesso di Soggiorno) ha un comportamento speciale:

- il campo **Categoria** viene presentato come menù a tendina anziché come campo libero
- è disponibile una sottogriglia per i **familiari** conviventi inclusi nel permesso
- è presente il pulsante **Allinea ANPR** per la sincronizzazione con il registro ANPR

## Campi principali

### Testata documento (DAN_DOCUM)

| Campo | Descrizione |
|-------|-------------|
| **Tipo Documento** | Selezionabile da tabella DTA_TIPDOC |
| **Numero Documento** | Numero identificativo del documento |
| **Data Rilascio** | Data di emissione del documento |
| **Stato** | Vedi tabella stati sotto |
| **Provincia Rilascio** | Provincia dell'ente che ha rilasciato il documento |
| **Comune Rilascio** | Comune dell'ente che ha rilasciato il documento |
| **Categoria** | Campo aggiuntivo (per permessi di soggiorno: selezionabile da combo) |
| **Motivo Perdita** | Compilare in caso di stato "Cancellata" |
| **Note 1-4** | Campi note libere |

### Rinnovo / Scadenza (DAN_DOCUMR)

| Campo | Descrizione |
|-------|-------------|
| **Data Inizio Validità** | Data inizio del periodo di validità corrente |
| **Data Scadenza** | Data di scadenza del documento |
| **Rinnovo** | Flag che indica se il documento è stato rinnovato |
| **Data Protocollazione** | Data in cui il documento è stato protocollato |
| **Numero Protocollo** | Numero protocollo della comunicazione |
| **Tipo Comunicazione** | 0 = Nessuna, 1 = Avviso, 2 = Diffida |

## Stati del documento

| Codice | Descrizione | Utilizzo |
|--------|-------------|----------|
| **1** | Attiva | Documento corrente e valido — assegnato automaticamente alla creazione |
| **2** | Non Consegnata | Documento emesso ma non ancora consegnato al cittadino |
| **3** | Cancellata | Documento annullato o ritirato; richiede la compilazione del motivo perdita |
| **4** | Sospesa | Documento temporaneamente sospeso |

## Operazioni principali

### Inserimento nuovo documento

1. Aprire il soggetto dalla scheda anagrafica oppure accedere al modulo dal menu
2. Fare clic su **Aggiungi**
3. Selezionare il **Tipo Documento** dalla combo
4. Compilare numero, data rilascio e comune/provincia di rilascio
5. Lo stato viene preimpostato a **1 - Attiva**
6. Completare la sezione **Rinnovi/Scadenze** con data inizio e data scadenza
7. Salvare con **Conferma**

### Modifica documento esistente

1. Selezionare il documento dalla griglia e fare clic su **Dettaglio**
2. I campi divengono modificabili
3. La **data scadenza** è editabile solo se già valorizzata; i nuovi documenti devono passare per la sezione rinnovi
4. Salvare con **Aggiorna**

### Cancellazione documento

La cancellazione logica avviene cambiando lo stato del documento in **3 - Cancellata** e compilando il campo **Motivo Perdita**. La cancellazione fisica dalla griglia è disponibile solo agli utenti abilitati.

## Aggiornamento massivo date di scadenza

Per aggiornare in blocco le date di scadenza di un tipo documento (es. rinnovo di massa delle carte d'identità) è disponibile il modulo accessibile da **Anagrafe → Aggiornamento Date Documenti**.

Funzionamento:

1. Selezionare il **Tipo Documento** da aggiornare
2. Indicare la **Data Scadenza** corrente da cercare (filtro)
3. Specificare il **periodo di aggiornamento**: anni, mesi, giorni da aggiungere o sottrarre
4. Confermare: l'operazione aggiorna la tabella **DAN_DOCUMR** in modo transazionale

## Emissione altri documenti

Il modulo **cwdDanAltridoc** gestisce l'emissione di documenti generici tramite numeratore automatico.

Prerequisiti:

- Il tipo documento deve avere **F_RILDOC = 1** (abilitato al rilascio)
- Deve essere definito il **numeratore dell'anno corrente** in DTA_PROGDO; se assente, il sistema propone di inserirlo automaticamente

Flusso operativo:

1. Selezionare il tipo documento tramite il pulsante di ricerca
2. Il sistema verifica la disponibilità del numeratore
3. Se il numeratore non esiste, viene proposto di crearlo
4. Confermare il rilascio

## Permessi di soggiorno

Il permesso di soggiorno (TIPDOC = 2) ha caratteristiche specifiche:

**Familiari inclusi nel permesso:** Nella scheda del permesso è presente una sottogriglia che elenca i familiari conviventi inclusi. È possibile aggiungere, modificare o rimuovere i componenti del nucleo familiare dal permesso senza modificare la scheda anagrafica.

**Allineamento ANPR:** Il pulsante **Allinea ANPR** (visibile nella vista risultati) consente di sincronizzare i dati del permesso di soggiorno con il registro ANPR, garantendo la coerenza tra le banche dati.

## Integrazione con la scheda soggetto

Il modulo documenti è accessibile in due modalità:

1. **Da menu** (autonomo): ricerca del soggetto tramite il campo nominativo con pulsante di lookup, poi gestione dei suoi documenti
2. **Da scheda soggetto** (wizard): aperto in modale dalla scheda anagrafica, mostra solo i documenti del soggetto corrente senza i controlli di ricerca; i dati vengono scritti al salvataggio del wizard padre

## Note operative

- Il campo **Nazionalità** (CODNAZI) è in sola lettura: viene ereditato dalla scheda anagrafica del soggetto
- Il campo **Comune Rilascio** è una lookup sulla tabella BTA_LOCAL (codice provincia + codice comune)
- Per i permessi di soggiorno, la modifica della data di scadenza può aggiornare automaticamente la data fine dell'annotazione associata (tabella DAN_NOTE), se presente
- L'operatore che effettua modifiche viene tracciato automaticamente nei campi CODUTE, DATAOPER, TIMEOPER