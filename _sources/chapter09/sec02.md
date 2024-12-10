# 9.2 Grenzwert einer Zahlenfolge

Im letzten Kapitel haben wir gelernt, was Zahlenfolgen sind und auch die beiden
Eigenschaften Monotonie und Beschränktheit betrachtet. In diesem Kapitel geht es
darum abzuschätzen, wie sich eine Folge für große Indizes verhält.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie wissen, was der **Grenzwert** einer Folge ist. Manchmal wird der Grenzwert auch als **Limes** bezeichnet. Das kommt aus dem Lateinischen, erinnert aber auch an den englischen Begriff Limit. 
* Sie wissen, dass eine Zahlenfolge **konvergent** genannt wird, wenn sie einen Grenzwert hat. Außerdem kennen Sie die beiden üblichen Schreibweisen für Grenzwerte: 
\begin{equation*}
(a_n) \rightarrow a \text{ für } n \rightarrow \infty \quad \text{ oder } \quad \lim_{n\rightarrow\infty} a_n = a.
\end{equation*}
Man sagt dazu: »Der Limes von $a_n$ für $n$ gegen unendlich ist $a$.« 
* Sie wissen, dass eine Zahlenfolge, die keinen Grenzwert hat, **divergent** genannt wird.
* Sie wissen, dass eine Zahlenfolge mit dem Grenzwert 0 **Nullfolge** heißt.  
* Sie wissen, dass jede monotone und beschränkte Folge automatisch konvergent ist (also einen Grenzwert hat).
```

## Grenzwert

```{admonition} Was ist ... der Grenzwert?
:class: note
Eine Folge $(a_n)$ besitzt den Grenzwert $a$, falls für jede (sehr kleine) Zahl
$\varepsilon >0$ alle Folgenglieder $a_n$ ab einem bestimmten Index $N$ in dem
offenen Intervall um $a$ liegen, d.h.

$$|a_{n} - a| < \varepsilon, \quad \text{ falls } n \geq N.$$
```

## Videos

```{admonition} Video
:class: seealso
<iframe width="560" height="315" src="https://www.youtube.com/embed/bG4qS9eHKM0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

```{admonition} Video
:class: seealso
<iframe width="560" height="315" src="https://www.youtube.com/embed/YUyyKPzurMw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```
