# Internet of Things
Network of uniquely adressable objects based on standard communication protocolls

Internetfähige Geräte mit Sensoren.

## Einsatz
- Home-automation
- Verkehrssteuerung
- Intelligente Straßenbeleuchtung
- Produktion
- Predictive Maintainence

## Cyber-physische Systeme
Rasberry Pi:
- Sensoren
- Aktoren
- Kommunikatoren
- Prozessoren

## Herausforderungen
- Speicher
- Rechenleistung
- Sicherheit
- Partielle Konnektivität
- Qualität
- Datenschutz
- Skalierung

![[IoTArchitektur.png]]

# Protokolle
## MQTT
[Publish - Subscribe](Basics.md#Publish%20-%20Subscribe) Modell für Geräte mit geringer Übertragungsrate.
Nachrichten bestehen aus Topic und Payload mit nicht-spezifiziertem Inhalt. Der Empfänger muss das Format bereits kennen.
`/` wird als Trenner zwischen Topics verwendet
![](MQTT.png)

### Quality of Service
Kommunikation kann über verschiedene "Quality of Services" stattfinden
1. At most once (QoS 0)
   Ein mal senden
2. At least once (QoS 1)
   Mindestens ein Mal senden bis Bestätigung erhalten wird
3. Exactly once (QoS 2)
   4-Wege Handshake um einmalige Übertragung sicherzustellen

### Last Will
Nachrichten können mit flag "retain" versandt werden, bei Verbindungsabbruch kann auf diese Werte zurückgegriffen werden.

## CoAP
Constrained Application Protocol [Client-Server](Basics.md#Client-Server) Modell und sehr effizient. Ähnlich aufgebaut wie HTTP und REST

## OPC UA
Open Platform Communications Unified Architecture ist ein industrieller Standard zum Austausch von Daten.
- Plattformunabhängig
- Sicherheit
- Skalierbar von Embedded bis Server 

Datenmodelle sind pro Industriezweig standardisiert
- OPC 30050: PackML - Packaging
- OPC 40550-1: Woodworking Machinery - Vertical Interface

Verschlüsselung über Public/Private Key Verfahren
Signierung
Authentifizierung
- Zertifikat
- User + Password
- Token

