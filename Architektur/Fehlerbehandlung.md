# Grundbegriffe
- Failure
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
Prozesse werden in Gruppen repliziert. Nachrichten an eine Gruppe werden von allen Mitgliedern empfangen. (Typisch: [Totally ordered Multicast](Verteilte%20Algorithmen.md#Empfangsreihenfolge))

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
Es wird ein global konsistenter Checkpoint erzeugt. Mit dem [Algorithmus von Lamport](Logisches%20Timing.md#Snapshot%20Algorithmus%20nach%20Chandy%20&%20Lamport) können diese erzeugt werden.

Alternativ kann ein blockierendes 2 Phasen Modell verwendet werden. Dies vereinfacht das Erstellen der Checkpoints, blockiert aber alle Prozesse im Verlauf.

### Lokale Checkpoints mit Message-Logging
![](MessageLogging.png)

Der Absturz eines Knoten kann lokal behoben werden, die eingegangenen Nachrichten zwischen Checkpoint und Crash können repliziert werden.
Um mit potentiell doppelt gesendeten Nachrichten keine Probleme zu verursachen, ist eine komplexere Wiederherstellungslogik notwendig.