# Mehrdimensionale Verteilungen
## Mehrdimensionale WS-Verteilungen
### Einführungsbeispiel
Zweimaliges Würfeln
$$
\Omega = \{(i,j) \; : \; 1 \leq j, j \leq 6\}
$$
Sei $X$ die Anzahl geworfener $1er$ 
$$ 
X : \Omega \to \{0;1;2\}
$$
Sei $Y$ die Anzahl geworfener $6er$
$$ 
Y : \Omega \to \{0;1;2\}
$$

Gesucht sind die Wahrscheinlichkeiten $P(X=x)$, $P(Y=y)$ und $P(X=x; Y=y)$ 

$$
\begin{array}{c|c|c}
P(X=x;Y=y) & 0 \quad 1 \quad 2 & P(X=x) 
\\ \hline
\begin{array}{}
0 \\ 1 \\ 2
\end{array} & 
	\begin{array}{c|c|c} 
		\frac{16}{36} & \frac{8}{36} & \frac{1}{36} \\\hline 
		\frac{8}{36} & \frac{2}{36} & \frac{0}{36} \\\hline 
		\frac{1}{36} & \frac{0}{36} & \frac{0}{36} 
	\end{array}
&   \left.\begin{array}{}
	\frac{25}{36} \\ \frac{10}{36} \\ \frac{1}{36}
	\end{array}
	\right\}\text{Randverteilung}
\\ \hline
P(Y=y) & 
	\begin{array}{}
		\frac{25}{36} & \frac{10}{36} & \frac{1}{36}
	\end{array}
	&
\\
\end{array}
$$

Definition:
Sei $(\Omega; \mathcal P(\Omega); P)$ ein WR.
Seien $X_1, \dots, X_n$ Zufallsvariablen
$X_i : \Omega \to \mathbb{R}$

Die Abbildung $X = (X_1, \dots, X_n): \Omega \to \mathbb{R}^n$ 
$\omega \mapsto (x_1(\omega), x_2(\omega), \dots, x_n(\omega))$

heißt $n$-dimensionaler Zufallsvektor (Zufallsvariable) mit den Komponenten $X_1, X_2 \dots, X_n$ 

Die Funktion $F_x:\mathbb{R}^n \to [0;1]$ 
$(x_1, \dots, x_n) \mapsto P(X_1 \leq x_1, X_2 \leq x_2 \dots X_n \leq x_n)$ heißt Verteilungsfunktion des Zufallsvektors $X=(X_1, \dots X_n)$

### Verteilungsfunktion Skizze
![TwoDBellcurve](TwoDBellcurve.png)

Eigenschaften der Verteilungsfunktion:
1. $\lim_{x \to -\infty} F(x;y) = \lim_{y \to -\infty} F(x;y) = 0$
2. $\lim_{\begin{array}{}x \to \infty \\ y \to \infty\end{array}} F(x;y) = 1$ 

### Diskrete zweidimensionale Verteilung
Definition
Eine zweidimensionale Zufallsvariable $Z=(X;Y)$ heißt diskret, wenn beide Komponenten $X$ und $Y$ diskret sind.

Annahme:
$X$ und $Y$ nehmen die endlich vielen Werte $x_1, \dots, x_n$ und  $y_1, \dots, y_n$ an.
$P_{ik} = P(X=x_1; Y=y_k)$ 

$$
\begin{array}{c|c|c}
X \setminus Y & y_1 \quad \dots \quad y_n 
\\ \hline
\begin{array}{}
x_1 \\ \vdots \\ x_m 
\end{array} & 
	\begin{array}{c|c|c} 
		p_{11} & \dots & p_{1n} \\\hline 
		\vdots & \ddots & \vdots \\\hline 
		p_{m1} & \dots & p_{mn} 
	\end{array}
&   \left.\begin{array}{}
	\frac{25}{36} \\ \frac{10}{36} \\ \frac{1}{36}
	\end{array}
	\right\}\text{Randverteilung } f_1(x)
\\ \hline
	& 
	\underbrace{
	\begin{array}{}
		\frac{25}{36} & \frac{10}{36} & \frac{1}{36}
	\end{array}
	}_{\text{Randverteilung } f_2(y)}
	&
\\
\end{array}
$$

Dichtefunktion
$f(x;y) = \left\{ \begin{array}{ll} p_{ik} & x=x_i \quad y = y_k \\ 0 & \text{sonst} \end{array}\right.$
für $i = 1, \dots, m$  und $k = 1, \dots, n$ 
$f(x,y) \geq 0$ und normiert:

$$
\sum_{i=1}^{m} \sum_{k=1}^{n} f(x_i, y_k) = 1
$$

Verteilungsfunktion
$$
F(x,y) = \sum_{i=1}^{x} \sum_{k=1}^{y} f(x_i, y_k)
$$
Randverteilungen
$$
f_1(x) = \left\{ \begin{array}{ll} p_i^* & x =   \end{array}\right.
$$
TODO


Beispiel
Dreimaliger Wurf einer Münze
$Z = \text{Zahl}$
$W = \text{Wappen}$ 

$\Omega = \{ ZZZ, ZZW, ZWZ, WZZ, WWZ, WZW, ZWW, WWW \}$
$Z = (X;Y)$ wobei
$X =  \text{Anzahl ''Zahl'' beim 1. Wurf}$
$Y =  \text{Anzahl ''Zahl'' beim 3 Würfen}$

$W_X = \{0;1\}$
$W_Y = \{0;1;2;3\}$


$$
\begin{array}{lll}
\boxed{x = 0} \\
y = 0 : & WWW & P(X=0, Y=0) = \frac{1}{8} \\
y = 1 : & WZW, WWZ & P(X=0, Y=1) = \frac{2}{8} \\
y = 2 : & WZZ & P(X=0, Y=2) = \frac{1}{8} \\
y = 3 : & -/- & P(X=0, Y=3) = 0 \\
\hline
\boxed{x = 1}\\
y = 0 : & -/- & P(X=0, Y=0) = 0 \\
y = 1 : & ZWW & P(X=0, Y=1) = \frac{1}{8} \\
y = 2 : & ZZW, ZWZ & P(X=0, Y=2) = \frac{2}{8} \\
y = 3 : & ZZZ & P(X=0, Y=3) = \frac{1}{8} \\
\end{array}
$$

$$
\begin{array}{c|c|c}
X \setminus Y  & 0 \quad 1 \quad 2 \quad 3 & 
\\ \hline
\begin{array}{}
0 \\ 1
\end{array} & 
	\begin{array}{c|c|c} 
		\frac{1}{8} & \frac{2}{8} & \frac{1}{8} & 0\\\hline 
		0 & \frac{1}{8} & \frac{2}{8} & \frac{1}{8} \\
	\end{array}
&   \left.\begin{array}{}
	\frac{1}{2} \\ \frac{1}{2}
	\end{array}
	\right\}f_1(x)
\\ \hline
& 
	\underbrace{\begin{array}{}
		\frac{1}{8} & \frac{3}{8} & \frac{3}{8} & \frac{1}{8}
	\end{array}}_{f_2(y)}
	&
\\
\end{array}
$$

### Stetige zweidimensionale Verteilungen
Eine Zweidimensionale Zufallsvariable $Z =  (X;Y)$ heißt stetig, falls die Zufallsvariablen $X$ und $Y$ ebenfalls stetig sind.

Verteilungsfunktion
$$
F(X;Y) = \int_{-\infty}^{x}\int_{-\infty}^{y} f(u,v) \, dv \, du
$$

Der Integrand $f \geq 0$ ist dabei die Dichtefunktion der zweidimensionalen Verteilung. Es gilt also:
$$
\int_{-\infty}^{\infty}\int_{-\infty}^{\infty} f(x,y) \, dy \, dx = 1
$$

Dichtefunktionen der Randverteilungen
$$
f_1(x) = \int_{-\infty}^{\infty} f(x,y) \, dy
$$$$
f_2(y) = \int_{-\infty}^{\infty} f(x,y) \, dx
$$

> [!NOTE] Rechenfehler
> Es wird ''kreuzweise'' integriert, also nach $x$ bei $f(y)$ und umgekehrt.

Beispiel
Die Dichtefunktion einer zweidimensionalen Gleichverteilung lautet:
$$
f(x,y) = \left\{ 
\begin{array}{ll}
	c & 0 \leq x \leq 2 \quad 0 \leq y \leq 5 \\
	0 & \text{sonst}
\end{array}
\right.
$$
Gesucht sind
1. die Verteilungsfunktion
2. $P(X \leq 1; y \leq 3)$

Die Konstante $c$ kann aus der Normierungsbedingung hergeleitet werden
$$
\int_{-\infty}^{\infty}\int_{-\infty}^{\infty} f(x,y) \, dy \, dx = \int_{x=0}^{2}\int_{y=0}^{5} f(x,y) \, dy \, dx = 1
$$
$\dots \to c = \frac{1}{10}$ 

$$
F(x;y) = \int_{0}^{x}\int_{0}^{y} \frac{1}{10} \, dv \, du = \int_{0}^{x} \frac{y}{10} \, du = \frac{xy}{10} 
$$

$$
P(X \leq 1; Y \leq 3) = F(1;3) = \frac{1 \cdot 3}{10} = 0.3
$$


Beispiel
$$
f(x;y) = \frac{1}{12\pi}e^{-\frac{1}{2}\left(\left(\frac{x}{3}\right)^2+\left(\frac{y-2}{2}\right)^2\right)}
$$

> [!NOTE] Hinweis
> $$
> \int_{-\infty}^{\infty} e^{-\frac{1}{2}t^2} = \sqrt{2\pi}
> $$

$$
f_1(x) = \int_{-\infty}^{\infty}f(x,y) \, dy = \frac{1}{12\pi} \int_{-\infty}^{\infty} e^{-\frac{1}{2}\left(\left(\frac{x}{3}\right)^2+\left(\frac{y-2}{2}\right)^2\right)} \, dy = \frac{1}{12\pi}\cdot e^{-\frac{1}{2}\left(\frac{x}{3}\right)^2} \int_{-\infty}^{\infty}e^{-\frac{1}{2} \cdot\left(\frac{y-2}{2}\right)^2}\, dy
$$
$$
t = \frac{y-2}{2} = \frac{y}{2} - \frac{2}{2} \qquad \frac{dt}{dy} = \frac12 \Rightarrow dy = 2 \cdot dt
$$
Untere Grenze $y \to -\infty \Rightarrow t \to -\infty$

Obere Grenze $y \to +\infty \Rightarrow t \to +\infty$

$$
I_1 = \int_{-\infty}^{\infty} e^{-\frac12 \left( \frac{y-2}{2} \right)^2} \, dy =  \int_{-\infty}^{\infty} e^{-\frac12 t ^2} \cdot 2 \, dt = 2 \int_{-\infty}^{\infty} e^{-\frac{1}{2}t^2} \, dt = 2\cdot \sqrt{2\pi}
$$
Somit gilt:
$$
f_1(x) = \frac{1}{12\pi}e^{-\frac12 \left( \frac{x}{3} \right)^2} \cdot 2\sqrt{2\pi} = \text{Dichtefunktion der Zufallsvariable X}
$$

$$
f_2(y) = \frac{1}{12\pi}e^{-\frac12 \left( \frac{y-2}{2} \right)^2} \cdot 3\sqrt{2\pi}
$$
