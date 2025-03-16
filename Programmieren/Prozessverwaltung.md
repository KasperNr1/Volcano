Das Anlegen eines neuen [Prozess](Paraprog-Basics.md#Prozess) ist sehr zeitintensiv (20ms)
Eine Möglichkeit variierende Mengen von Aufgaben zu verwalten ist mit dem Pre-Fork-Modell.

# Pre-Fork Modell
Prozesse werden nicht erst angelegt wenn sie benötigt werden.
Stattdessen wird ein Pool an wartenden Prozessen erzeugt die deutlich schneller mit der Bearbeitung einer Aufgabe beginnen können.
Dabei verwaltet ein einzelner Fater-Prozess die Erstellung und Aufgabenverteilung der Kind-Prozesse.
Er selbst kümmert sich nur darum, die Antworten zurück zu liefern.

## Vorteile
Wenn ein Kind crasht kann seine Aufgabe von einem anderen Kind-Prozess erneut bearbeitet werden. So ist der Fehlschlag einer einzelnen Berechnung nie Grund für den Absturz des Gesamtsystems.
Die Berechtigungen der Kinder können auf ein absolutes Minimum eingeschränkt werden, so dass Beispielsweise nur auf einzelne Dateien zugegriffen werden darf.

## Nachteile
Anzahl der benötigten Kind-Prozesse ist variabel und stets unsicher.
Der Vater muss so regelmäßig neue Prozesse anlegen und alte töten um die Menge wartender Kinder konstant zu halten.

# Kontrollstrukturen
## Locks
### Klassische Locks
Ein geteiltes "Lock-Objekt" wird an alle beteiligten [Threads](Paraprog-Basics.md#Threads) übergeben.
Lock.lock() ist ein Methode die von jedem Thread aufgerufen werden kann, aber nur falls das Lock verfügbar ist.
Wenn es bereits verwendet wird, so muss die Ausführung an der aufrufenden Stelle pausieren bis das Lock wieder freigegeben wird.
Da keine Begrenzung auf die Wartezeit existiert, sollte die Freigabe des Locks in einem ```finally{}``` Block stattfinden, um auch im Falle einer Exception im blockierenden Threads den Anderen die weitere Ausführung erlaubt.

Locks können reentrant sein, dass bedeutet rekursiven Aufrufen ein wiederholtes passieren des Locks zu gestatten.

### Read-Write Locks
Das gleichzeitige Lesen eines Wertes ist unproblematisch. [Probleme](Parallele%20Probleme.md) entstehen bei Überschneidung von mindestens einer Schreibenden Operation.
Um Programme nicht unnötig zu verlangsamen kann zwischen Read- und Write Zugriff unterschieden werden.
So werden beliebig viele Aufrufe von ``readLock()`` toleriert, nur bei ``writeLock()`` wird der entsprechende Bereich tatsächlich abgesperrt. Es wird gewartet bis alle Lesevorgänge beendet wurden und dann der Zugriff für den Schreiber gestattet. 
Die tatsächliche Zugriffsart der Programmabschnitte muss manuell überprüft und eingehalten werden.

## Synchronised
Einige Sprachen implementieren spezielle Keywords um Synchronisierung zu ermöglichen.
Darunter auch [Synchronised](Parallelisierung%20in%20Java.md#Synchronised)

## Semaphore
TODO
## Latch
TODO

## Barrier
TODO
