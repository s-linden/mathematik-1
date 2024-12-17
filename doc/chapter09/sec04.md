# 9.4 Funktionsgrenzwerte und ihre Rechenregeln

Grenzwerte spielen nicht nur bei Folgen eine zentrale Rolle, sondern auch bei
Funktionen. Beispielsweise kann das Verhalten eines schwingenden Systems bei
unendlich vielen Zyklen durch einen Grenzwert beschrieben werden. Oder in einem
Wärmetauscher nähert sich die Temperatur einem Grenzwert. Trotz der vielfältigen
Anwendungen bleiben wir in diesem Kapitel bei der mathematischen
Betrachtungsweise von Funktionsgrenzwerten.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie wissen, was ein **Funktionsgrenzwert** ist. Dazu wird eine Folge von Zahlen $(x_n)$ genommen, die gegen den Grenzwert $x_0$ konvergiert, und dann in die Funktion $f$ eingesetzt. Wenn dann die dadurch entstehende Folge $f(x_n)$ konvergent ist, nennt man diesen Grenzwert $F$ Funktionsgrenzwert von der Funktion $f$ an der Stelle $x_0$. Wir schreiben entweder
\begin{equation*}
\lim_{x\rightarrow x_0} f(x) = F \quad \text{ oder } \quad f(x)\rightarrow F \text{ für } x \rightarrow x_0. 
\end{equation*}
* Sie können Funktionsgrenzwerte von links und von rechts unterscheiden. Mit Funktionsgrenzwert von links meint man, dass man nur Zahlenfolgen betrachtet, für die $(x_n)$ kleiner als $x_0$ ist und die sich $x_0$ von links annähern. Umgekehrt meint der Funktionsgrenzwert von rechts, das man nur Zahlenfolgen $(x_n)$ nimmt, die sich $x_0$ von rechts annähern. Man verwendet die beiden Schreibweisen
\begin{align*}
\text{linksseitig:} \quad \lim_{x\rightarrow x_0^{\textcolor{blue}{-}}} f(x) = F \quad &\text{ bzw.} \quad \lim_{x\textcolor{blue}{\nearrow} x_0} f(x) = F \\
\text{rechtsseitig:} \quad \lim_{x\rightarrow x_0^{\textcolor{blue}{+}}} f(x) = F \quad &\text{ bzw.} \quad \lim_{x\textcolor{blue}{\searrow} x_0} f(x) = F 
\end{align*}
* Sie kennen die Rechenregeln für Funktionsgrenzwerte, also wenn $f$ und $g$ Funktionen sind mit $\lim_{x\rightarrow x_0}f(x)=F$ und $\lim_{x\rightarrow x_0}g(x)=G$, dann gilt
    * Addition: $\lim_{x\rightarrow x_0} (f(x)+g(x)) = F+G$
    * Subtraktion: $\lim_{x\rightarrow x_0} (f(x)-g(x)) = F-G$
    * Multiplikation: $\lim_{x\rightarrow x_0} (f(x)\cdot g(x)) = F\cdot G$
    * Division: $\lim_{x\rightarrow x_0} \left(\frac{f(x)}{g(x)} \right) = \frac{F}{G}\quad$ (vorausgesetzt $g(x), \,G\neq 0$)
```

## Was ist ein Funktionsgrenzwert?

Ein **Funktionsgrenzwert** beschreibt, wie sich eine Funktion $f(x)$ verhält,
wenn sich der Wert von $x$ einem bestimmten Punkt $x_0$ annähert. Betrachten wir
die Funktion

$$f(x) = 2x + 1$$

und untersuchen, was mit $f(x)$ passiert, wenn sich $x$ dem Punkt $x_0 = 3$
annähert. Dazu konstruieren wir eine Folge $(x_n)$, die gegen $x_0 = 3$
konvergiert, beispielsweise die Folge

$$x_n = 3 - \frac{1}{n^2}.$$

Damit ergeben sich die folgenden Funktionswerte:

|n|$x_n$|$f(x_n)$|
|---|---|---|
|1|2.000000|5.000000|
|2|2.750000|6.500000|
|3|2.888889|6.777778|
|4|2.937500|6.875000|
|5|2.960000|6.920000|
|6|2.972222|6.944444|
|7|2.979592|6.959184|
|8|2.984375|6.968750|
|9|2.987654|6.975309|
|10|2.990000|6.980000|

Wir haben die Vermutung, dass sich die Folge der Funktionswerte $f(x_n)$ dem
Grenzwert $F=7$ nähert.

Wir hätten auch eine andere Folge $(x_n)$ wählen können, z.B.

$$x_n = 3 + \frac{1}{2n}.$$

Dann würden sich folgenden Funktionswerte ergeben:

|n|$x_n$|$f(x_n)$|
|---|---|---|
|1|3.500000|8.000000|
|2|3.250000|7.500000|
|3|3.166667|7.333333|
|4|3.125000|7.250000|
|5|3.100000|7.200000|
|6|3.083333|7.166667|
|7|3.071429|7.142857|
|8|3.062500|7.125000|
|9|3.055556|7.111111|
|10|3.050000|7.100000|

Es bleibt bei dem Verdacht, dass der Grenzwert der Folge der Funktionswerte
$F=7$ ist.

```{admonition} Was ist ... ein Funktionsgrenzwert?
:class: notes
Wenn für jede Folge $(x_n)$, die gegen einen Grenzwert $x_0$ konvergiert, auch
die Folge der Funktionswerte $f(x_n)$ konvergiert, nennt man diesen Grenzwert
Funktionsgrenzwert. Wir schreiben

$$\lim_{x\to x_0}f(x) = F \; \text{ oder } \; f(x) \to F \text{ für } x\to x_0.$$
```

```{dropdown} Video "Grenzwerte von Funktionen" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/hbtp6cuCgbo" 
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; 
encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

## Links- und rechtsseitiger Grenzwert

In dem Beispiel haben wir zwei verschiedene Zahlenfolgen verwendet, um den
Funktionsgrenzwert zu bestimmen. Allgemein wird zwischen Folgen unterschieden,
die sich der Stelle $x_0$ von links nähern wie die Folge

$$x_n = 3 - \frac{1}{n^2}$$

und Folgen, die sich der Stelle $x_0$ von rechts nähern, wie die Folge

$$x_n = 3 + \frac{1}{2n}.$$

Wenn ein Funktionsgrenzwert existiert, ist es egal, ob wir uns von links oder
rechts nähern, denn jede Folge muss ja konvergieren. Es gibt aber auch
Funktionen, die keinen Funktionsgrenzwert an der Stelle $x_0$ haben,
beispielsweise weil die Funktion an der Stelle $x_0$ springt. Dennoch kann es
interessant sein, den Grenzwert der Funktionswerte von links und von rechts zu
untersuchen. Daher halten wir hier noch fest, was einseitige Grenzwerte von
links und rechts sind.

Wenn wir eine Folge $(x_n)$ benutzen, die gegen $x_0$ konvergiert, aber stets
kleiner als $x_0$ bleibt, dann wird der zugehörige Funktionsgrenzwert als
linksseitiger Grenzwert bezeichnet. In mathematischer Notation schreiben wir
linksseitige Grenzwerte folgendermaßen (beachten Sie bitte das kleine rote Minus
bzw. den kleinen roten Pfeil):

$$ \lim_{x\rightarrow x_0^{\textcolor{red}{-}}} f(x) = F \quad \text{ bzw.}
\quad \lim_{x\textcolor{red}{\nearrow} x_0} f(x) = F $$

Rechtsseitige Funktionsgrenzwerte sind analog dazu definiert. Die Folgenglieder
$x_n$ müssen alle größer sein als die Stelle $x_0$:

$$\lim_{x\rightarrow x_0^{\textcolor{red}{+}}} f(x) = F \quad \text{ bzw.} \quad
\lim_{x\textcolor{red}{\searrow} x_0} f(x) = F$$

```{dropdown} Video "Einseitige Grenzwerte von Funktionen" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/0Qc42YohWYs"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

## Rechenregeln für Funktionsgrenzwerte

Die Rechenregeln für Funktionsgrenzwerte sind dieselben wie die Rechenregeln von
konvergenten Folgen. Daher listen wir sie hier nur auf, ohne ins Detail zu
gehen:

Wenn $f$ und $g$ Funktionen sind mit

$$\lim_{x\rightarrow x_0}f(x)=F$$

und

$$\lim_{x\rightarrow x_0}g(x)=G,$$

dann gilt

* Addition:

$$\lim_{x\rightarrow x_0} (f(x)+g(x)) = F+G$$

* Subtraktion:

$$\lim_{x\rightarrow x_0} (f(x)-g(x)) = F-G$$

* Multiplikation:

$$\lim_{x\rightarrow x_0} (f(x)\cdot g(x)) = F\cdot G$$

* Division (vorausgesetzt $g(x)\neq 0, \,G\neq 0$):

$$\lim_{x\rightarrow x_0} \left(\frac{f(x)}{g(x)} \right) = \frac{F}{G}$$

```{dropdown} Video "Rechenregeln Funktionsgrenzwerte" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/A-39_aG6v9A"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

## Zusammenfassung und Ausblick

Mit Hilfe von Funktionsgrenzwerten werden wir im nächsten Kapitel klären, ob
eine Funktion stetig ist oder nicht.
