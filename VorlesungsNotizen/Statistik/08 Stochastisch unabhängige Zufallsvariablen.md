# Definition Stochastische Unabhängigkeit
Die Zufallsvariablen $X$ und $Y$ mit den Verteilungsfunktionen $f_1(x)$ und $F_2(y)$ und der gemeinsamen zweidimensionalen Verteilung $F(x;y)$ heißen stochastisch unabhängig, falls 
$$
F(x;y) = F_1(x) \cdot F_2(y) \quad \forall x;y
$$

## Bemerkung
- $X$ und $Y$ sind stochastisch unabhängig $\Leftrightarrow \{X \leq x\} \text{ und } \{Y \leq y\} \text{ stochastisch unabhängig sind}$
- $X,Y$ stochastisch unabhängig $\Leftrightarrow f(x,;y) = f_1(x) \cdot f_2(y) \quad \forall x;y$ 

## Beispiel Urne
3 Weiße Kugeln
2 Schwarze Kugeln

### Experiment 1
Es werden nacheinander zwei Kugeln ohne zurücklegen gezogen.
- $X$ sei die Farbe der ersten Kugel 
- $Y$ die Farbe der zweiten Kugel
Dabei
- Weiß $\mathrel{\widehat{=}}0$
- Schwarz $\mathrel{\widehat{=}}1$ 

$$
\begin{array}{c|c|c}
X \setminus Y & 0 \quad 1 
\\ \hline
\begin{array}{}
0 \\ 1 
\end{array} & 
	\begin{array}{c|c} 
		\frac{3}{10} & \frac{3}{10} \\\hline 
		\frac{3}{10} & \frac{1}{10}  
	\end{array}
&   \left.\begin{array}{}
	\frac{6}{10} \\ \frac{4}{10}
	\end{array}
	\right\}\text{Randverteilung } f_1(x)
\\ \hline
	& 
	\underbrace{
	\begin{array}{}
		\frac{6}{10} & \frac{4}{10}
	\end{array}
	}_{\text{Randverteilung } f_2(y)}
	&
\\
\end{array}
$$
$$
\begin{array}{c|c|c}
x & 0 & 1 \\\hline
f_1(x) & \frac{3}{5} & \frac{2}{5}
\end{array}
\qquad
\begin{array}{c|c|c}
y & 0 & 1 \\\hline
f_2(y) & \frac{3}{5} & \frac{2}{5}
\end{array}
$$
$$
f(0;0) \neq f_1(0) \cdot f_2(0)
$$
$X$ und $Y$ sind stochastisch abhängig

### Experiment 2
Zwei Kugeln nacheinander ziehen mit Zurücklegen

$$
\begin{array}{c|c|c}
X \setminus Y & 0 \quad 1 
\\ \hline
\begin{array}{}
0 \\ 1 
\end{array} & 
	\begin{array}{c|c} 
		\frac{9}{25} & \frac{6}{25} \\\hline 
		\frac{6}{25} & \frac{4}{25}  
	\end{array}
&   \left.\begin{array}{}
	\frac{3}{5} \\ \frac{2}{5}
	\end{array}
	\right\}\text{Randverteilung } f_1(x)
\\ \hline
	& 
	\underbrace{
	\begin{array}{}
		\frac{3}{5} & \frac{2}{5}
	\end{array}
	}_{\text{Randverteilung } f_2(y)}
	&
\\
\end{array}
$$
Die Wahrscheinlichkeit $F(x,y)$ ist für jeden Wert gleich dem Produkt $f_1(x) \cdot f_2(y)$

Die Werte sind somit stochastisch unabhängig.
# Summe und Produkte von Zufallsvariablen
Satz:
Seien $X_1; \dots; X_n, Z$ Zufallsvariablen mit $Z=X_1 + \dots + X_n$ 
Dann gilt:
$E(Z) = E(X_1 + \dots + X_n) = E(X_1) + \dots + E(X_n)$


> [!NOTE] Bemerkung
> 
> $X$ und $Y$ sind Zufallsvariablen, dann ist auch $X*Y$ eine Zufallsvariable. $X*Y(\omega) = X(\omega)*Y(\omega)$
> Allgemein gilt der Zusammenhang für die Erwartungswerte nicht
> $$
> E(X*Y) \neq E(X) * E(Y)
> $$

Satz:
Seien $X_1; \dots, X_n$ stochastisch unabhängige Zufallsvariablen
$Z = X_1 * \dots * X_n$ dann gilt 
$$
E(Z) = E(X_1 * \dots * X_n) = E(X_1) * \dots * E(X_n)
$$


> [!NOTE] Bemerkung
> Für die Varianz $\sigma ^2$ einer Summe $Z=X+Y$ lässt sich die allgemeine Beziehung
> $$
> \sigma_z^2=\sigma_x^2+\sigma_y^2+2\sigma_{xy}
> $$
> Wobei $\sigma_x^2 = Var(X)$ und $\sigma_y^2 = Var(Y)$
> Die Größe $\sigma_{xy}$ wird als Kovarianz der Zufallsvariablen $X$ und $Y$ bezeichnet und ist definiert durch 
> $$\sigma_{xy} = E(X*Y) - E(X)*E(Y)$$
> Sind $X$ und $Y$ stochastisch unabhängig, so gilt:
> $$
> E(X*Y) = E(X)*E(Y)
> $$
> und somit
> $$
> \sigma_{xy} = 0
> $$

Satz:
Seien $X_1, \dots, X_n$ stochastisch unabhängige Zufallsvariablen und $Z=X_1 + \dots + X_n$ dann gilt:
$$
Var(Z) = Var(X_1 + \dots + X_n) = Var(X_1) + \dots + Var(X_n)
$$

# Zentraler Grenzwertsatz
Satz
Seien $X_1, X_2, \dots, X_n$ stochastisch unabhängige Zufallsvariablen die alle normalverteilt sind mit $E(X_i)=\mu_i$ und $Var(X_i) = {\sigma_i}^2$. Dann ist die Summe $Z=X_1 + X_2 + \dots + X_n$ ebenfalls normalverteilt mit $E(Z) = \mu_1 + \mu_2 + \dots + \mu_n$ und $Var(Z) = {\sigma_1}^2 + {\sigma_2}^2 +\dots + {\sigma_n}^2$  

Satz (Zentraler Grenzwertsatz)
Seien $X_1, \dots, X_n$ stochastisch unabhängige Zufallsvariablen die alle der gleichen Verteilungsfunktion mit den Erwartungswerten $\mu$ und der Varianz $\sigma^2$ genügen.
$$
Z_n = X_1 + \dots + X_n
$$
$$
U_n = \dfrac{X_1 + \dots + X_n - n \cdot \mu}{\sqrt{n} \cdot \sigma}
$$
Dann konvergiert die Verteilungsfunktion $F_n(U)$ der Zufallsvariablen $U_n$ gegen die Verteilungsfunktion $\Phi(U)$ der Standardnormalverteilung.

$$
F_n(U) 
\overset{n \to \infty} \longrightarrow
\Phi(u) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{u}e^{-\frac{1}{2}t^2} \, dt
$$
Summen von unabhängigen identisch verteilten Zufallsvariablen sind näherungsweise normalverteilt.

Für die Approximation der Binomialverteilung ergibt sich folgender Sonderfall:
Erinnerung
$$
X_1, \dots, X_n \sim Ber(p)
$$
$$
\Rightarrow X_1 + \dots + X_n \sim Bin(n,p)
$$

## Grenzwert von Moivre-Laplace
Sei $X \sim Bin(n,p)$.
Dann konvergiert die Verteilungsfunktion $F_n(u)$ der standardisierten Zufallsvariablen $U=\dfrac{x - \mu}{\sigma} = \dfrac{x - n \cdot p}{\sqrt{n \cdot p (1-p)}}$ für $n \to \infty$ gegen die Verteilungsfunktion $\Phi$  der Standardnormalverteilung
