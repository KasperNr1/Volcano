Zahlen können beliebig in verschiedenen Zahlensystemen dargestellt werden. Zur Umrechnung gibt es einen speziellen [Algorithmus](Umrechnung%20von%20Zahlensystemen.md)

# Integers
## Positive Ganzzahlen
Im Binärsystem werden die positiven Ganzzahlen simpel dargestellt. Jede Ziffer einer Binärzahl hat den Wert $0$ oder $1$.
Jede Stelle stellt eine andere Zweierpotenz dar, die Ziffer an dieser Stelle beschreibt jeweils wie oft diese Potenz addiert werden muss um die codierte Zahl zu berechnen.

Die Zahl $11_{10}$ wird in Binär dargestellt als $1011_2$

| $2^3 = 8$ | $2^2 = 4$ | $2^1 = 2$ | $2^0 = 1$ |
| --------- | --------- | --------- | --------- |
| 1         | 0         | 1         | 1         |
Da 
$$
11 = 1 * 2^3 + 0*2^2 + 1 * 2^1 + 1 * 2^0
$$

Nach dem selben Prinzip lässt sich jede beliebige Zahl als Basis eines Zahlensystems verwenden.


## Negative Zahlen
Binärzahlen sollen so codiert werden, dass kein zusätzliches Vorzeichen notwendig ist um negative Zahlen zu unterscheiden.
Es werden 3 intuitive Varianten verglichen um den heute geläufigen Standard herzuleiten.


| $D$ | $C$ | $B$ | $A$ | $Y_1$ | $Y_2$ | $Y_3$ |
| --- | --- | --- | --- | ----- | ----- | ----- |
| 0   | 0   | 0   | 0   | 0     | 0     | 0     |
| 0   | 0   | 0   | 1   | 1     | 1     | 1     |
| 0   | 0   | 1   | 0   | 2     | 2     | 2     |
| 0   | 0   | 1   | 1   | 3     | 3     | 3     |
| 0   | 1   | 0   | 0   | 4     | 4     | 4     |
| 0   | 1   | 0   | 1   | 5     | 5     | 5     |
| 0   | 1   | 1   | 0   | 6     | 6     | 6     |
| 0   | 1   | 1   | 1   | 7     | 7     | 7     |
| 1   | 0   | 0   | 0   | -0    | -7    | -8    |
| 1   | 0   | 0   | 1   | -1    | -6    | -7    |
| 1   | 0   | 1   | 0   | -2    | -5    | -6    |
| 1   | 0   | 1   | 1   | -3    | -4    | -5    |
| 1   | 1   | 0   | 0   | -4    | -3    | -4    |
| 1   | 1   | 0   | 1   | -5    | -2    | -3    |
| 1   | 1   | 1   | 0   | -6    | -1    | -2    |
| 1   | 1   | 1   | 1   | -7    | -0    | -1    |
| $D$ | $C$ | $B$ | $A$ | $Y_1$ | $Y_2$ | $Y_3$ |
Alle Codierungen verwenden das MSB als Vorzeichenbit. Dabei gilt $0=+$ und $1=-$ 

$Y_1$ Verwendet für alle Zahlen die selbe Codierung, so entsteht eine zweite $0$ und Schwierigkeiten bei Berechnungen mit den negativen Zahlen. Möchte man beispielsweise $1+(-2)$ berechnen erhält man folgende Lösung
$$
\begin{array}{rr}
1 & 0001 \\
-2 & 1010 \\
\\
& 0001 \\
+ & 1010 \\
\hline 
-3 & 1011
\end{array}
$$


$Y_2$ Ordnet die negativen Werte dem binären [1er-Komplement](DigitaltechnischeBegriffe.md#1er-Komplement) zu. 
So sind die Ergebnisse der Berechnungen nicht völlig falsch, jedoch bleiben sie um exakt 1 verschoben und belegen weiterhin eine Kombination mit $-0$.

$Y_3$ Löst beide dieser Probleme in dem die Idee beibehalten wird, aber die negativen Zahlen jeweils um $1$ vermindert werden. So wird gleichzeitig die Rechenverschiebung und die überflüssige $0$ verhindert.

Mit dieser Codierung kann eine $n$-stellige Binärzahlen Werte zwischen $\dfrac{2^n-1}{2}$ und $-\dfrac{2^n}{2}$ darstellen. MSB bleibt dabei das Vorzeichenbit mit $0=+$ 


# Floats
Kompromiss zwischen Größe des Exponenten (Range) und der Mantisse (Präzision). Over- und Underflow sind problematisch. (Exponent hat auch Vorzeichen)

## IEEE 754
Bei IEEE 754 wird zur besseren Sortierbarkeit der Exponent nicht im 2K dargestellt,  es wird um +127 verschoben (1023 bei 64 Bit)  
$$
Z_D=(-1)^S \cdot (1+\text{Mantisse}) \cdot 2^{\text{Exponent} - \text{Verschiebekonstante}}
$$

### Umrechnung
Es soll die Zahl $19.3$ dargestellt werden.
Dazu werden Vor- und Nachkommateil zuerst separat in Binär geschrieben.

#### Vorkommastelle
Die Zahl wird immer durch $2$ geteilt und der Rest notiert. Bis schließlich die letzte Zeile ein Ergebnis von $0 \; R0$  oder $0 \;R1$ liefert. Die Reste sind in umgekehrter Reihenfolge die signifikanten Ziffern der Binärzahl.

$$
\begin{array}{r c l}
\text{Division} & \text{Ergebnis} & \text{Rest} \\
19 / 2 & 9 & 1 \\
9 / 2 & 4 & 1 \\
4 / 2 & 2 & 0 \\
2 / 2 & 1 & 0 \\
1 / 2 & 0 & 1 \\
\end{array}
$$
$$
19_{10} = 10011_{2}
$$
#### Nachkommastelle
Der Nachkommateil wird ähnlich konvertiert. In jedem Schritt wird der Nachkommateil verdoppelt und notiert ob das Ergebnis $1$ oder mehr ist. Die Bits werden sortiert nach Signifikanz berechnet.

$$
\begin{array}{r c l}
\text{Berechnung} & \text{Ergebnis} & \text{Bit} \\
0.3 * 2 & 0.6 & 0 \\
0.6 * 2 & 1.2 & 1 \\
0.2 * 2 & 0.4 & 0 \\
0.4 * 2 & 0.8 & 0 \\
0.8 * 2 & 1.6 & 1 \\
0.6 * 2 & 1.2 & 1 \\
\vdots
\end{array}
$$

$$
0.3_{10} = 0.0\overline{1001}_{2}
$$

$0.3$ lässt sich in Binärschreibweise nicht periodisch darstellen. Die Berechnung des Nachkommaanteils wird fortgesetzt bis man 0 erhält, oder eine periodische Folge erkennt.

#### Normierung
Vor- und Nachkommateil werden zusammengefasst

$$
19.3_{10} = 10011.0\overline{1001}_{2}
$$

Diese Zahl wird nun normiert. Das Komma wird verschoben um das Format $1.xxx$ zu erhalten.

$$
10011.0\overline{1001} * 2^0 = 1.00110\overline{1001} * 2^4
$$
Durch Multiplikation mit einer entsprechend großen Zweierpotenz wird der Zahlenwert des Ausdrucks erhalten.

#### Darstellung
Der Exponent $4$ wird mit der Verschiebekonstanten $127$ zusammen zu $131$, was in Binär der Zahl $10000011$ entspricht.
Das Vorzeichen ist positiv, dementsprechend wird das Vorzeichenbit auf $0$ gesetzt.
Durch die Verwendung der normierten Einstellung enthält die stets führende $1$ der Zahl keine notwendige Information und kann entfallen um Platz für eine weiter Nachkommastelle zu bieten.

Die Zahl ist vollständig nach IEEE754 umgewandelt also:
$$
\underbrace{0}_{1 \text{Bit}} \underbrace{10000011}_{8 \text{Bit}} \underbrace{00110100110011001100110}_{23 \text{Bit}}
$$

### Ausnahmen
Einige Kombinationen sind für besondere Werte reserviert.

![](FloatSpecialValues.png)

