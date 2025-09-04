# 9.3 Rechnen mit konvergenten Folgen

Konvergieren Folgen, darf mit ihnen bzw. ihren Grenzwerten gerechnet werden. So
kann in manchen Fällen der Grenzwert einer komplizierteren Folge aus den
Grenzwerten von einfacheren Folgen zusammengesetzt werden.

## Lernziele

```{admonition} Lernziele
:class: goals
Sie kennen die folgenden Rechenregeln für das Rechnen mit Grenzwerten von Zahlenfolgen und können Sie anwenden:
* Addition: 

$$\lim_{k\rightarrow\infty} (a_k + b_k) = \left( \lim_{k\rightarrow\infty}a_k\right) + \left(\lim_{k\rightarrow\infty}b_k\right) = a + b$$

* Subtraktion: 

$$\lim_{k\rightarrow\infty} (a_k - b_k) = \left(\lim_{k\rightarrow\infty}a_k\right) - \left(\lim_{k\rightarrow\infty}b_k\right) = a-b$$

* Multiplikation: 

$$\lim_{k\rightarrow\infty} (a_k \cdot b_k) = \left(\lim_{k\rightarrow\infty}a_k\right) \cdot \left(\lim_{k\rightarrow\infty} b_k\right) = a\cdot b$$

* Division (falls $b_k \neq 0$ und $b\neq 0$): 

$$\lim_{k\rightarrow\infty}\left(\frac{a_k}{b_k}\right) = \frac{\lim_{k\rightarrow\infty} a_k}{\lim_{k\rightarrow\infty} b_k} = \frac{a}{b}$$

* Potenzierung: 

$$\lim_{k\rightarrow\infty} \left( a_k\right)^r = \left(\lim_{k\rightarrow\infty} a_k\right)^r = a^r $$

* Einschließungsprinzip oder Sandwich-Regel: Ist die Folge $(c_k)$ zwischen $(a_k)$ und $(b_k)$ eingeschlossen, d.h. für alle Folgenglieder gilt $a_k \leq c_k \leq b_k$, dann liegt auch ihr Grenzwert zwischen den beiden anderen Grenzwerten: 

$$ a \leq \lim_{k\rightarrow\infty} c_k \leq b.$$
```

## Rechenregeln konvergente Folgen

Ist bereits bekannt, dass die Folgen $(a_n)$ und die Folge $(b_n)$ konvergieren,
so können wir mit ihren Grenzwerten rechnen. Werden die beiden Folgen addiert,
dann ist der Grenzwert der neuen Folge gleich der Summe der beiden Grenzwerte.

Als Beispiel betrachten wir die beiden Folgen

$$a_n = \frac{1}{n}, \; b_n = \frac{n^2+2}{n^2}.$$

Die erste Folge konvergiert gegen Null, die zweite gegen Eins, also

$$\lim_{n\to\infty}a_n = 0, \; \lim_{n\to\infty}b_n = 1.$$

Aufgrund der Rechenregeln für konvergente Folgen wissen wir, dass folgendermaßen
gerechnet werden darf:

$$\lim_{n\rightarrow\infty} (a_n + b_n) = \left(
\lim_{n\rightarrow\infty}a_n\right) + \left(\lim_{n\rightarrow\infty}n_k\right)
= a + b.$$

Also gilt auch hier, dass die Folge $(c_n)$

$$c_n = a_n + b_n = \frac{1}{n} + \frac{n^2 + 2}{n^2} = \frac{n + n^2 + 2}{n^2}$$

den Grenzwert Eins hat, denn

$$\lim_{n\to\infty}c_n = \lim_{n\to\infty}a_n + \lim_{n\to\infty}b_n = 0 + 1 =
1.$$

Die Folge $(d_n)$ mit $d_n = a_n - b_n$ hat den Grenzwert $-1$, denn

$$d_n = \frac{n - n^2 - 2}{n^2} = 0 - 1 = -1$$

gemäß der Subtraktionsregel

$$\lim_{n\rightarrow\infty} (a_n - b_n) = \left(\lim_{n\rightarrow\infty}a_n\right)
- \left(\lim_{n\rightarrow\infty}b_n\right) = a-b.$$

Analog zu den oben erläuterten Regeln für die Summe und die Differenz von konvergenten Folgen gelten die folgenden weiteren Rechenregeln:

* Multiplikation:

$$\lim_{n\rightarrow\infty} (a_n \cdot b_n) = \left(\lim_{n\rightarrow\infty}a_n\right) \cdot \left(\lim_{n\rightarrow\infty} b_n\right) = a\cdot b$$

* Division (falls $b_n \neq 0$ und $b\neq 0$):

$$\lim_{n\rightarrow\infty}\left(\frac{a_n}{b_n}\right) = \frac{\lim_{n\rightarrow\infty} a_n}{\lim_{n\rightarrow\infty} b_n} = \frac{a}{b}$$

* Potenzierung:

$$\lim_{n\rightarrow\infty} \left( a_n\right)^r = \left(\lim_{n\rightarrow\infty} a_n\right)^r = a^r $$

```{dropdown} Video "Rechenregeln konvergente Folgen" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/vPA8cas-RpE"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

## Beispiel für das Rechnen mit konvergenten Folgen

Der Folge

$$a_n = \frac{3n^4 - 2n^6}{3n^6 - 4n^3}$$

sieht man nicht auf den ersten Blick an, ob sie konvergiert und was ggf. der
Grenzwert ist. Wir können die Folge jedoch umformen, indem wir die höchste
Potenz $n^6$ ausklammern. Dann erhalten wir

$$a_n = \frac{3n^4 - 2n^6}{3n^6 - 4n^3} = \frac{n^6}{n^6}\cdot
\frac{\left(\frac{3}{n^2} - 2\right)}{\left(3 - \frac{4}{n^3}\right)} =
\frac{\frac{3}{n^2} - 2}{3 - \frac{4}{n^3}}.$$

Da die beiden Teilfolgen $\frac{3}{n^2}$ und $\frac{4}{n^3}$ Nullfolgen sind,
also

$$\lim_{n\to\infty} \frac{3}{n^2} = 0, \quad
\lim_{n\to\infty} \frac{4}{n^3} = 0$$

gilt, und darüber hinaus die beiden konstanten Folgen $-2$ und $3$ jeweils gegen
die Grenzwerte $-2$ und $3$ konvergieren, konvergiert die Folge $a_n$ und der
Grenzwert ist

$$\lim_{n\to\infty} a_n = \lim_{n\to\infty}\left(\frac{\frac{3}{n^2} - 2}{3 -
\frac{4}{n^3}}\right) = \frac{0 - 2}{3 - 0} = -\frac{2}{3}.$$

```{dropdown} Video "Grenzwerte von Folgen berechnen" von Mathematrick
<iframe width="560" height="315" src="https://www.youtube.com/embed/oQK8-u1zjdQ"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

Das Thema Rechnen mit konvergenten Folgen können Sie auch auf Studyflix noch
einmal nachlesen und das dazugehörige Video betrachten:

> https://studyflix.de/mathematik/grenzwertsaetze-5990

MATex bietet zufällige Aufgaben mit Lösungen an, um das Rechnen mit Grenzwerten
einzuüben:

> Aufgabengenerator Grenzwerte Zahlenfolgen:
> https://matex.mint-kolleg.kit.edu/MATeX/generatorview.php

## Zusammenfassung und Ausblick

Grenzwerte von Zahlenfolgen sind insbesondere bei schwingenden Systemen
interessant. Im nächsten Kapitel werden wir Zahlenfolgen in Funktionen einsetzen
und die Folgen der Funktionswerte analysieren, was uns zu dem Begriff der
Stetigkeit führen wird.
