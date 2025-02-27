# Begriffe
Eine Funktion ist eine Zuordnung aller Zahlen aus der Definitionsmenge $D$ zu genau einer Zahl aus der Wertemenge $W$.
Def- und Wertemenge lassen sich als [Intervalle](Intervalle%20und%20Mengen.md) schreiben, wie $D_f=[0; \infty)$ 

# Grenzwert
Der Grenzwert einer Zahl ist die Zahl, der die Funktionswerte beliebig nahe kommen, wenn $x$ sich in eine gewisse Richtung verändert.

## Schreibweise
$$
\lim_{n \to \infty}(f(x))=g $$$$
$ \lim_{n \to 0}(2n+1)=1
$$
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
1. $f(x)=\frac{1}{x+2}$ Polstelle bei $x=-2$ mit VZW
2. $f(x)=\frac{1}{(x+2)^2}$ Polstelle bei $x=-2$ ohne VZW
3. $f(x)=\frac{x^2-1}{x-1}$ $D=\mathbb{R} \setminus \{ 1 \}$ 

### Hebbare Definitionslücken
In Beispiel 3. mit $f(x)=\frac{x^2-1}{x-1}$ ist $x=1$ eine hebbare Definitionslücke. Da der Zähler aus dem Term rausgekürzt werden kann, ohne den Rest der Funktion zu beeinflussen.
Wenn man dies tut erhält man $F(x)=x+1$
Diese neue Funktion ist die stetige Fortsetzung von $f(x)$ da die Definitionslücke nicht mehr existiert und die Funktionen sonst identisch sind.
$x_0$ ist genau dann eine hebbare Lücke, wenn $Z(x_0)=N(x_0)=0$ gilt.
Falls sich die Vielfachheit der Nullstelle in $Z$ und $N$ unterscheidet, ist sie nicht hebbar.

## Verhalten um Unendlich $\infty$ 
Wenn der Funktionswert einer Zahl $g$ entgegenstrebt, so heißt die Funktion konvergent.
Gibt es keinen Grenzwert, so spricht man von Divergenz.

Betrachtet wird $f(x)=\frac{Z(x_0)}{N(x_0)}$ Wobei $Z$ und $N$ Polynome vom Grad $n$ bzw. $m$ sind.
Ansatz über Ausklammern der höchsten Potenz
1. Nenner Potenz ist größer
   Grenzwert $y=0$
2. Potenzen gleich groß
   Horizontale Asymptote bei $y=\frac{k_{n-max}}{k_{m-max}}$ dem Quotient der Koeffizienten der größten Potenz.
3. Zähler Potenz größer
   Verhalten grob wie $f(x)=a*x^{n-m}$ 
   Schiefe Asymptote
   Näherungsfunktion lässt sich durch Polynomdivision berechnen.