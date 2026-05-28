# Submission checklist — EasyChair upload

Una checklist datata/firmata per OGNI upload (Works + Paper). Stampare/copiare in fondo, completare, salvare in `docs/done/` come `submission-<track>-<YYYY-MM-DD>.md` dopo upload.

Regola: **nessun upload prima che ogni voce sia spuntata**. `make anonymize-check` deve passare immediatamente prima.

---

## Track Works — deadline 29 maggio 2026

**Nota:** Works track NON è double-blind. Compositore identificato esplicitamente nel form. Nessuna anonimizzazione richiesta.

### Pre-flight

- [ ] `works/application_form_filled.odt` compilato in inglese
- [ ] Tutti i campi richiesti dal bando compilati (titolo, durata, anno, descrizione, biografia compositore)
- [ ] Export PDF da LibreOffice
- [ ] `works/application_form_filled.pdf` esiste

### Audio

- [ ] WAV stereo 48 kHz / 24-bit
- [ ] Durata ≤ 12 minuti
- [ ] WAV uploadato su Drive/Dropbox/WeTransfer con link condivisibile pubblicamente
- [ ] URL del file inserito nel form
- [ ] `works/audio_link.txt` compilato:
  - [ ] `url:` URL host esterno
  - [ ] `commit:` SHA del commit GAMMA usato per render
  - [ ] `tag:` cim2026-submission (tag annotato in repo GAMMA)
  - [ ] `rendered:` data ISO render
  - [ ] `sha256:` hash WAV uploadato
- [ ] `shasum -a 256 <path-WAV-locale>` matcha riga `sha256:` di `audio_link.txt`
- [ ] Link funzionante in incognito/browser pulito

### Submodule anchoring

- [ ] `cd raw/GAMMA && git tag` mostra `cim2026-submission`
- [ ] Tag pinned su commit corrispondente al render
- [ ] Tag pushato su `origin/GAMMA` (`cd raw/GAMMA && git push origin cim2026-submission`)
- [ ] `git submodule status` in parent mostra commit pinned matching

### Bundle

- [ ] `make submission-works` genera `submission/Gamma_*` senza errori
- [ ] Verifica visiva del contenuto bundle

### Upload

- [ ] EasyChair login: https://easychair.org/conferences/?conf=xxvcim2026
- [ ] Form compilato; PDF allegato; link audio verificato
- [ ] Submission ID annotato sotto:

```
Submission Works ID: ____________
Data upload:        ____________
Firma:              ____________
```

---

## Track Paper — deadline 21 giugno 2026

### Pre-flight

- [ ] `paper/cim2026.tex` completo, 6-8 pagine effettive
- [ ] Abstract 150-200 parole (verificato con `pdftotext` + word count)
- [ ] Almeno 9 riferimenti bibliografici (target 9-21 per category CIM tool/system)
- [ ] Figure leggibili in B&W (test stampa monocromatica)
- [ ] `paper/refs.bib` aggiornato da Zotero
- [ ] `make paper` produce `paper/cim2026.pdf` senza warning critici

### Anonimizzazione

- [ ] Toggle LaTeX `\anonymoustrue` attivo in `cim2026.tex`
- [ ] `\author{}` mostra solo placeholder anonimo (nessun nome)
- [ ] `\thanks{}` vuoto/anonimizzato
- [ ] Tutte le self-citation a GAMMA usano `[anonymous]` o `[repository URL withheld]`
- [ ] Nessuna URL `github.com/DMGiulioRomano/...` visibile nel PDF
- [ ] Acknowledgments anonimizzati o assenti
- [ ] `pdfinfo paper/cim2026.pdf` non rivela identità
- [ ] `pdftotext paper/cim2026.pdf - | grep -iE 'De Mattia|Giulio|DMGiulioRomano'` vuoto
- [ ] `make anonymize-check` passa

### Verifica formato CIM

- [ ] A4 portrait, due colonne 8.2 cm, gutter 0.8 cm
- [ ] Body Times 10 pt, Title 16 pt bold caps
- [ ] Copyright notice 8 pt bottom-left p.1 (`\blfootnote`)
- [ ] No header/footer/page number
- [ ] References numerate `[1]`, ordine alfabetico

### Bundle

- [ ] `make submission-paper` genera `submission/Gamma_paper_anonymous.pdf`

### Upload

- [ ] EasyChair login: https://easychair.org/conferences/?conf=xxvcim2026
- [ ] Submission ID annotato sotto:

```
Submission Paper ID: ____________
Data upload:         ____________
Firma:               ____________
```

---

## Post-upload

- [ ] Copia di questo file in `docs/done/submission-<track>-<YYYY-MM-DD>.md`
- [ ] Append a `wiki/log.md` (su main): `## YYYY-MM-DD — submission` con tipo + ID
