# Gestire una Fattura Elettronica

L'utente assegnatario delle fatture elettroniche troverà le fatture da lavorare tra i propri **Documenti in carico**.

Spostandosi nella scheda **Vedi Chiusi**, potrà visualizzare tutti i flussi protocollati e a lui assegnati, ma non da lavorare.

[Schermata: elenco dei protocolli in carico con tabella contenente colonne Num., Trasmesso il, Oggetto, Prov./Dest., Al Termine, Trasm., Letti. In basso sono presenti i filtri: In Carico, Vedi Chiusi, Scaduti, Rifiutati, Vedi Inviati, Da Firmare.]

Tornando tra quelli **In Carico**, invece, troverà le singole fatture spacchettate da gestire, con le relative date di scadenza.

[Schermata: elenco dei protocolli in carico con fatture singole, colonne Num., Trasmesso il, Oggetto (con nome fornitore e codice destinatario), Prov./Dest., Al Termine (evidenziato in rosso), Trasm., Letti. Filtro attivo: In Carico.]

Per lavorare una fattura, aprirla con un doppio click. Nella scheda **Allegati** è presente la fattura vera e propria, che può essere aperta e visualizzata. Infine cliccare **Presa in Carico**.

[Schermata: finestra "Gestione Trasmissioni" con intestazione protocollo, mittente (STUDIO SPA), destinatario (MUCCI ALESSANDRO), scheda "Allegati (3)" attiva. Bottoni a destra: Visualizza Protocollo, Rifiuta, Presa in Carico, Ricevuta. Indicatore "ITER APERTO Tot.Giorni 1".]

---

## Azioni dopo la presa in carico

Dopo aver preso la fattura in carico, i bottoni di destra cambieranno e saranno possibili nuove azioni:

- Con il tasto **Invia**, dopo aver indicato uno o più destinatari nella tabella in fondo, può essere **ri-assegnata** ad un altro utente;
- Con il tasto **Chiudi Iter** si conclude il lavoro sulla fattura e la si sposta in *Vedi Chiusi*;
- Il tasto **Riscontro** permette invece di **accettare o rifiutare una fattura** creando un protocollo in partenza.

[Schermata: stessa finestra "Gestione Trasmissioni" ma con bottoni aggiornati: Visualizza Protocollo, F5 - Invia, F7 - Chiudi Iter, Ricevuta, Metti Evidenza, Riscontro. Indicatore "ITER APERTO Tot.Giorni 1".]

---

## Rispondere a una fattura

Per rispondere a una fattura, dopo aver cliccato **Riscontro**, si sceglie se accettarla o rifiutarla.

[Schermata: finestra "Riscontro Fattura Elettronica" con anteprima della fattura (Fattura Numero: 9954, Tipo Fattura: TD01, Data Fattura: 18/02/2016, Fornitore: SOCIETA' SRL). Bottoni a destra: "Accetta l'intera Fattura" (verde), "Rifiuta l'intera Fattura" (rosso), "Vedi Fattura".]

### Rifiuto della fattura

In caso di rifiuto della fattura, verrà chiesto il **motivo** e sarà aperto subito dopo un nuovo protocollo in partenza.

I campi risulteranno tutti già compilati e negli allegati sarà presente un file temporaneo *Esito Committente* in formato xml, che include la motivazione del rifiuto.

Esempio di contenuto del file XML:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<types:NotificaEsitoCommittente
  xsi:schemaLocation="http://www.fatturapa.gov.it/sdi/messaggi/v1.0
  MessaggiTypes_v1.0.xsd" version="1.0"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:ds="http://www.w3.org/2000/09/xmldsig#"
  xmlns:types="http://www.fatturapa.gov.it/sdi/messaggi/v1.0">
  <IdentificativoSdI>354</IdentificativoSdI>
  <Esito>EC02</Esito>
  <Descrizione>importo errato</Descrizione>
  <MessageIdCommittente>20190107164245</MessageIdCommittente>
</types:NotificaEsitoCommittente>
```

Sarà quindi sufficiente registrare il protocollo (**Registra**) e inviarlo (**Notifica Destinatari**).

Dopo la registrazione, il file temporaneo *Esito Committente* sarà sostituito con quello definitivo.

[Schermata: anteprima del documento "Notifica Esito Committente" Versione 1.0 con campi: Identificativo SdI: 354, Esito: EC02 (Rifiuto), Descrizione: Importo errato, Message Id Committente: 20190107172437.]

### Accettazione della fattura

In caso di accettazione della fattura, il procedimento da seguire sarà identico, con la differenza che **non sarà richiesta nessuna motivazione**.

> **Nota:** Se non si invia alcuna risposta, la fattura risulterà accettata automaticamente allo scadere dei **15 giorni**.