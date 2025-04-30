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
Auf der Hauptdiagonalen $y=x$ hat die Funktion den Wert








