# Profilazione Utenti

Le informazioni necessarie per profilare un utente sono: **Nome**, **Cognome**, **Codice Fiscale** e le **Autorizzazioni** ad esso legate.

## Creazione dell'utente

Dopo di che andare in:

**Amministrazione del Sistema** ➔ **Gestione Accessi** ➔ **Utenti** ➔ **Elenca** (per vedere l'elenco di tutti gli utenti presenti)

[Schermata: menu di navigazione con percorso Amministrazione del Sistema > Gestione Accessi > Utenti]

Scegliere il nominativo di un utente già presente (vi è la possibilità di ricercarlo direttamente) che abbia le stesse autorizzazioni del nuovo nominativo da caricare ➔ **Duplica**

[Schermata: elenco utenti con pulsante "Duplica" evidenziato a destra]

Nella schermata che si presenta, inserire il **Logname** (sempre **Maiuscolo**) e sotto i seguenti dati di **Cognome** e **Nome**, **Codice Fiscale** (con l'apposita matitina e Confermare) e indirizzo mail ➔ **Aggiungi** (in alto a destra possiamo constatare di essere in Modalità Duplicazione)

[Schermata: form di inserimento dati utente in Modalità Duplicazione con campi Logname, Cognome, Nome, Codice Fiscale, Email]

## Impostazione Password

A questo punto dopo aver caricato i dati, il programma chiede una **Password provvisoria** che l'utente dovrà cambiare al **Primo Accesso** (➔ **Aggiorna** ➔ **Conferma**)

[Schermata: finestra "Gestione Password" con campi Nuova Password e Conferma Password]

### Regole per la password

La password che viene richiesta ha le seguenti regole:

- Lunghezza minima **8**
- Lunghezza massima **16**
- Può contenere soltanto i simboli: `! $ % & / ( ) = ? - _ *`
- Deve contenere sia lettere che numeri
- Deve contenere almeno un simbolo

## Gestione delle Autorizzazioni

Per quanto riguarda le Autorizzazioni, avendo inserito l'utente come Duplicato, avrà tutte le Autorizzazioni dell'utente preso come base, ma nel caso queste dovessero essere modificate, sempre su:

**Amministrazione del Sistema** ➔ **Gestione Accessi** ➔ **Utenti**

una volta ricercato il soggetto, nei bottoni a destra trovo **Autorizzazioni**

[Schermata: elenco utenti con pulsante "Autorizzazioni" evidenziato a destra]

Dove andando nell'area **Demografici**, per ogni Modulo, vi è la possibilità di gestire ogni singola operazione selezionando tramite il menu a tendina il **Livello di autorizzazione** scelto:

| Livello | Descrizione |
|---------|-------------|
| **L** | Solo lettura |
| **G** | Lettura e modifica |
| **C** | Lettura, Modifica, Cancellazione |

oppure tramite gli appositi pulsanti a destra che in automatico mettono **TUTTE** le autorizzazioni di ogni Modulo dell'Area ad uno specifico Livello.

[Schermata: griglia Autorizzazioni con moduli (ANAGRAFICI, SERVIZI ECONOMICI, CONTROLLO DI GESTIONE, ecc.) e livelli di autorizzazione per ogni operazione]

## Configurazione Certificato per Colloquio ANPR

Ora che l'utente è creato, andare in:

**Anagrafe** ➔ **Tabelle** ➔ **Generiche** ➔ **Certificato per colloquio ANPR**

### Se il nuovo utente è in sostituzione di un altro impiegato:

1. **Modifica** (sempre con l'apposita matitina a sinistra del soggetto selezionato)
2. In **Codice Utente** selezionare (con l'apposita lente di ingrandimento) il nuovo soggetto da caricare
3. Selezionarlo con il **doppio click**
4. ➔ **Aggiorna**

[Schermata: tabella "Certificati per colloquio ANPR" con pulsante Modifica evidenziato]

### Se il nuovo utente va in aggiunta agli altri impiegati:

1. Selezionare un impiegato già presente ➔ **Duplica**
2. Nel campo **Codice Utente** (che in questo caso sarà vuoto) selezionare il soggetto da caricare (sempre con doppio click)
3. ➔ **Duplica**

[Schermata: form "Certificati per colloquio ANPR" in modalità duplicazione con campo Codice Utente vuoto e pulsante Duplica evidenziato]

---

> **NB:** Si ricorda che, se il nuovo utente deve operare in **ANPR**, dovrà essere profilato anche nella **WEBAPP del ministero** il cui documento guida si trova al seguente link:
>
> [https://docs.italia.it/italia/anpr/anpr/it/stabile/censimento-comuni/procedura-operativa.html](https://docs.italia.it/italia/anpr/anpr/it/stabile/censimento-comuni/procedura-operativa.html)