# Gestione Sospesi

Tale programma permette la gestione dei cittadini che perdono il diritto di voto e quindi devono essere "Sospesi".

Il percorso da seguire è il seguente:

**Servizi Demografici ⇒ Elettorale ⇒ Manutenzione ⇒ Variazione Extrarevisione ⇒ Gestione Sospesi**

[Schermata del menu di navigazione del software che mostra il percorso: Servizi Demografici → Elettorale → Manutenzione → Variazione Extrarevisione → Gestione Sospesi]

Per la gestione di tali soggetti, ci possono essere 2 casistiche:

1. Arriva la comunicazione di sospensione del diritto elettorale di un residente, **già iscritto** alle liste elettorali del comune;
2. Arriva la comunicazione di sospensione del diritto elettorale di un residente, **NON** ancora iscritto nelle liste elettorali.

---

## Caso 1

*"Comunicazione di sospensione del diritto elettorale di un residente, già iscritto alle liste elettorali del comune".*

In questo caso, bisognerà procedere in questo modo:

1. Andare all'interno del programma **"Gestione Sospesi"** (seguendo il percorso sopra indicato).
2. Una volta entrati, bisognerà premere il bottone **"Altra Ricerca"** così da andare nella schermata di ricerca.
3. Da lì, togliere il flag **"Sospesi"** e mettere il flag **"Elettori"** e ricercare l'elettore in questione.

[Schermata di ricerca con i flag "Elettori", "Sospesi", "Cancellati", "Non Iscritti" e il pulsante "Altra Ricerca" evidenziato in rosso sulla barra laterale destra]

4. Una volta ricercato l'elettore, selezionare con un solo click il record (il record deve diventare giallo) e premere sulla destra **"Invio ANPR cert. BLOCCATA"**.

[Schermata di interrogazione elettorale con un record selezionato (evidenziato in giallo) e il pulsante "Invio ANPR Cert. BLOCCATA" evidenziato in rosso sulla barra laterale destra]

5. Una volta fatto questo, cancellare il cittadino dalle proprie liste elettorali con la prima dinamica utile, inserendo la causale di cancellazione (che può essere, ad esempio, *interdizione pubblici uffici* oppure *condanna penale* ecc..), indicando la **certificabilità elettorale sospesa** e la **data di riacquisto diritto** nell'apposito campo (**nel caso la sospensione dovesse essere perpetua, nel campo si indicherà 31/12/9999**).

[Schermata "Gestione Cancellandi" con i campi evidenziati in rosso: "Data Riac. Diritto", "Causale Revisione" impostata su "Interdizione pubblici uffici", e "Posizione certificabile" impostata su "Certificabilità Elettorale Sospesa"]

---

## Caso 2

*"Comunicazione di sospensione del diritto elettorale di un residente, NON ancora iscritto nelle liste elettorali"*

Per questa casistica, essendo il cittadino non ancora iscritto nelle liste elettorali del comune, il tutto verrà gestito attraverso il programma **"Gestione Sospesi"**.

1. Come prima cosa, andare all'interno del programma (seguendo il percorso sopra indicato) e premere il bottone **"Altra Ricerca"**.

[Schermata di interrogazione elettorale con il pulsante "Altra Ricerca" evidenziato in rosso sulla barra laterale destra]

2. Una volta fatto, bisognerà indicare il **tipo di lista** e premere il bottone **"Nuovo"**.

[Schermata con il campo "Tipo Lista" a tendina evidenziato in rosso e il pulsante "Nuovo" evidenziato in rosso sulla barra laterale destra]

3. Premendo il bottone **"Nuovo"**, si aprirà l'archivio unico dei soggetti dal quale andare a selezionare il cittadino in questione.

4. Una volta selezionato, si aprirà la schermata dove bisognerà impostare i seguenti campi con i seguenti dati:

| Campo | Valore da impostare |
|-------|-------------------|
| **Stato** | `N` (indica che il soggetto non è iscritto alle liste elettorali del comune) |
| **Posizione Certificabile** | `Certificabilità elettorale sospesa` |
| **Data Riacq. Diritto** | Se la sospensione è perpetua: `31/12/9999`; altrimenti la data reale di riacquisto diritto elettorale |

[Schermata di inserimento soggetto con i campi evidenziati in rosso: "Stato" impostato su "N - Non Iscritto", "Posizione certificabile" impostato su "Certificabilità Elettorale Sospesa", e "Data Riacq. Diritto" impostato su "31/12/9999"]

5. Una volta aggiunto il soggetto, tornare nella schermata di ricerca, porre il flag su **"Non Iscritti"** e fare **elenca**.

[Schermata di ricerca con il flag "Non Iscritti" spuntato (evidenziato in rosso) e gli altri flag deselezionati]

6. Selezionare poi il soggetto e premere il bottone **"Invio ANPR cert. BLOCCATA"**.

[Schermata di interrogazione elettorale con i soggetti "Non Iscritti" (Stato N) visualizzati in giallo e il pulsante "Invio ANPR Cert. BLOCCATA" evidenziato in rosso sulla barra laterale destra]