# Fonti da reperire — PDF non auto-scaricabili

Lista delle fonti citate nella ricerca precursori (vedi
[wiki/concepts/precursori.md](../../wiki/concepts/precursori.md)) che **non**
sono state scaricate in automatico: paywall, anti-bot, o copyright. Da reperire
a mano e importare in Zotero + `raw/papers/`.

Workflow per ciascuna (cfr. `CLAUDE.md > Workflow add-paper`):
1. reperire il PDF;
2. metterlo in `inbox/`;
3. importare in Zotero (Better BibTeX genera la chiave definitiva);
4. spostare in `raw/papers/<FILENAME>.pdf`, appendere a `paper/refs.bib`;
5. aggiornare stato in `wiki/sources/bibliography.md` (`✗` → `✓` dopo ingest wiki).

Le chiavi qui sotto sono **provvisorie**: la definitiva la fissa Better BibTeX.

---

## Priorità alta — fonti primarie degli assi centrali

| Chiave provv. | Autore, anno | Titolo | Asse | Dove | Accesso |
|---|---|---|---|---|---|
| DiScipio1999 | Di Scipio, A. (1999) | The Synthesis of Environmental Sound Textures by Iterated Nonlinear Functions | caos / mappa logistica | *Organised Sound*, Cambridge UP | paywall Cambridge / ResearchGate login |
| Bidlack1992 | Bidlack, R. (1992) | Chaotic Systems as Simple (But Complex) Compositional Algorithms | mappa logistica | *Computer Music Journal* 16(3):33-47 | paywall MIT Press / JSTOR |
| Branchi19xx | Branchi, W. (s.d.) | Intervalli e sistemi di intonazione | nube pitagorica | UNESCO / LEMS | non open — biblioteca / acquisto |

## Priorità media — secondarie e contesto

| Chiave provv. | Autore, anno | Titolo | Asse | Dove | Accesso |
|---|---|---|---|---|---|
| Anderson2014 | Anderson, C. (2014) | Audible Ecosystems and Emergent Sound Structures in Di Scipio's Music | caos / emergenza | *Contemporary Music Review* 33(1), 2014 | HAL (hal-00770097) dietro anti-bot Anubis; provare mirror Taylor & Francis |
| Roads2001 | Roads, C. (2001) | Microsound | tempo differito | MIT Press | libro, copyright — riferimento, non cita-righe; reperire copia |

## Priorità bassa — scaricabili ma non ancora presi

| Chiave provv. | Autore, anno | Titolo | Asse | Dove | Accesso |
|---|---|---|---|---|---|
| Koenig19xx | Koenig, G. M. (s.d.) | Project 1 / Project 2 (documentazione, metodo Tendency) | maschere di tendenza | koenigproject.nl | open — manuali software scaricabili |

## Da identificare (riferimento incompleto)

- **SDM — Sistemi Dinamici e Musica**: progetto/articolo italiano che genera
  musica da ritratto di fase di sistemi di equazioni differenziali. Reperire
  citazione completa (autore, venue, anno).
- **Atti CIM**: i volumi XI 1995 (258 pp) e XVI 2006 (34 pp parziale) sono
  scaricati in `raw/proceedings/` (gitignored). Da spogliare per individuare i
  singoli paper su caos / Csound / sistemi dinamici da citare; quando trovati,
  aprire `wiki/sources/proceedings/<autore-anno>.md` per ciascuno.

---

Aggiornare questo file man mano che le fonti vengono reperite (spuntare riga o
spostarla). A lista esaurita, spostare in `docs/done/`.
