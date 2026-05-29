---
type: concept
sources:
  - raw/GAMMA/includes/voce.orc:L51-121
  - raw/GAMMA/includes/eventoSonoro.orc:L31-110
  - raw/GAMMA/includes/pfield_comp.udo:L8-20
updated: 2026-05-29
---

# Il ritmo come parametro generatore unico

Tesi centrale del sistema GAMMA, e architrave del paper CIM 2026: in *Gamma* il
**valore ritmico** non è un parametro fra molti, è il parametro generatore.
Un singolo intero per evento — `i_RitmoCorrente` — viene letto da quattro
dimensioni indipendenti della sintesi. Decidere il ritmo significa decidere,
nello stesso gesto, l'altezza, il tempo, lo spazio e l'ampiezza.

Il valore ritmico è esso stesso autogenerato (vedi [[mappa-logistica]]): il
compositore non scrive i ritmi, scrive il seme e il regime dinamico da cui i
ritmi si generano. Da qui la postura di [[poetica]]: controllo dello spazio di
possibilità, non del dettaglio.

## Le quattro letture del valore ritmico

Dentro `instr Voce` un evento nasce con un `i_RitmoCorrente` (intero, default
range 1–35). Quello stesso numero entra in quattro punti.

### 1. Tempo — suddivisione dell'armonica ritmica

L'intervallo fra un evento e il successivo, e la durata dell'evento, sono
frazioni di una durata di riferimento `i_DurataArmonica` divisa per il ritmo:

```
i_whileTime    += (i_DurataArmonica / i_RitmoCorrente)
i_EventDuration = (i_DurataArmonica / i_RitmoCorrente) * i_OverlapFactor
```

([voce.orc:L93](../../raw/GAMMA/includes/voce.orc#L93),
[L120](../../raw/GAMMA/includes/voce.orc#L120)).

Il ritmo è quindi un **numero armonico nel tempo**: `durata_armonica/1`,
`/2`, `/3`… È una serie armonica trasportata sull'asse temporale. Ritmo alto =
eventi fitti; ritmo basso = eventi radi. Questo è il senso di "armoniche
ritmiche".

### 2. Altezza — offset nella tabella pitagorica

`calcFrequenza(ottava, registro, ritmo)` usa il ritmo come spostamento
nell'indice di lettura della tabella di intonazione `gi_Intonazione`:

```
i_Freq table max(1, i_OffsetIntervallo + i_RitmoCorrente), gi_Intonazione
```

([pfield_comp.udo:L17](../../raw/GAMMA/includes/pfield_comp.udo#L17)).

A parità di `(ottava, registro)`, ritmi diversi leggono celle diverse della
tabella → **note diverse**. Poiché la tabella è una nube pitagorica a 200
intervalli per ottava (vedi [[accordatura-pitagorica]]), lo spostamento di
poche celle prodotto dal ritmo è uno scarto microtonale: il flusso ritmico fa
camminare l'altezza dentro la nube, e da lì emergono i battimenti.

### 3. Spazio — armonica spaziale Mid/Side

Nella `schedule` il ritmo viene passato a `eventoSonoro` come p7 →
`iHR` ([voce.orc:L114-115](../../raw/GAMMA/includes/voce.orc#L114)). Lì
definisce il **periodo angolare** della rotazione Mid/Side:

```
iHR    = max(1, abs(p7))          ; p7 = i_RitmoCorrente
iPeriod = 2*$M_PI / iHR
krad   = iradi + (ktab * iPeriod * i_senso)
kMid   = cos(krad)
kSide  = sin(krad)
aL = (aMid + aSide)/$SQRT2
aR = (aMid - aSide)/$SQRT2
```

([eventoSonoro.orc:L31-110](../../raw/GAMMA/includes/eventoSonoro.orc#L31)).

L'evento percorre un arco di `2π/HR` radianti nel piano Mid/Side: occupa cioè
**1/HR di una rotazione completa**. Il ritmo è letteralmente un'**armonica
spaziale** — un divisore del cerchio. Ritmo alto = arco piccolo (movimento
spaziale contenuto); ritmo basso = arco ampio. La direzione (orario/antiorario)
è `i_senso`, la fase di partenza viene dalla posizione `i_Pos`.

Dettaglio fine: quando l'inviluppo locale è l'abs-sin di default
(`ifn_shape == 2`), `kEnv_local = abs(sin(krad * iHR / 2))`. La stessa
variabile di fase `krad` governa rotazione spaziale **e** forma d'ampiezza: lo
spazio e l'inviluppo sono accoppiati sullo stesso ritmo.

### 4. Ampiezza — a valle dell'altezza

L'ampiezza dell'evento è `GetIsoAmp(i_Freq1, i_DynamicIndex)`
([voce.orc:L79](../../raw/GAMMA/includes/voce.orc#L79)). La dinamica simbolica
(`ppp`..`fff`) fissa il livello in Phon; la frequenza — decisa dal ritmo al
punto 2 — determina la compensazione isofonica (vedi
[[compensazione-isofonica]]). Quindi anche l'ampiezza lineare finale è
**a valle del ritmo**: cambiando ritmo cambia la frequenza, e con essa la
correzione percettiva.

## Catena completa (un evento)

```
i_RitmoCorrente
   ├─ tempo:    durata_armonica / ritmo        → onset e durata
   ├─ altezza:  offset in gi_Intonazione        → calcFrequenza → Freq1/Freq2
   │                └─ altezza → GetIsoAmp       → ampiezza (compensata ISO 226)
   └─ spazio:   2π/ritmo                         → arco Mid/Side + inviluppo
```

## Collegamenti

- [[mappa-logistica]] — come il valore ritmico si autogenera (feedback non lineare)
- [[accordatura-pitagorica]] — la tabella che il ritmo indicizza
- [[compensazione-isofonica]] — l'ampiezza a valle dell'altezza
- [[stato-musicale]] — i due strati ritmici (macro/micro)
- [[poetica]] — la postura compositiva che ne deriva
- Analisi per-modulo nella wiki GAMMA: [voce](../../raw/GAMMA/wiki/includes/voce.md),
  [eventoSonoro](../../raw/GAMMA/wiki/includes/eventoSonoro.md),
  [pfield_comp](../../raw/GAMMA/wiki/includes/pfield_comp.md)

## Sezioni paper CIM 2026 dove descrivere

Sezione architettura (il sistema), sezione poetica (la postura). È
probabilmente il nucleo argomentativo dell'intero paper: una sola variabile
genera la quadruplice texture.
