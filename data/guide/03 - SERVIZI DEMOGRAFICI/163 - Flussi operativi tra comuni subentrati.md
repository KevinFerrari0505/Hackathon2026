# Flussi operativi tra comuni subentrati

## Premessa

In questa guida potete trovare le informazioni generali su quali sono le operazioni da eseguire per la redazione di un atto, la gestione delle notifiche e il passaggio dei dati in anagrafe nonché la gestione delle annotazioni. Con le parole "flussi operativi" intendiamo l'**elenco delle operazioni**, si rimanda alle singole guide che trovate a questo link per vedere nel dettaglio come eseguirle, [elenco guide per atti].

Nel caso riscontriate casistiche non censite dalle presenti guide, che riportano le informazioni di SOGEI, potete contattare contatti SOGEI ANSC o chiamare il 800 863 116 o aprire un ticket presso di noi assistenza citypeople.

---

## Iter emissione Atto Digitale e Annotazioni Automatiche

Questa sezione è dedicata al flusso di notifiche automatiche generate da un atto. Prima di vedere l'iter una premessa:

- ANSC distingue tra **Atto primario digitale** e **Atto secondario digitale**, il primo è l'atto che viene annotato mentre il secondo è quello che genera le annotazioni, questo è importante per l'ID ANSC SOGGETTO che come l'ID ANPR identifica i soggetti degli atti in modo univoco.

L'iter di emissione dell'atto digitale è il seguente:

1. **Redazione dell'atto**, che trovate spiegate per singolo registro a questa pagina [elenco guide per atti]
2. **Controllo Automatico**, alla conferma dell'atto ANSC effettua una verifica sull'atto: "esiste un'altro atto digitale intestato a quel soggetto?"

| Atto Primario | Gestione della notifica ANSC | Gestione della Notifica ANPR | Subentrato |
|---|---|---|---|
| Digitale | Genera automaticamente proposta annotazione ai comuni competenti | Generata verso il comune di residenza | SI |
| Cartaceo | Generata verso il comune che redige atto digitale (poi la invia) | Riceve comunicazione via PEC | NO |

Si aprono due casi:

1) L'atto che confermate è il **primo atto digitale** per quel soggetto, in quel caso sarete voi a generare l'ID ANSC SOGGETTO: quindi **il sistema genera una notifica che scaricherete e invierete ai comuni competenti via PEC**, la dovete approvare prima, che provvederanno ad annotare l'atto primario cartaceo e ad aggiornare l'anagrafe.

2) L'atto che avete confermato annota un atto già presente in ANSC, in quel caso il sistema **genera una notifica automatica indirizzata al comune che detiene l'atto di nascita** che andrà validata da USC. Successivamente alla validazione il sistema genera una notifica per la registrazione anagrafica al comune di residenza, se subentrato in ANSC. **Attenzione:** il Comune che detiene atto di nascita (atto primario) può coincidere con il comune di residenza

3) Nel caso invece dovete trascrivere un atto o apporre un annotazione digitale su comunicazione di comune non subentrato consultate questa guida: [Elenco operazioni da comuni non subentrati] e l'ultimo punto di questa guida: ITER PER CASI D'USO DI SERVIZIO

Di seguito una rappresentazione grafica dei flussi operativi per i punti 1 e 2:

[Diagramma di flusso: "Redazione e conferma Atto" → "Controllo Automatico su Atto Primario/Secondario" → Branch 1: "è Atto Primario" → "ANSC genera notifica che si protocolla ai comuni competenti". Branch 2: "è Atto Secondario" → "Notifica automatica al comune che ha Atto Primario e al comune di residenza" → "Comune Atto Primario: Riceve una notifica di annotazione che accetta ed esegue" → "Comune di residenza: Recupera la notifica ANPR e aggiorna anagrafe"]

Per altre informazioni sulle notifiche e la loro gestione vi invitiamo a consultare l'apposita guida: [Gestione notifiche ANSC]

---

## Iter Annotazione Digitale

Lo stesso concetto si applica per le annotazioni, sia che derivino da atti digitali di comuni subentrati che da comunicazioni di enti esterni (tribunali, avvocati…):

- riceverete una notifica nel portlet ANSC che andrete a gestire approvandola e scaricandone il contenuto, non sarà necessario eseguire l'annotazione sul vostro atto digitale in quanto le notifiche sono automatizzate

Per **notifica automatica** si intende un'annotazione generata da ANSC sul vostro atto digitale partendo da un evento di stato civile avvenuto in altro comune subentrato.

[Diagramma di flusso: "Ricezione notifica ANSC" → "USC Gestisce il Portlet" → "Notifica automatica: USC approva la notifica"]

---

## Iter gestione notifica ANSC

Per la gestione completa delle notifiche ANSC, le azioni che potete compiere, vi si rimanda all'omonima guida [Gestione notifiche ANSC]. Invece, per quanto riguarda l'iter di gestione che SOGEI ha definito è il seguente:

1. Ogni Atto Digitale e Annotazione produce una **notifica ANSC** che viene inviata ai comuni interessati (nascita, residenza…)
2. Questa notifica deve essere **approvata dall'USC**
3. Una volta che la notifica ANSC è approvata da USC viene generata un'ulteriore **notifica anagrafica** al comune di sola residenza per l'aggiornamento dei dati anagrafici: l'Ufficiale di Anagrafe provvederà a gestirla compiendo tutte le operazioni per la modifica del dato sia nella banca dati locale che in ANPR.

Questo vale sia quando si emette un atto digitale, quindi sarà il vostro comune a creare i presupposti per l'invio automatico delle notifiche, sia che siate voi a ricevere le notifiche.

Lato Palitalsoft il passaggio delle variazioni anagrafiche derivanti da un evento ANSC avviene in questo modo:

- Se deriva da un atto da voi redatto, dopo aver approvato la notifica, utilizzerete il programma **Conferma atti digitali e passaggio in anagrafe**
- Se deriva da un atto redatto da altro Comune, approverete la notifica ricevuta, e utilizzerete la funzione **Eventi anagrafici da Atti ANSC**

### Esempio di Iter di notifica e aggiornamento anagrafe da atto ANSC di altro comune:

[Diagramma di flusso: "Ricevo notifica ANSC" → "USC approva" (L'Ufficiale di Stato Civile) → "ANPR genera una notifica per l'aggiornamento anagrafe" → Branch: "L'Ufficiale di Anagrafe: Usa la funzione 'NUOVI EVENTI' per aggiornare l'anagrafe locale e ANPR indicando gli estremi ID ATTO ANSC"]

### Esempio di Iter di notifica e aggiornamento anagrafe da atto ANSC del proprio Comune:

L'iter è il medesimo: redigerete l'atto e a seconda della causale CWOL che sceglierete dovrete o usare il programma di conferma degli eventi di stato civile oppure eseguire una variazione con il programma **NUOVI EVENTI**:

[Diagramma di flusso: "Ricevo notifica ANSC" → "USC approva" (L'Ufficiale di Stato Civile) → "ANPR genera una notifica per l'aggiornamento anagrafe" → Branch 1: "L'Ufficiale di Anagrafe: Usa la funzione 'NUOVI EVENTI' per aggiornare l'anagrafe locale e ANPR indicando gli estremi ID ATTO ANSC". Branch 2: "L'Ufficiale di Anagrafe: Usa la funzione CONFERMA EVENTI STATO CIVILE per aggiornare l'anagrafe locale e ANPR indicando gli estremi ID ATTO ANSC"]

---

## Iter per casi d'uso di servizio

Il dettaglio delle operazioni per queste casistiche è spiegato con esempi pratici a questa guida [Elenco operazioni da comuni non subentrati]; di seguito l'iter delle operazioni:

1) Nel caso riceviate comunicazione di eseguire una trascrizione da comune non subentrato, dovrete redigere l'atto come **Trascrizione** usando il caso d'uso di servizio, una volta fatto riceverete una notifica da approvare ed una volta approvata procederete alle comunicazioni verso il comune non subentrato

2) Nel caso dovete annotare un atto digitale per un evento proveniente da comune non subentrato userete i **casi d'uso di servizio per le annotazioni**, che anche in quel caso genereranno una notifica indirizzata al vostro comune, procederete poi alle comunicazioni verso il comune non subentrato

Per i punti 1 e 2 potrete anche inviare direttamente il PDF della notifica che avete ricevuto protocollandolo verso il comune

Rappresentazione grafica riferita ai punti 1 e 2:

[Diagramma di flusso: "Ricevo comunicazione da comune non subentrato" → "USC redige atto/annotazione con CASO D'USO DI SERVIZIO" (L'Ufficiale di Stato Civile) → "ANPR genera una notifica per l'aggiornamento anagrafe" → Branch 1: "L'Ufficiale di Anagrafe: Usa la funzione 'NUOVI EVENTI' per aggiornare l'anagrafe locale e ANPR indicando gli estremi ID ATTO ANSC". Branch 2: "L'Ufficiale di Anagrafe: Usa la funzione CONFERMA EVENTI STATO CIVILE per aggiornare l'anagrafe locale e ANPR indicando gli estremi ID ATTO ANSC"]

3) Nel caso un'altra PA vi dia comunicazione di dover annotare l'atto userete il **caso d'uso di servizio riservato alla comunicazioni da altre amministrazioni**

[Diagramma di flusso: "Ricevo comunicazione da altra amministrazione" → "USC redige annotazione con CASO D'USO DI SERVIZIO" (L'Ufficiale di Stato Civile) → "ANPR genera una notifica per l'aggiornamento anagrafe (se necessario)" → Branch 1: "L'Ufficiale di Anagrafe: Usa la funzione 'NUOVI EVENTI' per aggiornare l'anagrafe locale e ANPR indicando gli estremi ID ATTO ANSC". Branch 2: "L'Ufficiale di Anagrafe: Usa la funzione CONFERMA EVENTI STATO CIVILE per aggiornare l'anagrafe locale e ANPR indicando gli estremi ID ATTO ANSC". Branch aggiuntivo: "USC dà comunicazione dell'avvenuta annotazione"]