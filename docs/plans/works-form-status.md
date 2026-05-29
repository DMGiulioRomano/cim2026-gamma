# Works Form — stato compilazione

Aggiornato: 2026-05-29
Deadline submission Works: 29 maggio 2026 ore 23:59 (CEST, L'Aquila)
EasyChair: https://easychair.org/conferences/?conf=xxvcim2026

---

## Campi pronti (9/11)

| Campo | Valore | Stato |
|-------|--------|-------|
| Category | A. Electroacoustic composition on fixed media | ✓ |
| Title | Gamma | ✓ |
| Subtitle | _(vuoto)_ | ✓ |
| Year | 2026 | ✓ |
| Authors | Giulio Romano De Mattia | ✓ |
| Expected duration | 00:07:44 | ✓ |
| Min / Max duration | _(vuoto — durata fissa)_ | ✓ |
| Performers | _(vuoto — fixed media, no performers)_ | ✓ |
| Repository URL(s) | Audio: https://drive.google.com/file/d/1DFaRORUAwgChErPTUqlikodj9wXkLdaB/view?usp=sharing · Source: https://github.com/DMGiulioRomano/GAMMA (tag: cim2026-submission) | ✓ |
| Program notes | vedi sotto | ✓ |
| Authors' biographies | vedi sotto | ✓ |
| Performers' biographies | _(N/A — fixed media)_ | ✓ |
| Technical rider | vedi sotto | ✓ |
| **Work presentation** | **TODO — dalla wiki GAMMA** | ✗ |

---

## Program notes (EN, max 1000 char — ~700 char)

> Gamma is the primordial source from which the Delta cycle emerges.
> If Delta is the river's mouth — shaped by tributaries, sediment,
> and accumulation — then Gamma is the crystalline spring.
>
> This work brings into focus musical states in transition. Rhythmic
> structures weave an ever-shifting sonic texture from which timbral
> forms arise. As they thin and disperse, they stretch across time
> and gradually unfold as space.
>
> Here, the algorithmic essence of Delta is distilled to its most
> elemental condition — a cry becoming sound — inhabiting space in
> its purest form.
>
> Per *Intero* and Per *Lontano*

_(Nel form ODT: Delta, Gamma, Intero, Lontano in corsivo.)_

---

## Authors' biographies (EN, max 500 char)

> Giulio Romano De Mattia (Rome, 2000) is an electroacoustic music
> enthusiast. He is currently pursuing a Master's degree in
> Electronic Music at the Conservatory of L'Aquila with Agostino
> Di Scipio.

---

## Technical rider (EN, max 1000 char — ~180 char)

> Multichannel diffusion (periphonic / 3D ambisonic) preferred.
> Standard stereo playback is fully supported as a fallback. No
> specific mixer or equipment requirements.

---

## Work presentation (TODO, max 2000 char)

Spina dorsale concordata (5 blocchi, ~1850 char target):

1. **Inquadramento** (~150 char): fixed-media stereo 7'44", parte del ciclo Delta, forma ridotta/cristallina
2. **Sistema compositivo** (~400 char): pipeline YAML→Csound custom, maschere di tendenza, stato_iniziale + stato_finale, interpolazione stocastica nel lifespan
3. **Specifiche tecniche** (~500 char):
   - Accordatura pitagorica (catena di quinte 3/2 ridotta in ottava)
   - Ritmo modula pitch: stesso (ottava, registro) → note diverse a step ritmico diverso
   - Ampiezza compensata ISO 226:2003 (ppp..fff → Phon → dBFS)
   - Spazializzazione: Mid/Side orbitale per evento
4. **Struttura formale** (~500 char): 6 sezioni 14 layer — I. Nascita Lenta di Cluster · II. Solo ripresaglissante · III–VI. [da rinominare via issue GAMMA #2]
5. **Postura compositiva** (~300 char): loop di feedback lungo — specifica → render offline → ascolto → riscrittura. Tempo differito scelto, non subito.

**Blocco su:** titoli sezioni III–VI + layer informali ancora da decidere.
Issue GAMMA #2: https://github.com/DMGiulioRomano/GAMMA/issues/2
Quando issue risolta → scrivere testo EN completo → incollare nel form ODT.

---

## Prossimi passi

- [ ] Risolvere issue GAMMA #2 (rinomina sezioni III-VI + layer pinuzzo)
- [ ] Scrivere Work presentation EN (2000 char) a partire dalla spina + wiki GAMMA
- [ ] Compilare application_form_filled.odt (LibreOffice) con tutti i campi sopra
- [ ] Export PDF
- [ ] Eseguire docs/plans/submission-checklist.md — track Works
- [ ] Upload EasyChair
