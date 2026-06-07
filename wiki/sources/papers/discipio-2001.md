# [Di Scipio, 2001] Iterated Nonlinear Functions as a Sound-Generating Engine

## Citazione CIM
Di Scipio, A. (2001). Iterated Nonlinear Functions as a Sound-Generating Engine. *Leonardo*, 34(3), pp. 249–254. MIT Press / JSTOR stable URL: http://www.jstor.org/stable/1576944

## Argomento centrale
Versione estesa e più matura del framework FIS (Functional Iteration Synthesis), presentato come approccio compositivo fondato sull'esplorazione dello spazio delle fasi di funzioni non lineari iterate. Il paper enfatizza l'attitudine empirica necessaria: impossibilità di controllo analitico → esplorazione come metodo compositivo. Discussione su: matematica FIS, modello sine map, esplorazione spazio delle fasi, implementazione real-time (Kyma), issues di implementazione, progetto *Sound & Fury*.

## Gap o problema identificato
L'implementazione in tempo reale richiede soluzioni ad hoc (due loop annidati: sample loop + iteration subloop); la non-integrabilità rende impossibile separare r, x_0 e n senza side effects sull'output. Non esiste caratterizzazione quantitativa del legame parametri↔percezione.

## Rilevanza diretta per Gamma
Paper più citabile della serie Di Scipio per il paper CIM 2026: rivista peer-reviewed (Leonardo/MIT Press), versione consolidata del framework. Gamma usa la stessa struttura matematica FIS (iterate di funzione non lineare come generatore) ma a scala temporale diversa: non il campione ma il parametro compositivo (valore ritmico). L'iterazione in Gamma produce la partitura; in FIS produce il segnale.

## Collegamento alla tesi centrale
Questo paper permette di posizionare Gamma rispetto al precursore più diretto e più citato. L'argomento centrale della tesi — che Gamma estende la logica iterativa non lineare al livello della partitura parametrica mediata da DSL, aggiungendo il layer di partitura grafica come strumento compositivo — si costruisce in contrasto/continuità con questo paper. La distinzione scala campione / scala partitura è il cardine.

## Sezioni del paper CIM 2026 dove citare
- Introduzione (collocazione genealogica)
- Related work (precursore FIS principale)
- Architettura (confronto scala iterazione: campione vs. parametro)
- Conclusioni (postura ecologica della composizione, citazione "no knowledge without chaos")

## Quote chiave
- "The idea was that both the micro- and the macro-level of music would emerge from a hidden, low-level chaotic dynamics." (p. 249)
- "Using iterated nonlinear functions as a sound generating engine, one has to learn the sonorous possibilities and the musicality hidden in the process and finally liberate its aesthetic potential. The most appropriate strategy becomes one of an empirical investigation of the parameters in play." (p. 251)
- Abstract: "The required method of this exploration is interactive computer music systems. Some examples are discussed bearing on the author's compositional experience with his *Sound & Fury* project. The approach is described in terms of chaotic but structured flow of sonic information. The relevance of an 'ecological' view of composing is emphasized." (p. 249)
