# 12.2 Regel von Bernoulli-de L'Hospital

Die Regel von Bernoulli-de L'Hospital erlaubt die Berechnung von
Funktionsgrenzwerten der Form $\frac{0}{0}$ oder $\frac{\infty}{\infty}$. Oft
wird auch nur der kürzere Name Regel von L'Hospital verwendet.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können die Regel von Bernoulli-de L'Hospital anwenden, um Grenzwerte
  auszurechnen.
* Sie wissen, dass sich die Sinusfunktion für kleine Werte $x$ wie $x$ selbst
  verhält, also $\lim_{x\rightarrow 0} \frac{\sin(x)}{x} = 1.$
```

## Regel von Bernoulli-de L'Hospital

Die Regel von L'Hospital kann nur unter bestimmten Bedingungen angewendet werden:

1. **Form:** Der Grenzwert der betrachteten Funktionen muss entweder die Form
   $\frac{0}{0}$ oder $\frac{\infty}{\infty}$ haben.
2. **Differenzierbarkeit:** Sowohl der Zähler $f(x)$ als auch der Nenner $g(x)$
   müssen im betrachteten Intervall differenzierbar sein.
3. **Existenz des Grenzwertes:** Der Grenzwert $\lim_{x \to x_0}
   \frac{f'(x)}{g'(x)}$ muss existieren.

Seien $f(x)$ und $g(x)$ differenzierbar in einem Intervall um $x_0$ mit Ausnahme
von $x_0$ selbst. Wenn $\lim_{x \to x_0} f(x) = \lim_{x \to x_0} g(x) = 0$ oder
$\pm\infty$, dann gilt:

$$\lim_{x \to x_0} \frac{f(x)}{g(x)} = \lim_{x \to x_0} \frac{f'(x)}{g'(x)},$$

vorausgesetzt, der Grenzwert auf der rechten Seite existiert.

## Beispiele

### Beispiel 1: $\lim_{x \to 0} \frac{\sin(x)}{x}$

Die Funktionsgrenzwerte der Zählerfunktion $f(x)=\sin(x)$ und der Nennerfunktion
$g(x)=x$ lauten

$$\lim_{x\to 0}\sin(x) = 0, \; \lim_{x\to 0}x = 0.$$

Damit hat der Grenzwert

$$\lim_{x \to 0}\frac{\sin(x)}{x}$$

die Form $\frac{0}{0}$. Sowohl die Zählerfunktion als auch die Nennerfunktion
sind differenzierbar, ihre Ableitungen lauten

$$f'(x) = \cos(x), \; g'(x) = 1.$$

Damit können wir die Regel von L'Hospital anwenden:

$$\lim_{x \to 0} \frac{\sin(x)}{x} = \lim_{x \to 0} \frac{\cos(x)}{1} = \cos(0) = 1.$$

### Beispiel 2: $\lim_{x \to \infty} \frac{\ln(x)}{x}$

Die Funktionsgrenzwerte der Zählerfunktion $f(x)=\ln(x)$ und der Nennerfunktion
$g(x)=x$ lauten

$$\lim_{x\to\infty}\ln(x)=\infty, \; \lim_{x\to\infty}x = \infty.$$

Damit hat der Grenzwert

$$\lim_{x\to\infty}\frac{\ln(x)}{x}$$

die Form $\frac{\infty}{\infty}$. Beide Funktionen sind differenzierbar, ihre
Ableitungen lauten

$$f'(x) = \frac{1}{x}, \;  g'(x) = 1.$$

Damit können wir die Regel von L'Hospital anwenden:

$$\lim_{x \to \infty} \frac{\ln(x)}{x} = \lim_{x \to \infty}
\frac{\frac{1}{x}}{1} = \lim_{x \to \infty} \frac{1}{x} = 0.$$

## Mehrfaches Anwenden der Regel

Es kann vorkommen, dass die Regel von L'Hospital mehrmals angewendet werden
muss, wenn der Grenzwert nach dem ersten Schritt noch eine unbestimmte Form hat.
Ein Beispiel dafür ist $\lim_{x \to 0} \frac{1 - \cos(x)}{x^2}$.

Wir setzen $f(x) = 1 - \cos(x)$ und $g(x) = x^2$. Die ersten Ableitungen sind

$$f'(x) = \sin(x), \; g'(x) = 2x.$$

Die einmalige Anwendung der Regel von L'Hospital reicht diesmal nicht aus:

$$\lim_{x \to 0} \frac{1 - \cos(x)}{x^2} = \lim_{x \to 0} \frac{\sin(x)}{2x}.$$

Es liegt immer noch die Form $\frac{0}{0}$ vor. Aber wir können ein weiteres Mal
ableiten und die Regel von L'Hospital erneut anwenden:

$$\lim_{x \to 0} \frac{\sin(x)}{2x} = \lim_{x \to 0} \frac{\cos(x)}{2} = \frac{1}{2}.$$

Somit gilt insgesamt

$$\lim_{x \to 0} \frac{1 - \cos(x)}{x^2} = \lim_{x \to 0} \frac{\sin(x)}{2x} =
\lim_{x \to 0} \frac{\cos(x)}{2} = \frac{1}{2}.$$

Weitere Beispiele finden Sie in dem folgenden Video.

```{dropdown} Video "Grenzwerte von Funktionen: L'Hospital" von MathePeter
<iframe width="560" height="315" src="https://www.youtube.com/embed/qmfHgIBL-Jk"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Zusammenfassung und Ausblick

In diesem Kapitel haben Sie gelernt, Funktionsgrenzwerte von unbestimmten
Ausdrücken der Form $\frac{0}{0}$ und $\frac{\infty}{\infty}$ zu bestimmen,
falls die Funktionen differenzierbar sind. In den nächsten Kapiteln untersuchen
wir Funktionen bzgl. ihrer geometrischen Eigenschaften mit Hilfe von
Ableitungen.
