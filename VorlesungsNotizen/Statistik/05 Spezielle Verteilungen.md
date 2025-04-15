# Binomialverteilung
## Einführung
Urne mit $4$ weißen und $3$ schwarzen Kugeln. Gezogen wird $3$ Mal mit Zurücklegen. $X$ Sei die Anzahl der gezogenen weißen Kugeln.
$$
W_X = \{0;1;2;3\}
$$
$$
\begin{array}{ll} 
\displaystyle P(X=0) &= \displaystyle \left( \frac{3}{7} \right)^3 \\
\displaystyle P(X=1) &= \displaystyle \binom{3}{1} \left( \frac{3}{7} \right)^2 * \frac{4}{7} \\
\displaystyle P(X=2) &= \displaystyle \binom{3}{2} \frac{3}{7} * \left( \frac{4}{7} \right)^2 \\
\displaystyle P(X=3) &= \displaystyle \left( \frac{4}{7} \right)^3
\end{array}
$$

Dichtefunktion von $X$:
$$
f(k) = P(X=K) = \underbrace{\binom{3}{k}}_{\text{Permutationen}} * \underbrace{\left( \frac{4}{7} \right)^k}_{\text{Erfolg}} * \underbrace{\left( 1 - \frac{4}{7} \right)^{3-k}}_{\text{Misserfolg}}
$$
Definition:
In einem Zufallsexperiment wird beobachtet ob ein Ereignis $A$ eintritt oder nicht.
$$
X = \left\{
\begin{array}{cll}
0 & \text{Falls $A$ nicht eintritt} & \text{(Misserfolg)} \\
1 & \text{Falls $A$ eintritt} & \text{(Erfolg)}
\end{array}
\right.
$$

Verteilung von $X$

| $k$           | $0$   | $1$   |
| ----------- | --- | --- |
| $f(k)=P(X=k)$ | $1-p$ | $p$   |
Die Verteilung von $X$ heißt Bernoulli-Verteilung.
Schreibweise: 
$X \sim Ber(p)$ 

## Definition
Wir gehen von einem Bernoulli-verteilten Versuch mit Erfolgswahrscheinlichkeit $p$ aus.
$$
\begin{array}{cl}
X &= \text{Erfolge bei $n$-maliger stochastisch unabhängiger Wiederholung} \\
W_X &= \{0; 1; 2; \dots; n \}
\end{array}
$$
$$
[X = X_1 + X_2 + \dots + X_n \qquad X_i \sim Ber(p)]
$$
Diese Verteilung heißt Binomialverteilung
$$ 
X \sim Bin(n;p)
$$
Dichtefunktion 
$$
f(k) = P(X=k) = \binom{n}{k}*p^k*(1-p)^{n-k} \qquad k\in \{0; 1; \dots; n\}
$$ Verteilungsfunktion
$$
F(k) = P(X \leq k) = \sum_{i=0}^{k} \binom{n}{i} * p^i * (1-p)^{n-i}
$$

> [!NOTE] Spezialfall
> Für $n=1$ ist die Binomialverteilung gleich der Bernoulli-verteilung
> $$
> Bin(1,p) = Ber(p)
> $$

## Beispiel
### Tierarzt
Ein Tierarzt behandelt mit einem Medikament dass in $80\%$ der Fälle zu einer Heilung führt.
$$
\begin{array}{cl}
X &= \text{sei die Anzahl geheilter Tiere bei $10$ Behandlungen}
\end{array}
$$

$$
\begin{array}{cll}
P(X=6) &= \displaystyle \binom{10}{6} * \left( \frac{8}{10} \right)^6 * \left( \frac{2}{10} \right)^4 \approx 0.0881 \\
P(X\geq 7) &= P(X=7) + P(X=8) + P(X=9) + P(X=10) \approx 0.8791
\end{array}
$$

### Urne
$3$ Schwarze und $5$ Weiße Kugeln, $3$ Ziehungen mit Zurücklegen.
$X$ ist die Anzahl weißer Kugeln
$X \sim Bin(3; \frac{5}{8})$

$$
\begin{array}{cll}
P(X=2) &= \displaystyle \binom{3}{2} * \left( \frac{5}{8} \right)^2 * \left( \frac{3}{8} \right)^1 \approx 0.4395 \\
P(X \leq 2) &= P(X=2) + P(X=1) + P(X=0) = 1 - P(X=3) \approx 0.756
\end{array}
$$

---

Satz Sei $X \sim Bin(n;p)$ Dann gilt:
1. $E(X) = n*p$
2. $Var(X) = n*p*(1-p)$
3. $\sigma = \sqrt{Var(x)} = \sqrt{n*p*(1-p)}$

Beweis:
Sei $[X = X_1 + X_2 + \dots + X_n \qquad X_i \sim Ber(p)]$
$E(X_i) = 0*(1-p) + 1*p = p$
$E(X) = E(X_1) + E(X_2) + \dots + E(X_n)) = p + p + \dots + p = n*p$

## Beispiel
Ein homogener Würfel wird $100$ mal geworfen. $X$ ist die Anzahl der Würfe mit gerade Augenzahl.
$$
\begin{array}{l}
X &\sim Bin(100; \frac12) \\
\\
E(X) &= 100 * \frac12 = 50 \\
Var(X) &= 100 * \frac12 * (1-\frac12) = 25 \\
\sigma &= \sqrt{25} = 5 
\end{array}
$$

# Poissonverteilung
Die Verteilung einer diskreten Zufallsvariablen mit Wertebereich $\mathbb{N}_0$ und Dichtefunktion $f$ mit 
$$
f(k) = P(X=k) = \frac{\mu^k}{k!} e^{-\mu}
$$
heißt Poissonverteilung mit Parameter $\mu > 0$. Wir schreiben $X \sim \text{Pois}(\mu)$.


> [!NOTE] Bemerkung
> Für die Exponentialfunktion gilt
> $$
> e^x = \sum_{k=0}^{\infty}\frac{x^k}{k!}
> $$
> Daher gilt
> $$
> \sum_{k=0}^{\infty} f(k) = e^{-\mu} * \underbrace{\sum_{k=0}^{\infty} \frac{\mu^k}{k!}}_{=e^\mu} = 1
> $$

Die Verteilungsfunktion
$$
F(x) = P(X\leq x) = e^{-\mu} * \sum_{k\leq x} \frac{\mu^k}{k!}
$$

Satz:
Sei $X \sim \text{Pois}(\mu)$
Dann gilt:
1. $E(X) = \mu$
2. $Var(X) = \mu$
3. $\sigma = \sqrt{\mu}$

Beim Radioaktiven Zerfall sein die Zufallsvariable $X = \text{Anzahl der Atomkerne die in einer Sekunde zerfallen}$ 
$X \sim \text{Pois}(\mu)$ 
$\rightarrow \mu \text{ gibt an wie viele Atomkerne durchschnittlich pro Sekunde zerfallen.}$ Bei einem speziellen Präparat zerfallen im Durchschnitt $120$ Kerne pro Minute.

ges.: $P(X \geq 2) \qquad X \sim \text{Pois}(2)$
$$
\begin{array}{cl}
P(X=k) &= \displaystyle e^{-2} * \frac{2^k}{k!} \\
P(X \geq 2) &= \displaystyle\sum_{k=2}^{\infty} e^{-2} * \frac{2^k}{k!} \\
&= 1 - (P(X=0) + P(X=1)) \\
&= 1 - P(X=0) - P(X=1) \\
&= 0.594
\end{array}
$$
