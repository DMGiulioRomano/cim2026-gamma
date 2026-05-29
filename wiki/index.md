# Wiki index — cim2026-gamma

Catalogo della knowledge base. Leggere questa pagina **prima di ogni ricerca** per identificare quali pagine sono rilevanti per la query.

Convenzione: dopo ogni ingest, aggiungere una riga sotto la sezione appropriata con sintesi ≤ 2 righe.

---

## Bibliography

- [bibliography.md](sources/bibliography.md) — tabella tracciamento chiavi BibTeX ↔ stato ingest ↔ sezioni paper

## Sources — papers letteratura

PDF in `raw/papers/` (gitignored). Una pagina per PDF letto, schema fisso (vedi `CLAUDE.md > Workflow ingest paper PDF`).

_(nessuna fonte ingestita)_

## Sources — proceedings CIM

PDF in `raw/proceedings/` (gitignored). Una pagina per paper CIM individualmente letto.

_(nessuna fonte ingestita)_

## Sources — moduli GAMMA

Submodule in `raw/GAMMA/`. Una pagina per modulo analizzato per il paper.

Il submodule GAMMA ha **una propria wiki per-modulo** in `raw/GAMMA/wiki/` (immutabile): `includes/eventoSonoro.md`, `voce.md`, `initIsoAmp.md`, `GenPythagFreqs.md`, `NonlinearFunc.md`, `pfield_comp.md`, `concepts/maschera_tendenza.md`, `composizioni/Gamma.md`. Le concept page qui sotto **sintetizzano** quei moduli nell'ottica della tesi paper/works; per il dettaglio implementativo per-modulo rimandano alla wiki GAMMA.

_(nessuna pagina sources/gamma dedicata: la sintesi vive in Concepts)_

## Concepts

Sintesi trasversali che attraversano più moduli GAMMA, orientate alla tesi compositiva.

- [ritmo-generatore](concepts/ritmo-generatore.md) — il valore ritmico come parametro generatore unico: pilota tempo, altezza, spazio (Mid/Side) e ampiezza.
- [mappa-logistica](concepts/mappa-logistica.md) — il ritmo si autogenera per feedback non lineare (mappa logistica); lettura lookup che ricava l'input dal proprio output.
- [accordatura-pitagorica](concepts/accordatura-pitagorica.md) — nube pitagorica a 200 intervalli/ottava (eredità Branchi); zone di battimento emergenti.
- [compensazione-isofonica](concepts/compensazione-isofonica.md) — dinamica percettiva in Phon via ISO 226:2003; ampiezza a valle dell'altezza.
- [stato-musicale](concepts/stato-musicale.md) — maschere di tendenza, stato statico vs transizione, i due strati ritmici (macro/micro).
- [poetica](concepts/poetica.md) — tesi compositiva: stati in transizione, emergenza, tempo differito (in costruzione).

---

## Log

Cronologia operazioni: [log.md](log.md). Append-only, modificato solo su `main`.
