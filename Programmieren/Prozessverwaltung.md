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
Diese Kontrollstrukturen sind allgemeine Konzepte und nicht exklusiv in Java verfügbar. Sie alle bieten Möglichkeiten die zeitliche Ausführung von Threads zu verwalten. 
Die Seltenheit in der praktischen Anwendung steigt hier mit der Reihenfolge in der Auflistung.

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
Begrenzt die Menge an Threads in einem Bereich auf einen maximalen Wert. Abgesehen von den Selbstkosten der Verwaltung des Semaphores hat diese Struktur keinen Einfluss auf den Fluss des Programms falls die Schranke $n$ an erlaubter Threads größer ist als die Anzahl an Threads.n

## Latch
Funktioniert als Untergrenze für eine Anzahl Threads in einem bestimmten Bereich.
Die ersten $n-1$ Threads werden am Beginn des Blocks aufgehalten bis $n$ Threads den Eingang erreicht haben. Sobald das Limit erreicht ist, werden alle wartenden und zukünftigen Threads nicht weiter aufgehalten. 

## Barrier
Lässt Threads salvenweise arbeiten. Wie bei einem [Latch](#Latch) werden die ersten paar aufgehalten, jedoch setzt sich das System nach dem Durchlassen der Wartenden selbst zurück. So können zukünftige Threads nicht ungehindert fortfahren und müssen wieder warten um Teil der nächsten Gruppe zu sein.

# Thread-Pools
Funktionieren analog zum [Pre-Fork Modell](#Pre-Fork%20Modell). Eine Sammlung Worker-Threads wird bereitgehalten um anfallende Aufgaben zu bearbeiten. Besonders wenn die Workload aus vielen simplen Aufgaben besteht ist das ständige Erzeugen und beenden von Threads ein Faktor der die Laufzeit beeinflusst.
Eine Liste mit Aufgaben wird bearbeitet, jeder einzelne Thread darf seine Aufgabe erst dann beenden, wenn sie fertig ist.
Falls Ressourcen geteilt werden kann es sein dass die Bearbeitung der Aufgaben im [Konflikt](Paraprog-Basics.md#Mutex) zueinander steht.
Um wartende Threads im Pool zu verhindern gibt es eine Variante mit "Work-Stealing".
Rekursive Berechnungen die eine neue Aufgabe an den Threadpool übergeben können [Deadlocks](Parallele%20Probleme.md#Deadlocks) verursachen, da der aktuelle Thread auf das Ergebnis wartet. Das kann aber nicht berechnet werden bevor die vorherigen Aufgaben nicht abgeschlossen sind um den Thread freizugeben.

## Thread-Pools mit Work Stealing
Hier können Threads deren aktuelle Aufgabe gerade blockiert wird eine neue Aufgabe beginnen statt zu warten. Die neue Aufgabe erhält dabei keine Priorität. Sobald die blockierte Ressource freigegeben wird, bearbeitet er die ursprüngliche Aufgabe und legt die angefangene zweite Aufgabe wieder nieder. Sinnvoll ist dieses Vorgehen nur dann, wenn Zwischenschritte einzeln gegangen und deren Ergebnisse wieder abgespeichert werden können.

## Anwendung
Webserver die große Mengen simpler Aufgaben bearbeiten sind häufige Einsatzorte von Threadpools. Sie sind extrem vielseitig einsetzbar.

## Optimale Größe
Die Menge an [Threads](Paraprog-Basics.md#Threads) zu optimieren ist schwierig. Sie hängt stark von der aktiven Rechenzeit pro Aufgabe ab.
Bei Aufgaben die keine Wartezeiten haben, sollte ein Thread pro CPU-Kern verwendet werden.
Bei mehr Wartezeit empfiehlt es sich auch mehr Threads zu verwenden.

Bei $n$ CPU-Kernen und $p\%$ aktiver Rechenzeit ist als Richtwert der Einsatz von $n * \frac1p$ Threads zu empfehlen.

# Koordination von Prozessen
Manche [Verteilte Algorithmen](Verteilte%20Algorithmen.md) benötigen einen Koordinator oder Leader, der spezielle Aufgaben übernimmt.
Ziel der Wahlalgorithmen ist es einen solchen Leader zu bestimmen.
Die Aufgabe des Leaders ist dabei nicht besonders komplex, es muss nur sichergestellt sein, dass exakt ein Knoten diese Aufgaben ausführt.

Annahmen:
- Jeder Prozess im System hat eine eindeutige ID
- Jeder Prozess kennt die IDs aller anderen Prozesse
- Üblich wird ein Prozess nach willkürlichem Kriterium als Koordinator gewählt (Höchste / Geringste ID o.ä.)

Algorithmus muss schnell ein Ergebnis liefern das allen Teilnehmern der Wahl bekannt ist, wobei er robust gegen Ausfälle während der Wahl sein muss.

Verschiedene Wahlverfahren sind
- [Heartbeat](#Heartbeat)
- [Ringalgorithmen](#Ringalgorithmen)
- [Heartbeat](#Heartbeat)
- [Konsensbasierte Anätze](#Konsensbasierte%20Anätze)

## Bully Algorithmus
Wenn die Koordinatorlosigkeit festgestellt ist, wird ein Wahlprozess gestartet. Dabei wird der Prozess zum Koordinator, der während der Wahl die höchste ID hat.

Ein Prozess startet den Wahlprozess und fragt alle anderen Prozesse mit höherer ID ob sie Koordinator sein wollen.
Falls er nach einer gewissen Zeit keine Antwort erhält, ernennt sich der Prozess selbst zum Koordinator.

Fall ein Prozess antwortet beendet der Initiator seine Wahl, der antwortende höhere Prozess startet seinerseits eine Wahl.

![](BullyCoordinatorExample.png)

## Ringalgorithmen
Annahme ist, dass jeder Prozess in einem logischen Ring angeordnet ist und seine Nachbarn kennt.


> [!NOTE] Sichtbarkeit
> Alle Knoten kennen alle anderen Knoten, so kann auch bei fehlenden Antworten auf den nächsten Prozess weitergeleitet.
> Die Beschränkung auf Kommunikation mit dem Nachbarn kommt nur aus dem Algorithmus


Wahl läuft ab, indem eine Nachricht mit eigener Prozess ID an Nachbar geschickt wird. Wenn der Nachbar aktiv ist, fügt er seine eigene ID zur Nachricht hinzu und leitet sie weiter an seinen Nachfolger. Wenn ein Knoten nicht antwortet, wird die Nachricht unverändert an den nächsten Knoten weitergeleitet.

Sobald die Nachricht beim Absender ankommt, enthält sie eine Liste aller aktiven Prozesse. Der Prozess mit höchster ID wird als Koordinator bestimmt, diese Nachricht wird entsprechend an die Nachfolger übermittelt.

## Heartbeat
Regelmäßige Nachrichten erkennen Ausfälle schnell. Die Erkennung eines Ausfalls löst Neuwahlen aus.

> [!Info] Nicht Klausurrelevant
> Wurde nur genannt, nicht näher behandelt


## Konsensbasierte Ansätze
Für robuste replizierte Systeme mit starker Konsistenz

> [!Info] Nicht Klausurrelevant
> Wurde nur genannt, nicht näher behandelt
