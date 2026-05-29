---
type: concept
sources:
  - raw/GAMMA/yaml/guida.yaml:L124-294
  - raw/GAMMA/generative_composerYaml2.py:L548-705
  - raw/GAMMA/generative_composerYaml2.py:L78-130
updated: 2026-05-29
---

# Stato musicale: transizione vs stasi

Un layer di *Gamma* ha uno **stato musicale**: la configurazione completa delle
sue maschere di tendenza (altezza, registro, durata armonica, densità, dinamica,
ritmo, spazializzazione). Lo stato può essere **statico** — fermo per tutta la
vita del layer — o **in transizione** — che si trasforma con continuità da una
condizione iniziale a una finale. È la distinzione formale alla base della nota
di programma ("musical states in transition").

## Maschera di tendenza

Non valori fissi ma spazi di possibilità: ogni parametro definisce un range/
distribuzione da cui il sistema campiona a ogni evento
([guida.yaml:L124-188](../../raw/GAMMA/yaml/guida.yaml#L124)).

```yaml
parametro: { range: [min, max] }            # uniforme
parametro: { choices: [a, b], weights: [...] }
parametro: { value: X }                      # fisso
parametro: { mean: M, std: S }               # normale
```

## I due regimi

### Statico — `stato_unico`

Una sola maschera, valida per tutto il `lifespan`. Nel codice
`is_static_layer` è vero quando il layer dichiara `stato_unico`
([generative_composerYaml2.py:L637](../../raw/GAMMA/generative_composerYaml2.py#L637)):
ogni evento campiona dalla stessa maschera. La variabilità resta (è stocastica),
ma le **tendenze** non si muovono: stasi.

### Transizione — `stato_iniziale` / `stato_finale`

Due maschere; il sistema interpola fra loro lungo il lifespan
([guida.yaml:L195-207](../../raw/GAMMA/yaml/guida.yaml#L195)):

- `range`, `mean`, `std`: interpolazione lineare dei numeri;
- `choices`: cross-fade dei `weights`;
- `dinamica`: interpolata via indice numerico (anche `p` → `f` è fluido);
- `value` (stringhe): cambio netto a metà percorso;
- parametro presente in un solo stato → usato per l'intera durata.

`interp_shape` piega la curva di interpolazione (non lineare).

## Due strati ritmici (da non confondere)

Lo stato musicale governa **due** livelli di tempo, distinti:

1. **Macro — distribuzione delle attivazioni.** `TimeScheduler.generate_onsets`
   distribuisce `num_attivazioni` cluster nel lifespan secondo `timing_model`:
   `lineare`, `accelerando`, `rallentando`, `stochastic`, `breakpoint`
   ([generative_composerYaml2.py:L78-130](../../raw/GAMMA/generative_composerYaml2.py#L78),
   [L628](../../raw/GAMMA/generative_composerYaml2.py#L628)). È il respiro
   esterno del layer.
2. **Micro — ritmo interno alla voce.** Dentro ogni `Voce` il ritmo si
   autogenera (vedi [[mappa-logistica]]) e suddivide `durata_armonica`. È la
   grana interna.

A ogni attivazione vengono impilate `densita_cluster` voci
([generative_composerYaml2.py:L646-649](../../raw/GAMMA/generative_composerYaml2.py#L646)):
il cluster è la dimensione **verticale** (quante voci insieme), il timing_model è
quella **orizzontale** (quando), il ritmo interno è la **grana** (come si
suddividono).

## Parametri dello stato

Dal dizionario in `guida.yaml`
([L140-188](../../raw/GAMMA/yaml/guida.yaml#L140)):

| Parametro | Ruolo |
|---|---|
| `ottava` (0–10), `registro` (1–50) | altezza di partenza nella nube pitagorica |
| `ottava_arrivo`/`registro_arrivo`, `offset_ottava`/`offset_registro` | glissando |
| `dinamica` (`ppp`..`fff`) | livello in Phon ([[compensazione-isofonica]]) |
| `durata_armonica` | durata di riferimento suddivisa dal ritmo (obbligatoria) |
| `densita_cluster` | voci per attivazione (verticale) |
| `tipo_ritmi` | seme ritmico esplicito iniziale |
| `nonlinear_mode` (0–3) | regime del ritmo autogenerato ([[mappa-logistica]]) |
| `onset_jitter` | sbavatura gaussiana degli attacchi |
| `inviluppo_attacco` | forma del singolo evento (da `tables.yaml`) |
| `senso_movimento` (±1) | direzione dell'orbita Mid/Side |

## Collegamenti

- [[ritmo-generatore]] — cosa fa il ritmo una volta fissato lo stato
- [[mappa-logistica]] — `nonlinear_mode`, ritmo micro
- [[compensazione-isofonica]] — `dinamica`
- [[poetica]] — transizione/stasi come forma
- Wiki GAMMA: [maschera_tendenza](../../raw/GAMMA/wiki/concepts/maschera_tendenza.md)

## Sezioni paper CIM 2026 dove descrivere

Sezione architettura (maschere, due strati di tempo) e sezione forma/poetica
(stati in transizione come principio formale dell'opera).
