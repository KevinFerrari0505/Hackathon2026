# Creare e gestire un calendario

## Creazione preliminare del gruppo

Un utente amministratore dovrà creare il gruppo che condividerà lo stesso calendario.

Dal menù principale **Amministrazione del Sistema** → **Gestione Accessi** → **Gruppi**.

Cliccare **Nuovo** per aggiungere un nuovo calendario.

[Schermata: Gestione Gruppi con campi Codice e Descrizione, pulsante F2-Nuovo evidenziato]

Inserire un *codice numerico* e una *descrizione* del gruppo. Cliccare **Aggiungi** per crearlo.

[Schermata: Gestione Gruppi con Codice "99", Descrizione "ITALSOFT", pulsante F5-Aggiungi evidenziato]

Dalle impostazioni scegliere **Permessi menù**.

[Schermata: Pannello di Controllo con icone: Gestisci il tuo Profilo, Firma un Documento, Permessi menù (evidenziato), Gestione Portlet, Verifica un Documento, Gestione Parametri, Gestione parametri sessione, Poste Comunicazioni Elettroniche, Elenco Report, Cambia Password, Test Programmi]

Alla voce **Gruppo** selezionare il gruppo appena creato.

[Schermata: Parametri Menù con dropdown Gruppo aperto che mostra le opzioni: ITALSOFT, PROVA, NO AGGIUNTA MITT DEST, SVILUPPO CDS, PROVA]

Alla voce **Root** selezionare **Menu principale ItaEngine (TI_MEN)**.

[Schermata: Parametri Menù con dropdown Root aperto che mostra: Certificazione anagrafe (KIOSK_MEN), Menu Mobile (MOB_MEN), Menu principale (VAL_MEN), Menu dei portlet (PT_MEN), Menu principale ItaEngine (TI_MEN) evidenziato]

Alla voce **Applicativo** selezionare **Menu Principale**.

[Schermata: Parametri Menù con dropdown Applicativo aperto che mostra: Menu Principale, Gestione Documentale, Protocollo, Rassegna Stampa, Fascicoli Elettronici]

Chiudere tutte le voci del menù, impostando **Nega**.

[Schermata: Parametri Menù con tabella "Menu principale ItaEngine" che elenca le voci (Gestione Documentale, Protocollo, Rassegna Stampa, Fascicoli Elettronici, ecc.) con colonne Visualizza, Accesso, Inserimento, Modifica, Cancella. Alcune voci impostate su "Consenti", altre su "Nega"]

Associare ad ogni utente che utilizzerà quel calendario il gruppo creato precedentemente.

Dal menu principale → **Amministrazione del Sistema** → **Gestione Accessi** → **Utenti** e aprire il profilo dell'utente.

[Schermata: Gestione Utenti con campi Loginame utente, Codice fiscale, Gruppo utente, pulsanti F2-Nuovo e F4-Elenco]

Spostarsi nella tab **Gruppi** e aggiungere il gruppo creato per il calendario. Cliccare **Aggiorna** per salvare l'aggiunta.

[Schermata: Gestione Utenti - tab Gruppi attiva, con campo "Codice Gruppo 01" valorizzato con "ITALSOFT", pulsanti F5-Aggiorna, F7-Cancella, F8-Torna Elenco, F3-Altra Ricerca, Duplica]

## Impostazione del calendario

Per impostare il calendario nella propria *Home*, andare nelle impostazioni e selezionare **Gestione Portlet**.

Trovare la voce **Gestione Calendario** nell'elenco e cliccare il **+ verde**.

[Schermata: Gestione desktop utente - Visualizza Portlet con elenco: Dashboard CDS, Scadenza Punti, Gestione Calendario (+ verde evidenziato), Timbrature Online, Passi Fascicolo da prendere in carico, Visualizza Fascicoli per Utente, Visualizza Richieste Accesso Utenti, Controllo Orologi, Notifiche Anpr]

Cliccare **Portlet** per impostare il calendario nella Home oppure **App** se si preferisce visualizzare il calendario in una scheda parallela.

## Creazione di un calendario

Prima di poter inserire un nuovo evento, bisogna creare (**solo la prima volta**) un proprio calendario accessibile al gruppo. Cliccare l'ingranaggio.

[Schermata: Vista Calendario mensile (luglio 2019) con pulsanti Oggi, Nuovo, ingranaggio (evidenziato), e viste Mese/Settimana/Sett. Agenda/Attività/Scadenze]

Cliccare **Nuovo**.

[Schermata: Impostazioni Calendario - Selezione calendari con colonne Nome calendario, Proprietario, Perm. grupp, Perm. altri, Colore. Pulsante F2-Nuovo evidenziato]

Assegnare un nome al calendario, poi scegliere il gruppo che sarà abilitato a visualizzarlo.

[Schermata: Impostazioni Calendario con campi: Nome Calendario* "CALENDARIO SERVIZIO X", Proprietario* "chiara", Gruppo* (dropdown con "ITALSOFT"), sezione Permessi Gruppo (Lettura, Inserimento/Modifica, Cancellazione), sezione Permessi Pubblico (Lettura, Inserimento/Modifica, Cancellazione), pulsante Privato, pulsanti F3-Aggiungi e F8-Torna]

In **Permessi Gruppo** spuntare *Lettura*, *Inserimento/Modifica* e/o *Cancellazione* in base ai permessi che si vogliono dare agli altri componenti del gruppo.

In **Permessi Pubblico** spuntare le stesse voci solo se si vuole rendere pubblico il calendario a tutto l'ente.

Il tasto **Privato** serve solamente a togliere le spunte inserite.

## Inserimento di un nuovo evento

Una volta creato il calendario, si possono inserire gli eventi. Cliccare **Nuovo**.

[Schermata: Vista Calendario mensile con pulsante Nuovo evidenziato]

Scegliere il calendario appena creato e inserire l'evento nel campo *Titolo*. È possibile aggiungere anche una descrizione più estesa nella tabella *Descrizione*.

I campi obbligatori sono esclusivamente quelli indicati con l'asterisco rosso.

[Schermata: Finestra Evento con campi: Calendario* "CALENDARIO SERVIZIO X", Classificazione (dropdown), Titolo*, Descrizione (editor di testo con formattazione), sezione Date Evento (Data inizio* "15/07/2019" e ora "16:00", Data fine, Tutto il giorno), sezione Ricorsività (Ripeti Evento, ogni mesi, Fino al), sezione Promemoria (Attiva, Tipo "Notifica", Tempo "30", Unità "Minuti", prima), pulsante F5-Salva]

Inserire la **data dell'evento**, scegliendolo dal calendario o scrivendolo liberamente nel campo data, e specificare l'orario di inizio.

È possibile inserire anche una data fine, per gli eventi che si prolungano oltre la giornata, oppure spuntare la voce **Tutto il giorno**.

[Schermata: Sezione Date Evento con Data inizio* "15/07/2019" e ora "16:00", Data fine vuoto, Tutto il giorno (checkbox evidenziata) "(data fine esclusa)"]

Per gli eventi che si ripetono regolarmente, spuntare la voce **Ripeti Evento** e scegliere l'intervallo di tempo in mesi. È possibile impostare anche una data fine.

[Schermata: Sezione Ricorsività con dropdown "ogni mesi" aperto che mostra valori da 01 a 12]

Se per quell'evento si vuole mandare un **promemoria** al proprietario del calendario, spuntare la voce **Attiva** e scegliere il tipo di promemoria:

- **notifica**, per visualizzarla negli avvisi
- **email**, per inviare una mail all'indirizzo indicato nell'archivio Mittenti/Destinatari (se presente);
- **pop-up**, per ricevere una comunicazione a comparsa nel protocollo.

[Schermata: Sezione Promemoria con Attiva (checkbox), Tipo (dropdown aperto con opzioni: Notifica, Email, Pop-Up), Tempo "30", Unità (dropdown aperto con opzioni: Minuti, Ore, Giorni, Settimane, Mesi), "prima"]

Infine impostare quanto tempo prima dell'evento deve essere inviato il promemoria.

## Visualizzazione degli eventi

Per poter visualizzare gli eventi inseriti dagli utenti del proprio gruppo, bisogna attivare il loro calendario (**solo la prima volta**). Cliccare l'ingranaggio.

[Schermata: Vista Calendario con ingranaggio evidenziato]

Dall'elenco dei calendari presenti, spuntare quelli che si vogliono visualizzare.

[Schermata: Impostazioni Calendario - Selezione calendari con elenco: Calendario di ALEX (ALEX), Calendario Applicativi ANTIMO (ANTIMO), ANTIMO, Calendario di andrea (andrea), sssssssss (andrea), Calendario di Carlo (carlo), CALENDARIO SERVIZIO X (chiara, evidenziato con spunta), Calendario di michele (michele), Calendario Applicativi paolo (paolo), Calendario di paolo (paolo). Colonne: Nome calendario, Proprietario, Perm. grupp, Perm. altri, Colore]

A questo punto, gli eventi inseriti dal proprio gruppo saranno visibili nel calendario.

[Schermata: Vista Calendario mensile (luglio 2019) con eventi visibili nelle celle dei giorni, tooltip che mostra dettagli di un evento: "Calendario Applicativi paolo, 14/06/2019 - 09:00, Scadenza Richiesta Pareri, Atto: Determina, Numero: 4000069 del 2019, Data: 31/01/2019, Oggetto: AMBITO TERRITORIALE SOCIALE 14..."]