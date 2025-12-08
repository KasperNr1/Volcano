# Support Vector Machines
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

---
Ab Seite 206

> [!Example] Klausuraufgabe
> Formel des Polynomialen Kernels kennen
> $$
> K(x, y) = \left(x \cdot y + c\right)^{d}
> $$
