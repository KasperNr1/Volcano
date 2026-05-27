# MVCC
## Motivation
Lesende Transaktionen sind sehr häufig und verändern die Daten nicht.
Schreibende Operationen sollen auf einer Kopie der Daten arbeiten, damit Transaktionen die nur lesen niemals warten müssen.

Um diese Kopien zu verwalten und nach Ende ihrer Verwendung wieder zu löschen ist eine Garbage-Collection notwendig.

## Basiskonzept
Jede Transaktion erhält eine ID die als Zeitstempel verwendet wird. Jedes Datenobjekt speichert die ID der Transaktionen die es zuletzt gelesen oder geschrieben haben.

## Ablauf
Bei Zugriffen werden mehrere Varianten der Datenobjekte gespeichert. Jeder Eintrag verweist auf die vorherige Version. So kann stets die aktuellste Version gefunden werden, die jede Transaktion lesen darf.

![](MvccExample.png)

### Lesen
Beim Lesenden Zugriff wird der neueste Wert bestimmt, der zum Zeitpunkt $t$ des Lesens verfügbar sein sollte. In den Metadaten wird der Eintragt für den letzten Zugriff ggf. angepasst.
$$
\text{RTS} = \max(\text{RTS}, t)
$$

Beim Schreiben wird unterschieden, ob die Anfragende Transaktion bereits den neuesten schreibenden Zugriff durchgeführt hat. 
1. Falls $\text{WTS} = t$ gilt, wird der Wert aktualisiert und $\text{WTS} = \text{RTS} = t$ gesetzt.
2. Andernfalls wird eine neue Kopie angelegt, die Zeitstempel werden eingetragen und ein Verweis auf die nächstältere Version gesetzt.



> [!Example] Klausuraufgabe
> Zugriffe eines gegebenen Schedules mit MVCC verwalten und Daten mit Metadaten [korrekt fortsetzen](#Ablauf)


# Optimistische Techniken
Ausführung  von Transaktionen in drei Phasen
1. Lesephase (Bezogen auf Datenbank)
   Es wird eine lokale Kopie erstellt und entsprechend bearbeitet.
2. Validierungsphase
   Prüft auf Kollisionen mit parallel ablaufenden Transaktionen. Löst Konflikte durch Zurücksetzen von Transaktionen.
3. Schreibphase
   Nach einer erfolgreichen Validierung kann in die Datenbank geschrieben werden. Lesetransaktionen werden ohne Aufwand beendet.

Da Transaktionen bei Problemen abgebrochen werden, ist dieser Ansatz nur sinnvoll, wenn Konflikte zwischen Transaktionen nur selten sind. 
Da wenig Aufwand während dem Bearbeiten von Transaktionen notwendig ist, kann so sehr performant gearbeitet werden. Deadlocks, [Dirty Reads](05%20Transaktionssteuerung.md#Dirty%20Read) und [Kaskadierende Rollbacks](06%20Concurrency%20Control.md#Kaskadierende%20Rollbacks) werden dabei vermieden.

## Rückwärtsorientierte Validierung
Um eine Transaktion $T$ zu validieren wird geprüft, ob in allen Änderungen $T_j$, die seit Beginn von $T$ validiert wurden, Objekte vorkommen, die auch in $T$ verwendet werden. Falls keine Objekte geteilt sind, kann geschrieben werden. Sonst muss $T$ Zurückgerollt werden. 

![](BackwardsorientedValidation.png)

Diese Unschärfe ist eine Schwäche des Verfahrens. Es kann nicht genau bestimmt werden, was gelesen oder geschrieben wurde. Somit ist es nicht möglich präzise Korrekturen durchzuführen.

Da eventuelle Rücksetzungen erst zum Ende der Transaktion stattfindet, werden viele Arbeitsschritte unnötigerweise ausgeführt.
Da nur die aktuell validierende Transaktion zurückgerollt werden kann, besteht die Gefahr des Verhungerns. Besonders bei großen Transaktionen ist diese Gefahr relevant.

## Vorwärtsorientierte Validierung
![](ForwardorientedValidation.png)

Zum Validierungszeitpunkt wird geprüft, ob eine andere, aktuell laufende Transaktion einen Wert gelesen hat, den die prüfende Transaktion verändern möchte.

So lässt sich einige Arbeit vermeiden da Konflikte früher erkannt werden. Außerdem kann die ältere Transaktion bevorzugt werden um das Verhungern zu vermeiden.

# Kombinationen
Es gibt verschiedene Möglichkeiten die Vorteile von [Pessimistischen](06%20Concurrency%20Control.md#Pessimistisch) und [Optimistischen Techniken](#Optimistische%20Techniken) zu kombinieren. So wird die Geschwindigkeit der optimistischen Verfahren mit der Erfolgsrate der Pessimistischen kombiniert. Grundsätzlich kann z.B. immer Optimistisch gearbeitet werden und nur bei sehr langen oder fehlgeschlagenen Transaktionen auf ein pessimistisches Modell gewechselt werden.

Auch ist eine Strategie denkbar, bei der Zugriffe auf 'Hot-Spots' pessimistisch gehandhabt werden, während Arbeit auf seltener verwendeten Daten optimistisch und schnell ist.