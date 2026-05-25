Die bisher betrachteten [Indexstrukturen](02%20Dateiorganisation.md#Indexstrukturen) haben hohe Kosten bei Aktualisierungsoperationen. Mit Baumbasierten Strukturen kann hier eine bessere Leistung erreicht werden.
# B-Bäume
## Aufbau
Ein Baum ist dann ein B-Baum der Ordnung $m$ g.d.w.
1. Jeder Knoten außer der Wurzel mindestens $m$ Datensätze enthält
2. Jeder Knoten enthält höchstens $2m$ Datensätze
3. Knoten mit $k$ Datensätzen, die keine Blätter sind, besitzen genau $k+1$ Nachfolger
4. Alle Blätter besitzen das gleiche Niveau (Sie stehen auf einer Ebene)
5. Sind $S_1, S_2, \dots S_k$ mit $m \leq k \leq 2m$ die Schlüssel eines Knotens $x$, dann sind alle Schlüssel des ersten (linkesten) Nachfolgers von $x$ kleiner als $S_1$ 

![](BBaum.png)


## Größenberechnung BBäume
Die Anzahl $x$ der Einträge pro Speicherblock kann wie folgt berechnet werden.
- $b$ sei die Blockgröße
- $z$ der Platzbedarf eines einzelnen Zeigers
- $s$ der Bedarf eines einzelnen Schlüsselwerts
- $d$ der Bedarf des restlichen Inhalts eines Datensatzes

Es gilt:
$$
x \cdot (s + d) + z \cdot (x + 1) = b
$$
Somit kann die Anzahl der Einträge pro Knoten wie folgt berechnet werden:
$$
n = \left \lfloor \frac{b - z}{s + d + z} \right \rfloor 
$$
Um aus dieser Zahl die maximale Ordnung $m$ des Baumes zu bestimmen muss der größte gerade Wert gefunden werden, sodass gilt:
$$
2 \cdot m \leq n \qquad \text{mit} \; m \in \mathbb{N}
$$
Bei einer Blockgröße von $4096$ Byte, einer Zeigergröße von $8$ Byte und $32$ + $200$ Byte Bedarf für Schlüssel und Daten ergibt sich eine Kapazität von $17,03$ Einträge pro Block.
Entsprechend können 17 Einträge vollständig gespeichert werden. Somit wird $m = 8$ gewählt, damit ein Knoten mit bis zu $2 \cdot m = 16$ Einträgen gehalten werden kann.

> [!EXAMPLE] Klausuraufgabe
> Die Ordnung eines B-Baum berechnen, um Blockgröße der Festplatte ideal auszunutzen.



## Suchen
Einstieg über die Wurzel. Jeder Wert ist eine Intervallgrenze des untergeordneten Knotens.

So kann schnell gesucht werden, indem man tiefer einsteigt bis man den Wert findet, oder einen Blattknoten erreicht.

![](BBaumSearch.png)

## Einfügen
### Einfacher Fall
Falls im Blattknoten des richtigen Intervalls noch Platz verfügbar ist, kann der Eintrag hier eingefügt werden.
![](BBaumAddingSimple.png)

### Overflow
Wenn das Blatt bereits $2m$ Einträge besitzt, wird ein neuer Knoten gebildet.

- Die kleineren $m$ Einträge verbleiben im Knoten
- Die größten $m$ Einträge werden in einen neuen Knoten verschoben
- Der mittlere Eintrag wird in den Vorgängerknoten eingefügt


> [!Info] Kaskadierung
> Durch das Hinzufügen im Vorgängerknoten kann auch dieser Überlaufen. Eventuell kann dieser Effekt rekursiv durch den gesamten Baum verlaufen.


![](BBaumAddingOverflow.png)

## Löschen
Beim Löschen gibt es drei verschiedene mögliche Situationen.
1. Löschen ohne Unterlauf
2. Löschen mit Unterlauf, Nachbar hat über $m$ Einträge
3. Löschen mit Unterlauf, Nachbar hat exakt $m$ Einträge

Das Löschen aus einem gut gefüllten Knoten ist trivial, der Eintrag wird ohne weitere Operationen entfernt.
![](BTreeDeletionCase1.png)

Falls ein Unterlauf erzeugt wird, kann dieser behoben werden indem Einträge aus benachbarten Blättern umgezogen werden.
![](BTreeDeletionCase2.png)


> [!Info] Nachbarn
> Die Seite von der benachbarte Einträge zugezogen werden, ist einmalig fest definiert. Die Wahl beeinflusst die Performance der Datenstruktur im Allgemeinen nicht, lediglich konkrete Beispiele verhalten sich unterschiedlich.

Falls aus dem Nachbarknoten kein Eintrag entnommen werden kann, so werden die Knoten miteinander verschmolzen.
![](BTreeDeletionCase3.png)

# B+ Bäume
> [!Info] Name
> Die Literatur hat verschiedene Namen für diese Varianten der [B-Bäume](#B-Bäume)

In dieser Variante werden Daten ausschließlich in den Blattknoten gespeichert. Die Knoten in höheren Stufen enthalten lediglich Verweise auf darunterliegende Knoten. So wird eine kleine Menge Speicherplatz gespart, wodurch die Baumhöhe ggf. reduziert wird was die Suche beschleunigt.
Zusätzlich sind die Blätter miteinander verlinkt um ein sortiertes Traversieren zu ermöglichen.

![](BPlusTrees.png)

## Größenberechnung B+ Bäume
Auch hier lässt sich die Größe im Speicher berechnen.
Für innere Knoten gilt:
$$
p \cdot P_{\text{Block}} + (p - 1) \cdot K \leq B \Leftrightarrow p \leq \frac{B + K}{P_\text{Block} + K}
$$

 Für die Blätter gilt:
$$
p_\text{Leaf} \cdot (K + P_\text{Rec}) + P_\text{Block} \leq B \Leftrightarrow \frac{B - P_\text{Block}}{K + P_\text{Rec}}
$$

---
Der Unterschied ist an folgendem Beispiel erkennbar:
- Blockgröße $B = 4096$ Byte
- Indexwert $K = 10$ Byte
- Datensatzzeiger $P_\text{Rec} = 8$ Byte
- Blockzeiger $P_\text{Block} = 6$ Byte

[Größenberechnung der B-Bäume](#Größenberechnung%20BBäume) führt zu $85$ Einträgen pro Knoten.

Mit $p = 256$ und $P_\text{Leaf} = 227$ ergibt sich eine Grenze bei 128 Einträgen.


> [!NOTE] Was ist $p$?
> Mit $p$ ist der Verzweigungsgrad (Auch 'Fan-Out’) gemeint. Der Wert bestimmt die maximale Anzahl von Pointern pro Knoten im Baum. Ein hoher Wert führt entsprechend zu flacheren, breiteren Bäumen während kleine Zahlen das Gegenteil bewirken.
> Siehe 2 - 47 bis 2 -54

## Einfügen in B+ Bäume
Hier wird bei der Behandlung von Überläufen unterschieden, ob ein Blatt- oder ein Nicht-Blatt überläuft. 

Beim Überlauf eines Blatts wird der mittlere Wert des Knotens repliziert, sodass er weiterhin im Blatt enthalten ist aber auch ein Verweis im nächsthöheren Knoten eingefügt wird.
Ein Kaskadierender Überlauf oder initialer Überlauf eines Nicht-Blatts wird wie bei normalen [BBäumen](#Einfügen) behandelt.

# Überdeckender Index
Manchmal können Anfrageergebnisse rein aus dem Index ermittelt werden, ohne die Daten zu lesen.

Beispielsweise kann bei der Verwendung eines [Dichten Index](02%20Dateiorganisation.md#Dichter%20Index) für das Attribut "Name" die folgende Abfrage nur anhand dieses beantwortet werden.
``` SQL
SELECT COUNT(Nachname) FROM Mitarbeiter WHERE Nachname = 'Schmidt'
```


> [!MISSING] Lesezeichen
> 2 - 60


# Zusammengesetzter Index

# Mehrdimensionaler Index
