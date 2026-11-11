# Aggiornamento elettorale da anagrafe

Dal menù **Servizi Demografici→Elettorale→Manutenzione→Variazioni ExtraRevisione→Aggiornamento elettorale da anagrafe** è possibile aggiornare i dati elettorali in modo massivo basandosi sui dati registrati in anagrafe.

> **ATTENZIONE:** Questo programma deve essere utilizzato solo se non si hanno revisioni dinamiche in corso.

Il programma di aggiornamento massivo dei dati elettorali da anagrafe serve per aggiornare principalmente i dati legati ad una variazione indirizzo italiano o estero che non comporti un cambio di sezione (campi proposti di default). È possibile allineare anche i dati di professione, titolo di studio, stato civile e nome coniuge (solo per femmine), nominativo, luogo e data di nascita, atto di nascita.

Il programma deve essere utilizzato prima di ogni revisione dinamica per avere sempre i dati aggiornati legati all'indirizzo italiano e estero degli elettori. Va anche usato sempre prima di creare l'archivio AIRE per elezioni per gestire le operazioni di voto dei residenti esteri (vedi: Creazione AIRE per Elezioni).

---

## Stampa di controllo: per verifica dei dati da aggiornare

Come primo passaggio occorre selezionare i dati che si vuole aggiornare tra quelli proposti. Di default sono già spuntati i dati di variazione indirizzo italiano e estero.

**Potete scegliere quali dati aggiornare**, noi vi consigliamo il seguente:

[Schermata del programma "Aggiorna Elettorale da Anagrafe" con i seguenti campi di selezione:
- **Tipo Lista:** 1 - Liste Elettorali
- **Segnala le differenze tra Anagrafe e Elettorale per:**
  - ☑ Variazione indirizzo italiano
  - ☑ Variazione indirizzo estero
  - ☐ Professione
  - ☐ Titolo di studio
  - ☐ Stato Civile e nome coniuge (solo per femmine)
  - ☑ Nominativo
  - ☑ Luogo e data di Nascita
  - ☑ Atto di Nascita
  - ☑ Considera civico interno
  - ☐ Creazione Archivio
  - ☑ Stampa estratti
  - ☐ variare elettore solo se non cambiata sezione]

Dopo di che si può spuntare anche la **Stampa estratti** e premendo **OK** verrà generato un report che va verificato, quindi controllato. Il report vi proporrà per ogni nominativo le variazioni che farà, per esempio per l'indirizzo indicherà il dato precedente (**da**) e il dato che imposterà dopo aggiornamento (**a**):

[Report di controllo con colonne: Fascicolo, Nominativo, Sesso, Data Nascita, Dato Variato. Esempio: Fascicolo 40242, Sesso M, Data Nascita 04/06/2000, Dato Variato: "Variato indirizzo italiano" — da: VIA ... n. 126 — a: CONTRADA ... n. 12]

> **ATTENZIONE:** accertarsi che in questa fase di controllo **NON** sia spuntata la creazione archivio.

Per lanciare la stampa di controllo scegliete i dati che volete aggiornare e poi cliccate su **OK** in alto a destra per lanciare l'elaborazione e **controllarla**.

---

## Aggiornamento massivo dell'archivio elettorale

Dopo aver verificato il report con i nominativi che sono stati proposti per l'aggiornamento è possibile salvare i dati nell'elettorale spuntando **Creazione archivio** e premendo **OK**.

> **ATTENZIONE:** questa operazione è **irreversibile**.

[Schermata del programma con "Creazione Archivio" spuntato (☑) e "Stampa estratti" spuntato (☑), pulsante OK evidenziato in alto a destra]