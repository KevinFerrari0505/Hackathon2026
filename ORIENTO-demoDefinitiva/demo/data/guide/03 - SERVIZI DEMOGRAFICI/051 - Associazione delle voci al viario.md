# Associazione delle voci al viario

**Punto di menù:**
Servizi Demografici > Modulo Base > Tabelle Generali > Viario > Divisione del Territorio > Associazione delle Voci al Viario

In questo punto di programma è possibile aggiungere, consultare e modificare le vie associate agli elementi all'interno del sistema. Questa funzionalità consente di definire con precisione su quali vie (o parti di via) un determinato elemento e la relativa voce risultano validi, specificando anche eventuali intervalli di numeri civici.

## Tipi di ricerca

La finestra presenta 3 differenti tipi di ricerca a seconda di ciò che serve:

1. **Ricerca per elemento e voce:** Utile quando si vuole analizzare o modificare una voce specifica.
2. **Ricerca per elemento:** Vengono mostrate tutte le vie associate all'elemento selezionato.
3. **Ricerca per via:** Vengono visualizzati tutti gli elementi e le voci collegati a quella via.

Quando viene selezionata una via, il sistema mostra un elenco riepilogativo contenente le voci già associate, il tipo di associazione (intera via, pari o dispari) e l'intervallo dei numeri civici. In questo modo è possibile verificare rapidamente eventuali associazioni già esistenti e/o possibili sovrapposizioni.

[Schermata della finestra di ricerca con i tre radio button "Tipo di Ricerca": "Dato un elemento e una voce, mostra le vie associate", "Dato un elemento, mostra le vie associate sulle varie voci", "Data una via, mostra su quali elementi e voci è collegata". Campi: Elemento, Via da/a. Pulsanti: Nuovo, Elenca, Carica, Salva, Reset.]

## Aggiungere una nuova via ad un elemento

Cliccare il bottone → **Nuovo**, aprendo così la schermata di inserimento di una nuova associazione. All'apertura della form, viene automaticamente impostato un progressivo e l'associazione viene impostata su *intera via*. Passare a compilare quindi i campi principali:

- **Elemento:** Codice elemento di definizione del territorio (VEDI: Elementi)
- **Voce:** Codice voce elemento
- **Via:** Codice della via (VEDI: VIE)
- **Associazione:** scegliere una delle seguenti opzioni:
  - *Intera via:* È possibile indicare numero civico iniziale e finale e gli eventuali sottonumeri.
  - *Pari, Dispari:* spezzare la via e creare quindi due associazioni.

Quindi premere il bottone → **Aggiungi**

[Schermata del form di inserimento: Progressivo (1416), Elemento*, Voce*, Via*, Associazione (dropdown "Intera Via"), N.Civ.Iniziale, N.Civ.Finale, Sottonumero iniziale, Sottonumero finale. Pulsanti: Aggiungi, Altra Ricerca. Sotto: tabella "Voci già attribuite per questa via e elemento" con colonne Pari-Dispari-Tutta, Dal numero, Al numero, assegnato alla Voce.]

## Modificare un'associazione esistente

Per modificare una via già associata a un elemento, come prima cosa è necessario individuare il record tramite la ricerca, entrare in modifica del dettaglio con la **'matitina'** ed apportare le modifiche necessarie:

- Tipo di associazione
- Intervallo dei civici (è possibile impostare l'associazione *pari* indicando civico iniziale e finale)
- Sottonumeri (se previsti)

Quindi cliccare il bottone → **Aggiorna**

### Esempio

[Schermata di modifica associazione: Progressivo 1134, Elemento 5 (SEZIONI ELETTORALI), Voce 4 (Scuola Materna Via dello Sport 4), Via 30 (VIA CAPRERA), Associazione: Pari, N.Civ.Iniziale: 2, N.Civ.Finale: 80, Sottonumero iniziale/fine non impostati.]

| Pari - Dispari - Tutta | Dal numero | Al numero | Assegnato alla Voce |
|---|---|---|---|
| Pari | 2 | 80 | 4 Scuola Materna Via dello Sport 4 |