---
type: proceedings
bibtex: Rizzuti2006
source_pdf: raw/proceedings/CIM_XVI_2006_Atti.pdf
venue: XVI CIM, Genova, 24-25 ott 2006
updated: 2026-06-04
---

# [Rizzuti, 2006] Il "caos sonoro": studi preliminari per la realizzazione di un sistema di sintesi granulare controllato mediante iterazione di funzioni non lineari

## Citazione CIM
Rizzuti, C. (2006). Il "caos sonoro": studi preliminari per la realizzazione di
un sistema di sintesi granulare controllato mediante iterazione di funzioni non
lineari. In *Atti del XVI Colloquio di Informatica Musicale*, Genova.

## Argomento centrale
Sistema di sintesi granulare asincrona il cui controllo ad alto livello è
affidato a **funzioni non lineari iterate** invece che a generatori di numeri
casuali. Il caos deterministico fornisce varietà e imprevedibilità senza
randomness.

## Categoria e lunghezza
Comunicazione breve (2 pp). Studi preliminari / work in progress.

## Sistema o strumento descritto
Implementazione in **CSound**, due strumenti: uno genera gli eventi sonori
secondo la partitura, l'altro genera i grani secondo le direttive del primo
strumento e della partitura. Mappa logistica nella forma
`x[t+1] = c·x[t]·(2 - x[t])`, con `c ∈ [0,2]`: regime da convergente (punto
fisso) a periodico a completamente caotico. La mappa controlla ampiezza,
durata, istante d'attacco dei grani; l'iterazione controlla anche le frequenze
delle parziali (armoniche/inarmoniche).

## Gap o problema identificato
La sintesi granulare classica fa "largo impiego di generatori di numeri casuali"
per il controllo ad alto livello. Rizzuti vuole evitarli: controllo
**interamente deterministico** via relazioni matematiche, dove solo il
comportamento caotico introduce varietà.

## Analogia con Gamma
Il precursore CIM più vicino a GAMMA trovato finora. Punti di contatto:
- **Caos deterministico, no random**: identico alla postura di [[poetica]] e di
  [[mappa-logistica]] — emergenza da regola, non da casualità (GAMMA usa random
  solo nel mode 3 di `NonlinearFunc`).
- **Mappa logistica** con parametro che attraversa convergente→periodico→caotico:
  esattamente i regimi di `NonlinearFunc` (`iMode` 0/1/2 → convergente/periodico/
  caotico) di GAMMA.
- **Una sorgente non lineare → molti parametri di sintesi** (ampiezza, durata,
  attacco, frequenza parziali): omologo del ritmo-generatore di GAMMA
  ([[ritmo-generatore]]), benché lì la sorgente sia il valore ritmico.
- **CSound, architettura a due strati** partitura/generazione: GAMMA è
  Python→SCO + strumenti `.orc`, due strati analoghi.

Differenza: Rizzuti applica il caos al livello micro del **grano**; GAMMA al
livello meso dell'**evento/ritmo**. Stessa famiglia, scala diversa.

## Posizionamento storico
Italiano, 2006, area sintesi granulare + sistemi dinamici. Eredità Di Scipio /
Prignano (vedi [[discipio-1995]], [[prignano-1995]]): iterazione di funzioni non
lineari per il suono. Bibliografia: Bertacchini-Bilotta-Pantano "Modelli
Matematici, Linguaggi e Musica" (Sistemi Intelligenti 2005), Gleick *Caos*,
Dodge-Jerse *Computer Music*.

## Sezioni del paper CIM 2026 dove citare
Related work (precursore diretto), Architettura (mappa logistica, regimi),
Conclusione (caos deterministico come scelta condivisa nella tradizione CIM).

## Note stilistiche
Linguaggio sobrio, tecnico. Enfasi sul rifiuto del random come scelta estetica,
non solo tecnica — punto di forte risonanza con la postura di GAMMA.

## Quote chiave
> "si è voluto, infatti, evitare l'impiego di generatori di numeri casuali. Si è
> scelto, al contrario, di controllare tutti i parametri e le grandezze in
> maniera deterministica mediante ferree relazioni matematiche; soltanto il
> manifestarsi del comportamento caotico delle funzioni non lineari consente di
> introdurre varietà e imprevedibilità all'interno del materiale sonoro." (p.1)

## Collegamenti
[[mappa-logistica]] · [[ritmo-generatore]] · [[poetica]] · [[precursori]] ·
[[prignano-1995]] · [[discipio-1995]]
