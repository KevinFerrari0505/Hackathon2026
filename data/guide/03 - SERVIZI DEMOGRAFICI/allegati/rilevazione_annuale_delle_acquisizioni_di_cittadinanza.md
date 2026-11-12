# Rilevazione annuale delle acquisizioni di cittadinanza (Mod. Istat D.8 annuale)

La rilevazione annuale riepilogativa sulle acquisizioni e sui riconoscimenti della cittadinanza è effettuata attraverso il modello D.8. La rilevazione riguarda il conteggio delle acquisizioni e dei riconoscimenti della cittadinanza italiana giuridicamente conclusi nell'anno di riferimento.

## Normativa e modalità di compilazione

Per gli adeguamenti normativi sul D8 Annuale, sulle cittadinanze, la normativa prevede che:

- La compilazione del modello Istat D.8 è ammessa **esclusivamente via internet** collegandosi all'indirizzo [https://gino.istat.it/statocivile](https://gino.istat.it/statocivile).
- È possibile inserire manualmente i dati, utilizzando la funzionalità online del questionario, sia far acquisire al sistema un file in upload utilizzando il pulsante verde con le due frecce in alto e in basso che si trova fuori dal questionario (e poi seguire le istruzioni dal sistema).
- L'invio definitivo è richiesto **entro il 28 FEBBRAIO 2025**.

## Rilevazioni richieste ai Comuni

Ecco le rilevazioni che l'Istat chiede ai comuni:

- I comuni devono **inserire manualmente** i dati per i quesiti 2 e 4.
- I comuni **possono caricare il file** per i dati del quesito 5.

---

## Quesito 2 – Acquisizioni di cittadinanza da parte di individui iscritti in APR (nazionale)

Va indicato l'ammontare delle acquisizioni lavorate nel Comune suddivise per **sesso** e **tipologia di acquisizione**. Vanno indicate le acquisizioni che sono state giuridicamente chiuse nell'anno di riferimento della rilevazione.

Vanno conteggiati nelle varie motivazioni le seguenti tipologie di acquisizione:

| Tipologia | Descrizione |
|-----------|-------------|
| **Residenza** | I decreti emanati dal Presidente della Repubblica per concessione della cittadinanza per residenza (naturalizzazione) |
| **Matrimonio o unione civile** | I decreti emanati dal Presidente della Repubblica per concessione della cittadinanza per matrimonio |
| **Minori** | Le acquisizioni di cittadinanza per naturalizzazione dei genitori, per riconoscimento o per dichiarazione giudiziale di paternità o maternità e per adozione |
| **Elezione ai 18 anni** | Le acquisizioni di cittadinanza avvenute al compimento della maggiore età dell'individuo |
| **Iure sanguinis** | Riconoscimento di cittadinanza per discendenza da avo italiano |
| **Altro** | Altre modalità di acquisizione o riconoscimento di cittadinanza diverse da quelle sopra specificate |

---

## Quesito 4 – Acquisizione di cittadinanza da parte di residenti all'estero

Va indicato l'ammontare delle acquisizioni ottenute all'estero da parte di individui successivamente iscritti nell'AIRE del Comune, suddivise per **sesso** e **tipologia di acquisizione**.

Tipologie di acquisizione:

- **Matrimonio o unione civile**: i decreti emanati dal Presidente della Repubblica per concessione della cittadinanza per matrimonio;
- **Minori**: le acquisizioni di cittadinanza per naturalizzazione dei genitori, per riconoscimento o per dichiarazione giudiziale di paternità o maternità e per adozione;
- **Iure sanguinis consolari**: riconoscimenti di cittadinanza per discendenza da avo italiano provenienti dai consolati;
- **Iure sanguinis da tribunale**: riconoscimenti di cittadinanza per discendenza da avo italiano provenienti dai tribunali.

---

## Quesito 5 – Paese di provenienza degli individui che hanno ottenuto dall'estero la cittadinanza per iure sanguinis

Va indicato il numero di acquisizioni iure sanguinis suddivise per **sesso** e **Paese estero di provenienza** della pratica.

Solo per questo quesito è possibile sia inserire manualmente i dati, sia caricare un file in upload; in questo secondo caso bisogna predisporre un file in formato **CSV** seguendo il tracciato record, come indicato all'indirizzo [https://gino.istat.it/statocivile/documenti.php](https://gino.istat.it/statocivile/documenti.php) (file: `Tracciato_q5_per_upload_D8.xlsx`).

> **Nota operativa:** Al momento il software fornisce solo la generazione del file del quesito 5 e, nel caso, è possibile prevedere una stampa riepilogativa per i quesiti 2 e 4.

---

## QUESITO 5 – JURE SANGUINIS ESTERO

**(Causale 3.4.8 – Acquisto Cittadinanza Italiana Jure Sanguinis da registrare Ana)**

Prevede che il comune rilevi i conferimenti di cittadinanza jure sanguinis dall'estero attraverso un tracciato specifico conteggiate per il **codice stato** (Tabella Nazioni) e divise per **sesso**.

### Tracciato record per il file CSV di upload

| NOME_COLONNA | DESCRIZIONE | FORMATO_DATO | NUMERO_MAX_CARATTERI | CLASSIFICAZIONE |
|---|---|---|---|---|
| ID_RIGA_TABELLA | Progressivo di Riga della tabella che contiene la variabile | Intero | | 4 |
| A5_CODICE_PAESE | Codice Paese di provenienza | Numero intero | 3 | stato estero cittadinanza |
| A5_M | Maschi | Numero intero | | 4 |
| A5_F | Femmine | Numero intero | | 4 |