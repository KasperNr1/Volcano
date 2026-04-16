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

