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
Bietet ein breiteres Dienstleistungsmodell als [Grid-Computing](#Grid-Computing)
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
- Kooperation nur über Nachrichtenaustausch ([IP](04%20Network%20Layer.md#Internet%20Protocol), [TCP/UDP](05%20Transport%20Layer.md), HTTP, [MQTT](08%20IoT.md#MQTT))
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
  Lösung: [Middleware](Middleware.md) (CORBA, Web-Services)
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
Klassische Betriebssysteme, erweitert um Netzwerkunterstützung. Die Existenz der anderen Rechner ist sichtbar, sie kommunizieren über verschiedene Protokolle.

## Distributed Operating System
Einheitliches Betriebssystem für ein ganzes Netzwerk von Rechnern. Soll Transparenz erreichen, erfordert aber enge Kooperation der OS-Kerne und ist daher eher weniger weit verbreitet.

Für größere Fehlertoleranz und Verfügbarkeit werden Daten oft repliziert. Dabei werden mehrere (Idealerweise) identische Kopien der Daten an verschiedenen Orten gespeichert. 
Mehrere Prozesse können parallel auf unterschiedliche Repliken zugreifen, somit wird eine höhere Performance möglich. Herausforderung ist dabei die Sicherstellung von Konsistenz.
Auch die Latenz kann verbessert werden, indem Anfragen an Kopien geleitet werden, die dem Client am nächsten sind.

# Konsistenz
Bei Änderungen müssen alle Repliken konsistent bleiben. Dies kann simpel durch [total geordnete atomare Multicasts](Verteilte%20Algorithmen.md#Multicast) erreicht werden. Dabei wird allerdings ein großer Teil der Performance geopfert.

Man wählt oft andere Konsistenzformen wie 'eventual Consistency'.

## Datenzentrische Konsistenzmodelle
Mehrere Clients greifen auf eine logische gemeinsame Datenbasis zu.
![](DatacentricConsistency.png)

Daten sind physisch verteilt und über mehrere Knoten repliziert. Dabei hat jeder Knoten eine lokale Kopie für Lese und Schreibzugriffe.
Trotz Verteilung und Replikation soll Konsistenz erreicht werden.


## Sequentielle Konsistenz
Ein Datenspeicher ist sequentiell konsistent, wenn jede Programmausführung so erscheint, als ob:
- alle Lese- und Schreiboperationen aller Prozesse in einer beliebigen Reihenfolge ausgeführt werden.
- Die Operation eines Prozess hält die im Programm vorgegebene Reihenfolge ein.

Alle Prozesse beobachten Schreibzugriffe in der selben Reihenfolge
![](SequentialConsistency.png)

Die Operationen aller Prozess werden zu einer globalen Reihenfolge zusammengeführt. Alle Prozess greifen auf einen logischen Speicher zu, auch wenn dieser physisch verteilt ist.

## Linearisierbarkeit
Ist noch stärker als Sequentielle Konsistenz.
Vorausgesetzt ist hierbei eine globale Uhrzeit die in allen Prozessen gelesen werden kann.
Die Reihenfolge der Operationen muss hier mit der Reihenfolge ihrer Zeitstempel konsistent sein.
Sehr schwer zu implementieren, oft nur für formale Verifikation von nebenläufigen Algorithmen verwendet.

## Kausale Konsistenz
Kausal abhängige Schreiboperationen müssen für alle Prozess in der selben Reihenfolge sichtbar sein.
Unabhängige Writes können in verschiedenen Reihenfolgen gelesen werden.

Notation: $W(x) a$ "Schreibe den Wert $a$ in Variable $x$"
Notation: $R(x) a$ "Lese Variable $x$, Ergebnis war $a$"

![](CausalConsistency.png)

Obwohl $c$ nach $b$ in $x$ geschrieben wurde, kann $P_3$ erst den Wert $c$ lesen. Lediglich das ursprüngliche $a$ darf nicht mehr sichtbar sein nachdem ein $b$ oder $c$ gelesen wurde.

Diese Kausale Inkonsistenz ist im zweiten Beispiel in $P_3$ zu sehen.

## Schwache Konsistenz
Zugriff auf geteilte Ressourcen wird über Synchronisationsvariablen koordiniert.

![](WeakConsistency.png)

Bei der Synchronisation $S$ werden vorherige Writes global sichtbar gemacht.

## Freigabekonsistenz
Eine Variante der schwachen Konsistenz mit Mutexen.

![](MutexConsistency.png)

Für kritische Blöcke kann nur ein Prozess arbeiten, so wird die Datensicherheit gewährt. Bei weniger sensiblen Operationen wie in $P_3$ kann auch ein alter Wert gelesen werden um die Geschwindigkeit zu erhöhen.

## Vergleich
![](ConsistencyComparison.png)


## Client-Zentrische Konsistenzmodelle
Hier liegt der Fokus darauf, jedem Client eine für ihn konsistente Sicht auf die Daten zu bieten.

Diese Art von Konsistenz bietet sich nur unter bestimmten Bedingungen an.
- Client-Unabhängigkeit
  Es gibt nur selten eine direkte Kommunikation zwischen zwei Clients
- Read-dominierte Workloads
  Schreibzugriffe erfolgen selten, die meisten Operationen sind nur lesend.

Szenarien sind beispielsweise
- DNS Caches
- Content-Delivery-Networks

### Eventual Consistency
Änderungen werden asynchron an Repliken verteilt. Das geschieht nicht direkt, sondern meist in Ruhephasen durch Hintergrundmechanismen.
Die Repliken konvergieren zu einem gemeinsamen Stand.

Wenn Clients dieselbe Replik für mehrere Arbeiten verwenden funktioniert dies gut. Beim Einsatz mehrerer Geräte oder mobilen Einsatz-szenarien können Probleme auftreten.

![](ClientCenteredConsistencyProblem.png)

### Monotonic Reads
Sind gegeben, wenn ein Lesen eines Wertes immer Werte liefert, die dem letzten Wert entsprechen oder neuer sind. 
Ein Prozess sieht nie alte Versionen nachdem er bereits eine neuere gesehen hat.
Der Client bewegt sich logisch nur vorwärts in der Zeit.

- $x_i$ sei eine Version des Datenobjekts $x$
- $x_i$ entsteht durch eine Folge von Schreiboperationen. 
  Diese Menge an Änderungen wird mit $WS(x_i)$ bezeichnet
- Mit neuen Writes entsteht aus der aktuellen Version $x_i$ eine aktualisierte Version $x_j$.
  $x_j$ folgt aus $x_i$ wird dargestellt als $W(x_i; x_j)$
- Wenn unklar ist, ob $x_i$ aus $x_j$ folgt, so schreibt man $W(x_i \mid x_j)$ 

![](MonotonicReads.png)

### Monotonic Writes
Sind gegeben, wenn eine ältere Schreiboperation niemals sichtbar wird, nachdem bereits eine neuere stattgefunden hat.
Umgesetzt wird ein solches Verhalten mit Strategien wie Sequenznummern, monotonen Timestamps oder Sequencern.

Die [kausale Konsistenz](Logisches%20Timing.md#Happened-Before) wird dadurch nicht ersetzt.

Jeder Prozess sieht stets die Effekte seiner eigenen Änderungen. Nach einer Änderung ist mindestens diese eigene Änderung in allen folgenden Leseoperationen sichtbar.

# Verteilungsprotokolle
Wo wann und von wem werden Replikate erstellt?

Platzierung und Verteilungsstrategie beeinflussen Verfügbarkeit, Latenz, Bandbreite, Konsistenz und Kosten.
Trade-Off zwischen ressourcenintensiverer, proaktiver Replikation und reaktivem Kopieren. Hier entsteht potenziell eine größere Latenz.

## Server Initiierte Replikate
Permanente Replikate:
Fest vorgegebene Kopien auf Serverseite für hohe Verfügbarkeit und Lastverteilung.

Push Cache:
Server entscheidet proaktiv, wo/wann Replikate erstellt werden.

## Client initiiertes Caching
Clients speichern häufig genutzte Daten lokal, Ziel sind dabei schnellere Zugriffszeiten.
Haltedauer ist meist zeitlich begrenzt um veraltete Informationen nicht zu nutzen.

## Verteilungsmechanismen
Wann werden Updates übertragen?
- Push / Pull
- Transport per Unicast / Multicast
- Heartbeat-Nachrichten

Wenn ein Update verteilt wird, kann dies auf verschiedene Arten geschehen. Sie verwenden unterschiedlich viel Bandbreite und empfehlen sich abhängig vom Lese- zu Schreib Verhältnis.

- Neues Objekt wird vollständig übertragen
- Update Operation. Nur die Änderung wird gesendet.
- Invalidation. Es wird nur benachrichtigt, dass die Daten verändert sind. Beim nächsten Zugriff wird neu angefordert.

# Konsistenzprotokolle
Primary-Basierte Protokolle:
Schreiben findet nur auf einem bestimmten Replikat statt. Simpler zu koordinieren, aber single Point of Failure und gesteigerte Last.

Replicate Write Protokolle:
Writes werden an mehreren Replikaten ausgeführt.

## Primary-basiert
Reads sind auf allen Kopien möglich.
Writes müssen auf bestimmten Primaries geschehen.

### Remote Write
Der Schreiber leitet die Operation an einen festen Primary weiter. Dieser ändert sich nicht.

![](RemotePrimary.png)
1. Write Anfrage wird gestellt
2. Anfrage wird an Primary weitergeleitet
3. Schreiben wird ausgeführt
4. Neuer Zustand an andere Replikate übertragen
5. Bestätigung des neuen Zustands
6. Bestätigung des Schreibens an ursprünglichen Server
7. Bestätigung an Client


### Local-Write
Der Schreiber wird selbst primary, dann führt er das Update lokal aus.
![](RemoteWriteExample.png)
1. Schreibanfrage
2. Server macht sich selbst blockierend zum Primary
3. Erhält Primary Status
4. Schreibt Änderungen
5. Sendet neuen Stand an alle Kopien
6. Empfang wurde von allen Kopien bestätigt
7. Bestätigung an Client, Nächste Replikation darf nun Primary werden

# Replicated Write Protokolle
## Active Replication
Update Operationen werden immer an alle Kopien weitergegeben. So sind alle Zustände stets deterministisch und korrekt. Neben den hohen Kosten für die Kommunikation ist auch eine global eindeutige Reihenfolge der Ereignisse notwendig.

## Quorum basierte Protokolle
Bei $N$ Replikaten muss jede Schreiboperation von $N_W$ und jede Leseoperation von $N_R$ Knoten bestätigt werden. Dabei muss $N < N_W + N_R$ gelten, um stets eine mehrheitliche Antwort zu gewährleisten. Bei jedem Schreiben wird eine Versionsnummer für den aktuellen Zustand vergeben, bei unterschiedlichen Antworten auf ein Lesen, wird der Wert mit der höchsten Versionsnummer verwendet.

Bessere Verfügbarkeit und Schreib-Skalierbarkeit auf Kosten einer komplexeren Quorum Wahl und Lese-Kosten.
 ![](QuorumBasedProtocoll.png)

