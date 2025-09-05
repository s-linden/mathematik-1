# 2.1 Funktionen - Grundlagen und Definitionen

Die Höhe einer Kugel, die eine Kugelbahn durchläuft - wie können wir diese
mathematisch beschreiben? Diese scheinbar einfache Frage führt uns direkt zu
einem der wichtigsten Konzepte der Mathematik: dem Begriff der Funktion. In
diesem Kapitel entwickeln wir anhand einer GraviTrax-Kugelbahn das mathematische
Werkzeug, um technische Zusammenhänge präzise zu erfassen.

## Lernziele

```{admonition} Lernziele Funktionen
:class: goals
* Sie wissen, wie in der Mathematik eine **Funktion** definiert wird und kennen
  typische Darstellungsformen von Funktionen.
* Sie können die **Definitionsmenge** und **Wertemenge/Zielmenge** einer
  Funktion bestimmen.
* Sie können **Funktionen zur Beschreibung technischer Systeme** (am Beispiel
  einer Kugelbahn) entwickeln und anwenden.
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
Kugelbahn der Marke GraviTrax (Quelle: eigene Darstellung; 
Lizenz: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0))
```

Um die Höhe mathematisch zu beschreiben, benötigen wir ein Koordinatensystem.
Als erste Achse wählen wir die Gerade, die durch Start- und Zielstein geht und
die sozusagen auf der Tischoberfläche liegt. Als zweite Achse wählen wir die
Höhe über der Tischoberfläche, eine Gerade die senkrecht auf der Tischoberfläche
steht. Den Ursprung des Koordinatensystems können wir frei wählen. Wir nehmen
die Position des Start-Steins auf der Tischoberfläche als Ursprung $O$. Jetzt
können wir die Position der Kugel beschreiben, indem wir ihren Abstand zum
Ursprung auf der ersten Achse messen. Die Position kürzen wir mit $x$ ab. Die
Höhe über der Tischoberfläche kürzen wir mit $h$ ab.

Mit diesem Koordinatensystem können wir jeder Position $x$ der Kugel eindeutig
eine Höhe $h$ zuordnen.

### Von der Zuordnung zur Funktion

**Beobachtung:** Für jede Position x gibt es **genau eine** zugehörige Höhe h.

Diese **eindeutige Zuordnung** ist das Wesen einer mathematischen Funktion:

- **Eingabe (Input):** Position x entlang der Bahn
- **Ausgabe (Output):** Höhe h an dieser Position
- **Eindeutigkeit:** Zu jedem x gehört genau ein h

```{admonition} Was ist ... eine Funktion?
:class: note
Eine **Funktion** ist eine eindeutige Zuordnung zwischen zwei Mengen. Jedem
Element der ersten Menge (Definitionsmenge) wird genau ein Element der zweiten
Menge (Wertemenge) zugeordnet.

**Mathematische Schreibweise:** f: X → Y oder y = f(x)
- f: Name der Funktion
- x: unabhängige Variable (Eingabewert)  
- y: abhängige Variable (Ausgabewert, hängt von x ab)
```

**Für unsere Kugelbahn:** h = f(x), wobei f die "Höhenfunktion" ist, die jeder
Position x die entsprechende Höhe h zuordnet.

### Funktionen in der Technik

Das Kugelbahn-Beispiel zeigt ein universelles Prinzip der
Ingenieurswissenschaften: **Technische Größen hängen voneinander ab.**
Funktionen beschreiben diese Abhängigkeiten mathematisch präzise:

- Geschwindigkeit hängt von der Zeit ab: v(t)
- Spannung hängt von der Dehnung ab: σ(ε)  
- Leistung hängt von der Drehzahl ab: P(n)

## Darstellungsformen von Funktionen

Für unsere Kugelbahn-Höhenfunktion gibt es verschiedene Möglichkeiten der
mathematischen Beschreibung. Jede hat ihre spezifischen Vorteile.

### 1. Funktionsgleichung (analytische Darstellung)

Für eine **gerade Schiene** mit konstanter Neigung können wir die Höhe
mathematisch exakt beschreiben:

$$h(x) = mx + h₀$$

Dabei ist:

- **m:** Neigung der Schiene (negativ, da bergab)
- **h₀:** Starthöhe (Höhe bei x = 0)
- **x:** Position entlang der Bahn
- **h(x):** Höhe an Position x

Die Funktionsgleichung gibt uns die **exakte Formel** zur Berechnung der Höhe an
jeder beliebigen Position.

### 2. Funktionsgraph (visuelle Darstellung)

Der **Funktionsgraph** ist eine **Seitenansicht** unserer Kugelbahn im
Koordinatensystem:

- **x-Achse:** Position entlang der Bahn
- **y-Achse:** Höhe über Referenzniveau
- **Gerade Linie:** Entspricht der schrägen Schiene

*[TODO Skizze/Grafik eingefügen: Koordinatensystem mit eingezeichneter Geraden]*

Der Graph macht den Funktionsverlauf sofort sichtbar und ist besonders nützlich
für das intuitive Verständnis.

### 3. Wertetabelle (diskrete Datenpunkte)

Durch **Messungen an verschiedenen Positionen** erstellen wir eine Tabelle:

| Position x [cm] | Höhe h [cm] |
|-----------------|-------------|
| 0               | 20          |
| 10              | 18          |
| 20              | 16          |
| 30              | 14          |
| 40              | 12          |

Die Wertetabelle ist ideal für **experimentelle Daten** und praktische
Messungen.

### 4. Mengenschreibweise (mathematisch exakt)

$$H = \{(x,h) | h = mx + h₀, x ∈ D\}$$

Diese Schreibweise definiert die Funktion als **Menge aller Wertepaare**
(Position, Höhe).

### Vergleich der Darstellungsformen

- Funktionsgleichung: Präzise, kompakt, für Berechnungen ideal
- Funktionsgraph: Anschaulich, für Trends und Verläufe
- Wertetabelle: Praktisch für Messdaten und Experimente  
- Mengenschreibweise: Mathematisch vollständig, für theoretische Betrachtungen

Alle vier Formen beschreiben **dieselbe Funktion**, nur in unterschiedlicher Weise.

## Definitionsmenge, Zielmenge und Wertemenge

### Grenzen der Kugelbahn

Unsere GraviTrax-Schiene ist nicht unendlich lang, und wir können auch nicht beliebig hohe oder tiefe Werte messen. Diese **physikalischen Grenzen** führen uns zu wichtigen mathematischen Konzepten, die bei jeder Funktion zu beachten sind.

### Definitionsmenge: "Wo ist überhaupt Schiene?"

Die **Definitionsmenge D** umfasst alle x-Werte, für die unsere Funktion h(x) definiert ist.

**Für unsere Kugelbahn:**

- **Schienanfang:** x = 0 cm (Startblock)
- **Schienenende:** x = 50 cm (Auffangbehälter)
- **Definitionsmenge:** D = [0, 50] (Intervall von 0 bis 50 cm)

```{admonition} Was ist ... die Definitionsmenge?
:class: note
Die **Definitionsmenge** einer Funktion ist die Menge aller zulässigen Eingabewerte (x-Werte), für die die Funktion definiert ist.

**Notation:** D oder D_f

**Bestimmung:** 
1. **Physikalische Grenzen** (z.B. Baulängen, Materialgrenzen)
2. **Mathematische Einschränkungen** (z.B. Division durch Null vermeiden)
```

### Zielmenge: "Welche Höhen können wir theoretisch messen?"

Die **Zielmenge Z** ist die Menge aller Werte, **in die** unsere Funktion
abbilden könnte. Sie wird bei der Definition der Funktion **vorab festgelegt**.

**Für unsere Kugelbahn:**

- **Zielmenge:** Z = [0, 100] cm
- **Begründung:** Unser Maßband reicht von der Tischoberfläche (0 cm) bis zur Decke (100 cm)
- **Interpretation:** "Alle Höhen, die wir theoretisch messen könnten"

### Wertemenge: "Welche Höhen nimmt die Kugel tatsächlich an?"

Die **Wertemenge W** (auch Bildmenge genannt) enthält alle h-Werte, die unsere Funktion **tatsächlich** annimmt.

**Für unsere schräge Kugelbahn:**

- **Höchster Punkt:** h(0) = 20 cm (Start)
- **Tiefster Punkt:** h(50) = 10 cm (Ende)
- **Wertemenge:** W = [10, 20] cm

**Wichtiger Zusammenhang:** Die Wertemenge ist **immer eine Teilmenge** der Zielmenge: W ⊆ Z

```{admonition} Was ist ... der Unterschied zwischen Zielmenge und Wertemenge?
:class: note
**Zielmenge:** Die Menge, **in die** eine Funktion abbildet (vorab festgelegt, "theoretisch möglich")

**Wertemenge:** Die Menge der **tatsächlich angenommenen** Funktionswerte (Teilmenge der Zielmenge)

**Beispiel:** Messgerät mit Bereich 0-1000°C (Zielmenge), aber Motor arbeitet nur bei 20-150°C (Wertemenge)
```

### Praktische Bedeutung für Ingenieure

**Definitionsmenge = Gültigkeitsbereich:**

- Außerhalb der Definitionsmenge macht unsere Formel h(x) = mx + h₀ **keinen
  physikalischen Sinn**
- Bei x = -10 cm würde die Formel eine Höhe berechnen, aber dort ist gar keine
  Schiene!
- **Extrapolation** ist gefährlich: Formeln gelten nur in ihrem
  Definitionsbereich

**Zielmenge = Messbereich:**

- Definiert den **theoretischen Rahmen** unserer Betrachtung
- Legt fest, welche Werte **prinzipiell möglich** sind
- Wichtig für die **Sensorauswahl** und Messgeräte-Spezifikation

**Wertemenge = Realisierbare Werte:**

- Zeigt uns, **welche Höhen** die Kugel auf unserer speziellen Bahn erreichen kann
- Wichtig für die **Konstruktion:** Wo müssen Auffangbehälter platziert werden?
- **Optimierung:** Können wir den Höhenbereich durch Umkonstruktion erweitern?

### Erweiterungen des Konzepts

**Was passiert bei komplexeren Bahnen?**

**Unterbrochene Schienen:**

- Wenn zwischen den Schienenstücken eine Lücke ist
- **Definitionsmenge:** D = [0,20] ∪ [30,50] (Vereinigung von Intervallen)
- **Interpretation:** "Die Funktion ist nur dort definiert, wo auch Schiene ist"

**Höhenbegrenzungen:**

- **Zielmenge physikalisch begrenzt:** Nicht höher als die Decke, nicht tiefer
  als der Boden
- **Wertemenge durch Konstruktion begrenzt:** Abhängig vom gewählten Bahnverlauf

**Wichtige Erkenntnis:** Nicht alles, was **mathematisch möglich** ist (negative
Höhen, unendliche Positionen), ist auch **physikalisch sinnvoll**. Die
Ingenieurskunst liegt darin, die mathematischen Modelle so zu wählen, dass sie
die **physikalische Realität** korrekt abbilden.

## Zusammenfassung und Ausblick

### Kernkonzepte

**Funktion:** Eine eindeutige Zuordnung zwischen Position und Höhe (allgemein:
zwischen zwei Mengen)

**Vier Darstellungsformen:**

- Funktionsgleichung (h(x) = mx + h₀)
- Funktionsgraph (Seitenansicht der Bahn)
- Wertetabelle (Messpunkte)
- Mengenschreibweise (mathematisch exakt)

**Definitions- und Wertemenge:** Gültigkeitsbereich und realisierbare Werte
unserer Beschreibung

### Ausblick auf die folgenden Kapitel

Unsere einfache gerade Schiene ist nur der Anfang. In den kommenden Kapiteln erweitern wir unser Kugelbahn-System:

**Kapitel 2.2 - Eigenschaften von Funktionen:** Was passiert, wenn wir ein **ebenes Plateau** in die Bahn einbauen? (konstante Bereiche, Monotonie)

**Kapitel 2.3 - Polynome:** Wie beschreiben wir **Kurven und Bögen**? (quadratische und höhere Funktionen)

**Kapitel 2.4 - Exponential- und Logarithmusfunktionen:** Spezielle Bahnformen mit **charakteristischen Verläufen**

**Kapitel 2.5 - Trigonometrische Funktionen:** **Schwingungen und periodische Bewegungen**

Mit jeder Erweiterung werden unsere mathematischen Werkzeuge mächtiger - aber das physikalische Grundprinzip bleibt gleich: **Position bestimmt Höhe, mathematisch ausgedrückt durch Funktionen.**

## Videos zu Funktionen

```{admonition} Video
:class: seealso
<iframe width="560" height="315" src="https://www.youtube.com/embed/9HiHcxXhYn4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```
