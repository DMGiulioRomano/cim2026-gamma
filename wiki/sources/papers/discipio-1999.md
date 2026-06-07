# [Di Scipio, 1999] Synthesis of Environmental Sound Textures by Iterated Nonlinear Functions

## Citazione CIM
Di Scipio, A. (1999). Synthesis of Environmental Sound Textures by Iterated Nonlinear Functions. *Proceedings of the 2nd COST G-6 Workshop on Digital Audio Effects (DAFx99)*, NTNU, Trondheim, December 9–11, pp. 1–6.

## Argomento centrale
Formalizzazione della Functional Iteration Synthesis (FIS): framework generale in cui l'output di una funzione non lineare (prototipo: mappa del seno, `x_{n,i} = sin(r * x_{n-1,i})`) viene reiterato come input della stessa funzione, producendo segnale audio direttamente. I parametri r (scaling) e x_0 (valore iniziale) determinano la morfologia sonora: da oscillazioni regolari a rumore a banda stretta articolato. Applicazione principale: sintesi di texture ambientali (pioggia, temporale, turbolenza acustica).

## Gap o problema identificato
La non-integrabilità del sistema impedisce previsione analitica dei risultati: l'esplorazione empirica dello spazio dei parametri è necessaria. La relazione fra parametri fisici (r, x_0, n iterazioni) e percezione è qualitativa e non formalizzabile a priori.

## Rilevanza diretta per Gamma
Il meccanismo FIS con mappa del seno è esattamente il NonlinearFunc di GAMMA (vedi [mappa-logistica](../../concepts/mappa-logistica.md)). Gamma usa la stessa struttura iterativa ma come generatore di parametri di alto livello (valori ritmici) piuttosto che di campioni audio direttamente: l'iterazione opera sulla partitura, non sul segnale.

## Collegamento alla tesi centrale
Paper intermedio nella genealogia FIS di Di Scipio: formalizza il framework che nel 2001 diventerà articolo su Leonardo. Per la tesi Gamma: utile per distinguere l'uso che Gamma fa della non-linearità (livello parametrico-compositivo, mediato da DSL) dall'uso diretto di sintesi FIS (livello segnale). La differenza di scala dell'iterazione — campione vs. partitura — è un punto argomentativo centrale.

## Sezioni del paper CIM 2026 dove citare
- Related work (FIS come precursore, distinzione scala campione vs. scala parametrica)
- Architettura (confronto con NonlinearFunc di GAMMA)

## Quote chiave
- "I should stress that the crucial point here is more with the process of iteration than the function itself. As Mitchell Feigenbaum observed, '[…] precisely because the same operation is reapplied [...] self-consistent patterns might emerge where the consistency is determined by the key notion of iteration and not by the particular function performing the iterates'." (p. 1)
- "The exploration of the phase space, and the exploration of the parameter space as an ideal (but far from obvious) mapping of the perceptual space in the audible effects, should be left to interactive experiments." (p. 4)
