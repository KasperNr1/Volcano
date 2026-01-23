# Bilderkennung
Ist eine der häufigsten Anwendungsgebiete für maschinelles Lernen und eine Unterkategorie der breiter gefächerten "Computer-Vision".
Typisch ist die Erkennung von Objekten oder Mustern in Bildern und Videos.
Beispielsweise in der [Automatischen Qualitätskontrolle ](Bachelorarbeit.md#Qualitäts%20Sensor) oder dem autonomen Fahren zur Erkennung von Fußgängern und Verkehrsschildern.

Auch normale [neuronale Netze](07%20Neural%20Nets.md#Neural%20Nets) können Bilder verarbeiten. Beispielsweise der MNIST Datensatz wurde verarbeitet, ohne dem Netz jemals konkrete Tools zur Handhabung von Bildern zu geben.

## Filter
Es sollen nun Filter in das Netz eingebaut werden, die speziell in der Lage sind mit Bildern zu arbeiten.
In der Analysis ist eine "Faltung" (en. "Convolution") ein Operator der für zwei Funktionen $f$ und $g$ eine Funktion $f*g$ liefert.
Jeder Wert von $f$ wird durch das mit $g$ gewichtete Mittel der ihn umgebenden Werte ersetzt.

Gegeben sei folgendes Eingabebild $I$ und der Filter $k$
$$
I = 
\begin{array}{c|c|c}
2 & -1 & 0 \\ \hline
0 & 8 & -2 \\ \hline
-4 & 4 & 0 \\
\end{array} 
\qquad 
k = 
\begin{array}{c|c}
0.5 & 1 \\ \hline
0 & 2.5
\end{array} 
$$
Die Anwendung des Filters führt zu folgender Ausgabe
$$
I^\prime= 
\begin{array}{c|c}
20 & -3 \\\hline
18 & 2 
\end{array}
$$

Unterschiedliche Filter haben verschiedene Effekte auf ein Eingabebild.
![](Convolutions.png)
Bei den Filtern zur Kantenerkennung ist die Summe der Gewichte $=0$. Nur falls die Summe einen positiven Wert hat kann ein Pixel seine Farbe behalten.

Convolutional Neural Networks sind