Das Testen auf [Sicht-Serialisierbarkeit](05%20Transaktionssteuerung.md#Serializable) ist ein NP-Vollständiges Problem. Aus Effizienzgründen kann daher nicht jede Transaktion auf Serialisierbarkeit geprüft werden.
In der Praxis werden Protokolle verwendet die serialisierbare Schedules sicherstellen.

Synchronisationsmethoden werden in die beiden Kategorien 'pessimistisch' und 'optimistisch' eingeteilt.

# Synchronisationsmechanismen
## Pessimistisch
Diese Verfahren blockieren Transaktionen allgemein, falls Konflikte drohen. 

### Preclaiming
Alle benötigten Datenobjekte werden zu Beginn einer Transaktion gesperrt.
So wird eine große Menge Resets vermieden, auch [Deadlocks](Parallele%20Probleme.md#Deadlocks) sind nicht möglich.
Sperrzeiten sind insgesamt unnötig lang, außerdem ist es nicht immer bekannt welche Objekte im Verlauf der Transaktion verwendet werden.

### Sperrverfahren
Verwendet zwei Arten von Sperren.
[Read-Write Locks](Prozessverwaltung.md#Read-Write%20Locks) erlauben das gleichzeitige Lesen durch mehrere Transaktionen, jedoch nur eine Schreiboperation.

Die Sperren können auf verschiedenen Objekten gesetzt werden.
- Gesamte Datenbank
- Dateien
- Blöcke
- Tabellen
- Zeilen
- Felder

Feinere Granularität erlauben einen höheren Durchsatz an Transaktionen, verursachen allerdings auch mehr Verwaltungsaufwand da mehr Sperren gesetzt, geprüft und zurückgenommen werden müssen.

### Two Phase Locking 
Mit dem 'Two phase locking' (2PL) Protokoll werden alle `lock` Operationen vor allen `unlock` Operationen durchgeführt. Somit genügt das Protokoll auch [Regel 4 des Fundamentalsatzes.](#Fundamentalsatz%20des%20Sperrens)

#### Kaskadierende Rollbacks
Der Fehlschlag einer Transaktion kann auch einen Rollback einer weiteren Transaktion erzwingen, wenn die Sperre auf ein Objekt vor dem finalen Commit freigegeben wurde und bereits von einer anderen Transaktion verwendet wird.

Dieses Problem kann vermieden werden, indem alle Sperren gleichzeitig am Transaktionsende freigegeben werden. 
![](Rigoroses2PL.png)
Es gibt noch eine Strikte Variante, bei der im Gegensatz zur eben gezeigten Rigorosen Version die lesenden Sperren auch früher freigegeben werden können.
![](Striktes2PL.png)

#### Deadlock Vermeidung
Um [Deadlocks](Parallele%20Probleme.md#Deadlocks) zu vermeiden ist es notwendig alle benötigten Sperren direkt zur Beginn zu erlangen. Die Ermittlung dieser Menge ist allerdings eventuell aufwändig.

Eine andere Strategie verwendet Zeitstempel. So wird sichergestellt dass nur in 'eine Richtung' gewartet wird und keine Zyklen entstehen.

##### Wait-Die
Ältere Transaktionen warten auf jüngere.
1. T1 hält eine Sperre
2. T2 fordert die Sperre an
3. Entscheidung
	- Falls T1 jünger ist, so wartet T2 bis die Sperre frei ist
	- Falls T1 älter ist, bricht T2 ab und startet nach 'gewisser Zeit' mit altem Zeitstempel neu

```
if ts(Ti) < ts(Tj) then
	WAIT(Ti)
else
	ROLLBACK(Ti) // Die
```

##### Wound-Wait
Funktioniert umgekehrt zu [Wait-Die](#Wait-Die). Jüngere Transaktionen warten auf ältere.
```
if ts(Ti) < ts(Tj) then
	ROLLBACK(Tj) // Wound
else
	WAIT(Ti)
```


> [!Info] Rollback
> Mit 'Rollback' in [Wait-Die](#Wait-Die) und [Wound-Wait](#Wound-Wait) ist kein vollständiger Rollback gemeint, sondern ein zurücksetzen auf den letzten vergangenen Checkpoint. (Siehe Abschnitt 'Recovery')


> [!Example] Klausuraufgabe
> Bestimmung der Ausführungsreihenfolge bei mehreren Transaktionen mit [Wound-Wait](#Wound-Wait) und [Wait-Die](#Wait-Die) algorithmus.

![](Pasted%20image%2020260421114012.png)


| Zeit | Aktion               | Lock-Owner | Pro 1 (21) | Pro 2 (15) | Pro 3 (15) |
| ---- | -------------------- | ---------- | ---------- | ---------- | ---------- |
| 1    | 1 Startet            |            | 0          | 0          |            |
| 2    | 2 Startet            |            | 1          | 0          |            |
| 3    | 3 Startet            |            | 2          | 1          | 0          |
| 5    | 2 fragt Lock an      | 2          | 4          | 3          | 2          |
| 10   | 3 fragt lock an      | 2          | 9          | 8          | 7          |
| 10   | 3 muss auf 2 Warten  | 2          | 9          | 8          | 7          |
| 14   | Checkpoint erreicht  | 2          | 13         | 12         | 7          |
| 16   | 1 fragt Lock an      |            |            |            |            |
| 16   | 2 wird abgebrochen   | 1          | 15         | 0          | 7          |
| 19   | 2 Startet neu (CP 0) | 1          | 18         | 0          | 7          |
| 22   | 1 Beendet            | -          | 21         | 3          | 7          |
| 22   | 3 Erhält Lock        | 3          |            | 3          | 7          |
| 22   | 2 Fragt Lock an      |            |            |            |            |
| 22   | 3 Wird abgebrochen   | 2          |            | 3          | 0          |
| 25   | 3 Startet neu (CP 0) | 2          |            | 6          | 0          |
| 32   | 3 Fragt Lock an      | 2          |            | 13         | 7          |
| 32   | 3 Muss auf 2 Warten  | 2          |            | 13         | 7          |
| 34   | 2 Beendet            | -          |            | 15         | 7          |
| 34   | 3 Erhält Lock        | 3          |            |            | 7          |
| 42   | 3 Beendet            | -          |            |            | 15         |


| Zeit | 1                | 2                | 3                | 4     |
| ---- | ---------------- | ---------------- | ---------------- | ----- |
| 5    | hat A            |                  |                  |       |
| 6    |                  | hat B            |                  |       |
| 7    |                  |                  | hat C            |       |
| 8    | Wartet auf B (2) |                  |                  |       |
| 9    |                  |                  |                  | hat D |
| 10   |                  |                  | Wartet auf A (1) |       |
| 11   |                  | wartet auf C (3) |                  |       |

A wartet auf B wartet auf C wartet auf A; D ist separat

Deadlock mit ABC


> [!Example] Klausuraufgabe
> Deadlocks erkennen mit Waiting-For-Graph

#### Sperrprotokolle
Die Kompatibilitätsmatrix eines Objekts zeigt welche Übergänge des Sperrmodus möglich sind.
![](Kompatibilitätsmatrix.png)
Ein `+` bedeutet dass die Sperre vergeben werden kann, ein `-` verbietet es.

Die folgenden Beispiele basieren auf dieser Anfragereihenfolge:
![](LockingOrderExample.png)

##### RX Verfahren

|     | R   | X   |
| --- | --- | --- |
| R   | +   | -   |
| X   | -   | -   |
Es wird gleichzeitiges Lesen erlaubt, eine Änderungstransaktion schließt den Zugriff durch alle anderen Transaktionen aus.
![](RxExample.png)

Zu $t_4$ könnte $T_3$ schreiben, nur der Leser muss auf der alten Version weiter arbeiten.
Auch $T_4$ könnte zu $t_6$ mit dem alten Wert arbeiten, nur die neue Änderung von $T_3$ darf hier nicht sichtbar sein.

##### RAX Verfahren
Es wird neben read (R) und exclusive-write (X) noch eine analyse (A) Sperre eingeführt.

|     | R   | A   | X   |
| --- | --- | --- | --- |
| R   | +   | +   | -   |
| A   | +   | -   | -   |
| X   | -   | -   | -   |
-  Zulassen von Lesetransaktionen, auch wenn Änderungstransaktion läuft
- Für Änderungstransaktion wird Objekt kopiert, Änderungen folgen auf Kopie, Objekt mit Kopie besitzt A-Sperre (Analyse)
- Lesetransaktionen arbeiten auf Originalversion
- Sind alle Lesetransaktionen beendet, werden alle A-Sperren in X-Sperren verwandelt, Kopie wird zum Original (Sperrkonversion)

![](RaxExample.png)

##### RAC Verfahren
Lange Lesetransaktionen beim [RAX Verfahren](#RAX%20Verfahren) implizieren lange Wartezeiten für schreibende Transaktionen.
Beim Ende einer Transaktion werden A-Sperren hier in C-Sperren verwandelt. Dabei wird eine Kopie des ursprünglichen Objekts erstellt die durch die C-Sperre angezeigt wird. Lesende Aktionen versuchen erst auf Kopie 1 zuzugreifen, greifen bei Problemen auf Kopie 2 zu.


|     | R   | A   | C   |
| --- | --- | --- | --- |
| R   | +   | +   | +   |
| A   | +   | -   | -   |
| C   | +   | -   | -   |

![](RacExample.png)

In $t_7$ kann hier gleichzeitig die neue, zweite Kopie gelesen werden und das Ergebnis in der ersten Kopie an die Stelle des Originals kopiert werden.

# Fundamentalsatz des Sperrens
1. Vor dem Zugriff muss eine Sperre gesetzt werden
2. Transaktionen fordern eine von ihr gesetzte Sperre nicht erneut an
3. Sperren durch andere Transaktionen müssen beachtet werden.
4. Es gibt eine Wachstumsphase in der Sperren gesammelt werden, und eine Schrumpfphase in der sie wieder freigegeben werden.
5. Spätestens zum Transaktionsende müssen alle Sperren wieder freigegeben werden.


> [!Info] Begründung
> Während die Regeln 1-3 und 5 offensichtlich sind, scheint 4. nicht direkt sinnvoll. 
> Diese Vorgabe ist allerdings notwendig, um Serialisierbarkeit herzustellen.
> 
