---
course: "[[Modellierung und Simulation 1]]"
lecture: "1"
source: https://unitc-my.sharepoint.com/personal/iinme01_cloud_uni-tuebingen_de/_layouts/15/stream.aspx?id=%2Fpersonal%2Fiinme01%5Fcloud%5Funi%2Dtuebingen%5Fde%2FDocuments%2FTeaching%2DGITs%2Fmodellierung%5Fund%5Fsimulation%2FOnline%2FVideos%2FMuS%5F1%2D1%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E54e6bacd%2D1a3f%2D4f46%2Dbbc0%2D24b2f0a32a91
date: 2026-10-18
tags:
  - lecture
---
# Exponentialverteilung
Beschreibt oft die Länge von zufälligen Zeitintervallen (Wie die Dauer zwischen zwei Anrufen) in Abhängigkeit von der erwarteten Anzahl $\lambda$ pro Zeiteinheit. Der Mittelwert $\mu$ der Verteilung ist dabei der Kehrwert $\frac{1}{\mu} = \lambda$.
$$
\text{Exp}(\lambda) = f_\lambda(x) = \left\{ \begin{array}{ll} \lambda e ^{-\lambda x} & x \geq 0 \\ 0 & x <0\end{array}\right.
$$

## Visualisierung
Durch die exponentiell abnehmende Wahrscheinlichkeit größerer Werte ergibt sich folgende [Dichtefunktion](Zufallsvariablen.md#Definition%20Diskrete%20ZV). Dabei ist $f(0) =\lambda$ und somit auch einzelne Werte über $1$ möglich. Durch die Normierungseigenschaft verläuft der Rest der Kurve deutlich flacher.

![](https://thumb.wikimedia.org/wikipedia/commons/thumb/a/af/ExpDichteF.svg/960px-ExpDichteF.svg.png?utm_source=de.wikipedia.org&utm_campaign=imageinfo&utm_content=thumbnail)

Die [Verteilungsfunktion](Zufallsvariablen.md#Definition%20Verteilungsfunktion) verläuft entsprechend
![](https://thumb.wikimedia.org/wikipedia/commons/thumb/b/ba/ExpVerteilungF.svg/960px-ExpVerteilungF.svg.png?utm_source=de.wikipedia.org&utm_campaign=imageinfo&utm_content=thumbnail)

## Rechenregeln

> [!Missing] TODO
> Rechenregeln für den Umgang mit Exponentialverteilungen
> $P(X=a), P(X>a), P(X\leq a)$


#  Summe zweier Zufallsvariablen
Convolution, auf deutsch auch "Faltung” genannt ist eine wichtige Art um zwei Funktionen $f$ und $g$ zu einer neuen Funktion $f * g$ zu kombinieren.

> [!Info]- Notation
> Der Stern $*$ ist dabei ein Operator der speziell für Convolutions verwendet wird


Dabei kann beispielsweise eine Verteilung dargestellt werden, die die Summe zweier [Zufallsvariablen](Zufallsvariablen.md#Definition%20Zufallsvariable) beschreibt.

Die Dichtefunktion der Summe $X$ von $X_1$ und $X_2$ kann dargestellt werden als:
$$
P(X=i) = x(i) = \sum_j x_1(j) \cdot x_2(i-j) = (x_1 * x_2)(i)
$$
Für stetige Werte wird die Summe entsprechen durch ein [Integral](Integrale%20&%20Rotationskörper.md) ersetzt.
$$
a(t) = \int_{-\infty}^{\infty} a_1(\tau) \cdot a_2(t-\tau) = (a_1 * a_2)(t)
$$

# Differenz zweier Zufallsvariablen
Die Verteilung der Differenz zweier Zufallsvariablen berechnet sich sehr änlich zur [Summe zweier Zufallsvariablen](#Summe%20zweier%20Zufallsvariablen), jedoch ist der Aufbau nicht identisch zur Convolution.
Die Verteilung von $X = X_1 -X_2$ berechnet sich:
$$
P(X=i) = x(i) = \sum_j x_1(i+j) \cdot x_2(j)
$$

> [!Question] Unterschied Faltung
> Der Term könnte auch mit $x_2(j-i)$ dargestellt werden, wodurch der Unterschied leichter sichtbarer wäre.

Der Fall mit stetigen Werten ist analog aufgebaut.

# Statistische Kenngrößen
## Zentrale Momente

> [!Example] Klausuraufgabe
> Herleitung der 1. und 2. Momente (SA und Varianz)
> Im Skript bei Punkt 1.3.4
> Und im [Video](https://unitc-my.sharepoint.com/personal/iinme01_cloud_uni-tuebingen_de/_layouts/15/stream.aspx?id=%2Fpersonal%2Fiinme01%5Fcloud%5Funi%2Dtuebingen%5Fde%2FDocuments%2FTeaching%2DGITs%2Fmodellierung%5Fund%5Fsimulation%2FOnline%2FVideos%2FMuS%5F1%2D1%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E3f69263a%2De2a1%2D45d0%2D8d75%2D4444d49d0624) um 2:50:00 und am Ende nochmals
> Herleitung auch für verschiedene Verteilungen


## Variationskoeffizient
Beschreibt das Verhältnis aus Standardabweichung und Erwartungswert.
Die Größe ist dimensionslos und beschreibt die Schwankung der Zufallsgröße.
$$
c_{\text{var}}[A] = c_A = \frac{\sigma_A}{m_1} = \frac{\sqrt{\text{VAR}[A]}}{E[A]}
$$
Um Division durch $0$ zu vermeiden, muss die Variable positiv sein. Das Verhältnis der beiden Kenngrößen ändert sich nicht, wenn zur Berechnung des Koeffizienten eine konstante Verschiebegröße zu allen Werten addiert wird.

## Schiefe
$$
\upupsilon_A = \frac{E\left[\left(A-E\left[A\right]\right)^3\right]}{\sigma^{3}_{A}}
$$
Bei einer symmetrischen Verteilung ist $\upupsilon_A=0$.
Für negative Werte $\upupsilon_A<0$ ist die Verteilung Linksschief, bei positiven $\upupsilon_A>0$ Rechtsschief.