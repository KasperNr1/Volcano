Hat das Ziel ein tieferes Verständnis für die Struktur und Funktion von Wörtern innerhalb der Sprache zu entwickeln.

# Lexikalische Einheit
Umfasst Wörter, Wortbestandteile und Affixe (Präfixe und Suffixe) sowie zusammengesetzte Wörter und Phrasen

## Lexikon einer Sprache
Ist ein Katalog aller [Lexikalische Einheiten](#Lexikalische%20Einheit) einer Sprache.

# Lexikalische Beziehungen
## Homonymie
## Polysemie
## Metonymie
## Synonyme und Antonyme
## Hyponyme

> [!Missing] Fehlt
> Nur wenig, Seite 257-259


# Komplexe Spracheinheiten
Ziel ist es, Informationen in formale Repräsenation zu transformieren. 
## Symbolische Repräsentation
Stellt Logische Formeln durch inferelle oder Graphenbasierte Mechanismen dar.

## Vektorielle Darstellung
![](WordVector.png)

Ordnet Wörter in einem hochdimensionalen Raum an, sodass Beziehungen als Abstände codiert werden. Beispielsweise ist der Verbindungsvektor zwischen Frankreich und Paris sehr ähnlich zu dem, der Deutschland und Berlin verbindet.

Diese Technik wird in aktuellen Modellen am häufigsten verwendet.


> [!NOTE] Word Sense
> Die Wortbedeutung ist entscheidend für die Position im [Vektorraum](Vektoren%20und%20Vektorräume.md). Bei [Homonymen](#Homonymie) würden beide Bedeutungen des Wortes separat im Raum positioniert werden.


# Word Sense Disambiguation (WSD)
Syntaktische Mehrdeutigkeit wird durch [PoS Tagging](03%20PartOfSpeech.md#PoS%20Tagging) aufgelöst, WSD ist für die semantische Mehrdeutigkeit zuständig.

Ein Problem für die WSD sind die Unterschiedlichen Definitionen von Wörtern in verschiedenen Wörterbüchern.

PoS Tagging basiert auf der unmittelbaren Umgebung von Wörtern während WSD auch weiter entfernte Kontexte berücksichtigen kann.


> [!NOTE] Inter-Judge Variance
> Beim Vergleich von WSD Ergebnissen mit menschlichen Einordnungen von Wörtern fallen Unterschiede auf.
> Allerdings werden die von Menschen Labels von äußeren Faktoren wie Stimmung, Tageszeit und persönlichen Vorlieben beeinflusst.
> 
> Menschen sind insgesamt besser in der groben Unterscheidung als in der feingranularen Analyse der Bedeutungen


## Methoden
### Wissensbasierte Methode
Rechnerisch Intensiv, benötigt aber keine Korpusevidenz.

#### Lesk-Methode
1. Für jedes Wort im Kontext werden alle möglichen Bedeutungen aus einem Wörterbuch extrahiert
2. Gemeinsame Wörter in den Definitionen des aufzulösenden Wortes und den umgebenen Wörtern
3. Die Bedeutung mit der größten Überlappung wird akzeptiert.

### Überwachtes Lernen
Intensive Rechenressourcen und Korpusevidenz

[SVM](05%20SVM.md#Support%20Vector%20Machines) kann eine Trennlinie zwischen den Bedeutungen eines Wortes finden. Hohe Genauigkeit wenn Trainingsdaten in ausreichender Menge vorhanden sind.


### Unüberwachtes Lernen
Unabhängig von Korpusevidenz und rechnerisch effizient

Keine Notwendigkeit für manuelle Annotation, die Bedeutung von Wörtern wird anhand von Ähnlichkeiten in Strukturen erkannt.

Da keine definierten Trainingsdaten vorhanden sind, kann hier die Genauigkeit des Modells nur schwer validiert werden.

### Semi-Überwachtes Lernen
Kombiniert geringere rechnerische Intensität mit Korpusevidenz

Kombiniert gelablelte und ungelablete Daten.
Beim "Bootstrapping" wird mit einer kleinen Menge Trainingsdaten gestartet und die Vorhersagen für unbekannte Wörter ebenfalls in die Trainingsdaten aufgenommen.

Hier besteht die Gefahr dass sich Fehler sehr großflächig  fortpflanzen können.

# Synsets
![](Synset.webp)

"Synonym Sets" sind Graphen die jeweils Synonyme mit einander verbinden

## Pfadbasierte Ähnlichkeit
Der Abstand in der Bedeutung zweier Wörter kann anhand der Abstände in einem Synset erkannt werden.

![](PathBasedWordDistance.png)

Jedes Wort hat zu sich selbst den Abstand $1$

Die Pfad-basierte Ähnlichkeit $\text{simpath}(c_1, c_2)$ von zwei Knoten berechnet sich wie folgt:
$$
\text{simpath}(c_1, c_2) = \frac{1}{\text{pathlen}(c_1, c_2)}
$$
Die Wortähnlichkeit berücksichtigt auch die verschiedenen Bedeutungen von Wörtern. Es wird die maximale Distanz aller Kombinationen von Definitionen verwendet.
$$
\text{wordsim}(w_1, w_2) = \max \left( \text{simpath}(c_1, c_2) \right) \qquad \forall c_1 \in \text{senses}(w_1), c_2 \in \text{senses}(w_2)
$$

Schwächen dieses Ansatzes sind die konstanten Abstände innerhalb des Graphen. 

# Term Dokument Matrix
Zeigt die Häufigkeit und Verteilung von Begriffen in einem Dokument.

Zeilen symbolisieren Wörter oder Begriffe die im Dokument vorkommen.
Spalten Repräsentieren Sätze oder Dokumente, die analysiert werden.
Zellen zeigen die Anzahl an Vorkommnissen eines Begriffs in einem Dokument.


|         | As you Like it | Twelfth Night | Julius Caesar | Henry V | Sherlock Holmes | Moby Dick |
| ------- | -------------- | ------------- | ------------- | ------- | --------------- | --------- |
| Battle  | 1              | 1             | 8             | 15      | 1               | 20        |
| Soldier | 2              | 2             | 12            | 36      | 0               | 4         |
| Fool    | 37             | 58            | 1             | 5       | 3               | 7         |
| Trick   | 1              | 3             | 1             | 1       | 3               | 3         |

Zwei Dokumente gelten als ähnlich, wenn sie ähnlich Wortverteilungen haben. Z.B. Julius Caesar und Henry V haben vergleichbare Worthäufigkeiten.

Einzelne Zeilen nennt man "Wort-Vektoren".
Zwei Wörter sind ähnlich, wenn sie ähnliche Wort-Vektoren haben.

## Metriken

> [!Missing] Fehlt
> Formeln und Algorithmen zur Word-Vektor-Erstellung auf Seite 308-318







