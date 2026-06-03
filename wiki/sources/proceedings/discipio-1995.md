---
type: proceedings
bibtex: DiScipio1995
source_pdf: raw/proceedings/CIM_XI_1995_Atti.pdf
venue: XI CIM, Bologna, 8-11 nov 1995
updated: 2026-06-04
---

# [Di Scipio, 1995] Real-time Polyphonic Time-shifting of Sound with Interactive Systems

## Citazione CIM
Di Scipio, A. (1995). Real-time Polyphonic Time-shifting of Sound with
Interactive Systems. In *Atti dell'XI Colloquio di Informatica Musicale*,
Bologna, pp. 19-22.

## Argomento centrale
Metodi di granular processing (time-shifting polifonico e granulazione
ricorsiva) in due opere dell'autore (*Hybris*, *Essai du Vide. Schweigen*).
Centrale la nozione di **microcomposizione** (micro-time sonic design): comporre
le unità minime e temporalmente limitate perché da esse emergano proprietà
strutturali di alto livello.

## Categoria e lunghezza
Comunicazione scientifica, Digital Signal Processing (I), 4 pp.

## Sistema o strumento descritto
Sistemi KYMA-CAPYBARA (LMS) e PODX (Simon Fraser, set Truax/GSAMX). "Stream of
grain" = due granulatori (look-up + envelope + allpass) sfasati di mezza durata
di grano; controllo algoritmico dei flussi via script Smalltalk-80. **Granulazione
ricorsiva** in *Essai du Vide*: il suono granulato è riacceduto e ripassato nel
processo — iterazione di due funzioni di trasferimento su un dato iniziale:

```
x[n+1] = f_b(f_a(x[n]))
```

con `f_a` = time-shift, `f_b` = regola di accesso random. Le trasformazioni
iterate producono una "vaporizzazione" della sorgente e "gestural patterns
absolutely unpredictable at the outset".

## Gap o problema identificato
La microcomposizione "deals with a specific problem domain: in which way minimal,
time-limited units should be *composed* in order to give rise to high-level
structural properties. This is a problem of perception and a problem of music
theory." Aperto: come legare livello micro e macro percepito.

## Analogia con Gamma
- **Iterazione di funzioni → emergenza**: `x[n+1]=f_b(f_a(x[n]))` è omologa al
  feedback `x[n+1]=f(x[n])` di [[mappa-logistica]] in GAMMA, applicata però alla
  granulazione del suono concreto invece che al valore ritmico.
- **Emergenza di gesti imprevedibili da regola deterministica**: nucleo di
  [[poetica]].
- **Sistema dinamico con auto-regolazione**: l'esecutore (qui live) come "source
  of feedback and self-regulation within a dynamical system… to avoid totally
  uncontrolled results as much as strictly periodic behaviors" — la stessa
  tensione stasi↔caos di [[stato-musicale]], qui in performance, in GAMMA in
  tempo differito.

Differenza: Di Scipio lavora in **tempo reale interattivo** su suono concreto;
GAMMA è **tempo differito** su sintesi generata. La nozione di microcomposizione
e di emergenza è però condivisa.

## Posizionamento storico
**Laboratorio Musica e Sonologia, Università di L'Aquila** — stesso laboratorio
di Prignano ([[prignano-1995]]), **città del CIM 2026**. Figura di riferimento
internazionale per emergenza / sistemi dinamici / *Audible Ecosystemics* (vedi
[[precursori]] asse 1). Bibliografia: De Poli-Piccialli-Roads *Representations of
Musical Signals* (MIT 1991), Truax *Real-time Granular Synthesis*, Di Scipio
"Micro-time sonic design and the formation of timbre" (Contemporary Music Review
10(1), 1994), "Inseparable models of material and of musical design" (JNMR 24(1),
1995).

## Sezioni del paper CIM 2026 dove citare
Introduzione (postura: microcomposizione, emergenza), Related work (genealogia
L'Aquila + emergenza), Conclusione (forma come comportamento di sistema
dinamico).

## Note stilistiche
Riflessione teorica densa intrecciata al dettaglio tecnico: modello di come un
paper compositivo CIM lega sistema e poetica senza ridursi a descrizione tecnica
(cfr. mandato del paper GAMMA in `CLAUDE.md > Tesi paper`).

## Quote chiave
> "the performer becomes here a source of feedback and self-regulation within a
> dynamical system… in order to avoid totally uncontrolled results as much as
> strictly periodic behaviors." (p.21)

## Collegamenti
[[poetica]] · [[mappa-logistica]] · [[stato-musicale]] · [[precursori]] ·
[[prignano-1995]] · [[rizzuti-2006]]
