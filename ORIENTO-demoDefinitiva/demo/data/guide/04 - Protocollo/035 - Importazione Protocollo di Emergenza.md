# Importazione Protocollo di Emergenza

Accedere al programma **Importazione Protocolli Emergenza** dal menu principale → *Protocollo* → *Protocollo di Emergenza*.

Da qui è possibile creare un file Excel contenente l'elenco dei protocolli creati in emergenza, da importare poi nell'ambiente di protocollo.

Dal bottone **Scarica Template** si sceglie il formato Excel che si vuole utilizzare per compilare i dati da importare. Si possono scegliere formati xlsx, xls e csv.

## Struttura del file di importazione

Il file è composto da 15 colonne da compilare come segue:

| Colonna | Descrizione |
|---------|-------------|
| Numero di protocollo di emergenza | Numero di emergenza attribuito al protocollo |
| Data Protocollo | La data del protocollo di emergenza nel formato gg-mm-aaaa |
| Ora Protocollo | Ora del protocollo di emergenza nel formato 00:00:00 |
| Tipo di Protocollo | Tipologia del protocollo di emergenza (A/P/C) |
| Oggetto | Oggetto del protocollo di emergenza |
| Mittente/Destinatario | Descrizione del Mittente/Destinatario principale |
| Segnatura | Segnatura del protocollo di emergenza |
| Titolario | Titolario/Classificazione del protocollo di emergenza nel formato: `1.1` |
| Tipo Spedizione | Tipologia di spedizione/consegna del protocollo di emergenza |
| Protocollo Mittente | Eventuale numero di protocollo del mittente in arrivo |
| Data Protocollo Mittente | Eventuale data del protocollo del mittente in arrivo nel formato gg-mm-aaaa |
| Login Utente | Username dell'utente protocollatore. Deve rispettare maiuscole/minuscole ed eventuali punti dell'username |
| Ufficio | Ufficio creatore del protocollo di emergenza. Deve essere un ufficio valido associato all'utente |
| Numero Allegati | Numero di allegati del protocollo di emergenza |
| Descrizione Allegati-Note | Descrizione degli allegati del protocollo di emergenza ed eventuali annotazioni |

## Procedura di importazione

1. Compilare il file Excel con i dati dei protocolli.
2. Utilizzare il bottone **Scegli File** per caricare il file.
3. Se il file è conforme, la tabella riepilogativa di importazione verrà caricata con i dati contenuti all'interno del file Excel.
4. Verificare la colonna **Stato** (ultima colonna della tabella), che indica per ogni protocollo creato in emergenza se i dati sono corretti o se ci sono anomalie:
   - 🟢 **Verde**: sono stati compilati tutti i dati obbligatori e in modo corretto.
   - 🔴 **Rosso**: sono presenti anomalie; posizionando il mouse sul simbolo dello stato, sarà mostrata una descrizione dettagliata dell'anomalia.
5. Nel caso non ci siano anomalie, cliccare **Importa Protocolli** per confermare l'operazione.

> ⚠️ Se sono presenti anomalie, l'importazione **non verrà effettuata**.

## Modelli per la compilazione del protocollo di emergenza off-line

Scaricare i modelli, nei vari formati da poter utilizzare, che si trovano nel file zip allegato:

`prot_emergenza_template.zip`