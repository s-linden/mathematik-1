# 8.6 Potenzen und Wurzeln komplexer Zahlen

Auf die komplexen Zahlen stießen wir, indem wir versuchten, die Gleichung $z^2 =
-1$ zu lösen. In diesem Kapitel beschäftigen wir uns nun mit dem Potenzieren und
Wurzelziehen für komplexe Zahlen.


## Lernziele

```{admonition} Lernziele 
:class: goals
* Sie können eine komplexe Zahl potenzieren.
* Sie können aus einer komplexen Zahl die Wurzel ziehen.
```


## Potenzen von komplexen Zahlen

Die Potenz einer komplexen Zahl ist – genau wie bei den reellen Zahlen – eine
Abkürzung für das wiederholte Multiplizieren einer Zahl mit sich selbst. 

\begin{align*}
z^2 &= z\cdot z \\
z^3 &= z \cdot z \cdot z \\
z^4 &= z \cdot z \cdot z \cdot z \\
z^5 &= z \cdot z \cdot z \cdot z \cdot z\\
\vdots 
\end{align*}

Die Zahl $z$ heißt Basis und die Anzahl, wie oft die Basis mit sich selbst
multipliziert wird, heißt Exponent oder Hochzahl. Es gibt auch negative Potenzen:

\begin{align*}
z^{-2} &= \frac{1}{z\cdot z} \\
z^{-3} &= \frac{1}{z \cdot z \cdot z} \\
z^{-4} &= \frac{1}{z \cdot z \cdot z \cdot z} \\
z^{-5} &= \frac{1}{z \cdot z \cdot z \cdot z \cdot z}\\
\vdots 
\end{align*}

Wenn nun konkret eine Potenz einer komplexen Zahl ausgerechnet werden soll, ist
die Exponentialform am besten geeignet, wie das folgende Beispiel zeigt. Wir
möchten von der komplexen Zahl $z = 3e^{\frac{\pi}{4}\mathrm{i}}$ die Potenzen
bis 4 bilden.

Für die 2. Potenz erhalten wir zufälligerweise eine rein imaginäre Zahl, wie die
folgende Rechnung zeigt:

\begin{align*}
z^2 
&= \left( 3e^{\frac{\pi}{4}\mathrm{i}} \right) \cdot \left( 3e^{\frac{\pi}{4}\mathrm{i}} \right)\\
&= 3^2 \cdot e^{\left(\frac{\pi}{4}+\frac{\pi}{4}\right)\mathrm{i}} \\
&= 9 \, e^{\frac{\pi}{2} \mathrm{i}} \\
&= 9\mathrm{i}.
\end{align*}

Für die 3. Potenz erhalten wir

\begin{align*}
z^3 
&= \left( 3e^{\frac{\pi}{4}\mathrm{i}} \right) \cdot \left( 3e^{\frac{\pi}{4}\mathrm{i}} \right)\cdot \left( 3e^{\frac{\pi}{4}\mathrm{i}} \right)\\
&= 3^3 \cdot e^{\left(\frac{\pi}{4}+\frac{\pi}{4}+\frac{\pi}{4}\right)\mathrm{i}} \\
&= 27 \, e^{\frac{3}{4}\pi \mathrm{i}} \\
&\approx -19.0919 + 19.0919 \, \mathrm{i}.
\end{align*}

Und die 4. Potenz ist zufälligerweise rein reell:

\begin{align*}
z^4 
&= \left( 3e^{\frac{\pi}{4}\mathrm{i}} \right) \cdot \left( 3e^{\frac{\pi}{4}\mathrm{i}} \right) \cdot \left( 3e^{\frac{\pi}{4}\mathrm{i}} \right) \cdot \left( 3e^{\frac{\pi}{4}\mathrm{i}} \right)\\
&= 3^4 \cdot e^{\left(\frac{\pi}{4}+\frac{\pi}{4}+\frac{\pi}{4}+\frac{\pi}{4}\right)\mathrm{i}} \\
&= 81 \cdot e^{\pi \mathrm{i}} \\
&= 81 \cdot (-1) \\
&= -81.
\end{align*}

Zusammengefasst gilt für das Potenzieren von komplexen Zahlen die folgende
Rechenregel.

```{admonition} Wie wird eine komplexe Zahl potenziert?
:class: note
Für jeden ganzzahligen Exponenten $n$ wird die n-te Potenz einer komplexen Zahl
$z = r e^{\varphi\,\mathrm{i}}$ berechnet, indem der Betrag $r$ mit $n$ potenziert
wird und das Argument $\varphi$ mit $n$ multipliziert wird:

$$z^n = \big(r e^{\varphi\,\mathrm{i}}\big)^n = r^n e^{n\, \varphi \, \mathrm{i}}.$$
```

Wie geht man vor, wenn die komplexe Zahl in Normalform oder trigonometrischer
Form vorliegt? In Normalform können die Klammern einfach ausmultipliziert
werden. Bei höhereren Potenzen ist es nur etwas schwierig, den Überblick über die
einzelnen Terme zu behalten. Für die trigonometrische Form gibt es den [Satz von
de Moivre](https://de.wikipedia.org/wiki/Moivrescher_Satz). 

```{dropdown} Video "Komplexe Zahlen potenzieren" von MathePeter
<iframe width="560" height="315" src="https://www.youtube.com/embed/G_FRNyHpzrk" 
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; 
encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```


## Wurzelziehen von komplexen Zahlen

TODO


## Weiteres Lernmaterial

```{dropdown} Video 
<iframe width="560" height="315" src="https://www.youtube.com/embed/BKdqTn2iO4s" title="YouTube video player" 
frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```


## Zusammenfassung und Ausblick

TODO