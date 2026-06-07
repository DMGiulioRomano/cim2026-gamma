# [Di Scipio, 1990] Composition by Exploration of Non-Linear Dynamic Systems

## Citazione CIM
Di Scipio, A. (1990). Composition by Exploration of Non-Linear Dynamic Systems. *Proceedings of the International Computer Music Conference (ICMC)*, Glasgow, pp. 324–327.

## Argomento centrale
Resoconto compositivo del lavoro di Di Scipio con sistemi dinamici non lineari: la mappa logistica (e Henon, baker's transform) come generatore di struttura formale e di timbro, a scala macro (sequenza di eventi) e micro (sintesi granulare). Il segnale di output del sistema funge da indice in una tabella lookup che definisce il vocabolario sonoro.

## Gap o problema identificato
La procedura è ancora esplorativa e dipende fortemente dalla scelta dei parametri iniziali; non è possibile prevedere analiticamente il comportamento del sistema, solo esplorarlo empiricamente. La relazione fra struttura fisica del suono e suono percepito richiede calibrazione pratica.

## Rilevanza diretta per Gamma
Gamma eredita la stessa logica: un parametro (il ritmo) si autogenera via mappa logistica (lookup ricorsivo), e il suo output indicizza ulteriori parametri (altezza, ampiezza, spazio). La differenza è che in Gamma il meccanismo è integrato in un DSL YAML e il controllo avviene a livello di partitura parametrica, non di codice ad hoc.

## Collegamento alla tesi centrale
Questo paper è il fondamento storico-compositivo diretto. Di Scipio 1990 usa la non-linearità per articolazione formale e timbrica; Gamma usa lo stesso principio ma lo media attraverso un DSL che separa composizione e implementazione, aggiungendo un layer di partitura grafica come strumento decisionale. Il paper serve a posizionare Gamma nella genealogia di Di Scipio, non come mera applicazione tecnica.

## Sezioni del paper CIM 2026 dove citare
- Introduzione (genealogia compositiva)
- Related work (precursore diretto: mappa logistica come generatore musicale)
- Architettura (confronto meccanismo lookup)

## Quote chiave
- "In a series of compositions I have been experimenting with non-linear dynamic systems. The evolution of these systems is unpredictable, or analytically 'non-integrable', and shows alternatively both ordered structures and chaotic conditions." (p. 324)
- "Deterministic chaos procedures seem to be effective in resolving what I sensed a main musical problem: an unusual experiencing of time which could imply a dramatic suspension of the traditional 'logical continuity' wherever claimed for, in contemporary music composition." (p. 327)
- "However I do not propose a mere translation: no one actually listens to the sound of Henon's attractor! Once again purely formalized procedures are not in themselves composition; they only aid us in sensed motion throughout and within sound materials." (p. 327)
