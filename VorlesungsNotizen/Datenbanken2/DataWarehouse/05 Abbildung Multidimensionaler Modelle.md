# Relationale Speicherung
Für die Implementierung eines multidimensionalen Datenmodells muss dieses auf die unterstützten Funktionen des [Relationen Modells](Relationen.md) abgebildet werden.
Hierzu gibt es verschiedene Ansätze.
![](MultidimensionalToRelational.png)

## Schneeflockenschema
![](Faktentabelle.png)
Der gesamte Hypercube wird auf eine Tabelle abgebildet, wobei jede Dimension der Daten zu einer eigenen Spalte wird.
Diese Tabelle wird auch als 'Faktentabelle' bezeichnet.

Die Hierarchien werden als eigene Tabellen abgebildet. Dabei wird für jede Verdichtung der Fremdschlüssel der höheren Hierarchieebene hinterlegt.
![](RelationalHierarchie.png)

In der Faktentabelle würde entsprechend noch der Primärschlüssel einer zugehörigen Filiale als weiteres Attribut eingetragen werden.

Somit entsteht diese namensgebende, schneeflockenähnliche Struktur
![](SchneeflockenSchema.png)

### Bewertung
Das Schema ist normalisiert und vermeidet Redundanz und Anomalien. Es benötigt nur wenig Speicherplatz.
Nachteile sind die Vielzahl an Tabellen, wodurch die Verarbeitung von lesenden Anfragen durch die Menge an teuren Verbundoperationen wenig effizient wird.

## Sternschema
Um die Menge an Tabellen zu reduzieren werden beim Sternschema die Tabellen einer Dimension aus dem [Schneeflockenschema](#Schneeflockenschema) denormalisiert
![](Sternschema.png)

Die verschiedenen Tabellen werden zu einer einzelnen zusammengefasst.
![](Denormalisation.png)

Es entsteht ein übersichtliches und kompaktes Schema, wobei auch einige Nachteile vermieden werden. Beispielsweise lassen sich dimensionale Strukturen wie [Anteilige Verrechnung](02%20Multidimensionale%20Datenmodelle.md#Anteilige%20Verrechnung) gut abbilden.

Auch die [Dünnbesetztheit](02%20Multidimensionale%20Datenmodelle.md#Sparsity%20und%20Besetzung) ist kein Problem, da nur gefüllte Zellen des Hypercube einen Eintrag in der Faktentabelle erhalten.
Da die Faktentabelle deutlich mehr Daten enthält als die Dimensionstabellen ist auch der Effekt der Redundanzen auf das Gesamtvolumen vertretbar. Die Geschwindigkeitsgewinne bei Abfragen sind signifikant.

Da Dimensionsdaten nur sehr selten geändert werden und vom Ladeprozess kontrolliert werden ist die Gefahr von Änderungsanomalien gering.

Die beiden Schemata sind gut für die Anwendung in [OLAP Anwendungen](01%20Grundlagen%20und%20Definition.md#OLAP%20Server) geeignet, wobei das Sternschema aus Performancegründen verbreiteter ist.

# Änderungen in Dimensionen
Für unterschiedliche Arten von Änderungen müssen verschiedene  Schritte durchgeführt werden.

## a) Neue Dimensionselemente
Die neuen Elemente können problemlos eingefügt werden, ggf. kann mit [Constraints](Grundlagen.md#Datenmodell) gesichert werden dass bestimmte Kombinationen nicht möglich sind.
So werden Inkonsistente Zustände vermieden, bei denen Verbindungen genannt sind, die zu einem bestimmten Zeitpunkt nicht verfügbar waren.

## b) Änderung in einer Dimension
Wenn Einträge einer Dimension verändert werden müssen, wie bei der Umbenennung einer Filiale, kann dies auf zwei verschiedene Arten gespeichert werden.

Beispielsweise sei diese Menge an Produkten gegeben

| Name         | Gruppe   | Hauptgruppe  |
| ------------ | -------- | ------------ |
| Pizza Hawaii | Tiefkühl | Lebensmittel |
| Pizza Salami | Tiefkühl | Lebensmittel |
| Pizza Fungi  | Tiefkühl | Lebensmittel |

### b.1) Datensatz ändern
Hier wird der alte Wert überschrieben. Somit verändert er sich in allen referenzierenden Auswertungen, auch solchen die in der Vergangenheit liegen.
Somit sind diese alten Auswertungen eventuell nicht mehr nachvollziehbar.

Mit einem Überschreiben erhält man diese neue Relation

| Name         | Gruppe   | Hauptgruppe  |
| ------------ | -------- | ------------ |
| Pizza Hawaii | Tiefkühl | Lebensmittel |
| Pizza Salami | Tiefkühl | Lebensmittel |
| Pilzpizza    | Tiefkühl | Lebensmittel |

### b.2) Datensatz erneut einfügen
Wenn der neue Wert als separater Eintrag eingeführt wird, ist der Bezug zu den alten Daten nicht mehr erkennbar. 
Allerdings können einmal erstellte Auswertungen stets nachvollzogen werden, sie verändern sich nicht mehr.

Das Beispiel würde wie folgt lauten

| Name         | Gruppe   | Hauptgruppe  |
| ------------ | -------- | ------------ |
| Pizza Hawaii | Tiefkühl | Lebensmittel |
| Pizza Salami | Tiefkühl | Lebensmittel |
| Pizza Fungi  | Tiefkühl | Lebensmittel |
| Pilzpizza    | Tiefkühl | Lebensmittel |
### c) Neues Attribut einfügen
Wenn eine neue Gruppe oder Obergruppe eingefügt werden soll, so ist dies trivial möglich.

Wenn das neue Attribut auf der untersten Ebene der Hierarchie liegt, so muss für jeden Eintrag dieser neue Wert bestimmt werden. Dieser Schritt ist typischerweise sehr schwierig da die entsprechenden Daten meist nicht direkt erfasst sind.

![](AddingAttributesToDimension.png)

### d) Neue Dimension hinzufügen
Es wird eine neue Relation für die Dimension erstellt. Die Faktentabelle wird um ein Attribut erweitert. Für alle bestehenden Daten muss der Wert entsprechend nachgetragen werden, wobei auch hier eine Schwierigkeit darin besteht korrekte Werte zu ermitteln.

# Slowly Changing Dimensions
Vorschlag ist, die Dimensionsdaten bei jedem Nachladen vollständig abzugleichen.

## Typ I
Ist eine Kombination aus [a) Neue Dimensionselemente](#a%20Neue%20Dimensionselemente) und [b.1) Datensatz ändern](#b.1%20Datensatz%20ändern). Es wird auf Historisierung verzichtet.

Aus der Ausgangstabelle

| Name         | Gruppe       | Obergruppe    |
| ------------ | ------------ | ------------- |
| Pizza Tonno  | Tiefkühlkost | Fertigprodukt |
| Pizza Hawaii | Tiefkühlkost | Fertigprodukt |
| Pizza Funghi | Tiefkühlkost | Fertigprodukt |
wird durch die Änderung der Kategorie von 'Pizza Hawaii' und Hinzufügen einer neuen Sorte folgende Tabelle entstehen:

| Name         | Gruppe       | Obergruppe    |
| ------------ | ------------ | ------------- |
| Pizza Tonno  | Tiefkühlkost | Fertigprodukt |
| Pizza Hawaii | Tiefkühlkost | Gesundes      |
| Pizza Funghi | Tiefkühlkost | Fertigprodukt |
| Pizza Salami | Tiefkühlkost | Fertigprodukt |

## Typ II
Die Dimensionsdaten werden um Gültigkeitsintervalle erweitert. Um die Eindeutigkeit der Einträge zu sichern, wird der Primärschlüssel um ein Anfangsdatum erweitert.

Bei Veränderungen werden vier Fälle unterschieden:
- a) Neuer Datensatz ist noch nicht vorhanden $\to$ Einfügen
- b) Datensatz ist unverändert $\to$ Nichts tun
- c) Datensatz verändert  $\to$ Historisieren und neuen Eintrag einfügen
- d) Datensatz ist nicht mehr vorhanden $\to$ Enddatum eintragen

![](SlowlyChangingDimensionsTyp2.png)

## Typ III
Hinzufügen von Attributen (Verbreiterung der Tabelle)
Technisch ist diese Änderung sehr simpel. Die Dimensionstabelle wird um die neuen Attribute erweitert.

> [!Warning] Nicht gut
> Da das DWH die 'Single Source of Truth' sein soll, ist es schlecht diese Informationen im Nachhinein zu verändern. Vergangene Analysen werden eventuell verfälscht und sind nicht mehr nachvollziehbar.


# Relationale Umsetzung multidimensionaler Anfragen

> [!Warning] Schemaabhängigkeit
> Die genaue Umsetzung hängt vom verwendeten Schema ab. Hier wird im weiteren vom [Sternschema](#Sternschema) ausgegangen.

Die Anfragen können in SQL formuliert werden.
Hier anhand des  Beispiels: "Zeige die Anzahl aller Verkäufe kleiner als 100 aller Filialen der Region 'Südwest' der Jahre 2001 und 2002 für die Produktgruppe 'Kosmetik' oder 'Gemüse' an"

``` SQL
SELECT  Ort.Filiale,
		Zeit.Jahr,
		Produkt.Gruppe,
		SUM(V.Anzahl)

FROM    Verkaeufe V,
		Ort O,
		Zeit Z,
		Produkt P

WHERE   V.Ort_ID = Ort.ID AND
		V.Zeit_ID = Zeit.ID AND
		V.Produkt_ID = Produkt.ID AND
		Ort.Region = ‘Südwest‘ AND
		Zeit.Jahr IN [2001,2002] AND
		(Produkt.Gruppe = ‘Kosmetik‘ OR
		Produkt.Gruppe = ‘Gemüse‘)

GROUP BY Ort.Filiale,
		Zeit.Jahr,
		Produkt.Gruppe
		
HAVING  SUM(V.Anzahl) < 100;
```

Die weiteren multidimensionalen Anfragen lassen sich ebenfalls leicht in relationale Anfragen übersetzen.
- [Rotating und Pivoting](02%20Multidimensionale%20Datenmodelle.md#Pivoting) sind lediglich die Reihenfolge der Attribute innerhalb der Anfrage. Die resultierenden Daten sind identisch
- [Slice & Dice](02%20Multidimensionale%20Datenmodelle.md#Slice%20&%20Dice) Lassen sich durch Formulierungen in `WHERE` und `HAVING` Klausel abbilden.
- [Drill-Down und Roll-Up](02%20Multidimensionale%20Datenmodelle.md#Drill-Down%20und%20Roll-Up) durch separate Anfragen mit veränderter `GROUP BY` Klausel. Eventuell können Ergebnisse wiederverwendet werden um effizienter zu rechnen.

Es ist also möglich alle Arten von Anfragen im relationalen Modell darzustellen. Um dies eleganter zu gestalten, gibt es allerdings spezielle Erweiterungen die auf die Arbeit mit multidimensionalen Daten ausgelegt sind.


# Multidimensionale Speicherung
Es sind Datenstrukturen für die Dimensionen und den Hypercube notwendig.
Wesentlich werden diese Daten intern als Arrays dargestellt. Zur Verwendung dieser ist eine Ordnung der Dimensionen notwendig. Dabei ist diese Ordnung nur für die interne Verarbeitung relevant und soll dem Benutzer verborgen bleiben.

![](DimensionsAsArray.png)
Diese Liste enthält alle Elemente, allerdings ist die Relation nicht eindeutig. Es ist nicht erkennbar, welche Städte zu einer Region gehören.

Der Hypercube kann als mehrdimensionales Array gespeichert werden. Somit ist es beim Suchen eines Eintrags nicht nötig die Daten zu durchsuchen, es kann direkt über den Index zugegriffen werden.
![](MultidimensionalStorageOfHypercube.png)

## Linearisierung
Um den Hypercube in einem Array speichern zu können, muss er linearisiert werden. Die Hochdimensionale Struktur muss dazu in eine eindimensionale Reihenfolge gebracht werden.
Für eine einfache Abarbeitung entlang der Dimensionen würde sich die Position jeder Zelle im Array wie folgt berechnen:
$$
\text{Index}(z) = x_1 + (x_2 - 1) \cdot |D_1| + (x_3 -1) \cdot |D_1| \cdot |D_2| + \dots + (x_n - 1) \cdot |D_1| \cdot \dots \cdot |D_{n-1}|
$$
$$
= 1 + \sum_{i=1}^{n}(x_i - 1) \cdot \prod_{j=1}^{i-1} |D_i|
$$
Dabei sind $D_1, D_2, \dots, D_n$ die Dimensionen, $|D_i|$ die Anzahl an Elementen einer Dimension und die Koordinaten einer Zelle $(x_1, \dots, x_n)$

Da die Menge an Zellen für die physische Speicherung in Blöcke unterteilt wird, hat die Reihenfolge einen großen Einfluss auf die Performance. Aufgrund der hohen [Sparsity](02%20Multidimensionale%20Datenmodelle.md#Sparsity%20und%20Besetzung) ist es nicht sinnvoll alle Zellen tatsächlich im Speicher abzulegen. Viele Werte sind leer und könnten bei passender Trennung in Blöcken ignoriert werden um Speicherplatz zu sparen.

## Space-Filling Curves
Raumfüllende Kurven wie die Hilbertkurve sind Kurven, die jede Koordinate im Raum exakt einmal erreichen. Im Gegensatz zur primitiven Linearisierung werden hier beide Dimension näherungsweise 'gleichzeitig' erhöht. Felder die weiter rechts oder weiter unten als ein anderes sind, kommen näherungsweise nach dem oberen/linken. Trotzdem wird die unterste Reihe nicht als letztes besucht.
![](HilbertKurve.png)

Ebenfalls bekannt ist die "Z-Kurve". Namensgebend ist hier der Basisfall ihrer rekursiven Definition.
![](ZKurve.png)

## Physische Speicherung
### Blöcke
![](SparseBlocks.png)
Die Wahl der Reihenfolge hat erhebliche Einflüsse auf die Möglichkeiten zur Speicheroptimierung. Während im ersten Beispiel alle Blöcke gespeichert werden müssen, können im zweiten Beispiel 3 der vier Blöcke mit einem Verweis in den Metadaten ausreichend markiert werden.

### Zwei-Ebenen-Speicherung
![](TwoLayerStrategy.png)
Hier wird unterschieden zwischen Dimensionen mit vielen, und solchen mit wenigen Einträgen. 
Die Spärlich besetzten Kombinationen werden als separate Struktur ausgelagert und enthalten entsprechende Pointer auf die Blöcke in denen die Daten enthalten sind.
Dabei ist das Konzept nicht auf zwei Ebenen begrenzt, es lässt sich hierarchisch beliebig erweitern.

### Materialisierung
Verschieden Aggregationen werden typischerweise vorberechnet (Materialisiert) und redundant abgelegt um Antwortzeiten zu beschleunigen. 
Sei folgender Hypercube gegeben:
![](HierarchischerHypercube.png)

Die Anzahl der Hypercubes um jede Kombination aggregiert zu speichern berechnet sich aus dem Produkt der Hierarchiebene ($4 \cdot 4 \cdot 3 = 48$)

Die Menge an Insgesamt vorhandener Zellen berechnet sich aus der Anzahl an Instanzen pro Dimension. 
$$
1508*262*40163 \approx 15,8 \text{Mrd}
$$
Dabei sind ca. 4 Mrd Zellen nicht in der Detailebene
$$
1508*262*40163 -1440*200*40000 \approx 4 \text{Mrd}
$$
Diese Zellen stellen also Kombinationen verschiedener Aggregationen dar. So kann beispielsweise die Summe aller verkauften Produkte in einer Region direkt abgelesen werden.

Für die Unterstützung weiterer Aggregatfunktionen (Mittelwert / Min / Max etc.) steigt der Speicherbedarf entsprechend.