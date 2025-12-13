# Neural Nets
Eine Sammlung von mit einander vernetzten [Neuronen](#Neuronen).

Netze sind typischerweise in Schichten aufgebaut, wobei zwischen drei Kategorien unterschieden wird.
- Eingabeschicht
- Verdeckte Schicht
- Ausgabeschicht

Ein- und Ausgabeschichten bestehen aus einem Neuron für jedes Feature das ausgewertet wird. Ein Netz bei dem aus einem [Vektor](Vektoren%20und%20Vektorräume.md#Vektoren) der Größe $4$ eine Ja / Nein Entscheidung berechnet wird hat also $4$ Neuronen in der Eingabeschicht und ein einzelnes Neuron als Ausgabe. 

![](NeuralNet.png)

Typischerweise ist jedes Neuron mit allen Neuronen der darauf folgenden Schicht verknüpft. Die Anzahl der Verbindungen kann also extrem schnell ansteigen.

Die Ausgabe eines Neurons wird unverändert an alle mit ihm verbundenen Neuronen weitergegeben. Nicht benötigte Verbindungen können mit $0$ gewichtet werden. So sind sie effektiv deaktiviert.
Es ist auch möglich Neuronen mit sich selbst ode auch vorangegangenen Neuronen zu verbinden. Man spricht hier von [Rekurrenten neuronalen Netzen](Rekurrente%20Neuronale%20Netze.md).
Netze ohne solche Rückkopplung heißen **Feedforward-Netze**


## Neuronen
Neuronen sind die Grundbausteine [Neuraler Netze](#Neural%20Nets). Jedes Neuron stellt eine einfache [Funktion von Mehreren Variablen](Funktionen%20von%20Mehreren%20Variablen.md) dar, die aus allen Eingabedaten $x_1, x_2, \dots, x_i$ eine Ausgabe $y$ berechnet.

![](Neuron.png)

Da die Ausgabe eines Neurons als Eingabe für ein weiteres verwendet wird, werden normierte [Aktivierungsfunktionen](#Aktivierungsfunktion) eingesetzt. 

Es werden also in einem Neuron immer zwei Berechnungen durchgeführt.
1. Die gewichtete Summe $z$ der Eingänge mit den spezifischen Gewichten $b_1, \dots, b_i$
2. Das Ergebnis $y = \varphi(z)$, wobei $\varphi(x)$ eine beliebige Aktivierungsfunktion darstellt



### Aktivierungsfunktion
Eine Aktivierungsfunktion bestimmt, wie mit den Eingängen eines Neurons verfahren wird.

Häufig wird die sog. "Sigmoid-Funktion" verwendet.
$$
S_a(x) := \frac{1}{1+e^{-ax}}
$$
![](Sigmoid.jpeg)
Sie liefert für jeden Eingabewert eine Ausgabe im [Intervall](Intervalle%20und%20Mengen.md#Intervalle) $[0; 1]$ und ist differenzierbar.

Ebenfalls bekannt sind die **Identity-Funktion** und die **ReLU-Funktion**.
Sie sind beide sehr recheneffizient und geben positive Eingaben unverändert weiter. Die Identity-Funktion gibt auch Negative Werte weiter, sie verändert die Zahlen nicht. Bei der ReLU-Funktion wird eine Negative Eingabe in eine $0$ umgewandelt.


## Gradientenabstieg
Ist ein Verfahren zur Lösung numerischer Optimierungsprobleme.
Bei einem [Neuralen Netz](#Neural%20Nets) wird im Training für jeden der $n$ Datensätze die Ausgabe $\hat{y}$ mit dem Soll-Wert $y$ verglichen. Ihre Differenz wird quadriert und aufsummiert.
Somit ergibt sich für den Gesamtfehler $C$ des Netzes
$$
C = \sum_{i=1}^{n} \left(\hat{y_i} - y_i\right)^{2}
$$
Bei einem perfekten Netz würde dieser Gesamtfehler den Wert $0$ erreichen. 
Ziel des Trainings ist also, eine Kombination aus Gewichten für die einzelnen [Neuronen](#Neuronen) zu finden, bei denen $C$ minimal wird.

Der Gradient ist ein mathematisches Konzept das bei [Funktionen von Mehreren Variablen](Funktionen%20von%20Mehreren%20Variablen.md) die Richtung der größten [Steigung](Funktionen%20von%20Mehreren%20Variablen.md#Partielles%20Differenzieren) vorgibt.
Für eine Funktion $f(x_1, x_2, \dots, x_n)$ von $n$ Variablen ist der Gradient $\nabla f$ der [Vektor](Vektoren%20und%20Vektorräume.md#Vektoren) der [Partiellen Ableitungen](Funktionen%20von%20Mehreren%20Variablen.md#Partielles%20Differenzieren) von $f$ nach jeder Variable.
$$
\nabla f := \left(\begin{array}{c}\frac{\partial f}{\partial x_1} \\ \frac{\partial f}{\partial x_2} \\ \vdots \\ \frac{\partial f}{\partial x_n} \\ \end{array}\right)
$$

Einsetzen eines Punktes liefert den Vektor in dessen Richtung die Funktion am stärksten zunimmt.
$$
\begin{array}{c}
f(x,y) = x^2-y^2 \\ 
\\
\nabla f = (2x, -2y)^T \\
\nabla f(7, 1) = (14, -2)^T
\end{array}
$$
In diesem Beispiel muss also in Richtung des Vektors $\left(\begin{array}{c}14 \\ -2\end{array}\right)$ gegangen werden.


> [!Info] Parameter
> Bei einem Neuronalen Netz hat die Funktion deren Minimum gesucht wird so viele Parameter, wie das Netz Gewichte. Die Zahl steigt also sehr schnell und häufig auf mehrere Tausend bis Millionen Parameter an. Bei Besonders komplexen Modellen wie LLMs werden auch viele Milliarden Parameter erreicht. 

### Ablauf
Der Algorithmus startet an einem Punkt $\theta_0$ im Parameterraum. Also einer beliebigen Kombination von Parametern. Diese kann zufällig gewählt sein oder gezielt belegt sein.

An diesem Punkt wird der Gradient $\nabla f(\theta_i)$ berechnet.

Durch einen Schritt in die entgegengesetzte Richtung wird ein neuer Punkt ausgewählt. Dabei wird die Größe des Schritts von der Lernrate $\alpha$ bestimmt.
$$
\theta_{i+1} = \theta_i - \alpha \cdot \nabla f(\theta_i)
$$

Diese Schritte werden wiederholt, bis der Gradient nahe null ist (also eine Extremstelle gefunden wurde), oder ein Iterationslimit erreicht ist.

Die einzelnen Koordinaten von $\theta$ stellen die Gewichte aller Verbindungen dar.

### Optimierung
Die Berechnung des Gesamtfehlers wird sehr oft durchgeführt. Ihre Berechnungszeit hängt dabei auch von der Menge an Trainingsdaten ab.

Um die Berechnung zu beschleunigen werden in jedem Durchlauf nur eine zufällig ausgewählte [Teilmenge](Intervalle%20und%20Mengen.md#Teilmengen) der Trainingsdaten verwendet.
Dieses Verfahren heißt **Stochastic Gradient Descent**
Dabei wird jede Teilmenge der Daten als **Batch** bezeichnet. Sobald alle Batches verwendet wurden, ist eine **Trainingsepoche** vergangen.

![](Batches.png)


---

> [!Example] Klausuraufgabe
> Einfluss einzelner Neuronen auf das Ergebnis berechnen (Backpropagation Seite 294)
> Fehler wird von der Ausgabe Schichtenweise rückwärts durch das gesamte Netz berechnet

Bis Montag 3. November bestmögliches Modell für Handschrift Erkennung (MNIST-Datensatz)