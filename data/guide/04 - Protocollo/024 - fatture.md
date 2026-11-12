# Protocollare una Fattura Elettronica in arrivo

Per protocollare una fattura in arrivo, si procede normalmente seguendo la **protocollazione delle mail**.

Nell'elenco delle mail, la fattura è riconoscibile dal simbolo dell'euro €.

[Schermata: Elenco mail da protocollare con colonna "Certificazione" che mostra il simbolo € accanto alle fatture elettroniche in arrivo, con colonne Oggetto, Data, Ora, Giorni, Mittente, Mittente Originale, Account]

La fattura in questione è in realtà un **flusso**, che può contenere all'interno più fatture.

L'oggetto è compilato automaticamente e riporta il numero del lotto, il nome del fornitore e il codice destinatario; se precedentemente configurato, anche i campi **titolario** e **assegnatari interni** risulteranno già compilati.

In corrispondenza della voce *Termine* sarà inserita automaticamente anche la data di scadenza di **15 giorni**.

[Schermata: Tabella "Trasmissioni Interne" con campi Assegnatario, Ufficio, Settore e tabella con colonne Descrizione, Gest. Resp., Originale, Termine, Mail, Acc., Cons., Not. Pec, Invio mail. Esempio: Servizio Ragioneria / CHIARA COGNIGNI con termine 12/01/2019]

Nella tabella degli allegati, la fattura è già presente e, dopo aver registrato il protocollo, può essere visualizzata cliccando sul simbolo dell'euro.

[Schermata: Tabella Allegati con colonne Nome File, Descrizione, Tipo, Data. Esempio: file .xml con simbolo €, file daticert.xml e smime.p7s di tipo ALLEGATO]

---

## Spacchettamento del flusso

Dopo aver protocollato il flusso, il programma lo spacchetterà e protocollerà automaticamente ogni singola fattura contenuta; l'utente protocollatore delle fatture spacchettate risulterà lo stesso utente che ha registrato il flusso. Le fatture spacchettate saranno quindi visibili e accessibili nel suo portlet **Accesso ai protocolli**.

---

## Tipi di documento (campo *Tipo Doc.*)

Il tipo di fattura è riconoscibile dal campo **Tipo Doc.** nella schermata di protocollazione.

| Sigla | Descrizione |
|-------|-------------|
| **EFAA** | Fattura Elettronica in Arrivo (flusso in arrivo) |
| **EFAS** | Fattura Elettronica Spacchettata |
| **SDIA** | Notifica di interscambio in arrivo |

La sigla **SDIA** indica una notifica; il tipo di notifica (Ricevuta di consegna, Notifica decorrenza termini, ecc.) è poi specificata automaticamente nel campo oggetto.

---

## Notifiche di decorrenza termini

Attraverso uno specifico **parametro**, è possibile attivare l'associazione automatica delle **notifiche di decorrenza termini** alle relative fatture.

In questo modo, non saranno visibili nell'elenco delle mail in arrivo, né sarà mostrato alcun avviso. Si potranno però vedere andando a riaprire il protocollo e controllare gli **Allegati di Servizio**.

[Schermata: Tabella Allegati con pulsante "VEDI ALLEGATI DI SERVIZIO" in evidenza]

---

## Visualizzazione della fattura protocollata

La fattura così protocollata è ora visibile sul portlet **Protocolli in Carico** dell'utente che dovrà gestire la fattura elettronica.