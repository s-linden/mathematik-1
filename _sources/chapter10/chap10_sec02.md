# 10.2 Ableitung von elementaren Funktionen

Es ist umständlich, den Differentialquotienten zu berechnen. Glücklicherweise
sind für viele wichtige Funktionen die Ableitungen schon bekannt.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können eine konstante Funktion ableiten, d.h. 

$$f(x)=C \Rightarrow f'(x)=0.$$

* Sie können eine Potenzfunktion ableiten, d.h. 

$$f(x)=x^{n} \; (n\in\mathbb{N})\; \Rightarrow f'(x)=n\cdot x^{n-1}.$$

* Sie können die Wurzelfunktion ableiten, d.h. 

$$f(x)=\sqrt{x} \Rightarrow f'(x)=\frac{1}{2\sqrt{x}}.$$

* Sie können die trigonometrischen Funktionen ableiten, d.h.
\begin{align*}
f(x)=\sin(x) &\Rightarrow f'(x)=\cos(x) \\ 
f(x)=\cos(x) &\Rightarrow f'(x)=-\sin(x) \\ 
f(x)=\tan(x) &\Rightarrow f'(x)=\frac{1}{\cos^2(x)} \\ 
f(x)=\cot(x) &\Rightarrow f'(x)=-\frac{1}{\sin^2(x)} \\ 
\end{align*}
* Sie können die Exponentialfunktion ableiten, d.h. 

$$f(x)=e^{x}=\exp(x) \Rightarrow f'(x)=e^{x}=\exp(x).$$

* Sie können die Logarithmusfunktion ableiten, d.h. 

$$f(x)=\ln(x) \Rightarrow f'(x)=\frac{1}{x}.$$
```

## Die Ableitungsfunktion

Im letzten Kapitel haben wir den Differentialquotienten bzw. die Ableitung an
einer einzelnen Stelle berechnet. In diesem Abschnitt wollen wir dieses Vorgehen
auf ein Intervall verallgemeinern. Wir betrachten dazu als Beispiel die Funktion
$f(x) = x^2$. Zunächst berechnen wir die Ableitung an einer einzelnen Stelle,
beispielsweise für $x_1 = 2$. Dazu bilden wir den Grenzwert der Folge der
Differentialquotienten:

\begin{align*}
f'(2)
&= \lim_{x_2 \to 2} \frac{f(x_2) - f(2)}{x_2 - 2} = \\
&= \lim_{x_2 \to 2} \frac{x_2^2 - 4}{x_2 - 2} = \\
&= \lim_{x_2 \to 2} \frac{(x_2 - 2) \cdot (x_2 + 2)}{x_2 - 2} = \\
&= \lim_{x_2 \to 2} x_2 + 2 = \\
&= 4.
\end{align*}

Jetzt verallgemeinern wir die Grenzwertbildung auf beliebige Stellen
$x\in\mathbb{R}$. Die Vorgehensweise zur Berechnung des Grenzwertes bleibt dabei
gleich:

\begin{align*}
f'(x)
&= \lim_{x_2 \to x} \frac{f(x_2) - f(x)}{x_2 - x} = \\
&= \lim_{x_2 \to x} \frac{x_2^2 - x^2}{x_2 - x} = \\
&= \lim_{x_2 \to x} \frac{(x_2 - x) \cdot (x_2 + x)}{x_2 - x} = \\
&= \lim_{x_2 \to x} x_2 + x = \\
&= 2x.
\end{align*}

Wir haben also zu jeder Stelle $x\in\mathbb{R}$ einen Wert für die Ableitung
$f'(x)$ an dieser Stelle gefunden, nämlich $f'(x) = 2x$. Damit ist $f'$ eine
Funktion, denn jedem x-Wert wird eindeutig ein y-Wert f'(x) zugeordnet. Diese
Erkenntnis klingt erst einmal banal, hilft ungemein bei der konkreten Berechnung
von Ableitungen. Für häufig vorkommene Funktionen sind deren
Ableitungsfunktionen in Tabellen hinterlegt. Und wie wir in den nächsten
Abschnitten sehen werden, können viele komplizierte Funktionen aus einfachen
Grundfunktionen zusammengesetzt werden. Kennen wir die Ableitungsfunktionen der
Grundfunktionen, können wir so wieder die Ableitungsfunktion der komplizierten
Funktion zusammensetzen.

```{admonition} Was ist ... die Ableitungsfunktion?
:class: note
Wenn für eine Funktion $f$ an jeder Stelle ihrer Definitionsmenge die Ableitung
existiert, kann eine neue Funktion gebildet werden, die jedes $x$ aus der
Definitionsmenge auf die Ableitung $f'(x)$ abbildet. Diese Funktion $f'$ wird
Ableitungsfunktion von $f$ genannt.
```

## Ableitungen von wichtigen Grundfunktionen

Eine **konstante Funktion** ist besonders leicht abzuleiten, denn die Ableitung
ist an jeder Stelle Null:

$$f(x)=C \Rightarrow f'(x)=0.$$

Beispiel:

$$f(x) = 5 \Rightarrow f'(x) = 0.$$

Die Ableitung einer Potenzfunktion ergibt wieder eine Potenzfunktion, allerdings
wird der Exponent um Eins verringert und der alte Exponent wird ein neuer
Vorfaktor. Für natürliche Exponenten $n\in\mathbb{N}$ lautet die
Ableitung:

$$f(x)=x^{n} \Rightarrow f'(x)=n\cdot x^{n-1}.$$

Die Wurzelfunktion ist etwas schwieriger abzuleiten.

$$f(x)=\sqrt{x} \Rightarrow f'(x)=\frac{1}{2\sqrt{x}}.$$

Tatsächlich kann die Wurzelfunktion auch als Potenzfunktion interpretiert
werden, also $\sqrt{x} = x^{\frac{1}{2}}$. Für Potenzfunktionen, bei denen der
Exponent ein Bruch oder gar eine reelle Zahl ist, gelten dieselben
Ableitungsregeln wie für Potenzfunktionen mit natürlichem Expoenten. Die einzige
Einschränkung dabei ist, dass $x$ positiv sein muss.

$$f(x) = x^{r} \Rightarrow f'(x) = r\cdot x^{r-1}, \quad x >0.$$

Mit diesem Wissen kann die Ableitung der Wurzelfunktion auch folgendermaßen
berechnet werden:

$$f(x) = x^{\frac{1}{2}} \Rightarrow f'(x) = \frac{1}{2} x^{-\frac{1}{2}} = \frac{1}{2} \frac{1}{x^{\frac{1}{2}}} = \frac{1}{2}\frac{1}{\sqrt{x}}.$$

Die Liste der Ableitungen der trigonometrischen Funktionen lautet:
\begin{align*}
f(x)=\sin(x) &\Rightarrow f'(x)=\cos(x) \\
f(x)=\cos(x) &\Rightarrow f'(x)=-\sin(x) \\
f(x)=\tan(x) &\Rightarrow f'(x)=\frac{1}{\cos^2(x)} \\
f(x)=\cot(x) &\Rightarrow f'(x)=-\frac{1}{\sin^2(x)} \\
\end{align*}

Am einfachsten lässt sich die Exponentialfunktion ableiten, sie bleibt sie
selbst.

$$f(x)=e^{x}=\exp(x) \Rightarrow f'(x)=e^{x}=\exp(x).$$

Zum Abschluss der Liste mit den wichtigsten Ableitungsfunktionen notieren wir
noch die Ableitung der Logarithmsfunktion:

$$f(x)=\ln(x) \Rightarrow f'(x)=\frac{1}{x}.$$

```{dropdown} Video zu "Wichtige Ableitungen" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/Jf7-EVLjpZg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

> - [Studyflix: Exponentialfunktion ableiten](https://studyflix.de/mathematik/e-funktion-ableiten-1850)
> - [Studyflix: Logarithmusfunktion ableiten](https://studyflix.de/mathematik/ln-ableiten-1851)
> - [Studyflix: Sinusfunktion ableiten](https://studyflix.de/mathematik/ableitung-sinus-1852)
> - [Studyflix: Kosinusfunktion ableiten](https://studyflix.de/mathematik/ableitung-cosinus-1853)
> - [Studyflix: Tangensfunktion ableiten](https://studyflix.de/mathematik/ableitung-tangens-1854)
> - [Studyflix: 1/x ableiten](https://studyflix.de/mathematik/ableitung-1-x-6523)
> - [Studyflix: Wuzel ableiten](https://studyflix.de/mathematik/wurzel-ableiten-1849)

## Zusammenfassung und Ausblick

Kennen wir die Ableitungen von elementaren Grundfunktionen, können wir oft
Ableitungen von komplizierteren Funktionen aus diesen zusammensetzen. Wie das
funktioniert, sehen wir im nächsten Kapitel.
