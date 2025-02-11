# Nachweis von Monotonie / Beschränktheit

## Ansatz über Differenz benachbarter Werte
$$a_n=\frac{4n}{n+3}$$
**Behauptung: $a_n$ ist SMS (Streng-Monoton-Steigend)**
 
Beweis dass $a_{n+1}-a_n>0$

$$ \frac{4(n+1)}{(n+1)+3} - \frac{4n}{n+3} = \frac{4(n+1)\cdot(n+3)}{(n+4)\cdot(n+3)} - \frac{4n\cdot (n+4)}{(n+3) \cdot (n+4)} = \frac{12}{(n+3)(n+4)} > 0$$

## Ansatz Geschicktes Abschätzen
$$a_{n}=\frac{2n+1}{n+1}$$
**Behauptung: $a_n$ ist durch $1$ und $2$ beschränkt**
$$
\begin{matrix}
a_{n}=\frac{2n+1}{n+1} \geq \frac{2n+1}{2n+1} = 1 \\
\rightarrow s = 1
\end{matrix}
$$

$$
\begin{matrix}
a_{n}=\frac{2n+1}{n+1} \leq \frac{2n+2}{n+1} = \frac{2(n+1)}{n+1} = 2 \\
\rightarrow S = 2
\end{matrix}
$$


## Monotonie ab bestimmtem Wert
$$a_{n}=12n-n^{2}$$

**Behauptung: SMF ab $a_6$ also $a_{n+1} \geq a_n$ für $n > 5$**

$$
\begin{eqnarray}

12(n+1)-(n+1)^2 > 12n-n^2 \\
12n+12-(n^2+2n+1) > 12n-n^2 \\
12n+12-n^2-2n-1>12n-n^2 \\
\ldots \\
n > 5.5 \\
\rightarrow n \geq 6 \\
\end{eqnarray}
$$

## Monotonie bei rekursiven Folgen
$$a_0 = -\frac{1}{2}; \quad a_{n+1}=\sqrt{a_n + 1}$$
Beweis durch Induktion
$$\sqrt{a_{n+1}+1} > \sqrt{a_n +1}$$