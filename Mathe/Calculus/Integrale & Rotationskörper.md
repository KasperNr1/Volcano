Integrale sind das Gegenstück zur [Ableitung](Differentialrechnung.md#Ableitung). Statt der Steigung der [Funktionen](Funktionen.md)beschreiben sie die Fläche unter den Funktionsgraphen. 

# Stammfunktion
$F(x)$ sei eine Funktion mit der Ableitung $F'(x)$.
Sei weiterhin $f(x)$ eine Funktion mit $f(x) = F'(x)$.
$F(x)$ ist eine Stammfunktion von $f(x)$.
Im Allgemeinen besitzt jede differenzierbare Funktion mehrere Stammfunktionen, die sich mindestens um einen konstanten Summanden unterscheiden.

# Hauptsatz der Differential und Integralrechnung
$$
\int_a^bf(x)\,dx = \left[ F(x) \right]^b_a = F(b)-F(a)
$$
Vertauschen der Integralgrenzen führt zur Änderung des Vorzeichens des Ergebnisses 

# Fläche zwischen zwei Graphen
Das Integral stellt den orientierten Flächeninhalt dar. Das heißt, Flächen die teilweise über und unterhalb der Achse liegen werden von einander abgezogen. Wenn man die gesamte Fläche berechnen möchte, muss man sie eventuell in mehrere Teilflächen aufteilen und diese einzeln berechnen, bevor sie anschließend summiert werden.
![|200](IntegralZwischenFunktionen.png)
Für die Fläche zwischen zwei Graphen werden die Schnittpunkte der Graphen statt der Nullstellen als Intervallgrenzen genommen. 
Für Funktionen die im zu integrierenden Intervall keine Schnittpunkte besitzen berechnet sich das Integral wie folgt.
$$
A = \left| \int_a^bf(x)-g(x) \, dx \right|
$$
Gegebenenfalls muss das Integral zur Berechnung wie beschrieben in kleinere Intervalle aufgeteilt werden.

# Rotationskörper
Gegeben ist eine auf $[a;b]$ stetige Funktion $f(x)$ 
Das Schaubild zeigt $f$ im [Intervall](Intervalle%20und%20Mengen.md) $[a;b]$ und den Rotationskörper der durch Drehung an der $x$-Achse entsteht.
![|200](Rotationskörper01.png)
Auch die Fläche zwischen Graphen kann in einem Rotationskörper als Grundintegral dienen.
## Berechnung des Volumens
Ähnlich den Rechtecken die bei einem Integral aufsummiert werden, lassen sich bei einem Rotationskörper Zylinder finden, deren Gesamtvolumen dem des Körpers entspricht.
Es gilt also:
$$
V = \pi * \int_a^b \left[ f(x) \right]^2 \, dx
$$
### Beispiel
$$
\begin{array}{l}
f(x) = \dfrac{1}{2}\sqrt{x^2+4} \\
a = 0 \\
b = 4 \\\\
V = \pi \displaystyle\int_0^4{\left[ \dfrac{1}{2} \sqrt{x^2+4} \right]^2 \, dx} \\\\
= \pi \displaystyle\int_0^4 \left( \dfrac{1}{4}(x^2+4) \right) \, dx \\\\
= \pi \left[ \dfrac{1}{12}x^3 + x \right]^4_0 \\\\
= \pi \left( \dfrac{64}{12} + 4 - (0+0) \right) \\\\
= \dfrac{28}{3} \pi \approx 29.32
\end{array}
$$
## Rotation um die $y$-Achse
![|350](Rotationskörper02.png)
Das Volumen des Körpers wird durch verschieben, spiegeln und drehen nicht beeinflusst.
Daher ist das Volumen des Körpers der durch Rotation um die $y$-Achse entsteht gleich, wie das des Rotationskörpers der [Umkehrfunktion](Funktionen.md#Umkehrfunktion) um die $x$-Achse.

# Bogenlänge
Beschreibt die Länge des Funktionsgraphen in einem bestimmten Intervall $[a;b]$.

## Überlegung
$dx$ und $dy$ bilden ein Rechtwinkliges Dreieck, das einen Teil der Bogenlänge als Hypotenuse hat.
$$
s^2 = (\Delta x)^2(\Delta y)^2
$$
Auflösen nach $s$ ergibt:
$$
s = \sqrt{(\Delta x)^2(\Delta y)^2} = \sqrt{(\Delta x)^2*\left( 1+\dfrac{\Delta y^2}{\Delta x^2} \right)} = \Delta x*\sqrt{1+\dfrac{\Delta y^2}{\Delta x^2}}
$$
Die Annäherung wird besser wenn $\Delta x$ kleiner wird, $\Delta x$ geht also gegen $0$.
Das Sehnenstück $s$ wird damit zum Differential $ds$ 
$$
ds = \sqrt{1+\left(\frac{\Delta y}{\Delta x}\right)^2} * \Delta x = \sqrt{1+f'(x)^2} * \Delta x
$$
Die Summe all dieser beliebig kurzen Sehnenstücke $ds$ ist die gesamte Bogenlänge $l$.
$$
l = \int_a^b \sqrt{1+f'(x)^2} \, dx
$$