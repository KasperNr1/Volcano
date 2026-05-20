# Programmiermodelle
Definieren Kommunikationsmodell (Synchron / Asynchron) und Programmierparadigma

Gängig sind:
- [Remote Procedure Call (RPC)](#Remote%20Procedure%20Call%20(RPC))
  Remote Procedure Calls erlauben es, entfernte Prozeduren wie lokale aufzurufen. Sie arbeiten prozedural und synchron, sind einfach zu verwenden, bringen aber eine engere Kopplung
- RMI
  Remote Method Invocation kann entfernte Methoden auf Objekten aufrufen. Lässt sich gut auf OOP abbilden.
- [Message Oriented Model (MOM)](#Message%20Oriented%20Model%20(MOM))
  Kommuniziert asynchron und mit loser Kopplung. Ist gut geeignet für Event-driven-Architecture und [Publish - Subscribe](Basics.md#Publish%20-%20Subscribe) Muster

## Remote Procedure Call (RPC)
Wirkt wie lokaler Funktionsaufruf.
![](RpcAblaufTimeline.png)
Der Aufrufende Client bleibt stehen, bis das Ergebnis der Berechnung übertragen wird.
Entsprechend führt die Anwendung zu höherer Latenz und Fehleranfälligkeit durch Netzwerkausfälle.

1. Die Client-Prozedur ruft lokal den Client-Stub auf.
2. Der Client-Stub erstellt die Nachricht und übergibt sie an das lokale OS.
3. Das Client-OS sendet die Nachricht an das entfernte OS.
4. Das entfernte OS übergibt die Nachricht an den Server-Stub.
5. Der Server-Stub extrahiert die Parameter und ruft die Server-Prozedur.
6. Der Server führt die Arbeit aus und liefert das Ergebnis an den Stub.
7. Der Server-Stub verpackt das Ergebnis in eine Nachricht und übergibt sie dem Server-OS.
8. Das Server-OS sendet die Nachricht an das Client-OS.
9. Das Client-OS übergibt die Nachricht an den Client-Stub.
10. Der Client-Stub übergibt das Ergebnis an die aufrufende Client-Prozedur.

Aufgrund der eventuellen Unterschiede beider Plattformen in Codierung und Byte-Reihenfolge (Endianness) müssen die Parameter vor der Übertragung in ein einheitliches Format übertragen werden.
Diese Umwandlung wird typischerweise in den Stubs vorgenommen, verschiedene Stub-/Skeleton-Generatoren erzeugen dafür den Quellcode für beide Enden.

Problematisch sind die Übertragung von Daten. Bei großen Objekten ist die Duplikation auf beiden Systemen notwendig, oder eine tiefe Kopie bei jedem Aufruf. Simple "Call by Reference" kann nicht funktionieren da der Speicher nicht zwischen den Systemen geteilt wird.

- Verbot von Zeigern
- Copy by Value
- Copy by Value / Restore
- Objekt-Referenzen

RPC kann eng in Programmiersprachen integriert werden. So ist weniger Boilerplate notwendig und die Referenzprobleme werden ausgelagert.

### gRPC
Ist ein Tool zum Einsatz von RPC über verschiedene Betriebssysteme und Programmiersprachen hinweg.
Es wird besonders in Microservices oder mobilen Backends und [IoT-Anwendungen](08%20IoT.md) eingesetzt

In einer eigenen Definitionssprache werden die Schnittstellen definiert. Der tatsächliche Programmcode für beide Seiten wird daraus automatisch generiert und löst die Kompatibilitätsprobleme bereits.
```
[
	uuid(ba209999-0c6c-11d2-97cf-00c04f8eea45),
	version(1.0)
]
interface MyInterface
{
	const unsigned short INT_ARRAY_LEN = 100;
	
	void MyRemoteProc(
		[in] int param1,
		[out] int outArray[INT_ARRAY_LEN]
	);
}
```

> [!MISSING] Fehlt
> RMI
> Keine Folien, nur Übung anhand von [dieser Website](https://openbook.rheinwerk-verlag.de/java8/14_001.html#u14)

# Message Oriented Model (MOM)
## Motivation: Messaging
Bei RPC müssen Client und Server gleichzeitig online sein.
Mit Messaging wird dies entkoppelt, es wird eine asynchrone Kommunikation möglich.

Sender legt Nachrichten in Message Queue ab. Empfänger kann sie von dort verarbeiten, wenn er dazu bereit ist.
![](MessageQueue.png)

## Arten von Nachrichten

|           | Persistent                                                                  | Transient                                                       |
| --------- | --------------------------------------------------------------------------- | --------------------------------------------------------------- |
| Asynchron | Speichern von Nachrichten bis zur Zustellung (Email)                        | Fire-and-forget (UDP)                                           |
| Synchron  | Sender blockiert bis Übermittlung bestätigt ist<br>(Message Queue mit Ack.) | Nachrichten werden nur während der Ausführung gehalten<br>(RPC) |

## ZeroMQ
Eine plattformübergreifende Messaging-Bibliothek, die Sockets um höhere Abstraktion erweitert. Stellt gängige Kommunikationsmuster bereit (Pub/Sub, Req/Rep, Push/Pull)

Brokerless Design, geringe Anforderungen an Infrastruktur.

Ein Socket kann an mehrere Adressen gebunden werden. Ermöglicht Many-to-One Kommunikation.

Sender kann direkt fortfahren, ZeroMQ kümmert sich im Hintergrund um Zustellung / Retry von Nachrichten.

## Persistente Nachrichten
Message Queuing:
Zwischenspeicher für Nachrichten auf Client / Serverseite oder Zwischenstelle.

Geeignet für Längere Zeiträume, wenn Nachrichten innerhalb von Minuten übertragen werden müssen.

Zuverlässige Zustellung, auch bei temporären Verbindungsabbrüchen.

Sender und Empfänger müssen nicht gleichzeitig online sein.

![](PersistantCommunication.png)


> [!Info] Garantie
> Es ist sichergestellt, dass die Nachricht zugestellt wird.
> Es gibt keine Garantie, dass die Nachrichten tatsächlich gelesen werden.


## Message Broker
Ermöglicht tatsächliche Persistenz da kein Zeitpunkt nötig ist zu dem Client und Server gleichzeitig online sind.

Ermöglich auch fortgeschrittene Funktionalität wie das Umwandeln von Formaten.


# MQTT
Leichtgewichtiges Publish/Subscribe Protokoll mit Broker-Architektur.
Optimiert für ressourcenarme Clients.

Siehe auch [MQTT](08%20IoT.md#MQTT).
