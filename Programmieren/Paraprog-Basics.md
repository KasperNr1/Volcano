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
