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
