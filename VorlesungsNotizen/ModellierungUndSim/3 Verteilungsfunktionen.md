---
course: "[[Modellierung und Simulation 1]]"
lecture: "3"
source: https://unitc-my.sharepoint.com/personal/iinme01_cloud_uni-tuebingen_de/_layouts/15/stream.aspx?id=%2Fpersonal%2Fiinme01%5Fcloud%5Funi%2Dtuebingen%5Fde%2FDocuments%2FTeaching%2DGITs%2Fmodellierung%5Fund%5Fsimulation%2FOnline%2FVideos%2FMuS%5F2%2D2%5F3%2D1%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2Ecef3d3f5%2Dbca8%2D44b1%2D8285%2D7598df10acfb
date: 2026-11-01
tags:
  - lecture
---
# Inversion

> [!Missing] Video MuS_2-2_3-1 
> Skript ca. 3.1 
> Video ab ca. 1h:19min

# Accept Reject Methode
Effizienz hängt stark von der Wahl der Majorante ab.

## Beispiel Accept-Reject
Erzeugung einer Zufallsvariable gemäß der $\text{beta}(3,4)$ Verteilungsfunktion.
$$
f(x) = \left\{\begin{array}{cl} 
60x^3(1-x)^2 & 0 \leq x \leq 1 \\ 
0 & \text{sonst}\end{array} \right.
$$
![](AcceptRejectExample.png)
Da sich diese Funktion nur schwer invertieren lässt bietet sich die Accept-Reject Methode an.

Da die Funktion ein Maximum an der Stelle $(0.6 ; 2.0736)$ hat kann als Majorante die Funktion $t(x) = \left\{\begin{array}{cl}2.0736 & 0 \leq x \leq 1 \\ 0 & \text{sonst}\end{array} \right.$ verwendet werden.
Aus dieser Majorante resultiert die Dichtefunktion $r(x) = \left\{\begin{array}{cl}1 & 0 \leq x \leq 1 \\ 0 & \text{sonst}\end{array} \right.$ die somit einer normalen Gleichverteilung entspricht.

Für die Entscheidung werden nun die beiden Zufallszahlen $Y \sim U(0,1)$ und $U \sim U(0,1)$ gewählt.

Es wird geprüft, ob $U \leq \dfrac{f(Y)}{c(Y)}$ gilt. In diesem Fall also $U \leq \dfrac{60Y^3(1-Y)^2}{2.0736}$ da die Majorante mindestens den Wert von $f(x)$ hat, ist diese Verhältnis zwischen $0$ und $1$ 


# Kontinuierliche Verteilungsfunktionen
## Gleichverteilung
- Dichtefunktion $f(x) = \dfrac{1}{b-a}, X\in[a,b]$
- Verteilungsfunktion $F(x) = \dfrac{(x-a)}{(b-a)}$ 
- Range $[a,b]$
- Erwartungswert $E[X] = \dfrac{a+b}{2}$
- Varianz $VAR[X] = \dfrac{(b-a)^2}{12}$
- Mode: nicht definiert
- Erzeugung durch [Inversion](#Inversion) $U \sim U(0,1), X = a + (b-a)U$

## Exponentialverteilung
- Dichtefunktion $f(x) = \lambda \cdot e^{-\lambda \cdot x}$ für $x \geq 0$ 
- Verteilungsfunktion $F(x) = 1 - e^{\lambda \cdot x}$
- Range $[0, \infty)$ 
- $E[X] = \dfrac{1}{\lambda}$
- $VAR[X] = \dfrac{1}{\lambda^2}$
- $c_{\text{var}} = 1$
- Mode: $0$
- Erzeugung durch [Inversion](#Inversion): $U \sim U(0,1), X = -\dfrac{\ln(U)}{\lambda}$ 
- Exponentiell verteilte Zwischenankunftszeiten ergeben einen Poisson-Prozess

## Definition Rate
Beschreibt die Wahrscheinlichkeit, dass ein Ergebnis innerhalb eines Intervalls $dt$ eintritt: $P(A \leq dt)$ 
$$
\lim_{dt \to 0} \frac{P(A\leq dt)}{dt} = \lambda
$$
Die Rate der [exponentiellen Verteilungsfunktion](#Exponentialverteilung) erfüllt diese Definition (Stichwort Taylorreihe)
$$
\lim_{dt \to 0} \frac{1 - e^{-\lambda \cdot dt}}{dt} = \lim_{dt \to 0} \frac{1 - \left(1 - \frac{\lambda \cdot dt}{1!} + \frac{\left(\lambda \cdot dt\right)^2}{2!} - \dots \right)}{dt} = \lambda
$$



## Erlang Verteilung
Die Erlang-k Verteilung beschreibt die Summe von $k$ [exponentiell](#Exponentialverteilung) verteilten Zufallsvariablen.

- Dichtefunktion $f(x) = \left\{ \begin{array}{}\dfrac{\left(\lambda x\right)^{k-1}}{\left(k-1\right)!}\cdot \lambda \cdot e^{-\lambda x} & x \geq 0 \\ 0 & x < 0 \end{array}\right.$
- Verteilungsfunktion $F(x) = \left\{\begin{array}{} 1-e^{-\lambda x } \cdot \sum_{0\leq i < k} \frac{\left(\lambda x\right)^i}{i!} & x \geq 0 \\ 0 & x < 0\end{array}\right.$
- Range $[0, \infty)$
- $E[X] = \frac{k}{\lambda}$
- $VAR[X] = \frac{k}{\lambda^2}$
- $c_\text{var} = \frac{1}{\sqrt{k}}$ 
- Mode $\frac{k-1}{\lambda}$
- Erzeugung durch [Inversion](#Inversion)
  $U_i \sim U(0,1), X = \sum_{0 \leq i < k} - \frac{1}{\lambda} \cdot \ln(U_i) = - \frac{1}{\lambda} \ln \left(\prod_{0\leq i < k} U_i \right)$

## Hyperexponentialverteilung
Die Zufallsvariable $X \sim H(\lambda_i, p_i, 0\leq i < k)$ ist hier eine Kombination von $k$ einzelnen exponentialverteilten Zufallsvariablen.

Dabei wird die exponentialverteilte Zufallsvariable $i$ mit einer Wahrscheinlichkeit von $p_i$ als Ausgabe der Hyperexponentialverteilung ausgewählt. 
![](Pasted%20image%2020261101102959.png)

Die Kenngrößen sind somit die mit $p$ gewichteten Mittelwerte der Kenngrößen aus den Exponentialverteilungen.
- Verteilungsdichtefunktion $f(x) = \sum_{0 \leq i < k} p_i \cdot \lambda_i \cdot e^{-\lambda_i \cdot x}$ 
- Verteilungsfunktion $F(x) = 1 - \sum_{0 \leq i < k} p_i \cdot e^{\lambda_i  \cdot x}$ 
- Range $[0, \infty)$
- $E[X] = \sum_{0 \leq i < k} \frac{p_i}{\lambda_i}$ 
- Variationskoeffizient sehr komplex, nachschlagen.
- Erzeugung durch Komposition
	1. Erzeuge Zufallszahlen $U_1, U_2$ 
	2. Bestimmen der zu verwendenden Exponentialverteilung
	   $i = \min\left(m : \sum_{0 \leq j < m} p_j \geq U_1\right)$
	3. Verwende $U_2$ zur Erzeugung von $X \sim \exp(\lambda_i)$ 
  $X = \left\{ \begin{array}{}X_0 \sim \exp(\lambda_0) & \text{with probaility } p_0 \\ \vdots & \vdots \\ X_{k-1} \sim \exp(\lambda_{k-1}) & \text{with probaility } p_{k-1} \end{array}\right.$

  ## Vergleich
  ![](ComparisonOfContinousDistributions.png)

Alle Funktionen besitzen einen Wertebereich von $[0,\infty)$ und konvergiergen für $\lim_{x \to \infty}$ gegen $0$. 
Ebenfalls ist der Mittelwert aller gezeichneten Funktionen exakt $1$.

