# Definition
Rechteckige Zahlenschemen mit $m$ Zeilen und $n$ Spalten heißen $(m \times n)$-Matrix.
Eine Matrix $A$ ist formell definiert als linearer Operator der einem $n$-Tupel $x$ das $m$-Tupel $y$ zuordnet. $A$ angewendet auf $x$ ergibt $y$.
$$
\begin{pmatrix}
y_1 \\
y_2
\end{pmatrix}
=
\begin{pmatrix}
5 & 2 & 1 \\
1 & 0 & -6
\end{pmatrix}
*
\begin{pmatrix}
x_1 \\
x_2 \\
x_3
\end{pmatrix}

$$
Wenn $x=\begin{pmatrix}1 \\1 \\1\end{pmatrix}$ wird durch Anwenden von $A$ der Vektor $y=\begin{pmatrix}8 \\-5 \end{pmatrix}$ generiert. Anwenden bedeutet, die Koordinaten des [Vektors](Vektoren%20und%20Vektorräume.md) in das durch $A$ beschriebene LGS einzusetzen.

Für eine allgemeine Matrix gilt:
$$
A = (a_{ik}) = 
\begin{pmatrix}
a_{11} & \cdots & a_{1n} \\
\vdots & \ddots & \vdots \\
a_{m1} & \cdots & a_{mn}
\end{pmatrix}
$$
Wobei $a_{ik} \in \mathbb{K}$ Elemente der Matrix sind; $i$ der Zeilenindex und $k$ der Spaltenindex ist.

# Bezeichnungen
- Diagonalmatrizen: alle Elemente die nicht auf der Hauptdiagonalen sind, sind zwingend $=0$ 
$$
\begin{pmatrix}
-1 & 0 & 0 \\
0 & 2 & 0 \\
0 & 0 & 8
\end{pmatrix}
$$
- Einheitsmatrix: Alle Elemente sind $=0$, außerdem sind alle Elemente der Hauptdiagonalen $=1$ 
$$
\begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{pmatrix}
$$
- Skalarmatrix: Einheitsmatrix die mit einem Faktor $c$ skaliert wurde
$$
\begin{pmatrix}
c & 0 & 0 \\
0 & c & 0 \\
0 & 0 & c
\end{pmatrix}
$$

# Rechenregeln für Matrizen
- **Gleichheit**: Zwei Matrizen sind genau dann gleich, wenn sie die exakt selbe Größe haben und in jedem Element übereinstimmen.
- **Skalare Multiplikation**: $p * A$ Jedes Element der Matrix wird mit dem Faktor $p$ multipliziert
- **Addition**: Die Größen müssen übereinstimmen, Elemente mit gleichen Indexen werden einzeln addiert.

## Multiplikation
Das Produkt zweier Matrizen $A: (m \times n)$ und $B: (n \times m)$ ist eine Matrix $C: (m \times m)$ 
Dabei gilt das Kommutativgesetz nicht. Meistens ist also $A\times B \neq B\times A$ 

Jedes Element der Resultatmatrix ist das Skalarprodukt einer Zeile aus $A$ und einer Spalte aus $B$. Dabei ist $c_{13}$ das Produkt der 1 Zeile von $A$ mit der ersten Spalte aus $B$.
![](MatrixMultiplikation.png)
### Eigenschaften der Matrixmultiplikation
Das Kommutativgesetz gilt nicht, dafür aber einige andere Regeln:
- $(p * A) * B = A * (p * B)$ 
- $(A*B)*C = A * (B * C) = A * B * C$ 
- $A * (B + C) = A * B + A * C$
- $(A + B) * C = A * C + B * C$
- Die Nullmatrix kann das Ergebnis einer Multiplikation von zwei Matrizen sein, die nicht selbst die Nullmatrix sind

## Transponieren einer Matrix
Die transponierte Matrix $A^T$ entsteht aus $A$ indem Zeilen und Spalten vertauscht werden, bzw. an der Hauptdiagonales gespiegelt wird. Wenn $A: (n \times m)$ groß ist, so hat $A^T: (m \times n)$ 

Es gilt:
- $(A+B)^T = A^T + B^T$ 
- $(A^T)^T = A$  
- $(A * B)^T = B^T * A^T$
- **NICHT** $(A*B)^T=A^T*B^T$ 

## Spezielle Matrizen
Eine Quadratische Matrix heißt "symmetrisch", falls $A=A^T$, also $a_{ik}=a_{ki}$ für alle $k,i$ 
Sie ist "schiefsymmetrisch" wenn $B^T=-B$. Somit muss die Hauptdiagonale mit $0$ belegt sein, da keine andere Zahl ihr eigenes additives Invers ist.
$$
A=
\begin{pmatrix}
-2 & 1 & 4 \\
1 & 12 & 0 \\
4 & 0 & -3
\end{pmatrix}
\quad
B=
\begin{pmatrix}
0 & -2 & 1 \\
2 & 0 & 8 \\
-1 & -8 & 0
\end{pmatrix}
$$

Eine quadratische Matrix die $\frac{\text{oberhalb}}{\text{unterhalb}}$ der Hauptdiagonalen nur Nullen enthält, heißt eine $\frac{\text{obere}}{\text{untere}}$ Dreiecksmatrix.
$$
\begin{pmatrix}
2 & 0 & 0 \\
1 & 1 & 0 \\
-6 & 3 & 10
\end{pmatrix}
$$
Eine Matrix die nur in der Nähe der Hauptdiagonalen Werte ungleich $0$ enthält, heißt Bandmatrix.
$$
\begin{pmatrix}
1 & 2 & 0 & 0 & 0 \\
-3 & 5 & 8 & 0 & 0\\
0 & 6 & 7 & 1 & 0 \\
0 & 0 & 4 & 13 & 2\\
0 & 0 & 0 & 1 & -1\\
\end{pmatrix}
$$
