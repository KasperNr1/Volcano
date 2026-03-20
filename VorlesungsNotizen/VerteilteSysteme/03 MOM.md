# Motivation Messaging
Bei RPC müssen Client und Server gleichzeitig online sein.
Mit Messaging wird dies entkoppelt, es wird eine asynchrone Kommunikation möglich.

Sender legt Nachrichten in Message Queue ab. Empfänger kann sie von dort verarbeiten, wenn er dazu bereit ist.
![](MessageQueue.png)

# Arten von Nachrichten

|           | Persistent                                                                  | Transient                                                       |
| --------- | --------------------------------------------------------------------------- | --------------------------------------------------------------- |
| Asynchron | Speichern von Nachrichten bis zur Zustellung (Email)                        | Fire-and-forget (UDP)                                           |
| Synchron  | Sender blockiert bis Übermittlung bestätigt ist<br>(Message Queue mit Ack.) | Nachrichten werden nur während der Ausführung gehalten<br>(RPC) |

# ZeroMQ
Eine plattformübergreifende Messaging-Bibliothek, die Sockets um höhere Abstraktion erweitert. Stellt gängige Kommunikationsmuster bereit (Pub/Sub, Req/Rep, Push/Pull)

Brokerless Design, geringe Anforderungen an Infrastruktur.

Ein Socket kann an mehrere Adressen gebunden werden. Ermöglicht Many-to-One Kommunikation.

Sender kann direkt fortfahren, ZeroMQ kümmert sich im Hintergrund um Zustellung / Retry von Nachrichten.

# Persistente Nachrichten
Message Queuing:
Zwischenspeicher für Nachrichten auf Client / Serverseite oder Zwischenstelle.

Geeignet für Längere Zeiträume, wenn Nachrichten innerhalb von Minuten übertragen werden müssen.

Zuverlässige Zustellung, auch bei temporären Verbindungsabbrüchen.

Sender und Empfänger müssen nicht gleichzeitig online sein.

![](PersistantCommunication.png)

## Message Broker
Ermöglicht tatsächliche Persistenz da kein Zeitpunkt nötig ist zu dem Client und Server gleichzeitig online sind.

Ermöglich auch fortgeschrittene Funktionalität wie das Umwandeln von Formaten.


# MQTT
Leichtgewichtiges Publish/Subscribe Protokoll mit Broker-Architektur.
Optimiert für ressourcenarme Clients.


# Anwendungsorientierte Middleware
## Laufzeitumgebungen
Setzt auf Betriebssystem der Knoten auf.

Runtime erweitert OS um Rssourcenmanagement (Nebenläufigkeitsunterstützung, Verbindungsmanagement, Verfügbarkeit)

- Pooling von Verbindungen / Threads

So werden Allokationskosten veringert, was eine geringere Latenz und bessere Skalierbarkeit bietet.

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
Cients fragen Dienste über Namen an, somit sind Adresswechsel möglich.

Entkoppelt Client von Server.

## Session Management
Jede Client Instanz erhält eine Session (User ID, Warenkorb)

Session Daten können transient oder persistent sein.
Speichern Serverseitig oder Client-Seitig (Cookies)

Middleware sorgt für trnasparente Zuordnung von Requests zu Sessions

## Transaktionsverwaltung
Bildet eine Folge von Aktionen als atomare Operation ab.
1. Daten Holen
2. Modifizieren
3. Zurückschreiben


> [!WARNING] Problem
> Gleichzeitige Ausführung durch mehrere Clients erfordert Koordination


## Persistenzservice
Intelligente Schnittstelle zur Datenbank.

Häufigst als "Object-Relational-Mapper" (ORM)

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
Anfrage mit Identifikator wird per Broadcast an alle Knoten gesendet.
Entsprechender Knoten antwortet direkt mit seiner Adresse.
Z.B. DNS

Bei Adresswechseln kann eine Entität eine Kette an Weiterleitungszeigern hinterlassen.
Somit ist keine Globale Suche nötig, Ketten können aber sehr lang werden und eventuell Inkonsitent sein.

### Hierarchische Namen
Unterteilung in Domänen und Unterdomänen. Es entsteht eine Baumstruktur die sich effizient durchsuchen lässt.

![](StructuredNames.png)




  





