# Parametrizzazione Protocollo Remoto

## Parte SUAP (Esterno)

Per quanto riguarda il SUAP ci sono 3 punti da seguire per il corretto funzionamento il protocollo remoto:

1. Dal menu **Fascicoli Elettronici** → **Parametri** → **Dati ente** scegliere come tipo protocollo **Italsoft Remoto**

2. Dal menu **Fascicoli Elettronici** → **Parametri** → **Parametri Vari** Configurare i Modelli per la creazione dell'oggetto del protocollo.

3. Fare Click sull'ingranaggio in alto a destra e scegliere **Gestione Parametri** → **PARAMETRI PROTOCOLLAZIONE REMOTA ITALSOFT**. Inserire ora il link di dove si trova itaEngine nella macchina interna: (Es Loreto) `http://10.12.0.200/itaEngine/Start.php?accessorg=01`

4. Nella gestione degli utenti, una volta scelto l'utente desiderato, nel campo **Credenziali Protocollo Remoto** indicare il nome utente con il quale presentarsi al protocollo remoto. Ripetere l'operazione per gli utenti che si intendono abilitare.

5. Per far sì che nel protocollo vengano caricati correttamente gli uffici ed i destinatari, verificare:
   1. La presenza, nell'anagrafica dei mitt/dest, dei **soggetti interni** con i rispettivi uffici di appartenenza. Se non ci sono vanno caricati
   2. La presenza di uffici nella rispettiva anagrafica. Se non ci sono caricarli **Con lo stesso Codice con cui sono stati caricati nel Protocollo**
   3. Nell'archivio dipendenti del SUAP verificare che sia valorizzato il campo **Destinatario Protocollo**

6. Dal percorso **Fascicoli Elettronici** → **Parametri** → **Parametri Vari**, parametrizzare gli oggetti per Pratica, Comunicazione in Partenza, Comunicazione in Arrivo

## Parte PROTOCOLLO (Interno)

Per quanto riguarda il protocollo invece bisogna configurare solo alcune informazioni su dati ente.

1. Dal menu **Protocollo** → **Utilità** → **Dati ente** nel tab **Parametri Protocollazione SUAP** inserire login e password dell'utente che si collega al SUAP, il codice dell'ente corrispondente nel SUAP. Infine scrivere l'url di itaEngine nella macchina SUAP come segue: (Es) `http://193.254.241.22/itaEngine/ws/praWsFascicolo.php?wsdl`

2. Creare nella gestione utenti, un utente **nobody** password **nobody12**, creare un gruppo **nobody** e abbinarlo all'utente.

---

> **PS**
>
> Prima di protocollare accertarsi che entrambi i programmi (SUAP e Protocollo) e i web services siano aggiornati.