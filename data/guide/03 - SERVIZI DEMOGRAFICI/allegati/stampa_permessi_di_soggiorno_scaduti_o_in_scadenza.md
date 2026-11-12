# Stampa permessi di soggiorno scaduti o in scadenza

## Introduzione

L'iscrizione anagrafica dello straniero extracomunitario dipende dal possesso di un documento di soggiorno valido, ma in base alle vigenti normative, la domanda di cambio residenza va accolta anche con permesso scaduto qualora l'interessato esibisca la ricevuta della domanda di rinnovo rilasciata dalla questura, o la ricevuta delle poste con la quale ha fatto richiesta di rinnovo.

Gli stranieri regolarmente iscritti in anagrafe avranno un permesso di soggiorno prossimo alla scadenza, o già scaduto o addirittura mai consegnato.

In questi casi, per i documenti che hanno una scadenza, gli interessati devono provvedere al loro rinnovo e, ottenutolo, dichiararlo all'anagrafe del comune dove risiedono; in caso contrario, decorso un anno dalla scadenza, l'anagrafe procede alla cancellazione per mancato rinnovo del documento di soggiorno.

Solitamente le sequenze operative sono le seguenti:

- l'anagrafe verifica periodicamente quali residenti extracomunitari hanno il documento in scadenza e invia loro un **avviso** che li avverte della necessità di rinnovarlo e di comunicarlo poi all'anagrafe;
- gli interessati rinnovano il documento e lo presentano all'anagrafe rinnovando la dichiarazione di dimora, l'anagrafe caricherà la nuova scadenza o il nuovo documento;
- l'anagrafe verifica periodicamente quali residenti extracomunitari hanno il documento scaduto da un anno e invia loro una **diffida** che gli intima di rinnovarlo e riferirne all'anagrafe pena la cancellazione anagrafica decorsi 30 giorni.

Con questa funzione, è possibile generare l'**Avviso di Scadenza del Documento di Soggiorno**, per tutti i cittadini di cittadinanza extracomunitaria iscritti nella propria anagrafe, che sono in possesso di un documento di soggiorno prossimo alla scadenza in un determinato periodo (scelto dell'operatore).

## Generazione Elenchi o Avvisi di Scadenza

Con questa funzione, è possibile generare l'avviso, per tutti i cittadini che hanno un documento in base a ciò che è stato selezionato nella combo.

Prima di *generare gli avvisi*, soprattutto nel caso in cui sia la prima volta che la si effettua, sarebbe opportuno eseguire l'estrazione in excel per verificare eventuali anomalie e valutare la mole delle comunicazioni.

### Percorso di accesso alla funzione

**Servizi Demografici => Anagrafe => Stampe => Generazione Elenchi e avvisi di Scadenza**

[Schermata del menu di navigazione: Servizi Demografici > Anagrafe > Stampe > Generazione Elenchi e avvisi di Scadenza]

### Campi del modulo "Generazione Elenchi e Avvisi di Scadenza"

[Schermata del modulo di generazione elenchi e avvisi di scadenza con tutti i campi]

È possibile compilare i campi:

- **Tipo documento\*** (obbligatorio): selezionare dal menu a tendina "Permesso di Soggiorno".
- **Data avviso**: data già impostata di default dal programma.
- **Ricerca su**: selezionare dal menu a tendina "APR" o "AIRE".
- **Includi**: è possibile selezionare le voci "Italiani" e/o "Extracomunitari" e/o "Comunitari".
- **Scadenza**: "dal \_\_\_\_" "al \_\_\_\_".
- **Includi soggetti senza documento**: voce da selezionare o meno.
- **Testo per stampa lettera avviso**: selezionare, cliccando sulla "lentina", il testo dell'avviso da inviare.
- **Tipo comunicazione**: selezionare da menu a tendina l'opzione "Avviso 60gg per rispondere" oppure "Diffida 30gg per rispondere e poi si avvia la cancellazione per mancata presentazione".
- **Elenco cittadini (Excel)**: selezionando la seguente voce viene eseguita l'estrazione in excel per verificare eventuali anomalie.
- **Invio avviso tramite App IO**: selezionando la seguente voce è possibile inviare la comunicazione di avviso o di diffida tramite appIO.
- **Reinoltro avviso tramite app.IO**: selezionando la seguente voce è possibile re-inviare la comunicazione di avviso o di diffida tramite appIO.
- **Oggetto App IO**: campo in cui è possibile inserire l'oggetto della comunicazione.
- **Messaggio App IO**: campo in cui è possibile inserire il corpo della comunicazione.

---

## Procedura per l'estrazione in Excel dei permessi in scadenza

Compilare i campi:

1. **Tipo documento\***.
2. **Data avviso**, **Ricerca su**.
3. **Includi**.
4. **Scadenza "dal" "al"**.
5. **Includi soggetti senza documento**.
6. **Elenco cittadini (Excel)**.

[Schermata del modulo compilato con i campi evidenziati in rosso per l'estrazione Excel]

Cliccare sul tab **[Elabora]**.

[Schermata del risultato: file Excel "ElencoPermessiScaduti" con colonne: Cognome, Nome, Data di nascita, Luogo di nascita, Tipo documento, Num. documento, Scad. documento]

---

## Procedura per la stampa dell'avviso di scadenza del permesso di soggiorno

Compilare i campi:

1. **Tipo documento\***.
2. **Data avviso**.
3. **Ricerca su**, **Includi**.
4. **Scadenza "dal" "al"**.
5. **Includi soggetti senza documento**.
6. **Testo per stampa lettera avviso**.

Cliccare sulla "lentina". Inserire nel campo "Descrizione" il testo *"Lettera Scadenza Permesso di Soggiorno"* e premere sul testo **[Invio]** della tastiera del PC.

[Schermata del modulo compilato con il campo "Testo per stampa lettera avviso" evidenziato]

[Schermata della finestra "Risultato Ricerca" con Elenco Documenti: Codice 9469, Descrizione "Lettera Scadenza Permesso di Soggiorno", Tipo DOCX]

Doppio click con il tasto destro del mouse per selezionare il testo corrispondente.

[Schermata del modulo con il testo selezionato nel campo "Testo per stampa lettera avviso"]

Cliccare sul tab **[Elabora]**.

A questo punto è possibile estrarre tutte le comunicazioni dei soggetti con Permesso di Soggiorno in scadenza.

[Schermata della "Visualizzazione Documenti" con elenco file "Lettera_Scadenza_Permesso_di_Soggiorno" e anteprima del documento con intestazione del Comune, protocollo informatico e oggetto "Comunicazione scadenza/rinnovo Permesso di Soggiorno"]

---

## Procedura per l'invio dell'avviso di scadenza del permesso di soggiorno tramite App IO

Compilare i campi:

1. **Tipo documento\***.
2. **Data avviso**.
3. **Ricerca su**, **Includi**.
4. **Scadenza "dal" "al"**.
5. **Includi soggetti senza documento**.
6. **Tipo comunicazione**.
7. **Oggetto App IO**.
8. **Messaggio App IO**.

[Schermata del modulo compilato con i campi App IO evidenziati: Tipo comunicazione, Invio avviso tramite App IO, Oggetto App IO, Messaggio App IO]

Cliccare sul tab **[Elabora]**.

[Schermata del messaggio di conferma: "Attenzione – Flusso generato e inviato correttamente"]