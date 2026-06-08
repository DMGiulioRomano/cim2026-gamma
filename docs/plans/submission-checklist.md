# Submission checklist — Paper CIM 2026 (Gamma)

Checklist da firmare e datare **prima** dell'upload del Paper su EasyChair
(deadline 21 giugno 2026). Il track Paper è double-blind: ogni voce di
anonimizzazione è bloccante. Works NON è coperto (non anonimo, vedi CLAUDE.md).

## Stato corrente (2026-06-08, draft)

- Paper compila: `make paper` → `cim2026.pdf` (4 pp, in crescita verso 6-8).
- `make anonymize-check`: **OK** (metadati + testo PDF puliti).
- Toggle `\anonymoustrue` attivo in `paper/cim2026.tex`.
- `paper/refs.bib`: 8 chiavi seed (5 mancanti, stato `✗`, da ingestire).

## Anonimizzazione (bloccante, double-blind)

- [ ] `\anonymoustrue` attivo in `cim2026.tex` (NON `\anonymousfalse`).
- [ ] `\author` / affiliazione / email soppressi (autore = "Anonymous").
- [ ] Nessun "the submitted composition" sostituito con titolo riconoscibile;
      "Gamma" usato solo come nome opera, mai come self-identifier del repo.
- [ ] Self-citation del repo GAMMA: nessun link `github.com/DMGiulioRomano`,
      nessun "[anonymous]" rimasto scoperto.
- [ ] `make anonymize-check` esce 0 (metadati PDF + testo).
- [ ] Ispezione manuale metadati: `pdfinfo cim2026.pdf` — Author/Producer/Title
      privi di identificatori (De Mattia, Giulio, DMGiulioRomano, giuliodemattia).
- [ ] Nessuna figura con watermark/path autore (controllare i 3 PDF in
      `paper/figures/`).

## Conformità template (bloccante)

- [ ] 6-8 pagine (comunicazione orale). **Attuale: da completare.**
- [ ] A4 portrait, due colonne, Times 10 pt (dallo .sty template).
- [ ] Abstract 150-200 parole (EN). **Attuale: ~190, ok.**
- [ ] Refs numerate, ordine alfabetico, tutte citate nel testo.
- [ ] Nessun header/footer/numero pagina aggiunto a mano.
- [ ] Copyright notice 8 pt bottom-left p.1 (dal template, resta neutro in anon).

## Contenuto (qualità)

- [ ] 5 fonti mancanti ingestite o citate come "[source to be retrieved]"
      coerentemente (Bidlack, Branchi, Roads, Anderson, Koenig).
- [ ] Sezione Branchi (pitagorica) sviluppata dopo reperimento fonte.
- [ ] Pass `humanizer` / `no-ai-slop` sulla prosa EN finale.

## Firma

- Data upload: __________
- Firma: __________
- SHA256 PDF caricato: __________
