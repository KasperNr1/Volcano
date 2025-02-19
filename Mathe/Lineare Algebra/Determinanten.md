# Zweireihige Determinanten | Determinante 2. Ordnung
Treten bei der Untersuchung von zwei linearen Gleichungen mit zwei Unbekannten auf.
$$
\begin{array}{rlrl}
a_{11} \cdot x_1 + a_{12} \cdot x_2 &= b_1 & | & \times a_{22} \\
a_{21} \cdot x_1 + a_{22} \cdot x_2 &= b_2 & | & \times (-a_{12}) \\
\\
a_{11} \cdot a_{22} \cdot x_1 + a_{12} \cdot a_{22} \cdot x_2 &= b_1 \cdot a_{22} & & \\
- a_{21} \cdot a_{12} \cdot x_1 - a_{22} \cdot a_{12} \cdot x_2 &= -b_2 \cdot a_{12} & & \\
\\
(1)+(2) \\
\\
a_{11} \cdot a_{22} \cdot x_1 - a_{21} \cdot a_{12} \cdot x_1 &=b_1 \cdot a_{22} - b_2 \cdot a_{12} \\
\\
\ldots \\
\end{array}
$$
$$
\\
x_1 = \frac{b_1 \cdot a_{22} - b_2 \cdot a_{12}}{a_{11} \cdot a_{22} - a_{21} \cdot a_{12}}
$$
Gleiches Prinzip führt ebenfalls zu:
$$
x_2 = \frac{b_2 \cdot a_{11} - b_1 \cdot a_{21}}{a_{11} \cdot a_{22} - a_{21} \cdot a_{12}}
$$
Der Nenner der Lösungen $x_1$ und $x_2$ nennt man die Determinante der [Koeffizientenmatrix](Matrizen.md) $A$
Determinante $D = det \begin{pmatrix}a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix} = \begin{vmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{vmatrix} = a_{11} \cdot a_{22} - a_{12} \cdot a_{21}$ 
Für die Zähler gilt $D_1 = \begin{vmatrix} b_{1} & a_{12} \\ b_{2} & a_{22} \end{vmatrix}$ und $D_2 = \begin{vmatrix} a_{11} & b_{1} \\ a_{21} & b_{2} \end{vmatrix}$ 

## Cramer'sche Regel für ein (2x2)-System
Die Lösungen des LGS sind mit den obigen Definitionen 
$$x_1=\frac{D_1}{D} \qquad x_2=\frac{D_2}{D}$$
### Kriterien zur Lösbarkeit
$D\neq0 \rightarrow$ Genau eine Lösung
$D=D_1=D_2=0 \rightarrow$ Unendlich viele Lösungen
$D=0$ und $(D_1 \vee D_2) \neq 0 \rightarrow$ Keine Lösung ($D=0$ und nicht alle $D_i=0$) 

# Determinanten 3. und höherer Ordnung
## 3. Ordnung
In einem $(3\times3)$ LGS lässt sich die Determinante analog zum $(2\times2)$ System herleiten.
$$
\begin{array}{rlrl}
a_{11} \cdot x_1 + a_{12} \cdot x_2 + a_{13} \cdot x_3 &= b_1  \\
a_{21} \cdot x_1 + a_{22} \cdot x_2 + a_{23} \cdot x_3 &= b_2  \\
a_{31} \cdot x_1 + a_{32} \cdot x_2 + a_{33} \cdot x_3 &= b_3
\end{array}
$$
$$x_1=\frac{D_1}{D} \quad x_2=\frac{D_2}{D} \quad x_3=\frac{D_3}{D}$$
$$
D = a_{11} \cdot a_{22} \cdot a_{33} + a_{12} \cdot a_{23} \cdot a_{31} + a_{13} \cdot a_{21} \cdot a_{32} - a_{13} \cdot a_{22} \cdot a_{31} - a_{11} \cdot a_{23} \cdot a_{32} - a_{12} \cdot a_{21} \cdot a_{33} \\
$$
Durch Ausklammern der Elemente in der z.B. ersten Zeile $a_{11},a_{12},a_{13}$ wird eine Rekursion ersichtlich
$$ \begin{array}{rl}
D &=a_{11} \cdot (a_{22} \cdot a_{33} - a_{32} \cdot a_{23}) - a_{12} \cdot (a_{21} \cdot a_{33} - a_{31} \cdot a_{23}) + a_{13} \cdot (a_{21} \cdot a_{32} - a_{31} \cdot a_{22}) \\
&= -a_{11} \cdot 
\begin{vmatrix} a_{22} & a_{23} \\ a_{32} & a_{33} \end{vmatrix} +
a_{12} \cdot 
\begin{vmatrix} a_{21} & a_{23} \\ a_{31} & a_{33} \end{vmatrix} -
a_{13} \cdot 
\begin{vmatrix} a_{21} & a_{22} \\ a_{31} & a_{32} \end{vmatrix}
\end{array}$$
"Entwicklung der Determinante nach der 1. Zeile"
Bildung der Summanden in den Entwicklungsformeln mit Hilfe von sogenannter "Unterdeterminanten" $\rightarrow$ Streichen der Zeile bzw. Spalte des ausgeklammerten Elements führt zu einer Untermatrix

Beispiel
$$
A =
\begin{pmatrix}
\cancel{1} & \cancel{3} & \cancel{4} \\
2 & \cancel{0} & 1 \\
3 & \cancel{1} & 2
\end{pmatrix}
\quad
A =
\begin{pmatrix}
1 & \cancel{3} & 4 \\
\cancel{2} & \cancel{0} & \cancel{1} \\
3 & \cancel{1} & 2
\end{pmatrix}
\quad
A =
\begin{pmatrix}
1 & \cancel{3} & 4 \\
2 & \cancel{0} & 1 \\
\cancel{3} & \cancel{1} & \cancel{2}
\end{pmatrix}
$$
$$D = -a_{12} \cdot 
\begin{vmatrix} 2 & 1 \\ 3 & 2 \end{vmatrix} +
a_{22} \cdot 
\begin{vmatrix} 1 & 4 \\ 3 & 2 \end{vmatrix} -
a_{23} \cdot 
\begin{vmatrix} 1 & 4 \\ 2 & 1 \end{vmatrix}$$
Das Vorzeichen des ausgeklammerten a hängt davon ab, ob die Indexsumme gerade ist.
Gerade $\rightarrow +$
Ungerade $\rightarrow -$
