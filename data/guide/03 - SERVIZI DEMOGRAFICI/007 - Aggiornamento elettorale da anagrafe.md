# Aggiornamento elettorale da anagrafe

Dal menù **Servizi Demografici → Elettorale → Manutenzione → Variazioni ExtraRevisione → Aggiornamento elettorale da anagrafe** è possibile aggiornare i dati elettorali in modo massivo basandosi sui dati registrati in anagrafe.

> ⚠️ **ATTENZIONE:** Questo programma deve essere utilizzato solo se non si hanno revisioni dinamiche in corso.

Il programma di aggiornamento massivo dei dati elettorali da anagrafe serve per aggiornare principalmente i dati legati ad una variazione indirizzo italiano o estero che non comporti un cambio di sezione (campi proposti di default). È possibile allineare anche i dati di:

- Professione
- Titolo di studio
- Stato civile e nome coniuge (solo per femmine)
- Nominativo
- Luogo e data di nascita
- Atto di nascita

Il programma deve essere utilizzato **prima di ogni revisione dinamica** per avere sempre i dati aggiornati legati all'indirizzo italiano e estero degli elettori. Va anche usato sempre **prima di creare l'archivio AIRE per elezioni** per gestire le operazioni di voto dei residenti esteri.

---

## Stampa di controllo: per verifica dei dati da aggiornare

Come primo passaggio occorre selezionare i dati che si vuole aggiornare tra quelli proposti. Di default sono già spuntati i dati di variazione indirizzo italiano e estero.

Potete scegliere quali dati aggiornare; noi vi consigliamo il seguente:

[Schermata del programma "Aggiorna Elettorale da Anagrafe" con il seguente pannello di selezione:

- **Tipo Lista:** `1 - Liste Elettorali`
- **Segnala le differenze tra Anagrafe e Elettorale per:**
  - ☑ Variazione indirizzo italiano
  - ☑ Variazione indirizzo estero
  - ☐ Professione
  - ☐ Titolo di studio
  - ☐ Stato Civile e nome coniuge (solo per femmine)
  - ☐ Nominativo
  - ☑ Luogo e data di Nascita
  - ☑ Atto di Nascita
- ☑ Considera civico interno
- ☐ Creazione Archivio
- ☐ Stampare estratti
- ☐ variare elettore solo se non cambiata sezione

In alto è presente un banner di ATTENZIONE: *"Non eseguire questo programma durante una revisione dinamica: l'aggiornamento effettivo potrebbe essere sovrascritto dalla revisione..."]

Dopo di che si può spuntare anche la **Stampa estratti** e premendo **OK** verrà generato un report che va verificato, quindi controllato. Il report vi proporrà per ogni nominativo le variazioni che farà, per esempio per l'indirizzo indicherà il dato precedente (**da**) e il dato che imposterà dopo aggiornamento (**a**):

[Schermata del report di controllo con colonne: Fascicolo, Nominativo, Sesso, Data Nascita, Dato Variato. Esempio di riga: Fascicolo 40242, Sesso M, Data Nascita 04/06/2000, Dato Variato: "Variato indirizzo italiano — da VIA [cancellato] n. 126 → a CONTRADA [cancellato] n. 12"]

> ⚠️ **ATTENZIONE:** accertarsi che in questa fase di controllo **NON** sia spuntata la creazione archivio.

Per lanciare la stampa di controllo scegliete i dati che volete aggiornare e poi cliccate su **OK** in alto a destra per lanciare l'elaborazione e controllarla.

[Schermata del programma con il pulsante **OK** evidenziato in alto a destra e la casella **Stampa estratti** spuntata (evidenziata in rosso)]

---

## Aggiornamento massivo dell'archivio elettorale

Dopo aver verificato il report con i nominativi che sono stati proposti per l'aggiornamento è possibile salvare i dati nell'elettorale spuntando **Creazione archivio** e premendo **OK**.

> ⚠️ **ATTENZIONE:** questa operazione è **irreversibile**.

[Schermata del programma con la casella **Creazione Archivio** spuntata (evidenziata in rosso) e il pulsante **OK** evidenziato in alto a destra. Le altre caselle di selezione dati rimangono come nella fase di controllo.]