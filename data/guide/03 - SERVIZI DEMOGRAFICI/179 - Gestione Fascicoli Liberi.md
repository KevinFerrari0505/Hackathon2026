# Gestione Fascicoli Liberi

Permette la gestione dei suddetti fascicoli: il progressivo fascicolo libero e il codice armadio non sono compilabili in quanto fa riferimento al primo spazio libero che trova. Il flag "occupato" permette di designare come occupato o meno quello spazio e attraverso la lente è possibile effettuare un interrogazione elettorale per prendere il fascicolo.

## Interfaccia di gestione

[Schermata: Finestra "Gestione fascicoli liberi" con i seguenti campi:]

| Campo | Descrizione | Esempio |
|-------|-------------|---------|
| **Fascicolo** * | Progressivo del fascicolo (non compilabile, valorizzato automaticamente con il primo spazio libero) | `12` |
| **Codice Armadio** | Codice dell'armadio di riferimento (non compilabile) | `A01` |
| **Occupato?** | Flag (checkbox) per designare lo spazio come occupato o libero | ☑ |
| **Matricola** | Campo con pulsante di ricerca (lente) per interrogazione elettorale e assegnazione del fascicolo | `2785` |

## Note operative

- I campi **Fascicolo** e **Codice Armadio** sono in sola lettura: il sistema valorizza automaticamente il primo spazio libero disponibile.
- Il flag **Occupato?** consente di marcare manualmente uno spazio come occupato o liberarlo.
- Tramite il pulsante **lente** (🔍) accanto al campo *Matricola* è possibile effettuare un'interrogazione elettorale per selezionare e associare il fascicolo desiderato.