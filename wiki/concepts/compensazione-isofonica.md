---
type: concept
sources:
  - raw/GAMMA/includes/initIsoAmp.orc:L1-205
  - raw/GAMMA/includes/voce.orc:L79
  - raw/GAMMA/includes/eventoSonoro.orc:L91
updated: 2026-05-29
---

# Compensazione isofonica ISO 226:2003

> **Stato wiki:** l'implementazione **è già documentata** nella wiki GAMMA, pagina
> [initIsoAmp](../../raw/GAMMA/wiki/includes/initIsoAmp.md), che riporta formula,
> tabelle e pipeline UDO. Questa pagina è la **sintesi per il paper/works**: cosa
> fa e perché conta compositivamente. Per il dettaglio implementativo punto-punto
> rimandare a initIsoAmp.

La dinamica in *Gamma* è **percettiva**, non fisica. `ppp`..`fff` non sono
livelli in dBFS ma livelli in **Phon**: l'ampiezza fisica di ogni evento viene
corretta in base alla frequenza con la curva isofonica ISO 226:2003, così che la
sonìa percepita resti costante su tutto lo spettro a parità di dinamica.

## Mappatura simbolico → fisico

In `initIsoAmp.orc`
([L1-205](../../raw/GAMMA/includes/initIsoAmp.orc#L1)) la calibrazione vive in
quattro costanti (il "pannello di controllo"):

```
giPhonFFF  = 100   ; fff = 100 Phon
giPhonStep =   6   ; -6 Phon per gradino dinamico  → ppp = 64 Phon
giDbfsFFF  = -30   ; fff = -30 dBFS @ 1 kHz
giDbfsStep =   6
```

Indici dinamica: `0=ppp, 1=pp, 2=p, 3=mf, 4=f, 5=ff, 6=fff`. Due tabelle
mappano l'indice → Phon e → dBFS di riferimento a 1 kHz.

## Le tabelle ISO 226:2003

`giIsoFreqs` (29 frequenze, 20 Hz – 12.5 kHz) con i coefficienti standard
`giAf`, `giLu`, `giTf`. L'UDO `Interp` replica `numpy.interp`; `PhonToSpl_i`
applica la formula ISO 226:

```
af = Interp(freq, giIsoFreqs, giAf)
lu = Interp(freq, giIsoFreqs, giLu)
tf = Interp(freq, giIsoFreqs, giTf)
af_value = 4.47e-3·(10^(0.025·phon) - 1.15) + (0.4·10^((tf+lu)/10 - 9))^af
spl = (10/af)·log10(af_value) - lu + 94
```

A 1000 Hz esatti `spl = phon` (definizione del Phon).

## Pipeline `GetIsoAmp(freq, dyn) → ampiezza lineare`

1. `dyn` → `phon`, `dBFS_ref` @ 1 kHz;
2. `PhonToSpl_i(phon, freq)` → `dBSPL_target`;
3. `offset = dBSPL_target - phon` (compensazione spettrale);
4. `dBFS_final = dBFS_ref + offset`;
5. `ampdbfs(dBFS_final)` → ampiezza lineare.

Variante k-rate `GetIsoAmp_k` per i glissandi: calcola l'ampiezza agli estremi
`Freq1`/`Freq2` e interpola con `expseg`
([eventoSonoro.orc:L91](../../raw/GAMMA/includes/eventoSonoro.orc#L91)).

## Significato compositivo

- La dinamica è un'**intenzione di sonìa**, non un guadagno. Un `mf` a 60 Hz e un
  `mf` a 4 kHz hanno dBFS molto diversi ma stessa intensità percepita.
- Poiché la frequenza è decisa dal ritmo (vedi [[ritmo-generatore]] e
  [[accordatura-pitagorica]]), l'ampiezza è **a valle del ritmo**: il sistema
  garantisce coerenza percettiva mentre l'altezza cammina nella nube pitagorica.
- Sui glissandi la compensazione varia in modo continuo: l'ampiezza "segue"
  l'orecchio lungo lo scivolamento di frequenza.

## Collegamenti

- [[ritmo-generatore]] — perché l'ampiezza dipende dal ritmo (via altezza)
- [[accordatura-pitagorica]] — le frequenze da compensare
- [[stato-musicale]] — `dinamica` come parametro della maschera (interpolato per indice)
- Wiki GAMMA (dettaglio implementativo): [initIsoAmp](../../raw/GAMMA/wiki/includes/initIsoAmp.md)

## Sezioni paper CIM 2026 dove descrivere

Sezione architettura (modello dinamico). Possibile nota metodologica: porting
della logica da Python a UDO Csound, con equivalenza esplicita verificata.
