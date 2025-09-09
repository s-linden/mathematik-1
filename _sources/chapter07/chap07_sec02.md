# 7.2 Inverse Matrizen

In dem vorangegangenen Kapitel haben wir die Determinante kennengelernt. Mit
Hilfe der Determinante können wir beispielsweise entscheiden, ob ein lineares
Gleichungssystem eindeutig lösbar ist oder nicht. Dazu behandeln wir in diesem
Kapitel das Thema inverse Matrizen.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie wissen, wann es erlaubt ist, die **inverse Matrix** einer quadratischen
  Matrix zu berechnen und welche Rolle die Determinante dabei spielt.
* Sie können die **Inverse einer $2\times 2$-Matrix** berechnen.
* Sie können die **Inverse einer $n\times n$-Matrix** für $n>2$ berechnen.
* Sie kennen die **Rechenregeln für inverse Matrizen** und können sie anwenden.
```

## Inverse Matrix von $2\times 2$-Matrizen

Anhand der Überschrift können Sie schon erahnen, dass auch der Fachbegriff
**inverse Matrix** nur für quadratische Matrizen definiert ist. Wir beginnen mit
der Inversen einer $2 \times 2$-Matrix, also allgemein einer Matrix der Form

$$\mathbf{A} = \begin{pmatrix} a & b \\ c & d \end{pmatrix}.$$

Wenn die Determinante dieser Matrix *ungleich Null* ist, können wir die Inverse
$\mathbf{A}^{-1}$ mit der Definition

$$\mathbf{A}^{-1}=
\frac{1}{\det(\mathbf{A})} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$$

bilden. Jetzt ist auch ersichtlich, warum wir $\det{(\mathbf{A})}$ gefordert
haben, denn das Teilen durch Null ist strikt verboten.

Betrachten wir als Beispiel die Matrix

$$\mathbf{A} = \begin{pmatrix} 2 & 3 \\ 1 & 5 \end{pmatrix}.$$

Die Determinante lautet

$$\det(\mathbf{A}) = 2 \cdot 5 - 1 \cdot 3 = 10 - 3 = 7 \neq 0.$$

Da die Determinante ungleich null ist, können wir die Inverse der Matrix
berechnen. Wir setzen die Werte in die allgemeine Formel ein:

$$\mathbf{A}^{-1} = \frac{1}{7} \begin{pmatrix} 5 & -3 \\ -1 & 2 \end{pmatrix}.$$

Das ergibt die Inverse:

$$\mathbf{A}^{-1} =
\begin{pmatrix} \frac{5}{7} & \frac{-3}{7} \\ \frac{-1}{7} & \frac{2}{7} \end{pmatrix}.$$

Warum ist die Inverse so interessant? Wir berechnen das Matrizenprodukt
$\mathbf{A}\cdot\mathbf{A}^{-1}$:

$$\begin{pmatrix} 2 & 3 \\ 1 & 5 \end{pmatrix} \cdot
\frac{1}{7} \begin{pmatrix} 5 & -3 \\ -1 & 2 \end{pmatrix} =
\begin{pmatrix} 1 & 0 \\ 0 & 1 \\ \end{pmatrix}.$$

Das Ergebnis ist die Einheitsmatrix der Dimension $2\times 2$. Tatsächlich ist
das auch die Definition der inversen Matrix.

```{admonition} Was ist ... die inverse Matrix?
:class: note
Die inverse Matrix $\mathbf{A}^{-1}$ einer quadratischen Matrix $\mathbf{A}$ ist
ebenfalls eine quadratische Matrix, die wenn sie mit der ursprünglichen Matrix
multipliziert wird, die Einheitsmatrix $\mathbf{E}$ ergibt:

$$\mathbf{A}^{-1}\cdot \mathbf{A} = \mathbf{E}.$$
```

## Inverse Matrix von $n \times n$-Matrizen

Die obige Definition einer inversen Matrix ist für alle quadratischen Matrizen
gültig. Auch bei einer quadratischen $n\times n$-Matrix $\mathbf{A}$ ist also
die inverse Matrix $\mathbf{A}^{-1}$ diejenige Matrix, für die dann
$\mathbf{A}^{-1}\cdot\mathbf{A}=\mathbf{E}$ gilt. Leider gibt es keine so schöne
einfache Formel zur Berechnung der Inversen. Die Berechnung der Inversen einer
$n \times n$-Matrix ist aufwändiger als bei $2 \times 2$-Matrizen und erfordert
in der Regel eine systematische Methode. Eines der bekanntesten Verfahren ist
der Gauß-Algorithmus, den wir auch schon zur Lösung eines linearen
Gleichungssystems kennengelernt haben.

Das Gauß-Verfahren funktioniert durch das Anwenden von elementaren
Zeilenumformungen auf die Matrix $\mathbf{A}$, bis sie in die Einheitsmatrix
$\mathbf{E}$ umgewandelt ist. Dieselben Umformungen werden parallel auf eine
Einheitsmatrix der gleichen Dimension angewendet, um schließlich die Inverse zu
erhalten. Der Algorithmus verläuft in den folgenden Schritten:

1. Gegeben ist eine Matrix $\mathbf{A} \in \mathbb{R}^{n \times n}$.
2. Füge rechts neben $\mathbf{A}$ die Einheitsmatrix $\mathbf{E}$ dazu.
3. Wende elementare Zeilenumformungen an, um $\mathbf{A}$ in die Einheitsmatrix
   $\mathbf{E}$ zu überführen.
4. Führe die gleichen Zeilenumformungen mit der Einheitsmatrix $\mathbf{E}$
   rechts daneben durch.
5. Ist die ursprüngliche Matrix $\mathbf{A}$ in die Einheitsmatrix umgeformt,
   dann ist die ursprüngliche Einheitsmatrix rechts daneben nun die gesuchte
   inverse Matrix.

Am einfachsten ist es, sich den Gauß-Algorithmus im folgenden Video anzusehen.

```{dropdown} Video "INVERSE MATRIX 3x3 berechnen" von Mathematrick
<iframe width="560" height="315" src="https://www.youtube.com/embed/usya1zz-skM?si=TfW-HC43dbkEjoog"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
```

## Eigenschaften und Rechenregeln für inverse Matrizen

Die Inverse einer Matrix hat mehrere nützliche Eigenschaften, die häufig in der
linearen Algebra und in Anwendungen wie der Lösung von linearen
Gleichungssystemen verwendet werden. Im Folgenden listen wir die wichtigsten
Eigenschaften der Inversen einer Matrix auf.

### Inverse der Einheitsmatrix

Die Einheitsmatrix $\mathbf{E}$ ist immer invertierbar, und ihre Inverse ist sie
selbst:

$$\mathbf{E}^{-1} = \mathbf{E}.$$

Dies gilt für jede quadratische Einheitsmatrix beliebiger Dimension.

### Inverse des Produkts zweier Matrizen

Wenn $\mathbf{A}$ und $\mathbf{B}$ zwei invertierbare Matrizen der gleichen
Dimension sind, dann ist auch das Produkt $\mathbf{A} \cdot \mathbf{B}$
invertierbar, und es gilt:

$$\left(\mathbf{A} \cdot \mathbf{B}\right)^{-1} = \mathbf{B}^{-1} \cdot \mathbf{A}^{-1}.$$

Die Reihenfolge wird bei der Multiplikation der Inversen umgekehrt. Eine
Eselsbrücke für diese Rechenregel wird in dem folgenden Video gezeigt.

```{dropdown} Video "Inverse Matrix, Rechenregeln I" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/t1K_B1pPqmc?si=TMRR6UnIpu5mmEn4"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
```

### Inverse der inversen Matrix

Die Inverse einer Matrix ist eindeutig, und die Inverse der inversen Matrix ist
die ursprüngliche Matrix:

$$\left(\mathbf{A}^{-1}\right)^{-1} = \mathbf{A}.$$

### Inverse der Transponierten

Die Inverse der transponierten Matrix $\mathbf{A}^T$ ist die Transponierte der
Inversen von $\mathbf{A}$:

$$\left(\mathbf{A}^T\right)^{-1} = (\mathbf{A}^{-1})^T.$$

Das bedeutet, dass die Operationen der Inversion und der Transposition
miteinander vertauschbar sind.

### Inverse bei Skalarmultiplikation

Ist $s$ ein Skalar und $\mathbf{A}$ eine $n \times n$-Matrix, dann gilt für die
Inverse des Produkts von $s$ und $\mathbf{A}$:

$$ (s \cdot \mathbf{A})^{-1} = \frac{1}{s} \cdot \mathbf{A}^{-1}, \quad s \neq 0.$$

Das bedeutet, dass wenn der Skalar $s$ aus der Inversenoperation herausgezogen
wird, mit dem Kehrwert multipliziert werden muss.

### Inverse bei symmetrischen Matrizen

Ist eine Matrix symmetrisch, ist ihre inverse Matrix ebenfalls symmetrisch.

Die oben genannten Rechenregeln werden auch in dem folgenden Video erläutert.

```{dropdown} Video "Inverse Matrix, Rechenregeln II" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/6JHgy82gwiI?si=EPTgIjTOjyCvW2qp"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
```

## Zusammenfassung und Ausblick

In diesem Kapitel haben wir die Berechnung und Eigenschaften der Inversen von
Matrizen behandelt. Dabei haben wir gesehen, dass die Inverse existiert, wenn
die Determinante ungleich null ist, und wie man sie mit dem Gauß-Algorithmus
berechnet.

Im nächsten Kapitel werden wir orthogonale Matrizen untersuchen, die besondere
Eigenschaften haben, wie die Gleichheit von Transponierter und Inverser. Diese
Matrizen werden beispielsweise in der Robotik eingesetzt, um Rotationen zu
beschreiben.
