Sind Funktionen zur Bildung von Summen oder Rangfolgen. Auch komplexere Statistische Auswertungen fallen unter diese Kategorie.

# Einfache Aggregatfunktionen
Fassen Werte aus mehreren Zeilen zusammen.
Syntax: `<agg_function>(<expression>)`

``` SQL
SELECT SUM(b) AS sum FROM T
```

## Gruppierung
Unterteilt Datensätze in Teilmengen
Syntax `GROUP BY <expression>`
``` SQL
SELECT a, SUM(b) AS sum FROM T GROUP BY a;
```

Auf diesen Gruppen kann noch weiter gefiltert werden.
Die Bedingung wird mittels einer `HAVING` Klausel formuliert.
``` SQL
SELECT a, SUM(b) AS sum FROM T GROUP BY a HAVING SUM(b) > 10;
```


# Analytische Funktionen
Arbeiten auch auf Teilmengen, fassen die Daten aber im Gegensatz zu [Einfache Aggregatfunktionen](#Einfache%20Aggregatfunktionen) nicht zu einer Zeile zusammen.

Syntax:
``` 
<function> (<arg_1> [, <arg_2>])
OVER (
[<partition_clause>]
[<sorting_clause>]
[<windowing_clause>]
)
```

``` SQL
SELECT a, b, c, SUM(b) OVER () AS sum FROM T
```

![](AnalyticalFunctionExample1.png)

Das Resultat wird an jede Zeile angefügt, ist aktuell aber wenig aussagekräftig.

``` SQL
SELECT a, b, c, SUM(b) OVER (PARTITION BY a) AS sum FROM T
```

![](AnalyticalFunctionExample2.png)

Nun sind die Summen entsprechend nur auf die aktuelle Gruppe bezogen.
Das Resultat hängt von der Sortierung ab und ist in diesem Fall eher zufällig richtig.

``` SQL
SELECT a, c, b, SUM(b) OVER(PARTITION BY a ORDER BY c) AS sum FROM T;
```

![](AnalyticalFunctionExample3.png)

Die Summenwerte sind überraschend verändert, die Zeilen innerhalb der Gruppen aber nach `c` sortiert.

Grund für dieses Verhalten ist [Windowing](#Windowing).

![](AnalyticalFunctionSortingExample.png)

# Windowing
Mit Windowing lässt sich steuern auf welche Werte innerhalb der Teilmenge die Analytische Funktion bezogen wird.

Die Berechnung erfolgt dabei immer relativ zur aktuellen Position.

Syntax:
`<window_mode> BETWEEN <start_point> AND <end_point>`

- CR (Current Row) Meint die aktuelle Zeile
- PG (Peer Group) Meint alle Zeilen, die im Sortierargument den selben Wert haben.
- CG (Current Group) Meint die Peer Group der aktuellen Zeile

Eingezeichnet sind die jeweiligen Peer Groups
![](WindowingDefinitions.png)

Für den `<window_mode>` gibt es drei gültige Werte. Dabei beziehen sie sich entweder auf Zeilen oder Peer-Groups und sind physisch oder logisch.

![](WindowModeDefinitions.png)

![](WindowingStartAndEndPointOptions.png)

Dabei muss der Start vor dem Ende liegen, bei Berechnungen wie mit `RANGE` muss auf dem Datentyp gerechnet werden können.

Im folgenden einige Beispiele.
Der Pfeil deutet jeweils die Current Row an, der Markierte Bereich wird von der Aussage erfasst.
![](WindowingUnboundedPreceedingToCurrent.png)

![](Windowing1Preceeding1Following.png)

Falls keine `ORDER BY` Klausel angegeben ist, wird standardmäßig auf der gesamten Teilmenge gearbeitet
![](WindowingUnboundedPreceedingUnboundedFollowing.png)

Wenn eine beliebige `ORDER BY` Klausel angegeben ist, so wird standardmäßig anders ausgewählt
![](WindowingRangeUnboundedPreceedingCurrent.png)

## Unterschied ROW, RANGE, GROUP
``` SQL
SELECT id, year, sold,
SUM(sold) OVER(ORDER BY year
ROWS BETWEEN 2 PRECEDING AND 1 FOLLOWING) AS sum_ro,
SUM(sold) OVER(ORDER BY year
RANGE BETWEEN 2 PRECEDING AND 1 FOLLOWING) AS sum_ra,
SUM(sold) OVER(ORDER BY year
GROUPS BETWEEN 2 PRECEDING AND 1 FOLLOWING) AS sum_g
FROM T2
```

![](WindowingRangeVsRowVsGroup.png)

Rows greift auf die Aktuelle Zeile zu, sowie die beiden vorherigen und die nachfolgende.

Range bestimmt das akutelle Jahr und berechnet -2 und +1. Es werden die Werte mit Jahreszahlen im Intervall von $2017-2020$ angezeigt.

Groups bestimmt die aktuelle Gruppe, sowie die beiden existierenden vorherigen und die nächste folgende.


# Rangfunktionen


| Name         | Rang                                                                                   | Dichter Rang                                                                                    | Zeilennummer                                                                                                  |
| ------------ | -------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| SQL Keyword  | RANK                                                                                   | DENSE_RANK                                                                                      | ROW_NUMBER                                                                                                    |
| Beschreibung | Mario-Kart Mäßige Kollisionen. Bei zwei 1. Plätzen erhält der nächst-niedrigere Rang 3 | Bei Gleichstand erhalten alle den Besseren Rang, nächstniedriger wird ohne Lücke weitergezählt. | Auch bei Gleichstand wird jeder Rang nur einmal vergeben. Es wird willkürlich einer als Rang 1 und 2 gewählt. |




> [!MISSING] Unvollständig
> 'Zugriff bestimmter Zeilen'
> Seite 61ff.
