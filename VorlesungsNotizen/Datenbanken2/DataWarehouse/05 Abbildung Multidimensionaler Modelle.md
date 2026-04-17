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