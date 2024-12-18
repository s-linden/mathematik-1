# 9.5 Stetigkeit

Stetigkeit ist ein fundamentales Konzept der Mathematik, das in zahlreichen
technischen und ingenieurwissenschaftlichen Anwendungen eine zentrale Rolle
spielt. In der Praxis ist Stetigkeit oft eine Voraussetzung, um Systeme zu
modellieren, zu simulieren und zu analysieren.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können entscheiden, ob eine Funktion **stetig** ist oder nicht.
Mathematisch präzise wird eine Funktion **stetig an der Stelle $x_0$** genannt,
 wenn der Grenzwert der Funktion für $x$ gegen $x_0$ existiert und gleich dem
Funktionswert an der Stelle $x_0$ ist, falls also gilt \begin{equation*}
\lim_{x\rightarrow x_0} f(x) = f(x_0). \end{equation*}
* Die Funktion heißt **stetig**, wenn das für alle Stellen $x_0$ ihres
  Definitionsbereiches gilt.
* Sie wissen, dass die Summe oder Differenz zweier stetiger Funktionen wieder
  stetig ist. Das gilt auch für das Produkt oder den Quotienten zweier stetiger
  Funktionen (sofern nicht durch 0 geteilt wird).
* Sie wissen, dass die Komposition (Verkettung) zweier stetiger Funktionen
  wieder stetig ist. Oder anders ausgedrückt, wenn ich eine stetige Funktion in
  eine andere stetige Funktion einsetze, ist das Ergebnis wieder stetig.
* Sie kennen den **Zwischenwertsatz**. Vereinfacht ausgedrückt können stetige
  Funktionen gezeichnet werden, ohne den Stift abzusetzen.  
* Sie kennen den **Satz vom Minimum und Maximum**.
```

## Was ist Stetigkeit?

Im letzten Kapitel haben Sie gelernt, wie Funktionsgrenzwerte bestimmt werden.
Stetigkeit kann als eine Erweiterung dieses Konzepts verstanden werden. Eine
Funktion ist genau dann stetig, wenn der Grenzwert einer Funktion an einer
Stelle mit dem Funktionswert übereinstimmt.

Mathematisch ausgedrückt bedeutet dies:

```{admonition} Wann ist eine Funktion stetig?
:class: note
Eine reelle Funktion $f$ ist an einer Stelle $x_0$ stetig, wenn der Grenzwert
$\lim_{x\to x_0}f(x)$ existiert und dieser Grenzwert mit dem Funktionswert
$f(x_0)$ übereinstimmt, also

$$\lim_{x \to x_0} f(x) = f(x_0)$$

gilt. Ist die Funktion an allen Stellen des Definitionsgebietes stetig, so
bezeichnet man sie als stetige Funktion.
```

Ist die Funktion $f$ an der Stelle $x_0$ nicht stetig, dann nennt man sie an
dieser Stelle **unstetig**.

Es gibt auch eine alternative Definition von Stetigkeit, das sogenannte
**$\varepsilon$-$\delta$-Kriterium**. Demnach ist eine reelle Funktion $f$ an
der Stelle $x_0$ stetig, wenn zu jedem $\varepsilon > 0$ ein $\delta > 0$
existiert, so dass für alle $x$ der Definitionsmenge mit

$$|x - x_0| < \delta$$

gilt:

$$|f(x) - f(x_0)| < \varepsilon.$$

In dem folgenden Video wird das erste Kriterium für Stetigkeit, das sogenannte
Folgenkriterium verwendet.

```{dropdown} Video "Definition stetige Funktionen" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/2CU9QN5pjME"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

In dem nächsten Video wird ein Beispiel vorgerechnet, wie die Stetigkeit einer
Funktion überprüft werden kann.

```{dropdown} Video "Stetigkeit überprüfen" von Mathematrick
<iframe width="560" height="315" src="https://www.youtube.com/embed/_ke4E-zjI7k?si=xJ-4nocEoruJyx_e" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; 
encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
```

Weiteres Lernmaterial finden Sie hier:

> [https://studyflix.de/mathematik/stetigkeit-3251](https://studyflix.de/mathematik/stetigkeit-3251)

## Beispiele für stetige Funktionen

```{dropdown} Video "Beispiele stetige Funktionen" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/XPXXg1cDMe4"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

```{dropdown} Video "Wichtige stetige Funktionen I" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/kMP1LmadQxM"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

```{dropdown} Video "Wichtige stetige Funktionen II" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/odF1yjnXLQs"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

```{dropdown} Video "Wichtige stetige Funktionen III" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/J-m5Ib76ues"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

## Eigenschaften von stetigen Funktionen

Funktionen, die auf einem abgeschlossenen Intervall $[a,b]\subset\mathbb{R}$
stetig sind, haben zwei wichtige Eigenschaften.

Der Zwischenwertsatz besagt:

```{admonition} Was sagt der Zwischenwertsatz aus?
:class: note
Sei $f$ eine auf einem abgeschlossenen Intervall $[a, b]$ stetige Funktion. Dann
nimmt $f$ jeden beliebigen Wert $y$ zwischen $f(a)$ und $f(b)$ an mindestens
einer Stelle $c\in [a,b]$ an, d.h. $f(c) = y$.
```

Anschaulich bedeutet der Zwischenwertsatz, dass eine stetige Funktion alle Werte
zwischen $f(a)$ und $f(b)$ annimmt, ohne »Sprünge« zu machen. Das hat auch eine
wichtige Konsequenz, falls die Vorzeichen von $f(a)$ und $f(b)$ unterschiedlich
sind.

Betrachten wir beispielsweise die Funktion $f(x) = x^2 - 2$ auf dem Intervall
$[1, 2]$. Wir haben

- $f(1) = -1$ und
- $f(2) = 2$.

Da $f$ stetig ist und die Werte -1 und 2 unterschiedliche Vorzeichen haben,
garantiert der Zwischenwertsatz, dass eine Nullstelle im Intervall $[1, 2]$
existiert. Diese ist tatsächlich $x = \sqrt{2}$.

> [https://studyflix.de/mathematik/zwischenwertsatz-2405](https://studyflix.de/mathematik/zwischenwertsatz-2405)

Der Satz vom Minimum und Maximum besagt:

```{admonition} Was sagt der Satz vom Minimum und Maximum?
:class: note
Eine auf einem abgeschlossenen Intervall $[a, b]$ stetige Funktion besitzt
mindestens einen Punkt $x_{\text{max}} \in [a, b]$, an dem sie ihren Maximalwert
annimmt, und mindestens einen Punkt $x_{\text{min}} \in [a, b]$, an dem sie
ihren Minimalwert annimmt.
```

Dies bedeutet, dass der Graph der Funktion innerhalb eines geschlossenen
Intervalls stets einen höchsten und einen niedrigsten Punkt erreicht.

Wir betrachten als Beispiel die Funktion $f(x) = -x^2 + 4x$, die auf dem
Intervall $[0, 4]$ stetig ist. Sie erreicht

- das Maximum $4$ bei $x = 2$, denn $f(2) = 4$ und
- das Minimum $0$ bei $x = 0$, denn $f(0) = 0$ und zusätzlich $x = 4$, denn
  $f(4)=0$.

Leider liefert dieser Satz nur die Existenz eines Minimums und eines Maximums.
Wie die beiden sogenannten Extremwerte berechnet werden, sagt dieser Satz nicht.
Dazu benötigen wir Ableitungen.

## Zusammenfassung und Ausblick

Funktionen, die auf Intervallen stetig sind, haben besondere Eigenschaften
beschrieben durch den Zwischenwertsatz und den Satz vom Minimum und Maximum.
Diese Eigenschaften sind in der Ingenieurpraxis essentiell, um Nullstellen,
Maxima und Minima von Funktionen zu bestimmen und technische Prozesse zu
modellieren. Im nächsten Kapitel werden wir uns mit unstetigen Funktionen
beschäftigen.
