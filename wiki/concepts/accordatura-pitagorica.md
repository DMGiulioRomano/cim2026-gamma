---
type: concept
sources:
  - raw/GAMMA/includes/GenPythagFreqs.udo:L1-62
  - raw/GAMMA/includes/pfield_comp.udo:L8-20
  - raw/GAMMA/generative_composerYaml2.py:L20-22
  - raw/GAMMA/generative_composerYaml2.py:L897-924
updated: 2026-05-29
---

# Accordatura pitagorica a 200 intervalli e zone di battimento

Lo spazio delle altezze di *Gamma* è una nube pitagorica densissima. Non le 12
note della scala pitagorica storica, ma **200 intervalli per ottava**, generati
dalla stessa catena di quinte e ridotti all'ottava. La densità è il punto: a 200
gradi le altezze adiacenti sono quasi coincidenti, e quando il ritmo le fa
suonare insieme nascono **battimenti** che il compositore non controlla
direttamente.

## Lignaggio: Walter Branchi

La suddivisione pitagorica è studiata da Walter Branchi, che la impiega per
**interi** (la catena di quinte nella sua forma classica). L'estensione di
*Gamma* è quantitativa e ne cambia la natura: la stessa procedura — quinte giuste
`3/2` accatastate e ricondotte all'ottava — portata a un numero di gradi molto
alto (200), non per ottenere una scala suonabile ma per **saturare** lo spazio
frequenziale e produrre zone di interferenza.

> DA INGESTIRE: nessuna fonte Branchi in `raw/papers/` finora. Aprire una pagina
> `wiki/sources/papers/Branchi_<anno>.md` quando il testo di riferimento è
> reperito; aggiornare `wiki/sources/bibliography.md`.

## L'algoritmo (`GenPythagFreqs`)

`opcode GenPythagFreqs, i, iiii` riempie una f-table
([GenPythagFreqs.udo:L1-62](../../raw/GAMMA/includes/GenPythagFreqs.udo#L1)):

```
iRes GenPythagFreqs iFund, iNumIntervals, iNumOctaves, iTblNum
```

Per ogni ottava:

1. parte dal rapporto `1` → scrive `iFund * 2^ottava`;
2. itera moltiplicando per la quinta `3/2`;
3. riduce all'ottava di riferimento (`while iRatio >= 2: iRatio /= 2`);
4. genera `iNumIntervals` rapporti, poi li **ordina** (bubble sort) in ascendente;
5. replica su `iNumOctaves`.

## Valori reali in *Gamma*

Dall'header CSD generato dal Python
([generative_composerYaml2.py:L897-924](../../raw/GAMMA/generative_composerYaml2.py#L897)):

```
#define FONDAMENTALE #32#      ; 32 Hz
#define INTERVALLI   #200#     ; INTERVALLI_PER_OTTAVA = 200
#define OTTAVE       #10#      ; OTTAVE_RANGE = (0, 10)
#define REGISTRI     #50#      ; REGISTRI_RANGE = (1, 50)
gi_Intonazione ftgen 0, 0, $OTTAVE*$INTERVALLI+1, -2, 0   ; 2001 celle

i_Res GenPythagFreqs $FONDAMENTALE, $INTERVALLI, $OTTAVE, gi_Intonazione
```

Fondamentale 32 Hz, 200 gradi per ottava, 10 ottave → **2000 frequenze**
tabulate.

## Perché 200 gradi generano battimenti

La catena di quinte non si chiude mai sull'ottava (comma pitagorico): a ogni
quinta in più il nuovo grado cade vicinissimo a uno già presente. A 200 quinte
accatastate e ridotte si ottengono 200 altezze irregolarmente spaziate, molte
quasi coincidenti (frazioni di comma). Quando due voci leggono celle contigue
suonano frequenze separate da pochi Hz → **battimento**. La spaziatura non è
uniforme (non è un temperamento equabile a 200 gradi): è la firma irregolare
della riduzione pitagorica, e i battimenti che ne risultano non sono pianificati
grado per grado.

## Come il ritmo cammina nella nube

`calcFrequenza` ([pfield_comp.udo:L8-20](../../raw/GAMMA/includes/pfield_comp.udo#L8)):

```
idx_ottava   = int(ottava * 200)              ; salto di ottava intera
idx_registro = idx_ottava + int(registro*200/50)  ; registro 1..50 → 0..200
offset       = max(1, idx_registro + ritmo)   ; il ritmo sposta di poche celle
freq         = gi_Intonazione[offset]
```

`ottava` (0–10) salta di 200 celle; `registro` (1–50) si muove dentro l'ottava
a passi di 4 celle; il **ritmo** (1–35) aggiunge lo scarto fine. È il ritmo a
far camminare l'altezza dentro la nube microtonale — di qui il legame con
[[ritmo-generatore]]. Voci con ottava/registro uguali ma ritmi diversi cadono su
celle vicine → battimento emergente.

## Collegamenti

- [[ritmo-generatore]] — il ritmo come indice di lettura
- [[poetica]] — emergenza non controllata (battimenti) e tempo differito
- Wiki GAMMA: [GenPythagFreqs](../../raw/GAMMA/wiki/includes/GenPythagFreqs.md),
  [pfield_comp](../../raw/GAMMA/wiki/includes/pfield_comp.md)

## Domande aperte

- Spaziatura media a 200 gradi vs comma: quantificare i Hz di battimento tipici
  per registro (calcolo dalla tabella). Utile come figura nel paper.
- Confronto esplicito con la pratica di Branchi (a interi): dove finisce
  l'eredità e comincia l'estensione.

## Sezioni paper CIM 2026 dove descrivere

Sezione architettura (tabella di intonazione) e sezione poetica/related work
(eredità Branchi, battimenti come materiale non pianificato).
