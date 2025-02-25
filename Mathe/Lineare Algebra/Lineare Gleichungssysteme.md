Lineare Gleichungssysteme haben entweder genau eine, keine, oder unendlich viele Lösungen.
Systeme von $m$ linearen Gleichungen mit $n$ Unbekannten $x_1;x_2;x_3;\ldots;x_n$ 
$$
\begin{array}{rlrl}
a_{11} \cdot x_1 + a_{12} \cdot x_2 + \dots + a_{1n} \cdot x_n &= b_1  \\
a_{21} \cdot x_1 + a_{22} \cdot x_2 + \dots + a_{2n} \cdot x_n &= b_2  \\
\dots \\
a_{m1} \cdot x_1 + a_{32} \cdot x_2 + \dots + a_{mn} \cdot x_n &= b_m
\end{array}
$$
Kurz $(m \times n)$-System
$$
\begin{pmatrix}
a_{11} & \dots & a_{1n} \\
\vdots & \ddots & \vdots \\
a_{m1} & \dots & a_{mn}
\end{pmatrix}

\cdot

\begin{pmatrix}
x_{1} \\
\vdots \\
x_{n}
\end{pmatrix}

=

\begin{pmatrix}
b_{1} \\
\vdots \\
b_{n}
\end{pmatrix}
$$
Durch Hinzufügen des Vektors $b$ zur Koeffizientenmatrix entsteht die sogenannte "erweiterte Matrix" des LGS $B$ 
$$
B = (A;B) =
\begin{pmatrix}
a_{11} & \dots & a_{1n} & b_1 \\
\vdots & \ddots & \vdots & \vdots \\
a_{m1} & \dots & a_{mn} & b_n
\end{pmatrix}
$$

| Homogenes LGS           | Inhomogenes LGS |
| ----------------------- | --------------- |
| $b=0$ also alle $b_i=0$ | $b \neq 0$      |
# Lösen von LGS
Erlaubte Operationen:
1. Multiplizieren von Gleichungen mit $p \in \mathbb{R} \setminus \{0\}$ 
2. Addition des $p$-fachen einer Gleichung zu einer anderen Gleichung unter Beibehaltung der 1. Gleichung
3. Vertauschen von Gleichungen

## Der Gauß-Algorithmus zum Lösen eines LGS
Ziel ist es, die Matrix in die obere Dreiecksform zu bringen.
### 1. Eindeutig Lösbares, Homogenes LGS $(n\times n)$ 
$$
\begin{array}{l}
\begin{pmatrix}
2x_1 & -x_2 & -x_3 & = & 2 & (a) \\
4x_1 & +0 & +6x_3 & = & 2 & (b) \\
-3x_1 & +2x_2 & -x_3 & = & 1 & (c)
\end{pmatrix}
=
\begin{pmatrix}
2 & -1 & -1 & 2 \\
4 & 0 & 6 & 2 \\
-3 & 2 & -1 & 1
\end{pmatrix}
&
c^{*}=2*c+3*a
\\\\
\begin{pmatrix}
2 & -1 & -1 & 2 & (a) \\
4 & 0 & 6 & 2 & (b) \\
0 & 1 & -5 & 8 & (c^*)
\end{pmatrix}
&
b^* = b-2*a
\\\\
\begin{pmatrix}
2 & -1 & -1 & 2 & (a) \\
0 & 2 & 8 & -2 & (b^*) \\
0 & 1 & -5 & 8 & (c^*)
\end{pmatrix}
&
c^{**} = 2*c^{*}-b^* 
\\\\
\begin{pmatrix}
2 & -1 & -1 & 2 & (a) \\
0 & 2 & 8 & -2 & (b^*) \\
0 & 0 & -18 & 18 & (c^{**})
\end{pmatrix}
\quad \rightarrow x_3=-1 \quad x_2=3 \quad x_1=2
\end{array}
$$
### 2. Nicht-eindeutig lösbares, inhomogenes $(n\times n)$ System
Keine Lösung durch Widerspruch
$$
\begin{array}{l}
\begin{pmatrix}
3 & 2 & -1 & -2 & (a) \\
0 & 1 & -1 & 1 & (b) \\
4.5 & 3 & -1.5 & 0 & (c)
\end{pmatrix}
&
c^* = 3*a - 2*c
\\\\
\begin{pmatrix}
3 & 2 & -1 & -2 & (a) \\
0 & 1 & -1 & 1 & (b) \\
0 & 0 & 0 & -6 & (c)
\end{pmatrix}
&
\perp \rightarrow \text{Keine Lösung}
\end{array}
$$

Unendlich viele Lösungen durch $0=0$ Zeile
$$
\begin{array}{l}
\begin{pmatrix}
1 & -2 & 1 & 3 & (a) \\
0 & 1 & -3 & -5 & (b) \\
-2 & 4 & -2 & -6 & (c)
\end{pmatrix}
&
c^* = 2*a+c
\\\\
\begin{pmatrix}
1 & -2 & 1 & 3 & (a) \\
0 & 1 & -3 & -5 & (b) \\
0 & 0 & 0 & 0 & (c)
\end{pmatrix}
&
x_3 = t
\\\\
x_2 -3t = -5
\\
\rightarrow x_2 = 3t-5
\\\\
x_1-2*(3t-5)+t =3 \\
x_1-6t-10+t =3 \\
x_1+10-5+t =3 \\
\rightarrow x_1 = 5t-7
\\\\
L=\left( (5t-7); (3t-5); t \right)
\end{array}
$$
### 3. Homogenes System $A*x=0$ 
Besitzt immer die triviale Lösung $x_1=x_2=x_3=0$ 
Wenn eine weitere Lösung gefunden wird, hat das LGS unendlich viele Lösungen.
Vgl. [Cramer'sche Regel für ein (2x2)-System](Determinanten.md#Cramer'sche%20Regel%20für%20ein%20(2x2)-System)

### 4. Unterbestimmtes LGS - Weniger Gleichungen als Unbekannte
Falls das LGS überhaupt lösbar ist, hat es unendlich viele Lösungen da mindestens eine Unbekannte frei gewählt werden kann.

### 5. Überbestimmtes LGS
Ein LGS ist dann überbestimmt, wenn es mehr Gleichungen als Unbekannte besitzt. Zum Lösen werden bei $n$ Unbekannten die ersten $n$ beliebigen Gleichungen verwendet. Anschließend müssen die Lösungen mit allen Gleichungen verifiziert werden, ein einzelner Widerspruch führt zur Ungültigkeit der Ergebnisse.