# [Döbereiner, 2010] Model and Material: Composing Sound and the Construction of Compositional Models

## Citazione CIM
Döbereiner, L. (2010). *Model and Material: Composing Sound and the Construction of Compositional Models*. Master's Thesis, Institute of Sonology, Royal Conservatory, The Hague.

## Argomento centrale
La tesi articola la nozione di **compositionally motivated sound synthesis (CMSS)**: i metodi di sintesi "non-standard" (Koenig SSP, Brün SAWDUST, Xenakis Dynamic Stochastic Synthesis, Berg PILE) non modellano una sorgente o un ricevente acustico, ma costruiscono regole astratte in cui *il materiale sonoro stesso emerge nel processo compositivo*. Il modello di sintesi è simultaneamente modello di composizione, "una sorta di linguaggio macchina in cui il modello compositivo di alto livello viene compilato". Tesi di fondo: i modelli di sintesi operano all'intersezione fra **sensibile e intelligibile**, fra reale e simbolico, e vanno visti come *produttivi* anziché imitativi.

## Gap o problema identificato
Critica la visione positivista del modello (Smith 1991, Von Neumann/Morgenstern) per cui il modello è imitazione di una sorgente preesistente — "music can be said to be reduced to being the empirical proof of the model". Döbereiner oppone i modelli produttivi: la sintesi come atto compositivo (Brün: "composition *of* timbre, instead of *with* timbre"; Stockhausen: "Jeder Klang ist das Ergebnis eines kompositorischen Aktes"). Problema interno a SSP: l'applicazione di principi macro al livello micro (sample) non produce differenziazione percepibile — il valore istantaneo di pressione non ha identità riconoscibile (context-dependency); da cui il ripiego sui segmenti/permutazione.

## Rilevanza diretta per Gamma
Inquadramento teorico forte per la postura di Gamma. Il DSL YAML→Csound di GAMMA è un caso di modello compositivo che è anche modello del suono: i parametri (ritmo generatore, nube pitagorica, compensazione isofonica) non descrivono una sorgente preesistente ma costruiscono le regole da cui il materiale emerge. La triade real/symbolic e l'intersezione sensible/intelligible danno vocabolario filosofico (Badiou, Kittler) per la [[poetica]]. Differenza chiave da segnalare: SSP/SAWDUST eradicano i livelli micro/macro; Gamma li *mantiene gerarchici* (ritmo come parametro generatore unico che pilota più livelli) — Gamma è meno "axiomatic disorientation", più triangolazione decisionale.

## Collegamento alla tesi centrale
- "given the rules, find the music" (Koenig 1980) ≈ postura generativa differita di Gamma (tempo differito YAML→SCO→AIF).
- Il sistema come framework "in which the sound material itself emerges in the composition process" lega DSL parametrico + [[partitura-grafica]] (CompositionDebugger): la partitura grafica è la superficie sensibile dell'intelligibile codificato nello YAML.
- Anticommunication di Brün (creare l'ordine che il ricevente scopre per la prima volta) vs. modeling-the-receiver di Smith: utile per posizionare la [[compensazione-isofonica]] di Gamma — Gamma *modella il ricevente* (ISO 226 in Phon), scelta che CMSS-puro rifiuterebbe. Tensione produttiva da tematizzare, non da nascondere.

## Sezioni del paper CIM 2026 dove citare
- Intro / related work: lignaggio non-standard synthesis, definizione CMSS.
- Architettura: DSL come modello compositivo-e-di-suono.
- Poetica: real/symbolic, sensibile/intelligibile, sintesi come atto compositivo.
- Discussione: tensione Gamma (gerarchia micro/macro mantenuta + modeling-the-receiver) vs. CMSS ortodosso.

## Quote chiave
- "sound synthesis models need to be seen as compositional models and vice versa, I term this approach *compositionally motivated sound synthesis*." (p.2)
- "the synthesis methods of Brün, Xenakis, and Koenig form frameworks in which the sound material itself emerges in the composition process." (p.29)
- "the synthesis model is also a model of composition, or at least forms the basis of models of composition, like a sort of machine language into which the higher-level compositional model is to be compiled. […] seeing models as *productive* rather than imitative and emphasizing the intersection of the *intelligible* and the *sensible*." (p.31-32)

## Collegamenti
[[poetica]] · [[partitura-grafica]] · [[compensazione-isofonica]] · [[precursori]] (Koenig)
