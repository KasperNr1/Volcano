# Betriebstypen
## Network Operating System
Klassische Betriebssysteme, erweitert um Netzwerkunterstützung. Die Exsitenz der anderen Rechner ist sichtbar, sie kommunizieren über verschiedene Protokolle.

## Distributed Operating System
Einheitliches Betriebssystem für ein ganzes Netzwerk von Rechnern. Soll Transparenz erreichen, erfordert aber enge Kooperation der OS-Kerne und ist daher eher weniger weit verbreitet.

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




# Rollen von Prozessen
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

# Programmiermodelle
Definieren Kommunikationsmodell (Synchron / Asynchron) und Programmierparadigma

Gängig sind:
- RPC
- RMI
- Message Oriented

## Remote Procedure Call (RPC)
Wirkt wie lokaler Funktionsaufruf.

> [!Missing] Fehlt
> Seite 121 bis 126
> 

Problematisch sind die Übertragung von Daten. Bei großen Objekten ist die Duplikation auf beiden Systemen notwendig, oder eine tiefe Kopie bei jedem Aufruf. Simple "Call by Reference" kann nicht funktionieren da der Speicher nicht zwischen den Systemen geteilt wird.

- Verbot von Zeigern
- Copy by Value
- Copy by Value / Restore
- Objekt-Referenzen

RPC kann eng in Programmiersprachen integriert werden. So ist weniger Boilerplate notwendig und die Referenzprobleme werden ausgelagert.

