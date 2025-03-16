# 9.1 Grundwissen Zahlenfolgen

Folgen von Zahlen haben in der Signalverarbeitung eine wichtige Bedeutung. In
der Mathematik sind Zahlenfolgen der Baustein, aus dem die Differential- und
Integralrechnung gebaut werden.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie wissen, was eine **Zahlenfolge** ist und was ein **Folgenglied** ist.
* Sie können Zahlenfolgen definieren

    * durch die konkrete **Aufzählung** von Folgengliedern, z.B. $(a_k) = \{1,4,9,16,25,36, \ldots\}$,
    * durch eine **explizite Regel**, d.h. man gibt eine Formel an, mit der jedes Folgenglied unabhängig von den anderen berechnet werden kann, z.B. $a_k = k^2, \, k=1,2,\ldots$ oder
    * durch eine **rekursive Regel**, d.h. man gibt ein paar Anfangsglieder an und danach eine Formel, wie sich die übrigen daraus berechnen, z.B. $a_0 = 0, a_1 = 1 \text{ und } a_{k} = a_{k-2} + a_{k-1}$ für alle $k\geq 2$.

* Sie kennen den Fachbegriff **alternierend**, um Folgen zu beschreiben, bei denen sich das Vorzeichen abwechselt.  
* Sie können von einer gegebenen Folge bestimmen, ob die Zahlenfolge monoton fallend, streng monoton fallend, monoton wachsend oder streng monoton wachsend ist. Zur Erinnerung, man nennt eine Zahlenfolge $(a_k)$

    * **monoton fallend**, falls $a_k \geq a_{k+1}$,
    * **streng monoton fallend**, falls $a_k > a_{k+1}$,
    * **monoton wachsend**, falls $a_k \leq a_{k+1}$,
    * **streng monoton wachsend**, falls $a_k < a_{k+1}$.

* Sie können den Fachbegriff **beschränkte Zahlenfolge** erklären. 

```

## Was ist eine Folge?

Wir haben schon Mengen und Tupel kennengelernt, jetzt geht es weiter mit Folgen.
Bei einem Tupel kommt es auf die Reihenfolge an, in der die Elemente angeordnet
sind. Beispielsweise werden Farben durch RGB-Werte beschrieben, also den Anteil
an Rot, Grün und Blau. Ein pures Rot wird gekennzeichnet als (1.0, 0, 0),
während der RGB-Wert (0,0,1.0) ein reines Blau darstellt. Obwohl in dem Tupel
jeweils die Werte 0 und 1 vorkommen, werden durch ihre Anordnung zwei sehr
unterschiedliche Farben dargestellt. Tupel haben jedoch nur endlich viele
Elemente. Daher benutzen wir auch die Bezeichnung n-Tupel, wobei n die Anzahl
der Elemente ist. Folgen sind Tupel mit unendlich vielen Elementen. Die können
wir nicht mehr alle auflisten, wir brauchen eine Beschreibung für die unendlich
vielen Elemente.

Die Aufzählung

$$2, 4, 6, 8, 10, 12, 14, \ldots$$

ist ein klassisches Beispiel für eine Folge. Wir erkennen, dass es sich um die
*geraden* natürlichen Zahlen handelt.

An der dritten Stelle der Folge steht das Element 6. Bei Folgen benutzt man
allerdings selten den Fachbegriff »Element«, sondern spricht von dritten
**Folgenglied**. Da es bei Folgen auf die Reihenfolge der Elemente ankommt,
werden die Positionen durchnummeriert, also beispielsweise

\begin{align*}
a_1 &= 2 \\
a_2 &= 4 \\
a_3 &= 6 \\
a_4 &= 8 \\
a_5 &= 10 \\
a_6 &= 12 \\
& \; \vdots \\
\end{align*}

Allgemein schreibt man für eine Folge $(a_i)_{i\in\mathbb{N}}$ oder auch einfach
$(a_i)$ um anzudeuten, dass es sich hier um eine Aufzählung unendlich vieler
Folgenglieder $a_i$ handelt. Die Positionsangabe $i$ heißt **Index** der Folge.

```{admonition} Was ist ... eine Folge?
:class: note

Eine Folge ist eine Aufzählung von unendlich vielen Zahlen $a_i$ und wird mit
runden Klammern geschrieben: 

$$(a_i)_{i\in\mathbb{N}}.$$ 

Eine einzelne Zahl der Folge wird Folgenglied genannt. Die Position eines
Folgenglieds innerhalb der Folge wird Index genannt.
```

## Wie werden Folgen beschrieben?

Da eine Folge unendlich viele Folgenglieder hat, können wir nicht alle
hinschreiben. Eine Variante, eine Folge anzugeben, ist die **konkrete
Aufzählung** der ersten Folgenglieder in der Hoffnung, dass dann jeder versteht,
nach welchem Muster die Folge gebildet wurde und wie es weiter geht. Das haben
wir oben getan.

Eine zweite Variante ist die Angabe einer **expliziten Regel**, wie die
Folgenglieder gebildet werden sollen. Die explizite Regel können wir uns wie
eine Funktion vorstellen, bei der die Definitionsmenge die natürlichen Zahlen
sind. In dem obigen Beispiel lautet eine explizite Regel

$$a_k = 2 \cdot k, \quad k\in\mathbb{N}.$$

Eine dritte Variante, folgen zu beschreiben, ist die Beschreibung als
**rekursive Regel**. Wir können bei dem obigen Beispiel festhalten, dass die
Folge bei $a_1 = 2$ startet. Ist ein Folgenglied $a_{k}$ berechnet, wird das
nächste Folgenglied $a_{k+1}$ berechnet, indem die Zahl 2 addiert wird. Also
können wir die Folge auch folgendermaßen beschreiben:

$$a_1 = 2, \quad a_{k+1} = a_{k} + 2, \quad k = 2, 3, 4, \ldots .$$

Manche Folgen können explizit beschrieben werden, manche rekursiv und manchmal
ist es möglich, für eine Folge sowohl eine explizite als auch eine rekursive
Bildungsvorschrift zu finden.

```{dropdown} Video "Zahlenfolgen" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/GfhsHuTwIjA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

```{dropdown} Video "Explizite Formel finden" von Mathematrick
<iframe width="560" height="315" src="https://www.youtube.com/embed/c2hHWi-8wKo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

```{dropdown} Video "Rekursive Formel" von Mathematrick
<iframe width="560" height="315" src="https://www.youtube.com/embed/t2G7yviicAQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

## Alternierende Folgen

Die obige Folge der geraden natürlichen Zahlen kann auch so abgeändert werden,
dass das Vorzeichen immer abwechselt:

$$2, -4, 6, -8, 10, -12, \ldots.$$

Eine solche Folge heißt **alternierend**.

```{dropdown} Video "alternierende Folge" vom Mathematrick
<iframe width="560" height="315" src="https://www.youtube.com/embed/mQLADVxxRU8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

## Monotonie von Folgen

Da Folgen nur Funktionen mit Definitionsgebiet $\mathbf{N}$, verwundert es
nicht, dass es die Eigenschaft der Monotonie auch für Folgen gibt. Eine Folge
muss nicht monoton sein. Wenn sie monoton ist, gibt es vier Fälle. Eine Folge
$(a_k)$ heißt

* **monoton fallend**, falls $a_k \geq a_{k+1}$,
* **streng monoton fallend**, falls $a_k > a_{k+1}$,
* **monoton wachsend**, falls $a_k \leq a_{k+1}$,
* **streng monoton wachsend**, falls $a_k < a_{k+1}$.

```{dropdown} Video "Monotonie von Folgen" von Mathematrick
<iframe width="560" height="315" src="https://www.youtube.com/embed/YoNAdPOMMGQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

## Beschränktheit von Folgen

Als nächstes betrachten wir als Beispiel die Folge

$$1,\frac{1}{2},\frac{1}{4},\frac{1}{8},\frac{1}{16},\frac{1}{32},\ldots.$$

Das explizite Bildungsgesetz für diese Folge lautet

$$a_{k} = \left(\frac{1}{2}\right)^{k-1}, \quad k \in\mathbb{N}.$$

Die Folgenglieder werden immer kleiner und sind irgendwann so klein, dass sie
kaum von Null zu unterscheiden sind. Aber dennoch bleiben sie positiv, egal wie
groß auch $k$ wird. Man sagt daher, dass die Zahl 0 eine untere Schranke für
diese Folge ist bzw. dass die Folge nach unten beschränkt ist. Es gilt

$$0 \leq a_k, \quad \forall k\in\mathbb{N},$$

tatsächlich gilt sogar $0 < a_k$. Aber auch die Zahl -17.3 ist eine untere
Schranke für diese Folge, denn es gilt auch

$$-17.3 \leq a_k, \quad \forall k\in\mathbb{N}.$$

Auch hier gilt sogar das strikte Ungleichheitszeichen $<$.

Alle negativen Zahlen sind untere Schranken für diese Folge. Von den unteren
Schranken ist $S_{\text{unten}}=0$ die größte untere Schranke und wird
**Infimum** genannt.

Auch nach oben finden wir eine Schranke, die Folge $(a_k)$ ist nach oben
beschränkt. Beispielsweise sind alle Folgenglieder kleiner als 4, also

$$4 \geq a_k, \quad \forall k\in\mathbb{N}.$$

Auch hier gilt eigentlich das strikte Ungleichheitszeichen $>$. Eine Zahl
$S\in\mathbb{R}$ mit

$$s \geq a_k, \quad \forall k\in\mathbb{R}$$

wird obere Schranke genannt. Auch hier gibt es eine kleinste obere Schranke,
nämlich die Zahl 1, denn es gilt

$$1 \geq a_k, \quad \forall k\in\mathbb{R}.$$

Die kleinste obere Schranke wird **Supremum** genannt. Allrdings gibt es hier
bei diesem konkreten Beispiel einen Unterschied zwischen dem Infimum 0 und dem
Supremum 1. Es gibt kein Folgenglied $a_k$, das jemals den Wert 0 annimmt. Das
Infimum kommt niemals in der Folge vor. Aber das Supremum 1 entspricht gleich
dem ersten Folgenglied $a_1 = 1$. Weil das Supremum tatsächlich auch ein
Folgenglied ist, bezeichnet man das Supremum als **Maximum**. Gäbe es ein
Folgenglied mit dem Infimum, hätte man das Infimum auch **Minimum** genannt.

Halten wir noch fest, was beschränkt bedeutet: eine Folge die sowohl nach oben
als auch nach unten beschränkt ist, heißt einfach nur **beschränkt**.

> Weiteres Lernmaterial: <https://studyflix.de/mathematik/zahlenfolgen-5710>

Das folgende Video brauchen Sie nur bis ca. 7:58 min schauen, Konvergenz kommt
erst im nächten Kapitel.

```{dropdown} Video "Beschränktheit, Monotonie, Konvergenz von Zahlenfolgen" von MathePeter
<iframe width="560" height="315" src="https://www.youtube.com/embed/vlvdGYZyHo8?si=O1-MnemNzXvMOwH8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; 
clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
```

## Zusammenfassung und Ausblick

In diesem Kapitel haben Sie gelernt, was eine Folge ist und was die
mathematischen Fachbegriffe Folgenglied und Index bedeuten. Es gibt verschiedene
Varianten, Folgen zu beschreiben, beispielsweise die Aufzählung, die explizite
Regel oder die rekursive Formel. Neben den alternierenden Folgen haben Sie auch
gelernt, was Monotonie und Beschränktheit von Folgen bedeutet. Beides werden wir
im folgenden Kapitel brauchen, wenn es um Grenzwerte bzw. Konvergenz von Folgen
geht.
