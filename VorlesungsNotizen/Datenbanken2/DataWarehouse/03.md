# Data Mining
Wichtigste Verfahren sind
- [Clustering](#Clustering)
- [Klassifikation](#Klassifikation)
- [Assoziationsanalyse](#Assoziationsanalyse)

Beim Mining wird explorativ gearbeitet und nach neuen Mustern gesucht.

## Clustering
Objekte des selben Clusters sollen möglichst ähnlich sein, Objekte aus unterschiedlichen Clustern möglichst unterschiedlich.
Siehe auch [Clustering in der KI](01%20Grundidee.md#Clustering).

Anwendungsfälle sind beispielsweise innerhalb eines Online-Shops, wo anhand ähnlicher Kundenaktivität gewisse Werbekampagnen gestartet werden können.
Auch bei großen Textsammlungen kann Clustering helfen eine Ähnlichkeitssuche anzubieten. So müssen keine speziellen Schlüsselwörter gefiltert werden, wenn die Bedeutung des Textes enkodiert ist.

## Klassifikation
Gegeben sind eine Menge an Klassen $\{c_1, \dots, c_k\}$ und eine Menge an Daten. Für eine Teilmenge $I$ dieser Daten ist die Zugehörigkeit der Klassen bekannt.

Ein [Klassifikator](01%20Grundidee.md#Klassifikation) kann für alle Daten eine passende Klasse zuordnen.

## Assoziationsanalyse
Entdecken Assoziazionsregeln, also häufige Zusammenhänge. Klassisches Beispiel ist die Warenkorbanalyse, bei der häufig zusammen gekaufte Produkte analysiert werden.
![](Assoziazionsanalyse.png)

Zusätzlich werden zwei Kenngrößen "Support" und "Konfidenz" berechnet.
Für eine Assoziationsregel $X \to Y$ (z.B. $\{\text{Käse}\} \to \{\text{Butter}\}$) gilt:

Support:
$$
s(X \to Y) := \frac{\sigma(X \cup Y)}{|T|}
$$
Der Support ist also der Anteil aller Transaktionen die sowohl $X$ als auch $Y$ enthalten. Dabei ist nicht relevant, welche anderen Werte in den Einträgen vorkommen.

Für die Konfidenz gilt:
$$
k(X \to Y) := \frac{\sigma(X \cup Y)}{\sigma(X)}
$$
Also der relative Anteil an Transaktionen die beide Werte $X$ und $Y$ enthalten, gemessen an allen Transaktionen die $X$ enthalten.

![](SupportUndKonfidenzBeispiel.png)

> [!Example] Klausuraufgabe
> Support und Konfidenz für Aussagen über einen kleinen Datensatz ausrechnen

# Datenverarbeitung
Es gibt verschiedene Stufen der Datenverarbeitung. Diese sind in aufsteigend wertvoll für Unternehmen, allerdings auch aufsteigend komplexer werdend.

## Reports
Periodische Zusammenfassungen zu bestimmten Kennzahlen. Beispielsweise monatliche Auflistung der 20 besten Kunden.

## Dashboards
Dienen um bestehende Informationen sichtbar zu machen und einfache Kennzahlen zu berechnen.
Sie ermöglichen eine schnelle Erfassung des aktuellen Zustands.

## What-If-Analysis
Ermöglichen eine Analyse fiktiver Zustände. Es können die Auswirkungen von unterschiedlichen Größen auf verschiedene Kennzahlen simuliert werden.

## Forecasting
Hier werden aufgrund bestimmter Muster in Daten Prognosen über zukünftige Entwicklungen gemacht. Über Methoden wie Extrapolation oder Regression können sehr gute Vorhersagen getroffen werden.

## Aktive Systeme
Die Aktivität geht nicht vom Benutzer aus, sondern automatisch vom System beim Erreichen unterschiedlicher Schwellwerte oder Muster. Somit lässt sich noch besser reagieren.

## Near-Realtime
Daten werden stetig ins DWH nachgeladen anstelle der typischen periodischen Weise. Somit stehen sie früher zur Verfügung was ein besseres Monitoring und schnellere Reaktionen ermöglicht.