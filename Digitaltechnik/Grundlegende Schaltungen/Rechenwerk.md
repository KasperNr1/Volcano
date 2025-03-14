# Negative Zahlen im Binärsystem
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

# Halbaddierer
Diese Schaltung soll zwei Bits $A$ und $B$ addieren können. Ausgegeben werden ihre Summe $\Sigma$ und ihr Übertrag $C$.


| $B_0$ | $A_0$ | $\Sigma$ | $C_1$ |
| ----- | ----- | -------- | ----- |
| 0     | 0     | 0        | 0     |
| 0     | 1     | 1        | 0     |
| 1     | 0     | 1        | 0     |
| 1     | 1     | 0        | 1     |
$$
\begin{array}{ll}
\Sigma &= A \; XOR \; B \\
C &= A \wedge B
\end{array}
$$

# Volladdierer
Funktioniert wie ein [Halbaddierer](#Halbaddierer) der zusätzlich einen Übertrag der vorherigen Stelle auswerten kann.

| $C_n$ | $B_n$ | $A_n$ | $\Sigma_n$ | $C_{n+1}$ |
| ----- | ----- | ----- | ---------- | --------- |
| 0     | 0     | 0     | 0          | 0         |
| 0     | 0     | 1     | 1          | 0         |
| 0     | 1     | 0     | 1          | 0         |
| 0     | 1     | 1     | 0          | 1         |
| 1     | 0     | 0     | 1          | 0         |
| 1     | 0     | 1     | 0          | 1         |
| 1     | 1     | 0     | 0          | 1         |
| 1     | 1     | 1     | 1          | 1         |
$$
\begin{array}{ll}
\Sigma_n &= A\overline{B} \,\overline{C} \vee \overline{A}B\overline{C} \vee \overline{A} \, \overline{B} C \vee ABC \\
C_{n+1} &= A \wedge (B \vee C) \vee BC \\
\end{array}
$$
$C$ ist hier exakt die [2 aus 3 Schaltung](Boolsche%20Algebra.md#2%20aus%203%20Schaltung).

# Subtraktion
Zur Subtraktion kann analog eine eigene Schaltung entwickelt werden, jedoch ist es wünschenswert beide Funktionalitäten in einem Rechenwerk zu vereinen.
Bei Binärzahlen ist kann das Ergebnis einer Subtraktion auch durch Addition erreicht werden.
Hierfür wird vom Subtrahend das [2er Komplement](DigitaltechnischeBegriffe.md#2er%20Komplement) gebildet. Unter Weglassen eines eventuellen Übertrags wird der ursprüngliche Minuend und das neu gebildete Komplement addiert.

![](fullAdder.png)

Die gezeigte Schaltung ist in der Lage zwei Zahlen einzulesen und diese zu addieren oder subtrahieren, abhängig vom Signal $\pm$. Wird dieses mit $1$ belegt entsteht durch die XOR Gatter an jedem Bit von $B$ das [1er-Komplement](DigitaltechnischeBegriffe.md#1er-Komplement). Um daraus das 2er-Komplement zu bilden muss zu Zahl $1$ addiert werden. Dies wird erreicht indem das Signal zusätzlich in den Übertrag des ersten Volladdierers geleitet wird.
Eine Belegung mit $0$ hat keinen Effekt auf Signal $B$ und liefert einen ursprünglichen Übertrag von $0$, was bei einer normalen Addition erwünscht ist.

### Beispielrechnung
$3-5$ soll im Binärsystem durch Komplementbildung berechnet werden.

$$
\begin{array}{lrl}
3 & 0011 \\
5 & 0101 \\
\\
& 1010 & \text{1K von 5} \\
+ & 1 \\
\hline 
5 & 1011 & \text{2K von 5} \\
\\
& 0011 & 3 \\
+ & 1011 & \text{2K von 5} \\
\hline
& 1110
\end{array}
$$

Von diesem Ergebnis muss nun ebenfalls das 2er Komplement gebildet werden. Das Vorzeichen-Bit wird jedoch beibehalten.
$$
\begin{array}{lll}
1 & 110 \\
\downarrow \\
1 & 010 & =-2
\end{array}
$$
