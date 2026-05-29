---
type: concept
sources:
  - raw/GAMMA/includes/NonlinearFunc.udo:L14-82
  - raw/GAMMA/includes/voce.orc:L51-65
updated: 2026-05-29
---

# Ritmo autogenerato: mappa logistica e feedback

Il valore ritmico che governa tutto (vedi [[ritmo-generatore]]) non è scritto
nota per nota. Dopo una breve sequenza esplicita iniziale (`tipo_ritmi`), il
flusso si **autogenera**: ogni nuovo ritmo è funzione del precedente. Una
lettura lookup che ricava il proprio input dal proprio output — un sistema
dinamico a tempo discreto la cui orbita è la musica.

## Il feedback nel codice

In `instr Voce` i ritmi vivono in una tabella temporanea `i_TempRitmiTab`.
Quando gli step espliciti finiscono (o si incontra uno zero), parte il ramo
`generateNewRhythm`:

```
i_Vecchio_Ritmo  tab_i i_EventIdx - 1, i_TempRitmiTab     ; legge l'ultimo scritto
i_RitmoCorrente  NonlinearFunc i_Vecchio_Ritmo, i_NonlinearMode
tabw_i i_RitmoCorrente, i_EventIdx, i_TempRitmiTab         ; riscrive
```

([voce.orc:L58-64](../../raw/GAMMA/includes/voce.orc#L58)).

La tabella è insieme buffer di input e di output: all'iterazione successiva
`i_EventIdx` avanza e si rilegge ciò che si è appena scritto. È la ricorsione
`x[n+1] = f(x[n])` materializzata in una f-table.

## `NonlinearFunc` — la mappa

`opcode NonlinearFunc, i, ippo`: dato il valore precedente `iX` (clampato in
`[1, 100]`) e un `iMode`, restituisce un intero in `[iMinVal, iMaxVal]`
(default `[1, 35]`). Quattro regimi
([NonlinearFunc.udo:L14-82](../../raw/GAMMA/includes/NonlinearFunc.udo#L14)):

| `iMode` | Comportamento | Formula chiave |
|---|---|---|
| 0 — convergente | tende a punto fisso | mappa logistica `r = 2.8`: `2.8·x·(1 - x/40)` |
| 1 — periodico | oscillazione regolare | `|sin(x·π/18)·cos(x·π/10)|·20 + 10` |
| 2 — caotico | caos deterministico | **mappa logistica `r = 3.99`**: `3.99·x·(1-x)` + noise ±0.05 |
| 3 — caos vero (default) | misto | 60% deterministico (sin/cos/tan) + 40% random + perturbazione ogni 7 step |

Il cuore è la **mappa logistica** `x[n+1] = r·x[n]·(1 - x[n])`. A `r = 2.8`
(mode 0) converge a un punto fisso → ritmo che si stabilizza. A `r = 3.99`
(mode 2) è nel regime caotico → orbita aperiodica, sensibile alle condizioni
iniziali, ma interamente determinata dal seme. Mode 1 sostituisce la logistica
con un battito di seni/coseni → periodicità udibile. Mode 3 inietta casualità
vera.

## Significato compositivo

Il compositore sceglie due cose, non i valori:

1. il **seme** — la sequenza `tipo_ritmi` iniziale;
2. il **regime** — `nonlinear_mode` (stabilità, periodicità, caos).

La superficie ritmica — e con essa altezza, spazio, ampiezza, perché tutto pende
dal ritmo ([[ritmo-generatore]]) — è poi l'**orbita** del sistema. Emergenza da
una regola deterministica: il principio estetico di [[poetica]] (controllo del
regime, non del dettaglio).

## Note di riproducibilità

- Mode 3 usa `random:i` → **non riproducibile** fra render.
- Mode 2 ha un piccolo rumore (±0.05) → semi-deterministico.
- Mode 0 e 1 sono pienamente deterministici dato il seme.
- Implicazione per la submission: il WAV depositato è **un** render di
  un'orbita; l'ancora audio→commit (tag `cim2026-submission`) fissa il sorgente,
  non la singola realizzazione caotica. Vedi `works/audio_link.txt`.

## Collegamenti

- [[ritmo-generatore]] — dove finisce il valore generato
- [[stato-musicale]] — `nonlinear_mode` come parametro della maschera di tendenza
- [[poetica]] — emergenza, sistema dinamico, tempo differito
- Wiki GAMMA: [NonlinearFunc](../../raw/GAMMA/wiki/includes/NonlinearFunc.md)

## Sezioni paper CIM 2026 dove descrivere

Sezione architettura (meccanismo) e sezione poetica (perché un sistema
dinamico). Possibile aggancio a precursori: mappe non lineari e caos
deterministico in composizione algoritmica (fonti da ingestire).
