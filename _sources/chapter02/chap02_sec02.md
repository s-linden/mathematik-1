# 2.2 Eigenschaften von Funktionen

Nachdem wir im vorherigen Kapitel die Grundlagen von Funktionen anhand einer
einfachen geraden Kugelbahn kennengelernt haben, erweitern wir nun das
Kugelbahn-System. Wir bauen verschiedene Bahnformen und entdecken dabei wichtige
Eigenschaften von Funktionen, die uns helfen, das Verhalten mathematischer
Zusammenhänge zu verstehen und zu klassifizieren.

## Lernziele

```{admonition} Lernziele Eigenschaften von Funktionen
:class: goals
Sie kennen die wichtigsten Eigenschaften von mathematischen Funktionen wie
beispielsweise
- **Monotonie**,
- **Symmetrie**,
- **Periodizität** und
- **Beschränktheit**.
```

## Monotonie - Steigt oder fällt die Bahn?

Betrachten wir zunächst unsere ursprüngliche gerade Kugelbahn genauer. Die Kugel
rollt von links nach rechts und ihre Höhe wird dabei kontinuierlich niedriger.
Diese Eigenschaft nennen wir **Monotonie**.

```{raw} html
<div class="kugelbahn-wrapper">
<iframe src="../chap02/marble_track_simple.html"
width="100%" height="500"
frameborder="0"scrolling="no"
title="Interaktive Kugelbahn">
</iframe>
</div>
```

Je größer der Abstand zum Start ist, desto niedriger ist die Höhe der Kugel und
das gilt sogar streng. Wir formulieren diese Beobachtung mathematisch: Wenn
$x_1$ kleiner als $x_2$ ist, dann ist die Höhe $h(x_1)$ echt größer als die Höhe
$h(x_2)$. Verallgemeinert auf alle Funktionen gilt:

Eine Funktion $f$ heißt **streng monoton fallend**, wenn ihre Funktionswerte mit
wachsenden x-Werten streng abnehmen:

$$x_1 < x_2 \quad \Rightarrow \quad f(x_1) \textcolor{red}{>} f(x_2).$$

Wir können uns aber auch vorstellen, ein Plateau einzubauen, wie in der
folgenden Kugelbahn. Damit leichter erkennbar ist, wo das Plateau beginnt, wird
die Kugel bei einem Plateau weiß gefärbt. Je steiler die Kugelbahn ist, desto
dunkler wird die Kugel eingefärbt. Das hat nichts mit der physikalischen
Geschwindigkeit der Kugel zu tun, sondern zeigt die Eigenschaften der Schienen.

```{raw} html
<div class="kugelbahn-wrapper">
<iframe src="../chap02/marble_track_simple_with_plateau.html"
width="100%" height="500"
frameborder="0"scrolling="no"
title="Interaktive Kugelbahn">
</iframe>
</div>
```

Wenn wir die obige Kugelbahn als mathematische Funktion darstellen möchten,
müssen wir drei Abschnitte unterscheiden:

- Abschnitt 1: von 0 cm bis 8 cm gilt $\;h_1(x)=-0.25x+6$,
- Abschnitt 2: von 8 cm bis 12 cm gilt $\;h_2(x)=4$,
- Abschnitt 3: von 12 cm bis 24 cm gilt $\;h_3(x)=-\frac{1}{3}x+8$.

Die Definitionsmenge $D=[0;24]$ wird in drei Teilintervalle

$$I_1 = [0;8], \quad I_2 = (8; 12], \quad I_3 = (12; 24]$$

unterteilt und für jeden Abschnitt gilt eine andere Funktionsgleichung. Die
Intervalle sind dabei so gewählt, dass sie nicht überlappen. Die Position $x=8$
beispielsweise gehört eindeutig zum ersten Intervall und nicht zum zweiten. Eine
solche Funktion nennen wir **abschnittsweise definierte Funktion**. Insgesamt
schreiben wir die Höhenfunktion $h$ folgendermaßen:

$$h(x) = \begin{cases}
-0.25x+6, \quad & x\in[0;8],\\
4, \quad & x\in(8; 12],\\
-\frac{1}{3}x+8, \quad & x\in(12; 24].
\end{cases}$$

Mehr zu abschnittsweise definierten Funktionen finden Sie im folgenden Video:

```{dropdown} Video "abschnittsweise definierte Funktionen" von Mathematische Methoden
<iframe width="560" height="315"
src="https://www.youtube.com/embed/XGpoI5X5z5s?si=Afjv_VDPQwLUI_ln"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay;
clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
```

Die Höhenfunktion zeigt folgendes Monotonieverhalten:

- Abschnitt 1 (für das Intervall $I_1=[0; 8]$): streng monoton fallend, d.h.
  $h(x_1)>h(x_2)$,
- Abschnitt 2 (für das Intervall $I_2=(8; 12]$): konstant, d.h. $h(x_1)=h(x_2)$,
- Abschnitt 3 (für das Intervall $I_3=(12; 24]$): streng monoton fallend, d.h.
  $h(x_1)>h(x_2)$.

Wenn wir den Begriff »streng« lockern, dann gilt für die gesamte Funktion $h$
auf der kompletten Definitionsmenge $D=[0; 24]$ entweder $h(x_1) > h(x_2)$ oder
$h(x_1)=h(x_2)$, wobei $x_1<x_2$ vorausgesetzt wird. Die Funktion ist
abschnittsweise streng monoton fallend und insgesamt (auf $[0,24]$) **monoton
fallend**.

Für die Kugelbahn könnte es ein Förderband geben, das die Kugel zum Start-Block
transportiert. Das wäre eine wachsende Funktion, da die Funktionswerte größer
werden, je weiter wir uns nach rechts auf der $x$-Achse bewegen. Wir fassen
zusammen:

```{admonition} Was ist ... Monotonie?
:class: note
Sei $D\subset\mathbb{R}$ und $f$ eine reellwertige Funktion
$f:D\rightarrow\mathbb{R}$. Die Funktion $f$ heißt auf einem Intervall $I\subset
D$
- **monoton wachsend**, falls für alle $x_1, x_2 \in I$ gilt:<br>
Wenn $x_1 < x_2$, dann $f(x_1) \leq f(x_2)$.
- **streng monoton wachsend**, falls für alle $x_1, x_2 \in I$ gilt:<br>
Wenn $x_1 < x_2$, dann $f(x_1) < f(x_2)$.
- **monoton fallend**, falls für alle $x_1, x_2 \in I$ gilt:<br>
Wenn $x_1 < x_2$, dann $f(x_1) \geq f(x_2)$.
- **streng monoton fallend**, falls für alle $x_1, x_2 \in I$ gilt:<br>
Wenn $x_1 < x_2$, dann $f(x_1) > f(x_2)$.
```

Hinweis: In diesem Vorlesungsskript verwenden wir konsequent die Bezeichnungen
wachsend/fallend. In anderen Quellen wird oft auch steigend/abnehmend gesagt.

Mehr Details zur Monotonie finden Sie in den folgenden Videos.

```{dropdown} Video "Was ist Monotonie?" von studiVEMINT
<iframe width="560" height="315"
src="https://www.youtube.com/embed/QfDPvxHAz3k?si=krDjMMRx1o328vNU"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay;
clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
```

```{dropdown} Video "Monotonie" von HM Kompakt
<iframe width="560" height="315"
src="https://www.youtube.com/embed/FFfcZK_nCws?si=VPXEZSaDTb7Wdb3x"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay;
clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
```

```{admonition} Weiteres Lernmaterial
:class: seealso
- [Monoton steigend und fallend von
  Studyflix](https://studyflix.de/mathematik/was-ist-monotonie-7417)
- [Monotonie von Serlo](https://de.serlo.org/mathe/1911/monotonie)
```

## Beschränktheit - Wie hoch und wie tief geht es?

Jede reale Kugelbahn hat physikalische Grenzen. Diese führen uns zum Konzept der
**Beschränktheit**.

```{admonition} Was ist ... Beschränktheit?
:class: note
Eine Funktion $f$ heißt **nach oben beschränkt**, wenn es eine Zahl $M$ gibt,
sodass $f(x) \leq M$ für alle $x$ aus der Definitionsmenge.

Eine Funktion $f$ heißt **nach unten beschränkt**, wenn es eine Zahl $m$ gibt,
sodass $f(x) \geq m$ für alle $x$ aus der Definitionsmenge.

Eine **beschränkte** Funktion ist sowohl nach oben als auch nach unten
beschränkt.
```

## Symmetrie - Spiegelbahnen

Erweitern wir unser Kugelbahn-System um symmetrische Konstruktionen. Symmetrie
macht Bahnen oft besonders elegant und vorhersagbar.

```{admonition} Was ist ... Symmetrie?
:class: note
**Achsensymmetrie (gerade Funktion):** Eine Funktion ist achsensymmetrisch zur
y-Achse, wenn $f(-x) = f(x)$ gilt. Der Graph ist spiegelbar an der y-Achse.

**Punktsymmetrie (ungerade Funktion):** Eine Funktion ist punktsymmetrisch zum
Ursprung, wenn $f(-x) = -f(x)$ gilt. Der Graph ist spiegelbar am Ursprung.
```

## Periodizität - Wiederholende Muster

Stellen Sie sich eine Kugelbahn vor, die über eine Reihe identischer Hügel
führt. Diese wiederholende Struktur führt uns zur **Periodizität**.

```{admonition} Was ist ... Periodizität?
:class: note
Eine Funktion $f$ heißt **periodisch** mit der Periode $T > 0$, wenn $f(x + T) =
f(x)$ für alle $x$ aus der Definitionsmenge gilt.

Die kleinste positive Zahl $T$ mit dieser Eigenschaft heißt **Grundperiode**.
```

## Kombination von Eigenschaften

In der Realität können Kugelbahnen mehrere Eigenschaften gleichzeitig aufweisen:

**Berg-und-Tal-Bahn:** Eine Bahn $h(x) = -0.1x^2 + 3\cos(x) + 5$ könnte:

- Beschränkt sein (zwischen Boden und Tunneldecke)
- Periodische Elemente enthalten (die Cosinus-Komponente)
- Einen übergeordneten Trend haben (die Parabel-Komponente)

**Treppenbahn:** Eine Bahn mit stufenweisen Absenkungen zeigt abschnittweise
Monotonie und ist beschränkt.

## Praktische Bedeutung für das Bahndesign

Diese Eigenschaften helfen uns beim systematischen Design von Kugelbahnen:

1. **Monotonie:** Bestimmt die grundsätzliche Energieentwicklung (Beschleunigung/Abbremsung)
2. **Beschränktheit:** Legt die Konstruktionsgrenzen fest
3. **Symmetrie:** Vereinfacht Planung und erhöht Stabilität
4. **Periodizität:** Ermöglicht modularen Aufbau und Vorhersagbarkeit

## Zusammenfassung und Ausblick

Die Eigenschaften von Funktionen - Monotonie, Beschränktheit, Symmetrie und
Periodizität - helfen uns, das Verhalten mathematischer Zusammenhänge zu
verstehen und zu klassifizieren. Anhand unserer Kugelbahn-Beispiele wird
deutlich, wie diese abstrakten Konzepte ganz konkrete praktische Bedeutung
haben.

In den folgenden Kapiteln werden wir diese Eigenschaften nutzen, um komplexere
Funktionstypen zu verstehen und gezielt Kugelbahnen für spezifische
Anforderungen zu entwerfen. Die mathematische Analyse von Funktionseigenschaften
wird uns dabei helfen, optimale Lösungen zu finden.

```{admonition} Video
:class: seealso
<iframe width="560" height="315" src="https://www.youtube.com/embed/0tsv-OfsZNY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

```{admonition} Video
:class: seealso
<iframe width="560" height="315" src="https://www.youtube.com/embed/DUduGskMh3Q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

```{admonition} Video
:class: seealso
<iframe width="560" height="315" src="https://www.youtube.com/embed/HdPT8R3qOhM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```
