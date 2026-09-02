[Funktionen](Funktionen.md) können von mehreren Variablen abhängig sein. Beispielsweise die Elektrische Spannung oder die Parabel eines Wurfs sind Ergebnis von 2 Veränderlichen
$$
U(R;I) = R*I \qquad W(v_0,\theta)=\frac{{v_0}^2 \cdot \sin(2\theta)}{g}
$$
Die Oberfläche einer Halbkugel ist durch die Folgende Funktion beschrieben
$$z = \sqrt{R^2-x^2-y^2} \qquad z\geq0 \quad R=\text{konst.}>0$$
Der Graph dieser Funktion ist dreidimensional.

# Höhenlinien
Um den Verlauf einer solchen Funktion besser erkennbar zu machen werden Höhenlinien eingezeichnet. Bei alle Punkte mit einem bestimmten Funktionswert werden zu einer Höhenlinie zusammengefasst. 
Die Funktion $f(x,y)=x^2+y^2$ ist eine um die $z-$Achse rotierte Parabel. 
![](Höhenlinien.png)
Die Punkte mit einer Höhe von 1 oder 4 liegen Kreisförmig um den Ursprung. So kann der Verlauf der Fläche des Graphen besser gezeigt werden.

# Grenzwerte
Auch Funktionen von mehreren Variablen können [Grenzwerte](Grenzwerte%20von%20Folgen.md) besitzen. Diese müssen bekanntlich immer von allen Richtungen erreicht werden. Für Funktionen von mehreren Veränderlichen muss dieses Richtungskonzept erweitert werden.
Der Grenzwert wird entlang einer Gerade $y = mx$ bestimmt um nur von einer Variablen abhängig zu sein. Der Faktor $m$ ist dabei jede beliebige Zahl $\neq 0$ 

Beispiel:
Existiert in $f(x,y)=\frac{x^2-y^2}{x^2+y^2}$ ein Grenzwert bei $f(0,0)$?
$$
f(x,mx) = \frac{x^2-m^2x^2}{x^2+m^2x^2} = \frac{1-m^2}{1+m^2}
$$
Dieser Term ist unabhängig von $x$ 
$$
\lim_{x \to 0}\frac{1-m^2}{1+m^2} = \frac{1-m^2}{1+m^2}
$$
Der Wert wird von der Annäherungsrichtung $m$ beeinflusst. Somit existiert kein eindeutiger Grenzwert.

# Stetigkeit
Auch die [Stetigkeit](Funktionen.md#Stetig) einer Funktion wird mit steigender Anzahl an Eingabewerten komplexer. 

Beispiel
$$
f(x,y) = \left\{\begin{array}{cl} \dfrac{4xy}{x^2+y^2} & (x,y) \neq (0,0) \\ 0 & (x,y) = (0,0) \end{array} \right.
$$

Entlang der $x$-Achse $y=0$ 
für $x\neq 0$ ist $f(x,0) = \dfrac{0}{x^2} = 0$
Auf der Hauptdiagonalen $y=x$ (mit $y=x\neq0$ ) hat die Funktion den Wert $2$
Somit ist auch dieser Wert Abhängig von der Annäherungsrichtung und die Funktion als ganzes nicht stetig.

# Partielles Differenzieren
![](PartielleAbleitung.png)

Die [Ableitung](Differentialrechnung.md#Ableitung) bestimmt die Steigung einer Funktion in einem Punkt. 
Am Schaubild wird ersichtlich, dass die Steigung einer Mehrdimensionalen Funktion ebenfalls von der Richtung der Betrachtung abhängt. Man bestimmt sog. partielle Ableitungen für jeden Eingabeparameter.
Dabei wird ein Parameter als variabel angesehen, während alle anderen als Konstanten behandelt werden. 

$$
f(x,y) = -4x^3 y^2 + 3xy^4 -3x + 2y + 5
$$
Die Partiellen Ableitungen nach $x$ und $y$ werden als $f_x$ und $f_y$ beschriftet.
$$
\begin{array}{cl}
f_x(x,y) &= -12x^2 y^2 +3y^4 -3 \\
f_y(x,y) &= -8x^3y +12xy^3 +2 \\
\end{array}
$$

## Satz von Schwarz

> [!Warning] TODO
> Diese Einträge sind noch nicht vollständig. Die originalen Aufschriebe sind in OneNote `DH_S3/Mathematik` 

Bei mehrmaligem Partiellen Ableiten nach verschiedenen Variablen ist die Reihenfolge nicht relevant.
$$
f_{xy}(x,y,z) = f_{yx}(x,y,z)
$$

## Implizite Ableitungen
$$
y\prime = -\frac{F_x}{F_y}
$$

Ellipse:
$$
\begin{array}{r l}
F(x,y) &= \dfrac{x^2}{9} + \dfrac{y^2}{4} - 1 = 0 \\
F(x,y) &= 4x^2 + 9y^2 -36 = 0\\
\\
F_x(x,y) &= 8x \\
F_y(x,y) &= 18y \\
\end{array}
$$

$$
y\prime = -\frac{8x}{18y} = -\frac{4x}{9y}
$$
## Extremstellen in Dreidimensionalen Funktionen
![](BedingungenExtremwerte.png)

# Extremwertaufgaben
![](ExtremwertBeispielaufgabe.png)

Maximiert werden soll
$$
W = \frac{1}{6}bh^2
$$
wobei aufgrund des Satz des Pythagoras folgende Nebenbedingung gilt:
$$
b^2 + h^2 = \left(2R\right)^2
$$

Es kann nach $h^2$ aufgelöst werden, einsetzen ergibt:
$$
W(b) = \frac16 b \cdot \left(\left(2R\right)^2 - b^2 \right) = \frac16 \cdot \left( 4R^2b - b^3 \right)
$$

[Partielles Differenzieren](#Partielles%20Differenzieren) liefert
$$
W^\prime(b) = \frac16 \left( 4R^2 - 3b^2 \right)
$$
$$
W^{\prime\prime} (b) = \frac16 \left(0-6b\right) = -b
$$

Mit den hinreichenden Bedingungen $W^\prime=0$ und $W^{\prime\prime} < 0$ kann eine Extremstelle gefunden werden

$$
W^\prime(b) = \frac16 \left( 4R^2 - 3b^2 \right) = 0
$$
$$
\Longrightarrow 4R^2 -3b^2 = 0 \Longrightarrow b^2 = \frac43 R^2
$$
$$
b_{1/2} = \pm \frac23 \sqrt3 R
$$
Da aus geometrischen Gründen $0< b <2R$ gelten muss, kommt nur der positive Wert in Frage.

# Integrale von mehreren Variablen


> [!Missing] TODO
> DH3 in OneNote


# Polarintegrale
![](Polarkoordinaten.png)
$$
    r = \sqrt{x^2+y^2}
$$

$$
    tan({\phi})=\frac{x}{y}
$$

Berechnung von $\phi$:


| Quadrant | I                               | II                                    | III & IV                              |
| -------- | ------------------------------- | ------------------------------------- | ------------------------------------- |
| $y$      | $\arctan \left(\frac xy\right)$ | $\arctan \left(\frac xy\right) + 180$ | $\arctan \left(\frac xy\right) + 360$ |


$$
    z=f(x,y)=f(r*cos(\phi), r*sin(\phi))
$$

## Integrationsbereich
![](Polarflächeninhalt.png)


> [!Note] Wiederholung
> Bogenlänge $b = \frac{\pi*r*\alpha}{180°} = r * \phi$ wobei $\alpha$ der Winkel im Gradmaß ist und $\phi$ der Winkel im Bogenmaß

$$
    dA = rd\phi dr = rdr d\phi
$$

## Doppelintegral in Polarkoordinaten
$$
    \int_{A}{\int f(x,y) dA} = \int^{\phi_2}_{\phi=\phi_1}\int^{r_a(\phi)}_{r=r[\phi]}f(r*cos(\phi), r*sin\phi)
$$

Bsp:

$$
\begin{align*}
    f(x,y) = xy \\
    \int_{(A)}{\int{xy} \, dA}
\end{align*}
$$
![](IntegralBeispiel.png)
Transformation des Integranden

$$
    f(x,y)=x*y=r^2*sin(\phi)*cos(\phi)
$$

Integrationsgrenzen
$r$-Integration von $r=0$ bis $r=2$
$\phi$ von $\phi = 0$ bis $\phi = \frac{\pi}{4}$

$$
    dA=r dr d\phi
$$

Doppelintegral in Polarkoordinaten

$$
\begin{align*}
        \int_{\phi=0}^{\frac{\pi}{4}}{\int_{0}^{2} r^3*r*cos(\phi)*sin(\phi) \, dr \, d\phi} &= sin(\phi)*cos(\phi)\left[\frac{1}{4}r^4\right]^{2}_{0} \\
        &= 4 * \int^{\frac{\pi}{4}}_{\phi=0}sin(\phi)*cos(\phi) \, d\phi \\
        &= ProduktRegel \\
        &= \left[sin(\phi)^2\right]^{\frac{\pi}{4}}_{0} = 1
\end{align*}
$$

Rotationskörper:
$z = 4-x^2$ (Halbkreis) mit Rotation um z-Achse
In Polarkoordinaten:

$$
    z=4-(r^2cos(\phi)^2+r^2sin(\phi)^2)=4-r^2
$$

Integrationsbereich $(A \mid \text{mit} \; 0\le r \le 2, \quad 0 \le \phi \le 2\pi)$

Rotationsvolumen

$$
\begin{align*}
    V &= \int_{A}{\int{z, dA}} \\
      &= \int_{0}^{2\pi} \int_{0}^{2} \left(4 - r^2\right) r \, dr \, d\phi \\
      &= \left[ \frac{4}{2}r^2 - \frac{1}{4}r^4 \right]_{0}^{2} \\
      &= 8\pi
\end{align*}
$$

Flächeninhalt $r(\phi)=1+cos(\phi), 0 \le \phi \le 2\pi$
Kardioide
![](Kardioide.jpg)

Integrationsgrenzen
$$
\begin{align*}
    r_{i}(\phi) &=0, \\
    r_{a}(\phi) &=1+cos(\phi) \\
    \phi &= 0, \\
    \phi &= 2 \pi \\
\end{align*}
$$
$$
\begin{align*}
    A &=\int^{2\pi}_{0}{\int^{1+cos(\phi)}_{0}{r}dr}d\phi \\ 
      &= \int^{2\pi}_{\phi=0}{\left(1+cos(\phi)\right)^2}d\phi \\
      &= \frac{1}{2}\left[\frac{3}{2}\phi+2sin(\phi)+\frac{1}{4}sin(2\phi)\right]^{2\pi}_{0} \\ 
      &= \frac{3}{2}\pi
\end{align*}
$$
