Faustregel:
Approximation liefert gute Werte, falls
$$
\sigma^2 = n \cdot p \cdot (1-p) > 9
$$

Beispiel:
Bestimmte Pflanzensamen sind zu $95\%$ keimfähig.
Wie groß ist die Wahrscheinlichkeit, dass von $500$ ausgewählten Keimen 
- a) Höchstens $470$
- b) Mindestens $470$ und höchstens $485$ 
- c) Mindestens $480$ 
keimen?

$X$ ist die Anzahl keimfähiger Körner
$X \sim Bin(500,0.95)$ 
$E(X) = 500\cdot 0.95 = 475$
$Var(X) = 500 \cdot 0.95 \cdot 0.05 = 23.75 > 9$

Zentraler Grenzwertsatz $\to \frac{x -\mu}{\sigma} = \frac{x - 475}{\sqrt{23.75}} \sim Bin(0,1)$

a)
$$
P(X \leq 470) = \Phi \left( \frac{470 - 475}{\sqrt{23.75}} \right) = \Phi(-1.03) = 1-\Phi(1.03) = 0.1515 
$$

b)
$$
P(470 \leq X \leq 485) = \Phi \left( \frac{485 - 475}{\sqrt{23.75}} \right) - \Phi \left( \frac{469 - 475}{\sqrt{23.75}} \right) = 0.8705
$$

c)
$$
P(X \geq 480) = 1 - \Phi \left( \frac{479 - 475}{\sqrt{23.75}} \right) = 1 - \Phi(0.82) = 1 - 0.7939 = 0.2061 
$$

# Parameterschätzer
In diesem Abschnitt beschäftigen wir uns mit der Schätzung von unbekannten Mittelwerten,  Varianzen und Erfolgswahrscheinlichkeiten einer Verteilung.

## Einführungsbeispiel
Stichprobe
$$
1.4, 0.7, 0.9, -0.2, 2.1, 1.7
$$
Modellannahme:
Dies sind Realisierungen von $n=6$ unabhängig, identisch verteilten Zufallsvariablen (iid) $X_1, \dots X_6$ $X \sim \mathcal{N}$

Was ist $\mu; \sigma$?

Schätzfunktion:
Seien $X_1 \dots X_n$ unabhängig identisch verteilte Zufallsvariablen die eine mathematische Stichprobe beschreiben. 
Die konkrete Stichprobe $\underbrace{(x_1 \dots x_n)}_{\text{Stichprobenwerte}}$ wird interpretiert als Realisierung eines $n$-dimensionalen Zufallsvektors 
$$
\begin{array}{cl}
X=(X_1, \dots, X_n) & \to \text{n-dim. Zufallsgröße} \\
x_1 \dots x_n & \to \text{Stichprobenwerte}
\end{array}
$$

Eine Schätzfunktion für einen unbekannten Parameter $\vartheta$ einer Verteilung ist eine Funktion $\Theta = g(X_1 \dots X_n)$ die für jede konkrete Stichprobe $(x_1, \dots, x_n)$ einen Schätzwert $\hat{\vartheta} = g(x_1, \dots, x_n)$ für den Parameter $\vartheta$ liefert.
Gütekriterien (wünschenswerte Eigenschaften)
1. Eine Schätzfunktion $\Theta$ für den Parameter $\vartheta$ heißt erwartungstreu (unverfälscht), wenn $E(\Theta) = \vartheta$ 
2. Sie heißt konsistent, wenn ihre Varianz mit wachsendem Stichprobenumfang $n$ immer kleiner wird:
   $\lim_{n \to \infty} Var(\Theta)=0$

Beispiel
Optimale Schätzfunktion für den unbekannten Erwartungswert $\mu$ einer Verteilung:
$$
\begin{array}{ll}
\Theta & \displaystyle = g (X_1, \dots, X_n) = \frac{1}{n} \sum_{i=1}^{n} X_i \\
\hat{\mu} & \displaystyle  = \frac{1}{n} \sum_{i=1}^{n} x_i \text{ für eine Stichprobe}
\\
\end{array}
$$
Erwartungstreu $\boxed{E(\Theta) = \vartheta}$ 
$$
E(\Theta) = E\left(\frac{1}{n} \sum_{i=1}^{n} X_i \right) = \frac{1}{n} \cdot E\left( \sum_{i=1}^{n} X_i \right) = \frac{1}{n} \cdot \sum_{i=1}^{n} E\underbrace{(X_i)}_{\mu} = \frac{1}{n} \cdot n \cdot \mu = \mu
$$

Konsistent:
$$
Var(\Theta) = Var\left(\frac{1}{n} \sum_{i=1}^{n} X_i \right) = \frac{1}{n^2} \cdot \sum_{i=1}^{n} Var(X_i) = \frac{1}{n^2} \cdot n \cdot \sigma^2
$$
Der Grenzwert für $n \to \infty = 0$, somit ist die zweite Bedingung erfüllt.

## Maximum-Likelihood-Methode
Ein Verfahren zur Gewinnung von Schätzfunktionen für unbekannte Parameter einer Wahrscheinlichkeitsverteilung ist die sogenannte Maximum-Likelihood-Methode. 
Sei $X$ eine Zufallsvariable deren Dichtefunktion $f(x,\vartheta)$ noch einen unbekannten Parameter $\vartheta$ enthält. Bestimmung eines Schätzwerts $\hat{\vartheta}$ für den Stichprobenumfang $x_1 \dots x_n$ 

1. Aufstellen der Likelihood-Funktion
   $L=L(\vartheta) = f(x_1, \vartheta) \cdot \dots \cdot f(x_1, \vartheta)$ 
2. Schätzwert $\hat \vartheta$ für den Parameter $\vartheta$: Maximalstelle
   Also $\displaystyle \frac{\partial L}{\partial \vartheta} = 0$
   Erhalte $\hat \vartheta = g(x_1 \dots x_n)$
   Die Schätzfunktion $\Theta = g(x_1 \dots x_n)$ heißt Maximum-Likelihood-Schätzfunktion für den unbekannten Parameter $\vartheta$  


> [!NOTE] Bemerkung
> Enthält die Dichtefunktion mehrere unbekannte Parameter $\vartheta_1 \dots \vartheta_n : L(\vartheta_1 \dots \vartheta_n)$ 
> Erhalte $k$ Gleichungen
> $$
> \begin{array}{ll}
> \frac{\partial L}{\partial \vartheta_1} &= 0 \\
> \frac{\partial L}{\partial \vartheta_2} &= 0 \\
> \vdots \\
> \frac{\partial L}{\partial \vartheta_k} &= 0 \\
> \end{array}
> $$

2.Einfacher:
Verwenden der logarithmierten Likelihood-Funktion $L^{*}= \ln(L) = \ln(L(\vartheta_1 \dots \vartheta_n))$  

3.Maximum-likelihood-Schätzer ist derjenige Parameter, der die Wahrscheinlichkeit, die Stichprobe zu erhalten, maximiert.

# Übungen
## 1 Binomialverteilung $Bin(n,p)$
$$
L = L(p) = \binom{n}{k}*p^k*(1-p)^{n-k}
$$
$$
L^{*} = \ln(L(p)) = \ln \left(\binom{n}{k}*p^k*(1-p)^{n-k} \right) = \ln\left(\binom{n}{k}\right) + \ln\left(p^k\right) + \ln\left((1-p)^{n-k}\right) = \ln\left(\binom{n}{k}\right) + k \cdot \ln\left(p\right) + (n-k) \cdot \ln\left((1-p)\right) 
$$

$$
\frac{\partial L^{*}}{\partial p} = \frac{k}{p} - \frac{n-k}{1-p} = 0
$$

Nach $p$ auflösen

$$
\hat{p} = \frac{k}{n}
$$

## 2 Poissonverteilung : $X\sim Pois(\mu)$
$$
f(k; \mu) = \frac{\mu^k}{k!} \cdot e^{-\mu}
$$

konkrete Stichprobe $k_1 \dots k_n$ 
$$
L(\mu) = f(k_1; \mu) \cdot f(k_2; \mu) \cdot \ldots \cdot f(k_n; \mu) = \frac{\mu^{k_1}}{k_1!} \cdot e^{-\mu} \ldots \frac{\mu^{k_n}}{k_n!} \cdot e^{-\mu} = \left( \frac{\mu^{k_1}}{k_1!} \cdot \ldots \cdot \frac{\mu^{k_n}}{k_n!}\right) \cdot \underbrace{\left( e^{-\mu} \cdot \cdots \cdot e^{-\mu} \right)}_{\text{n mal}}
$$
$$
\boxed{= \frac{\mu^{k_1+k_2+\dots+k_n}}{k_1! \cdot k_2! \cdots k_n!} \cdot e^{-n\mu}}
$$
