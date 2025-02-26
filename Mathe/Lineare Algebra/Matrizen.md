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
Wenn $x=\begin{pmatrix}1 \\1 \\1\end{pmatrix}$ wird durch Anwenden von $A$ der Vektor $y=\begin{pmatrix}8 \\-5 \end{pmatrix}$ generiert. Anwenden bedeutet, die Koordinaten des [Vektors](Vektoren%20und%20Vektorräume.md) in das durch $A$ beschriebene [LGS](Lineare%20Gleichungssysteme.md) einzusetzen.

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
# Invertierbare Matrizen
Motivation:
Bei Linearen Gleichungen gilt $a*x = b \rightarrow x = a^{-1} *b$
Auch bei Matrizen? $A*x=b \rightarrow x=A^{-1}*x$

## Inversion einer $(2\times2)$-Matrix mit der Cramer'schen Regel
$$
\begin{pmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22} 
\end{pmatrix}
*
\begin{pmatrix}
x_1 \\
x_2
\end{pmatrix}
=
\begin{pmatrix}
b_1 \\
b_2
\end{pmatrix}
$$
Wenn $det(A)\neq0$ ist, dann gilt laut [Cramer'scher Regel](Determinanten.md#Cramer'sche%20Regel%20für%20ein%20(2x2)-System):
$$
\begin{array}{l}
x_1 = \frac{D_1}{D} = \frac{1}{det(A)} * 
\begin{vmatrix}
b_1 & a_{12} \\
b_2 & a_{22}
\end{vmatrix}
=
\frac{1}{det(A)} * (a_{22}*b_1-a_{12}*b_2)
\\\\
x_2 = \frac{D_2}{D} = \frac{1}{det(A)} * 
\begin{vmatrix}
a_{11} & b_1 \\
a_{21} & b_2
\end{vmatrix}
=
\frac{1}{det(A)} * (-a_{21}*b_1 + a_{11}*b_2)
\end{array}
$$
Wobei $D=det(A)$ 

$$
\begin{pmatrix}
x_1 \\
x_2
\end{pmatrix}
=
\boxed{
\frac{1}{det(A)}
*
\begin{pmatrix}
a_{22} & -a_{12} \\
-a_{21} & -a_{11} 
\end{pmatrix}
}
*
\begin{pmatrix}
b_1 \\
b_2
\end{pmatrix}
$$
Bzw.
$$
x = \boxed{A^{-1}}*b
$$
## Inversion einer Regulären $(2\times2)$-Matrix
Jede zweireihige quadratische Matrix $A$ mit $det(A)\neq0$ besitzt eine inverse Matrix $A^{-1}$ 
Wenn $A = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix}$ 
Dann gilt $A^{-1} = \frac{1}{det(A)} * \begin{pmatrix} a_{22} & -a_{12} \\ -a_{21} & a_{11} \end{pmatrix}$ 

### Beispiel
$$
A*x=b \qquad 
A = \begin{pmatrix} 4 & 1 \\ 5 & 2 \end{pmatrix} \qquad
b = \begin{pmatrix} 5 \\ 1 \end{pmatrix}
$$
also
$$
\begin{array}{l}
4x_1+1x_2=5 \\
5x_1+2x_2=1
\end{array}
$$
Mit $x=A^{-1}*b$

$$
\begin{array}{l}
A^{-1}=\frac{1}{4*2-5*1}*\begin{pmatrix}2 & -1 \\ -5 & 4 \end{pmatrix}
= \frac13 * \begin{pmatrix}2 & -1 \\ -5 & 4 \end{pmatrix}
= \begin{pmatrix}\frac23 & -\frac13 \\ -\frac53 & \frac43 \end{pmatrix} 
\\
x_1 = \frac23 * 5 - \frac13*1 = \frac93 = 3
\\
x_2 = -\frac53*5+\frac43*1 = -\frac{21}3 = -7
\\\\
\rightarrow x = \begin{pmatrix}3 \\ -7\end{pmatrix}
\end{array}
$$

$$B=\begin{pmatrix}1 & 1 \\ 1 & 1\end{pmatrix} \rightarrow \nexists B^{-1}$$
Die inverse Matrix zu $B$ existiert nicht, $B$ ist singulär

## Eigenschaften der inversen Matrix
Rechenregeln
1. $A*A^{-1}=A^{-1}*A=E$ 
2. $(A^{-1})^{-1}=A$ 
3. $(A*B)^{-1}=B^{-1}*A^{-1}$ 
4. $(A^{-1})^T=(A^T)^{-1}$

Überlegung zu 1.
$$
\begin{array}{ll}
A*x=b & |*A^{-1} \text{ von Links} \\
\boxed{(A^{-1}*A)}*x=A^{-1}*b \\
\boxed{=E},\text{ da } x=A^{-1}*b
\end{array}
$$

### Allgemeine Definition
Eine quadratische Matrix heißt invertierbar wenn $A^{-1}$ existiert mit der Eigenschaft
$$A * A^{-1} = A^{-1}*A = E$$
### Anwendung 
Lösen von Matrizengleichungen
$$
\begin{array}{ll}
A*X=B \qquad A;B;X=\text{Matrix} 
\\\\
A=\begin{pmatrix}2 & 1 \\ -3 & -2 \end{pmatrix} \qquad B=\begin{pmatrix}2 & 5 & -8 \\ -4 & -9 & 14 \end{pmatrix} \\\\
\rightarrow X=(2\times3) \\\\
A*X=B & |*A^{-1} \text{ von Links} \\
A^{-1}*A*X=A^{-1}*B \\
X=A^{-1}*\boxed{B} \\\\
\boxed{\boxed{A^{-1}}} =\frac{1}{-1}*\begin{pmatrix}-2 & -1 \\ 3 & 2 \end{pmatrix} = \begin{pmatrix}2 & 1 \\ -3 & -2 \end{pmatrix} \\\\
X = \boxed{\boxed{\begin{pmatrix}2 & -1 \\ -5 & 4 \end{pmatrix}}}*\boxed{\begin{pmatrix}2 & 5 & -8 \\ -4 & -9 & 14 \end{pmatrix}} \\\\
=\begin{pmatrix}0 & 1 & -2 \\ 2 & 3 & -4 \end{pmatrix}
\end{array}
$$
![](AnwendungInvers01.png)![](AnwendungInvers02.png)![](AnwendungInvers03.png)

# Eigenwerte & Eigenvektoren
Eigenvektor einer Matrix ist der Vektor, der durch Multiplikation mit der Matrix zu seinem eigenen Vielfachen wird.

$$
\begin{array}{ll}
A=\begin{pmatrix}-1 & 2 \\ 4 & 6 \\\end{pmatrix} \qquad v=\begin{pmatrix}1 \\ 4\end{pmatrix} \\\\
A*v = \begin{pmatrix}-1 & 2 \\ 4 & 6 \\\end{pmatrix} * \begin{pmatrix}1 \\ 4\end{pmatrix} = \begin{pmatrix}7 \\ 28 \end{pmatrix} = 7 * \begin{pmatrix}1 \\ 4\end{pmatrix}
\end{array}
$$
Ein Eigenvektor einer $(m\times n)$-Matrix ist ein Vektor $x$ so dass gilt:
$$A*x=\lambda*x$$
Wobei $\lambda$ ein Skalar ist. Dieser Skalar wird als Eigenwert von $A$ bezeichnet.
Eigenvektor $v=\begin{pmatrix}1 \\ 4\end{pmatrix}$ gehört zum Eigenwert $\lambda_1=7$ 
Und $w=\begin{pmatrix}-2 \\ 1\end{pmatrix} \quad \lambda_2=-2$ 
Alle quadratischen Matrizen haben Eigenvektoren und zugehörige Eigenwerte. Diese sind allerdings nicht immer reell.

## Bestimmung von Eigenwerten und Eigenvektoren
Damit $\lambda$ ein Eigenwert einer Matrix $A$ ist, muss das homogene [Lineare Gleichungssystem](Lineare%20Gleichungssysteme.md) 
$$
\begin{array}{l}
A*x & =\lambda*x \\
A*x-\lambda * E * x & = 0 \\
x*(A-\lambda*E) & =0
\end{array}
$$
Unendlich viele Lösungen besitzen. Da der Nullvektor immer eine Lösung ist, bedeutet jede weitere, dass es unendlich viele gibt.
Dies ist genau dann der Fall, wenn $det(A-\lambda*E)=0$ ist (vgl. [Cramer'sche Regel](Determinanten.md#Cramer'sche%20Regel%20für%20ein%20(2x2)-System))

### Herleitung anhand eines Beispiels
$$
\begin{array}{ll}
A=\begin{pmatrix}7 & 3 \\ 3 & -1\end{pmatrix} \\\\
A - \lambda * E = \begin{pmatrix}7 & 3 \\ 3 & -1\end{pmatrix} - \lambda * \begin{pmatrix}1 & 0 \\ 0 & 1\end{pmatrix} = \begin{pmatrix}7-\lambda & 3 \\ 3 & -1-\lambda\end{pmatrix} \\\\
det(A-\lambda*E)=(7-\lambda)(-1-\lambda)-3*3
=-7-7\lambda+\lambda+\lambda^2-9 \\\\
= \lambda^2-6\lambda-16
\end{array}
$$
Dies ist die **Charakteristische Gleichung** der Matrix. Ihre Nullstellen sind die Eigenwerte.
$$
\begin{array}{ll}
\lambda^2-6\lambda-16 = 0\\
\rightarrow \lambda_1=8 \quad \lambda_2=-2 \\
\end{array}
$$
#### Bestimmung der zugehörigen Eigenvektoren
Einsetzen der Eigenwerte in die Matrix ergibt ein LGS
$$
\begin{array}{ll}
\begin{pmatrix}7-8 & 3 \\ 3 & -1-8 \end{pmatrix} * \begin{pmatrix}x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \\\\
\begin{pmatrix}-1 & 3 \\ 3 & -9 \end{pmatrix}*\begin{pmatrix}x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix}0 \\ 0 \end{pmatrix} \\\\
\rightarrow x = \begin{pmatrix}3t \\ t \end{pmatrix}
\end{array}
$$
Alle Vielfachen des Vektors $\begin{pmatrix}3 \\ 1 \end{pmatrix}$ sind Eigenvektoren zum Eigenwert $8$.
Analog ergibt sich $\begin{pmatrix}1 \\ -3 \end{pmatrix}$ für den zweiten Eigenwert. Die Symmetrie der Ergebnisse ist hier zufällig.

## $(3\times3)$-Matrix 
$$
\begin{array}{l}
A = \begin{pmatrix} 4 & -3 & 0 \\ 4 & -1 & -2 \\ 1 & -3 & 3 \end{pmatrix} \\\\
A-\lambda*E = \begin{pmatrix} 4-\lambda & -3 & 0 \\ 4 & -1-\lambda & -2 \\ 1 & -3 & 3-\lambda \end{pmatrix} \\\\
\dots \\\\
= -\lambda^3 + \lambda^2 - 11\lambda + 6 \\\\
\dots \\\\
\lambda_1=1 \rightarrow \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} \\ \lambda_2=2 \rightarrow \begin{pmatrix} 3 \\ 2 \\ 3 \end{pmatrix} \\ \lambda_3=3 \rightarrow \begin{pmatrix} 3 \\ 1 \\ 4 \end{pmatrix}
\end{array}
$$

## Sonderfälle
### $A$ und $A^T$:
Beide Matrizen haben die gleiche Determinante und Charakteristische Gleichung. Somit sind auch ihre Lösung, damit die Eigenwerte und auch die Eigenvektoren gleich

### Dreiecksmatrizen
Die Eigenwerte stehen auf der Hauptdiagonalen.
$$
\begin{array}{l}
A = \begin{pmatrix} 1 & 4 & 2 \\ 0 & 2 & -1 \\ 0 & 0 & -3 \end{pmatrix} \\\\
det(A-\lambda*E) = det\begin{pmatrix} 1-\lambda & 4 & 2 \\ 0 & 2-\lambda & -1 \\ 0 & 0 & -3-\lambda \end{pmatrix} \\\\
=(1-\lambda)*(2-\lambda)*(-3-\lambda)+0*(\dots)
\end{array}
$$
Der Satz von Nullprodukt löst die charakteristische Gleichung. Somit sind die Werte der Hauptdiagonalen die Eigenwerte.
Dies gilt nur für Matrizen die in Dreiecksform starten, nicht wenn diese durch Gauß-Umformung hergestellt wurde.

### Eigenwerte und Vektoren von $A$ und $A^{-1}$ 
Wenn $A$ eine inverse Matrix $A^{-1}$ besitzt und $\lambda$ Eigenwert von $A$ ist, dann ist $\frac1\lambda$  Eigenwert von $A^{-1}$ 