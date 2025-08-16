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
