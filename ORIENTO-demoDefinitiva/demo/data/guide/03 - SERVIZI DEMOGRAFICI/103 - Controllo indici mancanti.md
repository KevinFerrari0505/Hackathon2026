# Controllo indici mancanti

Il programma permette il controllo degli atti mancanti per creare gli indici.

Inoltre, lanciando questo programma verrà scaricato un file Excel dove vengono riportati vari messaggi.

Ecco alcuni esempi di messaggi che **POTREBBERO** essere riportati:

1. **Atto mancante fra il numero 1 e 3;**
2. **Manca il sesso all'interno dell'atto;**
3. **Manca il cognome/nome all'interno dell'atto;**
4. **Numero di atto presente 2 volte.**

Lanciando appunto tale programma, si viene a conoscenza di tutte le eventuali incongruenze presenti all'interno degli atti di Stato civile così da poterle andare a correggere prima della stampa.

## Percorso di accesso

Il percorso da seguire è:

**Servizi demografici ⇒ Stato civile ⇒ Altre operazioni ⇒ Stampa indici ⇒ Controllo indici mancanti**

[Schermata del menu di navigazione: Servizi demografici → Stato civile → Altre operazioni → Stampa indici → Controllo indici mancanti]

## Parametri di esecuzione

Si ha la possibilità di lanciare tale programma relativo a più anni.

Se, ad esempio, volessi fare un controllo dal 2022 ⇒ Su **"Anno da"** metterò **"2022"** mentre su **"A"** inserirò **"2023"**.

Inoltre è possibile estrapolare le incongruenze per **tutti gli atti** oppure solo per un **determinato tipo di atto**, per **"Delegazione"** oppure per **"Parte"** e **"Serie"**.

[Schermata del pannello di controllo: campo "Anno da" (2022), campo "A" (2023), checkbox "Tipo Atto" con opzioni Cittadinanza, Nascita, Matrimonio, Morte, Unione Civile, e pulsante "Esporta Excel"]

## Esportazione Excel

Cliccando sull'apposito pulsante **"Esporta Excel"**, verrà generato un file come nell'esempio sotto riportato.

Il file si divide in due pagine:

- **Riepilogo**;
- **Progressivi**.

### Pagina "Riepilogo"

Nella prima pagina **"Riepilogo"**, vengono riportati i messaggi di incongruenze (*come gli esempi riportati ad inizio guida*).

[Schermata del foglio Excel "RIEPILOGO" con colonne: Cognome, Nome, Progressivo, Anno, Tipo Atto, Parte, Serie, Numen, Delegazione, Messaggio. Esempi di messaggi: "Atto mancante fra il numero 1 e 3", "Manca sesso o cognome o nome", "Atto mancante fra il numero 5 e 7", ecc.]

### Pagina "Progressivi"

Mentre, nella seconda pagina **"Progressivi"**, vengono indicati quali sono gli ultimi progressivi movimentati per tipo di **Atto**, **Parte** e **Serie**.

[Schermata del foglio Excel "PROGRESSIVI" con colonne: Tipo Atto, Anno, Delegazione, Parte, Serie, Ultimo numero utilizzato. Esempi: Nascita 2023 / Delegazione 1 / Parte 1 / Serie A / Ultimo 20; Matrimonio 2023 / Parte 2 / Serie C / Ultimo 12; Morte 2023 / Parte 2 / Serie B / Ultimo 3; Cittadinanza 2023 / Parte 1 / Serie 19; Unione Civile 2023 / Parte 1 / Serie 2 / Ultimo 1]