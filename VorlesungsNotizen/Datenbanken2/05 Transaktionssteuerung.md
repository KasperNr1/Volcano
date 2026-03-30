Soll Konsistenz und Zuverlässigkeit gewährleisten, vor allem bei
- Hardwarefehlern
- Softwarefehlern
- Mehrbenutzerzugriff

Siehe auch [Definition der Transaktion](Transaktionen.md)

# Mehrbenutzerprobleme
Es können beim unkontrollierten Zugriff durch mehrere Benutzer einige Probleme Auftreten
- [Lost Update](#Lost%20Update)
- [Inconsistent Read](#Inconsistent%20Read)
- [Dirty Read](#Dirty%20Read)
- [Non Repeatable Read](#Non%20Repeatable%20Read)
- [Phantomproblem](#Phantomproblem)


## Lost Update
![](LostUpdate.png)

Das Resultat ist $90$ anstatt der erwarteten $190$. Der zweite Prozess darf den Wert nicht lesen, bevor der erste nicht vollständig geschrieben hat.

## Inconsistent Read
$T_1$ versucht von $K_1$ auf $K_2$ umzubuchen.
$T_2$ möchte den Durchschnitt der drei Konten berechnen.
![](InconsistentRead.png)

Auch hier ist das Ergebnis falsch, es wurden Zahlen gelesen bevor die Schreib-Operation abgeschlossen wurde.

Der Fehler ist weniger schlimm, da keine Schreibende Operation Fehler enthält. Bei großen Datenmengen wäre auch die Abweichung im Ergebnis vermutlich weniger deutlich.

## Dirty Read
![](DirtyRead.png)

Das Ergebnis ist falsch, da der Zwischenstand aus $T_2$ weiterverarbeitet wurde. Die zweite Transaktion selbst wurde jedoch wieder zurückgesetzt.

## Non Repeatable Read
![](NonRepeatableRead.png)

Hier würden verschiedene Ergebnisse aus der gleichen Aktion geliefert werden.

## Phantomproblem
![](PhantomProblem.png)

Für $T_1$ ist nicht ersichtlich warum die Anzahl der Kunden sich verändert.


# Isolationslevel
Bei der Konfiguration können bewusst manche Konsistenzverletzungen in Kauf genommen werden um den Durchsatz zu erhöhen.

```SQL
SET TRANSACTION [Modus] | ISOLATION LEVEL [Isolationslevel]
```

Werte für `Modus`
- `READ ONLY`
- `READ WRITE`

Werte für Isolationslevel
- `SERIALIZABLE` 
  Vollständige Serialisierung
- `REPEATABLE READ`
  Phantomproblem kann auftreten
- `READ COMMITTED`
  Nicht wiederholbares Lesen ist möglich
- `READ UNCOMMITTED`
  Zusätlich sind dirty Reads möglich

![](IsolationsLevel.png)

## Read Uncommitted
Erlaubt das Lesen von Daten aus anderen Transaktionen, bevor diese comitted wurden.

Sehr effizient, keine Sperren.
Sollte nur für Lesetransaktionen ohne großen Genauigkeitsanspruch verwendet werden.

## Read Committed
Erlaubt nur das Lesen von gültigen Daten.

Lost-Update und Phantome sind weiterhin möglich, wird typisch für Lesetransaktionen verwendet.

Jeder gelesene Wert ist gültig, jedoch kann wiederholtes Lesen zu unterschiedlichen Resultaten führen.

## Repeatable Read
Gewährt konsistente Lese- und Schreibzugriffe. Wird realisiert durch Sperren auf Objekte die Gelesen oder geschrieben werden. Phantome sind weiterhin möglich, ebenfalls können mit diesen Einschränkungen [Deadlocks](Parallele%20Probleme.md#Deadlocks) entstehen.

Wird für schreibende Transaktionen verwendet.

## Serializable
Verhindert alle Anomalien indem seriell ausgeführt wird. Entsprechend ist die Effizienz und der Durchsatz deutlich geringer als bei den weniger sicheren Zugriffsformen.

Wird für Szenarien angewandt die höchste Anforderungen an Konsistenz haben.


> [!Example] Klausuraufgabe
> Bestimmung von Sicht- und Konfliktserialisierbarkeit von gleichzeitigen Transaktionen.
> Seite 4-38 bis 4-49



