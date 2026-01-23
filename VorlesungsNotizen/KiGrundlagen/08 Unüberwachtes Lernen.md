# Dimensionsreduktion
Oft möchte man Daten visualisieren die eine sehr große Anzahl Dimensionen enthalten. 
Um sie besser darstellbar zu machen, werden die Daten in einen Raum projiziert der eine geringere Anzahl Dimensionen besitzt. Eine Herausforderung 
dabei ist der Erhalt von Abständen. 

![](ProjectionLostDistance.png)

Man soll auch in der Projektion abschätzen können, wie nah die Daten im Ursprungsraum beieinander liegen.
Bei einer Abstandserhaltenden Projektion ist dies der Fall. Die Abstände von Datenpunkten sind in Ausgangs- und Zielraum ungefähr vergleichbar.

![](ProjectionKeptDistance.png)

## Multi-Dimensional-Scaling
Das MDS ist ein sehr robustes Verfahren zur abstandserhaltenden Projektion.
Es beruht auf dem [SMACOF-Algorithmus](https://en.wikipedia.org/wiki/Stress_majorization). 
Er eignet sich sehr gut um kleine bis Mittelgroße Datensätze darzustellen, wird bei größeren Datenmengen aber langsam. Bei Daten mit sehr vielen Dimensionen leidet auch die Qualität der Ergebnisse.

- **Eingabe**:
  Eine $n\times n$ Unähnlichkeitsmatrix $\delta$ mit den paarweisen Abständen aller Punkte im Ausgangsraum
- **Ziel**:
  Die Punkte sollen im 2D-Raum so verteil sein, dass ihre paarweisen Abstände den Abständen im Ausgangsraum entspricht
- **Ablauf**:
  Die Punkte werden verteilt und die Ungleichheit der Abstände berechnet. Durch mehrere Iterationen wird versucht diese Ungleichheit zu minimieren

``` Python
# Da Der Algorithmus mit Abständen arbeitet
# Müssen die Daten erst skaliert werden
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_transformed = scaler.fit_transform(X)

# Hier findet die eigentliche
# Transformation statt
from sklearn.manifold import MDS
mds = MDS(n_components=2, # Dimension des Zielraumes
			random_state=0)
X_2d = mds.fit_transform(X_transformed)
```

MDS wird oft eingesetzt um sich einen Überblick über Daten zu verschaffen. Man kann erkennen, wie gut sich Klassen separieren lassen.
Beispielsweise lässt sich erkennen, dass die Grenzen des [Iris-Datensatzes](https://www.kaggle.com/datasets/uciml/iris/data) relativ klar sind.
![](IrisProjection.png)

## t-SNE
t-distributed Stochastic Neighbour Embedding ist besonders für große, hochdimensionale Datensätze geeignet.
Der Algorithmus ist nicht besonders stabil. Kleine Änderungen an den Parametern führen zu drastisch verschiedenen Projektionen.

### Schritt 1
Zwischen allen Punkten wird die Paarweise Ähnlichkeit bestimmt.

Diese Abstände werden auf einer [Normalverteilungsfunktion](Normalverteilung.md) um den betrachteten Punkt platziert. So wird die "Unskalierte Ähnlichkeit" berechnet.
![](TSneSimilarity.png)

Nah gelegene Werte erhalten so eine große Ähnlichkeit, während weiter entfernte deutlich weniger ähnlich bewertet werden.
![](TSneSimilarity2.png)

Nachdem so die Ähnlichkeit zu allen Datenpunkten berechnet wurde, werden die Ergebnisse so skaliert, dass ihre Summe $1$ ergibt.
So werden die Abstände zwischen den Punkten irrelevant. Auch wenn der ähnlichste Punkt weit entfernt liegt, erhält er einen großen Wert im Vergleich zu den noch weiter entfernten, weniger ähnlichen Punkten.

Nachdem dies für alle Punkte wiederholt wurde, erhält man eine Ähnlichkeitsmatrix.
![](TSneMatrix.png)

### Schritt 2
Die Punkte werden initial zufällig im Zielraum verteilt.

Hier werden auch wieder die Abstände bestimmt, diesmal jedoch mit der "Student-t-Funktion"
In vielen kleinen Schritten werden die Punkte im Zielraum verschoben. Dabei soll die Ähnlichkeitsmatrix im Zielraum möglichst ähnlich zu der im Ausgangsraum werden.

> [!Info] Student-t-Funktion
> Die Funktion ähnelt der [Normalverteilung](Normalverteilung.md#Die%20Gauß'sche%20Normalverteilung), ist jedoch weniger spitz. Somit werden Werten die weiter abseits der Mitte liegen etwas größere Werte zugeordnet.
>
> [Wikipedia](https://de.wikipedia.org/wiki/Studentsche_t-Verteilung)
> 
  ![StudendVsNormal](StudendVsNormal.png) 

---

In Python wird der Algorithmus folgendermaßen angewandt

``` Python
from sklearn.manifold import TSNE
tsne = TSNE(n_components=2, # Dimensionen im Zielraum
			random_state=0, # Seed der Zufallsverteilung
			perplexity=50)  # Bestimmt skalierung (Viele Daten -> Viel Perplexity)

X_2d = tsne.fit_transform(X)
```

# Clustering
Beim unüberwachten Lernen haben wir eine große Menge Daten ohne Label. Ziel ist es, Ähnlichkeitsstrukturen (Cluster) zu erkennen.

Punkte in einem Cluster sollen ähnlich zu einander und unähnlich zu anderen Punkten sein.

## K-Means
Ein sehr simples und performantes Verfahren um eine vorgegebene Anzahl von Cluster zu identifizieren.

1. Man wählt die Menge der Cluster $k$.
2. Man wählt genau $k$ Centroiden (Anfangspunkte)
3. Jeder Datenpunkt wird dem nächstgelegenen Centroid zugeordnet
4. Alle Centroiden werden so verschoben, dass sie im Zentrum ihrer Punktemenge liegen
5. Falls sich mindestens ein Centroiden verändert hat, wird wieder bei Schritt 3. eingestiegen.

``` Python
# Daten erst skalieren da mit Abständen gearbeitet wird
from sklear.preprocessing import StandardScaler
scaler = StandardScaler()
X_transformed = scaler.fit_transform(X)

# K-Means
from sklearn.cluster import KMeans
model = KMeans(n_clusters = 3)
model.fit(X_transformed)
labels = model.labels_ # Liefert eine Liste mit Labels (Cluster-ID) zu jedem Punkt
```


> [!Warning] Problem
> Man muss vorher bereits wissen, wie viele Cluster enthalten sind, bzw. auf wie viele die Datenmenge aufgeteilt werden soll.
> 
> Um hier ein Optimum zu bestimmen, experimentiert man mit verschiedenen Größen von $k$ und trägt den [Mittelwert](Folgen.md#Arithmetisches%20Mittel) der [Quadratischen Fehler](01%20Grundidee.md#Lineare%20Regression) in einem Diagramm auf.
> 
> ![ElbowMethod.png](ElbowMethod.png)
>
> Der Knick im Diagramm ist ein guter Kandidat für eine korrekte Anzahl Cluster. Reale Daten haben teilweise mehrere Knicke, es bietet sich an die entsprechende Menge an Cluster zu verwenden und die Ergebnisse zu vergleichen. 
