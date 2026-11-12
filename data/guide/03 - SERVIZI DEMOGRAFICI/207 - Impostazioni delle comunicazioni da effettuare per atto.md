# Impostazioni delle comunicazioni da effettuare per atto

Questo programma permette di associare dei testi DOCX agli atti in modo da poterli selezionare alla conferma di un Atto di Stato civile. La funzione in oggetto è accessibile attraverso il seguente percorso:

**Servizi Demografici; Stato Civile; Tabelle; Personalizzazioni; Comunicazioni da effettuare per atto**

## Composizione della tabella

Al primo accesso al programma vi verranno proposte tutte le comunicazioni che al momento sono inserite come stampabili alla conferma di un atto di Stato Civile; la tabella che avete davanti è così composta:

- dati identificativi del tipo di atto (tipo, parte e serie)
- descrizione del testo che viene proposto in stampa
- causale di stato civile
- dati identificativi del testo (codice testo)
- identificativo della comunicazione (progressivo interno della tabella)

[Schermata: Tabella Comunicazioni da Atti con colonne Tipo Atto, Parte, Serie, Descrizione, Causale, Codice Testo, ID Com. Esempi di righe: Nascita / Comunicazione di nascita per ufficio Anagrafe_J / cwi_comunicazione_nascita / 518; Nascita / 1 / A / Attribuzione cittadinanza a bimbo straniero / cwi_attribuzioneCittadinanzaBimboStraniero / 528; Nascita / 1 / A / Comunicazione formaz.atto allo Sta.Civ. Comune di Nascita - rubrica / cwi_ComunicazioneAtto_aComuneNascita / 525; Nascita / 1 / A / Dichiarazione scelta del nome, convenzione di Monaco / cwi_dichiarazioneSceltaNomeMonaco / 527; Nascita / 1 / A / Trasmissione Atto Nascita al Comune di Residenza / cwi_comunicazioneNascitaComResidenza / 503; Nascita / 1 / A / Conferma avvenuta trascrizione nascita 2B a Direttore Sanitario / cwi_comunicazioneNascitaDirOspedale / 577; Nascita / 1 / A / Comunicazioe Nascita alla ASL / Atto di Nascita con iscrizione in famiglia / cwi_ComunicazioneNascitaASL / 578]

## Struttura delle comunicazioni per atto

Le comunicazioni stampabili alla conferma degli atti di stato civile sono associate agli Atti in base alla tipologia dell'atto (nascita, matrimonio…) alla parte (1,2) alla serie (A,B..) e la loro visualizzazione varia in base al tipo di associazione che viene impostata. Quindi associando un atto per la sola tipologia lo vedrò in stampa per tutti gli atti di quella tipologia; caratterizzando la parte, invece, la comunicazione sarebbe stampabile dagli atti per quella tipologia e parte.

Ecco un esempio:

- associando una comunicazione al solo tipo atto= Nascita, il testo sarà proposto e visibile in stampa per **tutti gli atti di nascita** senza quindi tenere conto della parte e della serie
- associando una comunicazione ad un tipo atto=nascita parte=1, il testo sarà proposto e visibile in stampa **per tutti gli atti di nascita in parte prima**, senza quindi tenere conto della serie
- associando una comunicazione ad un tipo atto=nascita parte=1 serie=A, il testo sarà proposto e visibile in stampa **per tutti gli atti di nascita in parte prima serie A**, non sarà proposto in stampa per gli atti di nascita parte=2 o per la serie B

## Cercare le comunicazioni stampabili per un determinato tipo di atto (tipo atto, parte, serie)

Tenuto conto di quanto sopraesposto, per ricercare le comunicazioni legate ad una classificazione, **quando siete nella videata principale** spostatevi a destra sul pulsante **altra ricerca** per cliccarlo.

Nella videata che vi mostriamo potrete ricercare le comunicazioni che vengono proposte in stampa secondo le classificazioni esposte prima (tipo atto, parte, serie); vediamo ora alcuni esempi pratici:

### Esempio associazione al solo tipo atto

ricercando per tipo atto= Atto di nascita saranno visualizzate tutte le comunicazioni associate a quel tipo di atto:

[Schermata: Videata di ricerca con campo "Tipo Atto" impostato su "1 - Nascita" (evidenziato in rosso), campi "Parte Atto" e "Serie Atto" vuoti, campo "Codice Testo" vuoto, campo "Causale Variazione" con valori 0 0 0]

questo perché associando una comunicazione al solo tipo atto= Nascita, il testo sarà proposto e visibile in stampa per **tutti gli atti di nascita** senza quindi tenere conto della parte e della serie

[Schermata: Risultati ricerca "Tabella Comunicazioni da Atti" con colonne Tipo Atto, Parte, Serie, Descrizione. Tutte le righe mostrano "Nascita" come Tipo Atto, con diverse combinazioni di Parte (vuoto, 1, 2) e Serie (vuoto, A, B). Esempi: Nascita / (vuoto) / (vuoto) / Comunicazione di nascita per ufficio Anagrafe_J; Nascita / 1 / A / Conferma avvenuta trascrizione nascita 2B a Direttore Sanitario; Nascita / 1 / A / Trasmissione Atto Nascita al Comune di Residenza; Nascita / 1 / A / Comunicazione formaz.atto allo Sta.Civ. Comune di Nascita; Nascita / 1 / A / Dichiarazione scelta del nome, convenzione di Monaco; Nascita / 1 / A / Attribuzione cittadinanza a bimbo straniero; Nascita / 1 / A / Comunicazioe Nascita alla ASL; Nascita / 1 / B / Trasmissione Atto Nascita al Comune di Residenza; Nascita / 1 / B / Comunicazione alla Procura - Nascita tardiva_K; Nascita / 2 / A / Comunicazione di nascita per ufficio Anagrafe_J; Nascita / 2 / A / Conferma avvenuta trascrizione al Comune atto originale; Nascita / 2 / B / Assicurata trascrizione nascita 2B a Consolato]

### Esempio associazione al tipo atto ed alla parte

ricercando per tipo atto= Atto di nascita e parte=2 saranno visualizzate tutte le comunicazioni associate a quel tipo di atto e quella parte, senza tenere conto della serie:

ricerchiamo per tipo atto=nascita e parte=2

[Schermata: Videata di ricerca con campo "Tipo Atto" impostato su "1 - Nascita" (evidenziato in rosso), campo "Parte Atto" impostato su "2" (evidenziato in rosso), campo "Serie Atto" vuoto, campo "Codice Testo" vuoto, campo "Causale Variazione" con valori 0 0 0]

[Schermata: Risultati ricerca "Tabella Comunicazioni da Atti" con colonne Tipo Atto, Parte, Serie, Descrizione. Tutte le righe mostrano "Nascita" come Tipo Atto e "2" come Parte, con Serie A o B. Esempi: Nascita / 2 / A / Conferma avvenuta trascrizione al Comune atto originale; Nascita / 2 / A / Comunicazione di nascita per ufficio Anagrafe_J; Nascita / 2 / B / Certificato di congruità solo per cambio cognome nome; Nascita / 2 / B / Conferma avvenuta trascrizione nascita 2B a Direttore Sanitario; Nascita / 2 / B / Comunicazione uff. Elettorale per Cambio Nominativo; Nascita / 2 / B / Certificato di congruità solo per cambio cognome nome; Nascita / 2 / B / Assicurata trascrizione nascita 2B a Consolato; Nascita / 2 / B / Comunicazioe Nascita alla ASL; Nascita / 2 / B / Comunicazione Nascita per Anagrafe di cambiamento Nome]

seguendo il ragionamento: associando una comunicazione ad un tipo atto=nascita parte=2, il testo sarà proposto e visibile in stampa **per tutti gli atti di nascita in parte seconda**, senza quindi tenere conto della serie

### Esempio associazione al tipo atto, alla parte ed alla serie

ricercando per tipo atto= Atto di nascita, parte=2 e serie=B saranno visualizzate tutte le comunicazioni associate a quel tipo di atto e quella parte e serie, escludendo quindi le comunicazione associate ad atti, parti e serie diverse da quelli impostati.

ricerchiamo per tipo atto=nascita parte=2 serie=B

[Schermata: Videata di ricerca con campo "Tipo Atto" impostato su "1 - Nascita", campo "Parte Atto" impostato su "2", campo "Serie Atto" impostato su "B", campo "Codice Testo" vuoto, campo "Causale Variazione" con valori 0 0 0]

[Schermata: Risultati ricerca "Tabella Comunicazioni da Atti" con colonne Tipo Atto, Parte, Serie, Descrizione. Tutte le righe mostrano "Nascita" come Tipo Atto, "2" come Parte e "B" come Serie. Esempi: Nascita / 2 / B / Comunicazione Nascita per Anagrafe di cambiamento Nome; Nascita / 2 / B / Certificato di congruità solo per cambio cognome nome; Nascita / 2 / B / Conferma avvenuta trascrizione nascita 2B a Direttore Sanitario; Nascita / 2 / B / Comunicazione uff. Elettorale per Cambio Nominativo; Nascita / 2 / B / Certificato di congruità solo per cambio cognome nome; Nascita / 2 / B / Assicurata trascrizione nascita 2B a Consolato; Nascita / 2 / B / Comunicazioe Nascita alla ASL]

seguendo il ragionamento: associando una comunicazione ad un tipo atto=nascita parte=2 serie=B, il testo sarà proposto e visibile in stampa **per tutti gli atti di nascita in parte seconda serie B**, senza quindi tenere conto delle parti e serie differenti.

## Impostare la stampa di una comunicazione al termine dell'atto

In riferimento agli esempi che sono stati visti per associare una comunicazione ad un atto e vederla poi proposta al termine dell'iter di redazione seguite i passi qua esposti:

1) premete sul pulsante **NUOVO** per inserire una nuova associazione Testo —> Atto

2) compilate il tipo atto, parte e serie per il quale volete che venga proposta in stampa la comunicazione (tenendo conto di quanto sopra spiegato se volete che la comunicazione venga proposta per tutti gli atti di una parte o di una serie)

3) scegliete il codice testo tra quelli proposti, è possibile anche associare dei testi personalizzati, che hanno come codice iniziale `codiceistatdeltuocomune_`

[Schermata: Videata "Dettaglio Comunicazioni da Atto" con campi: "Tipo Atto" (evidenziato in rosso, campo a tendina), checkbox "Da stampare?", "Codice Testo" (evidenziato in rosso, campo con lente di ricerca), "Causale Variazione" (con valori 0 0 0 e lente), "Uso Originale" (impostato su "0 - Tutti"), "Parte Atto" (evidenziato in rosso), "Serie Atto" (evidenziato in rosso), "CODICE UNITARIO" (valore 594)]

## Funzione RENDI MIO e comunicazioni per atto

Se trovate un testo che volete modificare e l'associazione al tipo di atto, parte e serie è corretta, potete utilizzare la funzione **RENDI MIO** per acquisire il testo, personalizzarlo e vederlo direttamente proposto in fase di stampa dell'atto.