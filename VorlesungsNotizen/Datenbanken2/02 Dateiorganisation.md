# Begriffe
## Zugriffsmethode
Bezeichnet die notwendigen Schritte zum Lesen / Speichern / Löschen eines Datensatzes

# Heap Dateien
Unsortierte Dateien, Daten werden in Reihenfolge des Einfügens geschrieben

![](HeapFiles.png)
## Lesen
Immer lineare Suche nötig
(Bei Scan / Punkt- und Bereichssuche)

## Einfügen
Immer am Ende anfügen, sehr schnell

## Löschen
Datensatz wird [gefunden](#Lesen) und gelöscht, in der Regel wird der Speicherplatz nicht wiederverwendet.

Bei häufigem Löschen muss in gewissen Zeitabständen reorganisiert werden.

# Sortierte Dateien
Datensätze sind nach einem oder mehreren Attributen sortiert

## Lesen
Scan: Sequentielles Lesen der ganzen Datei

Punktsuche: [Binary Search](Suchalgorithmen.md#Binary%20Search) möglich

Bereichssuche: Punktsuche nach erstem Element, danach sequenziell lesen

## Einfügen
Suche Einfügestelle mit [Binary Search](Suchalgorithmen.md#Binary%20Search)
Seite reorganisieren um Platz für neuen Eintrag zu schaffen

Eventuell überlaufende Einträge auf nächster Seite erneut einfügen (Kann beliebig lange kaskadieren)


> [!NOTE] Ausweg
> Durch separate Überlauf / Transaktionsdatei kann die wiederholte kaskadierung etwas gehemmt werden.

## Löschen
Suche der Löschstelle
Entfernen des Eintrags

# Hash-Dateien
Hash des Eintrags berechnet Seite auf der Eintrag gespeichert werden soll.

Weil Hash-Verteilung zufällig scheint wird dieses Verfahren auch als "random File" genannt

## Einfügen
Berechnung des Hashs, einfügen auf dieser Seite.

Falls kein Platz frei ist, muss sondiert werden:
### Lineares Sondieren
Es wird der erste freie Platz nach der berechneten Adresse gewählt

![](LinearHashCollision.png)

Besonders beim Löschen anderer Datensätze (Bsp. auf Seite 1) kann unübersichtlich werden, wo der auf Seite 3 geplante Eintrag hin-sondiert wurde.

### Nichtverkettete Überläufer
Es wird ein spezieller Bereich für Überläufer zur Verfügung gestellt.

![](HashOverFlowStorage.png)
Es kann ein Verweis auf die Speicherstelle im Überlaufbereich notiert werden, um die Suche dort zu beschleunigen.

# Dynamisches Hashing
Soll dynamische Dateigrößen ermöglichen.

Idee: Hashwert mit $n$ Bit Ergebnis wird berechnet.

Es wird versucht nur $b$ Buckets für alle Datensätze zu verwenden, Zuordnung über die letzten $b$ Bits des Hashwerts.

Ablauf:
- Fall 1: Seite hat noch freien Platz: Füge Element ein
- Fall 2: Seite ist voll:
	- Fall 2.A: Lokale Tiefe = Globale Tiefe:
		- Erhöhe globale und lokale Tiefe um 1
		- Erweitere Directory
		- Splitte übergelaufenen Bucket auf
		- Weise entsprechende Zeiger zu
	- Fall 2.B: Lokale Tiefe < Globale Tiefe:
		- Erhöhe lokale Tiefe um 1
		- Splitte übergelaufenen Bucket auf
		- Weise entsprechende Zeiger zu
	- In beiden Fällen: Re-Hashing der Elemente des übergelaufenen Bucket

### Beispiel Dynamisches Hashing
Seien die folgenden Elemente und ihre Hashwerte gegeben:

| Element | Hash-Wert |
| ------- | --------- |
| Z       | 101000    |
| B       | 100101    |
| V       | 001110    |
| M       | 100110    |
| F       | 110001    |
| K       | 010110    |
| X       | 010010    |

Die Einträge sollen in der Gegebenen Reihenfolge eingefügt werden, Buckets haben die Größe $3$.
Für die ersten drei Einträge ist das Einfügen trivial.
![](DynamicHashingExample1.png)

Um Platz für den vierten Wert zu schaffen, muss die Seite aufgeteilt werden. Da die lokale und globale Tiefe beide bei $0$ liegen, wird sie auf $1$ erhöht, die Seite aufgeteilt und alle enthaltenen Elemente erneut zugeordnet.

![](DynamicHashingExample2.png)

Das Einfügen von $F$ ist in diesem Zustand problemlos, bei Eintrag $K$ muss erneut aufgeteilt werden.

![](DynamicHashingExample3.png)

Bemerkenswert ist, dass die Bitkombinationen $01$ und $11$ beide auf den selben Bucket mit lokaler Tiefe von $1$ verweisen. So wird nur dort Speicherplatz allokiert, wo er auch wirklich notwendig ist.

Der Effekt ist nach dem Einfügen von $X$ noch stärker sichtbar.
![](DynamicHashingExample4.png)

> [!Example] Klausuraufgabe
> Einfügen von mehreren Elementen mit Aufsplittung überlaufender Buckets
> Siehe Folie 1 -- 45 bis 1 -- 58

## Lesen
Konstante Zugriffszeiten möglich
## Einfügen
Schnell, eventuell muss gesplittet werden, jedoch ist der Aufwand hier lokal beschränkt
## Löschen
Schnell, Hash-Wert berechnen und löschen.


> [!NOTE] Notiz
> Theoretisch müsste das Splitting auch rückgängig gemacht werden, wird typischerweise nicht gemacht.
> Reduktion des Datenbankvolumens eher manuell durch DB-Admin


# Vergleich
Von [Heap Dateien](#Heap%20Dateien), [Sortierte Dateien](#Sortierte%20Dateien) und [Hash-Dateien](#Hash-Dateien)
![](ComparisonHeapSortAndHash.png)

# Begriffe
## Index
Ist eine Sekundärorganisation mit der auch nach nicht-Schlüsselattributen gesucht werden kann.

Die Verwendung eines Index kann große Performance Verbesserungen bringen, erfordert aber zusätzlichen Speicherplatz und Aufwand um sie aktuell zu halten.

## Anfragearten
### Sequentieller Zugriff
(Sortiert)
"Alle Mitarbeiter, sortiert nach PersNummer"
### Direkter Zugriff
Punktabfrage
"Mitarbeiter mit PersNummer 49"

### Direkter Zugriff
Multi-Punktabfrage
"Alle Mitarbeiter der IT-Abteilung"

### Bereichszugriff
"Alle Mitarbeiter mit Gehalt zwischen 2000 und 3000"

### Existenztest
"Gibt es einen Mitarbeiter mit PersNummer 123"


# Indexstrukturen
## Primärindex
Der Primärindex ist eine sortierte Datei mit Indexeinträgen.
Jeder einzelne dieser Einträge besteht dabei aus einem Schlüssel und einem Zeiger auf den entsprechenden Datensatz / Block.

## Dichter Index
Ein Eintrag pro Indexattributwert
Alle Sätze direkt lokalisierbar

![](DichterIndex.png)

## Dünner Index
Jeweils erster Satz einer Seite wird indexiert 
Setzt sortierte Datei voraus

![](DünnerIndex.png)


> [!Info] Vergleich
> Bei einem dünnen Index muss die Relation nach diesem Indexattribut sortiert sein. Entsprechend kann nur maximal ein einzelner dünner Index pro Relation verwendet werden.
> Ein dichter Index benötigt mehr Speicherplatz, hier gibt es aber keine Beschränkung bezüglich der Anzahl gleichzeitig eingesetzter Indixe.

## Clusterindex
Strategie ist das Speichern von logisch zusammenhängenden Datensätzen in physisch benachbarten Stellen. Dabei wird der Index (beinahe) gleich geordnet.
Für jeden Eintrag wird die Form `<K(i), P(i)>` verwendet, wobei $K(i)$ Ein Eintrag pro Indexattributwert $A$ ist und $P(i)$ auf die Position verweist, an der $A$ zum ersten Mal vorkommt.
Es wird dabei ein [dünner Index](#Dünner%20Index) verwendet.
Besonders ist hier, dass zu jedem möglichen Wert von $A$ ein Eintrag im Index gespeichert wird.


## Sekundärindex
Hängt nicht mit der physischen Speicherung zusammen und kann über beliebige Attribute erstellt werden.
- `<Value>, TID` (Eindeutige Werte)
Für mehrdeutige Attribute wird dabei eine Liste mit allen Matches gespeichert (Invertierte Liste)
- `<Value>, ListOfTIDs`

![](Sekundärindex.png)

Um konstante Größen zu erreichen kann die Liste der `TIDs` auch indirekt gespeichert werden. So verweist jeder Indexeintrag auf exakt eine Liste, diese enthalten dann jeweils beliebig viele `TIDs`.


## Mehrstufiger Index
Auch der Index einer entsprechend großen Datenmenge wird groß (= zu groß für den Hauptspeicher).
Um weiterhin schnell zu suchen, kann ein Index über diesen Index gebildet werden.
Mit mehreren Schichten kann so das Volumen des höchsten Levels reduziert werden, bis er vollständig im Hauptspeicher gehalten werden kann.

![](MultiLevelIndex.png)

![](IndexCategories.png)
![](IndexCategories2.png)
