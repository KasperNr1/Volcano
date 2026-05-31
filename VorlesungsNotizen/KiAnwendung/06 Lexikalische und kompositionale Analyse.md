Hat das Ziel ein tieferes Verständnis für die Struktur und Funktion von Wörtern innerhalb der Sprache zu entwickeln.

# Lexikalische Einheit
Umfasst Wörter, Wortbestandteile und Affixe (Präfixe und Suffixe) sowie zusammengesetzte Wörter und Phrasen

## Lexikon einer Sprache
Ist ein Katalog aller [Lexikalische Einheiten](#Lexikalische%20Einheit) einer Sprache.

# Lexikalische Beziehungen
Manche Wörter stehen in festen Beziehung zueinander.
Im folgenden sind einige der Beziehungsarten gelistet.
## Homonymie
Wörter die gleich klingen, aber verschiedene Bedeutungen haben

> [!Quote] Beispiel
> "Bank" als Geldinstitut vs. "Bank" als Sitzgelegenheit

## Polysemie
Mehrdeutigkeiten desselben Wortes

> [!Quote] Beispiel
> "Kopf" kann das Körperteil bedeuten, oder den Anführer einer Gruppe meinen

## Metonymie
Übertragung der Bedeutung durch Assoziation

> [!Quote] Beispiel
> "Das Weiße Haus" als Begriff für die US-Regierung

## Synonyme und Antonyme
Wörter mit sehr ähnlicher oder gegenteiliger Bedeutung

> [!Quote] Beispiel
> "Auto" oder "Fahrzeug" als Synonyme,
> "Heiß" und "Kalt" als Antonyme

## Hyponyme und Hypernyme
Unter- und Oberbegriffe

> [!Quote] Beispiel
> "Apfel" als Hyponym von "Frucht"
> "Frucht" als Hypernym von "Apfel"

# Komplexe Spracheinheiten
Die Bedeutung von Aussagen basiert neben der Bedeutung der einzelnen Wörter auch auf ihren syntaktischen Verbindungen.

`Andrew likes Jane` $\to \text{likes}(Andrew, Jane)$ 
`Jane likes Andrew` $\to \text{likes}(Jane, Andrew)$  

Nur durch Ändern der Reihenfolge erhält der Satz eine andere Bedeutung.
Ziel ist es, die Informationen in formale Repräsenationen zu transformieren. 

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
2. Gemeinsame Wörter in den Definitionen des aufzulösenden Wortes und den umgebenen Wörtern werden gezählt
3. Die Bedeutung mit der größten Überlappung wird akzeptiert.

Die Qualität der Ergebnisse hängt stark von der detailreiche der Definitionen im verwendeten Wörterbuch ab. Bei sehr komplexem Kontext kann die Genauigkeit ebenfalls sinken. 

### Überwachtes Lernen
Intensive Rechenressourcen und Korpusevidenz

Eine [SVM](05%20SVM.md#Support%20Vector%20Machines) kann eine Trennlinie zwischen den Bedeutungen eines Wortes finden. Hohe Genauigkeit wenn Trainingsdaten in ausreichender Menge vorhanden sind.

### Semi-Überwachtes Lernen
Kombiniert geringere rechnerische Intensität mit Korpusevidenz

Kombiniert gelablelte und ungelablete Daten.
Beim "Bootstrapping" wird mit einer kleinen Menge Trainingsdaten gestartet und die Vorhersagen für unbekannte Wörter ebenfalls in die Trainingsdaten aufgenommen.

Hier besteht die Gefahr dass sich Fehler sehr großflächig  fortpflanzen können.

### Unüberwachtes Lernen
Unabhängig von Korpusevidenz und rechnerisch effizient

Keine Notwendigkeit für manuelle Annotation, die Bedeutung von Wörtern wird anhand von Ähnlichkeiten in Strukturen erkannt.

Da keine definierten Trainingsdaten vorhanden sind, kann hier die Genauigkeit des Modells nur schwer validiert werden.

# Synsets
![](Synset.webp)

"Synonym Sets" sind Graphen die jeweils Synonyme mit einander verbinden

## Pfadbasierte Ähnlichkeit
Der Abstand in der Bedeutung zweier Wörter kann anhand der Abstände in einem [Synset](#Synsets) erkannt werden.

![](PathBasedWordDistance.png)

Jedes Wort hat zu sich selbst den Abstand $1$

Die Pfad-basierte Ähnlichkeit $\text{simpath}(c_1, c_2)$ von zwei Knoten berechnet sich wie folgt:
$$
\text{simpath}(c_1, c_2) = \frac{1}{\text{pathlen}(c_1, c_2)}
$$
Die Wortähnlichkeit berücksichtigt auch die verschiedenen Bedeutungen von Wörtern. Es wird die maximale Ähnlichkeit aller Kombinationen von Definitionen verwendet.
$$
\text{wordsim}(w_1, w_2) = \max \left( \text{simpath}(c_1, c_2) \right) \qquad \forall c_1 \in \text{senses}(w_1), c_2 \in \text{senses}(w_2)
$$

Schwächen dieses Ansatzes sind die konstanten Abstände innerhalb des Graphen. Daher werden Ähnlichkeiten zu abstrakteren Worten tendenziell immer als größer berechnet. 

# Term Dokument Matrix
Zeigt die Häufigkeit und Verteilung von Begriffen in einem Dokument.

Zeilen symbolisieren Wörter oder Begriffe die im Dokument vorkommen.
Spalten Repräsentieren Dokumente oder Sätze, die analysiert werden.
Zellen zeigen die Anzahl an Vorkommnissen eines Begriffs in einem Dokument.

|         | As you Like it | Twelfth Night | Julius Caesar | Henry V | Sherlock Holmes | Moby Dick |
| ------- | -------------- | ------------- | ------------- | ------- | --------------- | --------- |
| Battle  | 1              | 1             | 8             | 15      | 1               | 20        |
| Soldier | 2              | 2             | 12            | 36      | 0               | 4         |
| Fool    | 37             | 58            | 1             | 5       | 3               | 7         |
| Trick   | 1              | 3             | 1             | 1       | 3               | 3         |

Zwei Dokumente gelten als ähnlich, wenn sie ähnlich Wortverteilungen haben. Z.B. Julius Caesar und Henry V haben vergleichbare Worthäufigkeiten.

Einzelne Zeilen nennt man "Wort-Vektoren".
Zwei Dokumente sind ähnlich, wenn sie ähnliche Wort-Vektoren haben.

## Metriken
### Pointwise mutual Information (PMI)
Vergleicht die Wahrscheinlichkeiten dass zwei Ereignisse gemeinsam auftreten mit der Wahrscheinlichkeit, dass sie unabhängig erscheinen.
$$
\text{PMI}(x; y) = \log_2 \left( \frac{p(x,y)}{p(x) \cdot p(y)} \right)
$$
Dabei ist $p(x,y)$ die Wahrscheinlichkeit, dass die Wörter gemeinsam auftreten und $p(x)$ die Wahrscheinlichkeit der Wörter im Text vorzukommen.

Worte die nur gemeinsam auftreten erhalten große positive Werte, während Worte die nur selten oder nie zusammen auftreten mit kleineren oder negative Zahlen versehen werden.

#### Positive Pointwise Mutual Information (PPMI)
Ist eine Variante von [Pointwise mutual Information (PMI)](#Pointwise%20mutual%20Information%20(PMI)), wobei negative Werte ausgeschlossen durch $0$ ersetzt werden und somit ausgeschlossen sind.

$$
\text{PPMI}(x;y) = \max \left( \text{PMI}\left(x,y\right), 0 \right)
$$
Grund ist, dass mit negativen Werten in vielen Modellen nur schlecht umgegangen werden kann.
