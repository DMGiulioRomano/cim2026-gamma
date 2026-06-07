# Wiki index — cim2026-gamma

Catalogo della knowledge base. Leggere questa pagina **prima di ogni ricerca** per identificare quali pagine sono rilevanti per la query.

Convenzione: dopo ogni ingest, aggiungere una riga sotto la sezione appropriata con sintesi ≤ 2 righe.

---

## Bibliography

- [bibliography.md](sources/bibliography.md) — tabella tracciamento chiavi BibTeX ↔ stato ingest ↔ sezioni paper

## Sources — papers letteratura

PDF in `raw/papers/` (gitignored). Una pagina per PDF letto, schema fisso (vedi `CLAUDE.md > Workflow ingest paper PDF`).

- [discipio-1990](sources/papers/discipio-1990.md) — mappa logistica come generatore formale e timbrico (ICMC Glasgow 1990); fondamento genealogico diretto per Gamma.
- [discipio-1999](sources/papers/discipio-1999.md) — formalizzazione FIS con sine map, texture ambientali; distinzione scala-campione vs. scala-partitura centrale per tesi.
- [discipio-2001](sources/papers/discipio-2001.md) — versione consolidata FIS su Leonardo/MIT Press; paper più citabile della serie, attitudine empirica/ecologica.

## Sources — proceedings CIM

PDF Atti in `raw/proceedings/` (gitignored): XI CIM 1995 (258 pp), XVI CIM 2006
(34 pp, parziale). Una pagina per paper CIM individualmente letto.

- [discipio-1995](sources/proceedings/discipio-1995.md) — granulazione ricorsiva `x[n+1]=f_b(f_a(x[n]))`, microcomposizione, emergenza; Lab Musica e Sonologia L'Aquila.
- [prignano-1995](sources/proceedings/prignano-1995.md) — functional iteration synthesis, mappa seno iterata, spazio delle fasi/biforcazione; stesso lab L'Aquila.
- [leach-1995](sources/proceedings/leach-1995.md) — composizione algoritmica come gene expression: grammatica context-sensitive che "cresce da una cellula".
- [rizzuti-2006](sources/proceedings/rizzuti-2006.md) — "caos sonoro": sintesi granulare via iterazione funzioni non lineari + mappa logistica in CSound, no random. Match più stretto.
- [bottoni-2006](sources/proceedings/bottoni-2006.md) — Multimedia LaB: loop differito assioma→regole→riscrittura, linguaggio musicale formale (DSL/CAC).

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
- [precursori](concepts/precursori.md) — related work per asse: Di Scipio/Bidlack (caos), Branchi (pitagorica), Koenig (tendenza), Roads (tempo differito), ISO 226; Atti CIM scaricati.

---

## Log

Cronologia operazioni: [log.md](log.md). Append-only, modificato solo su `main`.
