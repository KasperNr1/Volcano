# B-Bäume
## Aufbau
Ein Baum ist dann ein B-Baum der Ordnung $m$ g.d.w.
1. Jeder Knoten außer der Wurzel mindestens $m$ Datensätze enthält
2. Jeder Knoten enthält höchstens $2m$ Datensätze
3. Knoten mit $k$ Datensätzen, die keine Blätter sind, besitzen genau $k+1$ Nachfolger
4. Alle Blätter besitzen das gleiche Niveau (Sie stehen auf einer Ebene)
5. Sind $S_1, S_2, \dots S_k$ mit $m \leq k \leq 2m$ die Schlüssel eines Knotens $x$, dann sind alle Schlüssel des ersten (linkesten) Nachfolgers von $x$ kleiner als $S_1$ 

![](BBaum.png)

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

> [!Missing] Unvollständig
> Siehe 2 - 40 bis 2 -44

# B+ Bäume


> [!Info] Name
> Die Literatur hat verschiedene Namen für diese Varianten der [B-Bäume](#B-Bäume)


> [!Missing] Unvollständig
> Siehe 2 - 47 bis 2 -54


# Überdeckender Index
Manchmal können Anfrageergebnisse rein aus dem Index ermittelt werden, ohne die Daten zu lesen.

Beispielsweise kann bei der Verwendung eines [Dichten Index](02%20Dateiorganisation.md#Dichter%20Index) für das Attribut "Name" die folgende Abfrage nur anhand dieses beantwortet werden.
``` SQL
SELECT COUNT(Nachname) FROM Mitarbeiter WHERE Nachname = 'Schmidt'
```

# Zusammengesetzter Index

# Mehrdimensionaler Index
