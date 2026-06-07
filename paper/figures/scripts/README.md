# Script delle figure del paper

Generatori Python delle figure per `paper/cim2026.tex`. Ricreazioni di grafici
provenienti da repo sorella dell'autore (vendored come riferimento concettuale,
non come dipendenza di build).

## Figure

| Script | Figura | Origine ricreata |
|---|---|---|
| `rhythmic_harmonics.py` | Armoniche ritmiche: una durata suddivisa dalla serie armonica (riga `i` = `i` parti uguali) | TikZ di `rhythmic-harmonics/latex/main.tex` |
| `spatial_harmonics.py` | Armoniche spaziali polari `\|sin/cos(i/2·θ)\|^n` lungo la circonferenza | `delta/src/delta/builder/Spazio.py` (metodi `genera_e_plotta_polare_*`) |

## Uso

```bash
# dalla root del repo, con la .venv del repo
.venv/bin/python paper/figures/scripts/rhythmic_harmonics.py
.venv/bin/python paper/figures/scripts/spatial_harmonics.py
```

Output in `paper/figures/`:

- `*.pdf` — versione per il paper (tracciata in git, inclusa dal LaTeX).
- `*.png` — anteprima (gitignored).
- `spatial_harmonics.html` — versione plotly interattiva con slider
  sull'esponente `n` (gitignored), fedele all'originale `Spazio.py`.

## Opzioni utili

```bash
# armoniche ritmiche: numero di armoniche, cicli, geometria
python rhythmic_harmonics.py --num-lines 16 --units 1

# armoniche spaziali: numero di armoniche, esponente, base, niente HTML
python spatial_harmonics.py --num 10 --exp 2 --basis cos --no-html
```

## Dipendenze

`numpy`, `matplotlib`, `plotly`, `kaleido` (export statico). Installazione nella
`.venv` del repo:

```bash
python3.11 -m venv .venv
.venv/bin/pip install numpy matplotlib plotly kaleido
```
