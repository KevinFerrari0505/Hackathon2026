# Gestione soggetti ricercati su ANPR

È stata migliorata la gestione dei soggetti residenti e non residenti integrata nell'atto. Durante la stesura dell'atto, quando si ricerca un soggetto da ANPR, è stata aggiunta la form intermedia di gestione dei soggetti nell'archivio unico posizionata su **Dati Nascita** per permettere all'USC di gestire i dati nel caso in cui non fossero corretti o debbano essere implementati.

La ricerca deve essere effettuata inserendo come dati minimi **COGNOME** e **NOME**.
Per maggiore precisione consigliamo di indicare sempre anche la data di nascita del soggetto.

Si possono presentare principalmente quattro casistiche:

---

## ESEMPIO 1 – Soggetto residente nel comune

Basta un doppio click per selezionare la persona.

[Schermata: finestra "Interrogazione Soggetti in ANPR" con elenco di soggetti. La colonna "IN ANPR" mostra lo stato di residenza (es. "Residente CECINA (LI)", "Residente FANICALE (PG)", ecc.) e la colonna "IN CITYWARE" mostra "//" per i residenti. Il soggetto selezionato (evidenziato in giallo) mostra nella colonna "IN CITYWARE" la dicitura "Residente nella nascita". Pannello di navigazione a destra con pulsanti: F2 - Altra Ricerca, Nuovo, Gestione Soggetto.]

---

## ESEMPIO 2 – Soggetto Non Residente

In Locale/Cityware si trova la dicitura **Non residente**. Con il doppio click in automatico verrà aperta la schermata della gestione soggetti non residenti per verificare i dati di nascita, di residenza, ecc.

[Schermata: finestra "Interrogazione Soggetti in ANPR" con elenco di soggetti. La colonna "IN ANPR" mostra stati come "Residente AREZZO (AR)", "Residente POTENZA PICENA (MC)", ecc. La colonna "IN CITYWARE" mostra "Non residente" (evidenziato in rosso) per il soggetto selezionato. Pannello di navigazione a destra con pulsanti: F2 - Altra Ricerca, Nuovo, Gestione Soggetto.]

Se i dati **CORRISPONDONO** è sufficiente premere **AGGIORNA**.
Se invece non corrispondono con quanto contenuto nei documenti è possibile modificarli e con il tasto **Aggiorna** verranno utilizzati tali dati per redigere l'atto.

[Schermata: finestra "Anagrafico Soggetti" con campi: Persona (Fisica), Matricola, Cognome (MEDICI), Nome (MATTEO), Sesso (Maschio), Ditta indiv., Ragione Sociale (MEDICI MATTEO). Tab attivi: Soggetto, Residenza, **Nascita** (selezionato). Sezione "Atto Originale" con campi: Luogo (CERNUSCO SUL NAVIGLIO (MI)), Num., Parte, Serie, Delegaz., Volume, Anno (2013), Paternità (MEDICI ANTONIO), Maternità (DIOMEDE ROBERTA). Sezione "Atto Trascritto" con campi vuoti. Pulsanti a destra: **Aggiorna** (evidenziato in rosso), Torna Elenco, Uffici FE, Dutc, Allegati, Depositi, Anagrafe.]

---

## ESEMPIO 3 – Soggetto inesistente nell'archivio unico soggetti

In Locale/Cityware si trovano due barre `//`. Con il doppio click il programma crea il soggetto nell'archivio unico dei soggetti con i dati reperiti da ANPR. **In questa fase**, è possibile prima premere il tasto **Gestione Soggetto** per verificare se i dati sono coincidenti con i documenti in possesso dell'USC e come nell'esempio precedente, se i dati corrispondono, è sufficiente premere **Aggiorna**; altrimenti, se non corrispondono, è possibile modificarli e con il tasto **Aggiorna** verranno utilizzati tali dati per redigere l'atto.

[Schermata: finestra "Interrogazione Soggetti in ANPR" con elenco di soggetti. La colonna "IN ANPR" mostra "Residente STRANGOLAGALLI (FR)" per il soggetto selezionato (evidenziato in giallo). La colonna "IN CITYWARE" mostra "//" (evidenziato in rosso). Pannello di navigazione a destra con pulsante **Gestione Soggetto** evidenziato in rosso.]

---

## ESEMPIO 4 – Soggetto inesistente in ANPR

Caso di straniero residente all'estero. In questo caso se il soggetto è inesistente con il tasto **Nuovo** è possibile inserire i dati direttamente in questa fase per poi essere usati all'interno dell'atto.

[Schermata: finestra "Interrogazione Soggetti in ANPR" con elenco di soggetti. La colonna "IN ANPR" mostra "Residente AREZZO (AR)", "Residente POTENZA PICENA (MC)", ecc. La colonna "IN CITYWARE" mostra "//" per i soggetti senza corrispondenza locale. Pannello di navigazione a destra con pulsante **Nuovo** evidenziato in rosso.]