# Arten der Aufgabenteilung
Man unterscheidet primär zwischen Aufteilung der einzelnen Arbeitsschritte oder der Aufgaben.
Beim Kochen kann beispielsweise nach Zubereitung der einzelnen Gerichten aufgeteilt werden, oder nach den einzelnen Aufgaben in der Erstellung eines Gerichts.
4 Köche sollen 100 Burger zubereiten. Anhand dieses Beispiels wird der Unterschied anschaulich erklärt.
## Datenparallelismus
Jeder Koch bereitet 25 Burger zu.
![](Datentrennung.jpg)
Eventuell kann es hier zu Wartezeiten bei den geteilten Ressourcen kommen.
Diese Aufteilung ist robuster, da Ausfälle kompensiert werden können. Jeder Koch ist in der Lage die Aufgabe alleine zu beenden und kann eventuell die Arbeit eines anderen zu vervollständigen.
## Aufgabenparallelismus
![](Aufgabentrennung.jpg)
Jeder Koch hat eine spezielle Aufgabe die er für alle 100 Burger ausführt. Beispielsweise die Brötchen oder das Fleisch vorzubereiten.
Diese Art der Aufteilung bietet sich an, wenn es für die einzelnen Aufgaben Optimierungsstrategien gibt, bzw. Vorteile entstehen mehrere auf einmal zu bearbeiten. Eventuell können Rechenergebnisse wiederverwendet werden.
Allerdings können Fehler in einem Produktionsschritt nicht ausgeglichen werden.
# Prozess
Jeder Prozess besitzt:
- Programm
- Heap-Speicher
- Stack-Speicher
- Prozessregister / Stackpointer / Program Counter
- Liste verwendeter Ressourcen

Mehrere Prozesse können gleichzeitig ausgeführt werden (Multitasking)

# Fork
Forken ist das Erstellen eines neuen [Prozess](#Prozess), wobei ein aktiver Prozess eine vollständige Kopie von sich selbst anfertigt.
Man spricht auch von einem "Kindprozess".
Die Erstellung ist sehr Zeitintensiv (~20ms), da direkt mit dem Betriebssystem kommuniziert werden muss.
Dies ist bei längeren Aufgaben sinnvoll, wenn nicht jeder zwischenschritt direkt von dem vorherigen abhängt.
Das Ergebnis des Kindprozesses muss übertragen werden.

# Parallel vs Nebenläufig
Gleichzeitige Ausführung mehrerer Prozesse macht sie nebenläufig. 
Man spricht nur von Parallelität wenn sie völlig isoliert von einander arbeiten und sich keine [Ressourcen](#Ressourcen) teilen müssen.

# Ressourcen
- RAM
- ROM
- Maus
- Tastatur
- Dateien
Zugriff auf diese wird vom Betriebssystem verwaltet.

# Pipes
Sind eine Möglichkeit um mit laufenden Programmen zu kommunizieren. Eine Pipe hat ein schreibendes und ein lesendes Ende.
Beide Enden sind gepuffert und werden blockierend verwaltet, sodass keine Daten verloren gehen. Wenn kein Platz im Puffer verfügbar ist  wird der Eingang blockiert.
Man spricht von einer "Broken Pipe" wenn nicht beide Enden verwendet werden, also Daten in einer Pipe landen die nie gelesen werden.
# Scheduler
Ist Teil des Betriebssystems und kümmert sich um die Verwaltung von Prozessen. Dabei sind einige Informationen über die Prozesse relevant:
- OS-Syscalls die beschreiben, ob der Prozess in seinem aktuellen Zustand unterbrechbar ist.
- Ressourcen:
  Eine Liste an verwendeter Dateien
- Programm-Counter:
  Aktuelle Stelle der Ausführung (Lesezeichen in der .exe)
- Register
- RAM:
  Verwendete Bereiche im Speicher
- Stackpointer
- User priviliges

# Threads
Auch "Lighweight-Processes" genannt haben sehr ähnliche Eigenschaften wie ein [Prozess](#Prozess).
Größter Unterschied ist, dass Threads sich Heap-Speicher Teilen, während jeder Prozess seinen eigenen Heap besitzt.
Sie sind leichter zu erstellen und haben die Möglichkeit in dedizierte Wartezustände überzugehen. Wenn ein Thread nicht weiter rechnen kann, da eine benötigte Ressource belegt ist oder er von einer [Kontrollstruktur](Prozessverwaltung.md#Kontrollstrukturen) geblockt wird, erhält er die Markierung "Waiting". So kann der [Scheduler](#Scheduler) schneller prüfen ob es sinnvoll ist dem Thread Rechenzeit zuzuteilen.

# Synchronisation
Der Einsatz mehrerer Threads sollte möglichst wenig Überschneidung in den verwendeten Ressourcen haben. Um [Race-Conditions](Parallele%20Probleme.md#Race-Conditions) zu vermeiden gibt es viele Möglichkeiten Threads zu synchronisieren.
Dabei wird eine Markierung verwendet die die aktuelle Verwendung signalisieren und Andere einschränken oder bis zur erneuten Freigabe aussperren.
Unterschiedliche [Kontrollstrukturen](Prozessverwaltung.md#Kontrollstrukturen) bieten hier Möglichkeiten verschiedenste Verhaltensweisen zu implementieren.

# Mutex
Kurz für ''mutual exclusion'' beschreibt mehrere Instanzen die sich gegenseitig vom Zugriff auf Ressourcen ausschließen können. Die Implementierung kann mittels unterschiedlicher [Kontrollstrukturen](Prozessverwaltung.md#Kontrollstrukturen) erfolgen.

# Tests
Automatisierte Tests von Nebenläufigkeit ist quasi nicht-existent/unmöglich