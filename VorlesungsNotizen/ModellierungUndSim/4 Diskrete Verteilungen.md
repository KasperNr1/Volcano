---
course: "[[Modellierung und Simulation 1]]"
lecture: "4"
source: https://unitc-my.sharepoint.com/personal/iinme01_cloud_uni-tuebingen_de/_layouts/15/stream.aspx?id=%2Fpersonal%2Fiinme01%5Fcloud%5Funi%2Dtuebingen%5Fde%2FDocuments%2FTeaching%2DGITs%2Fmodellierung%5Fund%5Fsimulation%2FOnline%2FVideos%2FMuS%5F3%2D2%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E42660bb3%2D4ec5%2D4c59%2Dbe71%2D2548c313b0bb
date: 2026-11-01
tags:
  - lecture
---
# Anhang zu [3 Verteilungsfunktionen](3%20Verteilungsfunktionen.md)
## Normalverteilung
Siehe Artikel zu [Normalverteilung](Normalverteilung.md)

- Verteilungsfunktion $f(x) = \frac{1}{\sqrt{2 \cdot \pi \cdot \sigma^2}}\cdot e^{-\left(\frac{\left(x - \mu\right)^2}{2 \sigma}\right)}$ 
- Range $(-\infty, \infty)$ 
- $E[X] =\mu$
- $VAR[X] = \sigma^2$
- Erzeugung durch [Accept Reject Methode](3%20Verteilungsfunktionen.md#Accept%20Reject%20Methode)
  1. Bestimmung von $U_1, U_2$, wobei die beiden Variablen [stochastisch unabhängig](Bedingte%20Wahrscheinlichtkeit.md#Stochastische%20Unabhängigkeit) sein müssen.
  2. $V_i = 2U_i -1$ 
  3. $W = V_1^2 + V_2^2$
  4. Falls $W \leq 1$ 
	  - Accept
	  - $Y = \sqrt{\dfrac{-2 \ln W}{W}}$ 
	  - Man erhält zwei normalverteilte Werte $X_1 = V_1 \cdot Y$ und $X_2 = V_2 \cdot Y$
  5. Sonst Reject
	  - Man erhält keinen neuen Wert und versucht in einer nächsten Iteration erneut.

# Diskrete Verteilungsfunktionen
## Deterministische Verteilung
Die primitive Verteilung gibt binär $0$ oder $1$ aus, je nachdem ob die Eingabe dem Parameter $\gamma$ entspricht
- Verteilung $x(i) = \left\{\begin{array}{}1 & \text{für } i=\gamma \\ 0 & \text{sonst} \end{array}\right.$ 
- $E[X] = \gamma$
- $VAR[X] =0$ 
- Range $\gamma$
- Mode $\gamma$

## Diskrete Gleichverteilung
- Verteilung $p(k) = \left\{\begin{array}{cl}\dfrac{1}{j - i + 1} & \text{if} \; k \in \{i, i+1, \dots, j \} \\ 0 & \text{else}\end{array}\right.$ 
- Range $i \leq k \leq j$
- $E[X] = \dfrac{i+j}{2}$
- $VAR[X] = \dfrac{\left(j - i + 1\right)^2 -1 }{12}$ 
- Mode: --
- Erzeugung durch Inversion
  $U \sim U(0,1)$
  $X = i + \left\lfloor \left(j - i + 1\right) \cdot U \right\rfloor$ 

## Beliebige Diskrete Verteilung
- $p(x) = \left\{\begin{array}{}p_k & \text{if} \; x=x_k, 0\leq k < n \\ 0 & \text{otherwise} \end{array}\right.$ 
- Range ist beliebig, aber diskret
- Erzeugung durch Inversion
  $U \sim U(0,1)$
  $X = x_k$ mit $k = \min(i: \sum_{0 \leq j \leq i} p_j \geq U)$ 
  Durch intelligente Datenstrukturen lässt sich die Implementierung hier optimieren und Suchaufwand vermeiden.

![](DiscreteDistribution.png)

> [!NOTE] Wertebereich
> Die Ausgabewerte können beliebig sein und sind nicht auf ganzzahlige Werte beschränkt. Lediglich die Anzahl der möglichen Werte muss diskret sein.

## Bernoulli Verteilung
Beschreibt ein Zufallsexperiment mit exakt zwei möglichen Ausgängen.
Klassisches Beispiel ist der Münzwurf.
- Verteilung $p(k) = \left\{\begin{array}{}1-p & \text{if} & k=0 \\ p & \text{if} & k=1 \\ 0 & \text{else} \end{array}\right.$  
- $E[X] = p$
- $VAR[X] =p \cdot (1-p)$ 
- $c_\text{var} = \sqrt{\frac{1-p}{p}}$ 
- Mode $0$ bzw. $1$ 
- Erzeugung durch [Inversion](3%20Verteilungsfunktionen.md#Inversion)

## Binomialverteilung
Beschreibt die Erfolge eines mehrfach wiederholten [Bernoulli Versuchs](#Bernoulli%20Verteilung)
Siehe auch [Binomialverteilung](Spezielle%20Verteilungen.md#Binomialverteilung)
- $p(k) = \binom{n}{k} \cdot p^k \cdot (1 - p)^{n-k}$  
- $E[X] = n\cdot p$
- $VAR[X] = n \cdot p \cdot (1-p)$ 
- $c_\text{var} [X] = \sqrt{\dfrac{1-p}{n\cdot p}}$ 


> [!Tip] Approximation
> Für $p << 1$ und $n$ sehr groß kann die Verteilung durch $\text{Poisson}(E[X])$ approximiert werden. Dies ist hilfreich beim Berechnen von $P(x_l \leq X \leq x_u)$
> Z.B. bei einer Erfolgswahrscheinlichkeit von $2\%$ und $1000$ Versuchen, um zu bestimmen wie hoch die Wahrscheinlichkeit von einer Anzahl Erfolgen zwischen $50$ und $150$ ist.
> 
> Für $n \to \infty$ kann die Binomialverteilung durch die Normalverteilung $N(E[X], VAR[X])$ approximiert werden.


## Geometrische Verteilung
Beschreibt die Anzahl der Fehlversuche bis zum Erfolg eines [Bernoulli Experiments](#Bernoulli%20Verteilung).
- $p(k) = (1-p)^k \cdot p, k\geq 0$ 
- Verteilungsfunktion $F(x) = 1 - (1-p)^{\left\lfloor x \right\rfloor + 1}$ 
- $E[X] = \dfrac{1-p}{p}, p\geq0$ 
- $VAR[X] = \dfrac{1-p}{p^2}$ 
- $c_\text{var}[X] = \dfrac{1}{\sqrt{1-p}}$ 
- Mode $0$ 
- Erzeugung durch 
  $X = \left\lfloor \dfrac{\ln(U)}{\ln(1-p)}\right\rfloor$ mit $U\sim U(0,1)$

### Um 1 Verschobene Geometrische Verteilung
Beschreibt die Anzahl aller Versuche bis das Bernoulli Experiment einen Erfolg erzielt anstelle nur die Zahl der Fehlversuche.

- $p(k) = (1-p)^{k-1} \cdot p, k\geq 1$ 
- Verteilungsfunktion $F(x) = 1 - (1-p)^{\left\lfloor x \right\rfloor}$ 
- $E[X] = \dfrac{1-p}{p}+1, p\geq0$ 
- $VAR[X] = \dfrac{1-p}{p^2}$ 
- $c_\text{var}[X] = \sqrt{1-p}$ 


> [!Warning] Namenskonvention
> Die um 1 verschobene Variante wird in der Literatur teilweise auch einfach als ‘Geometrische Verteilung’ bezeichnet. 


## Negativ-Binomiale Verteilung
Ähnlich wie die [Geometrische Verteilung](#Geometrische%20Verteilung) die Fehlversuche bei einem [Bernoulli Experiment](#Bernoulli%20Verteilung) beschreibt, wird durch diese Verteilung die Anzahl der Fehlversuche beschrieben bis bei einem [Binomialverteilten Experiment](#Binomialverteilung) $s$ erfolgreiche Versuche eintreten.
Die Verteilung kann auch als Summe von geometrischen Verteilungen dargestellt werden.
$\text{NegBin}(s,p) \sim \sum_{0 \leq i <s} \text{Geom}(p)$ 

- $p(k) = \binom{s + k -1}{k} \cdot p^s \cdot (1-p)^k = \binom{-s}{k}\cdot p^s \cdot (-(1-p))^k$ 
- $E[X] = s \cdot \dfrac{1-p}{p}$ 
- $VAR[X] = s \cdot \dfrac{1-p}{p^2}$
- $c_\text{var}[X] = \dfrac{1}{\sqrt{s \cdot (1-p)}}$ 
- Mode $y$ und $y+1$ falls $y$ ganzzahlig ist, sonst $\lfloor y \rfloor +1$
- Erzeugung durch Komposition:
  $Y_1, Y_2, \dots, Y_s \sim \text{geom}(p)$ und unabhängig
  $X = Y_1 + \dots + Y_s$


> [!Info] Erweiterung auf Reelle s Möglich
> Mittels der Gamma Funktion $\Gamma(x)$ kann die Verteilung auf nicht-ganzzahlige Werte erweitert werden.
>  $$
> p(k) = \frac{\Gamma(s+k)}{\Gamma(s) \cdot k!} \cdot p^s \cdot (1-p)^k
> $$
> Falls $s$ eine ganze Zahl ist, so gilt $\Gamma(s) = (s-1)!$

Für sehr große $p$ und $s$ nähert sich die Verteilung der [Poissonverteilung](Spezielle%20Verteilungen.md#Poissonverteilung) 

## Poisson-Verteilung
Sie beschreibt die Anzahl der Ankünfte in einem Intervall wobei die Zwischenankunftszeiten [exponentiell verteilt](3%20Verteilungsfunktionen.md#Exponentialverteilung) sind.
Der Parameter $y$ ist gleichzeitig der Erwartungswert der Verteilung.
- $p(k) = \dfrac{y^k}{k!} \cdot e^{-y}$ 
- $P(X \leq x) = e^{-y} \cdot \sum_{0 \leq k \leq x} \dfrac{y^k}{k!}$
- $E[X] = y$
- $VAR[X] = y$
- $c_{\text{var}} = \dfrac{1}{\sqrt{y}}$ 
- Mode $\left\{ \begin{array}{}y \; \text{und} \; y-1 & \text{falls} \; y \; \text{ganzzahlig} \\ \lfloor y \rfloor & \text{sonst}\end{array} \right.$ 


> [!Info] Praktische Implementierung
> Die Ergebnisse lassen sich durch ein Produkt vieler Terme bestimmen.
> Um Präzisionsfehler zu vermeiden wird in der Praxis ‘von beiden Enden’ Multipliziert. So wird jeder Term als Produkt einer sehr großen und sehr kleinen Zahl gruppiert, um eine mittlere Größe des Ergebnis zu gewährleisten. 

# Verwandtschaft Kontinuierlicher und Diskreter Verteilungen
![](ContiousArrival.png)

Die Zeit zwischen benachbarten Ankünften ist [exponentiell Verteilt](3%20Verteilungsfunktionen.md#Exponentialverteilung) mit Rate $\lambda$ und somit einer durchschnittlichen Zwischenankunftszeit von $\frac{1}{\lambda}$.
Die Zeit bis sich $k$ Ankünfte ereignen ist [Erlang-k-Verteilt](3%20Verteilungsfunktionen.md#Erlang%20Verteilung) 

Die Anzahl der Ankünfte in einem Intervall mit fester Länge $\tau$ ist [Poisson-Verteilt](#Poisson-Verteilung) mit Parameter $y= \tau \cdot \lambda$ 

![](DiscreteArrivals.png)

Wenn wir die Zeit in diskrete Slots einteilen ist die Anzahl der Slots zwischen Ankünften [Geometrische Verteilt](#Geometrische%20Verteilung) mit $p=\dfrac{1}{E[X]+1}$.
Die Anzahl der freien Slots bis $s$ Ankünfte geschehen, ist [Negativ-Binomial verteilt](#Negativ-Binomiale%20Verteilung).
Die Anzahl der Ankünfte innerhalb eines Intervalls fester Länge $n$ ist [binomial verteilt](#Binomialverteilung).
