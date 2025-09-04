# 11.4 Monotonie und Krümmung

Als nächstes betrachten wir Monotonie und Krümmung.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie wissen, was **höhere Ableitungen** sind.
* Die erste Ableitung an der Stelle $x_0$ beschreibt das **Monotonieverhalten**
  einer Funktion $f$ in der unmittelbaren Umgebung von $x_0$. Ist $f'(x_0)<0$,
  dann fällt die Funktion. Ist $f'(x_0)>0$, dann wächst die Funktion.
* Die zweite Ableitung an der Stelle $x_0$ beschreibt das **Krümmungsverhalten**
  der Funktion in der näheren Umgebung von $x_0$. Ist $f''(x_0)<0$, so haben wir
  Rechtskrümmung. Ist $f''(x_0)>0$, so Linkskrümmung.
```

## Höhere Ableitungen

Ist die Ableitung $f'$ einer Funktion wiederum differenzierbar, so bezeichnen
wir ihre Ableitung als zweite Ableitung von $f$ und notieren sie mit zwei
Strichen: $f''$. Ist nun die zweite Ableitung wiederum differenzierbar, dann
bezeichnen wir ihre Ableitung als dritte Ableitung: $f'''$. Alternativ dürfen
diese sogenannten höheren Ableitungen auch mit einer Zahl notiert werden:

$$f''=f^{(2)}, \quad f'''= f^{(3)}.$$

Ab der vierten Ableitung sind nur noch Zahlen üblich: $f^{(4)}, f^{(5)},
\ldots$.

Beispiel: Das Polynom vierten Grades

$$f(x) = 2x^4 + 5x^3 -7x^2 + x +2$$

ist unendlich oft differenzierbar. Die ersten sieben Ableitungen lauten:

\begin{align*}
f'(x)      &= 8x^3 + 15x^2 - 14x + 1 \\
f''(x)     &= 24x^2 + 30x - 14 \\
f'''(x)    &= 48x + 30 \\
f^{(4)}(x) &= 48 \\
f^{(5)}(x) &= 0 \\
f^{(6)}(x) &= 0 \\
f^{(7)}(x) &= 0 \\
\vdots\; &= \;\vdots \\
\end{align*}

## Monotonie

Den Begriff Monotonie haben wir schon bei Folgen kennengelernt. Bei Funktionen
wird Monotonie analog definiert.

Wir betrachten alle Stellen $x_1$ und $x_2$ mit der Eigenschaft $x_1 < x_2$.
Dann vergleichen wir die zugehörigen Funktionswerte $f(x_1)$ und $f(x_2)$. Je
nachdem, wie der Vergleich ausfällt, führen wir die folgenden Bezeichnungen ein:

* $f$ ist streng monoton fallend, wenn $f(x_1) > f(x_2)$,
* $f$ ist monoton fallend, wenn $f(x_1) \geq f(x_2)$,
* $f$ ist streng monoton wachsend, wenn $f(x_1) < f(x_2)$ und
* $f$ ist monoton wachsend, wenn $f(x_1) \leq f(x_2)$.

Manchmal wird auch der Begriff steigend für wachsend verwendet und strikt für
streng. Eine Funktion kann aber keine der vier oben genannten
Monotonieeigenschaften haben.

Ist eine Funktion differenzierbar, dann können wir das Monotonieverhalten mit
der ersten Ableitung bestimmen:

* Ist $f'(x)>0$ für alle $x$, dann wächst $f$ streng mononton.
* Ist $f'(x)<0$ für alle $x$, dann fällt $f$ streng monoton.

Die Umkehrung gilt nicht. Es gibt auch streng monotone Funktionen, bei der die
erste Ableitung Null wird. Beispielsweise ist die Funktion $f(x)=x^3$ streng
monoton wachsend, aber die erste Ableitung an der Stelle $x_0 = 0$ wird Null.

> * [https://studyflix.de/mathematik/monotonie-2157](https://studyflix.de/mathematik/monotonie-2157)
> * [https://studyflix.de/mathematik/monotonieverhalten-4227](https://studyflix.de/mathematik/monotonieverhalten-4227)

```{dropdown} Video "Monotonie" von Mathematrick
<iframe width="560" height="315" src="https://www.youtube.com/embed/R0zBCociKiI"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Krümmung

Die Krümmung beschreibt die Veränderung der Steigung. Wir unterscheiden zwischen
links- und rechtsgekrümmten Funktionen bzw. eine Funktion kann auch gar keine
Krümmung haben. Befinden wir uns an der Stelle $x_0$ und ist die Funktion $f$
zwei differenzierbar, dann können wir die Krümmung durch die zweite Ableitung
beschreiben:

* $f''(x_0) < 0$: rechtsgekrümmt, die Steigung nimmt ab
* $f''(x_0) > 0$: linksgekrümmt, die Steigung nimmt zu

Wietere Details finden Sie und in dem nachfolgenden Video.

> [https://studyflix.de/mathematik/kruemmungsverhalten-5168](https://studyflix.de/mathematik/kruemmungsverhalten-5168)

```{dropdown} Video "Krümmung einer Funktion" von Mathematrick
<iframe width="560" height="315" src="https://www.youtube.com/embed/a1QIlo7Xf_A"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Zusammenfassung und Ausblick

Die Eigenschaften Monotonie und Krümmung fokussieren sich auf das generelle
Verhalten einer Funktion auf einem Intervall. In den nächsten Kapiteln
betrachten wir einezelne Punkte, die von besonderer Bedeutung für einen
Funktionsgraphen sind.
