# Support Vector Machines
## Linearer Kernel
Wenn Trennlinien durch Datensätze gezogen werden, entstehen Fehlklassifikationen sobald Datenpunkte der selben Klasse auf beiden Seiten der Linie enden.
SVM versuchen Trennlinien so zu legen, dass die Abstände zu allen Datenpunkten maximal werden.

![](TrennlinieSVM.png)



> [!Info] Hyperebene
> ## Hyperebene
> Eine Hyperebene im $n$-dimensionalen Raum ist eine $(n-1)$-dimensionale Fläche, die den Raum in zwei Teile trennt.
> Die Bereiche werden als 'vor' und 'hinter' der Ebene bezeichnet.
> 
> Im Zweidimensionalen ist sie eine Linie, im 3D-Raum eine Ebene.
 > 
> Der Normalenvektor $w$ bestimmt die Lage der Ebene.
> $$
> \vec{w} = \left(\begin{array}{}w_1 \\ w_2 \\ \dots \\ w_n \end{array}\right)
> $$
> Die Ebene hat die Gleichungsform
> $$
> w_1x_1 + w_2x_2 + \dots + w_nx_n = d
> $$
> Allgemein wird $w_0 = -d$ definiert um folgende Variante zu erhalten
> $$
> w_0 + w_1x_1 + w_2x_2 + \dots + w_nx_n = 0
> $$
> 
> Der Abstand eines Punktes zur Ebene wird also aus dem Ortsvektor des $\vec{x}$, dem [Vektor](Vektoren%20und%20Vektorräume.md#Vektoren) $\vec{w}$ und dem Wert $w_0$ berechnet.
> $$
> g(x) = w_0 + w \cdot x
> $$
> 
 
Berechnung des Abstand eines Punktes $P$ zur Hyperebene:
$$
r = \frac{g(x)}{\left|\left|w\right|\right|} = \frac{w \cdot x + w_0}{\left|\left|w\right|\right|}
$$
Für die Klassifikation zählt nur das Vorzeichen. Es zeigt auf welcher Seite der Ebene ein Punkt liegt.

- $w \cdot x + w_0 > 0$ : Klasse $A$
- $w \cdot x + w_0 < 0$ : Klasse $B$

![](SupportVectors.png)

Nur wenige Punkte sind für die Positionierung der Trennebene wirklich relevant. Sie heißen Support-Vectors.


> [!Warning] Normalisierung
> Da mit Abständen zwischen Punkten gearbeitet wird, haben die Maßstäbe der einzelnen Dimensionen einen großen Einfluss. Um hier keine Fehler zu verursachen werden die Werte normalisiert.
> 
> ``` Python
> from sklearn.preprocessing import StandardScaler
> 
> scaler = StandardScaler()
> scaler.fit(X_train)
> 
> X_train = scaler.transform(X_train)
> X_test = scaler.transform(X_test)
> ```
> 
> ![](Scaling.png)


In Realen Datensätzen lässt sich jedoch oftmals keine Fehlerfreie Trennlinie finden. Aus diesem Grund wird eine **Soft Margin** verwendet.
![](SoftMargin.png)

Es wird ein Parameter $C$ eingeführt, der beschreibt wie stark Fehlklassifikationen vermieden werden sollen. Er kann wenige Fehler erlauben um die Entscheidungsgrenze für alle anderen Werte breiter zu halten.

![](SizesOfC.png)

## Polynomialer Kernel
Gegeben ist eine eindimensionale Reihe von Daten die getrennt werden soll. Sie lassen sich nicht durch eine 0-Dimensionale Hyperebene (Einen Punkt) trennen.

Idee ist es, die Daten in einen höherdimensionalen Raum abzubilden um sie dort trennen zu können.
![](PolynomialKernel.png)

Durch hinzufügen einer $Y$ Koordinate mit dem Wert $X^2$ verteilen sich die Punkte so im Raum, dass sie sich durch eine 1-Dimensionale Ebene (Gerade Linie) trennen lassen.

Durch den [Kernel-Trick](https://de.wikipedia.org/wiki/Kernel-Methode) müssen die Daten nie direkt transformiert werden. Es ist möglich die Skalarprodukte durch die Kernel-Funktion zu ersetzen, um so aufwändige Berechnungen einzusparen.

> [!Danger] Nacharbeiten
> Die Kernel-Funktion und wie die Ersparnis erreicht wird ist mir unklar

Der Polynomiale Kernel $K: R^n \times R^n \to R$ ist definiert durch:
$$
K(x, y) = \left(x \cdot y + c\right)^{d}
$$
Wobei
- $c$ Ein konstanter Bias-Term ist, typischerweise $c \geq 0$
- $d$ Der Grad des Polynoms, ein ganzzahliger Wert mit $d > 1$

Höhere Grade des Polynoms erlauben komplexere Entscheidungsgrenzen und stärke Anpassung an Trainingsdaten. Somit kann auch durch zu große Polynome eine Überanpassung stattfinden.

## RBF Kernel
Bei der Radical Basis Function wird zu jedem Datenpunkt eine Gauß'sche Glockenkurve platziert.

![](RbfKernel.png)

Diese Kurven werden summiert und bilden die finale Entscheidungsfunktion.
Das Vorzeichen an einem Punkt sagt aus, welcher Klasse er angehört.

### Parameter
Um die Glockenkurve etwas anpassen zu können wurde der Parameter $\gamma$ eingeführt. Er wird benutzt um den Bruch im Exponenten zu vermeiden und ist daher folgendermaßen definiert:
$$
\gamma := \frac{1}{2\sigma^{2}}
$$
Je größer $\gamma$ wird, desto spitzer sind die Hügel der Kurven. Bei kleineren Werten nahe $0$ flachen die Hügel ab.


> [!Info] Kernelfunktion
> Der RBF-Kernel ist durch folgende Funktion definiert:
> $$
> K(x, y) := e^{-\gamma \left|\left|x-y\right|\right|^{2}}
> $$
> $\gamma$ ist dabei stets positiv und steuert die Breite
