# Tabelle Collegi

La tabella è utilizzata per definire eventuali collegi o circoscrizioni, è possibile aggiungerne o modificarne sempre, rispettivamente, dai pulsanti **nuovo** e modifica**(matitina)**.

[Schermata: interfaccia "Tipi collegio" con elenco dei codici ministeriali: 1-Senato, 2-Camera, 3-Parlamento europeo, 4-Regionali, 101-Senato, 102-Camera, 103-Parlamento europeo, 104-Regionali, 105-Provinciali, 106-Circoscrizionali. Ogni riga presenta icone per visualizzazione e modifica.]

All'interno dei record sono contenuti i codici ministeriali che identificano la suddivisione del territorio che fa seguito alla normativa elettorale in vigore. **NB.** La modifica di tali codici si effettua solo, ed esclusivamente, nel caso di modifiche alla normativa vigente.

## Dettaglio del record

[Schermata: vista di dettaglio di un tipo collegio con Id "101" e Descrizione "Senato". Sotto è presente la "Tabella Collegi" con i campi: Numero e un campo testo contenente il codice territoriale (es. "MARCHE | P01 | U01"). Sono presenti i pulsanti di azione: aggiungi (+), elimina (cestino), impostazioni (ingranaggio). In basso è visibile la sezione "Audit" con data/ora ultima modifica e utente che ha effettuato la modifica.]

### Struttura della Tabella Collegi

| Numero | Codice territoriale |
|--------|---------------------|
| 1 | MARCHE \| P01 \| U01 |
| 0 | test |

### Campi del record

- **Id\***: codice identificativo del tipo collegio (campo obbligatorio)
- **Descrizione\***: nome del tipo collegio (campo obbligatorio)
- **Tabella Collegi**: sotto-tabella contenente i codici territoriali ministeriali associati al collegio
  - **Numero**: progressivo del codice
  - **Codice territoriale**: stringa che identifica la suddivisione del territorio secondo la normativa elettorale vigente (formato: `REGIONE | P<provincia> | U<ufficio>`)

### Sezione Audit

Ogni record riporta le informazioni di tracciamento:

- **Ultima modifica**: data e ora dell'ultima modifica
- **Effettuata da**: utente che ha eseguito la modifica