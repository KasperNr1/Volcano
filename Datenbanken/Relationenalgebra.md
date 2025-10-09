Mit dieser Formalen Schreibweise lassen sich Abfragen aus verschiedenen [Relationen](Relationen.md) formulieren.

# Selektionen
Das Symbol $\sigma$ symbolisiert die Auswahl. Dabei wird ein Datensatz nach den Werten der angegebenen [Attributen](Relationen.md#Attribut) gefiltert.
Es werden alle Spalten übernommen. 

![](Selektion.png)

# Projektion
Bei einer Projektion $\Pi$ werden einzelne Spalten einer Auswahl gefiltert. Entgegen der [Selektion](#Selektionen) bleiben die Zeilen hier unverändert.

![](Projektion.png)

# Umbenennung
Bei einer Umbenennung $\varrho$ wird ein Attribut umbenannt. Die Transformation hat keinen Einfluss auf die selektierten Daten.
Falls eine Umbenennung in einer verschachtelten Kette auftritt, müssen alle äußeren Transformationen den neuen Namen verwenden. Im Beispiel ist dies ersichtlich, die [Projektion](#Projektion) verweist auf `Vorname` anstelle des ursprünglichen `Name`

![](Umbenennung.png)


# Kartesisches Produkt
Das Kartesische Produkt $\times$ berechnet alle möglichen Kombinationen zweier [Relationen](Relationen.md).
Das Resultat enthält demnach bei zwei Relationen der Größen $n$ und $m$ exakt $n*m$ Elemente.

![](KartesischesProdukt.png)


# Vereinigung
Die Vereinigung $\cup$ ist in der Lage mehrere Relationen zu kombinieren. Dabei müssen die beiden Relationen **vereinigungskompatibel** sein. Das bedeutet, dass sie in sämtlichen Attributnamen und [Domänen](Relationen.md#Domäne) übereinstimmen müssen.
Duplikate werden hierbei ignoriert.

![](Vereinigung.png)

# Schnitt
Der Schnitt $\cap$ bestimmt alle Elemente, die in beiden Relationen vorhanden sind.
![](Schnitt.png)


# Differenz
Die Differenz $-$ oder $\setminus$  einer Relation $A$ zu einer Anderen $B$ sind alle Elemente aus $A$, die nicht in $B$ enthalten sind.
Dabei müssen die Relationen wie auch bei der [Vereinigung](#Vereinigung) vereinigungskompatibel sein.

![](Differenz.png)


> [!Warning] Besonderheit
> Die Differenz zwischen $A$ und $B$ ist im Allgemeinen nicht identisch zur Differenz von $B$ und $A$.


# Verbund (Join)
Beim [Kartesisches Produkt](#Kartesisches%20Produkt) entstehen häufig Ergebnismengen mit zu vielen Elementen.
Die verschiedenen Varianten des Verbunds grenzen die Ergebnismenge etwas ein.

## Thetaverbund
Der Verbund $\bowtie_P$  ist ein Verbund der alle Tupel des Kartesischen Produkts enthält, für die eine Aussage $P$ wahr ist.

![](ThetaVerbund.png)


## Natürlicher Verbund
Beim Natürlichen Verbund $\Join$ wird anhand gemeinsamer Attribute verbunden.
Es wird immer über alle Attribute mit gleichem Namen abgeglichen

![](NaturalVerbund.png)

## Äußerer Verbund
Bei einem äußeren Verbund werden allen Elementen der Linken Relation ein Element der Rechten Relation zugeordnet. Ähnlich wie beim [Natürlichen Verbund](#Natürlicher%20Verbund) wird nach passenden, gleichnamigen Attributen gesucht. Falls kein passender Eintrag gefunden wurde, wird mit dem leeren Wert `Null` aufgefüllt.
Dieses Auffüllen ist der einzige Unterschied zum natürlichen Verbund.

![](OuterJoin.png)



