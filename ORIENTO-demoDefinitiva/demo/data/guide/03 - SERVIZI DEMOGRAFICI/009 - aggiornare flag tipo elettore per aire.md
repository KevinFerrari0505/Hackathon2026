# Allineamento Flag Elettore per Iscritti Aire

## Contesto

Ogni anno il Ministero degli Affari Esteri invia una circolare con scadenza **31.12.0000** di ogni anno relativa all'aggiornamento dell'Elenco unico dei cittadini residenti all'estero (AIRE).

I Comuni devono:
- Controllare gli indirizzi AIRE
- Verificare il campo **"TIPO ELETTORE"**
- Risolvere le anomalie segnalate sulla web app, se presenti

## Procedura di aggiornamento del campo Tipo Elettore per gli AIRE

### Percorso nel gestionale

```
Servizi Demografici > Anagrafe > ANPR - Funzioni di Servizio > ANPR - Allineamento elettori aire
```

### Passaggi operativi

1. Accedere alla funzione **ANPR: allinea elettori AIRE**
2. **Non cambiare nessun valore** e confermare la videata che si presenta
3. Cliccare sul pulsante **Conferma**

[Schermata: Videata "ANPR: allinea elettori AIRE" con messaggio "Verrà allineato su ANPR il dato di elettore sì/no, per gli iscritti Aire." e avvertenza "Attenzione: chiudere il messaggio a video non terminerà l'elaborazione sul server." Campi visibili: "A partire dalla matricola: 0" e "per numero di soggetti: 99999". Pulsanti: "Conferma" e "Apr il Log".]

### Tempi di elaborazione

> ⚠️ Il programma può impiegare parecchi minuti, dipende da quanti AIRE deve aggiornare.

### Anomalie riscontrate

Al termine dell'elaborazione può comparire un **file con le anomalie riscontrate** da aggiornare a mano.

## Nota Tecnica – Anomalie rilevate nella banca dati AIRE

Da verifiche effettuate in base all'Elenco Unico sono state rilevate nella banca dati AIRE posizioni che presentano anomalie. Per consentirne la correzione sono stati predisposti i seguenti elenchi:

- AIRE Elenchi Anomalie – Soggetti con codice territorio di nascita valorizzato ma senza luogo di nascita
- AIRE Elenchi Anomalie – Soggetti con codice territorio di nascita valorizzato e luogo nascita uguale alla denominazione di un comune italiano
- AIRE Elenchi Anomalie – Soggetti con tipo elettore non valorizzato
- AIRE Elenchi Anomalie – Soggetti indirizzo o località che riportano il nome di uno stato estero
- AIRE Elenchi Anomalie – Soggetti SOLO MIN che non vengono aggiornati da almeno 4 anni
- AIRE Elenchi Anomalie – Soggetti con luogo nascita composto da soli caratteri speciali o numeri
- AIRE Elenchi Anomalie – Soggetti con cognome, nome, o cognome coniuge composto da soli caratteri speciali o numeri
- AIRE Elenchi Anomalie – Soggetti con codice ISTAT comune di nascita inesistente
- AIRE Elenchi Anomalie – Soggetti con territorio di nascita errato
- AIRE Elenchi Anomalie – Soggetti nati a Fiume, Pola, Zara dopo il 15/09/1947
- AIRE Elenchi Anomalie – Posizioni senza indicazione del comune o dello stato estero di nascita
- AIRE Elenchi Anomalie – Soggetti con luogo nascita contenente parole non valide
- AIRE Elenchi Anomalie – Soggetti con luogo di residenza contenente parole non valide
- AIRE Elenchi Anomalie – Soggetti con toponimo di residenza non valorizzato
- AIRE Elenchi Anomalie – Soggetti con residenza non individuabile
- AIRE Elenchi Anomalie – Data arrivo circoscrizione consolare non valida
- AIRE Elenchi Anomalie – Codici fiscali duplicati
- AIRE Elenco Unico – Soggetti scartati nell'elenco unico

## Comune subentrato

I suddetti elenchi sono disponibili facendo accesso all'applicazione **Web di ANPR** e selezionando la voce di menù **Utilità e notifiche**.

Dal menù di sinistra:
1. Cliccare su **Download**
2. Selezionare il **Tipo file**
3. Cliccare su **Conferma**
4. Cliccare sul **numero di protocollo** del file visualizzato per effettuare il download sul proprio PC

Per ciascuna posizione elencata è necessario:
- Verificare l'anomalia segnalata
- Apportare le necessarie modifiche sul gestionale o sull'applicazione WEB di ANPR

## Contatto tecnico

Per informazioni tecniche contattare **SOGEI** al recapito: **800.863.116**