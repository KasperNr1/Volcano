# Definition
Ein Verteiltes System ist eines, das auf mehreren Computern ausgeführt wird, ohne dass dieser Fakt relevant für einen Benutzer ist


> [!Cite] Leslie Lamport
> Ein verteiltes System ist ein System, mit dem ich nicht arbeiten kann, weil irgendein Rechner abgestürzt ist, von dem ich nicht einmal weiß, dass es ihn überhaupt gibt.

Es gibt verschiedene Typen solcher Systeme:
- [Verteilte Rechensysteme](#Verteilte%20Rechensysteme)
- [Verteilte Informationssysteme](#Verteilte%20Informationssysteme)
- [Allgegenwärtige Systeme](#Allgegenwärtige%20Systeme)

## Verteilte Rechensysteme
Werden in der Hochleistungsberechnung eingesetzt
z.B. Fold@Home zur Proteinfaltung

- Cluster-Computing: Ähnliche Workstations, Hochgeschwindigkeits-LAN
- Grid-Computing: Locker verbundene, heterogene Rechner über weite Strecken

### Cluster
- Günstiger als Monolith Computer
- Erhöhte Verfügbarkeit
- Load Balancing


### Grid-Computing
Ressource aus unterschiedlichsten Organisationen werden zur Zusammenarbeit vereint.

Die verschiedenen Ressourcen werden von einem einheitlichen System verwaltet um Zugriffsrechte und Kooperation zu managen.

![](GridComputingLayers.png)

- Anwenungsschicht
  Leichte Nutzung der verteilten Ressourcen durch bereitgestellte Schnittstellen.
  Zentrale Dienste wie Authentifizierung, Autorisierung und Datenübertragung werden von [Middleware](Middleware.md) des Grids durchgeführt und bereitgestellt. 
- Kollektive Ebene
  Bietet Zugang zu mehreren Ressourcen, verwaltet Datenreplikation und Aufgabenplanung
- Ressourcenebene
  Verwaltung einzelner Ressourcen
- Verbindungsebene
  Anwendung von Kommunikationsprotokollen und Sicherheitsmaßnahmen
- Infrastruktur
  Stellt die Schnittstelle zu lokalen Ressourcen dar, ermöglicht die Teilung von diesen

Moderne Grid-Systeme werden zunehmend hybrid mit [Cloud-Ressourcen](#Cloud%20Computing) kombiniert um kurze Anfragestürme abzufangen.
Anwendungen werden i.d.R. containerisiert und mit Docker / Kubernetes ausgeführt.

### Cloud Computing
Bietet ein breiteres Dienstleisungsmodell als [Grid-Computing](#Grid-Computing)
Skalierbarkeit und Flexibilität

Virtueller Ressourcenpool, dynamisch anpassbar und Benutzerfreundlich.
Abrechnung auf "Pay-Per-Use" basis

![](CloudServiceModelResponsibilities.png)

Generell werden drei Varianten von Cloud-Diensten unterschieden
- Infrastructure as a Service:
  Virtuelle Maschinen werden zur Verfügung gestellt. Netzwerkanbindung und Storage werden verwaltet.
- Plattform as a Service:
  Laufzeitumgebungen, APIs und Dienste für Entwickler werden vom Anbieter gestellt.
- Software as a Service:
  Die gesamte Anwendung wird vom Anbieter gestellt und kann direkt vom Endanwender genutzt werden.

## Verteilte Informationssysteme
Integrieren mehrere Anwendungen zu einem firmenweiten Informationssystem.
In der Regel stellen einige wenige Server die Software bereit.

## Allgegenwärtige Systeme 

![](UbiquitousVsPervasive.png)
### Pervasive Systems
Diese Systeme sind mobil und in die Umwelt integriert. Oft gibt es hier keine herkömmliche UI, sondern Sensoren und Aktoren von "Smart Devices"

Ziel ist hier, dass Objekte intelligent werden und miteinander kommunizieren.

### Ubiquitous Systems
In diesen Systemen verschmilzt die Technik komplett mit der Umwelt. Technologie arbeitet unsichtbar im Hintergrund.
- Intelligent klimatisierte Räume
- Automatische Rollläden
Es ist keine direkte Interaktion vom Benutzer notwendig / keine aufdringliche.

### Mobile Computing
Sind ein spezialfall der allgegenwärtigen Systeme. Ihr Fähigkeiten können sich nach Standort / Netzwerk dynamisch ändern.
(Drucker im Heimnetz vs. Nur WLAN im Eduroam)

Daher gelten besondere Anforderungen an Diensterkennung / robuste Verbindungshandhabung


# Grundlagen Verteilter Systeme
## Warum Verteilung?
Zentrale Anwendungen sind oft sicherer und performanter. Verteilung senkt Kosten und verteilt Ressourcen.
Skalierbarkeit und Ausfallsicherheit sprechen für die Verteilung eines Systems.

## Charakteristika
- Ressourcen sind (weltweit) verteilt
- Kooperation nur über Nachrichtenaustausch ([IP](04%20Network%20Layer.md#Internet%20Protocoll), [TCP/UDP](05%20Transport%20Layer.md), HTTP, [MQTT](08%20IoT.md#MQTT))
- [Nebenläufigkeit](Paraprog-Basics.md#Parallel%20vs%20Nebenläufig) ist gegeben, jedoch nicht das primäre Ziel
- Keine Globale Uhr
- Kein eindeutiger Zustand
- Teilfehler sind möglich, einzelne Knoten können ausfallen
- Monitoring, Replikation und Fehlertoleranz sind erforderlich
- Grobkörnige Tasks, seltenere Kommunikation
- Heterogene Hardware und Betriebssysteme

## Herausforderungen
- Heterogenität
  Unterschiedliche Hardware, Netzwerke, Betriebssysteme und Programmiersprachen
  Lösung: Middleware (CORBA, Web-Services)
- Offenheit
  einfache Erweiterbarkeit durch öffentliche Schnittstellen und einheitliche Kommunikationsmechanismen
- Teilfehler
  unabhängige Ausfälle einzelner Knoten erfordern Fehlertoleranz, Redundanz und Recovery-Mechanismen
- Sicherheit
  Vertraulichkeit, Integrität und Verfügbarkeit, Authentifizierung und Autorisierung
- Skalierbarkeit
  Wachstum von Ressourcen oder Nutzerzahl ohne Leistunseinbruch oder hohe Kosten
- Konsistenz
  Synchronisation bei nebenläufiger Ausführung. Besonders schwierig da [keine gemeinsame Uhr](#Charakteristika) vorhanden ist.
- Betrieb
  Monitoring, Logging, und automatisierte Recovery sind wichtig

## Transparenz
Ein verteiltes System soll bei der Benutzung nicht unbedingt als solches erkennbar sein.

- Zugriffstransparenz
  Gleiches Verhalten bei Zugriff auf Lokale und entfernte Ressourcen
- Positionstransparenz
  Zugriff ohne Kenntnis über den Standort
- Nebenläufigkeitstransparenz
  Mehrere Prozesse beinträchtigen sich gegenseitig nicht
- Replikationstransparenz
  Nutzung mehrerer Instanzen ohne dass diese Repliken sichtbar sind
- Fehlertransparenz
  Fehler werden verborgen, Nutzer können weiterarbeiten
- Mobilitätstransparenz
  Ressourcen und Clients können verschoben werden ohne dass Nutzer dies merken
- Leistungstransparenz
  Systemoptimierung bei Laständerungen bleiben für Nutzer unsichtbar
- Skalierungstransparenz
  Das System kann wachsen, ohne dass Änderungen an der Architektur oder den Anwendungsalgorithmen notwendig sind
  

# Betriebstypen
## Network Operating System
Klassische Betriebssysteme, erweitert um Netzwerkunterstützung. Die Exsitenz der anderen Rechner ist sichtbar, sie kommunizieren über verschiedene Protokolle.

## Distributed Operating System
Einheitliches Betriebssystem für ein ganzes Netzwerk von Rechnern. Soll Transparenz erreichen, erfordert aber enge Kooperation der OS-Kerne und ist daher eher weniger weit verbreitet.
