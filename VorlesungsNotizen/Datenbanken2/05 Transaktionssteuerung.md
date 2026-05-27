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


# Schedules
Sei $T$ eine einzelne Transaktion die aus beliebig vielen read- oder Write-Operationen besteht. $T = \{t_1, t_2, \dots, t_n\}$

Sie $\Psi$ eine Menge von Transaktionen $\Psi = \{T_1, T_2, \dots, T_m\}$

Ein Schedule $S$ ist eine Reihenfolge der Einzelschritte aller $T_i$ in $\Psi$, wobei für jede einzelne Transaktion die vorgegebene Reihenfolge der Einzelschritte eingehalten wird.


> [!NOTE] Begriff: Seriell
> Falls alle Operationen der Transaktionen direkt hintereinander ausgeführt werden, heißt der Schedule 'seriell'.
> Falls einzelne Transaktionen ineinander verzahnt ablaufen, so heißt der Schedule 'nicht-seriell'
> ![](ScheduleSeriellVsNichtSeriell.png)
> ^4c80f7

Bei einem Seriellen Schedule wird die Konsistenz der Datenbank zu jedem Zeitpunkt gesichert. Es wird jede Form der parallelen Ausführung verhindert.

Die Ausführungsreihenfolge ist relevant, evtl. kann eine andere Reihenfolge zu unterschiedlichen Resultaten führen, ohne dabei inkonsistente Zustände zu verwenden.

## Serialisierbarkeit
Wünschenswert sind [Nicht-Serielle Schedules](#^4c80f7) die diese Eigenschaft der Konsistenzerhaltung besitzen. Solche Schedules  nennt man 'serialisierbar'.

Diese Schedules können systematisch gefunden werden.
1. Zwei Transaktionen die einen Datenwert nur lesen, können keinen Konflikt verursachen
2. Zwei Transaktionen die ausschließlich auf unterschiedlichen Daten lesen oder schreiben, können keinen Konflikt verursachen.
3. Wenn zwei Transaktionen auf den selben Datenwert arbeiten und mindestens eine der beiden schreibt, kann es an dieser Stelle zu einem Konflikt kommen.

### Konflikt-Serialisierbarkeit
Die Serialisierbarkeit kann anhand eines Vorranggraphen (Serializable Graph) überprüft werden.
- Jede Transaktion $T_i$ ist ein Knoten des Graphen
- Wenn eine Transaktion $T_A$ auf einen zuvor von $T_B$ verwendeten Wert zugreift, so wird eine gerichtete Kante von $T_B$ nach $T_A$ eingefügt.
  Es handelt sich jeweils um einen Konflikt der Form $\text{Op}(B)-\text{OP}(A)$.
  Also dann ein "Read-Write-Konflikt" wenn das Lesen zeitlich früher stattgefunden hat.

Für diesen Schedule ergibt sich nach den genannten Regeln ein Graph mit drei Knoten.
![](SerialisableTestSchedule.png)

Da der Graph einen Zyklus enthält ist der vorliegende Schedule nicht Konflikt-Serialisierbar.
![](SerialisableTestScheduleGraph.png)

### Sicht-Serialisierbarkeit
Die [Konflikt-Serialisierbarkeit](#Konflikt-Serialisierbarkeit) ist sehr restriktiv.
Eine weniger strenge Form der Serialisierbarkeit ist die sog. "Sicht-Serialisierbarkeit".
Zwei Schedules $S_1$ und $S_2$ heißen "Sicht-äquivalent" g.d.w.
1. Falls $T_A$ in $S_1$ den initialen Wert der Variable $x$ liest, muss $T_A$ auch in $S_2$ den initialen Wert von $x$ lesen.
2. Falls einer Leseoperation auf einem Datenwert $x$ von Transaktion $T_A$ im Schedule $S_1$ eine Schreiboperation von $T_B$ vorausgeht dann muss dies auch in $S_2$ geschehen.
   Die lesenden Operationen haben also in beiden Schedules dieselbe Sicht.
3. Falls die letzte Schreibaktion auf einem Datenwert $x$ im Schedule $S_1$ von $T_A$ vorgenommen wurde, so muss auch in $S_2$ die letzte Schreibaktion von $T_A$ vorgenommen werden.

Ein Schedule $S$ ist "Sicht-Serialisierbar" g.d.w. $S$ zu einem seriellen Schedule $S_\text{ser}$ Sicht-äquivalent ist.

Im [gezeigten Beispiel](#Konflikt-Serialisierbarkeit) war der Schedule nicht Konflikt-Serialisierbar. Er ist jedoch Sicht-Serialisierbar da alle Bedingungen eingehalten werden. 
Der Serielle Schedule sei hierzu $S_\text{ser} = T_1, T_2, T_3$
1. $T_1$ liest in beiden Fällen den initialen Wert von $x$
2. Ist eingehalten, das initiale Lesen ist die einzige lesende Operation und findet jeweils als erste Handlung im Schedule statt.
3. Das letzte Schreiben wird jeweils von $T_3$ durchgeführt.


## Recovery-Fähigkeit
Ein Schedule ist Recovery-Fähig, wenn für jedes Paar $T_A$ und $T_B$ von Transaktionen gilt:
Falls $T_B$ einen Wert liest der zuvor von $T_A$ geschrieben wurde, so muss die `COMMIT` Anweisung in $T_A$ vor der in $T_B$ stattfinden.
![](RecoverableSchedules.png)

In diesem Beispiel wäre $T_1$ nicht Recovery-fähig, da ab $t_{11}$ die auf $T_1$ basierenden Änderungen von $T_2$ bereits dauerhaft committed sind.


> [!Example] Klausuraufgabe
> Bestimmung von Sicht- und Konfliktserialisierbarkeit von gleichzeitigen Transaktionen.
> Seite 4-38 bis 4-49
