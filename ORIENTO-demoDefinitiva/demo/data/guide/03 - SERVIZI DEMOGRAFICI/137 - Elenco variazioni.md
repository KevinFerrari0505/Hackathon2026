# Elenco variazioni

Con questo programma si può generare un file di riepilogo di tutte le variazioni effettuate nel periodo di tempo che viene indicato (Es. Iscrizioni per Nascita, Cancellazioni per Morte, Cambio indirizzo ecc..)

Il percorso da seguire è:

**Servizi demografici ⇒ Anagrafe ⇒ Variazioni ⇒ Elenco Variazioni**

[Schermata del menu di navigazione: Servizi demografici → Anagrafe → Variazioni → 110. Elenco Variazioni]

## Inserimento del periodo di tempo

Entrando, la finestra come prima cosa propone l'inserimento del periodo di tempo, di default presenta flaggate 3 possibilità:

[Schermata "Elenco Variazioni Anagrafe" con campi "Dalla Data" e "Alla Data" e tre checkbox flaggate]

- **"Data Registrazione"**: si riferisce alla data della registrazione e non dell'evento (evento 01/01/2024 - registrazione **04/01/2024**)
- **"Estraggo le pratiche registrate"**: registrazione nelle 48h (anche se non sono confermate)
- **"Crea istruzioni di accompagnamento"**: legenda sulle voci dell'estrazione (consigliate per la prima volta)

### Istruzioni di accompagnamento

[Schermata "Istruzioni di accompagnamento per estrazione Variazioni Anagrafiche" con tabella GRUPPO / COLONNA / NOTE]

| GRUPPO | COLONNA | NOTE |
|--------|---------|------|
| GENERALITÀ | | |
| | CODFISCALE | Codice Fiscale del cittadino |
| | COGNOME | CogNOME del cittadino |
| | NOME | Nome del cittadino |
| | DATANAS | Data di Nascita del cittadino |
| | SESSO | Sesso del cittadino |
| | LUOGO_NASCITA | Luogo di Nascita del Cittadino |
| | PROV_NASCITA | Provincia di Nascita del cittadino |
| | STATO_NASCITA | Stato di Nascita del cittadino |
| | ISTAT_NASCITA | Codice Istat relativo al luogo di Nascita del cittadino |
| | CITTADINANZA | Cittadinanza del Soggetto |

## Opzioni alternative (flag non selezionati)

Ma vi è anche la possibilità di togliere il flag delle 3 opzioni facendogli acquistare un altro significato:

[Schermata "Elenco Variazioni Anagrafe" con checkbox non flaggate: "Data evento", "Estraggo le pratiche confermate", "Non crea istruzioni di accompagnamento"]

- **"Data Evento"**: si riferisce alla data dell'evento e non della registrazione (evento **01/01/2024** - registrazione 04/01/2024)
- **"Estraggo le pratiche confermate"**: Pratiche confermate (Accertamento nei 45gg)
- **"Non crea istruzioni di accompagnamento"**: non crea la legenda sulle voci dell'estrazione

## Selezione dei tipi di variazione e informazione

Una volta impostate queste prime 4 voci, il programma propone i **tipi di variazione** e i **tipi di informazione** da impostare per l'estrazione.

### Tipi di Variazione

| Sel. | Tipo Variazione |
|------|-----------------|
| ✓ | Iscrizioni per Nascita |
| ✓ | Iscrizioni altri motivi |
| ✓ | Cancellazioni per Morte |
| ✓ | Cancellazioni altri motivi |
| ✓ | Cambio indirizzo |

### Tipi di Informazione

| Sel. | Tipo Informazione |
|------|-------------------|
| | frazione |
| ✓ | indirizzo |
| ✓ | operazione |
| | famiglia |
| | codici |

Di default presenta già selezionati tutti i vari tipi di variazione e solo due tipi di informazione, ma è possibile modificare le varie scelte semplicemente con il click del mouse sulla spunta che si desidera togliere o nello spazio vuoto che si desidera aggiungere.

## Estrazione

Una volta effettuate tutte le scelte si procede all'estrazione cliccando sulla destra il tasto → **Elenco Variazioni**

[Pulsante "Estrai Variazioni" con icona di download]

che scaricherà un file Excel con tutto ciò che è stato chiesto nella schermata principale.

[Schermata di anteprima del file Excel generato con colonne: CODFISCALE, COGNOME, NOME, DATANAS, SESSO, LUOGO_NASCITA, PROV_NASCITA, STATO_NASCITA, ISTAT_NASCITA, CITTADINANZA, E. ESTRAT, TI...]