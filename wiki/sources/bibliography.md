# Bibliography — tracking

Tabella di tracciamento per la bibliografia del paper CIM 2026.

Source of truth per LaTeX: `paper/refs.bib` (gestito da Zotero + Better BibTeX, **non modificare a mano**).
Questa pagina è la vista operativa per Claude: ingest, propagazione in wiki, mapping su sezioni paper.

**Stati ingest:**
- `✗` — entry BibTeX presente ma PDF non ancora letto / nessuna pagina wiki
- `◐` — parzialmente ingestito (es. solo alcuni capitoli di un libro)
- `✓` — pagina wiki completa con schema rispettato

---

## Papers (raw/papers/)

Chiavi candidate dalla ricerca precursori (2026-06-03, vedi [precursori](../concepts/precursori.md)).
Stato `✗` = entry da creare in `refs.bib` via Zotero + PDF da ingestire.

| Chiave BibTeX | Autori, anno | Titolo breve | Wiki | Sezioni paper |
|---------------|--------------|--------------|------|---------------|
| DiScipio1990 | Di Scipio, 1990 | Composition by Exploration of Non-Linear Dynamic Systems | ✓ | intro, related work, architettura |
| DiScipio1999 | Di Scipio, 1999 | Synthesis of Environmental Sound Textures by Iterated Nonlinear Functions | ✓ | related work, architettura |
| DiScipio2001 | Di Scipio, 2001 | Iterated Nonlinear Functions as a Sound-Generating Engine | ✓ | intro, related work, architettura, conclusioni |
| Anderson2014 | Anderson, 2014 | Audible Ecosystems (Di Scipio) | ✗ | related work |
| Bidlack1992 | Bidlack, 1992 | Chaotic Systems Compositional Algorithms | ✗ | architettura, related work |
| Branchi19xx | Branchi, s.d. | Intervalli e sistemi di intonazione | ✗ | architettura, related work |
| Koenig19xx | Koenig, s.d. | Project 1 / Project 2 (Tendency) | ✗ | architettura |
| Roads2001 | Roads, 2001 | Microsound | ✗ | poetica (tempo differito) |

## Proceedings CIM (raw/proceedings/)

PDF Atti scaricati (gitignored): XI 1995 (258 pp), XVI 2006 (34 pp parz.).
Singoli paper ingestiti dagli Atti:

| Chiave BibTeX | Autori, anno | Titolo breve | Wiki | Sezioni paper |
|---------------|--------------|--------------|------|---------------|
| Rizzuti2006 | Rizzuti, 2006 | Il caos sonoro (granular + iterazione non lineare, Csound) | ✓ | related work, architettura |
| Prignano1995 | Prignano, 1995 | Sintesi eventi sonori per iterazioni funzionali | ✓ | related work, architettura |
| DiScipio1995 | Di Scipio, 1995 | Real-time Polyphonic Time-shifting (granulazione ricorsiva) | ✓ | intro, related work |
| Leach1995 | Leach, 1995 | Algorithmic Composition as Gene Expression | ✓ | related work |
| Bottoni2006 | Bottoni et al., 2006 | Multimedia LaB (loop differito, linguaggio formale) | ✓ | poetica, architettura |

Da spogliare ancora negli Atti: Belladonna 1995 (HyperCSound, generazione eventi
complessi), Di Scipio 1995 "Riflessioni sull'analisi della musica elettroacustica",
Liuni-Morelli 2006 (Playing Music, Xenakis game theory).

## Documentazione software

| Chiave BibTeX | Tool | URL | Wiki | Sezioni paper |
|---------------|------|-----|------|---------------|
| _(nessuna entry)_ | | | | |
