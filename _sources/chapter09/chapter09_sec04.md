# Funktionsgrewnzwerte und ihre Rechenregeln

## Lernziele

```{admonition} Lernziele 
:class: tip
* Sie wissen, was ein **Funktionsgrenzwert** ist. Dazu wird eine Folge von Zahlen $(x_n)$ genommen, die gegen den Grenzwert $x_0$ konvergiert, und dann in die Funktion $f$ eingesetzt. Wenn dann die dadurch entstehende Folge $f(x_n)$ konvergent ist, nennt man diesen Grenzwert $F$ Funktionsgrenzwert von der Funktion $f$ an der Stelle $x_0$. Wir schreiben entweder
\begin{equation*}
\lim_{x\rightarrow x_0} f(x) = F \quad \text{ oder } \quad f(x)\rightarrow F \text{ für } x \rightarrow x_0. 
\end{equation*}
* Sie kennen die Rechenregeln für Funktionsgrenzwerte, also wenn $f$ und $g$ Funktionen sind mit $\lim_{x\rightarrow x_0}f(x)=F$ und $\lim_{x\rightarrow x_0}g(x)=G$, dann gilt
    * Addition: $\lim_{x\rightarrow x_0} (f(x)+g(x)) = F+G$
    * Subtraktion: $\lim_{x\rightarrow x_0} (f(x)-g(x)) = F-G$
    * Multiplikation: $\lim_{x\rightarrow x_0} (f(x)\cdot g(x)) = F\cdot G$
    * Division: $\lim_{x\rightarrow x_0} \left(\frac{f(x)}{g(x)} \right) = \frac{F}{G}\quad$ (vorausgesetzt $g(x), \,G\neq 0$)

* Sie können Funktionsgrenzwerte von links und von rechts unterscheiden. Mit Funktionsgrenzwert von links meint man, dass man nur Zahlenfolgen betrachtet, für die $(x_n)$ kleiner als $x_0$ ist und die sich $x_0$ von links annähern. Umgekehrt meint der Funktionsgrenzwert von rechts, das man nur Zahlenfolgen $(x_n)$ nimmt, die sich $x_0$ von rechts annähern. Man verwendet die beiden Schreibweisen
\begin{align*}
\text{linksseitig:} \quad \lim_{x\rightarrow x_0^{\textcolor{blue}{-}}} f(x) = F \quad &\text{ bzw.} \quad \lim_{x\textcolor{blue}{\nearrow} x_0} f(x) = F \\
\text{rechtsseitig:} \quad \lim_{x\rightarrow x_0^{\textcolor{blue}{+}}} f(x) = F \quad &\text{ bzw.} \quad \lim_{x\textcolor{blue}{\searrow} x_0} f(x) = F 
\end{align*}
```

## Videos

