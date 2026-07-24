# Middleware
![](Middleware.png)
Middleware kann verschiedene Aufgaben übernehmen, "Kommunikationsorientierte Middleware" abstrahiert nur die Netzwerkprogrammierung.
"Anwendungsorientierte Middleware" unterstützt auch höhere Dienste verteilter Anwendungen.

### Aufgaben
- Verbergen von Verteilung und Heterogenität
- Bereitstellung einer einheitlichen Schnittstelle
- Bereitstellung allgemeiner Dienste

### Funktionen
- Kommunikationsdienste, Notifications
- Authentifizierung / Autorisierung / Verschlüsselung

### Beispiele
#### Klassisch
- CORBA
- Enterprise Java Beans
- .NET
- Web Services

#### Moderner
Verwendet Cloud-Native-Patterns wie "Containerisierung", "Orchestrierung", "Observability"

- Kubernetes
- Service Mesh
- Message Streaming
- Serverless und API-Gateways

## Kommunikationsorientierung
- Nachrichtenaustausch
- Abstraktion der Heterogenität
	- Big vs. Little Endian
	- Zeichencodierung
	- Unterschiedliche Programmiersprachen
- Fehlerbehandlung
	- Timeouts / Retries
	- Duplikaterkennung 
	- Wiederherstellung

# Rollen von Prozessen in Middleware
## Clientprozesse
Kurzlebig, initiiert Interprozesskommunikation (IPC)

## Serverprozesse
Langlebige Prozesse die Dienste für IPC anbieten

## Peerprozesse
Kurzlebig, kombiniert Rollen. Sie initiierten Anfragen und bieten Dienste an.

Nützlich bei symmetrischer Kommunikation.

# Modelle
## Peer to Peer
Verteilt Koordination und Synchronisation.

Typisch in
- Router
- File-Exchange Systeme
- verteilte Speichersysteme

## Client/Server
- Asymmetrisch: Client nutzt Dienste des Servers
- Zentrale Verwaltung
- Hybride Rollen: Server können als Client Dienste von anderen Servern in Anspruch nehmen
- Verbreitung: ca. $80\%$ der Systeme

![](ClientServerModell.png)

### Kooperierende Server
![](CoopServer.png)
Ein Netzwerk von Servern arbeitet transparent. So können auch große Aufgabenmengen bewältigt werden.

### Proxy-Server
![](ProxyServer.png)
Proxy als Schnittstelle zwischen Clients und Servern. Kann Informationen durch Cashing behalten und Rechenlast der Server reduzieren.

### N-Tier Architektur
Verfeinert die [Client/Server](#Client/Server) Architektur. Durch klare Trennung von Verantwortlichkeit soll Skalierbarkeit, Wartbarkeit und Sicherheit erhöht werden.

Typisch sind 2,3 oder 4 -Schicht-Architektur

#### 2 Tier
Gesamter Stack wird in zwei Teile getrennt, einer läuft auf dem Client, der andere auf dem Server

![](2Tier.png)

Einfach zu implementieren, hohe Performance aber schlechter skalierbar.

#### 3 Tier
Trennung von Datenhaltung, Anwendungslogik und Darstellung

- Client als Webbrowser zur Darstellung
- Middle Tier: Webserver für Geschäftslogik
- Server-Tier: Datenbankserver für persistente Speicherung

![](3Tier.png)

Zentrale Verwaltung der Logik bietet bessere Skalierbarkeit und klare Trennung der Verantwortung.

#### 4+ Tier
Die Anwendungslogik selbst lässt sich ebenfalls aufteilen. Für Darstellung oder Datenhaltung ist das nicht sinnvoll.

Für besonders große Systeme oder solche die mit Firewalls separat gehalten werden sollen kann diese Strategie verwendet werden.

![](4Tier.png)

# IPC
Beschreibt den Nachrichtenaustausch hinweg über verschiedene Prozesse (Lokal oder über Netzwerkgrenzen)

Verschiedene Mechanismen wie Ports, Mailboxes und Streams sind verfügbar.

Programmierschnittstellen sind Sockets, Datagramme (UDP) und Streams (TCP)

Umgesetzt wird diese Kommunikation mit verschiedenen [Programmiermodellen](Programmiermodelle.md#Programmiermodelle)

## Synchrone Kommunikation
Sender und Empfänger blockieren bei Sende- / Empfangsaufruf.

Enger Kopplungsgrad führt zu einfachem System, aber starken Abhängigkeiten bei Fehlern.
Besonders anfällig für Probleme bei langsamer Netzwerkverbindung oder Ausfällen
![](SyncCommunication.png)

## Asynchrone Kommunikation
Sender sendet Nachrichten ohne auf sofortige Antwort zu warten. (Fire and Forget / Callback / Event-Notification)

Programmierung ist etwas komplexer (Message Queues, Warteschlangen, Callbacks, Retries).
![](AsyncCommunication.png)

Einsatz hängt von Latenz, Zuverlässigkeit und Kopplungsgrad ab.


> [!Tip] Timeouts
> Nachrichten können verloren gehen. Es muss eine Reihe von Exceptions behandelt werden.
> - Wiederholtes Senden von Nachrichten
> - Abbruch nach fehlgeschlagenem Wiederholen
> - Behandlung doppelter Anfragen (Neuer Versuch und originale Anfrage kommen gleichzeitig an)
> - Timeout bei fehlender Antwort

# Anwendungsorientierte Middleware
## Laufzeitumgebungen
Setzt auf Betriebssystem der Knoten auf.

Runtime erweitert OS um Ressourcenmanagement (Nebenläufigkeitsunterstützung, Verbindungsmanagement, Verfügbarkeit)
 
- [Pooling von Threads](Prozessverwaltung.md#Thread-Pools) und Verbindungen 

So werden Allokationskosten verringert, was eine geringere Latenz und bessere Skalierbarkeit bietet.

Runtime sorgt für Ausfallschutz bei Hardware oder Software Fehlern.
- Replikation von Daten / Diensten
- Clustering
- Load-Balancing

Handhabung von Sicherheit (Passwörter / Rechteverwaltung / Verschlüsselung / Integrität / Signaturen)

# Dienste
Stellen wiederverwendbare Laufzeitfunktionen für verteilte Anwendungen bereit.
- Service-Publikation
- Namensauflösung
- Sitzungsverwaltung
- Transaktionssteuerung

Ziel ist eine Entkopplung von Anwendung und Infrastruktur.

## Namensdienst
Zuordnung von Namen zu Referenzen / Adressen. Name als eindeutiger Identifier.
Clients fragen Dienste über Namen an, somit sind Adresswechsel möglich.

Entkoppelt Client von Server.

## Session Management
Jede Client Instanz erhält eine Session (User ID, Warenkorb)

Session Daten können transient oder persistent sein.
Speichern Serverseitig oder client-seitig (Cookies)

Middleware sorgt für transparente Zuordnung von Requests zu Sessions

## Transaktionsverwaltung
[Bildet eine Folge von Aktionen als atomare Operation](Transaktionen.md) ab.
1. Daten Holen
2. Modifizieren
3. Zurückschreiben


> [!WARNING] Problem
> Gleichzeitige Ausführung durch mehrere Clients erfordert Koordination


## Persistenzservice
Intelligente Schnittstelle zur Datenbank.

Häufigst als "Object-Relational-Mapper" (ORM)
Dabei werden Klassen als Tabellen, Attribute als Spalten und Objekte als Zeilen dargestellt.

# Komponentenmodell
Sind Einheiten die verschiedene Funktionalitäten abkapseln und über klar definierte Schnittstellen bereitstellen.

Bekannte Modelle sind:
- OSGi
- Jakarta EE / EJB / CDI
- Spring / Spring-Boot
- CORBA CCM
- Microservices + Kubernetes
- Serverless / Functions as a Service

Komponenten sind modular und versioniert. So ist eine klare Abtrennung und unabhängige Updates möglich.

Dependency Injection & Lifecycle:
Jakarta EE, Spring bieten standardisiertes Management

Verteilung und Betrieb:
Microservices / Kubernetes verschieben Komponentenmodell in die Infrastruktur.

Persistenz und Transaktionen:
Klassische Modelle (EJB / CCM) bieten TM / ORM. Moderne Ansätze nutzen eher eventual consistency.

# Middleware Technologien
Legacy: ORB / CORBA / EJB / CCM

Heute größerer Fokus auf Cloud-Native Plattformen, Microservices, Containerisierung und Orchestrierung (Kubernetes)

Frameworks:
- Spring Boot
- Quarkus
- Micornaut
- Jakarta EE

Messaging und Datapipelines:
- Apache Kafka
- RabbitMQ
- NATS

## Microservices
Lose gekoppelte Systeme, skalierbar pro Dienst.

Infrastruktur: Container (Docker) und Orchestrierung (Kubernetes).

Entwicklung nach dem "API-First" Ansatz. Observability und CI/CD.

## Kommunikation
- REST / HTTP
  Einfache Formate, weniger Performant bei vielen kleineren Aufrufen
- gRPC (Protobuf)
  Streaming, niedrige Latenz.
  Höherer Integrationsaufwand
- Event-driven / Streaming (Kafka)
  Persistente Event-Logs für fehlertolerante Pipelines
  Gut für Asynchronität, Entkopplung, Event Sourcing
  Erfordert Schema-Management und eventual Consistency

## Service Mesh
Trennt Networking-Funktionen wie mTLS, Retries und Traffic-Shaping vom Code.

Vereinheitlicht Observability durch Tracing, Metrics und Logs. Security durch Policy-Enforcement.

# Namendienste
Ziel ist das Auffinden und gemeinsame Nutzen von Ressourcen.
Eindeutige Identifikation soll die Unterscheidung von Entitäten ermöglichen.

Auflösung von Namen muss sehr schnell möglich sein. Konflikte werden durch Einsatz von Namespaces vermindert.


## Arten von Namen

| Namen                                                                                      | IDs                                                                                              | Adressen                                                                                  |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| Menschenlesbar und benutzerfreundlich.<br>Flexibel, unabhängig von tatsächlicher Position. | Spezielle Namen zur eindeutigen Identifikation<br>- weniger Menschenlesbar<br>- Global eindeutig | Maschinenlesbar,<br>kann sich bei Standortwechsel ändern. Dient der direkten Ansteuerung. |

## Namenssysteme
### Flache Namenssysteme
Eindeutige und bedeutungslose Identifikatoren (Hashes / UUIDs)

Keine Struktur im Name selbst.

Einfach und eindeutig, aber keine Informationen zur Suche oder Lokalisierung

### Strukturierte Namenssysteme
Besizen innere Struktur, unterstützen Gliederung und gezielte Suche.

Hierarchischer Aufbau (Dateipfade) oder komponentenbasiert (LDAP DN).

Struktur erlaubt delegation, lokale Suche und effizientes Caching. Erfordert aber entsprechende Auflösemechanismen

## Auflösen von Namen
### Flache Namen
Anfrage mit Identifikator wird per [Broadcast](Basics.md#Broadcast) an alle Knoten gesendet.
Entsprechender Knoten antwortet direkt mit seiner Adresse.
Z.B. DNS

Bei Adresswechseln kann eine Entität eine Kette an Weiterleitungszeigern hinterlassen.
Somit ist keine Globale Suche nötig, Ketten können aber sehr lang werden und eventuell Inkonsistent sein.

### Hierarchische Namen
Unterteilung in Domänen und Unterdomänen. Es entsteht eine Baumstruktur die sich effizient durchsuchen lässt.

![](StructuredNames.png)

Es kann auch ein Graph verwendet werden, bei dem einzelne Knoten über mehrere Wege erreicht werden können. Dabei wird in der Regel jedoch trotzdem nur ein einzelner Wurzelknoten verwendet. 
Dieser Graph darf keinen Zyklus enthalten.
![](StructuredNameNamespace.png)

Um einen Name oder Pfad aufzulösen, wird bei der aktuellen Position gestartet und zum nächsten Knoten übergegangen (Falls dieser existiert).
Dort wird der Prozess rekursiv wiederholt, bis der verbleibende Pfad leer ist oder ein Teilschritt nicht erfolgreich ist. Entsprechend wird die Ressource oder eine Fehlermeldung zurückgegeben.

# Scheduling
## Ziele
- Load Balancing
- Max-Systemleistun (Min Mittlere Antwortzeit)
- Minimale Kommunikation zwischen Knoten

## Ansätze
[Statisches](#Statisches%20Scheduling) und [Dynamisches scheduling](#Dynamisches%20Scheduling), wobei Verteilung entweder vor oder während der Ausführung geschieht.

### Statisches Scheduling
Die Zuordnung eines Jobs basiert auf seiner Struktur und Modellierung, sie wird vor der Ausführung festgelegt.

> [!NOTE] Komplexität
> Die Statische Verteilung von Aufgaben ist NP-komplex

Kommunizierende Prozesse über Graph-Partitionierung.
Nicht-Kommunizierende Prozesse Tasks: List Scheduling

#### Graph-Partitionierung
![](GraphPartitioning.png)

Jede Kante symbolisiert die Kosten für die Kommunikation zwischen zwei Knoten.
Es wird versucht die Knoten aufzuteilen und die Kosten für Kommunikation zwischen den Partitionen zu minimieren.

![](GraphPartitition1.png)

![](GraphPartitition2.png)

#### List Scheduling
Annahme ist, dass die Tasks nur vor / nach der Arbeit kommunizieren müssen. Während der Runtime kann minimaler Austausch stattfinden, sollte aber wenig Overhead besitzen.

Die Tasks werden als DAG (Directed, Acyclical Graph) modelliert.
![](ListScheduling.png)

In den Knoten steht der Name des Prozess, sowie seine Ausführungszeit.
Die Gewichte der Kanten beschreiben den Aufwand für die Kommunikation zwischen zwei Tasks.
Diese Zeitwerte werden vorausgesetzt, sie müssen aus historischen Aufzeichnungen oder anderen Quellen stammen.

Priorisierung kann veschieden erfolgen, (High Level First with Estimated Time) oder (Earliest Time First)

##### HLFET
Ziel ist die Minimierung der Gesamtausführungszeit.

Tasks mit dem höchsten "Level" (Kritischer Pfad) werden zuerst bearbeitet.
- $w(v)$ ist die Ausführungszeit von Task $v$
- $succ(v)$ ist der Nachfolger von Task $v$

Für Endknoten ist $level(v) = w(v)$. Sonst gilt:

$$
level(v) = w(v) + \max_{u \in \text{succ}(v)} level(u)
$$

> [!NOTE] Endknoten
> Ein Endknoten ist der "unterste" im Graph, also der keine Nachfolger in der Ausführung besitzt


Tasks werden absteigend nach level sortiert und so priorisiert.
Tasks im kritischen Pfad erhalten automatisch ein hohes Level und werden bevorzugt bearbeitet.


> [!Example] Klausuraufgabe
> Prioritätenliste aus Ausführungsgraph erstellen und schedulen (Seite 265)
> Kommunikationskosten fallen nur zwischen Knoten an. (siehe lösung auf 266)

![](HlfetListScheduling.png)


> [!Tip] Kommunikationskosten
> Wenn zwei Tasks auf der selben Node ausgeführt werden, so fallen keine Kommunikationskosten an.
> Aus diesem Grund wurde Task `D` bewusst auf Node 3 gelegt und nicht auf Node 2 ausgeführt.


### Dynamisches Scheduling
Bei dynamischem Load Balancing kann der Ausführungsort zur Erstellung des Prozess festgelegt werden. In einer anderen Variante kann er zur Laufzeit wieder verändert werden ("Prozessmigration")

- Information Policy (Wann wird Balanciert)
- Transfer Policy (Schwellenwert-Entscheidung)
- Location Policy (Wie wird das Ziel gefunden? Polling / Broadcast / Zufällig)
- Selection Policy (Welche Tasks werden verschoben?)

#### Typische Ansätze
- Sender Initiated
	- Überlastete Knoten suchen aktiv nach Unterstützung
- Receiver Initiated
	- Unterausgelastete Knoten fragen andere gezielt nach Aufgaben
- Kombiniert

#### Code Migration
Weak und Strong Mobility

##### Weak
Nur Code-Segmente, wie Java-Klassen und javascript

##### Strong
Code und gesamter Ausführungszustand. (Stack, Heap, Code)
Hier wird der gesamte [Prozess](Paraprog-Basics.md#Prozess) migriert.

Sicherheit, Heterogenität und externe Ressourcen sind dabei Herausforderungen.


Nach der Migration eines Prozess kann auf dem Ursprungsrechner ein "Shadow-Prozess" verbleiben. Er dient dazu, Systemaufrufe des migrierten Prozesses zu verwalten, die sich noch auf lokale Ressourcen (Dateien / Sockets) beziehen. Aufrufe und Daten werden ggf. an den neuen Standort des Prozess weitergeleitet.
Der Shadow Prozess wird eventuell gelöscht, wenn keine Weiterleitung mehr erforderlich ist.

Adressräume können auf mehrere Arten migriert werden
- Eager
  Alles wird auf einmal migriert
- Precopy
  Prozess läuft weiter, während Seiten übertragen werden. Modifizierte Seiten werden nachgesendet
- Eager (Dirty) 
  Nur geänderte Seiten werden übertragen. Rest nur bei Zugriff (Copy-on-Reference)
- Flushing
  Alle Seiten auf Disk speichern, dann Copy-on-reference beim Ziel
