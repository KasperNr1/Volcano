# Feed-Forward-Netze
Werden in den Encoder- und [Decoder](#Decoder)-Teilen der [Transformer](08%20Transformer.md#Transformer)-Architektur verwendet.
Dabei lernen die Netze Beziehungen zwischen den Eingabe- und Ausgabesequenzen.

## Residuenverbindungen
Auch "Skip-Verbindungen" umgehen Schichten in einem [Neuronalen Netz](07%20Neural%20Nets.md#Neural%20Nets) um einen einfacheren Informationsfluss zu ermöglichen.
In der Transformer Architektur werden solche Verbindungen im Encoder- und im Decoder Teil verwendet.

In tieferen Netzen wird so die Informationspropagation durch das Netz verbessert und somit die Lernfähigkeit erhöht.

![](SkipLayersInTransformer.png)

Das Lernen komplexer Zuordnungen zwischen Eingabe- und Ausgabesequenzen wird erleichtert, das Lernen allgemeiner Merkmale wird gefördert.
Modelle mit diesen Skip-Layern sind weniger zu Overfitting geneigt und verallgemeinern besser auf neuen Daten.

# Encoder
Wie auch der Decoder enthält der Encoder die folgenden Komponenten:
- [Multi-Head Attention Schichten](08%20Transformer.md#Attention%20Heads)
- [Feed-Forward-Netze](#Feed-Forward-Netze)
- [Residualverbindungen](#Residuenverbindungen)
- Layer Normalisierung

![](EncoderAndDecoder.png)

Der Encoder nimmt eine Sequenz von [Token](02%20N-Gramm.md#Token) als Eingabe und berechnet eine Sequenz von Vektoren, die eine Codierung der Eingabe darstellen.

Er besteht aus einem Stapel von $N$ identischen Schichten. Jede Schicht enthält folgende Sublayer:
- [Multi-Head Attention Schicht](08%20Transformer.md#Attention%20Heads)
- [Feed-Forward-NN-Schicht](#Feed-Forward-Netze)
- [Residualverbindungen](#Residuenverbindungen)

## Encoder: Feed-Forward-Netz-Schicht
Die Eingabe dieser Schicht besteht aus Vektoren, die aus der vorhergegangenen [Multi-Head-Self-Attention-Schicht](08%20Transformer.md#Attention%20Heads) stammen. In diesen Vektoren sind bereits Informationen über die Eingabesequenz enthalten.

Erst wird der Eingabevektor in einen höherdimensionalen Raum umgewandelt um mehr Kapazität für Repräsentationen zu erreichen.
In diesem Raum wird eine nicht lineare Transformation wie [ReLU](07%20Neural%20Nets.md#Aktivierungsfunktion) durchgeführt um auch komplexe Muster zu erkennen.
In einer zweiten Transformation wird der Vektor wieder auf seine ursprüngliche Dimension reduziert.
Ausgabe ist somit ein Vektor, der eine nicht-lineare Transformation widerspiegelt und an die nächste Schicht weitergegeben werden kann.

Nach jedem Sublayer (wie der Attention-Schicht oder dem FFN) wird die Eingabe des Sublayers mit seiner Ausgabe addiert.
Diese Addition ist die Anwendung der [Residualverbindung](#Residuenverbindungen).

## Layer-Normalisierung
Um die Trainingsstabilität zu verbessern wird dieser Schritt auf den Eingaben jeder Schicht angewandt.
Dabei wird der Mittelwert $\mu$ und die Standardabweichung $\sigma$ der Elemente des Eingabevektors berechnet.
Die Normalisierung erfolgt abhängig von beiden Zahlen:
$$
\text{Norm}(X) = \frac{X - \mu}{\sigma - \mathcal{E}}
$$

Durch die Normalisierung ist das Modell weniger empfindlich gegenüber den Initialisierungswerten und trainiert somit stabiler. 
Da die Eingaben jeder Schicht eine ähnliche Verteilung erhalten, kann die Konvergenz beschleunigt werden.


> [!Missing] Bookmark
> Hier weitermachen
> Skript Seite 518

# Decoder
Erhält als Eingabe die Ausgabe des Encoders, zusammen mit dem bisher generierten Ausgabetext.
Alle Generierten Wörter $0$ bis $i-1$ wird verwendet um Wort $i$ zu generieren.
Zu Beginn wird ein Token `<start>` übergeben, das Vorgehen wiederholt sich, bis ein spezielles Token `<eos>` (End Of Sequence) erzeugt wurde.

# Grenzen der Transformer
Hauptproblem ist die Skalierung des 'self-Attention-Mechanismus'. Da jedes Token mit jedem anderen kombiniert werden muss, liegt hier eine Quadratische Abhängigkeit in Größe und Rechenzeit vor.

## Optimierungsansätze
Effizientere Implementierung:
Bessere Soft- und Hardware zur Verarbeitung dieser (Matrix-) Berechnungen. Spezialisierte Techniken wie 'Batch-Verarbeitung' oder andere Algorithmen um die Speicherverwendung zu optimieren.

Sparse Attention Mechanismen:
Statt alle Kombinationen zu erlauben, reduziert dieser Ansatz die Zahl der erlaubten Kombinationen. Nur eine Teilmenge der Tokens wird miteinander in Beziehung gesetzt.
Für die genaue Einschränkung gibt es verschiedene Ansätze.
![](SparseAttention.png)

# Training von Transformern
Vielfältige Daten:
- Bücher
- Artikel
- Webseiten
- Dialoge

Hohe Qualität und Menge notwendig für effektives Lernen. 
Vermeidung von Verzerrungen durch ausgewogene Datensätze, diese müssen zuvor bereinigt und tokenisiert werden.

## Pretraining
Nutzung großer Mengen ungelabelter Daten für grundlegende Sprachmuster und Kontextinformationen.

## Fine-Tuning
Anpassung des vortrainierten Modells auf spezifische Anwendungen durch weiteres Training mit speziell gelabelten Daten. So wird die Leisungsfähigkeit und Genauigkeit bei einzelnen Aufgaben erhöht.

## Masked Language Modeling (MLM)
Training von Modellen um maskierte Wörter in einem Text zu erkennen und vorherzusagen.

Beispiel:
`Das Wetter ist <MASK>`, Modell sagt "schön"

Einfaches füllen eines Lückentextes. Ermöglicht das Erlernen kontextueller Beziehungen und semantischer Bedeutungen.

## Autoregressives Lernen
Modell sagt Tokens für das Ende der gegebenen Sequenz vorher. 
Wiederholte Anwendung kann ganze Texte generieren.

# BERT
Bidirectional Encoder Representation from Transcoders ist ein Vortrainiertes Modell von Google.

Bietet eine umfassende Kontextanalyse durch sein Vortraining mit [MLM](#Masked%20Language%20Modeling%20(MLM)).

Nach dem Vortraining kann das Modell auf spezifische Anwendungsarten trainiert werden

