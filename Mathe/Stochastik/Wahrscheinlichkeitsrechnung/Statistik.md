# Parameterschätzer
In diesem Abschnitt beschäftigen wir uns mit der Schätzung von unbekannten Mittelwerten, [Varianzen](Zufallsvariablen.md#Varianz)  und Erfolgswahrscheinlichkeiten einer Verteilung.

## Einführungsbeispiel
Stichprobe
$$
1.4, 0.7, 0.9, -0.2, 2.1, 1.7
$$
Modellannahme:
Dies sind Realisierungen von $n=6$ unabhängig, identisch verteilten Zufallsvariablen (iid) $X_1, \dots X_6$ $X \sim \mathcal{N}$

Was ist $\mu; \sigma$?
 Schätzfunktion: Seien $X_1 \dots X_n$ unabhängig identisch verteilte Zufallsvariablen die eine mathematische Stichprobe beschreiben. 
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

Schätzer Binomialverteilung
$$
\hat{p} = \frac{k}{n}
$$

Bsp.:
Um den Ausschussanteil $p$ in der Tagesproduktion von Glühbirnen zu schätzen, wurde eine Stichprobe vom Umfang $n=120$ entnommen. Dabei erwiesen sich $k=6$ Birnen als nicht brauchbar.
Mit der [Maximum-Likelihood-Methode](Statistik.md#Maximum-Likelihood-Methode) wird ein Schätzwert / Näherungswert für den Ausschussanteil $p$ bestimmt.

$$
\hat{p} = \frac{k}{n} = \frac{6}{120} = 5\%
$$
Wir können davon ausgehen, dass jede $20.$ Glühbirne unbrauchbar ist.

---

3 Gaußsche Normalverteilung
$$
X \sim \mathbb{N}(\mu, \sigma)
$$
$$
f(x; \mu; \sigma) =\frac{1}{\sigma \sqrt{2\pi}}*e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}
$$

Stichprobe $x_1, \dots, x_n$
Schätzwert für den unbekannten Parameter $\mu$
$$
\hat{\mu} = \frac{x_1 + \dots + x_n}{n} = \overline{x}
$$
Schätzwert für den unbekannten Parameter $\sigma$ 
$$
\hat{\sigma}^2 = \frac{1}{n} \sum(x_i - \overline{x})^2
$$
