# 10.6 Ableitung der Umkehrfunktion

Die Ableitung einer Funktion liefert die Steigung ihrer Tangente an einem bestimmten Punkt. Doch was passiert, wenn wir nicht nur die Funktion, sondern auch ihre Umkehrfunktion betrachten? Wie hängen ihre Ableitungen zusammen?

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können die Umkehrfunktion ableiten, also 

$$\left(f^{-1}(y)\right)' = \frac{1}{f'(x)},$$

wobei $y=f(x)$ und $x=f^{-1}(y)$.
```

## Was ist eine Umkehrfunktion?

Die Umkehrfunktion kehrt die Zuordnung einer Funktion um, sodass sie zu jeden
Funktionswert den ursprünglichen Wert liefert. Beispielsweise ist die
Umkehrfunktion von $f(x) = x^2$ (für $x \geq 0$) die Funktion $f^{-1}(x) =
\sqrt{x}$.

Eine interessante Fragestellung dabei ist: Wie verhalten sich die Ableitungen
$f'$ und $(f^{-1})'$, wenn die Umkehrfunktion differenzierbar ist? Dies wollen
wir systematisch untersuchen.

Um die Ableitung der Umkehrfunktion zu untersuchen, müssen wir erst einmal
voraussetzen, dass zu einer reellen Funktion $f$ die Umkehrfunktion $f^{-1}$
existiert. Wir setzen also voraus, dass $f: D \to W$ eine bijektive Funktion
ist, also eine Funktion, die injektiv und surjektiv ist. $D$ ist die
Definitionsmenge und $W$ die Wertemenge. Die Umkehrfunktion $f^{-1}$ ist
definiert durch:

\begin{align*}
f^{-1}(f(x)) = x, \quad & \text{ für alle } x \in D,\\
f(f^{-1}(y)) = y, \quad & \text{ für alle } y \in W.
\end{align*}

## Ableitung der Umkehrfunktion

Nachdem wir wiederholt haben, was eine Umkehrfunktion ist, wenden wir uns nun
der Ableitung zu. Dazu setzen wir voraus, dass die Funktion $f$ differenzierbar
ist und dass $f^{-1}$ existiert und ebenfalls differenzierbar ist. Dann gilt

$$\left(f^{-1}(y)\right)' = \frac{1}{f'(x)},$$

wobei $y=f(x)$ und $x=f^{-1}(y)$.

Diese Formel ergibt sich aus der Kettenregel. Zur Herleitung setzen wir $y =
f(x)$ und differenzieren die Identität $f(f^{-1}(y)) = y$ nach y:

$$\left(f(f^{-1}(y))\right)' \cdot (f^{-1}(y))' = 1.$$

Auflösen nach $(f^{-1}(y))'$ liefert die obige Beziehung.

```{dropdown} Video "Umkehrfunktion ableiten" von Mathematrick
<iframe width="560" height="315" src="https://www.youtube.com/embed/77DjMQsv1rA"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

## Zusammenfassung und Ausblick

In diesem und den letzten Kapitel haben wir uns mit der Ableitung von Funktionen
beschäftigt. In den nächsten Kapiteln werden wir Ableitungen anwenden um
beispielsweise geometrische Probleme zu lösen.
