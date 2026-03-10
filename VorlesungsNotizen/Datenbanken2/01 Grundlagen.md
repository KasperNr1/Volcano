# Wiederholung Begriffe
## Datenbank
Datenbasis & Dateien, Metadaten

## Datenbankmanagementsystem (DBMS)
Software zur Interaktion mit [Datenbank](#Datenbank) und zur Verwaltung von Constraints und Berechtigungen

## Datenbanksystem (DBS)
Kombination aus [Datenbank](#Datenbank) und [Datenbankmanagementsystem (DBMS)](#Datenbankmanagementsystem%20(DBMS))

# ACID Prinzip
Siehe [ACID](Transaktionen.md#ACID)

# Random Notes
Pagination: Seitengröße typisch bei $2-32kb$  

Festplatte lesen ist sehr teuer, daher Buffer 

# Speichern von Daten
## Feste Länge
Wenn Speicherblöcke stets mit fester Länge bemessen werden, ist das sehr effizient für die Speicherung und den Zugriff auf das Datum, jedoch wird viel Platz verschwendet , wenn die Daten kleiner sind als der zur Verfügung stehende Speicherplatz.

## Variable Länge
![](VariableLengthStorage.png)

Hier gibt es mehrere Varianten.
1. Speichern mit Trennzeichen, verwendet zusätzlichen Speicher und benötigt Iteration über komplette Datensätze um Werte am Ende zuzugreifen.
2. Speichern von 
	1. Offsets der Datenpunkte
	2. Die Datenpunkte selber
	So kann schneller zu beliebigen Stellen gesprungen werden. Hinzufügen gänzlich neuer Einträge hat eine Verschiebung aller Daten-Werte im Speicher zur Folge
3. Speichern von
	1. Nummer des Felds
	2. Länge des Felds
	3. Wert des Felds
	Hier kann beliebig erweitert werden. Der Zugriff ist jedoch wieder nur durch Iteration möglich, durch die Längenangaben jedoch etwas schneller.

## Datensatzorganisation
Wenn ein Datensatz sehr groß wird (Größer als eine Seite im Speicher) kann er nicht auf einmal gehalten werden.
Typischerweise wird der Inhalt aufgeteilt. 
Entweder
1. Nach Wichtigen / Unwichtigen Attributen
2. Nach Name / Preview / Metadaten und Hauptinhalt (Besonders bei Bild-Datenbanken)

## Alignment
Daten müssen oft ausgerichtet sein. (Siehe Rechnerarchitektur)
Das bedeutet dass jede Anfangsadresse ein vielfaches der Größe eines Datentyps sein muss.

Bei Booleans (1Byte) und Integers (4 Byte) dürften Booleans in jedem Byte $(0,1,2,3,4,5,\dots)$ des Speichers liegen, Ints jedoch nur in solchen die durch 4 teilbar sind $(0,4,8,\dots)$

# Seitenorganisation
## Feste Länge
### Gepackte Organisation
Alle $n$ Daten sind an den Stellen $0$ bis $n-1$ 
Addieren von Einträgen geht immer an Stelle $n$, beim Löschen muss häufig ein Teil der Daten verschoben werden um die Lücke zu schließen.

### Ungepackte Organisation
Jeder Slot hat ein Attribut in den Metadaten dass aussagt, ob er aktuell gefüllt ist.
Somit muss nicht veschoben werden, einfügen muss aber erst nach freier Stelle suchen.

## Variable Länge
Wiederholtes Löschen führt zu Fragmentierung des Speichers
Beim Einfügen muss nach Stelle mit passender Größe gesucht werden.

![](VariableLengthOrga.png)
Links sind die "Globalen Adressen" der Datensätze. Zu lesen als "Block 123, Stelle n".
Im Header der Blöcke (Unten rechts in der Abbildung) ist für jeden Eintrag im Block seine Adress im Block hinterlegt.
An dieser Adress im Block liegen die tatsächlichen Werte.

Wenn durch Änderung in einem Datensatz der verfügbare Platz nicht ausreicht, wird er in einen andern Block verschoben und durch "Chaining" eine Referenz auf seinen neuen, größeren Speicherort hinterlegt. Das [DBMS](#Datenbankmanagementsystem%20(DBMS)) sorgt typischerweise dafür, dass maximal eine Stufe an Chaining eingesetzt wird. So bleiben die Zugriffszeiten konsistent.

Die von "außen" sichtbare Adresse hat sich durch die Verschiebung mit Chaining nicht geändert. 

