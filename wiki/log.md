# Log operazioni

Append-only. Una entry per sessione/operazione, formato:

```
## YYYY-MM-DD HH:MM — <tipo>
<descrizione 1-3 righe>
```

Modificato **solo su `main`** (mai da feature branch — i conflitti di merge su file append-only sono pessimi).

Tipi:
- `bootstrap` — setup iniziale repo
- `ingest paper` — nuova pagina in `wiki/sources/papers/`
- `ingest proceedings` — nuova pagina in `wiki/sources/proceedings/`
- `ingest gamma` — analisi modulo in `wiki/sources/gamma/`
- `concept` — nuova/aggiornata pagina in `wiki/concepts/`
- `submodule bump` — bump di `raw/GAMMA`
- `render` — nuovo render WAV submission
- `submission` — upload EasyChair completato
- `refactor` — modifica struttura repo

---

## 2026-05-28 — bootstrap
Setup struttura repo: CLAUDE.md (schema operativo + branch policy + 3 livelli anonimizzazione), Makefile (paper/works/anonymize-check/submission/wiki-lint), submodule `raw/GAMMA` pinned a `b070e1a`, skeleton wiki/sources e wiki/concepts, docs/plans/submission-checklist.md, .gitignore esteso. Branch `bootstrap/repo-structure`.

## 2026-05-29 15:50 — concept
Costruite 6 concept page in `wiki/concepts/` (ritmo-generatore, mappa-logistica, accordatura-pitagorica, compensazione-isofonica, stato-musicale, poetica): sintesi del sistema generativo GAMMA citata a riga di sorgente (`raw/GAMMA/`). Verificato dal sorgente: il ritmo è parametro generatore unico (tempo/altezza/spazio M-S/ampiezza), autogenerato per mappa logistica; pitagorica a 200 intervalli/ottava (fondamentale 32 Hz); ISO 226:2003 già documentata nella wiki GAMMA `initIsoAmp.md`, qui sintetizzata. Hanno alimentato il draft EN della Work presentation (1797 char). Merge branch `works/drop-partitura` → main.

## 2026-06-04 — concept
Fix tecnici: init submodule `raw/GAMMA` (checkout `bf117d4`, tag `cim2026-submission`), eliminato branch stale `works/drop-partitura` (già merged). Ricerca web precursori per i sei assi di Gamma → nuova concept `wiki/concepts/precursori.md`: Di Scipio + Bidlack (caos/mappa logistica), Branchi (nube pitagorica, *Intero*), Koenig Project 1/2 (maschere di tendenza), Roads *Microsound* (tempo differito), ISO 226 (compensazione isofonica); asse "variabile unica → 4 dimensioni" senza match stretto → candidato a contributo. 8 chiavi candidate in `bibliography.md` (stato `✗`). Scaricati Atti CIM XI 1995 (258 pp) e XVI 2006 (34 pp parz.) in `raw/proceedings/` (gitignored); fonti primarie non auto-scaricabili tracciate in `docs/plans/fonti-da-reperire.md`. Merge branch `wiki/concepts-precursori` → main.

## 2026-06-07 — ingest paper
Ingestiti 3 PDF Di Scipio da `inbox/` in `raw/papers/`. Rinominati secondo convenzione (rimosso nome proprio, aggiunto anno): `DiScipio_1990_Composition-by-Exploration-of-Non-Linear-Dynamic-Systems.pdf`, `DiScipio_1999_Synthesis-of-Environmental-Sound-Textures-by-Iterated-Nonlinear-Functions.pdf`, `DiScipio_2001_Iterated-Nonlinear-Functions-as-a-Sound-Generating-Engine.pdf`. Pagine wiki create in `wiki/sources/papers/`: discipio-1990 (ICMC Glasgow, precursore genealogico diretto), discipio-1999 (DAFx99, formalizzazione FIS con sine map), discipio-2001 (Leonardo/MIT Press Vol. 34 No. 3, versione consolidata FIS + attitudine ecologica). Aggiornati bibliography (stato ✓, 3 nuove chiavi) e index. `inbox/` svuotata.

## 2026-06-04 — ingest proceedings
Spogliati i due Atti CIM scaricati e ingestiti i 5 paper più vicini a Gamma in `wiki/sources/proceedings/`: Rizzuti 2006 ("Il caos sonoro": sintesi granulare via iterazione di funzioni non lineari + mappa logistica in CSound, senza random — match più stretto), Prignano 1995 (functional iteration synthesis, mappa seno iterata), Di Scipio 1995 (granulazione ricorsiva `x[n+1]=f_b(f_a(x[n]))`, microcomposizione, emergenza), Leach 1995 (composizione algoritmica come gene expression, grammatica context-sensitive), Bottoni et al. 2006 (Multimedia LaB, ciclo differito assioma→regole→riscrittura, linguaggio formale). Scoperta: Di Scipio e Prignano operano entrambi al Laboratorio Musica e Sonologia di L'Aquila (città del CIM 2026) → genealogia locale di sintesi per iterazione non lineare. Aggiornati precursori, index, bibliography (stato ✓), plan fonti. Da spogliare ancora: Belladonna 1995, Di Scipio 1995 (Riflessioni), Liuni-Morelli 2006. Merge branch `wiki/ingest-proceedings-cim` → main.

## 2026-06-07 — concept
Verifica copertura wiki GAMMA per il paper: solida su pipeline/poetica/maschere/ritmo/pitagorica/isofonica, due buchi reali. Colmato #1 con `wiki/concepts/partitura-grafica.md`: analisi di `CompositionDebugger` (raw/GAMMA/generative_composerYaml2.py:L958-1356) come strumento compositivo (angolo #2 del paper) — tre assi (altezza/durata, dinamica lineare, dinamica probabilistica), buste di tendenza vs eventi campionati, paginazione partitura, cosa NON mostra. Colmato #2 con `wiki/sources/gamma/gamma-opera.md`: struttura completa delle 6 sezioni da yaml/Gamma.yaml (timeline, durate, offset, layer/stati per sezione), durata totale ~8:05; corregge la md GAMMA stale (sez. II era `TODO`, scampanello mancante in sez. I, durata I 140→154). Scoperta: III e IV si sovrappongono per intero (offset -60). Aggiornati index + backlink poetica/stato-musicale. Merge branch `wiki/concepts-partitura-grafica` → main.

## 2026-06-07 — refactor
Ricreati in Python due grafici dai repo sorella dell'autore, come figure del paper in `paper/figures/scripts/`: `spatial_harmonics.py` (armoniche spaziali polari |sin/cos(i/2·θ)|^n lungo la circonferenza, da delta/src/delta/builder/Spazio.py — matplotlib statico + plotly interattivo con slider esponente) e `rhythmic_harmonics.py` (durata armonica suddivisa dalla serie armonica, riga i = i parti uguali, da rhythmic-harmonics/latex/main.tex TikZ → matplotlib). Output PDF tracciati (inclusi dal LaTeX), PNG/HTML gitignored. venv `.venv` con numpy/matplotlib/plotly/kaleido. README in scripts/. Merge branch `paper/figures-armoniche` → main.

## 2026-06-08 — refactor
Avviata scrittura bottom-up del paper. (1) Terza figura: `paper/figures/scripts/graphic_score.py` ricrea la partitura grafica del `CompositionDebugger` in EN, copiando GAMMA pinnato in dir temp con seed fisso (riproducibile) e render Csound saltato, poi ritaglia 1 pagina (`graphic_score.pdf`, pag. 3, 120-180s). Scoperta: la partitura del WAV Works NON è riproducibile (reso senza seed, nessuna cache) → Work e paper non condividono lo stesso render (confermato dall'autore). (2) Consolidata `wiki/concepts/poetica.md`: sezione Posizionamento (caos/Di Scipio+Bidlack, genealogia L'Aquila, eredità Branchi sospesa per fonte, tempo differito/Roads); resta sospeso solo Branchi. (3) `paper/refs.bib` seed manuale con le 8 chiavi a wiki completa (Di Scipio x4, Rizzuti, Prignano, Leach, Bottoni) dai metadati wiki; 5 chiavi `✗` mancanti da ingestire. (4) `paper/cim2026.tex`: skeleton derivato dal template (intoccato), toggle `\anonymoustrue`, abstract EN ~190 parole, 7 sezioni con contenuto sostanziale dalle concept page, 3 figure incluse, `\bibliography{refs}`. Makefile esteso con `TEXINPUTS` al template dir per trovare `cim2026.sty`. `make paper` compila (4 pp, da espandere a 6-8), `anonymize-check` OK. (5) `docs/plans/submission-checklist.md` firmabile. Branch mergiati: `paper/figura-partitura`, `wiki/concepts-poetica`, `paper/refs-bib-seed`, `paper/skeleton`. Restano: ingest 5 fonti (PDF da reperire), espansione paper a 6-8 pp.
