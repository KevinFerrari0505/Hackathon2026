# VARIAZIONE DATA SCADENZA DOCUMENTI

Questo programma permette di convertire una data fissa impostata in un'altra. Viene fatta una ricerca nei dati per i documenti che hanno la data di scadenza impostata; una volta trovati, sostituisce la data di scadenza calcolandola come la data di emissione del documento sommata al periodo che imposteremo a video (10 anni, 7 mesi, 5 giorni ecc.).

> **VNB:** VOI DOVRETE MODIFICARE QUEI DOCUMENTI CHE HANNO SCADENZA **31/12/9999**, QUINDI DOVE NOI ABBIAMO POSIZIONATO **11/11/1811** VOI METTETE **31/12/9999**

---

## Accesso al programma

Seguire il percorso indicato per effettuare l'accesso o in alternativa digitare il nome del programma nella barra di ricerca applicazioni.

[Immagine: Percorso di accesso al programma tramite menu: Servizi di Sviluppo → 180. Servizi Esigenze → 80. Variazione data scadenza documenti]

---

## Utilizzo del programma

Come da immagine, procedere compilando la sezione di sinistra per poi eseguire il programma:

[Immagine: Schermata del programma "Variazione data documenti" con i campi: Tipo documento, Scadenza, Periodo e pulsante "Esegui". Note a schermo: "SELEZIONARE IL TIPO DOCUMENTO, DALLA LISTA DELLE PROPRIE" / "MODIFICA: - LA DATA DI SCADENZA, CHE VIENE USATA COME FILTRO PER SELEZIONARE DAI DATI TUTTI I DOCUMENTI CHE PER UN TIPO DEFINITO HANNO QUELLA DATA DI SCADENZA. - PERIODO, INSIEME A TEMPO CHE VIENE AGGIUNTO ALLA DATA DI EMISSIONE QUINDI (PERIODO + DATA DI EMISSIONE) PER I DOCUMENTI CHE SARANNO SELEZIONATI. VIENE ESPRESSO IN GIORNI, MESI E ANNI E NEL PRIMO CAMPO SI IMMETTE IL VALORE NUMERICO, COME ES. 20, 30 (GIORNI/GIORNI/MESI)"]

### Esempio (ambiente di test con dati fittizi)

Scelgo il tipo documento, vedo la data di scadenza, che per esempio era impostata nel 1811, ed è come se dicessi al programma che: *"Per ogni documento con questa data di scadenza, prendi la data di rilascio e somma il periodo che ti ho indicato, in questo caso 200 anni"*.

> ⚠️ **Attenzione:** i dati usati nell'esempio non sono reali quindi i risultati possono essere dissimili da quelli che avrete voi nell'utilizzo.

> **VNB:** VOI DOVRETE MODIFICARE QUEI DOCUMENTI CHE HANNO SCADENZA **31/12/9999**, QUINDI DOVE NOI ABBIAMO POSIZIONATO **11/11/1811** VOI METTETE **31/12/9999**

**Parametri dell'esempio:**

| Campo | Valore |
|-------|--------|
| Tipo documento | 6 – Permesso di Soggiorno |
| Scadenza | 11/11/1811 |
| Periodo | 200 anni |

### Esecuzione e conferma

Una volta lanciato il programma, verrà visualizzato un messaggio di conferma della modifica:

[Immagine: Finestra "Attenzione" con messaggio: "Sono stati trovati 113 documenti. La nuova data di scadenza verrà calcolata come la data di rilascio + 200 anni. Si desidera confermare l'operazione?" con pulsanti F5-Conferma / F8-Annulla]

Il programma indica:
- Il numero di documenti trovati con la data di scadenza impostata (es. 113 documenti)
- Il calcolo che viene fatto in base ai dati immessi

Procedere con la conferma dell'operazione (**F5-Conferma**).

### Elaborazione e risultato

Vedrete una fase di elaborazione la cui durata dipende dalla mole di dati che andrete a modificare, e di seguito un messaggio di avvenuta modifica:

[Immagine: Finestra "Attenzione" con messaggio: "Operazione conclusa con successo. Sono stati aggiornati con successo 113 documenti."]

---

## Aggiornamento dati in CWOL

L'aggiornamento interessa i dati dei documenti che sono visualizzati nei programmi di **CWOL - Cityware Online**, quindi aggiornando i documenti e poi interrogando i soggetti vedrete i dati nuovi.