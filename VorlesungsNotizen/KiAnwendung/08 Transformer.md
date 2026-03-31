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

> [!Missing] Fehlt
> Seite 436-437


# Rekurrente Neuronale Netze

> [!Missing] Fehlt
> Seite 441 bis 475


# Gated Recurrent Unit (GRU)
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




