# 12.6 Integralfunktionen und das uneigentliche Integral

Das bestimmte Intgeral liefert eine Zahl. Wir können das bestimmte Integral auch
dazu nutzen, eine neue Funktion einzuführen, indem wir die untere Grenze auf
einen festen Wert setzen und die obere Grenze als Variable betrachten. Damit
erhalten wir die sogenannte Integralfunktion.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie wissen, was eine **Integralfunktion** ist.
* Sie kennen **uneigentliche Integrale**.
```

## Was ist die Integralfunktion?

Wenn wir einen Punkt $a\in\mathbb{R}$ festlegen, dann ist das bestimmte Integral

$$\int_{a}^{x} f(t)\, dt$$

eine Funktion, denn für jeden Wert $x\in\mathbb{R}$ wird durch diese Vorschrift
ein Funktionswert

$$I_{a}(x) = \int_{a}^{x} f(t)\, dt$$

erzeugt. Wichtig dabei ist, dass die untere Grenze $a$ festgelegt ist. Diese
Funktion wird **Integralfunktion** genannt.

Weitere Informationen finden Sie hier:

> [https://studyflix.de/mathematik/integralfunktion-6480](https://studyflix.de/mathematik/integralfunktion-6480)

## Uneigentliche Integrale

Uneigentliche Integrale treten auf, wenn ein Integral entweder eine oder zwei
unendliche Grenzen hat oder wenn der Integran unstetig ist. Das uneigentliche
Integral ist eine Erweiterung des bestimmten Integrals und erlaubt die Analyse
von Flächeninhalten oder Summen, die auf den ersten Blick divergieren könnten.

Wir gehen jetzt davon aus, dass $f$ eine Funktion ist, die auf jedem Intervall
$[a,b]$ mit $b\in (a,\infty)$ definiert ist. Wenn der Grenzwert

$$\lim_{t \to b}\int_{a}^{t} f(x)\, dx$$

existiert, dann nennt man

$$\int_{a}^{\infty} f(x)\, dx = \lim_{t \to b}\int_{a}^{t} f(x)\, dx$$

das uneigentliche Integral von $f$ über $[a,\infty)$.

Falls die untere Grenze unendlich sein sollte, wird analog vorgegangen. Ebenso
wird das Integral über einen Grenzwert definiiert, wenn der Integrand ein
einzelnen Stellen unstetig sein sollte.

Weitere Informationen finden Sie hier:

> [https://studyflix.de/mathematik/uneigentliche-integrale-1806](https://studyflix.de/mathematik/uneigentliche-integrale-1806)
