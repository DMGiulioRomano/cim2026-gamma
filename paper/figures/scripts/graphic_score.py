#!/usr/bin/env python3
"""Partitura grafica: spazio di possibilita dichiarato vs eventi campionati.

Ricrea la figura del `CompositionDebugger` di GAMMA
(`raw/GAMMA/generative_composerYaml2.py`) per il paper: le maschere di tendenza
(buste sfumate) descrivono lo spazio di possibilita dichiarato nello YAML; gli
eventi (barre piene) sono il campionamento stocastico effettivo. La figura
materializza l'asse #2 della tesi: la partitura grafica come strumento
compositivo, non solo di debug.

Strategia: non reimplementa il motore. Copia il modulo GAMMA pinnato (submodule
`raw/GAMMA`, immutabile) in una dir temporanea, applica patch usa-e-getta (seed
fisso per riproducibilita, no-op del render Csound, label IT->EN), esegue la
pipeline fino alla FASE 3 (plot) e ritaglia una pagina rappresentativa.
Riproducibile dal repo: dipende solo da `raw/GAMMA` + stdlib + matplotlib.

NB: la partitura del WAV sottomesso (Works) non e riproducibile (reso senza
seed, nessuna cache salvata). Work e paper non condividono lo stesso render:
questa figura illustra il meccanismo, non e il ground-truth dell'opera.

Uso:
    .venv/bin/python paper/figures/scripts/graphic_score.py [--page N]
                     [--seed S] [--out FILE]
"""
import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
GAMMA = REPO / "raw" / "GAMMA"
YAML = "yaml/Gamma.yaml"

# Sostituzioni label IT -> EN applicate al sorgente GAMMA nella copia temp.
# Stringhe verbatim dal CompositionDebugger; se GAMMA cambia, aggiornare qui.
LABELS = {
    '"Ottava.Registro"': '"Octave.Register"',
    '"Durata Armonica (s)"': '"Harmonic duration (s)"',
    '"Prob. Dinamica"': '"Dynamics prob."',
    '"Dinamica (Lineare)"': '"Dynamics (linear)"',
    'f"Tempo (secondi, da {int(page_start_time)}s a {int(page_end_time)}s)"':
        'f"Time (s, from {int(page_start_time)}s to {int(page_end_time)}s)"',
    "'Maschera Ottava'": "'Octave mask'",
    "'Maschera Durata Armonica'": "'Harmonic-duration mask'",
    'plot_title = f"Visualizzazione Composizione: {base_composition_name}"':
        'plot_title = f"{base_composition_name}"',
    'fig.suptitle(f"{title} (Pagina {i+1}/{num_pages})" if partitura_mode else title, fontsize=14)':
        'fig.suptitle(f"{title} (page {i+1}/{num_pages})" if partitura_mode else title, fontsize=14)',
}


def _patch_source(src: str, seed: int) -> str:
    """Applica seed, no-op Csound e label EN al sorgente GAMMA."""
    anchor = "    yaml_file_path = sys.argv[1]\n"
    if anchor not in src:
        sys.exit("ERRORE: anchor seed non trovato nel sorgente GAMMA.")
    src = src.replace(
        anchor,
        anchor + f"    import numpy as _np, random as _rnd\n"
        f"    _np.random.seed({seed})\n    _rnd.seed({seed})\n",
        1,
    )

    csound = re.search(
        r"def run_csound_process\(csd_path, process_name, log_dir\):\n"
        r'    """\n    Lancia un singolo processo.*?\n        return None\n',
        src,
        re.DOTALL,
    )
    if not csound:
        sys.exit("ERRORE: run_csound_process (render reale) non trovato.")
    stub = ('def run_csound_process(csd_path, process_name, log_dir):\n'
            '    """PATCH: render saltato, il plot non richiede audio."""\n'
            '    return None\n')
    src = src[:csound.start()] + stub + src[csound.end():]

    for it, en in LABELS.items():
        if it not in src:
            sys.exit(f"ERRORE: label non trovata, GAMMA cambiata: {it}")
        src = src.replace(it, en, 1)
    return src


def _crop_page(pdf_in: Path, pdf_out: Path, page: int) -> None:
    """Estrae una pagina 1-based dal PDF multipagina."""
    try:
        from pypdf import PdfReader, PdfWriter
    except ImportError:
        from PyPDF2 import PdfReader, PdfWriter  # type: ignore
    reader = PdfReader(str(pdf_in))
    n = len(reader.pages)
    if not 1 <= page <= n:
        sys.exit(f"ERRORE: pagina {page} fuori range (1..{n}).")
    writer = PdfWriter()
    writer.add_page(reader.pages[page - 1])
    with open(pdf_out, "wb") as f:
        writer.write(f)
    print(f"  pagina {page}/{n} -> {pdf_out}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--page", type=int, default=3,
                    help="pagina (60s) da estrarre, 1-based (default 3)")
    ap.add_argument("--seed", type=int, default=20260528,
                    help="seed campionamento (default 20260528)")
    ap.add_argument("--out", type=Path,
                    default=REPO / "paper" / "figures" / "graphic_score.pdf")
    args = ap.parse_args()

    if not (GAMMA / "generative_composerYaml2.py").exists():
        sys.exit(f"ERRORE: submodule GAMMA assente in {GAMMA}. "
                 "git submodule update --init --recursive")

    tmp = Path(tempfile.mkdtemp(prefix="gamma-graphic-score."))
    try:
        shutil.copytree(GAMMA, tmp, dirs_exist_ok=True)
        mod = tmp / "generative_composerYaml2.py"
        mod.write_text(_patch_source(mod.read_text(), args.seed))

        # La pipeline crasha alla FASE 4 (assembly: niente WAV perche render
        # saltato). Irrilevante: la FASE 3 ha gia scritto il PDF partitura.
        subprocess.run([sys.executable, str(mod), YAML],
                       cwd=tmp, capture_output=True, text=True)

        pdf = tmp / "composizioni_generate" / "Gamma_partitura.pdf"
        if not pdf.exists():
            sys.exit("ERRORE: Gamma_partitura.pdf non generato (FASE 3 fallita).")

        args.out.parent.mkdir(parents=True, exist_ok=True)
        _crop_page(pdf, args.out, args.page)
        print(f"OK: {args.out}")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
