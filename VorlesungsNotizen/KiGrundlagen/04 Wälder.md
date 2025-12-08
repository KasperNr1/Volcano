# Bäume
[Entscheidungsbäume](03%20Entscheidungsbäume.md) neigen zu Überanpassung an die Trainingsdaten.

![](OverfittedTree.png)

Das liegt daran, dass weitere Entscheidungsknoten angefügt werden, bis diese nur noch eine Klasse von Objekten enthalten.

## Einschränkungen
Es gibt unterschiedliche Möglichkeiten die Bäume zu beeinflussen. Die simpelsten sind eine Begrenzung der Tiefe oder der Anzahl an verwendeter Knoten.

Auch die Anzahl an Beispielen pro Knoten kann angehoben werden. So wird verhindert, dass wegen einem potentiell fehlerhaft gelabeltem Datum tiefe Unterbäume entstehen.

![](OptimizedTree.png)

In diesem Bild wurden Entscheidungsgrenzen nur dann gezogen, wenn sich mindestens drei Datenpunkte in den entsprechenden Bereichen befinden.

# Speichern
Modelle können auch als Datei gespeichert und übergeben werden. Dazu verwendet Python die Bibliothek "Pickle".
``` Python
import pickle

file_name = "Modell.pickle"
pickle.dump(model, open(file_name, "wb"))
```

In einem anderen Programm kann das Modell entsprechend wieder eingelesen werden

``` Python
import pickle

filename = "Modell.pickle"
model = pickle.load(open(filename, "rb"))

model.predict(data) #Kann wie erwartet verwendet werden
```


# Bewertung von Klassifikatoren
Die [Güte](01%20Grundidee.md#Bestimmtheitsmaß) eines Klassifikators wird mit `model.score()` ausgegeben und beschreibt den Anteil der korrekt klassifizierten Eingaben. 

Bei Unbalancierten Datensätzen ist die Trefferquote alleine jedoch kein gutes Gütemaß


> [!Info] Balancierte Datensätze
> Ein Datensatz heißt balanciert, wenn von allen Klassen eine vergleichbare Anzahl Einträge existieren.
> Die Verteilung von `Kopf` und `Zahl` bei einem Münzwurfexperiment ist  balanciert.
> 
> Unbalanciert hingegen ist die Verteilung von gültiger und betrügerischer Kreditkartentransaktionen.
> Hier liegt das Verhältnis bei ca. $99,98 \%$ zu $0,02 \%$
> 
> Ein Klassifikator der immer `gültig` zuordnet hätte so eine Trefferquote von $99,98 \%$, ohne einen einzigen Betrug zu erkennen. 

## Konfusionsmatrix
$$
\begin{array}{c | c | c}
\begin{array}{c c c}
\diagdown & & \text{Actual} \\
& \diagdown & \\
\text{Prediction} & & \diagdown
\end{array}
& \text{Positiv} & \text{Negativ} \\ \hline
\text{Positiv} & \text{True Positive} & \text{False Positive} \\ \hline
\text{Negativ} & \text{False Negative} & \text{True Positive}
\end{array}
$$

Aus diesen Werten lassen sich verschiedene Gütemaße berechnen.


> [!Info] Sensitivität
> Auch "True-Positive-Rate" oder "recall" beschreibt den Anteil der korrekt erkannten Gut-Teile
> $$
> \text{Recall} = \frac{\text{True Positive}}{\text{True Positive} + \text{False Negative}}
> $$

> [!Info] Spezifizität
> Auch "True-Negative-Rate" beschreibt den Anteil der korrekt erkannten Schlecht-Teile
> $$
> \text{Spezifizität} = \frac{\text{True Negative}}{\text{True Negative} + \text{False Positive}}
> $$

Auch die Trefferquote lässt sich leicht ermitteln

$$
\text{Trefferquote} = \frac{\text{True Negative} + \text{True Positive}}{\text{False Negative} + \text{False Positive} + \text{True Negative} + \text{True Positive}}
$$

Analog lässt sich auch die Fehlerrate bestimmen.

### Balancierte Fehlerrate
Sie wird häufig bei stark unbalancierten Datensätzen verwendet. Dabei besteht ihr Wert aus dem [Arithmetischen Mittel](Folgen.md#Arithmetisches%20Mittel) der einzelnen Fehlerraten.

$$
\begin{array}{c | c | c}
& \text{Positiv} & \text{Negativ} \\ \hline
\text{Positiv} & 120 & 20 \\ \hline
\text{Negativ} & 40 & 20
\end{array}
$$
In diesem Beispiel würde die BER folgendermaßen berechnet:
1. False Positive: $\frac{20}{20 + 20} = 50\%$
2. False Negative: $\frac{40}{120+40} = 75\%$
3. Mittelwert: $\frac{75 + 50}{2} = 62,5\%$

# Ensemble Learning
Da einzelne [Bäume](#Bäume) zu Überanpassung neigen wird eine Reihe unterschiedlicher Bäume erzeugt. Dieser "Wald" entscheidet dann per Mehrheit über das Gesamtergebnis.

Grundsätzlich wird zwischen zwei Varianten unterschieden.
Beim **Bagging** werden alle Daten gleich wahrscheinlich ausgewählt. Jeder Baum erhält zum Training eine Teilmenge des gesamten Datensatzes.
Beim **Boosting** werden die Bäume sukzessive trainiert. Daten die von früheren Bäumen öfter falsch klassifiziert werden, tauchen im Training der späteren öfter auf.

## Random Forests
Um die Varianz zwischen den einzelnen Bäumen zu steigern werden bei diesem Ansatz zufällige Attribute der Daten für einzelne Bäume ignoriert. Wenn ein Attribut mit großer [Entropie](03%20Entscheidungsbäume.md#Entropie) wegfällt, wird anhand eines anderen Merkmals entschieden. Die Vorhersage einzelner Bäume wird etwas schlechter, die Entscheidung der Mehrheit profitiert in der Regel.

## Bewertung
### Vorteile
Keine Vorverarbeitung der Daten notwendig, kann gut als erste Analyse eingesetzt werden.

Keine Probleme mit hochdimensionalen Eingabedaten

Durch die Abstimmungsergebnisse erhält man ein Maß für die "Confidence"

### Nachteile
Es ist ein höherer Rechenaufwand erforderlich.

Die Ergebnisse sind nicht so einfach visualisier- oder nachvollziehbar wie bei einzelnen [Bäumen](#Bäume)

# Naiver Bayes
Dieses Klassifikationsverfahren basiert auf Wahrscheinlichtkeiten. Es berechnet für einen neuen Datenpunkt die Wahrscheinlichkeit mit der er zu jeder Klasse gehört und gibt die zurück, bei der die Wahrscheinlichkeit maximal ist.

![](NaiverBayes.png)

Um diese neue Messung zu klassifizieren müssen also zwei Wahrscheinlichkeiten berechnet werden:
- $P(\text{Lachs} \mid \text{Helligkeit = 7, Länge = 10})$
- $P(\text{Barsch} \mid \text{Helligkeit = 7, Länge = 10})$

Durch den [Satz von Bayes](02%20Modellauswahl.md#Satz%20von%20Bayes) kann man diese Wahrscheinlichkeit auch folgendermaßen ausdrücken
$$
P(\text{Klasse}_i \mid \text{H. = 7, L. = 10}) = \frac{P(\text{Klasse}_i) \cdot P(\text{H. = 7, L. = 10} \mid \text{Klasse}_i)}{P(\text{H. = 7, L. = 10})}
$$
Da der Nenner unabhängig von der betrachteten Klasse ist und wir nur die relativen Größenverhältnisse der unterschiedlichen Wahrscheinlichkeiten berechnen wollen, kann er ignoriert werden um die Berechnung zu vereinfachen.

Die Wahrscheinlichkeiten für das Auftreten einzelner Klassen können aus den Trainingsdaten abgeschätzt werden.
$$
P(\text{Barsch}) \approx \frac{\text{Anzahl Barsche}}{\text{Anzahl Fische}}
$$
Falls die Kenngrößen [stochastisch Unabhängig](Stochastisch%20unabhängige%20Zufallsvariablen.md#Definition%20Stochastische%20Unabhängigkeit) von einander sind kann man folgende Vereinfachung durchführen um die [Mehrdimensionale Verteilung](Mehrdimensionale%20Verteilungen.md#Mehrdimensionale%20Verteilungen) aufzulösen:
$$
P(\text{H. = 7, L. = 10} \mid \text{Klasse}_i) = P(\text{H. = 7} \mid \text{Klasse}_i) \cdot P(\text{L. = 10} \mid \text{Klasse}_i)
$$
Namensgebend für den Klassifikator ist die Naive Annahme, dass die Variablen immer unabhängig voneinander sind. Ebenfalls wird davon ausgegangen, dass sich die einzelnen Kriterien der Objekte jeweils durch eine [Verteilungsfunktion](Zufallsvariablen.md#Definition%20Verteilungsfunktion) beschreiben lassen.

## Bewertung Naiver Bayes
Das Verfahren ist simpel und funktioniert auch mit nur wenigen Trainingsdaten. Auch bei Hochdimensionalen Eingaben ist die Technik anwendbar.
Jedoch sind die getroffenen Annahmen oftmals nicht gegeben, was zu einer Ungenauigkeit der Ergebnisse führt.


