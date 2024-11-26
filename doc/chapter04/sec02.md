# 4.2 Skalarprodukt

In diesem Kapitel werden wir uns mit dem Skalarprodukt beschäftigen. Zunächst
führen wir es für reelle Standardvektorräume $\mathbb{R}^n$ ein.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie wissen, was das **Skalarprodukt** im reellen Standardvektorraum $\mathbb{R}^n$ ist.
* Sie können das Skalarprodukt berechnen.
* Sie kennen wichtige Eigenschaften des Skalarproduktes wie beispielsweise
  * **positive Definitheit**,
  * **Symmetrie** und
  * **Bilinearität**.
```

## Was ist das Skalarprodukt?

Wikipedia beschreibt das Skalarprodukt als »... eine mathematische Verknüpfung,
die zwei Vektoren eine Zahl (Skalar) zuordnet.« Etwas präziser wird eine positiv
definite, symmetrische Bilinearform, die zwei Vektoren einen Skalar zuordnet,
Skalarprodukt genannt. In dieser Vorlesung werden wir uns jedoch auf das
**Skalarprodukt** im reellen Standardvektorraum $\mathbb{R}^n$ beschränken.

Zur Motivation betrachten wie ein Beispiel, das nicht aus der Geometrie kommt.
Angenommen, Sie haben Aktien der DAX-Unternehmen adidas, BASF, Commerzbank,
Deutsche Telekom und E.ON. Die folgende Tabelle listet auf, wie viele Aktien Sie
von jedem dieser fünf Unternehmen besitzen.

|Unternehmen|Anzahl Aktien|
|---|---|
|adidas|5|
|BASF|3|
|Commerzbank|1|
|Deutsche Telekom|10|
|E.ON|7|

In einer weiteren Tabelle werden nun die Aktienkurse für zwei Tage notiert, z.B.
Montag und Dienstag von dieser Woche:

|Aktienkurs|Montag|Dienstag|
|---|---|---|
|adidas|216.50 €|211.37 €|
|BASF|42.55 €|41.89 €|
|Commerzbank|12.76 €|12.50 €|
|Deutsche Telekom|25.15 €|27.21 €|
|E.ON|12.22 €|13.11 €|

Wenn Sie nun den Wert des gesamten Aktiendepots am Montag ermitteln wollen, muss
zuerst für jedes Unternehmen der Kurswert der Aktie mit der Anzahl der Aktien
multiplizert werden. Danach werden die Depots der Unternehmen aufsummiert. Für
Montag erhalten wir

$$5\cdot 216.5 \unicode{0x20AC} + 3\cdot 42.55 \unicode{0x20AC} + 1\cdot 12.76
\unicode{0x20AC} + 10\cdot 25.15 \unicode{0x20AC} + 7\cdot 12.22
\unicode{0x20AC} = 1559.95 \unicode{0x20AC}.$$

Soll nun für jedem Tag eines Jahres der aktuelle Wert des gesamten Aktiendepots
ermittelt werden, ist das händische Bilden der Zwischenprodukte und das
anschließende Aufsummieren etwas unpraktisch. So eine Aufgabe könnte besser eine
Tabellenkalkulationssoftware oder ein Computerprogramm übernehmen. Es bietet
sich an, die Anzahl der Aktien als ein 5-Tupel zu schreiben:

$$\vec{a} = \begin{pmatrix} 5 \\ 3 \\ 1 \\ 10 \\ 7 \end{pmatrix}.$$

Den aktuellen Aktienkurs können wir ebenfalls als ein 5-Tupel notieren, das
Euro-Symbol für die Währung lassen wir dabei weg:

$$\vec{k} = \begin{pmatrix} 216.5 \\ 42.55 \\ 12.76 \\ 25.15 \\ 12.22
\end{pmatrix}.$$

Beides sind Vektoren des reellen Standardvektorraumes, denn wir können die
Vektoraddition und skalare Multiplikation sinnvoll als Änderungen des
Aktienkurses oder den Zukauf oder Verkauf von Aktien interpretieren. Darüber
hinaus führen wir jetzt noch eine neue mathematische Verknüpfung ein, die den
Wert des Gesamtdepots ermittelt. Wir verwenden dazu (wieder einmal) das Symbol
$\;\cdot\;$

$$\vec{a} \cdot \vec{k} =
\begin{pmatrix} 5 \\ 3 \\ 1 \\ 10 \\ 7 \end{pmatrix} \cdot
\begin{pmatrix} 216.5 \\ 42.55 \\ 12.76 \\ 25.15 \\ 12.22 \end{pmatrix} =
5\cdot 216.5 + 3\cdot 42.55 + 1\cdot 12.76 + 10\cdot 25.15 + 7\cdot 12.22 = 1559.95.$$

Diese mathematische Verknüpfung hat noch viele weitere Anwendungen in der Physik
und in der Geometrie, so dass sie einen eigenen Namen bekommen hat:
Skalarprodukt. Allgemein wird sie folgendermaßen definiert.

```{admonition} Was ist ... das Skalarprodukt?
:class: note
Sind $\vec{a}\in\mathbb{R}^n$ und $\vec{b}\in\mathbb{R}^n$ zwei Vektoren des
reellen Standardvektorraumes, so wird die mathematische Verknüpfung

$$\vec{a} \cdot \vec{b} =
\begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_n \end{pmatrix} \cdot
\begin{pmatrix} b_1 \\ b_2 \\ \vdots \\ b_n \end{pmatrix} =
a_1 \cdot b_1 + a_2 \cdot b_2 + \ldots + a_n \cdot b_n =
\sum_{i=1}^{n} a_i \cdot b_i $$

Skalarprodukt genannt.
```

Damit haben wir nun die dritte Bedeutung des Symbols $\;\cdot\;$ kennengelernt.
Bei den folgenden drei Verknüpfungen wird das Symbol $\;\cdot\;$ benutzt. Nur
aus dem Zusammenhang wird klar, welche Verknüpfung gemeint ist.

1. **Multiplikation**, also Skalar "mal" Skalar = Skalar, z.B.

   $$3\cdot 2 = 6,$$

2. **skalare Multiplikation**, also Skalar "mal" Vektor = Vektor, z.B.

   $$3\cdot \begin{pmatrix} -1 \\ 3.1 \end{pmatrix} = \begin{pmatrix} -3 \\ 9.3 \end{pmatrix},$$

3. **Skalarprodukt**, also Vektor "mal" Vektor = Skalar, z.B.

   $$\begin{pmatrix} 1 \\ 2 \end{pmatrix} \cdot \begin{pmatrix} -1 \\ 3.1
   \end{pmatrix} = 5.2.$$

Die folgenden Videos zeigen weitere Beispiele zur Berechnung des Skalarproduktes
von zwei Vektoren. Danach werden wir uns mit allgemeinen Eigenschaften des
Skalarproduktes beschäftigen.

```{dropdown} Video "Skalarprodukt" von Visual X
<iframe width="560" height="315" src="https://www.youtube.com/embed/1T1aTlEUO0E"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay;
clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

```{dropdown} Video "Skalarprodukt berechnen" von Einfach Mathe!
<iframe width="560" height="315" src="https://www.youtube.com/embed/EpOG1alQUz0?si=E3uP3xzkf8kA2PHB"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share"
referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
```

## Eigenschaften des Skalarproduktes

Das Skalarprodukt hat einige sehr wichtige Eigenschaften. Für jeden Vektor
$\vec{a}\in\mathbb{R}^n$ gilt, dass das Skalarprodukt des Vektors mit sich
selbst positiv ist. Null kann das Skalarprodukt eines Vektors mit sich selbst
nur werden, wenn der Vektor $\vec{a}$ der Nullvektor ist. Negativ hingegen wird
das Skalarprodukt eines Vektors mit sich selbst nie. Wir können leicht
nachrechnen, dass diese Aussagen stimmen, indem wir das Skalarprodukt des
Vektors $\vec{x}$ mit sich selbst ausrechnen:

$$\vec{a}\cdot\vec{a} = a_1 \cdot a_1 + a_2 \cdot a_2 + \ldots + a_n \cdot a_n =
 a_1^2 + a_2^2 + \ldots + a_n^2.$$

Da jede Komponente $a_i$ eine reelle Zahl ist, sind die Quadrate der Komponenten
nicht-negativ, also $a_i^2 \geq 0$. Damit ist aber auch die Summe der Quadrate
$a_1^2 + a_2^2 + \ldots + a_n^2$ nicht-negativ. Nur wenn der Vektor $\vec{a}$
der Nullvektor ist, dann haben wir

$$\vec{0} \cdot \vec{0} = 0\cdot 0 + 0\cdot 0 + \ldots + 0\cdot0 = 0.$$

Diese Eigenschaft nennt man **positive Definitheit** bzw. man bezeichnet das
Skalarprodukt als **positiv definit**.

Das Skalarprodukt ist auch **symmetrisch** und erfüllt das **Kommutativgesetz**. Es gilt

$$\vec{a} \cdot \vec{b} = \vec{b} \cdot \vec{a},$$

was auch leicht nachgerechnet werden kann:

\begin{align*} \vec{a}\cdot\vec{b} &= a_1\cdot b_1 + a_2\cdot b_2 + \ldots +
a_n\cdot b_n =\\
&= b_1\cdot a_1 + b_2\cdot a_2 + \ldots + b_n\cdot a_n = \vec{b}\cdot\vec{a}\\
\end{align*}

Es überträgt sich sozusagen die Symmetrie der "normalen" Multiplikation von
den reellen Zahlen auf das Skalarprodukt.

Für das Skalarprodukt gilt darüber hinaus das **gemischte Assoziativgesetz**.
Sind $\vec{a}$ und $\vec{b}$ zwei Vektoren des reellen Standardvektorraumes,
also $\vec{a}, \vec{b}\in\mathbb{R}^n$ und ist $s$ ein Skalar, also
$s\in\mathbb{R}$, dann gilt

$$(s\cdot\vec{a})\cdot\vec{b} = s\cdot (\vec{a}\cdot\vec{b}) = \vec{a}\cdot
(s\cdot\vec{b}).$$

Ein richtiges Assoziativgesetz gilt für das Skalarprodukt nicht. Im Allgemeinen
gilt also

$$(\vec{a}\cdot\vec{b})\cdot\vec{c} \textcolor{red}{\neq}
\vec{a}\cdot(\vec{b}\cdot\vec{c}).$$

Das Skalarprodukt ist **nicht assoziativ**.

Die letzte Eigenschaft, mit der wir uns in diesem Kapitel beschäftigen wollen,
ist das **Distributivgesetz**. Es gelten für alle Vektoren $\vec{a}, \vec{b},
\vec{c} \in \mathbb{R}^n$ die beiden Distributivgesetze

\begin{align*}
(\vec{a}+\vec{b})\cdot\vec{c} &= \vec{a}\cdot\vec{c} + \vec{a}\cdot\vec{c} \\
\vec{a}\cdot(\vec{b}+\vec{c}) &= \vec{a}\cdot\vec{b} + \vec{a}\cdot\vec{c} \\
\end{align*}

Aufgrund der beiden letzten Eigenschaften, dem gemischten Assoziativgesetzt und
dem Distributivgesetz, wird das Skalarprodukt **bilinear** genannt.

Wir fassen zusammen: Das Skalarprodukt ist eine positiv definite, symmetrische
Bilinearform. Tatsächlich wird in vielen mathematischen Disziplinen umgekehrt
vorgegangen und jede positiv definite, symmetrische Bilinearform als
Skalarprodukt bezeichnet. Das Skalarprodukt aus diesem Kapitel ist nur eines
unter vielen Skalarprodukten. Da es in natürlicher Weise zum reellen
Standardvektorraum gehört, wird es auch **Standardskalarprodukt** genannt.

## Zusammenfassung und Ausblick

Nachdem wir in diesem Kapitel das Skalarprodukt des reellen Standardvektorraumes
und seine Eigenschaften kennengelernt haben, werden wir es im nächsten Kapitel
in der Geometrie anwenden.
