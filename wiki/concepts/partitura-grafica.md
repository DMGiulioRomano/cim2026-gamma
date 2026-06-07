---
type: concept
sources:
  - raw/GAMMA/generative_composerYaml2.py:L958-1356
  - raw/GAMMA/wiki/pipeline.md
updated: 2026-06-07
---

# Partitura grafica: il plot come strumento compositivo

Il sistema GAMMA emette, accanto al WAV, un **PDF della partitura** generato dalla
classe `CompositionDebugger`
([generative_composerYaml2.py:L958](../../raw/GAMMA/generative_composerYaml2.py#L958)).
Il nome della classe dice "debugger", ma la funzione è compositiva: è il terzo
vertice della triangolazione decisionale (DSL parametrico ↔ partitura visuale ↔
ascolto) descritta in [[poetica]]. Non si legge il codice né si ascolta soltanto:
si **guarda l'orbita dei parametri** prima e dopo il render.

Output: `composizioni_generate/<nome>_partitura.pdf` (modalità partitura,
multi-pagina) oppure `<nome>_visual_A3.pdf` (pagina singola). Mai rigenerato a
mano: è artefatto del Python, si cita.

## Cosa mostra — non il suono, le tendenze

Il punto centrale per il paper: la partitura **non** plotta la forma d'onda né lo
spettro. Plotta le **maschere di tendenza** ([[stato-musicale]]) — le buste di
possibilità da cui il sistema campiona — sovrapposte agli eventi effettivamente
campionati. Si vede insieme lo **spazio dichiarato** e la **realizzazione
stocastica** che ne è uscita. È la rappresentazione visiva del principio
"controllo dello spazio di possibilità, non del dettaglio".

Tecnicamente: per ogni layer `_calculate_plot_data_for_layer` interpola
`stato_iniziale`→`stato_finale` in 100 campioni temporali
([L964-1035](../../raw/GAMMA/generative_composerYaml2.py#L964)) e disegna la busta
con `fill_between` (alpha 0.2). Sopra, gli eventi reali come rettangoli colorati.

## Layout della pagina — tre assi impilati

Figura A3 landscape (420×297 mm), tre righe con `height_ratios [3, 1, 1]`
([L1326-1329](../../raw/GAMMA/generative_composerYaml2.py#L1326)). Asse X = tempo
in secondi, condiviso.

1. **Pannello altezza (3/5 dell'altezza) — `ax_pitch` + `ax_dur`**
   ([L1176-1188](../../raw/GAMMA/generative_composerYaml2.py#L1176)):
   - Y sinistro: **Ottava.Registro** (la nube pitagorica,
     [[accordatura-pitagorica]]). Pitch = `ottava + registro/(max+1)`
     ([L1303](../../raw/GAMMA/generative_composerYaml2.py#L1303)).
   - Buste di tendenza dell'ottava (`fill_between`), una per layer, colore per
     layer.
   - **Eventi** = rettangoli `viridis`, colore = ampiezza normalizzata
     ([L1243](../../raw/GAMMA/generative_composerYaml2.py#L1243)): si legge la
     dinamica anche qui, per colore.
   - Y destro gemello (`twinx`): **Durata Armonica (s)** in darkcyan
     ([L1186](../../raw/GAMMA/generative_composerYaml2.py#L1186)).
   - Linee verticali tratteggiate: confini layer (colore layer), attivazioni
     (`Attivazione`, dodgerblue,
     [L1344](../../raw/GAMMA/generative_composerYaml2.py#L1344)) = il respiro macro
     del [[ritmo-generatore]], confini sezione (verde inizio / rosso fine).

2. **Pannello dinamica lineare (1/5) — `ax_dyn_linear`**
   ([L1190-1197](../../raw/GAMMA/generative_composerYaml2.py#L1190)): trend del
   livello quando la dinamica è una tendenza continua (`value`/`mean`). Y
   etichettato `ppp..fff` via `dynamic_to_index`. È la dinamica in Phon a monte
   della [[compensazione-isofonica]].

3. **Pannello dinamica probabilistica (1/5) — `ax_dyn_prob`**
   ([L1199-1201](../../raw/GAMMA/generative_composerYaml2.py#L1199)): quando la
   dinamica è `choices`+`weights`, `stackplot` dei pesi nel tempo
   ([L1073](../../raw/GAMMA/generative_composerYaml2.py#L1073)). Si vede il
   **cross-fade delle probabilità** da inizio a fine layer: la transizione di uno
   stato stocastico resa esplicita.

## Modalità partitura — paginazione

In `partitura_mode` il pezzo è spezzato in pagine da `page_duration_s` (default
60s): `num_pages = ceil(total_duration / page_duration_s)`
([L1315-1321](../../raw/GAMMA/generative_composerYaml2.py#L1315)). Ogni pagina è
una finestra temporale fissa — leggibile come una partitura tradizionale per
sistemi. La modalità `visual_A3` comprime invece tutto in una pagina sola.

## Perché è strumento, non debug

Il workflow è a tempo differito ([[poetica]]): YAML → render offline → ascolto →
riscrittura. La partitura grafica entra **prima dell'ascolto** e lo informa:

- rende visibile la **distanza fra dichiarato e realizzato** (busta vs eventi):
  se l'orbita campionata non riempie lo spazio voluto, lo si vede senza ascoltare;
- mostra le **transizioni di stato** ([[stato-musicale]]) come curve continue —
  l'accelerando, il glissando d'ottava, il cross-fade dinamico — cioè la forma
  come evoluzione di tendenze, non come lista di eventi;
- separa visivamente i **due strati di tempo**: attivazioni macro (linee
  dodgerblue) vs durate armoniche (asse destro) vs grana micro implicita nei
  rettangoli.

Il plot non corregge errori di sintassi (quello lo fa il parser): corregge
**errori di intenzione formale**. Per questo è compositivo.

## Limiti / cosa NON mostra

- Nessuna informazione spettrale o di forma d'onda: l'identità timbrica del
  singolo evento ([eventoSonoro, wiki GAMMA](../../raw/GAMMA/wiki/includes/eventoSonoro.md))
  non è visibile.
- La grana ritmica micro ([[mappa-logistica]]) non è plottata come orbita: si
  deduce dalle durate, non si vede l'iterazione non lineare.
- La spazializzazione Mid/Side ([[ritmo-generatore]]) non ha un proprio asse.

## Collegamenti

- [[poetica]] — la triangolazione DSL ↔ partitura ↔ ascolto; il tempo differito
- [[stato-musicale]] — le maschere di tendenza che la partitura visualizza
- [[ritmo-generatore]] — le attivazioni macro plottate come linee verticali
- [[compensazione-isofonica]] — la dinamica in Phon dei due pannelli inferiori
- [[accordatura-pitagorica]] — l'asse Ottava.Registro
- Pipeline GAMMA: [pipeline](../../raw/GAMMA/wiki/pipeline.md) (step 9, plot)
- Composizione: [Gamma (wiki GAMMA)](../../raw/GAMMA/wiki/composizioni/Gamma.md)

## Sezioni paper CIM 2026 dove descrivere

Angolo centrale #2 del paper (cfr. `CLAUDE.md > Tesi paper`): la partitura grafica
come strumento compositivo, non di debug. Da collocare nella sezione architettura
(cosa plotta, i tre assi) e nella sezione metodo/poetica (come informa la
decisione prima dell'ascolto, la distanza dichiarato↔realizzato). Candidata a una
**figura** del paper: una pagina di `Gamma_partitura.pdf`.
