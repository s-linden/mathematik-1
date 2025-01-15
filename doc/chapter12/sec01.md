# 12.1 Linearisierung

Die Welt, in der wir leben, ist selten linear. Dennoch können wir viele Prozesse
in einer ersten Näherung als linear behandeln. In diesem Kapitel beschäftigen
wir uns daher mit der Linearisierung von nichtlinearen Funktionen.

## Lernziele

```{admonition} Lernziele
:class: goals
Sie wissen, dass eine nichtlineare Funktion **linearisiert** werden kann. Damit
ist gemeint, dass die nichtlineare Funktion $f:\mathbb{R}\to\mathbb{R}$
näherungsweise durch die lineare Funktion

$$T(x) = f(x_0) + f'(x_0)\cdot (x-x_0)$$

ersetzt werden kann. Das stimmt nur in der Nähe des sogenannten
**Arbeitspunktes** $(x_0,f(x_0))$.
```

## Idee der Linearisierung

Die Kernidee der Linearisierung liegt in der Annäherung einer Funktion durch
eine lineare Funktion an einem bestimmten Punkt. Die folgende Grafik zeigt, wie
die nichtlineare Exponentialfunktion $f(x) = \exp(x)$ in dem Punkt $(0, 1)$
durch die lineare Funktion

$$T(x) = x + 1$$

angenähert wird. In der Mathematik sagt man auch, die Exponentialfunktion wird
in dem Punkt $(0, 1)$ durch die lineare Funktion **approximiert**.

```{figure} pics/Exp_e.svg
---
width: 50%
name: Exp_e
---
Quelle: Von Marcel Marnitz, reworked by user:Georg-Johann - Selbst erstellt (own work using GeoGebra),
completely reworked 2010-08-22, Gemeinfrei, https://commons.wikimedia.org/w/index.php?curid=5905583
```

Im Folgenden beschreiben wir, wie man auf die Funktionsgleichung der linearen Funktion kommt.

## Tangentenansatz

Der Tangentenansatz ist eine wichtige Methode zur Linearisierung von
eindimensionalen Funktionen. Er wird für Funktionen verwendet, die abgeleitet
werden können. Der Tangentenansatz basiert auf der Idee, dass eine Funktion in
der Nähe eines bestimmten Punktes durch ihre Tangente genähert werden kann.

Geometrisch betrachtet ist die Tangente an einer Funktion die gerade Linie, die
die Funktion in dem Arbeitspunkt $(x_0, f(x_0)$ berührt und deren Steigung
$f'(x_0)$ entspricht. Generell hat die Gerade die Funktionsgleichung

$$y = m\cdot x + b$$

mit der Steigung $m$ und dem y-Achsenabschnitt $b$. Wenn die Funktion $f$
differenzierbar ist, stimmt die Steigung der Tangente mit der ersten Ableitung
$f'(x_0)$ über ein, es gilt also $m = f'(x_0)$. Jetzt setzen wir den Punkt
$(x_0, f(x_0))$ in die Geradengleichung $y = m\cdot x + b$ ein und erhalten für
$b$ den Term $f(x_0) - f'(x_0)\cdot x_0$. Somit lässt sich die
Funktionsvorschrift der Tangente schreiben als

$$T(x) = f(x_0) + f'(x_0) \cdot (x - x_0).$$

In der Nähe dieses Punktes liegt die Tangente sehr nah an der Funktion und
bietet somit eine einfache lineare Beschreibung des ursprünglich nichtlinearen
Verhaltens.

```{dropdown} Video "Tangentenfunktion" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/9-sYXAkbJQQ"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Beispiel

Linearisiere die Funktion $f(x)=\sin(x)$ im Punkt $x_0 = \frac{\pi}{4}$.

Als erstes bestimmen wir den Funktionswert an der Stelle $x_0 = \frac{\pi}{4}$.
Es gilt

$$f(x_0)= f\left(\frac{\pi}{4}\right) = \sin\left(\frac{\pi}{4} \right) =
\frac{\sqrt{2}}{2}.$$

Als zweites berechnen wir die Ableitung der Funktion $f(x)=\sin(x)$:

$$f'(x) = \cos(x).$$

Der Wert der Ableitung an der Stelle $x_0 = \frac{\pi}{4}$ ist

$$f'\left(\frac{\pi}{4}\right) = \cos\left(\frac{\pi}{4}\right) =
\frac{\sqrt{2}}{2}.$$

Eingesetzt in die Tangentenfunktion

$$T(x) = f(x_0) + f'(x_0) \cdot (x - x_0)$$

erhalten wir somit die Linearisierung von $f(x)=\sin(x)$

$$T(x) = \frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{2} \cdot \left(x -
\frac{\pi}{4}\right).$$

Diese Funktionsvorschrift können wir noch zur

$$T(x) = \frac{\sqrt{2}}{2} \cdot x - \frac{\sqrt{2}\pi}{8} +
\frac{\sqrt{2}}{2}$$

vereinfachen. Die folgende Grafik zeigt die Sinusfunktion und ihre
Linearisierung im Arbeitspunkt $(\frac{\pi}{4}, \frac{\sqrt{2}}{2})$.

```{figure} pics/tangente_sinus.svg
---
width: 75%
name: tangente_sinus
---
```

## Zusammenfassung und Ausblick

In der Mathematik 2 werden wir lernen, wir wir beispielsweise eine quadratische
Funktion an eine Funktion $f$ annähern. Allgemein können beliebige Polynome
benutzt werden, um eine Funktion au approximieren. Diese Polynome heißen
Taylorpolynome.
