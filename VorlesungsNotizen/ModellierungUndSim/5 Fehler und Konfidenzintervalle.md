---
course: "[[Modellierung und Simulation 1]]"
lecture: "5"
source: https://unitc-my.sharepoint.com/personal/iinme01_cloud_uni-tuebingen_de/_layouts/15/stream.aspx?id=%2Fpersonal%2Fiinme01%5Fcloud%5Funi%2Dtuebingen%5Fde%2FDocuments%2FTeaching%2DGITs%2Fmodellierung%5Fund%5Fsimulation%2FOnline%2FVideos%2FMuS%5F3%2D3%5F4%2D1%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2Eb5beceeb%2D6de2%2D479e%2D950f%2Dfe232a44970b
date: 2026-11-08
tags:
  - lecture
---
Bei empirischer Messung von Daten kann ein Intervall berechnet werden, in dem der Echte Mittelwert der zugrundeliegenden Verteilung tatsächlich liegt.

> [!Missing] Aufschrieb unvollständig
> Die Herleitung und genaue Definition / Bedeutung der Konfidenzintervalle fehlt noch. 
> Im Skript sind die Abschnitte um ca. 4.5 relevant.
> Im [Video](https://unitc-my.sharepoint.com/personal/iinme01_cloud_uni-tuebingen_de/_layouts/15/stream.aspx?id=%2Fpersonal%2Fiinme01%5Fcloud%5Funi%2Dtuebingen%5Fde%2FDocuments%2FTeaching%2DGITs%2Fmodellierung%5Fund%5Fsimulation%2FOnline%2FVideos%2FMuS%5F3%2D3%5F4%2D1%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2Eb5beceeb%2D6de2%2D479e%2D950f%2Dfe232a44970b) von 1:09:00 bis Ende (ca 100 Minuten)

# Statistische Grundlage (Part 2)
## Kovarianz
$$
\text{Cov}[X,Y] = E\left[\left(X - E[X]\right)\right] \cdot E\left[\left(Y - E[Y]\right)\right] = E\left[X \cdot Y\right] - E[X] \cdot E[Y]
$$
Für [stochastisch unabhängige](Stochastisch%20unabhängige%20Zufallsvariablen.md#Definition%20Stochastische%20Unabhängigkeit) [Zufallsvariablen](Zufallsvariablen.md) ist die Kovarianzfunktion immer $=0$.
Das invers gilt nicht, es kann aus einem Wert von $0$ nicht auf unabhängigkeit geschlossen werden.


> [!NOTE]- Gegenbeispiel
> Sei $X$ eine diskrete ZV mit den gleichwahrscheinlichen Ergebnissen $-2, -1, 1, 2$. Sei $Y=X^2$. 
> $X$ und $Y$ sind offensichtlich nicht unabhängig, aber sie sind unkorreliert. 
> $$
> E[X] = 0 \qquad \frac{1}{4}(-2\cdot 4 - 1 \cdot 1 + 1 \cdot 1 + 2 \cdot 4) - 0 \cdot E[Y] = 0
> $$ 

## Korrelation
Die Korrelation ist mittels [Kovarianz](#Kovarianz) und [Varianz](Zufallsvariablen.md#Varianz) definiert.
$$
\text{Cor}[X,Y] = \frac{\text{Cov}[X,Y]}{\sqrt{\text{VAR}[X] \cdot \text{VAR}[Y]}}
$$
Die Funktion beschreibt, wie stark zwei Zufallsvariablen gleichzeitig von ihrem [Mittelwert](Folgen.md#Arithmetisches%20Mittel) abweichen.

Für die Spezialfälle $X = Y$ und $X = -Y$ gilt:
$$
Y = X \Rightarrow \text{Cor}[X,Y] = 1 \\
Y = -X \Rightarrow \text{Cor}[X,Y] = -1 \\
$$
Ein Positiver Wert drückt aus, dass gleichzeitige Abweichungen vom Mittelwert dazu tendieren, das selbe Vorzeichen zu haben.
Für negative Werte kann analog geschlossen werden, dass gleichzeitige Abweichung dazu neigen verschiedene Vorzeichen zu besitzen.

## Empirische Bestimmung der Kovarianz 
Im Zeitdiskreten Fall gilt:
$$
\overline{\text{Cov}}[X,Y] = \frac{1}{n-1} \sum_{0 \leq i < n} \left(X_i - \overline{X} \left(n\right)\right) \cdot \left(Y_i - \overline{Y}\left(n\right)\right)
$$

Für den Zeitkontinuierlichen Fall gilt analog:
$$
\overline{\text{Cov}}[X,Y] = \frac{1}{T} \int_0^T \left(X_i\left(t\right) - \overline{X} \right) \cdot \left(Y_i\left(t\right) - \overline{Y}\right) \, dt
$$
## Empirische Bestimmung der Korrelation
Die [empirische bestimmte Kovarianz](#Empirische%20Bestimmung%20der%20Kovarianz) wird durch die Varianz geteilt um den normierten Wert zu erhalten
$$
\overline{COR}[X,Y] = \frac{\overline{COV}[X,Y]}{\sqrt{S^2[X] \cdot S^2[Y]}}
$$

## Autokovarianz
Auch `Lag` genannt.
Diese Größe beschreibt wie sehr aufeinanderfolgende Werte der selben Zeitreihe variieren.
Sie berechnet sich als die [Kovarianz](#Kovarianz) der Zeitreihe selbst und einer um das lag verschobene Kopie.

Die Autokovarianz $C_i$ eines stochastischen Prozesses $X_i$ mit Abstand $j$ ist definiert als 
$$
	C_i = \overline{\text{COV}}[X,Y] \qquad \text{Mit} \; Y_i = X_{i+j}
$$

$$
\widehat{C}_j(n) = \frac{1}{n-j} \sum_{0 \leq i < n-j} \left[ X_i - \overline{X} \right]\left[X_{i+j} - \overline{X}\right]
$$
Eine ähnliche Definition mit einem anderen Vorfaktor exisitiert. Diese hat angenehmere analytische Eigenschaften.


> [!Tip] Verwendete Formel
> Für die Vorlesung MuS 1 wird die erste Definition mit dem Vorfaktor $\frac{1}{n-j}$ verwendet


$$
\widehat{C}_j(n) = \frac{1}{n} \sum_{0 \leq i < n-j} \left[ X_i - \overline{X} \right]\left[X_{i+j} - \overline{X}\right]
$$
Für den zeitkontinuierlichen Fall existiert eine analoge Definition
$$
\widehat{C}_u(T) = \frac{1}{T} \int_0^{T-u} \left[ X(t+u) - \overline{X} \right]\left[X(t) - \overline{X}\right] \, dt
$$
## Autokorrelation
Durch Normierung wird die [Autokovarianz](#Autokovarianz) zur Autokorrelation.
$$
p_j(n) = \frac{\widehat{C}_j(n)}{S^2(n)}
$$

> [!Warning] Genauigkeit der Kenngrößen
> Die [Autokovarianz](#Autokovarianz) und [Autokorrelation](#Autokorrelation) sind nicht erwartungstreu. Bei größer werdendem betrachteten Abständen, werden die Ergebnisse schlechter.
> 
> Generell ist die Berechnung dieser Kenngrößen nur sinnvoll, wenn $j << n$ also die Anzahl der Werte die Länge des Lags deutlich übersteigt.


