# 2.2 Eigenschaften von Funktionen

Nachdem wir im vorherigen Kapitel die Grundlagen von Funktionen anhand unserer
einfachen geraden Kugelbahn kennengelernt haben, erweitern wir nun unser
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
das gilt sogar strikt. Wir formulieren diese Beobachtung mathematisch: Wenn
$x_1$ kleiner als $x_2$ ist, dann ist die Höhe $h(x_1)$ echt größer als die Höhe
$h(x_2)$. Verallgemeinert auf alle Funktionen gilt:

Eine Funktion $f$ heißt **streng monoton fallend**, wenn ihre Funktionswerte mit
wachsenden x-Wert strikt abnehmen:

$$x_1 < x_2 \quad \Rightarrow \quad f(x_1) \textcolor{red}{>} f(x_2).$$

Wir können uns aber auch vorstellen, ein Plateau einzubauen, wie in der
folgenden Kugelbahn. Damit leichter erkennbar ist, wo das Plateau beginnt, wird
die Kugel bei einem Plateau weiß gefärbt. Je steiler die Kugelbahn nach unten
geht, desto dunkelblauer wird die Kugel eingefärbt. Das hat nichts mit der
physikalischen Geschwindigkeit der Kugel zu tun, sondern zeigt die Eigenschaften
der Schienen.

```{raw} html
<div class="kugelbahn-wrapper">
<iframe src="../chap02/marble_track_simple_with_plateau.html"
width="100%" height="500"
frameborder="0"scrolling="no"
title="Interaktive Kugelbahn">
</iframe>
</div>
```

```{admonition} Was ist ... Monotonie?
:class: note
Eine Funktion heißt **monoton steigend** (oder monoton wachsend), wenn ihre
Funktionswerte mit wachsendem x-Wert nicht abnehmen: $x_1 < x_2 \Rightarrow
f(x_1) \leq f(x_2)$.

Eine Funktion heißt **monoton fallend** (oder monoton abnehmend), wenn ihre
Funktionswerte mit wachsendem x-Wert nicht zunehmen: $x_1 < x_2 \Rightarrow
f(x_1) \geq f(x_2)$.

Bei **streng monoton steigend/fallend** gilt das entsprechende
Ungleichheitszeichen ohne Gleichheit.
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
