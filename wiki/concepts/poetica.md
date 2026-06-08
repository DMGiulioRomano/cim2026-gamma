---
type: concept
sources:
  - docs/plans/works-form-status.md
  - raw/GAMMA/yaml/Gamma.yaml
  - wiki/concepts/precursori.md
updated: 2026-06-07
---

# Poetica: stati musicali in transizione, tempo differito

> **Stato:** tesi consolidata. Qui vive la postura compositiva del paper CIM 2026
> (cfr. `CLAUDE.md > Tesi paper`). Unico punto sospeso: l'eredità Branchi, in
> attesa della fonte primaria (vedi §Posizionamento). La postura è personale e
> situata: mai formulare come "è meglio fare così".

## Il nucleo

*Gamma* mette a fuoco **stati musicali in transizione**. La forma non è una
successione di eventi scelti, ma l'evoluzione di tendenze: uno stato che si
trasforma con continuità da inizio a fine, oppure che resta fermo (stasi). La
distinzione tecnica vive in [[stato-musicale]]; la sua lettura formale è il
soggetto dell'opera.

## I tre principi che si tengono

1. **Una variabile genera la texture.** Il ritmo decide tempo, altezza, spazio e
   ampiezza ([[ritmo-generatore]]). Il compositore non scrive la quadruplice
   superficie: ne sceglie la sorgente.
2. **La sorgente è un sistema dinamico.** Il ritmo si autogenera per feedback non
   lineare ([[mappa-logistica]]): si fissa il seme e il regime, l'orbita emerge.
3. **Lo spazio frequenziale produce ciò che non controllo.** La nube pitagorica a
   200 gradi ([[accordatura-pitagorica]]) genera battimenti che non sono
   pianificati grado per grado: emergono dall'incontro delle voci.

Il filo comune: **controllo dello spazio di possibilità, non del dettaglio**.
L'ampiezza isofonica ([[compensazione-isofonica]]) è il contrappeso — l'unico
luogo dove il sistema reimpone una coerenza percettiva sul materiale emergente.

## Tempo differito

Il ciclo di lavoro è un feedback lungo: specifica YAML → render offline →
ascolto → riscrittura. Il tempo differito è una scelta, non un limite: separare
la decisione dalla resa permette di trattare l'ascolto come uno strumento di
giudizio sull'orbita, non sul gesto. È la triangolazione fra DSL parametrico,
partitura visuale (il plot PDF del `CompositionDebugger`, [[partitura-grafica]])
e ascolto.

## Il ciclo Delta → Gamma

Dalla nota di programma: se *Delta* è la foce — modellata da affluenti,
sedimenti, accumulo — *Gamma* è la sorgente cristallina. La stessa essenza
algoritmica ridotta alla condizione più elementare: un grido che diventa suono,
che abita lo spazio nella forma più pura. (Per *Intero* e per *Lontano*.)

## Posizionamento

La postura di *Gamma* non si inventa: si situa. I precursori (mappati per asse in
[[precursori]]) collocano la scelta in una tradizione, non la giustificano.

### Caos deterministico come sorgente

Il ritmo che si autogenera per feedback non lineare ([[mappa-logistica]]) ha un
lignaggio preciso. **Agostino Di Scipio** è il match più stretto: sintesi via
funzioni nonlineari iterate, stessa famiglia matematica del `NonlinearFunc` di
GAMMA, e soprattutto la stessa poetica dell'**emergenza** — il compositore
progetta il sistema, non l'esito. È la formulazione, vent'anni prima, del
principio "controllo dello spazio di possibilità, non del dettaglio". **Rick
Bidlack** (1992) fissa il riferimento canonico mappa logistica → musica: la
sensibilità alle condizioni iniziali come generatore. La differenza di *Gamma*
non è la matematica del caos ma il punto di applicazione: non la sintesi del
campione, ma il *ritmo* come variabile a monte che propaga su quattro dimensioni
(asse 6 in [[precursori]], [[ritmo-generatore]]).

### Genealogia situata: L'Aquila

Di Scipio e Prignano (XI CIM 1995) operano entrambi al Laboratorio Musica e
Sonologia dell'Università di L'Aquila — la stessa città del CIM 2026. Entrambi
sintesi per iterazione di funzioni non lineari; [[rizzuti-2006]] ne è erede
diretto ("il caos sonoro" in CSound). La linea locale "iterazione non lineare →
suono" è il contesto naturale del paper: *Gamma* vi si inscrive, non la fonda.

### Eredità Branchi (pitagorica)

L'asse della nube pitagorica densa ([[accordatura-pitagorica]]) discende da
**Walter Branchi** e dal suo lavoro sui sistemi di intonazione ("Intervalli e
sistemi di intonazione"). È fonte **primaria** del repo, non semplice citazione:
l'opera *Intero* di Branchi è anche tassello del ciclo Delta→Gamma→Intero (§"Il
ciclo Delta → Gamma"). Sviluppare questa sezione dopo aver reperito la fonte
(non open-access, reperimento manuale in corso — vedi *Stato fonti* in
[[precursori]]); finché manca, il claim resta sospeso e citato come
`[Branchi, fonte da reperire]` nel paper.

### Tempo differito come scelta, non limite

Il ciclo YAML→render→ascolto→riscrittura ha un precedente storico in **Curtis
Roads** (*Microsound*): il render granulare non-realtime degli anni '70,
composizioni "in anni", il tempo differito assunto come scelta poetica. Inquadra
la triangolazione DSL↔partitura↔ascolto come postura, non come vincolo tecnico.

## Collegamenti

- [[ritmo-generatore]] · [[mappa-logistica]] · [[accordatura-pitagorica]] ·
  [[compensazione-isofonica]] · [[stato-musicale]] · [[precursori]]
- Composizione: [[gamma-opera]] (struttura 6 sezioni) · [Gamma (wiki GAMMA)](../../raw/GAMMA/wiki/composizioni/Gamma.md)
- Materiali Works: [works-form-status](../../docs/plans/works-form-status.md)

## Sezioni paper CIM 2026 dove descrivere

Introduzione (postura) e sezione conclusiva (forma come stato in transizione).
