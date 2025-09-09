# 2.1 Funktionen - Grundlagen und Definitionen

Die Höhe einer Kugel, die eine Kugelbahn durchläuft - wie können wir diese
mathematisch beschreiben? Diese scheinbar einfache Frage führt uns direkt zu
einem der wichtigsten Konzepte der Mathematik: dem Begriff der Funktion. In
diesem Kapitel entwickeln wir anhand einer Kugelbahn das mathematische Werkzeug,
um technische Zusammenhänge präzise zu erfassen.

## Lernziele

```{admonition} Lernziele Funktionen
:class: goals
* Sie wissen, wie in der Mathematik eine **Funktion** definiert wird.
* Sie können die **Definitionsmenge** und **Wertemenge** einer Funktion
  bestimmen.
* Sie kennen die verschiedenen Darstellungsformen einer Funktion wie
  **Wertetabelle**, **Funktionsgleichung** und **Funktionsgraph**.
```

## Was ist eine Funktion?

Stellen Sie sich vor, wir haben eine einfache Kugelbahn aufgebaut. Es gibt einen
Start-Stein, eine gerade, schräge Schiene und einen Ziel-Stein, der als
Auffangbehälter dient. Unsere zentrale Frage lautet: *Wie hoch befindet sich die
Kugel an jeder beliebigen Position entlang der Bahn?*

```{figure} pics/kugelbahn_gerade_w800px.png
---
width: 75%
name: kugelbahn_gerade_w800px
---
Kugelbahn der Marke
[GraviTrax](https://www.ravensburger.de/de-DE/entdecken/gravitrax)
(Quelle: eigene Darstellung; Lizenz: [CC BY-SA
4.0](https://creativecommons.org/licenses/by-sa/4.0))
```

Um die Höhe mathematisch zu beschreiben, benötigen wir ein Koordinatensystem.
Als erste Achse wählen wir die Gerade, die durch Start- und Zielstein geht. Diese
liegt auf der Tischoberfläche. Als zweite Achse wählen wir die Höhe über der
Tischoberfläche. Diese steht senkrecht auf der Tischoberfläche. Den Ursprung des
Koordinatensystems können wir frei wählen. Wir nehmen die Position des Start-Steins
auf der Tischoberfläche als Ursprung $O$.

Jetzt können wir die Position der Kugel eindeutig beschreiben. Wir messen ihren
Abstand zum Ursprung auf der ersten Achse. Diese Position kürzen wir mit $x$ ab.
Die Höhe über der Tischoberfläche kürzen wir mit $h$ ab.

Mit diesem Koordinatensystem können wir jeder Position $x$ der Kugel eindeutig
eine Höhe $h$ zuordnen. Eindeutig bedeutet: Es gibt nicht zwei verschiedene
Höhen zu einer x-Position. Wir können nun messen und die x-Positionen mit ihrer
jeweiligen Höhe in einer Tabelle notieren:

| Position x \[cm\] | Höhe h \[cm\] |
| ------------------| --------------|
| 0.0 | 6.0 |
| 4.8 | 4.8 |
| 9.6 | 3.6 |
| 14.4 | 2.4 |
| 19.2 | 1.2 |
| 24.0 | 0.0 |

Wir haben nicht an jeder Position der Kugelbahn die Höhe gemessen, aber wir
könnten es tun. Auch an Zwischenstellen wie beispielsweise $x = 0.567~\text{cm}$
oder $x = 17.9~\text{cm}$ lassen sich die zugehörigen Höhen messen.

Diese eindeutige Zuordnung zwischen Position und Höhe ist das Wesen einer
mathematischen Funktion. In der Mathematik bezeichnet man eine solche eindeutige
Zuordnung zwischen zwei Mengen als **Funktion**. Formal definieren wir eine
mathematische Funktion folgendermaßen:

```{admonition} Was ist ... eine Funktion?
:class: note
Eine Funktion ist eine eindeutige Zuordnung zwischen zwei Mengen. Jedem
Element der ersten Menge (Definitionsmenge) wird genau ein Element der zweiten
Menge (Wertemenge) zugeordnet.
```

Kürzen wir die Definitionsmenge mit $D$ ab, die Wertemenge mit $W$ und die
Funktion mit $f$, so lässt sich diese Definition auch kompakt schreiben als:

$$f: D \to W, \quad x \mapsto f(x).$$

Das Element aus der Wertemenge, das dem Element $x$ aus der Definitionsmenge
zugeordnet wird, heißt **Funktionswert** und wird mit $f(x)$ abgekürzt.

## Darstellungsformen von Funktionen

Für unsere Kugelbahn-Höhenfunktion gibt es verschiedene Möglichkeiten der
mathematischen Beschreibung. Jede hat ihre spezifischen Vorteile.

Eine der einfachsten Darstellungen ist die **Wertetabelle**. Sie ist besonders
vorteilhaft, wenn die Funktion durch Messungen bestimmt wird. Die Tabelle mit
den Messwerten unserer Kugelbahn haben wir bereits oben erstellt. Die Wertetabelle
ist ideal für experimentelle Daten und praktische Messungen.

Im Fall der Kugelbahn können wir die Höhe der Kugel auch mathematisch exakt
beschreiben als:

$$h(x) = -\frac{1}{4}x + 6$$

$h(x)$ gibt die Höhe an der Position $x$ wieder. Wir haben also eine *exakte
Formel* zur Berechnung der Höhe an jeder beliebigen Position in Form einer
Gleichung. Daher wird diese Darstellungsform **Funktionsgleichung** genannt.
Die Funktionsgleichung ist präzise, kompakt und ideal für Berechnungen.

Eine weitere Darstellungsform ist der **Funktionsgraph** oder **Plot** der
Funktion. Der Funktionsgraph entspricht der Seitenansicht unserer Kugelbahn. Zu
jedem $x$-Wert wird der zugehörige Funktionswert $h(x)$ ermittelt. Üblicherweise
wird der Funktionswert mit $y$ abgekürzt. Die Punkte $(x,y)$ werden dann in ein
xy-Koordinatensystem eingezeichnet.

```{figure} pics/function_marble_track.svg
---
width: 75%
name: function_marble_track
---
Graph bzw. Plot der Höhenfunktion der Kugel in der Kugelbahn
(Quelle: eigene Darstellung; Lizenz: [CC BY-SA
4.0](https://creativecommons.org/licenses/by-sa/4.0))
```

Der Graph macht den Funktionsverlauf sofort sichtbar und ist besonders nützlich
für das intuitive Verständnis. Alle drei Darstellungsformen beschreiben dieselbe
Funktion, nur in unterschiedlicher Weise.

## Definitionsmenge und Wertemenge

Unsere Kugelbahn ist nicht unendlich lang, und auch die möglichen Höhenwerte
sind begrenzt. Diese physikalischen Grenzen führen uns zu wichtigen
mathematischen Konzepten.

Nicht alle x-Positionen sind sinnvoll. Positionen links des Start-Steins (also
$x < 0~\text{cm}$) und rechts des Ziel-Steins ($x > 24~\text{cm}$) sind nicht
relevant. Wir betrachten daher nur das Intervall:

$$D = [0; 24] \quad \text{gemessen in cm}.$$

Die tatsächlich relevanten x-Positionen bezeichnen wir als **Definitionsmenge**.

Für die Höhenwerte bestimmen wir die **Wertemenge**. Die Kugel startet bei 6 cm
und endet bei 0 cm. Daher ist die Wertemenge:

$$W = [0; 6] \quad \text{gemessen in cm}.$$

```{admonition} Was ist ... die Definitionsmenge und Wertemenge?
:class: note
**Definitionsmenge D:** Die Menge aller zulässigen Eingabewerte (x-Werte), für
die die Funktion definiert ist.

**Wertemenge W:** Die Menge aller Ausgabewerte (y-Werte), die die Funktion
tatsächlich annimmt.
```

Die **Definitionsmenge** ist der Gültigkeitsbereich für die Funktion. Außerhalb der
Definitionsmenge ergibt unsere Formel $h(x) = -\frac{1}{4}x + 6$ keinen
physikalischen Sinn. Bei $x = -10~\text{cm}$ würde die Formel eine Höhe
berechnen, aber dort ist gar keine Schiene! Extrapolation, also das Verlassen
des Gültigkeitsbereichs, ist gefährlich: Formeln gelten nur in ihrem
Definitionsbereich.

Die **Wertemenge** zeigt uns die realisierbaren Werte. Sie gibt an, welche
Höhen die Kugel auf unserer Bahn erreichen kann. Dies ist wichtig für die
Konstruktion: Wo müssen Auffangbehälter platziert werden? Können wir den
Höhenbereich durch Umkonstruktion erweitern?

```{dropdown} Video "Funktion und Graph" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/9HiHcxXhYn4"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

```{dropdown} Video "Funktionen: Notation" von HM Kompakt
<iframe width="560" height="315" src="https://www.youtube.com/embed/QZKQDLh1evA?si=OD-6-bDDpErXUvh8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
```

```{dropdown} Video "Was ist eine Funktion?" von studyVEMINT
<iframe width="560" height="315" src="https://www.youtube.com/embed/u4lbFXPlyAI?si=ufbDe-Zyl-rwYQHi" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
```

## Zusammenfassung und Ausblick

In diesem Kapitel haben wir anhand einer einfachen Kugelbahn die Grundlagen von
Funktionen entwickelt: Eine Funktion ist eine eindeutige Zuordnung zwischen
Position und Höhe, die wir durch Wertetabelle, Funktionsgleichung oder
Funktionsgraph darstellen können. Definitionsmenge und Wertemenge bestimmen den
Gültigkeitsbereich und die realisierbaren Werte unserer mathematischen
Beschreibung. Unsere einfache gerade Schiene ist nur der Anfang. In den
kommenden Kapiteln erweitern wir unser Kugelbahn-System, um weitere
mathematische Konzepte zu entdecken.
