# 9.2 Grenzwert einer Zahlenfolge

Im letzten Kapitel haben wir gelernt, was Zahlenfolgen sind und auch die beiden
Eigenschaften Monotonie und Beschränktheit betrachtet. In diesem Kapitel geht es
darum abzuschätzen, wie sich eine Folge für große Indizes verhält.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie wissen, was der **Grenzwert** einer Folge ist. Manchmal wird der Grenzwert
  auch als **Limes** bezeichnet. Das kommt aus dem Lateinischen, erinnert aber
  auch an den englischen Begriff Limit. 
* Sie wissen, dass eine Zahlenfolge **konvergent** genannt wird, wenn sie einen
Grenzwert hat. Außerdem kennen Sie die beiden üblichen Schreibweisen für
Grenzwerte: 

\begin{equation*} (a_n) \rightarrow a \text{ für } n \rightarrow
\infty \quad \text{ oder } \quad \lim_{n\rightarrow\infty} a_n = a.
\end{equation*} 

Man sagt dazu: »Der Limes von $a_n$ für $n$ gegen unendlich ist
$a$.« 
* Sie wissen, dass eine Zahlenfolge, die keinen Grenzwert hat, **divergent**
  genannt wird.
* Sie wissen, dass eine Zahlenfolge mit dem Grenzwert 0 **Nullfolge** heißt.  
* Sie wissen, dass jede monotone und beschränkte Folge automatisch konvergent
  ist (also einen Grenzwert hat).
```

## Grenzwert einer Folge

In technischen Systemen, wie Feder-Dämpfer-Systemen, treten oft Schwingungen
auf, deren Amplitude mit der Zeit abnimmt. Die Amplitudenfolge $a_n = A_0 \cdot
e^{-kn}$ beschreibt die Abnahme der Schwingung, wobei $A_0$ die Anfangsamplitude
ist und $k$ der Dämpfungskoeffizient.

Für $A_0 = 10$ und $k = 0.2$ ergibt sich:

- $a_1 = 10 \cdot e^{-0.2} \approx 8.19$
- $a_2 = 10 \cdot e^{-0.4} \approx 6.70$
- $a_3 = 10 \cdot e^{-0.6} \approx 5.49$
- $a_4 = 10 \cdot e^{-0.8} \approx 4.49$
- $a_5 = 10 \cdot e^{-1} \approx 3.68$

Die Amplitudenfolge lautet: $10, 8.19, 6.70, 5.49, 4.49, 3.68 \dots$.

Wenn wir diese Amplitudenfolge weiter betrachten, wird die Amplitude immer
weiter gedämpft, bis sie irgendwann kaum noch von Null zu unterscheiden ist.
Allgemein kann sich eine Folge $(a_n)$ einem festen Wert $a$ annähern, wenn $n$
gegen unendlich geht. Diesen Wert nennt man den Grenzwert der Folge.

Die mathematisch präzise Definition eines Grenzwertes lautet wie folgt.

```{admonition} Was ist ... der Grenzwert?
:class: note
Eine Folge $(a_n)$ besitzt den Grenzwert $a$, wenn für jede (sehr kleine) Zahl
$\varepsilon >0$ alle Folgenglieder $a_n$ ab einem bestimmten Index $N$ in dem
offenen Intervall um $a$ liegen, d.h.

$$|a_{n} - a| < \varepsilon, \quad \text{ falls } n \geq N.$$
```

Eine Zahlenfolge, die einen Grenzwert besitzt, heißt **konvergent**. Wenn dieser
Grenzwert Null ist, wird die Folge eine **Nullfolge** genannt.

```{dropdown} Video "konvergente Zahlenfolgen" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/bG4qS9eHKM0"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

```{dropdown} Video "Grenzverhalten von Folgen" von MathePeter
<iframe width="560" height="315" src="https://www.youtube.com/embed/ag_SQh4Ikds?si=YaDprtKvxNXzcLGv" 
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; 
encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
```

```{dropdown} Video "Grenzwert Folge" von Mathematrick
<iframe width="560" height="315" src="https://www.youtube.com/embed/p4itQ6UmtXA?si=JP66PWQVX2OwoI_K"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
```

## Beispiel

Die Folge $a_n = 2 + \frac{1}{n}$ hat vermutlich den Grenzwert $a=2$. Dies
wollen wir überprüfen. Wir probieren zunächst mit einem Taschenrechner aus, ob
wir für verschiedene (sehr kleine) Werte von $\varepsilon > 0$ einen Index $N$
finden, so dass

$$\left|2 + \frac{1}{n} - 2\right| < \varepsilon$$

gilt. Da $\frac{1}{n}$ für alle natürlichen Zahlen $n$ positiv ist, können wir
obige Ungleichung vereinfachen zu

$$\frac{1}{n} < \varepsilon.$$

Damit finden wir leicht die folgenden Indizes $N$ mit dem Taschenrechner:

- $\varepsilon = 0.1$: Index $N = 11$
- $\varepsilon = 0.01$: Index $N = 101$
- $\varepsilon = 0.001$: Index $N = 1001$

Allgemein können wir festhalten, dass die Ungleichung $\frac{1}{n} <
\varepsilon$ erfüllt ist, wenn $N$ größer gewählt wird als
$\frac{1}{\varepsilon}$. Damit gilt für dieses Beispiel

$$ \left(2+\frac{1}{n}\right) \rightarrow 2 \; \text{ für } \; n \rightarrow
\infty \quad \text{ oder } \quad \lim_{n\rightarrow\infty} \left(2+\frac{1}{n}\right) = 2.$$

## Divergente Zahlenfolgen

Nicht jede Zahlenfolge besitzt einen Grenzwert. Folgen, die keinen Grenzwert
haben, werden **divergent** genannt. Typische Beispiele für divergente Folgen
sind unbeschränkte Folgen wie die folgenden Beispiele.

1. Unbeschränkt wachsende Folge:<br>
   $a_n = n \quad \text{mit} \quad a_1 = 1, \, a_2 = 2, \, a_3 = 3, \dots $

2. Unbeschränkt fallende Folge:<br>
   $b_n = -n \quad \text{mit} \quad b_1 = -1, \, b_2 = -2, \, b_3 = -3, \dots $

Aber auch beschränkte Folgen können keinen Grenzwert haben, wie die folgenden
Beispiele zeigen.

3. Periodische Folge ohne Grenzwert:<br>
   $c_n = (-1)^n \quad \text{mit} \quad c_1 = 1, \, c_2 = -1, \, c_3 = 1, \, c_4 = -1, \dots $

4. Unregelmäßige Folge:<br>
   $d_n = \sin(n) \quad \text{mit} \quad d_1 = \sin(1), \, d_2 = \sin(2), \, d_3 = \sin(3), \dots $

Die ersten beiden Beispiele für divergente Folgen sind unbeschränkte Folgen. Im
dritten und vierten Beispiel sind die Zahlenfolgen beschränkt, jedoch nicht
monoton. Tatsächlich kann man beweisen, dass monotone und beschränkte Folgen
konvergent sind.

```{admonition} Konvergenz für monotone und beschränkte Folgen
:class: hint
Jede monotone und beschränkte Folge ist konvergent.
```

Die Umkehrung gilt nicht unbedingt. Zwar ist jede konvergent Folge beschränkt,
aber nicht jede konvergente Folge ist monoton. Beispielsweise ist die Folge

$$a_n = \frac{(-1)^n}{n}$$

eine Nullfolge, d.h. sie hat den Grenzwert Null. Dennoch ist sie nicht monoton.

```{dropdown} Video "divergente Zahlenfolgen" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/YUyyKPzurMw"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

```{dropdown} Video "Konvergenz - Beschränktheit - Monotonie" von Prof. Hoever
<iframe width="560" height="315" src="https://www.youtube.com/embed/lsRMf7e8M98?si=xSWUu1H6ytaeuH-3"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
```

## Zusammenfassung und Ausblick

In diesem Kapitel haben wir gelernt, was ein Grenzwert einer Folge ist. Im
nächsten Kapitel werden wir uns damit beschäftigen, wie Grenzwerte leichter aus
schon bekannten Grenzwerten berechnet werden können.
