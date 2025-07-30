# Zufallsvariablen und Verteilungsfunktionen
## Definition Zufallsvariable
Sei $(\Omega; \mathcal P(\Omega); P)$ ein [Wahrscheinlichkeitsraum](Einführung.md#Wahrscheinlichkeitsraum).
Unter einer Zufallsvariablen (ZV) $X$ verstehen wir eine Funktion $X : \Omega \mapsto \mathbb{R}$ 

Typische Ereignisse:
$\left[X \leq k \right] := \left\{ \omega \in \Omega \mid X(\omega) \leq k \right\}$
$\left[X = k \right] := \left\{ \omega \in \Omega \mid X(\omega) = k \right\}$

Wir unterscheiden zwischen einer Diskreten und einer steigen Zufallsvariablen. 
- Stetig ist sie dann, wenn sie jeden Wert in einem beliebigen Wert annehmen kann.
## Beispiel (Zweimaliges Würfeln)
$\Omega = \left\{ \omega = \left( w_1, w_2 \right) \mid  w_i \in \left\{ 1; \dots ; 6 \right\} \right\}$ 
$X = \text{Augensumme}$
$X: \Omega \mapsto \mathbb{R}$
$A = [X=10] = \left\{(4;6); (5;5); (6;4) \right\}$
$P(X=10) = \frac{3}{36} = \frac{1}{12}$

## Definition Verteilungsfunktion
Sei $(\Omega; \mathcal P(\Omega); P)$ ein WR.
Eine Funktion
$F: \mathbb{R} \rightarrow [0;1]$
$x \mapsto P(X \leq x)$
heißt Verteilungsfunktion der [ZV](#Definition%20Zufallsvariable) $X$

Die Verteilungsfunktion $F(x)$ einer ZV $X$ ist die WKeit dafür, dass die ZV $X$ einen Wert annimmt, der kleiner oder gleich einer vorgegebenen reellen Zahl ist.

$$
\boxed{F(x) = P(X\leq x)}
$$

Eine ZV $X$ wird dabei durch ihre Verteilungsfunktion $F(x)$ vollständig beschrieben. 

### Eigenschaften Verteilungsfunktion
1. $F(x)$ ist eine monoton wachsende Funktion mit $0 \leq F(x) \leq 1$
2. $\lim_{x \to -\infty} F(x) = 0$ (Unmögliches Ereignis)  
3. $\lim_{x \to \infty} F(x) = 1$ (Sicheres Ereignis)  
4. Die WKeit $P(a < X \leq b)$ dafür, dass die ZV $X$ einen Wert zwischen $a$ (ausschließlich) und $b$ (einschließlich) annimmt, lässt sich mit Hilfe der [Verteilungsfunktion](#Definition%20Verteilungsfunktion) $F(x)$ wie folgt berechnen:
   $P(a < X \leq b) = F(b) - F(a)$

Typischer Verlauf einer stetigen Verteilungsfunktion:
![](stetigeVF.png)

und einer diskreten VF
![](diskreteVF.png)
# Diskrete Zufallsvariablen
## Definition Diskrete ZV
Eine ZV heißt diskret, wenn sie endlich viele oder höchstens zählbar unendlich viele reelle Werte annehmen kann.

Verteilungstabelle

| $x_i$      | $x_1$ | $x_2$ | $x_3$ | $x_4$ | $\dots$ |
| ---------- | ----- | ----- | ----- | ----- | ------- |
| $P(X=x_i)$ | $P_1$ | $P_2$ | $P_3$ | $P_4$ | $\dots$ |
Die diskrete Funktion
$$
f(x) = \left\{ \begin{array}{ll} P_i & x = x_i \\ 0 & \text{sonst} \end{array}\right.
$$
heißt Wahrscheinlichkeitsdichte (Dichtefunktion) der Verteilung. Sie ist auf $1$ normiert, d.h. 
$$
\displaystyle \sum_{i = 1}^{\infty} f(x_i) = 1
$$
Die zugehörige [Verteilungsfunktion](#Definition%20Verteilungsfunktion) der ZVn ist:
$$
F(x) = P(X \leq x) = \sum_{x_i \leq x}f(x_i)
$$

> [!Warning] Unterschied Dichte- und Verteilungsfunktion
> Die Dichtefunktion $f(x)$ beschreibt die Wahrscheinlichkeiten eines einzelnen Ereignisses.
> Mit $F(x)$ ist die Verteilungsfunktion gemeint, sie ist monoton und beschreibt die WS einen Wert $a \leq x$ zu erhalten
> 

### Beispiel
Wurf eines Würfels

| $x_i$               | $1$       | $2$       | $3$       | $4$       | $5$       | $6$       |
| ------------------- | --------- | --------- | --------- | --------- | --------- | --------- |
| $f(x_i) = P(X=x_i)$ | $\frac16$ | $\frac16$ | $\frac16$ | $\frac16$ | $\frac16$ | $\frac16$ |

---
Zweimaliger Münzwurf

$X = \text{Anzahl Kopf}$
$X : \Omega = \left\{ (z;z); (z;k); (k;z); (z;z) \right\}$

| $x_i$               | $0$       | $1$       | $2$       |
| ------------------- | --------- | --------- | --------- |
| $f(x_i) = P(X=x_i)$ | $\frac14$ | $\frac12$ | $\frac14$ |

## Kennwerte einer diskreten Zufallsvariablen
### Begriffsdefinitionen
Gegeben: Diskrete ZV $X$ mit Dichtefunktion $f$ 

#### Erwartungswert
$\displaystyle  E(X) = \mu$
$\displaystyle  E(X) = \sum_{i} x_i * f(x_i) = \sum_{i} x_i * P(X=x_i)$

#### Varianz
$\displaystyle  Var(X) = \sigma^2$
$\displaystyle Var(X) = \sum_{i}(x_i - E(X))^2*f(x_i)$ 

#### Standartabweichung
$\sigma = \sqrt{Var(X)}$ 
Ist ein gutes Streumaß, da die Einheit und Dimensionen mit denen des [Erwartungswerts](#Erwartungswert) übereinstimmen.

---
#### Beispiel
Urne mit 3 Weißen und 2 Schwarzen Kugeln, es wird 3 mal mit Zurücklegen gezogen.
$X = \text{Anzahl schwarzer Kugeln}$


| $x_i$    | $0$                                | $1$                                            | $2$                                            | $3$                               |
| -------- | ---------------------------------- | ---------------------------------------------- | ---------------------------------------------- | --------------------------------- |
| $f(x_i)$ | $(\frac{3}{5})^3 = \frac{27}{125}$ | $3*\frac25 * (\frac{3}{5})^2 = \frac{54}{125}$ | $3*\frac35 * (\frac{2}{5})^2 = \frac{36}{125}$ | $(\frac{2}{5})^3 = \frac{8}{125}$ |

$E(X) = 0 * \frac{27}{125} + 1 * \frac{54}{125} + \dots = 1.2$

$Var(X) = \dots = 0.72$

$\sigma = \sqrt{Var(X)} \approx 0.85$
	