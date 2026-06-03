---
type: concept
sources:
  - wiki/concepts/poetica.md
  - wiki/concepts/mappa-logistica.md
  - wiki/concepts/accordatura-pitagorica.md
  - wiki/concepts/stato-musicale.md
updated: 2026-06-03
---

# Precursori e related work

Mappa dei precursori per il paper CIM 2026, organizzata per asse distintivo di
*Gamma*. Costruita da ricerca web (2026-06-03); le fonti primarie sono ancora da
ingestire (`raw/papers/` quasi vuoto: vedi *Stato fonti* in fondo). Questa
pagina serve a impostare la sezione *related work* e a evitare di riscoprire le
stesse fonti.

Postura (cfr. [[poetica]]): mai "è meglio fare così". I precursori
**situano** la scelta, non la giustificano.

## Asse 1 — Caos deterministico / mappa logistica

Asse di parentela più stretto (vedi [[mappa-logistica]]).

- **Agostino Di Scipio** — match più prossimo, e italiano (centrale a CIM).
  Sintesi via **funzioni nonlineari iterate** (fine anni '80–'90): stessa
  famiglia matematica del `NonlinearFunc` di GAMMA. Poetica dell'**emergenza**:
  il compositore progetta il *sistema*, non l'esito — sovrapponibile al
  principio "controllo dello spazio di possibilità, non del dettaglio" di
  [[poetica]]. Micro-composizione da cui emergono proprietà macro-gestuali.
  Serie *Audible Ecosystemics*, *Modes of Interference*.
  - Fonte primaria: Di Scipio, "The Synthesis of Environmental Sound Textures
    by Iterated Nonlinear Functions" (*Organised Sound*, fine anni '90).
    Paywall Cambridge / ResearchGate login → ingest manuale via Zotero.
  - Secondaria open-access (anti-bot HAL al 2026-06-03): Anderson, "Audible
    Ecosystems and Emergent Sound Structures in Di Scipio's Music"
    (*Contemporary Music Review* 33(1), 2014).

- **Rick Bidlack (1992)** — riferimento canonico mappa logistica → musica.
  "Chaotic Systems as Simple (But Complex) Compositional Algorithms",
  *Computer Music Journal* 16(3):33–47. Cita la logistica esplicitamente;
  sensibilità alle condizioni iniziali come generatore di varianti. Aggancia
  direttamente la tabella regimi (`iMode` 0/2) di [[mappa-logistica]].

- **Altri pionieri** — Jeff Pressing, Michael Gogins, Jeremy Leach: caos →
  parametri nota. Pressing per il mapping caos→altezza/ritmo.

## Asse 2 — Nube pitagorica densa, battimenti (eredità Branchi)

Vedi [[accordatura-pitagorica]].

- **Walter Branchi** — lignaggio diretto. Testo di riferimento sui sistemi di
  intonazione: **"Intervalli e sistemi di intonazione"**. Opera *"Intero"*
  (Princeton 1979 / CCRMA 1983) — rilevante anche per il ciclo Delta→Gamma→Intero
  di [[poetica]]. Fondò il LEMS; autore del primo manuale italiano di tecnologia
  della musica elettronica. Fonte **primaria** del repo, non solo citazione.
  - Stato: nessun PDF reperito in auto (non open-access). Reperire a mano.

## Asse 3 — Maschere di tendenza

Vedi [[stato-musicale]].

- **Gottfried Michael Koenig**, *Project 1 / Project 2* — il metodo di selezione
  **"Tendency" (directionally defined selection)** è la radice storica delle
  maschere di tendenza: scelta entro un range che evolve direzionalmente nel
  tempo. Precedente diretto della distinzione stato statico vs transizione.
  - Doc/software: koenigproject.nl (manuali Project 1/2 scaricabili).

## Asse 4 — Tempo differito / render offline

Vedi [[poetica]] §"Tempo differito".

- **Curtis Roads**, *Microsound* (MIT Press, 2001) — primo render granulare in
  non-realtime (1975: ore di calcolo per secondi di suono). Composizioni "in
  anni": il tempo differito come **scelta** poetica (separare decisione da resa),
  non come limite tecnico. Inquadra il ciclo YAML→render→ascolto→riscrittura.
  - Libro copyright (no auto-download); riferimento, non paper da citare a righe.

## Asse 5 — Compensazione isofonica ISO 226

Vedi [[compensazione-isofonica]].

- Pratica metodologica consolidata: in sonification i suoni vengono
  **loudness-normalizzati sulla curva 40-phon ISO 226** per coerenza timbrica
  fra frequenze. Conferma che l'ampiezza in Phon a valle dell'altezza ha
  precedenti di metodo. Standard: ISO 226 ed. **2003** (quella usata da GAMMA),
  rev. **2023** esistente — citare l'edizione corretta.

## Asse 6 — Variabile unica → quadruplice texture

Vedi [[ritmo-generatore]]. **Asse più originale.** La letteratura
parameter-mapping copre gesture→synth o feature-based synthesis, non *un singolo
intero generativo che pilota quattro dimensioni indipendenti* (tempo, altezza,
spazio, ampiezza). Nessun match stretto trovato → candidato a claim di
contributo nel paper. Da verificare con ricerca mirata prima di rivendicare
novità.

## Precursori CIM (atti open-access)

Atti del Colloquio di Informatica Musicale full-text su `cim.lim.di.unimi.it`.
Caos, sistemi dinamici e Csound già presenti negli atti storici → fonte diretta
per la sezione *posizionamento rispetto ai precursori CIM* di [[poetica]].

- Scaricati in `raw/proceedings/` (gitignored): Atti **XI 1995** (258 pp, full),
  Atti **XVI 2006** (34 pp, parziale).
- Da spogliare per singoli paper rilevanti → quando individuati, aprire una
  pagina `wiki/sources/proceedings/<autore-anno>.md` per ciascuno.
- Progetto **SDM (Sistemi Dinamici e Musica)**: caos→musica via ritratto di
  fase — parente concettuale, da reperire riferimento.

## Stato fonti (da ingestire)

| Fonte | Asse | Auto-download | Azione |
|-------|------|---------------|--------|
| Di Scipio, *Iterated Nonlinear Functions* | 1 | no (paywall) | Zotero manuale |
| Anderson 2014, *Audible Ecosystems* | 1 | no (HAL anti-bot) | reperire |
| Bidlack 1992, *CMJ* 16(3) | 1 | no (paywall) | Zotero manuale |
| Branchi, *Intervalli e sistemi di intonazione* | 2 | no | reperire |
| Koenig, *Project 1/2* docs | 3 | sì (koenigproject.nl) | scaricare |
| Roads, *Microsound* | 4 | no (copyright) | riferimento, no cita-righe |
| Atti CIM XI 1995 / XVI 2006 | CIM | **sì (fatto)** | spogliare paper |

`paper/refs.bib` **non** ancora creato a mano (regola: è generato da Zotero).
Le chiavi candidate vivono in [bibliography.md](../sources/bibliography.md) con
stato `✗` finché non ingestite.

## Collegamenti

- [[poetica]] · [[mappa-logistica]] · [[accordatura-pitagorica]] ·
  [[ritmo-generatore]] · [[stato-musicale]] · [[compensazione-isofonica]]
- Tracking chiavi: [bibliography.md](../sources/bibliography.md)

## Sezioni paper CIM 2026 dove descrivere

Related work (tutti gli assi); Introduzione (postura, Di Scipio/emergenza);
Architettura (Bidlack per logistica, Branchi per intonazione, Koenig per
tendenza); Conclusione (asse 6 come possibile contributo).
