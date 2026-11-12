# Rilascio CIE con PagoPA

Prima di effettuare il rilascio del documento dal programma del Ministero, è necessario effettuare un'operazione di **Prenotazione Cie** da Cityware richiamabile da Menu **Servizi Demografici > Anagrafe > Variazioni > Gestione Carte d'Identità**.

L'operazione di **Prenotazione Cie** si occuperà di creare una posizione sul canale pagoPA, di pagare l'importo CIE tramite collegamento Pos e di registrare i diritti nell'applicativo Cityware.

## Prima di iniziare il procedimento, l'operatore dovrà accertarsi che:

- il Cittadino abbia tutto il materiale con sé
- il Cittadino possa pagare con bancomat
- il pos sia collegato al pc
- il programma del Ministero per il rilascio CIE sia funzionante.

## Procedura

Da **Gestione Carte d'Identità**, una volta selezionato il soggetto e fatto **Elenca**, se configurato il servizio, si attiverà sulla destra il pulsante **Prenotazione CIE pagoPA**.

Selezionare la prima riga presente nella griglia e cliccare **Prenotazione CIE pagoPA**. Si aprirà una videata che darà la possibilità di selezionare il tipo di documento e il canale di pagamento.

[Schermata: finestra "Prenotazione CIE con pagoPA" con campi "Tipo CIE" (selezionato: CIE) e "Modalità pagamento" (selezionato: PagoPA), pulsanti "Paga con pagoPA" e "Chiudi" sulla destra, e griglia sottostante con dati di audit]

Cliccando su **Paga con pagoPa**, la procedura salverà i diritti della Carta in Cityware e pubblicherà la posizione da pagare sul portale pagoPA. Quest'ultimo restituirà poi un codice univoco che servirà per procedere con il pagamento. L'utente vedrà a video l'apertura del browser con i dettagli del pagamento:

[Schermata: pagina web "Pagamento Nexi" con sezioni "Contribuente" (Codice Fiscale, Nominativo) e "Dati Pagamento" (Codice Identificativo, Numero Avviso, Codice Ente, Descrizione Servizio: CARTA DI IDENTITA, Descrizione Ente, Data Scadenza, Stato: Da pagare, Importo €), pulsanti "Annulla" e "Prosegui"]

Facendo **Prosegui** si attiverà la JVM che permetterà l'interazione con il pos per il pagamento. Non appena il pagamento potrà essere effettuato, il pos emetterà un bip, da quel momento si potrà far pagare l'utente. **Attenzione!** Questo passaggio deve essere fatto abbastanza velocemente perché la connessione al pos potrebbe andare in timeout.

Una volta che il pagamento è andato a buon fine, la pagina browser restituirà l'esito positivo del pagamento. A questo punto i diritti sono stati registrati correttamente su Cityware e può essere emessa la CIE come di consueto dal programma del Ministero.

## Riepilogo Diritti

Per poter verificare le CIE pagate tramite pagoPA è possibile fare il **Riepilogo Diritti Incassati** (da **Menu Sportello**) scegliendo come canale di pagamento **Rendicontazione Separata**.

[Schermata: finestra "Riepilogo diritti incassati" con campi Data emissione (da/a), Ora Emissione (da/a), Tipo Stampa (Dettagliato), Canale Pagamento (Rendicontazione separata), Tipo Emissione (Emessi allo sportello), Utente, sezione "Terminale che ha emesso il certificato" (Tutti / Lista terminali), sezione "Selezionare tipo Carta di identità/Doc. Riconoscimento" (Cartacce, CIE, Doc. Riconoscimento)]

## Pagamento non andato a buon fine

Nel caso il pagamento non abbia avuto esito positivo, il cittadino non aveva soldi sul conto, è necessario annullare il diritto emesso nella gestione diritti e procedere con un'altra prenotazione CIE scegliendo come metodo di pagamento **"CASSA"**, o provare un nuovo tentativo con PagoPA.

Di seguito come fare se il cittadino paga in **CONTANTI**:

1) Ricercate il diritto emesso nel programma **GESTIONE DIRITTI incassati** che trovate a questo percorso:

   **Servizi Demografici > Anagrafe > Sportello > Gestione diritti incassati**

   e selezionando il diritto e poi premendo il pulsante **annulla** sulla destra annullerete il diritto emesso con pago pa che non è stato realmente incassato.

[Schermata: griglia "Gestione Diritti Incassati" con colonne Data Emissione, Ora Emissione, Descrizione Servizio, Importo, Canale, Tipo Emissione, Numero Avviso, Utente, e pulsante "Annulla" evidenziato sulla destra]

2) Procedete ad una nuova prenotazione indicando come modalità di pagamento **"CASSA"** accedete al percorso:

   **Servizi Demografici > Anagrafe > Variazione > Gestione Carta Identità**

   premete sul pulsante **RILASCIO CIE**, compilate come segue e cliccate su **CONFERMA**

[Schermata: finestra "Emissione Nuova CIE" con dati del soggetto (Fam., Nome, Data nas., Matr., Comune, Residenza, C.F.), messaggio informativo in giallo, campi "Tipo CIE" (CIE) e "Modalità pagamento" (Cassa), pulsanti "Conferma" e "Chiudi"]

**OPPURE**, se il cittadino vuole ancora pagare con **PAGOPA**, sempre nella gestione delle carte di identità, cliccare sul pulsante **PRENOTAZIONE CIE PAGOPA** selezionando il metodo di pagamento come **PAGOPA**

[Schermata: finestra "Carte d'Identità" con griglia dei documenti e pulsanti sulla destra: Nuovo, Rilascio CIE, Prenotazione CIE pagoPA (evidenziato), Alta Ricerca, Aggiorna carta su ANPR]

## Pagamento effettuato, con esito positivo, ma CIE Online non funziona

Nel caso il pagamento vada a buon fine, viene incassato, ma CIE Online non risponde/non è funzionante occorre che vi segnate il nome del soggetto per il quale avete emesso la CIE e provvederemo noi a riagganciare il diritto di Cityware Online al relativo Pago PA.

Per contattare l'assistenza e dare informazione scrivere una mail a **citypeople@palitalsoft.it** descrivendo la situazione e lasciando i nomi dei soggetti in modo da poter intervenire.

Vanno rispettate le regole di base dell'apertura dei ticket quindi:

- indicare la problematica (immagini e dati aiutano la velocità nella comprensione del problema)
- recapito e fascia di reperibilità in caso di contatto telefonico
- dotarsi su una postazione pc di un teamviewer, anydesk o altro supporto per il collegamento remoto. Si consiglia anche **Iperius Remote**

## FAQ

**Tutti i browser sono compatibili con la procedura?**

No, non tutti i browser sono compatibili. Si consiglia l'uso di **Chrome**, da impostare sul pc come predefinito.

**Se si ha attivo pagoPA è possibile continuare a pagare con altri metodi di pagamento?**

Si, basta selezionare correttamente il *Metodo Pagamento* durante la procedura di prenotazione.

**E' possibile annullare la procedura di prenotazione CIE perché il programma del Ministero nel frattempo ha smesso di funzionare?**

Si, se l'utente non ha ancora pagato si può. Basta andare in **Gestione Diritti Incassati**, da **Menu Sportello**, selezionare la riga interessata, tasto destro **Annulla**. In questo modo verranno annullati i diritti registrati in Cityware e anche la posizione aperta su pagoPA.

**E' possibile Annullare un pagamento effettuato?**

No, non è possibile annullare un pagamento già effettuato.