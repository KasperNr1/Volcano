![](DecisionTree.png)

Entscheidungsbäume sind ein Werkzeug zur [Klassifikation](01%20Grundidee.md#Klassifikation) von Objekten.
Ein Klassifikationsmodell ist in der Lage, einen solchen Entscheidungsbaum zu erstellen.

Jeder Schritt soll die Datenmenge möglichst Sortenrein trennen
![](DecisionTree2.png)

Es gibt eine unbegrenzte Menge korrekter Lösungsbäume, wobei die Qualität eines Baums anhand verschiedenen Kriterien bestimmt wird (Schlimmster-Worst-Case / Summe von Knoten / etc.)

## Bewertung
Entscheidungsbäume sind gut nachvollziehbar und lassen sich anschaulich darstellen. Ebenfalls ist die Berechnung einer Vorhersage mit einem trainierten Baum sehr schnell.
Bei einer getroffenen Aussage lässt sich genau nachvollziehen welche Folge von Entscheidungen zum Ergebnis geführt hat.

Jedoch neigen diese Bäume zu Überanpassung und sind bei Datensätzen mit komplexeren Entscheidungsgrenzen nicht sehr akkurat. Da die Trennebenen nur Senk- oder Waagrecht verlaufen werden diese freier geformten realen Entscheidungsgrenzen nur selten exakt abgebildet.


TODO Hyperparameter beschreiben (Maximale Baumhöhe oder Knotenzahl - Seite 154)

# ID3-Algorithmus
Liefert relativ gute, simple Bäume für Datensätze mit [Nominalen Merkmalen](https://de.wikipedia.org/wiki/Nominalskala)  (Funktioniert nicht bei stetigen Werten). Der Algorithmus ist auch bei vielen Features effizient

Es wird zu jedem Attribut eine Abfrage erstellt wenn die aktuelle Restmenge nicht ausreichend getrennt ist. Die exakte Wahl des Wertes bei dem getrennt wird ist zwischen verschiedenen Varianten des Algorithmus unterschiedlich.
Im Standardfall wird so gewählt, dass der "Information Gain" maximal ist.

Nach der Entscheidung für ein Kriterium wird rekursiv erneut gewählt, bis jedes Kriterium abgefragt wurde oder die [Menge](Intervalle%20und%20Mengen.md#Mengen) der verbleibenden Datenpunkte hinreichend gut getrennt ist.

## Informationsgehalt
Dabei ist der Informationsgehalt $I(P(A))$ über den Eintritt eines Ereignis mit Eintrittswahrscheinlichkeit $P(A)$ folgendermaßen definiert.

$$
I(P(A)) := -P(A) \cdot \log_{2}(P(A))
$$

![InfoGain](InfoGain.png)

Es wird keine Information gewonnen wenn ein Test bezüglich eines Ereignisses durchgeführt wird dass sicher eintritt oder nicht eintritt.

## Entropie
Sie ist ein Maß für den Mittleren Informationsgehalts eines Zufallsexperiments $V$  mit den möglichen Ausgängen $A_1, A_2, \ldots, A_i$ 
$$
H(V) := - \sum_{i=1}^{n} P(A_i) \cdot \log_{2}(P(A_i))
$$
Jeder einzelne Wert ist negativ, somit wird eine große negative Summe gebildet und in einem Schritt negiert um einen positiven Wert zu erhalten. Dabei wird nicht durch die Anzahl der Werte dividiert wie es beim [Arithmetischen Mittel](Folgen.md#Arithmetisches%20Mittel) üblich ist. Die Gewichtung erfolgt durch die Multiplikation mit der Eintrittswahrscheinlichkeit. Da die Ereignisse konkurrieren normiert sich der Wert hier immer selbst.
Ein großer Wert der Entropie deutet auf sehr ähnliche Wahrscheinlichkeiten hin.


> [!Info] Eintrittswahrscheinlichkeiten
> In unserem Fall werden die Häufigkeiten innerhalb der gemessenen Daten als Eintrittswahrscheinlichkeit verwendet.

### Beispiel: Münzwurf 
$$
\text{Information Gain} = -0,5 \cdot \log_2(0,5)
$$

Da beide Möglichkeiten des Münzwurfs gleich wahrscheinlich sind berechnet sich die Anwendung der Formel zur Entropie also
$$
H(V) = -\sum_{i=1}^{2} 0,5 \cdot \log_2(0,5) = -2 \cdot 0,5 \cdot \log_2(0,5) = -1 \cdot \log_2(2^{-1}) = \log_2(2) = 1
$$
Der Münzwurf hat also einen Entropiewert von $1\,Sh$ 


### Bedingte Entropie
Es soll immer die Information als nächstes geprüft werden, die den größten Einfluss auf die Qualität der Schätzung hat.
"Wie unsicher ist $V$ wenn wir $W$ kennen?"
$$
H(V \mid W) = \text{Bedingte Entropie}
$$
Eine geringe bedingte Entropie bedeutet, dass die Daten durch das Attribut gut getrennt werden.

![](BedingteEntropie.png)

### Information Gain
Ein Maß für die Senkung der Entropie durch eine Entscheidung.
$$
IG(V, W) = H(V) - H(V \mid W)
$$
Da $H(V)$ an einem Knoten immer Konstant ist bietet diejenige Entscheidung den höchsten Information Gain, bei der die [Bedingte Entropie](#Bedingte%20Entropie) am niedrigsten ausfällt.




> [!Example] Klausuraufgabe
> Entropie / Information Gain berechnen



