# cim2026-gamma

Submission al **XXV CIM — Colloquio di Informatica Musicale**, L'Aquila, 13-16 ottobre 2026.

Autore: Giulio Romano De Mattia.

Opera: **Gamma** — composizione elettroacustica su supporto fisso, generata via sistema YAML→Csound del repo [GAMMA](https://github.com/DMGiulioRomano/GAMMA) (vendored come submodule in `raw/GAMMA/`).

Convenzioni operative, workflow ingest fonti, branch policy e regole di anonimizzazione: vedi [CLAUDE.md](CLAUDE.md). Checklist pre-upload EasyChair: [docs/plans/submission-checklist.md](docs/plans/submission-checklist.md).

## Struttura

```
works/   submission Call for Works (deadline 29 maggio 2026)
  cim2026_template_works_en_v2.odt   template ufficiale (compilare)
  cim2026_template_works_en_v2.pdf   template ufficiale (riferimento)
  application_form_filled.odt        compilato (da generare)
  application_form_filled.pdf        compilato anonimizzato (da generare)
  audio_link.txt                     URL Drive/Dropbox del WAV stereo 48k/24bit

paper/   submission Call for Papers (deadline 21 giugno 2026)
  CIM2026_LaTeX_template_paper_v3/   template LaTeX ufficiale (intoccato)
  cim2026.tex                        sorgente paper (da derivare dal template)
  refs.bib                           bibliografia (gestita da Zotero + Better BibTeX)
  figures/                           figure paper

raw/                                 sorgenti immutabili (LLM legge, mai modifica)
  GAMMA/                             submodule pinned a commit di render
  papers/                            PDF letteratura citata (gitignored)
  proceedings/                       PDF atti CIM (gitignored)

wiki/                                knowledge base LLM-generated
  index.md                           catalogo (leggere prima di ogni ricerca)
  log.md                             append-only (solo main)
  sources/{papers,proceedings,gamma}/
  concepts/                          sintesi trasversali

docs/
  plans/submission-checklist.md      checklist pre-upload EasyChair
  done/

Makefile                             make paper, make works, make anonymize-check
CLAUDE.md                            schema operativo + branch policy
```

## Build

```
make paper                # compila paper/cim2026.pdf + anonymize-check
make works                # verifica completezza works/ + anonymize-check
make anonymize-check      # greppa metadati PDF per identificatori autore
make submission-works     # bundle Works per EasyChair
make submission-paper     # bundle Paper anonimizzato per EasyChair
```

## Workflow

- Modifiche **grandi** (paper.tex, Makefile, ingest fonti, bump submodule): feature branch + PR
- Modifiche **piccole** (typo, link, append wiki/log, .gitignore): commit diretto su main
- Mai push --force su main; mai amend di commit pushati
- Mai commit di PDF non anonimizzati sotto `paper/` o `works/`

Dettagli completi in [CLAUDE.md](CLAUDE.md).

## Riferimenti

- Call works: https://musel.consaq.it/cim2026/info-autori/works/
- Templates: https://musel.consaq.it/cim2026/cim2026-submission-templates/
- Date: https://musel.consaq.it/cim2026/date-importanti/
- EasyChair: https://easychair.org/conferences/?conf=xxvcim2026
- Repo opera/codice (Repository URL per il form): https://github.com/DMGiulioRomano/GAMMA

## Vincoli chiave

- Categoria A: Electroacoustic composition on fixed media
- Audio: 48 kHz / 24-bit, 1-8 canali (Gamma: stereo), ≤ 12 min
- Lingua submission: EN
- Works NON è double-blind (compositore identificato nel form). Paper sì.
- Max 1 opera per autore
