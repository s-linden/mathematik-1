# 12.3 Neigungswinkel / Schnittwinkel

Mit Ableitungen lassen sich geometrische Eigenschaften des Funktionsgraphens
bestimmen. In diesem Kapitel geht es um den Neigungsewinkel und den
Schnittwinkel.

## Lernziele

```{admonition} Lernziele
:class: goals
* Die erste Ableitung einer Funktion beschreibt den Neigungswinkel an dem Punkt
  $(x_0, f(x_0))$, also $f'(x_0) = \tan (\alpha)$. 
* Wenn zwei Funktionen sich in dem Punkt $(x_0,y_0)$ treffen, dann sind sie
  senkrecht zueinander, wenn $f'(x_0)\cdot g'(x_0)=-1$ gilt. Und sie berühren
  sich nur, wenn $f'(x_0) = g'(x_0)$.
```

## Neigungswinkel

Der **Neigungswinkel**, manchmal auch **Steigungswinkel** genannt, ist derjenige
Winkel, den eine Gerade mit der x-Achse hat. Da bei einer Gerade die Steigung
konstant ist, muss der Winkel nicht an der Nullstelle abgelesen werden, sondern
kann auch an anderen Stellen über das Steigungsdreieck bestimmt werden, wie die
folgende Abbildung zeigt.

```{figure} pics/neigungswinkel.svg
---
width: 75%
name: neigungswinkel
---
```

Die Steigung $m$ einer Gerade $f(x) = m\cdot x + b$ ist gegeben als

$$m = \frac{\Delta y}{\Delta x}.$$

Wenn wir das Steigungsdreieck einzeichnen, sehen wir aber auch, dass der
Neigungswinkel $\alpha$ über den Tangens berechnet werden kann. Es gilt also

$$m = \tan(\alpha).$$

Wenden wir die Arkustangensfunktion an, können wir so den Neigungswinkel aus der
Steigung der Geraden berechnen:

$$\alpha = \arctan(m).$$

Der Begriff des Neigungs- oder Steigungswinkel lässt sich von Geraden auch auf
andere Funktionen übertragen. Handelt es sich jedoch nicht um eine Gerade, so
variiert der Winkel und ist abhängig von dem Punkt $(x_0, y_0)$ auf dem
Funktionsgraphen, an dem der Neigungswinkel bestimmt werden soll.

```{admonition} Was ist ... der Neigungswinkel?
:class: note
Der Neigungswinkel im Punkt $(x_0, f(x_0))$ einer Funktion $f$ ist der Winkel
$\alpha$, den ihre Tangente an dieser Stelle mit der x-Achse bildet. Da die
Steigung der Tangente an dieser Stelle durch die erste Ableitung $f'(x_0)$
gegeben ist, erhalten wir

$$\tan(\alpha) = f'(x_0).$$
```

```{dropdown} Video "Steigungswinkel berechnen" von Mister Mathe
<iframe width="560" height="315" src="https://www.youtube.com/embed/oraxntrhRYI"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Schnittwinkel

Der Schnittwinkel für den Punkt $(x_0,y_0)$ ist definiert für zwei beliebige
Funktionen $f$ und $g$, die sich in diesem Punkt schneiden. An jede der beiden
Funktionen kann eine Tangente gelegt werden. Der Schnittwinkel ist dann der
Winkel, den die beiden Tangenten einschließen.

```{figure} pics/Schnittwinkel.svg
---
width: 50%
name: schnittwinkel
---
Quelle: MushroomCloud - selbst gezeichnet, Bild-frei,
<https://de.wikipedia.org/w/index.php?curid=2905230>
```

Man kann diesen Winkel $\alpha$ auch als Differenz der beiden Neigungswinkel
berechnen. Wenn $\alpha_f$ der Neigungswinkel der Funktion $f$ ist und
$\alpha_g$ der Neigungswinkel der Funktion $g$, dann ist der gesuchte
Schnitwinkel

$$\alpha = \left|\alpha_f - \alpha_g\right|.$$

Da wir beide Neigungswinkel auch mit den Ableitungen formulieren können und ein
Additionstheorem für den Tangens gilt, erhalten wir

$$\tan(\alpha) = \left|\frac{f'(x_0) - g'(x_0)}{1 + f'(x_0)g'(x_0)}\right|.$$

Sind die beiden Tangenten senkrecht zueinander, dann ist

$$f'(x_0)\cdot g'(x_0)=-1.$$

Und sie berühren sich nur, wenn $f'(x_0) = g'(x_0)$ gilt. Weitere Deteils findem
Sie hier:

> [https://studyflix.de/mathematik/schnittwinkel-berechnen-5408](https://studyflix.de/mathematik/schnittwinkel-berechnen-5408)

```{dropdown} Video "Schnittwinkel berechnen" von Mister Mathe
<iframe width="560" height="315" src="https://www.youtube.com/embed/Dm_Uznx-lBw"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Zusammenfassung und Aucblick

Die Angabe des Neigungswinkels einer Funktion und des Schnittwinkels von zwei
Funktionen ist nur eine von vielen geometrischen Eigenschaften einer Funktion,
die mit Hilfe von Ableitungen berechnet werden kann. Weitere geometrische
Eigenschaften wie Monotonie und Krümmung lernen wir im nächsten Kapitel kennen.
