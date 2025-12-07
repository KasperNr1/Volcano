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
