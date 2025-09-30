Mehrere Operationen werden in einer Transaktion als atomare Handlung ausgeführt. So bleibt auch bei Komplexeren Änderungen die Konsistenz der [Datenbank](Grundlagen.md#Datenbank) gewährleistet.

Beispielsweise bei der Durchführung einer Überweisung muss sichergestellt werden, dass kein Guthaben verschwindet oder hinzugefügt wird. Nur der bestehende Wert soll verschoben werden.

Eine Transaktion hinterlässt die Datenbank immer in einem gültigen Zustand. (Unter der Annahme dass sie sich zu Beginn in einem korrekten Zustand befindet.)


> [!Info] Steuerung
> Es stehen 3 Anweisungen zur Verfügen
> - `begin` zum Starten einer Transaktion
> - `commit` zum Abschließen einer Transaktion
> - `rollback` zum Zurücksetzen auf den Zustand von Beginn der Transaktion
>

# ACID
Ist beschreibt die grundlegenden Prinzipien einer Transaktion.

## Atomicity (Atomarität)
Die Transaktion ist unteilbar. Sie wird vollständig, oder gar nicht ausgeführt.

## Consistency (Konsistenz)
Eine Transaktion ist ein Übergang zwischen zwei logisch korrekten Zuständen einer [Datenbank](Grundlagen.md#Datenbank)

## Isolation
Jede Transaktion wird isoliert durchgeführt. Temporäre Verletzungen der Konsistenz sind nach außen nicht sichtbar und werden vor dem Ende der Transaktion stets behoben.

## Durability (Dauerhaftigkeit)
Effekte einer erfolgreichen Transaktion sind dauerhaft und dürfen nicht durch spätere Hard- oder Softwarefehler verloren gehen.