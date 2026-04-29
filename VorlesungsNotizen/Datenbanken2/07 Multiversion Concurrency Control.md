# Übung
|![](ProbeAufgabeSupportUndKonfidenz.jpg)

| Regel               | Support | Konfidenz |
| ------------------- | ------- | --------- |
| Milch -> Brot       | 5/12    | 5/8       |
| Brot-> MIlch        | 5/12    | 5/7       |
| Milch -> BUtter     | 3/12    | 3/8       |
| Eier -> MIlch       | 2/12    | 2/4       |
| Milch, Brot -> Eier | 1/12    | 1/5       |
| Butter -> Brot      | 4/12    | 4/5       |


# MVCC
## Motivation
Lesende Transaktionen müssen niemals warten.


> [!Missing] Fehlt
> Seite 5-58

## Basiskonzept
Jede Transaktion erhält eine ID die als Zeitstempel verwendet wird. Jedes Datenobjekt speichert die ID der Transaktionen die es zuletzt gelesen oder geschrieben haben.

## Ablauf
Bei Zugriffen werden mehrere Varianten der Datenobjekte gespeichert. Jeder Eintrag verweist auf die vorherige Version. So kann stets die aktuellste Version gefunden werden, die jede Transaktion lesen darf.

![](MvccExample.png)

### Übung

| ID  | A   | WTS | RTS | TID  | Zeiger |
| --- | --- | --- | --- | ---- | ------ |
| 1   | 100 | 1   | 1   | 1000 | NULL   |
| 1   | 100 | 1   | 6   | 1001 | 1000   |
| 1   | 100 | 1   | 7   | 1002 | 1001   |
| 1   | 110 | 7   | 7   | 1002 | 1001   |
| 1   | 110 | 7   | 8   | 1003 | 1002   |
| 1   | 110 | 7   | 9   | 1004 | 1003   |
| 1   | 220 | 9   | 9   | 1004 | 1003   |
| 1   | 220 | 9   | 10  | 1005 | 1004   |
|     |     |     |     |      |        |

# Optimistische Techniken
Ausführung  von Transaktionen in drei Phasen
1. Lesephase (Bezogen auf Datenbank)
   Es wird eine lokale Kopie erstellt und entsprechend bearbeitet.
2. Validierungsphase
   Prüft auf Kollisionen mit parallel ablaufenden Transaktionen. Löst Konflikte durch Zurücksetzen von Transaktionen.
3. Schreibphase
   Nach einer erfolgreichen Validierung kann in die Datenbank geschrieben werden. Lesetransaktionen werden ohne Aufwand beendet.

Da Transaktionen bei Problemen abgebrochen werden, ist dieser Ansatz nur sinnvoll, wenn Konflikte zwischen Transaktionen nur selten sind. 
Da wenig Aufwand während dem Bearbeiten von Transaktionen notwendig ist, kann so sehr performant gearbeitet werden und dabei Deadlocks, dirty Reads und Kaskadierende Rollbacks vermieden werden.

## Rückwärtsorientierte Validierung
Um eine Transaktion $T$ zu validieren wird geprüft, ob in allen Änderungen $T_j$ seit Beginn von $T$ validiert wurden Objekte vorkommen, die auch in $T$ verwendet werden. Falls keine Objekte geteilt sind, kann geschrieben werden. Sonst muss $T$ Zurückgerollt werden. 

![](BackwardsorientedValidation.png)

Diese Unschärfe ist eine Schwäche des Verfahrens. Es kann nicht genau bestimmt werden, was gelesen oder geschrieben wurde. Somit ist es nicht möglich präzise Korrekturen durchzuführen.

Da eventuelle Rücksetzungen erst zum Ende der Transaktion stattfindet, werden viele Arbeitsschritte unnötigerweise ausgeführt.
Da nur die aktuell validierende Transaktion zurückgerollt werden kann, besteht die Gefahr des Verhungerns. Besonders bei großen Transaktionen ist diese Gefahr relevant.

## Vorwärtsorientierte Validierung
![](ForwardorientedValidation.png)

Zum Validierungszeitpunkt wird geprüft, ob eine andere, aktuell laufende Transaktion einen Wert gelesen hat, den die prüfende Transaktion verändern möchte.

So lässt sich einige Arbeit vermeiden da Konflikte früher erkannt werden. Außerdem kann die ältere Transaktion bevorzugt werden um das Verhungern zu vermeiden.
