# Grundbegriffe
- Failure|
  Beobachtetes Fehlverhalten, System reagiert nicht wie erwartet
- Error
  Inkorrekter interner Zustand (Nicht beobachtet)
- Fault
  Physikalischer Defekt, Periodisch oder Dauerhaft
- Fault Tolerance
  System fällt trotz Fault nicht aus.


> [!Info] Byzantinisch
> Stammt aus der Geschichte, beschreibt böswilliges Verhalten.
> Ein Byzantinischer Ausfall beschreibt willkürliche, zufällig falsche Antworten

Zusätzlich wird zwischen "Omissionsfehlern", bei denen eine Handlung unterlassen wird und "Commissionsfehlern" unterschieden. Im zweiten Fall wird eine Handlung vorgenommen, aber nicht korrekt ausgeführt.

# Fault Masking
Fehlertolerante Systeme müssen Fehler vor anderen Prozessen verbergen. Wichtigste Technik dazu ist Redundanz.


## Triple Modular Redundancy
![](TripleModularRedundancy.png)

Jede Komponente wird dreifach umgesetzt, nach jeder Stufe sitzt ein Mehrheitsschalter. So kann der Ausfall einer jeder beliebigen Komponente maskiert werden.

Da dieser Einsatz vieler Redundanter Bauteile sehr teuer ist, wird es typischerweise nur bei sehr kritischen Systemen angewendet (Raumfahrt / Industrie)

# Prozess-Elastizität
Prozesse werden in Gruppen repliziert. Nachrichten an eine Gruppe werden von allen Mitgliedern empfangen. (Typisch: [Totally ordered Multicast](06%20Verteilte%20Mutexe.md#Empfangsreihenfolge))

Organisiert können diese Gruppen flach (symmetrisch) sein oder hierarchisch mit einem zentralen Koordinator.

## k Fehlertoleranz
Um einen stillen Crash in $k$ Prozessen zu maskieren, sind $k+1$ Prozesse nötig. 
Um einen byzantinischen Fehler zu maskieren, werden $2k+1$ Prozesse gebraucht.

## Two Army Problem
Mit unzuverlässiger Kommunikation ist ein allgemeiner Konsens unmöglich. 

## Byzantinische Generäle
Viele Prozesse müssen Konsens finden. Die Kommunikation ist verlustfrei, allerdings arbeiten ein Teil der Prozesse nicht korrekt.

Um einen Konsens erreichen zu können, müssen $> \dfrac23$ korrekt arbeiten. Dann kann in jeder Kombination von mehr als $50\%$ der Teilnehmer eine korrekte Mehrheitsentscheidung getroffen werden.

# Zuverlässige Kommunikation
Zuverlässige Kommunikation ist der Schlüssel zur Fehlertoleranz. Verlässliche Übermittlung vereinfacht die Fehlerbehandlung.

# Wiederherstellung
Nach einem Error soll das System selbst in einen korrekten Zustand zurückgeführt werden.
Dazu kann ein Rollback auf einen vergangenen Zustand verwendet werden, oder mit 'Forward-Recovery' in einen neuen, korrekten Zustand übergegangen werden.

## Checkpointing
![](Checkpointing.png)

Der Einsatz von Checkpoints vereinfacht die Recovery, verwendet allerdings Speicherplatz und Koordination.

### Independent Checkpointing
Prozesse Speichern ihren Zustand unabhängig voneinander. Die Implementierung ist hier sehr einfach, aber beim Rollback kann es zu einem Domino-Effekt kommen. Abhängige Prozesse müssen ggf. ebenfalls zurückrollen, eventuell sogar bis zum Anfang.

### Koordinierte Checkpoints
Es wird ein global konsistenter Checkpoint erzeugt. Mit dem [Algorithmus von Lamport](05%20Logische%20Uhren.md#Snapshot%20Algorithmus%20nach%20Chandy%20&%20Lamport) können diese erzeugt werden.

Alternativ kann ein blockierendes 2 Phasen Modell verwendet werden. Dies vereinfacht das Erstellen der Checkpoints, blockiert aber alle Prozesse im Verlauf.

### Lokale Checkpoints mit Message-Logging
![](MessageLogging.png)

Der Absturz eines Knoten kann lokal behoben werden, die eingegangenen Nachrichten zwischen Checkpoint und Crash können repliziert werden.
Um mit potentiell doppelt gesendeten Nachrichten keine Probleme zu verursachen, ist eine komplexere Wiederherstellungslogik notwendig.

# Verteilte Dateisysteme
Ziel ist das gemeinsame Nutzen von Dateien im Netz. Dabei gibt es verschiedene Anforderungen die für den korrekten Betrieb notwendig sind.
- [Verschiedene Transparenzen](VorlesungsNotizen/VerteilteSysteme/01%20Grundlagen.md#Transparenz)
- Konsistenz & Nebenläufigkeit um gleichzeitige Updates zu behandeln
- Replikation und Caching um Latenz und Verfügbarkeit zu verbessern
- Unterstützung verschiedener Betriebssysteme

## Flat File Service
Bietet idempotente Operationen auf Dateien an.
- `read`
- `write`
- `create`
- `move`
- `get / set attributes`

Dateien werden durch UFIDs (Unique File IDs) eindeutig markiert.
Ein Directory Service kann Dateinamen oder Pfade in diese UFIDs übersetzen.

## NFS
![](ArchitekturNfs.png)

Wurde 1984 von SUN eingeführt und arbeitet plattformübergreifend. Die Server sind zustandslos und prüfen daher Zugriffsrechte bei jeder Anfrage neu. Dadurch wurden Spoofing Angriffe möglich.

Über Erweiterungen wie Firewalls, Mount-Optionen und kryptographischer Authentifizierung wird das System sicher. Diese werden ab NFSv4 unterstützt.

Um Anfragen zu beschleunigen wird mit einem Cache gearbeitet, Cache auf Clientseite muss regelmäßig überprüft werden, um nicht mit veralteten Daten zu arbeiten.
Auf Serverseite werden Änderungen teilweise erst im Cache geschrieben, bei einem Ausfall gehen diese jedoch verloren. Ein Write-Trough schreibt direkt auf die Disk, ist jedoch langsamer.

NFS garantiert keine strikte Konsistenz des Client Caches, Anwendungen müssen diese Problematiken selbst erwarten und behandeln.

# Verteilter Shared Memory
Ziel ist die Bereitstellung eines gemeinsamen Speichers über mehrere Knoten hinweg.
Grundtechnik ist die seitengesteuerte (Page based) Speicherverwaltung pro Knoten.

![](DifferentStorageLocations.png)
![](DifferentStorageLocationsExplanation.png)

Der verteilte Speicher kann Byte- oder Objektorientiert sein. 

Um Konsistenz zu wahren wird meist ein 'local write' verwendet. Die beschreibbare Page wird zur schreibenden Instanz migriert. Um zu lesen wird eine Kopie der Daten angefordert.

Die Verwaltung der beschreibbaren Seite wird von ihrem 'Owner' verwaltet. Dazu kann ein Zentraler Manager die Rolle übernehmen oder eine feste Verteilung benutzt werden. Auch Multicasts sind möglich, so wird der Manager ersetzt.
Dynamische Strategien sind möglich, bei der Prozesse einen vermuteten Owner kennen und die Anfragen im Fehlerfall weitergeleitet werden.


> [!Info] Forschung
> Die Thematik ist eher in der Forschung angesiedelt, Shared Memory wird aktuell in keiner größeren Anwendung produktiv eingesetzt
