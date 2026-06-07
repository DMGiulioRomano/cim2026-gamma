#!/usr/bin/env python3
"""Armoniche spaziali lungo la circonferenza.

Ricreazione del grafico polare di `delta/src/delta/builder/Spazio.py`
(metodi genera_e_plotta_polare_sine / _cosine). Le funzioni |sin(i/2 * theta)|^n
e |cos(i/2 * theta)|^n, plottate in coordinate polari, descrivono lobi di energia
distribuiti lungo la circonferenza: le "armoniche spaziali". L'esponente n ne
restringe i lobi (focalizzazione spaziale).

Genera:
  - una figura statica matplotlib (PDF + PNG) per il paper, a esponente fisso;
  - una figura plotly interattiva (HTML) con slider sull'esponente, fedele
    all'originale Spazio.py.

Uso:
    python spatial_harmonics.py [--num N] [--exp E] [--basis sin|cos]
                                [--no-html] [--out FILE]
"""
import argparse
from pathlib import Path

import numpy as np


def _r_base(theta, num, basis):
    fn = np.sin if basis == "sin" else np.cos
    return [np.abs(fn(theta * i / 2)) for i in range(1, num + 1)]


def matplotlib_figure(num=10, exponent=1.0, basis="sin"):
    """Figura polare statica (matplotlib) a esponente fisso, per il paper."""
    import matplotlib.pyplot as plt

    theta = np.linspace(0, 2 * np.pi, 1000)
    r_base = _r_base(theta, num, basis)
    cmap = plt.get_cmap("hsv")

    fig, ax = plt.subplots(subplot_kw={"projection": "polar"},
                           figsize=(6, 6))
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(1)  # antiorario, come l'originale
    for i in range(num):
        ax.plot(theta, r_base[i] ** exponent,
                color=cmap(i / num), linewidth=1.5,
                label=f"{basis}({(i + 1) / 2:g}θ)")
    ax.set_title(f"Armoniche spaziali |{basis}(i/2·θ)|"
                 f"$^{{{exponent:g}}}$", pad=20)
    ax.set_rticks([0.5, 1.0])
    ax.legend(loc="upper right", bbox_to_anchor=(1.25, 1.05),
              fontsize=6, ncol=1)
    fig.tight_layout()
    return fig


def plotly_html(num=10, basis="sin", out_html="spatial_harmonics.html"):
    """Figura polare interattiva (plotly) con slider sull'esponente.

    Riproduce genera_e_plotta_polare_sine/_cosine di Spazio.py.
    """
    import plotly.graph_objects as go

    theta = np.linspace(0, 2 * np.pi, 500)
    r_base = _r_base(theta, num, basis)
    colori = [f"hsl({hue}, 70%, 50%)"
              for hue in np.linspace(0, 360, num)]
    valori_n = np.arange(1, 5, 0.5)

    fig = go.Figure(
        data=[
            go.Scatterpolar(
                r=r_base[i] ** 1,
                theta=np.degrees(theta),
                mode="lines",
                line=dict(width=2, color=colori[i]),
                name=f"{basis}({(i + 1) / 2:g}θ)",
            )
            for i in range(num)
        ],
        layout=go.Layout(
            title=f"Armoniche spaziali polari |{basis}(θ·i/2)|^n",
            polar=dict(
                angularaxis=dict(
                    tickvals=[0, 90, 180, 270],
                    ticktext=["0°", "90°", "180°", "270°"],
                    rotation=90,
                    direction="counterclockwise",
                ),
                radialaxis=dict(visible=True, showline=True, linewidth=2),
            ),
            template="plotly_white",
        ),
    )

    fig.frames = [
        go.Frame(
            data=[
                go.Scatterpolar(
                    r=r_base[i] ** n,
                    theta=np.degrees(theta),
                    mode="lines",
                    line=dict(width=2, color=colori[i]),
                    name=f"{basis}({(i + 1) / 2:g}θ)",
                )
                for i in range(num)
            ],
            name=f"n={n:.1f}",
        )
        for n in valori_n
    ]

    sliders = [{
        "steps": [
            {
                "args": [[f"n={n:.1f}"],
                         {"frame": {"duration": 500, "redraw": True},
                          "mode": "immediate"}],
                "label": f"n = {n:.1f}",
                "method": "animate",
            }
            for n in valori_n
        ],
        "active": 0,
        "currentvalue": {"font": {"size": 20}, "prefix": "Esponente n: ",
                         "visible": True, "xanchor": "center"},
        "pad": {"b": 10, "t": 50},
        "x": 0.1,
        "len": 0.9,
    }]
    fig.update_layout(sliders=sliders)
    fig.write_html(out_html)
    return out_html


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--num", type=int, default=10)
    p.add_argument("--exp", type=float, default=2.0)
    p.add_argument("--basis", choices=["sin", "cos"], default="sin")
    p.add_argument("--no-html", action="store_true",
                   help="salta la figura plotly interattiva")
    p.add_argument("--out", type=str,
                   default=str(Path(__file__).resolve().parents[1]
                              / "spatial_harmonics.pdf"))
    args = p.parse_args()

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)

    fig = matplotlib_figure(num=args.num, exponent=args.exp, basis=args.basis)
    fig.savefig(out, bbox_inches="tight")
    fig.savefig(out.with_suffix(".png"), dpi=150, bbox_inches="tight")
    print(f"Scritto: {out} e {out.with_suffix('.png')}")

    if not args.no_html:
        html = plotly_html(num=args.num, basis=args.basis,
                           out_html=str(out.with_suffix(".html")))
        print(f"Scritto: {html}")


if __name__ == "__main__":
    main()
