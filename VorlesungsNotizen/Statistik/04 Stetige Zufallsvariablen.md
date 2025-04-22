# Definition Stetige Variable
Wir nennen eine Zufallsvariable stetig, wenn sie einen beliebigen Wert aus einem endlichen oder unendlichen Intervall annehmen kann. 
Dabei wird die Verteilungsfunktion in Integralform dargestellt 
$$
\begin{array}{}
\displaystyle F(X) = P(X \leq x) = \int_{-\infty}^{x} f(u) \, du
\end{array}
$$
Der Integrand $f$ ist die Dichtefunktion der stetigen Verteilung

Eigenschaften von $f$ und $F$ 
- $f(x) \geq 0$
- $f$ ist normiert, dh $\int_{-\infty}^{\infty} f(x) \, dx = 1$
- Die monoton wachsende Verteilungsfunktion $F$ ist Stammfunktion der Dichtefunktion $f$
  d.h. $\boxed{F'(x) = f(x)}$ 

# Glockenkurve
![](Glockenkurve.png)

## Beispiel
### 1 Verteilung gegeben
$$
F(x) = \left\{
\begin{array}{cl}
0 & x<2 \\
\dfrac{x-2}{3} & 2 \leq x \leq 5 \\
1 & x > 5
\end{array}
\right.
$$

![](Verteilung2.png)

$$
f(x) = \left\{
\begin{array}{cl}
0 & x<2 \\
\dfrac{1}{3} & 2 \leq x \leq 5 \\
0 & x > 5
\end{array}
\right.
$$
![](Verteilung.png)

### 2 Dichte gegeben
Sei $X$ eine stetige Zufallsvariable mit folgender Dichtefunktion
$$
f(x) = \left\{
\begin{array}{cl}
0 & x<0 \\
0.02x & 0 \leq x \leq 10 \\
0 & x > 10
\end{array}
\right.
$$

![](Dichtefunktion.png)

$$
F(x) = \left\{
\begin{array}{cll}
c & x<0 & c = 0 \\
0.01x^2 & 0 \leq x \leq 10 \\
c & x > 10 & c = 1 (\text{Monotonie berücksichtigt})
\end{array}
\right.
$$

![Verteilungsfunktion](Verteilungsfunktion.png)
### 3 
Die Lebensdauer $T$ eines elektronischen Bauteils sei eine exponentialverteile Zufallsvariable mit Dichtefunktion
$$
f(t) = \left\{
\begin{array}{cl}
0 & t<0 \\
0.1e^{-0.1t} & t \geq 0  
\end{array}
\right.
$$

![](ExponentialDichte.png)
#### Verteilungsfunktion
$$
F(t) = -e^{-0.1t} + 1 = 1-e^{-0.1t}
$$

![](ExponentialVerteilung.png)

#### P(t > 10)
$$
P(T \geq 10) = \int_{10}^{\infty} f(t) \, dt = F(\infty) - F(10) = \left(1 - 0\right) - \left(1-\frac{1}{e}\right) = \frac{1}{e} \approx 0.368
$$


---
# Definition
Sei $X$ eine stetige Zufallsvariable mit Dichtefunktion $f$

1. Erwartungswert $E(X) = \mu$
   $E(X) = \int_{-\infty}^{+\infty} x*f(x) \, dx$
2. Varianz $Var(X) = \sigma ^2$ 
   $\sigma = \int_{-\infty}^{+\infty} \left( x - \mu \right)^2 * f(x) \, dx$
3. Standardabweichung $\sigma$
   $\mu = \sqrt{Var(x)}$

## Beispiel 1
Sei $X$ eine stetige Zufallsvariable mit Dichtefunktion
$$
f(x) = \left\{
\begin{array}{cl}
0.02x & 0 \leq x \leq 10 \\
0 & \text{sonst} \\
\end{array}
\right.
$$

### Erwartungswert
$$
E(x) = \int_{0}^{10}x*(0.02x) \, dx = \left[ \frac{0.02}{3}x^3 \right]_{0}^{10} = 6.\overline{66}
$$

### Varianz
$$
Var(x) = \int_{0}^{10}(x-6.\overline{66})^2*(0.02x) \, dx = \left[ \frac{0.02}{3}x^3 - 0.0\overline{66} x^2 \right]_{0}^{10} = 6
$$
TODO, Quadrat am Anfang vergessen 50/9 ist richtig, nicht 6

### Standardabweichung
$$
\sigma = \sqrt{Var(x)} = \sqrt{\frac{50}{9}}
$$

## Beispiel 2
$T \sim Exp(\lambda)$  
$$
f(t) = \left\{
\begin{array}{cl}
0 & t<0 \\
\lambda e ^{-\lambda t} & t \geq 0
\end{array}
\right.
$$

$$
E(T) = \int_{-\infty}^{\infty} t * f(t) \, dt = \int_{-\infty}^{\infty} \underbrace{t}_{u} * \underbrace{\lambda * e^{-\lambda t}}_{v'} \, dt
$$
# Erwartungswert und Varianz von Funktionen einer Zufallsvariablen

## Definition 
Sei $X$ eine Zufallsvariable mit Dichtefunktion $f$ und $Z=g(X)$ eine von $X$ abhängige Funktion. Dann definiert man:
1. Falls $X$ diskret ist
   $E(Z) = E(g(X)) = \sum_{i}g(x_i * f(x_i))$ 
   $Var(Z) = \sum_{i}(g(x_i) - \mu)^2 * f(x_i)$
2. Falls $X$ eine stetige ZV ist:
   $E(Z) = \int_{-\infty}^{\infty}g(x) * f(x) \, dx$ 
   $Var(Z) = \int_{-\infty}^{\infty}(g(x)-\mu)^2 * f(x) \, dx$

In beiden Fällen kann die Varianz auch über das zweite Moment berechnet werden. 
$$
\sigma^2 = \underbrace{\int_{-\infty}^{\infty} \left( x - \mu \right)^2 \cdot f(x) \, dx}_{\text{Normale Berechnung Varianz}} = \underbrace{E(X^2) - [E(X)]^2}_{\text{Zweites Moment und Erwartung}}
$$

## Beispiele
### Diskret

| $x_i$    | $1$       | $2$       | $3$       | $4$       |
| -------- | --------- | --------- | --------- | --------- |
| $f(x_i)$ | $\frac18$ | $\frac38$ | $\frac38$ | $\frac18$ |
Sei $Z = x^2$, dann gilt
$$
E(Z) = E(x^2) = \sum_{i=1}^{4}x_i^2 * f(x_i) = \frac{56}{8} = 7
$$

### Stetig
Sei $X$ eine stetige ZV mit Dichtefunktion
$$
f(x) = \left\{
\begin{array}{cl}
0 & x<0 \\
e^{-x} & x \geq 0
\end{array}
\right.
$$
$$
Z = 2x+1
$$
$$
E(Z) = E(2x + 1) = \int_{-\infty}^{\infty}(2x+1)*(e^{-x})\, dx = \dots = 3
$$


> [!NOTE] TODO
> Partielle Integration nachrechnen / üben

# Satz
Sei $X$ eine ZV; $Z = aX + b$ dann gilt:
1. $Var(X) = E(X^2) - (E(X))^2$
2. $E(Z) = E(aX+b) = a * E(X) +b$
3. $Var(Z) = Var(aX + b) = a^2 * Var(X)$
4. $\sigma_Z = \sigma_{aX+b} = |a|\sigma_b$ 

## Beispiel Lineare Transformation
Sei $X$ eine ZV mit $E(X) = \mu_x$ und $Var(X) = \sigma_x^2$ 

Definiere $Z = \frac{X - \mu_x}{\sigma_x} = \frac{1}{\sigma_x} * X - \frac{\mu_x}{\sigma_x}$
Dann 
$$
E(Z) = E(\frac{1}{\sigma_x} * X - \frac{\mu_x}{\sigma_x}) = \frac{1}{\sigma_x} * \underbrace{E(X)}_{\mu_x} - \frac{\mu_x}{\sigma_x} = 0
$$
und 
$$
Var(Z) = \left( \frac{1}{\sigma_x} \right)^2 * \underbrace{Var(X)}_{\sigma_x^2} = 1
$$
$Z$ heißt standardisierte Zufallsvariable