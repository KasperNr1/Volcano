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
Sie wird häufig bei stark unbalancierten Datensätzen verwendet. Dabei besteht ihr Wert aus dem [Arithmetischen Mittel](Folgen.md#Arithmetisches%20Mittel) der einzelnen Trefferquoten.

$$
\begin{array}{c | c | c}
& \text{Positiv} & \text{Negativ} \\ \hline
\text{Positiv} & 120 & 20 \\ \hline
\text{Negativ} & 40 & 20
\end{array}
$$
In diesem Beispiel würde die BER folgendermaßen berechnet:
1. Trefferquote Positiv: $\frac{120}{120 + 40} = 75\%$
2. Trefferquote Negativ: $\frac{20}{20+20} = 50\%$
3. Mittelwert: $\frac{75 + 50}{2} = 62,5\%$
