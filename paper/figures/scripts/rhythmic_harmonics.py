#!/usr/bin/env python3
"""Armoniche ritmiche: una durata armonica suddivisa dalla serie armonica.

Ricreazione in matplotlib del grafico TikZ del repo `rhythmic-harmonics`
(latex/main.tex, latex/layout.tex). Ogni riga `i` rappresenta l'i-esima armonica
ritmica della durata fondamentale: lo stesso intervallo di tempo diviso in `i`
parti uguali. I punti sono gli attacchi della suddivisione; le verticali
tratteggiate mostrano l'allineamento delle suddivisioni fra armoniche diverse
(coincidenze = consonanze ritmiche).

Analogia con GAMMA: `durata_armonica` (lo stesso intervallo di riferimento)
suddivisa dal ritmo interno alla voce. Vedi wiki concepts/ritmo-generatore.

Uso:
    python rhythmic_harmonics.py [--num-lines N] [--units U] [--out FILE]
"""
import argparse
from pathlib import Path

import matplotlib.pyplot as plt


def plot_rhythmic_harmonics(num_lines=32, units=2, length=22.0, spacing=0.95,
                            ax=None):
    """Disegna la griglia delle armoniche ritmiche.

    num_lines : numero di armoniche (righe).
    units     : numero di griglie ripetute lungo x (cicli della durata).
    length    : lunghezza in unità della durata fondamentale.
    spacing   : distanza verticale fra righe.
    """
    own_fig = ax is None
    if own_fig:
        fig, ax = plt.subplots(figsize=(units * 8.5, num_lines * 0.28))

    grid_margin = 0.5
    grid_width = length + 2 * grid_margin
    top_space = 1.0
    timeline_space = 0.2
    bottom_y = -spacing * num_lines - spacing - timeline_space - top_space

    for k in range(units):
        x_shift = k * grid_width

        # frame superiore della singola griglia
        ax.plot([x_shift - grid_margin, x_shift + length],
                [-top_space, -top_space], color="black", linewidth=1.2)

        for i in range(1, num_lines + 1):
            y = -i * spacing - top_space - timeline_space

            # la linea dell'armonica i-esima
            ax.plot([x_shift, x_shift + length], [y, y],
                    color="black", alpha=0.5, linewidth=1.2)

            # punto d'inizio (attacco della fondamentale di riga)
            ax.plot(x_shift, y, "o", color="black", markersize=3)

            # etichetta dell'armonica a sinistra
            ax.annotate(str(i), (x_shift + 0.5, y + 0.2),
                        ha="right", va="bottom", fontsize=6)

            # suddivisioni: riga i ha i parti => i-1 punti interni
            if i > 1:
                division = i - 1
                for j in range(1, division + 1):
                    x_pos = x_shift + j * length / (division + 1)
                    ax.plot(x_pos, y, "o", color="black", markersize=3)
                    ax.annotate(str(j), (x_pos, y), ha="center", va="top",
                                fontsize=4, xytext=(0, -3),
                                textcoords="offset points")
                    # verticale tratteggiata: allineamento della suddivisione
                    ax.plot([x_pos, x_pos], [bottom_y, y],
                            linestyle=(0, (1, 3)), color="black", alpha=0.6,
                            linewidth=0.6)

    ax.set_xlim(-grid_margin - 0.5, units * grid_width + 0.5)
    ax.set_ylim(bottom_y - 0.5, 0)
    ax.set_aspect("equal")
    ax.axis("off")

    if own_fig:
        fig.tight_layout()
        return fig
    return ax


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--num-lines", type=int, default=32)
    p.add_argument("--units", type=int, default=2)
    p.add_argument("--length", type=float, default=22.0)
    p.add_argument("--spacing", type=float, default=0.95)
    p.add_argument("--out", type=str,
                   default=str(Path(__file__).resolve().parents[1]
                              / "rhythmic_harmonics.pdf"))
    args = p.parse_args()

    fig = plot_rhythmic_harmonics(num_lines=args.num_lines, units=args.units,
                                  length=args.length, spacing=args.spacing)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, bbox_inches="tight")
    # PNG di anteprima a fianco
    fig.savefig(out.with_suffix(".png"), dpi=150, bbox_inches="tight")
    print(f"Scritto: {out} e {out.with_suffix('.png')}")


if __name__ == "__main__":
    main()
