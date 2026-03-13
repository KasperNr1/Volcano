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


> [!Example] Klausuraufgabe
> Einfügen von mehreren Elementen mit Aufsplittung überlaufender Buckets
> Siehe Folie 1 -- 45 bis 1 -- 58


Siehe Folie 1 -- 44

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
## Dichter Index
Ein Eintrag pro Indexattributwert
Alle Sätze direkt lokalisierbar

## Dünner Index
Jeweils erster Satz einer Seite wird indexiert 
Setzt sortierte Datei voraus


> [!Missing] Lücke
> Hier fehlt Info zu Indexen
> Seite 2 -- 11 bis 2 -- 31


