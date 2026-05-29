# Grundbegriffe
## Aufbau
![](MultidimensionalData.png)

Als Fakt wird ein Datum bezeichnet, das eine Frage zu einer gewissen Kombination von Dimensionen beantwortet. Hier wird die Anzahl an Verkäufen geliefert, abhängig von `Ort`, `Produkt` und `Datum`.

Alle Fakten zusammen bilden einen (Hyper-)Cube

Verschiedene Werte einer Dimension können in einer `Hierarchie` zusammengefasst werden.

## Operationen
### Drill-Down und Roll-Up
![](DrillDownUndRollUp.png)

Als Drilling wird die Aufteilung von Daten in kleinere Kriterien bezeichnet. Beispielsweise wenn Quartalsweise Zahlen in Monate sortiert werden.

Beim Roll-Up geschieht der Gegenteilige Prozess, Informationen werden anhand von Gemeinsamen Eigenschaften zusammengefasst.

### Pivoting
![](Pivoting.png)

Bezeichnet ein 'Drehen' des [Hypercube](#Aufbau) um die Daten anschaulich als abhängig von verschiedenen Dimensionen zu betrachten.

### Slice & Dice
![](SliceAndDice.png)

Bezeichnet ein Aufteilen des Hypercubes durch Filtern in Untermengen. Diese kleineren Datensätze können dann beliebig weiterverwendet werden.

# Eigenschaften multidimensionaler Schemata
## Berechnungsvorschriften
Die Berechnung von Kenngrößen entlang Hierarchiepfaden ist nicht immer sinnvoll.

Bei Verkaufszahlen pro Ort und Region lassen sich die Werte problemlos addieren, für Werte der Außentemperatur ist dies jedoch nicht sinnvoll. Eine Minimums oder Maximumsfunktion kann in beiden Fällen nützlich sein.

Um korrekte Ergebnisse zu erhalten, müssen drei Eigenschaften erfüllt sein.
- [Disjunktheit](#Disjunktheit)
- [Vollständigkeit](#Vollständigkeit)
- [Typverträglichkeit](#Typverträglichkeit)

### Disjunktheit
Jeder Wert einer Kennzahl darf exakt einmal in eine Berechnung einfließen.
![](Disjunktheit.png)

Eine einfache Summe würde hier falsche Ergebnisse liefern, da Kunden die in mehreren Jahren eingekauft haben als mehrere Personen gezählt werden würden.
Die Berechnung kann in einem anderen Kontext nützlich  sein, ist aber nicht anwendbar wenn die Zahl der individuellen Personen bestimmt werden soll.

### Vollständigkeit
Das Ergebnis einer Rechnung wird nur von den gegebenen Daten beeinflusst.
![](Vollständigkeit.png)

Die Anzahl der insgesamt verkauften Artikeln geht über die Verkäufe an Sonderaktionen hinaus. Mit der gezeigten Benennung könnte das Ergebnis leicht missverstanden werden. 
Tatsächlich berechnet wird die Anzahl an Verkäufen bei Sonderaktionen pro Jahr.

### Typverträglichkeit
Die Datentypen entscheiden über die erlaubten oder verbotenen Operationen der Werte.

Es wird klassisch zwischen drei Typen unterschieden:
- FLOW: 
  Bewegungszahlen, sind beliebig aggregierbare Werte z.B. "Bestellmenge eines Artikels pro Tag"
- STOCK
  Bestandsangaben, sind generell nicht über die Zeit addierbar. "Lagerbestand eines Artikels X"
- ValuePerUnit
  Sind Wertangaben die sich nicht summieren lassen. Beispielsweise "Steuersatz" oder "Wechselkurs"

![](OperationenProDatentyp.png)

In der Abbildung bedeutet ein `X` dass die Operation auf dem Datentyp erlaubt ist, ein `--` verbietet sie


> [!Info] Unvollständigkeit bei STOCK
> Diese Typklassifikation ist nicht unbedingt vollständig.
> In der Realität muss für einzelne Werte geprüft werden ob anhand ihnen summiert werden darf

## Struktur
Fakten können eine "innere Struktur" besitzen und dabei aus einem oder mehreren Attributen bestehen. Auch abgeleitete Attribute sind möglich.
![](InnereStruktur.png)

## Dimensionen
### Hierarchien
#### Einfach- und Mehrfach
![](HierarchieEinfachUndMehrfach.png)

Wenn sich jeder Wert zu genau einer Gruppe zählen lässt die ohne Duplikate eine Gesamtheit bilden, so spricht man von einer einfachen Hierarchie.

Bei einer mehrfachen Hierarchie können auch mehrere Ebenen auf eine andere folgen.
![](AlternativeVerdichtungspfade.png)

Wenn die Pfade einer Mehrfachhierarchie wieder zusammenlaufen, so spricht man von alternativen Verdichtungspfaden.
Berechnungsergebnisse müssen dabei auf allen Pfaden gleich sein.

#### Unbalancierte Hierarchie
Bei einer Zuordnung muss nicht immer jede Schicht durchlaufen werden.
![](UnbalancierteHierarchie.png)

#### Anteilige Verrechnung
![](AnteiligeVerrechnung.png)
Die Zuordnung von Hierarchieelementen muss hier nicht immer eindeutig sein.

#### Nicht-Vollständige Verdichtung
![](NichtVollständigeVerdichtung.png)
Hier nehmen nicht alle Instanzen an der Verdichtung teil.

## Schema
### Fakten
![](FaktenImSchema.png)
Mehrere Fakten können in einem Schema enthalten sein.
Dabei sind Beziehungen zwischen Fakten innerhalb desselben Schemas möglich.

### Dimensionen
![](DimensionenImSchema.png)

Auch verschiedene Dimensionen können Beziehungen zueinander haben.

## Sparsity und Besetzung
Die Dimensionen eines Schema spannen einen Raum auf.

Beispiel:
- Drei Dimensionen
	- Zeit (Tage)
	- Ort
	- Produkt
- Annahme 4 Jahre (1460 Tage), 50 Filialen, 4000 Produkte
Maximales Volumen des Hypercube: $1460 \times 50 \times 4000 = 292.000.000$ 

Bei $55.000.000$ Einträgen ist der Würfel zu $18,8\%$ besetzt. Man spricht auch vom "Besetzungsgrad"

Der Sparsity Faktor gibt den Anteil der Unbesetzten Zellen an:
$$
\text{Sparsity} = 1 - \text{Besetzung} = 1 - 18.8\% = 81.2\%
$$


> [!Info] Realistische Sparsity
> Werte der Größenordnung $80\%$ sind keine Seltenheit in echten Datenbanken.
> Dieser Fakt ist später bei der Realisierung einer solchen relevant.

# Notationen
Es gibt eine Reihe verschiedener Notationskonventionen.

Näher betrachtet wird die MML / $_mUML$ 

## MML
Multidimensional Modeling Language ist eine Erweiterung der UML. Sie soll objektorientierte Konstrukte beibehalten und um multidimensionale Konstrukte ergänzen. Sie erlaubt mit verschiedenen graphischen Notationen die Modellierung vielseitiger dimensionaler Strukturen.
![](MmlExample.png)

Als neue Verbindungen werden die folgenden hinzugefügt:
- Zwischen Fakt und dimensionaler Klasse
  Durchgezogener Pfeil mit Text`<<Dimension>>` und Name 
- Zwischen dimensionalen Klassen (Jeweils mit dem Zusatztext "Name der Nächsten Ebene")
	- `<<RollUp>>`
	- `<<SharedRollUp>>`
	- `<<NonCompleteRollUp>>`

![](MmlExampleComplex.png)
