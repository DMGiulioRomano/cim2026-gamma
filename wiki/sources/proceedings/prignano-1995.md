---
type: proceedings
bibtex: Prignano1995
source_pdf: raw/proceedings/CIM_XI_1995_Atti.pdf
venue: XI CIM, Bologna, 8-11 nov 1995
updated: 2026-06-04
---

# [Prignano, 1995] Sintesi di Eventi Sonori Complessi per mezzo di Iterazioni Funzionali

## Citazione CIM
Prignano, I. (1995). Sintesi di Eventi Sonori Complessi per mezzo di Iterazioni
Funzionali. In *Atti dell'XI Colloquio di Informatica Musicale*, Bologna,
pp. 23-26.

## Argomento centrale
Metodo di sintesi non-standard ("functional iteration synthesis"): iterazione di
una mappa non lineare dipendente da parametri `F(x0; a1,…,am)` a partire da un
dato iniziale `x0`. Variando parametri e dato iniziale a sample rate si
costruisce la sequenza di campioni. Nessun modello acustico: il suono *è*
l'orbita di un sistema dinamico discreto.

## Categoria e lunghezza
Comunicazione scientifica, Digital Signal Processing (I), 4 pp.

## Sistema o strumento descritto
Formalismo: `A ⊂ ℝ` dati iniziali, `G ⊂ ℝ^m` parametri della mappa, `B ⊂ ℝ`
campioni; `f^n(x)` = applicazione ripetuta n volte. Applicazione con la **"mappa
seno"**: `x[k,i] = sin(r_i · x[k-1,i])`, parametro `r ∈ [0,4]`. Diagramma di
biforcazione: al crescere di `r` il sistema passa da attrattori periodici ad
attrattori caotici, con transizioni improvvise. Le traiettorie nello **spazio
delle fasi** generano i segnali. Suoni da "attivi" (transienti spettralmente
ricchi, turbolenza, rumore) a "inattivi" (curve quasi piatte), con spettri anche
armonici.

## Gap o problema identificato
Le tecniche non-standard portano a rappresentazione microstrutturale del suono;
domanda aperta: si possono far emergere proprietà macrostrutturali operando al
livello micro (campione)? Si cita esplicitamente "l'uso della mappa logistica
nell'organizzazione dei grani in tecniche di sintesi granulare" come riferimento.

## Analogia con Gamma
Stessa famiglia matematica di [[mappa-logistica]]: iterazione di mappe non
lineari dipendenti da parametro, regimi convergente/periodico/caotico letti dal
diagramma di biforcazione. Differenza di scala: Prignano itera **a sample rate**
(la mappa È il segnale audio); GAMMA itera **a event rate** (la mappa genera il
valore ritmico che poi pilota la sintesi, [[ritmo-generatore]]). Comune: il
compositore fissa seme + parametro/regime, la superficie emerge come orbita.
"Dimenticanza" del dato iniziale ad alte iterate ≈ sensibilità alle condizioni
iniziali / caos.

## Posizionamento storico
**Laboratorio Musica & Sonologia, L'Aquila** — stesso laboratorio di Di Scipio
(vedi [[discipio-1995]]). Genealogia locale della sintesi per iterazione non
lineare, **nella stessa città del CIM 2026**. Diretto antenato del "caos sonoro"
di Rizzuti ([[rizzuti-2006]]).

## Sezioni del paper CIM 2026 dove citare
Related work (precursore iterazione funzionale), Architettura (biforcazione,
spazio delle fasi come modello del passaggio stasi↔transizione, cfr.
[[stato-musicale]]).

## Note stilistiche
Matematicamente esplicito (formalismo insiemistico, equazioni). Utile per
giustificare con rigore il vocabolario "attrattore / biforcazione / spazio delle
fasi" se il paper CIM lo adotta.

## Quote chiave
> "una vasta classe di tali sistemi mostrano comportamenti complessi
> qualitativamente simili, al variare del parametro, indipendentemente dalla
> forma particolare dei sistemi stessi." (p.23)

## Collegamenti
[[mappa-logistica]] · [[ritmo-generatore]] · [[stato-musicale]] · [[precursori]] ·
[[discipio-1995]] · [[rizzuti-2006]]
