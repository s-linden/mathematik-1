# 11.5 Extremwerte

In diesem Kapitel betrachten wir einzelne Punkte des Funktionsgraphens, die eine
besondere Bedeutung haben. Um diese Punkt zu berechnen, sind Ableitungen
nützlich.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie wissen, was ein **lokales Minimum** und ein **lokales Maximum** sind.
* Sie kennen die Bedingungen für ein Minimum, wenn die Funktion differenzierbar ist.
* Sie kennen die Bedingungen für ein Maximum, wenn die Funktion differenzierbar ist.
```

## Minimum und Maximum

Als nächstes betrachten wir die Funktion

$$f(x) =\frac{\cos(3\pi x)}{x}$$

im Intervall $0.1 \leq x \leq 1.1$. Der Funktionsgraph ist in der folgenden
Abbildung visualisiert.

```{figure} pics/Extrema_example_de.svg
---
width: 50%
name: extrema_example
---
Quelle: Georg-Johann - Eigenes Werk, Gemeinfrei, <https://commons.wikimedia.org/w/index.php?curid=11692680>
```

In diesem Intervall hat die Funktion je ein lokales und globales Minimum und je
ein lokales und globales Maximum. Ein **lokales Minimum** ist ein Funktionswert
$f(x_0)$, so dass in einer Umgebung um die Stelle $x_0$ alle Funktionswerte
größer oder gleich als $f(x_0)$ sind. Ist dieser Funktionswert sogar kleiner
(oder gleich) als alle anderen Funktionswerte für alle $x$ aus der
Definitionsmenge, dann nennt man diesen Funktionswert **globales Minimum**. Der
Punkt $(x_0, f(x_0))$ wird dann **Tiefpunkt** genannt.

Die Begriffe **lokales Maximum** und **globales Maximum** sind analog definiert.
Bei einem lokalen Maximum $f(x_0)$ sind die Funktionswerte in einer Umgebung von
$x_0$ alle kleiner oder gleich diesem Funktionswert. Gilt das sogar für alle
$x$ aus der Definitionsmenge, dann sprechen wir von einem globalen Maximum. Der
Punkt $(x_0, f(x_0))$ wird dann **Hochpunkt** genannt.

Wenn man allgemein von einem Minimum oder einem Maximum sprechen möchte,
verwendet man den Begriff **Extremum** oder **Extremwert**. Der Plural dieser
Fachbegriffe lautet Minima, Maxima und Extrema.

## Vorzeichenwechselkriterium

Wenn eine Funktion differenzierbar ist, ist die Steigung der Tangente an einer
Extremstelle 0. Es gilt also

$$f'(x_0)=0.$$

Bei differenzierbaren Funktionen ist es notwendig, dass die erste Ableitung am
Extremum verschwindet, aber diese Bedingung ist nicht hinreichend. Bei der
Funktion $f(x)=x^3$ ist die erste Ableitung $f'(x)=3x^2$ an der Stelle $x_0$
auch Null, aber diese Funktion hat an dem Punkt $(0,0)$ kein Extremum.
Zusätzlich zu der Bedingung $f'(x)=0$ muss noch das Vorzeichen in einer Umgebung
von $x_0$ wechseln.

Bei einem Minimum wechselt das Vorzeichen der ersten Ableitung von Minus nach
Plus, d.h. gilt zusätzlich

$$f'(x) > 0, \text{ falls } x < x_0 \; \text{ und } \; f'(x) < 0, \text{ falls }
x > x_0,$$

dann hat $f$ an der Stelle $x_0$ ein lokales Minimum.

Bei einem lokalen Maximum erfolgt der Wechsel von Plus nach Minus, also

$$f'(x) < 0, \text{ falls } x < x_0 \; \text{ und } \; f'(x) > 0, \text{ falls }
x > x_0,$$

## Kriterium mit 2. Ableitung

Ist die Funktion zweimal differenzierbar, können wir alternativ zum
Vorzeihenwechselkriterium auch die zweite Ableitung nutzen, um Extremstellen zu
berechen. Es gilt:

* Wenn $f'(x_0) = 0$ und $f''(x_0) < 0$, dann hat $f$ an der Stelle $x_0$ ein
  lokales Maximum $f(x_0)$ bzw. einen Hochpunkt $(x_0, f(x_0))$.
* Wenn $f'(x_0) = 0$ und $f''(x_0) > 0$, dann hat $f$ an der Stelle $x_0$ ein
  lokales Minimum $f(x_0)$ bzw. einen Teifpunkt $(x_0, f(x_0))$.

```{dropdown} Video "lokale Extrema: notwendige Bedingung" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/5qkvVQgjczU"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{dropdown} Video "lokale Extrema: hinreichende Bedingung" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/cpzvX___VZA"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{dropdown} Video "lokale Extrema: Vorzeichenwechselkriterium" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/icHYGCoyyz0"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

Weiteres Material finden Sie hier:

> * <https://studyflix.de/mathematik/extremwerte-berechnen-5248>
> * <https://studyflix.de/mathematik/extrempunkte-berechnen-2127>
> * <https://studyflix.de/mathematik/extremstellen-4147>
> * <https://studyflix.de/mathematik/hochpunkt-und-tiefpunkt-2126>

## Zusammenfassung und Ausblick

Für die Fuktion $f(x)=x^3$ haben wir schon festgestellt, dass die erste
Ableitung Null ist, aber trotzdem dort kein Extremum vorliegt. Auch die zweite
Ableitung ist an dieser Stelle Null und die Krümmung wechselt dort. Solche
Wendestellen betrachten wir im nächsten Kapitel.
