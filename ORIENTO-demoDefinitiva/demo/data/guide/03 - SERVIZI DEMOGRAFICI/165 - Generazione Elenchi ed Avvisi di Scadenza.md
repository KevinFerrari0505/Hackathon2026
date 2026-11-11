# Generazione Elenchi ed Avvisi di Scadenza

Questo programma permette di generare gli avvisi (notifiche cartacee o messaggi APP.IO) da inviare ai cittadini per il rinnovo della *dimora abituale* e quindi generare un avviso di scadenza per tutti i cittadini per i quali è presente un documento in scadenza; quest'ultimo lo si può vedere dalla **Gestione Documenti**. Allo stesso tempo è possibile generare una *diffida* nel caso di documenti scaduti per i quali i cittadini non si sono presentati in comune dopo aver ricevuto l'avviso.

## Percorso di menu

Il programma è presente al seguente percorso di menù:

**Servizi Demografici → Anagrafe → Stampe → Generazione Elenchi ed Avvisi di Scadenza**

## Compilazione della form

Compilare nella form i dati richiesti, come ad esempio:

- **Tipo documento**
- **Data avviso**
- **Ricerca su** (APR/AIRE)
- **Includi soggetti**
- **Scadenza** (intervallo di date: dal / al)

per filtrare i soggetti per i quali si vuole generare l'avviso di scadenza. Scegliere poi un **testo da stampare** e il **tipo comunicazione** → **Elabora** per stampare i testi per tutti i soggetti con quelle determinate caratteristiche.

[Schermata della form "Generazione Elenchi ed Avvisi di Scadenza" con i campi: Tipo documento (Permesso di Soggiorno), Data avviso, Ricerca su (APR), Includi: Italiani / Extracomunitari / Comunitari, Scadenza dal/al, Includi soggetti senza documento, Testo per stampa lettera avviso, Tipo comunicazione (Avviso 60gg per rispondere), Elenco cittadini (Excel), Invio avviso tramite App IO, Reinvio avviso tramite app.IO, Oggetto App IO, Messaggio App IO. Pulsanti: Elabora, Parametri Ricerca, Reset.]

> **Nota:** Non è necessario compilare tutti i campi della form. Da qui è possibile anche produrre un semplice elenco di tutti i nominativi con il permesso di soggiorno in scadenza selezionando solo alcune voci e poi cliccare su → **Elabora**.

## Generazione della diffida

Lo stesso concetto vale anche per le **diffide**. Ricordarsi di includere i soggetti per i quali non si ha un documento nel caso.

## Generazione della notifica APP IO

Vale la compilazione descritta sopra: inserire i filtri che estrarranno i soggetti. Nel caso si voglia generare una notifica APP.IO:

1. **Non** selezionare il codice testo
2. Selezionare il flag corrispondente all'invio tramite **APP.IO** (campo "Invio avviso tramite App IO")
3. Compilare l'**Oggetto App IO** ed il **corpo del testo** della notifica (campo "Messaggio App IO") che si vuole compaia sull'APP.IO del soggetto
4. Cliccare su **ELABORA** a destra per completare l'invio

[Schermata della form con il campo "Invio avviso tramite App IO" selezionato (checkbox spuntata), e i campi "Oggetto App IO" e "Messaggio App IO" con editor di testo formattato (B, I, H, virgolette, elenchi, link, immagine, anteprima).]