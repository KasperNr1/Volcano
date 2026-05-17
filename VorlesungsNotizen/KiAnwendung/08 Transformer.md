Transfer Learning gilt als Schlüssel zur Leistungsfähigkeit großer Sprachmodelle.

# Transfer Learning in LLMs
![](TransferLearningStepsInLlm.png)

Beim Finetuning werden ggf. Firmeninterne Dokumente zum Training verwendet. So kann sich ein Modell an den Kontext bestimmter Aufgaben anpassen.

Transfer Learning ist deutlich effizienter als Modelle für jeden Kontext von Grund auf neu zu trainieren. Das teure Basismodell kann flexibel auf verschiedene Aufgaben spezialisiert werden.

Mit diesem Ansatz ist es lohnenswert das Basismodell mit mehr Daten zu trainieren, da es für verschiedene Aufgaben weiterverwendet werden kann.
![](TransferLearningTraningData.png)

Beispielsweise könnte ein auf Buchrezensionen trainiertes Basismodell auf Filmrezensionen spezialisiert werden, da die Anwendungen ähnlich sind.

# Randwahrscheinlichkeit
Die [Randwahrscheinlichkeit](Mehrdimensionale%20Verteilungen.md#Mehrdimensionale%20WS-Verteilungen) beschreibt die Wahrscheinlichkeit eines Datenpunktes zu einer bestimmten Klasse zu gehören, unabhängig von anderen Parametern.

$P(\text{Katze})$ Ist die Wahrscheinlichkeit dass ein zufällig ausgewähltes Bild eine Katze zeigt, ohne weitere Merkmale zu beachten.

# Transfer Learning
## Homogenes Transfer Learning
Quell- und Zieldomäne haben ähnliche Aufgaben und Daten. Die erlernten Merkmale und Strukturen lassen sich effizienter übertragen und liefern mit kleinen Anpassungen bereits gute Resultate.

## Heterogenes Transfer Learning
Hier sind Daten und Aufgaben sehr verschieden. Beispielsweise wenn ein Basismodell auf die Klassifikation von Bildern trainiert wurde und nun zur Generierung von Texten genutzt werden soll.

Die Unterschiede erschweren die Anwendbarkeit des Basismodells, es sind umfangreiche Anpassungen nötig.


> [!Info] Warum ist das besser als eine untrainiertes Modell?
> Auch wenn die Art der Aufgaben sehr unterschiedlich ist, kann ein Teil der Muster übereinstimmen. 
> Beim weiteren Training kann eine Art "Converter" entstehen um die zunächst inkompatiblem Formate an Informationen ineinander zu wandeln

## Domänenunterschiede
Die Unterschiede zwischen den Domänen werden mit vier grundlegenden Ansätzen reduziert.

- Instanzbasiert
- Merkmalbasiert
- Parameterbasiert
- Relationalbasiert

### Instanzbasiert
Proben aus der Quelldomäne werden durch Gewichtung angepasst um sie in der Zieldomäne besser nutzen zu können.
Die Datenpunkte werden als unterschiedlich gewichtet, entsprechend ihrer Anwendbarkeit für die Zieldomäne.

Diese Strategie ist Modell- und Datentypsunabhängig. Sie lässt sich sehr gut an verschiedene Aufgaben anpassen.

### Merkmalbasiert
Modifikation einer Domäne um die Lücke zwischen Quelle und Ziel zu verringern. Anwendbar wenn die Zielvariablen identisch sind.

Asymmetrische Merkmalsumwandlung (Für Sentiment-Analyse):
Beispielsweise die Wandlung eines auf Filmrezensionen trainierten Modells auf Produktbewertungen. Das Modell soll in beiden Fällen die Stimmung der Kunden aus den Bewertungen erkennen.

Symmetrische Merkmalsumwandlung (Für Dokumentenklassifikation):
Trainiert auf Nachrichten, soll auch mit wissenschaftlichen Artikeln arbeiten.
Es werden beide Domänen in einen gemeinsamen Merkmalsraum transformiert (symmetrisch)

### Parameterbasierte Methoden
Basiert auf der Annahme, dass ähnliche Aufgaben auch ähnliche Modellstrukturen aufweisen.
Wissen wird übertragen, indem Parameter zwischen den Modellen der Quell- und Zieldomäne geteilt werden.

![](TransferLearningParameterBased.png)

### Relationalbasierte Methoden
Relationale Methoden übertragen Wissen, indem sie Muster in den Strukturen von Quell- und Zieldaten erkennen. Trotz Unterschiede in den Inhalten selbst können die Beziehungen ähnlich sein.

![](RelationalBasedMethod.png)


# Rekurrente Neuronale Netze (RNNs)
Sprache enthält einen fundamentalen Aspekt der Zeit. Sowohl gesprochene Sprache, als auch schriftliche Texte enthalten eine zeitliche Reihenfolge.
Bisher beschriebene Modelle berücksichtigen diesen Aspekt nicht, alle Eingaben werden gleichzeitig verarbeitet.

Bei [Feed-Forward Netzen](07%20Neural%20Nets.md#Neural%20Nets) wird mit einem Sliding-Window gearbeitet, damit nur eine begrenzte Anzahl von Wörtern betrachtet wird um Vorhersagen zu treffen.

In RNNs ist ein Mechanismus integriert, der direkt mit der sequenziellen Natur der Sprache umgeht und sie ohne willkürlich festgelegten Fenstergrößen behandelt. 
Durch Rückkopplung können sie vorherige Kontexte repräsentieren, somit können Entscheidungen auch aufgrund von vorherigen Entscheidungen getroffen werden.

![](RnnCycle.png)

Typische Anwendung von RNNs sind
- Sprachmodellierung:
  Vorhersage von Wortfolgen basierend auf vorherigem Text
- Textklassifikation
  Aufgaben wie Sentimentanalyse
- Sequenzmodellierung
  Aufgaben wie [PoS Tagging](03%20PartOfSpeech.md#PoS%20Tagging)

Die zyklische Struktur mach RNNs besonders leistugsstark bei der Verarbeitung zeitlicher Daten, birgt jedoch auch einige Herausforderungen.
Die Struktur erschwert das Verständnis der Funktionsweise des Netzwerks.
Auch das Training ist schwieriger, da bei besonders langen Sequenzen der [Gradient](07%20Neural%20Nets.md#Gradientenabstieg) verschwinden oder explodieren kann (Diminishing and Exploding Gradients)

## Elman-Netze
Auch "einfache rekurrente Netze" sind eine eingeschränkte Architektur die sich für die Sprachverarbeitung als äußerst effektiv erwiesen haben.

![](ElmanNetsVsFullyConnectedRnn.png)

Links dargestellt ist ein Elman-Netz, bei dem nur die [Neuronen](07%20Neural%20Nets.md#Neuronen) in einer versteckten Schicht rekurrent verbunden sind. Rechts in der Abbildung ist ein vollständig verbundenes rekurrentes neuronales Netz dargestellt.
Da deutlich weniger Verbindungen vorhanden sind ist das Training und die Nachvollziehbarkeit von Ergebnissen erleichtert.

Bei der Berechnung eines Ergebnis werden dabei die neuen Eingaben mit Informationen aus vorherigen Zeitpunkten kombiniert.
Dabei kann der Kontext bis zum Beginn der Sequenz zurückreichen.

![](RecurrentNeuralNet.png)

Um $h_t$ zu berechnen, wird der Eingang $x_t$ mit der Gewichtsmatrix $W$ multipliziert und die versteckte Schicht des vorherigen Zeitschritts $h_{h-1}$ mit der Gewichtsmatrix $U$.
Diese Werte werden addiert und durch eine gewählte [Aktivierungsfunktion](07%20Neural%20Nets.md#Aktivierungsfunktion) $g$ geleitet um den Aktivierungswert der aktuellen versteckten Schicht $h_t$ zu erhalten.

$$
h_t = g(U \cdot h_{t-1} + W \cdot x_t)
$$
$$
y_t = f(V \cdot h_t)
$$

Um die Rekurrenz zu eliminieren kann man das Netz "entrollt" darstellen. 
![](UnrolledRnn.png)
In der Darstellung sind $x_i$ die jeweiligen Eingaben aus der Eingabesequenz.
Die $h_i$ sind das Feedback aus allen vorherigen Schritten.

### Wortschatz
Der Wortschatz $V$ eines Modells ist die [Menge](Intervalle%20und%20Mengen.md#Mengen) aller einzigartigen Wörter die verwendet werden.
Die Größe des Wortschatzes wird mit $|V|$ dargestellt. Sie gibt die Anzahl der in Trainings- und Testdatensatz vorkommenden Wörter an.

Dabei hat jedes Wort im Wortschatz ein zugehöriges [Embedding](#Embedding) die in der [Embedding Matrix](#Embedding%20Matrix) gespeichert ist. Die Dimension der Embedding ist in der Regel sehr viel kleiner als die Dimension des Wortschatzes selbst.


### Embedding Matrix
Repräsentiert die Einbettung der Wörter im Wortschatz. Jedes Wort wird durch einen [Vektor](Vektoren%20und%20Vektorräume.md#Vektoren) in einem kontinuierlichen Raum dargestellt.

Bei einem Wortschatz der Größe $|V|$ und einer Embedding-Dimensinon $d$ hat die Embedding-Matrix die Dimension $|V| \times d$.
Jede Spalte der Matrix stellt den Embedding Vektor eines bestimmten Wortes dar.

Bei der Verarbeitung einer Eingabesequenz wird der entsprechende Embedding-Vektor von jedem Wort abgerufen. 
Dabei haben ähnliche Worte auch ähnliche Vektoren, um semantische Beziehungen zu erfassen.
Während dem Training wird auch die Embedding-Matrix optimiert, um Beziehungen besser abzubilden. 
Die [Matrix](Matrizen.md#Definition) spielt dabei eine entscheidende Rolle um die diskreten Eingabeworte in stetige Zahlenwerte umzuwandeln, die für die Verarbeitung durch das [neuronale Netz](07%20Neural%20Nets.md#Neural%20Nets) notwendig sind.

### Architektur
Die Eingabe $X = (x_1, x_2, \dots, x_n)$ besteht dabei aus einer Reihe aus Wörtern $x_i$, jedes dargestellt als ein [One-Hot-Vektor](02%20Modellauswahl.md#One%20Hot%20Encoding) der Größe $|V|$.
Die [Embedding Matrix](#Embedding%20Matrix) $E$ enthält die Embeddings $e_t$ für alle Wörter $x_t$. 
![](RnnArchitecture.png)
Das Embedding wird mit der Gewichtsmatrix $W$ multipliziert und zum versteckten Layer des vorherigen Schritts (gewichtet durch die Gewichtsmatrix $U$) addiert, um einen neuen versteckten Layer zu berechnen.
Der neue versteckte Layer wird verwendet, um eine Ausgabeschicht zu erzeugen, die durch eine Softmax-Schicht geleitet wird um eine [Wahrscheinlichkeitsverteilung](Einführung.md#Wahrscheinlichkeitmaß%20/%20Wahrscheinlichkeitsverteilung) über den gesamten Wortschatz zu generieren.
Die Wahrscheinlichkeit, dass das Wort am Index $k$ das nächste Wort ist, beträgt $\hat{y}_t[k]$ 

- $e_t = E \cdot x_t$
- $h_t = g(U\cdot h_{t-1} + W \cdot e_t)$
- $\hat{y}_t = \text{Softmax}(V \cdot h_t)$


> [!NOTE] Modell-Dimensionen
> Bei der Sprachmodellierung mit RNNs nehmen wir an, dass die Embedding-Dimension $d_e$ und die verborgene Dimension $d_h$ gleich sind. Wir bezeichnen beide als Modell-Dimension $d$

### Bewertung
RNNs sind besonders gut im Umgang mit Sequenzdaten, wie Sprache, Zeitreihen oder Musik.
Sie können Eingaben beliebiger Länge verarbeiten, was sie von den klassischen Neuronalen Netzen mit fester Eingabegröße abhebt.

Durch das Vanishing Gradient Problem haben diese Modelle teilweise Schwierigkeiten von langfristigen Abhängigkeiten zu lernen. Sie werden aufgrund ihrer Natur nicht parallelisiert trainiert, da jeder Schritt auf dem vorherigen aufbaut.
Auch neigen sie besonders zu Overfitting, insbesondere bei kleineren Datensätzen.


## Long Short-Term Memory (LSTM) Network
Ist eine besondere Art von RNN um das Problem der explodierenden oder verschwindenden Gradienten zu umgehen.
Bei längeren Sequenzen zeigt diese Architektur bessere Leistungen als ein naives RNN.

Es werden spezielle Speicherzellen eingesetzt, um Informationen auch über längere Zeiträume zu behalten.
Im Gegensatz zu klassischen RNNs wird eine innere Zelle und drei spezielle "Gates" eingesetzt.
- Eingangsgate
  Bestimmt wie stark ein neuer Wert in die Zelle einfließt
- Vergessensgate
  Bestimmt, wie viel eines Wertes in der Zelle verbleibt
- Ausgangsgate
  Kontrolliert, wie stark der Zellwert für die nächste Berechnung verwendet wird

![](LstmArchitecture.png)
![](LstmArchitectureForgetGate.png)

Alle Gates werden durch die Eingangsdaten aktiviert oder deaktiviert. Dabei werden ebenfalls Gewichte berechnet, die während dem Training angepasst werden.

Die Zustände des Gates werden aus den Vektoren $x_t$ und $h_{t-1}$ berechnet.
Dabei hat das Netz drei logische Eingaben:
- Die aktuelle Eingabe $x_t$
- Den bisherigen Verborgenen Zustand $h_{t-1}$
- Der Kontext-Wert $c_{t-1}$ aus der Speicherzelle

![](LstmCalculationGraph.png)

### Gate-Berechnungen
Jedes Gate ist ein Vektor. Es wird berechnet als die gewichtete Summe der Eingabedaten $x_t$ und $h_{t-1}$ die dann in eine [Aktivierungsfunktion](07%20Neural%20Nets.md#Aktivierungsfunktion) $\in \text{Abb}(\mathbb{R}^n \to \mathbb{R}^n)$ (z.b. Sigmoid) gegeben werden.

- Forget Gate: $f_t = \sigma(U_fh_{t-1} + W_fx_t)$
- Input Gate: $i_t = \sigma(U_ih_{t-1} + W_ix_t)$
- Output Gate: $o_t = \sigma(U_oh_{t-1} + W_ox_t)$

Dabei sind mit $U$ und $W$ jeweils die beim Training erlernten Gewichtsmatrizen gemeint.


Bei jeder Berechnung werden zuerst die eigentlichen Eingabedaten aus dem neuen Input und dem bisherigen Zustand berechnet.
$$
g_t = \tanh (U_gh_{t-1} + W_gx_t)
$$
Es wird der Kontextzustand aktualisiert um die neuen Informationen zu berücksichtigen
$$
c_t = f_t \odot c_{t-1} + i_t \odot g_t
$$

Schließlich wird der neue verborgene Zustand $h_t$ unter Verwendung des aktuellen Kontextzustands und des neuen Output Gates berechnet
$$
h_t = o_t \odot \tanh (c_t)
$$
Hier sind $U_g$ und $W_g$ wieder trainierte Matrizen.
Das Symbol $\odot$ steht führ die elementweise Multiplikation zweier Vektoren. (["Hadamard-Produkt"](Vektoren%20und%20Vektorräume.md#Rechenoperationen)) 


## Gated Recurrent Unit (GRU)
> [!Missing] Fehlt
> Seite 476 bis 479


# Transformer
Bestehen aus zwei Hauptkomponenten, Encoder und Decoder.

![](TransformerEncoderDecoder.png)

Sie wandeln jeweils von oder in eine interne Informationsdarstellung um.

## Attention-Mechanismus
Mit Attention können Modelle bestimmte Teile der Eingabe stärker gewichten. Dadurch bleibt der Fokus auf relevanten Informationen.

Welche Teile im Fokus stehen hängt dabei von der Eingabe selbst ab.

### Self-Attention
1. Eingaberepräsentation
   Jedes Wort oder Token wird als Vektor dargestellt. Dieser wird typischerweise aus Einbettungen abgeleitet
2. Abfrage-, Schlüssel- und Wertvektoren
   Für jedes Wort der Eingabe werden drei Vektoren erzeugt
	1. Abfragevektor $Q$
	   Repräsentiert das Wort für das Informationen gefunden werden sollen
	2. Schlüsselvektor $K$
	   Repräsenstiert potentielle Wörter, die relevante Informationen liefern könnten
	3. Wertvektor $V$
	   Enthält die tatsächlichen Informationen die aus den Attention Scores aggregiert wurden
3. Berechnung der Attention-Scores
   Der Attention Score zwischen einem Abfragevektor und allen Schlüsselvektoren wird in der Regel durch ein Skalarprodukt berechnet.
   Der Score misst dabei die Ähnlichkeit zwischen einer Abfrage und einem Schlüssel
4. Normalisierung der Werte mit Softmax
   Die Werte werden vor der weiteren Verarbeitung normalisisert
5. Gewichtete Summe der Wertvektoren
   Endgültiger Output für jedes Wort wird als gewichtete Summe der Wertvektoren berechnet. Gewicht sind dabei die Aufmerksamkeitswerte

#### Embedding
Eingabewörter werden in Vektoren umgewandelt.


> [!Missing] Title
> Seite 492-493

#### Einzelschritte: Query, Key und Value
Diese Vektoren werden verwendet um die Wichtigkeit des Tokens im Verhältnis zu anderen Tokens zu bestimmen. Dabei werden alle drei Vektoren gleichzeitig für alle Eingaben berechnet, indem der Eingabetensor mit lernbaren Gewichtsmatrizen multipliziert wird.

Jede Zeile des resultierenden Tensors entspricht dabei dem Vektor eines Eingabetokens.

#### Attention Score
Man berechnet das Skalarprodukt zwischen jedem Abfrage- und jedem Schlüsselvektor. Anschließend werden die Werte mit "SoftMax" normalisiert.
Diese Operation wird als Matrixmultiplikation der $Q$ und $K$ Tensoren realisiert. Jeder Wert der Ausgabematrix entspricht einem Skalarprodukt.

![](AttentionScoreCalculation.png)

Die Werte in der Produktmatrix werden durch $\sqrt{d_k}$ geteilt um die Größe der Zahlen zu begrenzen.
Dabei ist $d_k$ die Dimension des Key-Vektors. (Also die Anzahl Spalten der untransponierten $K$-Matrix)

#### Attention Heads
Sind eine Möglichkeit gleichzeitig mehrere Aspekte der Eingabedaten zu analysieren.

- Lernfähige Gewichtsmatrizen
  Jeder Head besitzt eigene Gewichtsmatrizen die beim Training optimiert werden.
- Parallele Verarbeitung
  Die Berechnungen lassen sich gleichzeitig ausführen
- Vielfältige Informationsaufnahme
  Verschiedene Merkmale können fokussiert werden. (Syntax / Semantik)
- Aggregation der Resultate
  Ausgabe aller Heads werden zusammengeführt um eine umfassende Repräsentation zu erzeugen.
- Erweiterte Modellkapazität
  Mehrere Heads erhöhen die Fähigkeiten des Modells, ohne die Gesamtzahl der Parameter stark zu erhöhen




