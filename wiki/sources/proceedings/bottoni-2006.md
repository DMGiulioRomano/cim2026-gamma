---
type: proceedings
bibtex: Bottoni2006
source_pdf: raw/proceedings/CIM_XVI_2006_Atti.pdf
venue: XVI CIM, Genova, 24-25 ott 2006
updated: 2026-06-04
---

# [Bottoni et al., 2006] Multimedia LaB: presentazione

## Citazione CIM
Bottoni, P., Faralli, S., Labella, A., Pierro, M., & Scozzafava, C. (2006).
Multimedia LaB: presentazione. In *Atti del XVI Colloquio di Informatica
Musicale*, Genova.

## Argomento centrale
Presentazione dell'attività del gruppo (Univ. Roma "Sapienza", dal 1993): il
linguaggio musicale visto come **linguaggio formale** la cui generazione è
programmabile. Il computer è "supporto per il compositore che, scelto l'assioma e
le regole, deve poi, dopo uno o più passi di riscrittura, effettuare una selezione
sui risultati ed eventualmente richiedere nuove elaborazioni fino a raggiungere il
risultato desiderato".

## Categoria e lunghezza
Report di laboratorio, ~2 pp.

## Sistema o strumento descritto
Architettura **Chambre** (accetta ed elabora stringhe da sorgenti diverse);
ambiente generativo **Clipscore** (composizione via trasformazioni geometriche
iterative di "celle", dentro l'interfaccia Hyperscore); linguaggio **GO/Max**
(modella patch Max/MSP come variabili di stato + operatori con precondizioni;
un agente pianifica la sequenza di operatori per portare lo stato in uno stato
obiettivo). TouchBox: strumento low-cost programmabile (DSP Atmel).

## Gap o problema identificato
Integrare teoria dei linguaggi formali, generazione automatica e governo dei
parametri di controllo in un unico ambiente, dove l'autore itera assioma→regole→
riscrittura→selezione.

## Analogia con Gamma
- **Loop differito autore**: "scelto l'assioma e le regole … dopo uno o più passi
  di riscrittura, … selezione … nuove elaborazioni fino al risultato desiderato"
  è esattamente il ciclo YAML→render→ascolto→riscrittura di [[poetica]] (§tempo
  differito).
- **Linguaggio formale come strumento compositivo**: omologo del DSL YAML→Csound
  di GAMMA; comporre = definire assioma + regole, non scrivere la superficie.
- **Generazione iterativa** (Clipscore, "trasformazioni geometriche iterative di
  celle"): risuona con l'iterazione che genera la superficie in GAMMA
  ([[mappa-logistica]]) e con la grammatica di [[leach-1995]].

Differenza: qui la generazione è simbolico/visuale (celle, patch); GAMMA è
parametrico/numerico. Comune: il compositore governa lo spazio di possibilità via
regole, non il dettaglio.

## Posizionamento storico
2006, informatica musicale come teoria dei linguaggi formali (radice anni '90,
"follia"/"fuga" come grammatiche). Filone DSL/CAC italiano.

## Sezioni del paper CIM 2026 dove citare
Poetica (tempo differito, comporre via regole), Architettura (DSL come paradigma).

## Note stilistiche
Tono di report; il valore per GAMMA è la *formulazione esplicita* del ciclo
differito assioma→riscrittura→selezione, da citare a supporto della postura.

## Quote chiave
> "il compositore, dopo aver scelto l'assioma e le regole, doveva poi, dopo uno o
> più passi di riscrittura, effettuare una selezione sui risultati ed
> eventualmente richiedere nuove elaborazioni fino a raggiungere il risultato
> desiderato." (p.1)

## Collegamenti
[[poetica]] · [[mappa-logistica]] · [[precursori]] · [[leach-1995]]
