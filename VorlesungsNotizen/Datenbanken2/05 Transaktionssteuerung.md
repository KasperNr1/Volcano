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