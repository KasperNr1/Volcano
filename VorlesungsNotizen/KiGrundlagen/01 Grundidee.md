# Grundlegender Prozess
- Es gibt Daten
- Daten werden für Training eines Modells verwendet
- Modell kann Vorhersagen treffen

![](DataModelPrediction.png)

## Aufgabenarten
### Regression
Mit der Regression werden kontinuierliche Werte vorhergesagt. Es wird eine Mathematische Funktion angenähert.

![](Regression.png)

### Klassifikation
Messwerte sind Teil einer Gruppe. Das Modell ist in der Lage neue Werte in die bestehenden Gruppen einzuordnen.

![](Classification.png)

### Klassifikation
Das Modell erkennt Gruppen und Muster in einer unsortierten Menge an Messwerten

![](Clustering.png)


> [!Info] Überwachung
> Die Bereitstellung der erwarteten "Korrekten" Werte ist sehr aufwändig. Beispielsweise bei Captchas wird von Menschen genau markiert, welche Ergebnisse wünschenswert sind.
> Beim Clustering gibt es eine solche vorherige Klassifizierung nicht.
> Man spricht hier von einem unüberwachten Lernverfahren, während Regression und Klassifikation als überwacht beschrieben werden.  

## Ablauf
Bei Komplexeren Systemen, die beispielsweise Bilder als Eingabe verarbeiten, muss erst eine Reihe von "Kenngrößen" aus der Eingabe erstellt werden. Es wird nicht jeder Pixel an das Modell übergeben. 

Beispielsweise wird bei diesem System zur Erkennung von Fußgängern der Normalenvektor in jedem Bildbereich berechnet. Das System erhält so nur Informationen über die Kontrastreichen Teile des Bildes.
![](CarView.png)

Die Signale werden also erst bereinigt und überarbeitet, bevor die Kennwerte an die Modelle übergeben werden.

![](SensorToModellFlow.png)

# Regression
## Lineare Regression
Bei der Linearen Regression wird versucht eine Reihe Messwerte durch eine lineare Funktion anzunähern. Dabei wird der Unterschied zwischen jedem Mess- und Schätzwert quadriert. Die Summe dieser Fehler ist der "quadratische Fehler $E$ " 
$$
E = \sum_{i = 1}^{n}\left(y_{i} - \widehat{y_i}\right)^{2}
$$
Durch den Quadratischen Einfluss werden einige kleinere Abweichungen weniger schlimm bewertet als größere.

![](LinearRegression.png)

## Modellauswahl
#### Training vs Test
Die Modelle sollen in der Lage sein, auch mit Daten zu rechnen die nicht im Training enthalten waren. Man spricht von einer "Verallgemeinerungsfähigkeit"
Aus diesem Grund werden nur ca $75\%$ der Messdaten zum Training verwendet, während die restlichen $25\%$ zur Verifikation des Modells verwendet werden.
In der Regel werden die Daten zufällig in Training und Verifikation aufgeteilt. Bei besonders wenigen Messungen die manche Fälle eventuell vermehrt enthalten kann auch anders aufgeteilt werden.

#### Bestimmtheitsmaß
Das Bestimmtheitsmaß ist eine Angabe über die Qualität eines Modells. Es wird als Wert zwischen $0$ und $1$ angegeben, wobei eine $1$ perfekte Überdeckung mit den Messwerten bedeutet. Ein Bestimmtheitsmaß näher $0$ sagt aus, dass die Werte größere Abweichungen enthalten und nicht besonders akkurat sind.

Zur Berechnung des Bestimmtheitsmaßes vergleicht man das trainierte Modell mit einem (Schlechten) Vergleichsmodell. Bei Linearer Regression nimmt man hier meist den Mittelwert der Testdaten als konstante Ausgabe dieses Vergleichsmodells.

Man Berechnet den Fehler des trainierten und den des Vergleichsmodells.
$$
E_{\text{Trainiert}} = \sum (y_i - \hat{y_i})
$$
$$
E_{\text{Vergleich}} = \sum (y_i - \overline{y_i})
$$

Das Bestimmtheitsmaß $R^2$ berechnet sich nun wie folgt aus dem Verhältnis dieser beiden Werte:
$$
R^2 := 1 - \frac{\sum (y_i - \hat{y_i})}{\sum (y_i - \overline{y_i})} = 1 - \frac{E_{\text{Trainiert}}}{E_{\text{Vergleich}}}
$$

### Kreuzvalidierung
Wegen der zufälligen Aufteilung in Test- und Trainingsdaten werden Modelle nie exakt gleich trainiert. 

![](kFoldCrossValidation.png)

Um diese Schwankungen auszugleichen wird mit mehreren Durchgängen trainiert und bewertet. 

Ein Gängiges Verfahren ist die **k-fache Kreuzvalidierung** (k-fold Cross Validation)

![](kFoldDataSplit.png)

In diesem Beispiel wird das Modell nun 4 Mal mit unterschiedlichen Aufteilungen der Daten trainiert. Die resultierenden Score-Werte werden gemittelt um eine allgemeinere Aussage über die Qualität treffen zu können.

Für die finale Vorhersage wird ein $n+1$-tes Modell trainiert, indem alle Messdaten zum Training eingesetzt werden. Die Einzel-Scores der Test-Modelle dienen zur Abschätzung der insgesamten Modellqualität.
