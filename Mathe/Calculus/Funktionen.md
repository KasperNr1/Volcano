# Begriffe
Eine Funktion ist eine Zuordnung aller Zahlen aus der [Definitionsmenge](Intervalle%20und%20Mengen.md#Mengen) $D$ zu genau einer Zahl aus der Wertemenge $W$.
Def- und Wertemenge lassen sich als [Intervalle](Intervalle%20und%20Mengen.md) schreiben, wie $D_f=[0; \infty)$ 

## Darstellung
Funktionen können explizit oder implizit dargestellt werden. 
Ersteres ist eine Vorschrift die beschreibt, wie aus den Eingabewerten der Ausgabewert berechnet werden kann.
Man schreibt 
$$f(x)$$
Beispiel:
$$
f(x) = 2x+1
$$

Bei Impliziten Funktionen wird auf eine direkte Zuordnung von Ein- und Ausgabewerten verzichtet. Es wird eine Bedingung beschrieben, die von verschiedenen Kombinationen aus Koordinaten erfüllt sein kann.
$$F(x,y) = 0$$
Beispiel:
$$F(x,y) = x^2+y^2-1=0$$
Nicht alle Funktionen können in beiden Formen dargestellt werden. Diese implizite Funktion beschreibt den Einheitskreis. Da sich mehrere Punkte des Graphen übereinander befinden kann die Funktion nicht explizit beschrieben werden.

# Grenzwert
Der Grenzwert einer Zahl ist die Zahl, der die Funktionswerte beliebig nahe kommen, wenn $x$ sich in eine gewisse Richtung verändert.
Eine Funktion hat an der Stelle $x_0$ den Grenzwert $g$ wenn gilt:
$$\lim_{x\to x_0}f(x)=\lim_{y\to x_0}f(y)=g$$
mit $x>x_0$ und $y<x_0$.

## Schreibweise
$$
\lim_{n \to \infty}(f(x))=g
\lim_{n \to 0}(2n+1)=1
$$

# Stetig
Eine Funktion ist dann stetig, wenn der [Grenzwert](#Grenzwert) in jedem Punkt der [Definitionsmenge](Intervalle%20und%20Mengen.md) mit dem Funktionswert übereinstimmt.

# Lineare Funktionen
Sind Funktionen der Form $f(x)=mx+b$ 
Die Steigung $m$ ist hierbei konstant, wodurch ihr Schaubild stehts eine gerade Linie darstellt. 

# Quadratische Funktionen
Entsprechen der allgemeinen Form $f(x)=ax^2+bx+c$
Der Graph folgt einer Parabel.
Häufig müssen die Nullstellen der Funktion berechnet werden, hier hilft die [Mitternachtsformel](Gleichungen.md#Quadratische%20Gleichungen) 

# Potenzfunktionen
Funktionen der Form $f(x)=x^n$
Die Form wird als Parabel $n$-ten Grades bezeichnet. (Ausnahme $n=1$)

# Ganzrationale Funktionen
Auch Polynomfunktionen genannt bestehen aus mehreren Potenzfunktionen die mit unterschiedlichen Faktoren addiert werden.
$f(x)=a_nx^n + a_{n-1}x^{n-1} + \dots + a_1x + a_0$ 
$n =$ Grad der Funktion
$a_0 =$ Abschlussglied

# Symmetrie

## Achsensymmetrie zur $Y$-Achse
Ist gegeben wenn für jeden Punkt auf einer Funktion $f$ gilt:
$$f(x)=f(-x)$$ 

## Punktsymmetrie
Die Funktion ist symmetrisch in einem Punkt $P(x_0|y_0)$ wenn folgende Bedingung stets erfüllt ist:
$$
f(x_0-h)-y_0=y_0-f(x_0+h)
$$

# Gebrochenrationale Funktionen
Die gebrochenrationale Funktion $f(x)$ lässt sich als Quotient einer Zählerfunktion $Z(x)$ und einer Nennerfunktion $N(x)$ definieren.
1. Ungerade Hochzahlen
   Alle Hyperbeln verlaufen durch $(1|1)$ und $(-1|-1)$ und befinden sich im $3.$ und $1.$ Quadranten.
2. Gerade Hochzahlen
   Laufen alle durch $(1|1)$ und $(-1|1)$ 
Definiert über $\mathbb{R}$ mit Ausnahme aller Nullstellen der Nennerfunktion

## Verhalten um Definitionslücken
1. $f(x)=\dfrac{1}{x+2}$ Polstelle bei $x=-2$ mit VZW
2. $f(x)=\dfrac{1}{(x+2)^2}$ Polstelle bei $x=-2$ ohne VZW
3. $f(x)=\dfrac{x^2-1}{x-1}$ $D=\mathbb{R} \setminus \{ 1 \}$ 

### Hebbare Definitionslücken
In Beispiel 3. mit $f(x)=\dfrac{x^2-1}{x-1}$ ist $x=1$ eine hebbare Definitionslücke. Da der Zähler aus dem Term rausgekürzt werden kann, ohne den Rest der Funktion zu beeinflussen.
Wenn man dies tut erhält man $F(x)=x+1$
Diese neue Funktion ist die [stetige](#Stetig) Fortsetzung von $f(x)$ da die Definitionslücke nicht mehr existiert und die Funktionen sonst identisch sind.
$x_0$ ist genau dann eine hebbare Lücke, wenn $Z(x_0)=N(x_0)=0$ gilt.
Falls sich die Vielfachheit der Nullstelle in $Z$ und $N$ unterscheidet, ist sie nicht hebbar.

## Verhalten um Unendlich $\infty$ 
Wenn der Funktionswert einer Zahl $g$ entgegenstrebt, so heißt die Funktion konvergent.
Gibt es keinen Grenzwert, so spricht man von Divergenz.

Betrachtet wird $f(x)=\dfrac{Z(x_0)}{N(x_0)}$ Wobei $Z$ und $N$ Polynome vom Grad $n$ bzw. $m$ sind.
Ansatz über Ausklammern der höchsten Potenz
1. Nenner Potenz ist größer
   Grenzwert $y=0$
2. Potenzen gleich groß
   Horizontale Asymptote bei $y=\dfrac{k_{n-max}}{k_{m-max}}$ dem Quotient der Koeffizienten der größten Potenz.
3. Zähler Potenz größer
   Verhalten grob wie $f(x)=a*x^{n-m}$ 
   Schiefe Asymptote
   Näherungsfunktion lässt sich durch Polynomdivision berechnen.

### Beispiel zu 3.
$$
f(x) = \frac{x^2+1.5x}{2x-1}
$$

![LongDivision | 600](LongDivision.png)
Man rechnet bis zum Schluss, ein eventueller Rest wird wie in der Klammer gezeigt geschrieben. Durch Grenzwertsätze lässt sich erkennen dass der Einfluss auf den Graph minimal ist und für $x=\pm\infty$ vernachlässigt werden kann.

Der Ganzrationale Teil des Ergebnisses ist also der Term der Näherungsfunktion.

# Betragsfunktion
Eine Funktion heißt Betragsfunktion wenn in beliebiger Weise ein $x$ zwischen Betragsstrichen vorkommt.
1. $f(x)=|x|$ mit $D=\Bbb{R}$ und $W=\Bbb{R}^+$ 
2. $g(x)=|x-2|+3=\left\{ \begin{array}{rll} x^2-4 & \text{ bei } & x \geq 2 \\ -x+5 & \text{ bei } & x < 2 \end{array} \right.$ 
3. $h(x)=|x^2-4|=\left\{ \begin{array}{rll} x^2-4 & \text{ bei } & x<-2 \cup 2<x \\ -x^2+4 & \text{ bei } & -2 \leq x \leq 2 \end{array} \right.$ 

# Umkehrfunktion
$f(x)=\dfrac{1}{2}x + 2$ Stellt die Kosten pro Stückzahl dar, die Umkehrung ist diejenige Zuordnung, die aus der Stückzahl jeweils die entsprechenden Kosten liefert.
Hier wäre es $U(x)$ mit $U(x)=2x-4$
Die Umkehrfunktion entspricht einer Spiegelung an der ersten Winkelhalbierenden (Graph von $y=x$) 
Rechnerisch erhält man sie durch Auflösen nach $x$, zur Einheitlichkeit wird dann jedoch $x$ und $y$ vertauscht um die Umkehrfunktion $U(x)$ zu bekommen.
Eine Funktion $f$ heißt dann umkehrbar, wenn ihre Umkehrung eine gültige Funktion ist. Es können also nur Funktionen umkehrbar sein, bei denen jeder Funktionswert einmalig ist.

## Beispiel
$$
\begin{array}{l}
f(x) = 2(x-1)^2 + 3 & D_f = [1;\infty) \qquad W_f = [3;\infty) \\\\
x = 2\left( \overline{f}(x) - 1 \right)^2 + 3 \\\\
\dots \\\\
\overline{f}(x) = \sqrt{\frac{x-3}{2}}+1 & D_{\overline{f}} = W_f \qquad W_{\overline{f}} = D_f
\end{array}
$$
Eventuell müssen Definitions- und Wertemenge in Ausnahmefällen weiter eingeschränkt werden.

# Trigonometrische Funktionen
![](UnitCircle.png)
## Sin und Cos
Der Graph ist periodisch mit einer Periodenlänge von $P=2\pi$ 
$$
D = \Bbb{R} \qquad W = [-1;1]
$$
Nullstellen bei $k*\pi$ für Sinus und $\dfrac{\pi}{2} + k*\pi$ für Cosinus

## Tangens
Periodisch mit Periodenlänge von $P=\pi$
Punktsymmetrisch zu $(0|0)$ und jeder anderen Nullstelle

## Wichtige Werte

| $\alpha$ | $0 \textdegree$ | $30 \textdegree$    | $45 \textdegree$  | $60 \textdegree$ | $90 \textdegree$ |
| -------- | --------------- | ------------------- | ----------------- | ---------------- | ---------------- |
| Sin      | $0$             | $0.5$               | $\dfrac12\sqrt2$  | $\dfrac12\sqrt3$ | $1$              |
| Cos      | $1$             | $\dfrac12 \sqrt3$   | $\dfrac12 \sqrt2$ | $0.5$            | $0$              |
| Tan      | $0$             | $\dfrac{1}{\sqrt3}$ | $1$               | $\sqrt3$         | $\bot$           |

## Arkusfunktionen
Sind die Umkehrfunktionen von Sin, Cos und Tan. 
$\text{Sin}^{-1}(x)$ im TR. Sie geben zu jedem Wert $A$ zwischen $-1$ und $1$ den kleinstmöglichen Winkel $\alpha$ sodass $sin(\alpha)=A$ 
Die Funktionen heißen jeweils Arkus-(Trig-funktion), also Arkussinus / Arkuscosinus / Arkustangens

## Veränderte Sinusfunktionen
Die Sinuskurve lässt sich in parametrisierter Form schreiben
$$
a * sin(b(x-c)) + d
$$
Dabei haben die Parameter die folgenden Effekte auf das Schaubild:
$$
\begin{array}{lcl}
a & = & \text{Streckfaktor Amplitude} \\
b & = & \text{Streckfaktor Periode} \\
c & = & \text{Verschiebung X-Richtung} \\
d & = & \text{Verschiebung Y-Richtung}
\end{array}
$$

# Exponentialfunktionen
$$
\begin{array}{l}
f(x) = c * b^x \qquad
D = \Bbb{R} \qquad
W = \Bbb{R}^+ \\\\
b>1 \rightarrow \text{Wachstum} \\
b<1 \rightarrow \text{Zerfall} \\
\end{array}
$$
$b^x$ und $\left( \dfrac1b \right)^x$ sind an der $y$-Achse zueinander symmetrisch
Jede Exponentialfunktion kann mit der Basis $e$ geschrieben werden.
Da $$b=e^{\ln{(b)}}$$ gilt ist $$b^x = e^{\ln{(b)}^x}$$
also
$$
e^{x*\ln{(b)}}
$$ 
Dabei sind $e$ und $\ln{(b)}$ Konstanten

# Logarithmusfunktionen
Sind Asymptotisch zur $y$-Achse
Ähnlich wie die Exponentialfunktion lässt sich auch jeder Logarithmus durch $\ln$ ausdrücken.
$$
\log_{b}{(a)} = \dfrac{\ln{(a)}}{\ln{(b)}}
$$
$\log_{b}{(x)}$ ist an der $x$-Achse symmetrisch zu $\log_{\frac{1}{b}}{(x)}$ 