# [Fletcher & Munson, 1933] Loudness, Its Definition, Measurement and Calculation

## Citazione CIM
Fletcher, H., & Munson, W. A. (1933). Loudness, Its Definition, Measurement and Calculation. *The Journal of the Acoustical Society of America*, 5(2), 82–108. https://doi.org/10.1121/1.1915637

## Argomento centrale
Paper fondativo della psicoacustica della loudness. Definisce la loudness come **grandezza di una sensazione uditiva**, dipendente dal numero totale di impulsi nervosi al secondo lungo il tratto uditivo, non riducibile alla sola intensità fisica del suono. Introduce il livello di loudness (in Phon) come intensità del tono di riferimento a 1000 Hz egualmente forte, e formula una teoria empirica per *calcolare* la loudness di toni complessi steady-state sommando i contributi delle componenti. Origine delle **curve isofoniche** (equal-loudness contours) poi standardizzate (ISO 226).

## Gap o problema identificato
Le notazioni musicali (ff, f, mf, p, pp) e i termini "very loud / soft" sono imprecisi e dipendono da esperienza e acuità dell'ascoltatore. Serviva una formula di applicazione generale per la loudness di suoni complessi: le formule precedenti (Steinberg 1925) erano risultate inadeguate al crescere dei dati. Gap: relazione loudness↔intensità non semplice, mediata da frequenza e composizione spettrale.

## Rilevanza diretta per Gamma
Radice storica diretta della [[compensazione-isofonica]] di Gamma. Il modulo `initIsoAmp` di GAMMA applica una compensazione in Phon via **ISO 226:2003** — che è la discendente normata delle curve Fletcher-Munson. Fletcher-Munson è la fonte primaria citabile per giustificare *perché* la dinamica di Gamma è calcolata a valle dell'altezza: la loudness percepita di un evento dipende dalla sua frequenza, non solo dall'ampiezza. Posiziona la scelta come radicata in 90 anni di psicoacustica, non arbitraria.

## Collegamento alla tesi centrale
Lega all'angolo della **triangolazione decisionale** (DSL parametrico ↔ partitura visuale ↔ ascolto): la compensazione isofonica è esattamente il punto in cui il sistema *modella il ricevente* (l'orecchio) anziché solo la sorgente. Cfr. tensione con [[doebereiner-2010]]: il CMSS ortodosso (Brün anticommunication) rifiuta il modeling-the-receiver; Gamma lo abbraccia. Fletcher-Munson fornisce la base empirica di quella scelta, da tematizzare nella poetica come postura percettiva esplicita.

## Sezioni del paper CIM 2026 dove citare
- Architettura: modulo di compensazione isofonica (`initIsoAmp`), ampiezza derivata dall'altezza in Phon.
- Poetica / discussione: modeling-the-receiver come scelta consapevole, in tensione con il non-standard ortodosso.

## Quote chiave
- "Loudness is a psychological term used to describe the magnitude of an auditory sensation. […] If loudness depended only upon the intensity of the sound wave producing the loudness, then measurements of the physical intensity would definitely determine the loudness […] However, no such simple relation exists." (p.82)
- "the loudness of an auditory sensation, is probably dependent upon the total number of nerve impulses that reach the brain per second along the auditory tract." (p.82)
- "The loudness level of any sound shall be the intensity level of the equally loud reference tone at the position where the listener's head is to be placed." (p.83)

## Collegamenti
[[compensazione-isofonica]] · [[doebereiner-2010]] · [[precursori]] (ISO 226)
