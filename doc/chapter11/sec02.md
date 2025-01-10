# 11.2 Bestimmtes Integral

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können mit Hilfe der Stammfunktionen ein **bestimmtes Integral** der
  Funktion $f$ in einem Intervall $[a,b]$ berechnen (Hauptsatz der Differential-
  und Integralrechnung).
* Sie wissen, wie das bestimmte Integral mathematisch abgekürzt wird, nämlich
  $\int_{a}^{b} f(x) \, dx$, und können die einzelnen Bestandteile dieser
  Notation bezeichnen:
  * Integralsymbol $\int$,
  * untere Integrationsgrenze $a$,
  * obere Integrationsgrenze $b$,
  * Integrand $f(x)$,
  * Integrationsvariable $dx$.
```

## Bestimmtes Integral

Stammfunktionen sind für viele technische Anwendungen nützlich, weil sie
sozusagen die Umkehrung der Ableitung sind. Das Suchen einer Stammfunktion wird
**Integration** genannt. Eine Anwendung der Stammfunktion ist die Berechnung des
sogenannten bestimmten Integrals. Das **bestimmte Integral** ist wichtig für die
Berechnung von Flächeninhalten, Längen von Kurven und Volumen von
Rotationskörpern.

Der sogenannte **Hauptsatz der Differential- und Integralrechnung** sagt aus,
dass das bestimmte Integral mit Hilfe von Stammfunktionen folgendermaßen
berechnet wird.

```{admonition} Wie wird das bestimmte Integral berechnet?
:class: note
Das bestimmte Integral eine Funktion $f$ in einem Intervall $[a,b]$ wird
berechnet, indem zuerst eine Stammfunktion $F$ gebildet wird. Dann wird in die
Stammfunktion $F$ zuerst $b$ eingesetzt und dann $a$. Aus beiden Werten wird
dann die Differenz gebildet. Diese Zahl heißt bestimmtes Integral von $f$ im
Intervall $[a,b]$.

Mathematisch wird dazu folgende Schreibweise verwendet:

$$\int_{a}^{b} f(x)\, dx = F(b) - F(a).$$
```

```{dropdown} Video: bestimmtes Integral
<iframe width="560" height="315" src="https://www.youtube.com/embed/XtWVTl4fMmY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Beispiel für bestimmtes Integral

Als nächstes soll das bestimmte Integral der Funktion $f(x)= 5x^2$ im Intervall
$[-1,3]$ ausgerechnet werden. Als erstes wird eine Stammfunktion berechnet
(geraten):

$$F(x) = \frac{5}{3}x^3.$$

Danach werden $a=-1$ und $b=3$ in die Stammfunktion eingesetzt und die Differenz
berechnet:

* $F(-1)=\frac{5}{3}(-1)^3 = -\frac{5}{3}$
* $F(3) = \frac{5}{3}(3)^3 = 45$
* Differenz: $F(3) - F(-1) = 45 - \left(-\frac{5}{3}\right) = \frac{140}{3}$.

Damit ist das bestimmte Integral der Funktion $f(x) = 5x^2$ im Intervall
$[-1,3]$ die Zahl $\frac{140}{3}$.

Es ist etwas umständlich, so viel Text in eine Rechnung zu packen. Deshalb ist
folgende Schreibweise üblich:

$$\int_{-1}^{3} 5x^2 \, dx = \left[\frac{5}{3}x^3 \right]_{-1}^{3} = 45 -
\left(-\frac{5}{3}\right) = \frac{140}{3}.$$

Zuerst kommt die mathematische Schreibweise für das bestimme Integral mit

$$\int_{-1}^{3}  5x^2 \, dx.$$

Das geschwungene $\int$ wird **Integralsymbol** genannt. Der Anfang des
Intervalls, hier also -1, wird **untere Integrationsgrenze** genannt. Das Ende
des Intervalls, hier also 3, wird **obere Integrationsgrenze** genannt. Die
Funktion, von der die Stammfunktion gesucht wird, hier also $f(x)=5x^2\, dx$,
wird **Integrand** genannt. Da manchmal Funktionen auch Parameter enthalten,
muss eindeutig geklärt werden, welches die Variable der Funktion ist. Das wird
durch die **Integrationsvariable** spezifiziert, hier $dx$. Warum da ein "d"
dabei steht, kommt in einem späteren Kapitel.

In der Rechnung muss als erstes die Stammfunktion $F$ berechnet werden. Um klar
zu machen, dass das jetzt die Stammfunktion ist, werden sehr große eckige
Klammern verwendet, hier also $\left[\frac{5}{3}x^3\right]$. Für die
Integrationsvariable $c$ wählen wir Null. In der anschließenden Differenzbildung
würde sie ohnehin wegfallen. Zuletzt folgt noch das Einsetzen der
Integrationsgrenzen in die Stammfunktion. Zuerst wird die obere
Integrationsgrenze $b=3$ eingesetzt, hier also $F(3)=45$, und dann der Wert
der Stammfunktion an der unteren Integrationsgrenze, hier also
$F(-1)=-\frac{5}{3}$ subtrahiert.

Im folgenden Video finden Sie weitere Beispiele.

```{dropdown} Video: bestimmtes Interal - Beispiele
<iframe width="560" height="315" src="https://www.youtube.com/embed/aEtIsjWr0dg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Integrale als Fläche interpretiert

Bisher ist das bestimmte Integral über $f$ von $a$ bis $b$ einfach eine Zahl,
die als Differenz von der Stammfunktion $F$ an den Stellen $a$ und $b$ bestimmt
wird, also $F(b)-F(a)$. Je nach Anwendung wird dieser Zahl eine ganz bestimmte
Bedeutung gegeben. Als ersten und wichtigsten Fall betrachten wir das Integral
in der Geometrie. Hier entspricht das Integral von $a$ bis $b$ über $f$ dem
**orientierten Flächeninhalt** zwischen dem Funktionsgraphen $f(x)$ und der
x-Achse. Aber was ist eigentlich der orientierte Flächeninhalt?  

Wenn alle Funktionswerte $f(x)$ oberhalb der x-Achse liegen, dann ist $f(x)\geq
0$ für alle $x$ im Intervall $[a,b]$. Dann ist der Flächeninhalt zwischen
$f(x)$, der x-Achse und den Geraden $x=a$ und $x=b$ gleich dem Integral über $f$ , d.h.

$$A = \int_{a}^{b} f(x)\, dx.$$

Liegen aber alle Funktionswerte $f(x)$ unterhalb der x-Achse, so ist das
Integral negativ. Aber eigentlich entspricht es auch der Fläche, nur sind
Flächen natürlich immer positiv. Deswegen sagen wir, der Flächeninhalt ist
orientiert. Liegt die Fläche oberhalb der x-Achse, so wird diese positiv
gewertet. Liegt sie unterhalb der x-Achse, wird der orientierte Flächeninhalt
mit einem Minus versehen, um klar zu machen, dass diese Fläche unterhalb der
x-Achse liegt.

In dem folgenden Video wird die Flächeninterpretation des Integrals nochmal
erläutert und auch gezeigt, wie diese Interpretation bei punktsymmetrischen
Funktionen ausgenutzt werden kann, sich selbst das Rechnen etwas zu erleichtern.

```{dropdown} Video: bestimmtes Integral - Flächeninterpretation
<iframe width="560" height="315" src="https://www.youtube.com/embed/6rJOt8mWY_I" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Zusammenfassung und Ausblick

Jetzt kennen wir den Zusammenhang zwischen Stammfunktion und dem bestimmten
Integral. Als nächstes lernen wir die Rechenregeln für das bestimmte Integral.
