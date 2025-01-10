# 11.1 Stammfunktion

In diesem Abschnitt führen wir zunächst Stammfunktionen ein.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie wissen, was eine **Stammfunktion** ist.
* Sie wissen, dass wenn es eine Stammfunktion gibt, es gleich unendlich viele
  Stammfunktionen gibt, die sich durch eine **Integrationskonstante**
  unterscheiden.
```

## Stammfunktion

```{admonition} Was ist ... eine Stammfunktion?
:class: note
Angenommen, die Funktion $f$ ist stetig. Dann wird die Funktion $F$
Stammfunktion von $f$ genannt, wenn ihre Ableitungsfunktion gleich $f$ ist, also
wenn gilt $F'(x) =  f(x)$.
```

Beispiel: Wir betrachten die Funktion $f(x)=x$. Mit ein bisschen Probieren fällt
auf, dass die Funktion $F(x)=\frac{1}{2}x^2$ abgeleitet genau $x$ ergibt. Also
ist die Funktion $F$ eine Stammfunktion von $f$. Jetzt probieren wir die
Funktion $\tilde{F}(x)=\frac{1}{2}x^2+1$ aus. Wenn wir diese Funktion ableiten,
kommt

$$\tilde{F}'(x) = \left( \frac{1}{2}x^2 + 1 \right)'= x + 0 = x$$

heraus. Das ist aber auch gleich der Funktion $f$. Welches ist denn nun die
richtige Stammfunktion?

Beide Funktionen sind eine Stammfunktion. Wenn eine Funktion $f$ eine
Stammfunktion hat, dann hat sie gleich unendlich viele Stammfunktionen, denn es
muss nur eine reelle Zahl hinzuaddiert werden und schon hat man eine neue
Stammfunktion.

```{admonition} Wie viele Stammfunktionen gibt es?
:class: note
Wenn eine Funktion $f$ eine Stammfunktion hat, hat sie gleich unendlich viele
Stammfunktionen. Die Stammfunktionen unterscheiden sich nur dadurch, dass eine
reelle Zahl am Ende dazuaddiert wird. Diese Zahl wird **Integrationskonstante**
genannt.
```

Begründung: Wenn $F$ die erste gefundene Stammfunktion ist, dann muss ihre 1.
Ableitung gleich $f$ sein, also $F'(x) = f(x)$ gelten. Dann basteln wir eine
neue Funktion $\tilde{F}(x) = F(x) + c$ mit $c\in\mathbb{R}$. Das muss dann aber
auch eine Stammfunktion sein, denn

$$\tilde{F}'(x) = \left(F(x)+c\right)' = F'(x) + 0 = f(x).$$

```{dropdown} Video: Stammfunktion und unbestimmtes Integral
<iframe width="560" height="315" src="https://www.youtube.com/embed/m__ID4PHBIA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Wichtige Stammfunktionen

Zu Funktionen, die häufig im Maschinenbau vorkommen, sollten Sie die
Stammfunktionen auswendig kennen.

* $f(x) = a \Rightarrow F(x) = ax + c$
* $f(x) = x^{n} \Rightarrow F(x) = \frac{1}{n+1} x^{n+1} + c$ ($n$ muss ungleich -1 sein)
* $f(x) = x^{-1}=\frac{1}{x} \Rightarrow F(x) = |\ln(x)| + c$
* $f(x) = e^{x} \Rightarrow F(x)=e^{x}+c$
* $f(x) = \sin(x) \Rightarrow F(x)=-\cos(x)+c$
* $f(x) = \cos(x) \Rightarrow F(x)=\sin(x)+c$
* $f(x)=\frac{1}{1+x^2} \Rightarrow F(x) = \arctan(x) + c$

```{dropdown} Video: wichtige Stammfunktionen
<iframe width="560" height="315" src="https://www.youtube.com/embed/hKiAG99XmTE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Zusammenfassung und Ausblick

Im nächsten Kapitel lernen wir das bestimmte Integral kennen und klären, was das
bestimmte Integral mit einer Stammfunktion zu tun hat.
