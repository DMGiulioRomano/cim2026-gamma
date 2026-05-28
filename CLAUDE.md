# CLAUDE.md

Questo file fornisce guida operativa a Claude Code (claude.ai/code) per lavorare in questo repository.

## Cosa è questo repository

Repository di **doppia submission** per il **XXV CIM 2026** (Colloquio di Informatica Musicale), L'Aquila, 13-16 ottobre 2026.

Autore: Giulio Romano De Mattia.

Opera: **Gamma** — composizione elettroacustica su supporto fisso, generata via sistema YAML→Csound del repo separato [GAMMA](https://github.com/DMGiulioRomano/GAMMA) (vendored in `raw/GAMMA/` come submodule).

**Due track di submission:**

| Track | Cosa | Deadline | Materiale | Lingua |
|-------|------|----------|-----------|--------|
| **Works** | Composizione elettroacustica fixed media (Categoria A) | **29 maggio 2026** | `application_form_filled.pdf` (anonimizzato) + WAV stereo 48k/24bit su Drive/Dropbox + partitura tecnica | EN |
| **Paper** | Comunicazione orale 6-8 pp double-blind che descrive l'opera | **21 giugno 2026** | `paper/cim2026.pdf` anonimizzato | EN (raccomandato) o IT con abstract EN |

EasyChair: https://easychair.org/conferences/?conf=xxvcim2026

Repo riferimento sorella (solo paper, stesso autore): `../cim2026-granular-engine-paper`. Convenzioni operative ispirate ma adattate per doppia submission e anchoring riproducibile audio→commit.

---

## Repository structure

```
cim2026-gamma/
├── CLAUDE.md                              ← questo file (schema operativo)
├── README.md                              ← overview pubblica
├── Makefile                               ← `make paper`, `make works`, `make anonymize-check`
├── .gitmodules                            ← raw/GAMMA submodule
├── .vscode/settings.json                  ← semantic tokens PGE
├── paper/
│   ├── CIM2026_LaTeX_template_paper_v3/   ← template ufficiale, INTOCCATO
│   ├── cim2026.tex                        ← sorgente paper (derivato dal template)
│   ├── refs.bib                           ← bibliografia (gestita da Zotero + Better BibTeX)
│   └── figures/                           ← figure paper
├── works/
│   ├── cim2026_template_works_en_v2.{odt,pdf}   ← template ufficiale, riferimento
│   ├── application_form_filled.odt        ← form compilato, modificabile
│   ├── application_form_filled.pdf        ← form anonimizzato per EasyChair
│   ├── audio_link.txt                     ← URL + commit + tag + SHA256 WAV
│   └── partitura.pdf                      ← documento tecnico/plot
├── raw/                                   ← sorgenti immutabili (LLM legge, mai modifica)
│   ├── GAMMA/                             ← submodule pinned a commit specifico
│   ├── papers/                            ← PDF letteratura citata (gitignored)
│   └── proceedings/                       ← PDF atti CIM (gitignored)
├── wiki/                                  ← knowledge base LLM-generated (LLM scrive, umano legge)
│   ├── index.md                           ← catalogo: leggere prima di ogni ricerca
│   ├── log.md                             ← append-only operazioni (SOLO main)
│   ├── sources/
│   │   ├── bibliography.md                ← tracking Zotero ↔ refs.bib ↔ sezioni paper
│   │   ├── papers/                        ← una pagina per PDF in raw/papers/
│   │   ├── proceedings/                   ← una pagina per paper CIM citato
│   │   └── gamma/                         ← una pagina per modulo GAMMA analizzato
│   └── concepts/                          ← sintesi trasversali (poetica, granular, etc.)
├── docs/
│   ├── plans/
│   │   └── submission-checklist.md        ← checklist firmata pre-upload EasyChair
│   └── done/
└── inbox/                                 ← staging area ingest paper (gitignored)
```

**Separazione layer:**
- `raw/` = sorgenti immutabili — PDF, submodule. Mai modificati.
- `wiki/` = knowledge base derivata — sintesi, cross-reference. LLM scrive; umano legge.
- `CLAUDE.md` = schema — convenzioni struttura + workflow operativi.
- `paper/` e `works/` = artefatti di submission.

**Wiki usage:** sempre leggere `wiki/index.md` prima di cercare. Dopo ogni operazione sostanziale: aggiornare `index.md` e appendere a `log.md`.

---

## Tesi paper (placeholder, da elaborare)

Il paper descrive l'opera **Gamma** e il workflow YAML→Csound che la genera. Angolazione probabile (da consolidare durante scrittura):

- Poetica della composizione differita nel pipeline YAML→SCO→AIF
- Ruolo della partitura grafica (CompositionDebugger di GAMMA) come strumento compositivo, non solo di debug
- Relazione fra DSL parametrico, partitura visuale e ascolto come triangolazione decisionale
- Posizionamento rispetto a precursori CIM (granulazione offline, tempo differito, controllo parametrico gerarchico)

Il paper NON è una descrizione tecnica del sistema GAMMA: è un paper compositivo che usa GAMMA come strumento e materiale per argomentare una postura. Lo sviluppo della tesi vive in `wiki/concepts/poetica.md` (da scrivere).

Non formulare mai come "è meglio fare così". La postura è personale e situata.

---

## Vincoli CIM 2026 — Paper (Call for Papers)

Hard requirements del template `paper/CIM2026_LaTeX_template_paper_v3/`:

- **6-8 pagine** (comunicazione orale).
- A4 portrait. Text area 17.2 × 25.2 cm. Margini: top 2.0 cm, bottom 2.5 cm, left/right 1.9 cm.
- Due colonne, 8.2 cm ciascuna, gutter 0.8 cm.
- Body: Times New Roman 10 pt. Title: 16 pt bold caps. Section heads: 12 pt bold centered.
- No header/footer/page number (aggiunti dall'editor proceedings).
- Copyright notice 8 pt Times New Roman bottom-left p.1 (via `\blfootnote` nel template).
- Refs numerate `[1]`, ordine alfabetico.
- **Double-blind:** PDF sottomesso anonimizzato. No nome autore, affiliazione, link repo riconoscibili. Per self-reference: "the submitted composition", "the described system [anonymous]".
- Lingua: IT o EN. Se IT, abstract EN obbligatorio.
- Abstract: 150-200 parole.

---

## Vincoli CIM 2026 — Works (Call for Works)

Dal bando https://musel.consaq.it/cim2026/info-autori/works/ e template `works/cim2026_template_works_en_v2.odt`:

- **Categoria A:** Electroacoustic composition on fixed media.
- Audio: **48 kHz / 24-bit**, **1-8 canali** accettati (Gamma: stereo 2 ch), **≤ 12 min**.
- Form compilato in EN, compositore identificato (Works NON è double-blind).
- Max 1 opera per autore.
- WAV su host esterno (Drive/Dropbox/WeTransfer); URL nel form.

**Nota anonimato:** il bando Works NON menziona requisiti di anonimato (a differenza del Paper, esplicitamente double-blind). Il form chiede esplicitamente i dati del compositore. Quindi: nessuna anonimizzazione applicata a `works/application_form_filled.pdf`, `works/audio_link.txt`, link Drive, metadati WAV.

---

## Branch e commit policy

Single-author repo ma con doppio binario di submission e materiali sensibili (anonimizzazione, SHA256 audio, submodule pin). Workflow misto.

### LARGE → feature branch + PR + merge su main

Naming `<categoria>/<topic>` o `<categoria>/<identifier>`:

- `paper/<topic>` — edit sezioni di `paper/cim2026.tex` (es: `paper/sezione-3-architettura`)
- `works/<topic>` — modifiche a materiali Works (es: `works/form-anonimizzazione`)
- `wiki/<autore-anno>` — nuova ingest source (es: `wiki/truax-1988`)
- `wiki/<concept>` — nuova concept page (es: `wiki/concepts-poetica`)
- `submodule/gamma@<short-sha>` — bump submodule GAMMA (es: `submodule/gamma@a1b2c3d`)
- `audio/render-<YYYY-MM-DD>` — nuovo render del WAV
- `fix/<topic>` — bugfix generico

Flow: `git checkout -b <branch>` → commit → `git push -u origin <branch>` → `gh pr create` → merge.

### SMALL → commit diretto su main

- Typo fix in qualsiasi file
- Estensioni `.gitignore` non controverse
- Update link in README
- Append a `wiki/log.md` (SOLO su main, evita conflitti append)
- Append a `wiki/sources/bibliography.md` (riga tabella)
- Note in `docs/plans/`
- Update `wiki/index.md` come entry

### Regole rigide

- **Mai** `git push --force` su `main`
- **Mai** amend di commit già pushati
- `wiki/log.md` modificato **solo su main** (append-only, conflitti di merge sono pessimi su file lineare)
- **Submodule bump dopo render del WAV** invalida la SHA256 in `works/audio_link.txt`: richiede conferma esplicita utente, branch dedicato, e re-render + nuovo SHA256 nello stesso PR
- Mai committare `paper/cim2026.pdf` non anonimizzato (vedi sezione Anonimizzazione)
- `paper/cim2026.pdf` e `works/application_form_filled.pdf` gitignored di default (rigenerati da sorgenti)

---

## Submodule policy — `raw/GAMMA`

Tre anchor indipendenti per riproducibilità audio→commit:

1. **Tag annotato in repo GAMMA:** `cim2026-submission` sul commit usato per render del WAV sottomesso. Tag, non branch (i branch driftano).
2. **Gitlink commit in `.gitmodules` parent:** source of truth del commit pinned. Nessun campo `branch =` (mirror riferimento; altrimenti invita drift via `submodule update --remote`).
3. **`works/audio_link.txt` strutturato** con commit SHA + tag + ISO date render + SHA256 WAV uploadato.

### Setup iniziale

```bash
git submodule add https://github.com/DMGiulioRomano/GAMMA.git raw/GAMMA
git submodule update --init --recursive
cd raw/GAMMA && git checkout <commit-render> && cd ../..
git add .gitmodules raw/GAMMA
git commit -m "submodule: pin raw/GAMMA at <short-sha> for cim2026 render"
```

### Clone fresh

```bash
git clone --recurse-submodules <url>
# oppure
git clone <url> && cd cim2026-gamma && git submodule update --init --recursive
```

### Bump submodule

Solo via branch `submodule/gamma@<short-sha>`. Se il bump è POST-render del WAV submission:
- Re-render WAV richiesto
- Aggiornare `works/audio_link.txt` con nuovo SHA256
- Nuovo tag `cim2026-submission` in repo GAMMA (force-update tag accettato SOLO se non ancora sottomesso)
- Richiede conferma esplicita utente

---

## Anonimizzazione — solo Paper (Works NON è double-blind)

Solo il track Paper richiede anonimizzazione (peer review double-blind). Works identifica esplicitamente il compositore nel form. Quindi i livelli sotto si applicano solo a `paper/cim2026.pdf`.

### Livello 1 — `make anonymize-check`

Greppa metadati PDF di `paper/cim2026.pdf` per identificatori autore. Esce nonzero se trovati. Chiamato come last step di `make paper`.

Pattern bloccati: `De Mattia`, `Giulio`, `DMGiulioRomano`, `giuliodemattia`. La lista vive nel Makefile (target `anonymize-check`).

### Livello 2 — Pre-commit hook

Check su qualsiasi `.pdf` sotto `paper/` in stage. Blocca commit se match trovato. Setup da definire (hook diretto in `.git/hooks/pre-commit`).

### Livello 3 — Checklist firmata

`docs/plans/submission-checklist.md`: lista datata firmata prima di upload Paper. Coprire metadati PDF, refs anonimizzate, toggle LaTeX `\anonymoustrue`.

### Toggle LaTeX

`paper/cim2026.tex` definisce `\newif\ifanonymous\anonymoustrue`. Wrapping su `\author{}`, `\thanks{}`, self-citation del repo GAMMA, link footnote. A camera-ready: flip a `\anonymousfalse`.

### Self-citation paper

"Gamma" è nome dell'opera ma è anche self-identifier dell'autore (`github.com/DMGiulioRomano/GAMMA`). Durante review paper usare:
- "the submitted composition" anziché "Gamma"
- "the system [anonymous]" anziché "GAMMA"
- footnote URL repo: solo `[repository URL withheld for double-blind review]`

---

## Build

```bash
make paper          # compila paper/cim2026.pdf con anonymize-check
make works          # verifica completezza works/ + anonymize-check
make anonymize-check
make submission-works   # bundle deliverable Works per EasyChair
make submission-paper   # bundle deliverable Paper per EasyChair
make wiki-lint
make clean
```

Output non-tracked: `paper/cim2026.pdf`, file aux LaTeX, bundle submission.

---

## Bibliography

Gestione con **Zotero + Better BibTeX**.

- `paper/refs.bib` — generato da Zotero, fonte di verità per LaTeX. **Non modificare a mano.** Incluso in `cim2026.tex` con `\bibliography{refs}`.
- `wiki/sources/bibliography.md` — tabella di tracking: chiave BibTeX ↔ stato ingest wiki ↔ sezioni paper.
- PDF citati in `raw/papers/` (gitignored), importati anche in Zotero.
- Proceedings CIM in `raw/proceedings/` (gitignored), aggiunti a Zotero manualmente post-ingest.

Chiavi BibTeX formato: `Cognome1Anno` / `CognomeCognome1Anno` / suffisso disambiguante. Stesse chiavi in wiki, `cim2026.tex`, `bibliography.md`.

---

## Wiki (knowledge base)

Tre layer: `raw/` (immutabile) → `wiki/` (LLM-generated) → `CLAUDE.md` (schema).

### Struttura

- `wiki/index.md` — catalogo, leggere prima di ogni ricerca
- `wiki/log.md` — append-only, una entry per sessione (SOLO main)
- `wiki/sources/bibliography.md` — tracking table
- `wiki/sources/papers/<autore-anno>.md` — una pagina per PDF in `raw/papers/`
- `wiki/sources/proceedings/<autore-anno>.md` — una pagina per paper CIM citato
- `wiki/sources/gamma/<modulo>.md` — una pagina per modulo GAMMA analizzato
- `wiki/concepts/` — sintesi trasversali (poetica, granular technique, decorrelazione, partitura grafica)

### Workflow ingest — paper PDF

1. Read PDF con Read tool
2. Scrivere summary in `wiki/sources/papers/<autore-anno>.md` con schema fisso:

```markdown
# [Autore, Anno] Titolo completo

## Citazione CIM
[formato: Autore, A. (anno). Titolo. *Rivista*, vol(n), pp.]

## Argomento centrale
[1-2 frasi: cosa afferma il paper]

## Gap o problema identificato
[cosa manca o resta aperto secondo l'autore]

## Rilevanza diretta per Gamma
[come Gamma o GAMMA si posiziona rispetto a questo paper]

## Collegamento alla tesi centrale
[come il paper si lega alla poetica della composizione, partitura grafica,
DSL parametrico, o uno degli angoli del paper CIM 2026]

## Sezioni del paper CIM 2026 dove citare
[es: sezione 1 Introduzione, sezione 2 Granular, related work]

## Quote chiave
[max 2-3 frasi verbatim rilevanti, con numero pagina]
```

3. Se introduce elementi nuovi per tesi o precursori: aggiornare `wiki/concepts/<concept>.md` rilevanti
4. Aggiornare colonna Wiki in `wiki/sources/bibliography.md`
5. Aggiornare `wiki/index.md` con nuova entry
6. Appendere a `wiki/log.md` (su main, dopo merge)

### Workflow ingest — paper proceedings CIM

Identico a paper PDF ma in `wiki/sources/proceedings/<autore-anno>.md` con sezioni extra: "Categoria e lunghezza", "Sistema o strumento descritto", "Analogia con Gamma", "Posizionamento storico", "Note stilistiche".

### Workflow ingest — modulo GAMMA

1. Leggere sorgente da `raw/GAMMA/`
2. Scrivere analisi in `wiki/sources/gamma/<modulo>.md`:

```markdown
# [NomeModulo] — analisi

## Ruolo nell'architettura
[posizione nella pipeline YAML→Csound]

## Classi/funzioni principali
[per ogni: attributi, metodi, pattern usato]

## Comportamento runtime
[flusso dati, decisioni, side effects]

## Collegamento alla tesi paper CIM 2026
[come il modulo materializza un aspetto della tesi compositiva]

## Sezioni paper CIM 2026 dove descrivere
[es: sezione 3 Architettura, sezione 4 Partitura grafica]

## Domande aperte
[da verificare con autore o lettura ulteriore]
```

3. Aggiornare `wiki/index.md` e `log.md`

### Workflow query

1. Read `wiki/index.md` per trovare pagine rilevanti
2. Read pagine identificate
3. Sintesi con citazioni alle pagine wiki
4. **Ogni risposta sostanziale = nuovo ingest.** Archiviare come pagina wiki (concepts/, sources/). Esplorazioni compoundano la KB come i sorgenti.

### Workflow lint

`make wiki-lint` o manuale. Check:
- Pagine orfane (no link in entrata)
- Contraddizioni tra pagine
- Claim obsoleti superati da fonti più recenti
- Concetti citati ma senza pagina propria
- Gap di fonti (paper non ingestiti, moduli GAMMA non analizzati)

### Workflow add-paper

Aggiunge PDF da `inbox/` a `raw/papers/`, genera entry BibTeX, aggiorna `refs.bib` e `wiki/sources/bibliography.md`.

Nomenclatura filename:
- 1 autore: `Truax_1988_Real-Time-Granular-Synthesis.pdf`
- 2 autori: `DePoli-Piccialli_1988_Forme-Onda-Sintesi.pdf`
- 3+ autori: `Roads_2021_Architecture-Real-Time-Granular.pdf` (solo primo)
- Cognomi composti: concatenati senza spazio (`DePoli`, `DiScipio`)
- Titolo: 6-8 parole significative, ASCII

Chiave BibTeX: `Cognome1Anno`.

Step:
1. Scansiona `inbox/`
2. Per ogni PDF: leggere prime 4 pp, estrarre metadati (autori, anno, titolo, venue, DOI)
3. Verifica via Crossref API (`https://api.crossref.org/works/<DOI>`) o web search
4. Costruisci entry BibTeX (stile Better BibTeX, file path assoluto)
5. Conferma utente
6. Sposta PDF in `raw/papers/<FILENAME>.pdf`, appendi a `refs.bib`, aggiungi riga in `bibliography.md` con stato `✗` (non ancora ingestito)

A workflow completato `inbox/` vuota.

---

## Lingua

- CLAUDE.md, README, wiki, commit, branch name, `docs/plans/`: **Italiano**
- Paper CIM (`paper/cim2026.tex`): preferenza **English** (visibilità). Se IT: abstract EN obbligatorio
- Works form (`works/application_form_filled.odt`): **English** (richiesto dal bando)
- Commit messages: italiano, imperativo presente (`aggiungi`, `correggi`, `aggiorna`), max 72 char subject

## Convenzioni generali

- Mai emoji nei file tracked
- Mai commit di PDF non anonimizzati sotto `paper/` o `works/`
- Mai modificare file in `raw/` (eccetto `git submodule update`)
- Mai modificare il template ufficiale in `paper/CIM2026_LaTeX_template_paper_v3/` (riferimento immutabile)
- File generati (PDF paper, bundle, aux LaTeX, .venv): gitignored

---

## Riferimenti esterni

- Bando CIM 2026: https://musel.consaq.it/cim2026/
- Call works: https://musel.consaq.it/cim2026/info-autori/works/
- Templates: https://musel.consaq.it/cim2026/cim2026-submission-templates/
- Date: https://musel.consaq.it/cim2026/date-importanti/
- EasyChair: https://easychair.org/conferences/?conf=xxvcim2026
- Repo opera: https://github.com/DMGiulioRomano/GAMMA
- Repo sorella (riferimento operativo): `../cim2026-granular-engine-paper`
