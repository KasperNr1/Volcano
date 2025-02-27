Eine Aussage ist gültig für alle natürlichen Zahlen $n \in \mathbb{N}$, wenn man nachweisen kann:
1. Induktionsanfang
   Die Aussage gilt für $n=1$, bzw. den Base-Case der Aussage
2. Induktionsannahme
   Man nimmt an, dass die Aussage für $n=k$ gilt.
3. Induktionsschritt
   Unter Berücksichtigung der Induktionsannahme muss man zeigen, dass die Aussage auch für $n=k+1$ gilt.

# Beispiel
Zu beweisen ist:
$$
1+2+3+\dots+n=\frac12*n(n+1)
$$
## 1. Induktionsanfang
$$
\begin{array}{l}
1=\frac12*1(1+1) \\
1=1
\end{array}
$$
## 2. Induktionsannahme
$n = k$, es gelte
$$
1+2+3+\dots+k =\frac12*k(k+1)
$$
## 3. Induktionsschritt
$n = k+1$

$$
\begin{array}{l}
\underbrace{1 + 2 + 3 + \cdots + k}_{\text{Induktionsannahme } \frac12*k(k+1)} + (k+1) = \frac12 * (k+1)((k+1)+1) \\\\
\frac12*k(k+1)+(k+1)=\frac12 * (k+1)(k+2) \\\\
k^2+k+2k+2=k^2+k+2k+2 \\\\
0=0  \\\\
q.e.d.
\end{array}
$$
