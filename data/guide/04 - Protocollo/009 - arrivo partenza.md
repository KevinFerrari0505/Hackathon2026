# Gestione Protocollo

Dal menu principale, accedere alla funzione **Protocollo → Protocollo → Gestione → Gestione Protocollo**.

Da questa finestra è possibile ricercare un protocollo attraverso una serie molto ampia di dati: tipo, data, numero, mittente, destinatario, oggetto, trasmissione, titolario, segnatura, allegati, ecc.

La schermata può essere suddivisa in due parti:

- *Vai al Protocollo*
- *Ricerca Avanzata*

## Vai al Protocollo

**Vai al Protocollo** permette di accedere direttamente al protocollo digitandone il numero. Il campo *Anno* è già impostato all'anno corrente e la ricerca viene effettuata tra i protocolli in arrivo e in partenza, se il campo *Tipo* non viene modificato.

Cliccando **Elenca**, il programma verifica l'esistenza e la visibilità del protocollo e apre direttamente il numero richiesto. In caso contrario, un messaggio avvisa che il protocollo non è accessibile o inesistente.

## Ricerca Avanzata

**Ricerca Avanzata** permette di impostare un'ampia serie di filtri utilizzando anche le lentine per selezionare le voci dagli archivi. Cliccando **Elenca**, il programma mostra tutti i protocolli che rispettano i parametri impostati.

Utilizzando il bottone **Svuota Ricerca**, si ripuliscono tutti i campi, così da poter avviare una nuova ricerca con nuovi parametri.

[Schermata di Ricerca Avanzata con campi: Tipo, Protocollo Da/A, Data Protocollo, Arrivato in Partenza Da, Tipo Documento, Oggetto, Segnatura, Mitt./Dest./Fornitore, Trasmesso a, Trasmissione via PEC, Criteri ricerca, Titolo, Descrizione Titolo, Titolario Fascicolo, Descrizione Fascicolo, Fascicolo, Solo non protocollati, Ricerca per uffici, Tipo Speditore, Visualizza Protocollo, Allegati, Visualizza doc. da firmare, Utente, Ruolo. A destra i pulsanti: Vai al Protocollo, Ricerca Avanzata, Svuota Ricerca, e i pulsanti colorati Arrivo, Partenza, Interno, Doc. Alla Firma.]

Aprendo il protocollo cercato, viene mostrata la schermata di protocollazione.

## Vis. Trasmissioni

Con il tasto **Vis. Trasmissioni** sulla destra della schermata, è possibile controllare:

- se il protocollo è stato lavorato
- da chi è stato trasmesso ✅ e a chi
- se è stato letto o chiuso e in che data
- se è stato rifiutato 🚫 in che data e per quale motivo
- se è stato ritrasmesso
- se era in gestione o in visione
- se presso un utente è ancora aperto ✅ o è stato chiuso ✅

[Screenshot della finestra "Trasmissione del Documento" con tab: Dati Principali, Trasmissioni del Documento, Allegati (2), Dati Aggiuntivi, Note (0), Fascicoli (0). La tabella mostra colonne: Data, Cg, Cod., Destinatario, Annotazioni, Letto il, Chiuso, Scadenza, Gest., Stato, Acc/Rif., Motivo. Le righe mostrano trasmissioni con stati diversi: ANNULLATO PER VARIAZIONE PROTOCOLLO, ANNULLATO PER INSERIMENTO NUOVO PROTOCOLLO, ANNULLATO PER VARIAZIONE DEL PROTOCOLLO, non di competenza, ecc.]

## Prot. Collegati

Dal bottone **Prot. Collegati**, in alto a destra, è possibile vedere i protocolli collegati a quello cercato (indicato in rosso).

[Screenshot della finestra "Risultato Ricerca" con "Elenco Protocolli" contenente: A - 000249/2018 - FATTURA N° - MUCCI ALESSANDRO; A - 000248/2018 - PARTENZA DI PROVA - ITALSOFT; P - 000245/2018 (in rosso) - PARTENZA DI PROVA - ITALSOFT. A destra il pulsante "Prot. Collegati".]

## Registro di Protocollo

Se non è valorizzato nessun parametro di ricerca e si clicca **Elenca**, il programma mostra il registro di protocollo completo dell'anno corrente.

### Codifica colori dei protocolli

| Colore / Aspetto | Significato |
|---|---|
| Scritta **RISERVATO** su sfondo grigio | Visibili solamente agli utenti abilitati (chi lo ha registrato e a chi è stato assegnato) |
| Evidenziato in **giallo** | Protocolli senza allegati o senza classificazione |
| Testo in **nero** | Protocollo annullato |

### Colonne del registro

La prima colonna indica se il documento è:

- **A** → Arrivo
- **P** → Partenza
- **C** → Documento interno formale

Le altre colonne mostrano:

- L'anno del protocollo
- Il numero assegnato
- La data e l'ora di registrazione
- Il numero del precedente protocollo collegato se presente (*N. Antecedente*)
- La data di protocollo del documento inviato dal mittente (*Data Carte*)
- Il numero di protocollo del documento inviato dal mittente (*Riferimento*)
- Il mittente o destinatario
- La presenza o meno di allegati (*All.*)

[Screenshot dell'"Elenco Protocolli" con colonne: A/P, Anno, Numero, Data Reg., Ora, N. Antec., Data Carte, Riferimento, Provenienza/Destinatario, All., Oggetto. Esempi di righe con protocolli in arrivo (A) e partenza (P), alcuni evidenziati in giallo, alcuni con scritta RISERVATO su sfondo grigio. A destra i pulsanti: F3 - Altra Ricerca, Stampa, Arrivo, Partenza, Doc. Formale, Doc. Alla Firma.]

### Icona fascicolo (documenti collegati)

Il simbolo del fascicolo sulla seconda colonna 📁 indica che il protocollo è legato ad un altro; cliccando sull'icona, si può visualizzare la catena dei documenti collegati. Quello in rosso è il protocollo selezionato.

[Screenshot della finestra "Risultato Ricerca" con "Elenco Protocolli" che mostra la catena di documenti collegati: A - 000125/2017 - PROTOCOLLO PER ASSOCIAZIONE MAIL - TEST; A - 000128/2017 (in rosso) - PROTOCOLLO PER ASSOCIAZIONE MAIL - TEST. A destra i pulsanti: Arrivo, Partenza, Doc. Formale, Doc. Alla Firma.]

## Accesso alla protocollazione dalla finestra principale

Dalla finestra principale di *Gestione Arrivi/Partenze* è possibile anche accedere alla protocollazione. Attraverso i tasti presenti sulla destra, il programma reindirizza alle relative schermate dedicate alla protocollazione di:

- **Documenti in arrivo**
- **Documenti in partenza**
- **Documenti interni formali**
- **Predisposizione di un documento per la firma**