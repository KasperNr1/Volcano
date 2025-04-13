# Definition Betriebssystem
Software zur Steuerung und Überwachen von Programmen
Abstrahiert die Komplexität der Hardware

# Sichten
## OS als erweiterte Maschine
Abstraktion von Hardware und Schnittstellen des Systems. Benötigtes Detailwissen sinkt.
Anzahl der Abstraktionsschichten ist variabel, allgemein wird jedoch Performance gegen Abstraktion abgewogen.

![](TopDownSicht.png)
## OS als Ressourcenverwalter
Verwaltung aller Systembestandteile.
Ordnet und kontrolliert Verteilung von Ressourcen an anfordernde Programme, insbesondere bei Konflikten.

![](BottomUpSicht.png)

# Operationsmodi
Definiert den Ausführungskontext (Zugriffsrechte auf Hardware, verfügbare Maschinenbefehle)

## Kernel Mode
Exklusiv für Betriebssystem
Vollständiger Zugriff auf Hardware
Alle Befehle sind verfügbar

## User Mode
Eingeschränkter Zugriff auf Hardware und Befehlssatz
Für Benutzerprogramme


# Hardware-Komponenten
## Prozessor
"Frequency Wall" motiviert Entwicklung von Multi-Core-Prozessors

Bestandteile
- Befehlssatz
- Register
	- Allgemeines Register
	- Spezielle Register
		- Programm Counter
		- Stackpointer
		- Statusregister
- Cache

### Arbeitsweise
1. Befehl laden
2. Decodieren
3. Ausführen

Wird für jeden Befehl bis Programmende wiederholt.
Laden von Befehlen aus Speicher sehr langsam (Notwendige sollten vom OS in möglichst hohe Speicherebene gelagert werden)

#### Optimierung
CPU-Pipelining

Paralleles Laden, Decodieren und Ausführen mehrerer Befehle
![](CpuPipelining.png)

Superskalare CPU

Mehrere Ausführungseinheiten (Festkommaarithmetik, Gleitkomma, Bool'sche Operationen)
Viele Befehle werden gleichzeitig in Puffer geladen, einer pro Einheit ausgeführt
![](SuperscaleCPU.png)

"Hyperthreading" (Umschalten von [Threads](Paraprog-Basics.md#Threads) innerhalb von Nanosekunden) als Technologie von Intel
Hyperthreading bietet keine echte Parallelität, reale Parallelität bedarf mehrerer physischer Kerne.

### Mehrkernchips
Tatsächliche Existenz mehrerer physischer Kerne

![](SharedMemory.png)

Verschiedene Konzepte zur Aufteilung von Speicher, Koordinationsaufwand und maximal Verfügbarer Cache (Kurzzeitig) je nach Anwendungsfall vorteilhafter.

## Speicher
- CPU-Register
- CPU-Cache
- Arbeitsspeicher
- Festplatte

Anforderungen an Speicher
- Performanter Zugriff
- Großes Speichervolumen
- Günstige Preise

![](SpeedSpaceTradeoff.png)

Optimierung der Speicherzugriffe ist Aufgabe des OS (Pre-Fetching)
Aktualisierung und Invalidierung ebenfalls.

![](MemoryWall.png)

# Aufgaben des OS
## Abstraktion
Verbergen der komplexen Hardware-Ansteuerung
Bereitstellung einfacher APIs
Abstraktion des Maschinenbegriffs
![](MaschinenBegriff.png)


## Verwaltung von Hardwareressourcen  
Ansteuerung der Geräte
Interrupt-Steuerung
Fehlererkennung & Behebung
- Prozessor(en)  
- Hauptspeicher  
- Festspeicher  
- Peripheriegeräte  
- Rechenzeit

## Prozessverwaltung
Prozess [Scheduling](Paraprog-Basics.md#Scheduler)
Überwachung von Prozessen während der Ausführung
Erzeugen und Beenden von Prozessen
## Speicherverwaltung
Abstraktion Speicherzugriff und Hierarchie
Effiziente Speicherverwaltung
Bereitstellung von Speicher für Prozesse
Zugriffs-Sicherheit
## Dateisystemverwaltung
Abstraktion des Zugriffs auf persistente Speicher
Erstellen, Lesen und Löschen von Dateien und Ordnern
Caching-Mechanismen
Zugriffssicherheit und Verwaltung von Berechtigungen
Verwaltung physischer / Logischer Speicher (Massenspeicher-Verbund: RAID)
Defragmentierung / Partitionierung
## Sicherheit und Rechteverwaltung
Authentifizierung : Wer ist es
Autorisierung : Darf er das
Verwaltung Zugriff auf Ressourcen
Kryptographische Features (Digitale Signaturen / Public-Key)
Ausfallsicherheit
Backup und Recovery
## Bereitstellung einer Benutzer-Schnittstelle (Shell)
Kommandozeile oder GUI zur Verwaltung des Betriebssystems
Konfiguration von Berechtigungen
Ausführen und Beenden von Benutzerprogrammen

# Arten von Betriebssystemen
## Großrechner
- Sehr Hohe Ein-/Ausgabeleistung
- Hohe Kapazität an Ressourcen (1000< Festplatten, 1000< TB)
- Auf Parallele Aufgaben ausgelegt
- 3 Arten der Prozessverwaltung
	- Stapel / Batch-Processing
	- Dialog / Interaktive
	- Timesharing
- Beispiel OS/360 und OS/390

## Server
- Entworfen für Server (Leistungsfähige PCs oder Großrechner)
- Zentrale Verantwortung, gleichzeitiges Bearbeiten viele Benutzeranfragen
- Anwendungen sind Druckserver, Dateiserver, Webserver
- Beispiele Solaris, FreeBSD, Linux, Windows Server 20xx

## Multiprozessor
- Fassen mehrere Prozessoren zu einem System zusammen
- Besondere Anforderungen
	- Kommunikation zwischen Prozessen
	- Konsistenz
	- Speicherverwaltung

## PC
- Unterstützt große Masse unterschiedlicher Anwender
- Möglichst umfangreiches Tooling (Browser, Media Player, Editor) 
- Robust und fehlertolerant

## Handheld und mobil
- Kleine Hardwaresysteme
- Zeichnen sich durch Vielzahl kleiner Apps von Drittanbietern aus
- Herausforderungen
	- Energieeffizienz
	- User Experience
	- Dev Experience
- OS meist auf eine zentrale Aufgabe ausgerichtet

## Embedded
- Fokus auf Rechensysteme die Geräte steuern die nicht direkt als Computer angesehen werden
- User können allgemein keine eigene Software installieren
- Beispiele:
	- Mikrowelle
	- Autos
	- MP3-Player

## Sensorknoten
- Fokus auf Sensorknoten
	- Gebäudeschutz
	- Überwachung von Landesgrenzen
	- Temperatur / Niederschlagsmessungen
- Verwendung kleiner OS die ereignisorientiert oder periodisch arbeiten
- Wie bei [Embedded](#Embedded) sind Anwendungen vorinstalliert

## Echtzeit
- Erfüllen Zeitkritische Aufgaben
- Reaktionszeit wichtiger als verarbeitete Datenmenge
- Weiche Echtzeit
	- Verzögerungen nicht erwünscht aber tolerierbar (Audio- / Multimediasysteme)
- Harte Echtzeit
	- Verspätung nicht tolerierbar (Medizingeräte, Airbags)

## Smartcard
- Laufen auf Smartcards mit winziger Hardware
- Verwendet für Bezahlvorgängen
- Ausgelegt auf minimale Kapazitäten