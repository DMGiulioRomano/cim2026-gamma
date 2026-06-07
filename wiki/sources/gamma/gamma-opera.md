---
type: composizione
sources:
  - raw/GAMMA/yaml/Gamma.yaml
updated: 2026-06-07
---

# Gamma — struttura dell'opera

Analisi della partitura concreta sottomessa a CIM 2026, letta da
[yaml/Gamma.yaml](../../../raw/GAMMA/yaml/Gamma.yaml) (351 righe).

> Questa pagina è la fonte di verità sulla struttura per il paper/works del repo
> cim2026. La pagina [Gamma (wiki GAMMA)](../../../raw/GAMMA/wiki/composizioni/Gamma.md)
> è **stale**: sezione II marcata `_(TODO)_`, sezione I priva del layer
> "scampanello", durata I errata (140 vs 154). Il submodule è immutabile: la
> correzione vive qui.

## Sei sezioni, durate e sovrapposizioni

`offset_inizio` negativo = la sezione entra **prima** che la precedente finisca
(le sezioni si embricano, non si succedono nette).

| # | Sezione | Durata | offset | Inizio abs | Fine abs |
|---|---|---|---|---|---|
| I | Nascita Lenta di Cluster | 154 | 0 | 0 | 154 |
| II | solo ripresaglissante | 150 | −14 | 140 | 290 |
| III | Dalle nubi allo sciame | 60 | −15 | 275 | 335 |
| IV | Rottura | 80 | −60 | 275 | 355 |
| V | Cluster | 50 | −0.3 | ~355 | ~405 |
| VI | Ultra glissando | 110 | −30 | 375 | 485 |

Durata totale ≈ **485 s (~8:05)** — entro il limite Works ≤ 12 min. III e IV si
**sovrappongono per intero** (entrambe 275→335/355): la "rottura" irrompe dentro
lo sciame.

## Sezione per sezione

### I. Nascita Lenta di Cluster — 154 s, ratio_temporale 0.8
- **salita di gamma** — lifespan [0, .76], accelerando shape 2.0. Ottava sale
  [0,2]→[3,8], durata_armonica 24-32→12-24, densità cluster cresce. Il gesto
  fondante: dal grave verso l'acuto.
- **scintillii** — lifespan [.5, .74], `ppp`, durate brevi (.8-4→.72-2.4). Coda
  acuta sovrapposta alla salita.
- **scampanello** — lifespan [.76, 1], durate medie (9-12→4.5-9). *(assente nella
  md GAMMA)* — chiude la sezione.

### II. solo ripresaglissante — 150 s, offset −14
La sezione mancante nella md GAMMA. Quattro layer:
- **solista** — lifespan [0, .44], 4 attivazioni, accelerando shape 2.0. Ottava
  fissa 3, registro 10-11→1-40 (si apre), durata 30-36→21-27, `ppp`→`p`,
  densità 1-2→1-7 (interp_shape 2.0). `tipo_ritmi` esplicito che si infittisce:
  `[3,2,4,5,...]` → `[3,6,4,7,11,15,...]`. È il "solo".
- **glissando** — lifespan [.25, 1], 10 att., accelerando 2.0. Ottava 3-4,
  registro normale mean 10 std 2→std 20 (si allarga), offset_registro
  0→−30 (interp_shape .7): la "ripresa glissante". `ppp`→`p`.
- **Nubi sparsissime** — lifespan [.65, .7], 12 att., stochastic, ottava 8 fissa
  acuta, durate 0.1-0.4, densità 10-20, `ppp`, inviluppo triangolo.
- **Nubi Sparse** — lifespan [.7, 1], 35 att., stochastic, ottava 7-8, registro
  mean 30, da impulsivo (nonlinear_mode 3) verso triangolo, densità 10-20→1-6.
  Prepara la transizione di III.

### III. Dalle nubi allo sciame — 60 s, offset −15
- **Nubi Sparse verso sciame** — lifespan [0,1], leeway 20, accelerando.
  Densità cluster e onset_jitter crescono: la nube si addensa in sciame.
- **sciame** — lifespan [0,1], leeway 30, stochastic, ottave alte, coda.

### IV. Rottura — 80 s, offset −60 (irrompe dentro III)
- **impulso** — 13 att., accelerando, full range ottava [0,8], `ppp`→`ff`.
- **impulso grave** — lifespan [.7,1], 4 att., ottava [0,1], registro basso,
  cluster piccoli. Il contrappunto grave alla rottura.

### V. Cluster — 50 s, offset −0.3
- **cluster** — **1 sola attivazione**, densità 200-250 voci, durata 10-15,
  `f`, mega-impulsivo. La massa verticale: tutto insieme.

### VI. Ultra glissando — 110 s, offset −30
- **ultra glissando** — lifespan [0, .75], 6 att., densità 7-10→2-4, `p`→`ppp`.
  Il lungo glissando finale che si rarefà.
- **sciame** — lifespan [0, .5], 12 att., stochastic, `ppp`, densità 1-6. Coda.

## Arco formale (per il paper)

Lettura come stati in transizione ([[stato-musicale]]): nascita dal grave (I) →
solo che si apre e glissa (II) → addensamento nube→sciame (III) spezzato dalla
rottura piena (IV) → massa verticale singola (V) → glissando che si dissolve (VI).
Non eventi scelti: tendenze che si trasformano. È l'arco che la
[[partitura-grafica]] rende visibile come curve continue.

Il principio della singola variabile generatrice ([[ritmo-generatore]]) e
l'autogenerazione caotica ([[mappa-logistica]]) governano ogni layer; la nube
pitagorica ([[accordatura-pitagorica]]) i battimenti emergenti; la
[[compensazione-isofonica]] le dinamiche `ppp`..`ff`.

## Collegamenti

- [[poetica]] — l'arco come forma; il ciclo Delta→Gamma
- [[stato-musicale]] — transizione vs stasi nei singoli layer
- [[partitura-grafica]] — visualizzazione dell'arco
- Wiki GAMMA (stale su sez. I/II): [Gamma](../../../raw/GAMMA/wiki/composizioni/Gamma.md)

## Sezioni paper CIM 2026 dove descrivere

Sezione che descrive l'opera (struttura formale, arco delle sei sezioni) e
sezione poetica (forma come evoluzione di tendenze). Tabella timeline candidata a
figura/tabella del paper. Durata totale ~8:05 da citare nel form Works.
