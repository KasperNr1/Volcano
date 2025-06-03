# Signal
Ein Signal ist eine physikalisch messbare, zeitabhängige Größe.
Abhängig vom verwendeten Medium gibt es verschiedene Ausprägungen der relevanten Größen.
![Signalklassifizierung](Signalklassifizierung.png)
## Medium
![](ÜbersichtMedien.png)
## Amplitude
Maximale Auslenkung von der "Mitte" aus, stark abhängig vom [physischen Medium](#Medium)

## Frequenz
Wiederholungen des Signals pro Sekunde

## Phase
Genaue "Position" des Signals innerhalb einer Periode

## Bandbreite
Frequenzbereich in dem ein Signal effektiv übertragen werden kann.
Gibt die Differenz zwischen der höchsten und der niedrigsten [Frequenz](#Frequenz) in diesem Bereich an.

## Baudrate
Geschwindigkeit mit der Symbole übertragen werden.
Wird verwendet um beim Dekodieren die Richtige Menge Bits zu Messen und zu verarbeiten

## Bitrate
Menge an übertragener Bits pro Sekunde, meist gleich wie [Baudrate](#Baudrate)
Szenarien sind möglich bei denen die Bitrate höher ist.
![](BitVsBaud.png)

## Modulation
Die Information eines Signal kann durch Veränderung unterschiedlicher Eigenschaften symbolisiert werden.

Amplitude Key Shifting (AKS)
![](AKS.png)

Frequency Key Shifting (FKS)
![](FKS.png)

Phase Key Shifting (PKS)
![](PKS.png)

Diese werden beispielsweise bei Wi-Fi 6 kombiniert eingesetzt um mit einer Welle mehr Informationen übertragen zu können.
![](QuadratureAmplitudeModulation.png)
# Kollision
Je nach Wahl des physischen [Übertragungsmediums](#Medium) kann durch gleichzeitiges Senden verschiedener [Signale](#Signal) eine Störung der Kommunikation entstehen. Beispielsweise Interferenz der elektrischen Wellen.
Sie sind nur bei [Halbduplex](#Halbduplex) möglich.
Bei [Simplex](#Simplex) gibt es nur einen Sender, bei [Vollduplex](#Vollduplex) existieren separate Kanäle für beide Kommunikationsrichtungen.
Es gibt verschiedene Protokolle zur Behandlung von Kollisionen.

## Kollisionsdomäne
Beschreibt den Teil eines [Netzwerks](#Netzwerk) in dem mehrere Geräte ein gemeinsames Medium verwenden.
Durch den Einsatz von [Hubs](ISO-OSI%20Referenzmodell.md#Hubs) werden sie vergrößert.
Jedes physische Netz ist eine Kollisionsdomäne. [Bridges](ISO-OSI%20Referenzmodell.md#Bridge) oder Switches unterteilen die Kollisionsdomäne. Idealerweise ist jedes Gerät an einen eigenen Port eines Switches angebunden. In diesem Fall spricht man von einem vollständig geswitchten Netzwerk.

![](Kollisionsdomäne.png)

# Netzwerk
Ein Netzwerk ist eine Gruppe von (Computer-)Systemen die über Kommunikationsleitungen verbunden sind und gemeinsame Ressourcen und Informationen nutzen.
Es umfasst sowohl die physische Einrichtung als auch die entsprechenden Vermittlungs- und Übertragungsverfahren.
# Netzwerktypen
- PAN
  Personal (Bluetooth)
- LAN
  Local (Heimnetz)
- MAN
  Metropolitan
- WAN
  Wide Area (Mobilfunk)
- GAN
  Global (Internet)

## VLAN
Virtuelles LAN ist eine Trennung eines physischen Netzes durch VLAN fähige [Switches](ISO-OSI%20Referenzmodell.md#Switches) anhand von Ports oder anderen Merkmalen.
Datenpakete werden nur in dem VLAN versandt aus dem sie geschickt wurden.
# Netzwerktopologien
Beschreiben verschiedene Varianten Rechner in einem System mit einander zu verbinden. Bei der Entscheidung sind verschiedene Eigenschaften der unterschiedlichen Optionen zu beachten. Beispielsweise die Erweiterbarkeit des Systems oder das Verhalten bei Ausfällen eines Einzelnen relevant.
Übertragungsgeschwindigkeit und tatsächliche physische Anschlussmöglichkeiten spielen ebenfalls eine Rolle.
![](Netztopologien.png)
## Vermascht
Verbindungen werden zwischen Computern gezogen deren Kommunikation besonders hohe Übertragungsraten benötigt.
Wenn jedes Paar an Rechnern eine Verbindung besitzt, so spricht man von einem voll-vermaschten System.
### Vorteile
- Optimale Datenübertragung
- Ausfall eines Computers hat kaum Einfluss auf das restliche Netzwerk
### Nachteile
- Komplex und Teuer
  (Besonders bei weiten Wegen)
- Schlechte Skalierbarkeit
  (Extremer bei Vollvermaschung)

## Bus
Alle Rechner sind an eine Zentrale Datenleitung angebunden. So werden alle Daten von immer von jedem Empfangen und individuell verwendet oder aussortiert.
### Vorteile
- Erweiterung sehr Einfach
### Nachteile
- Kabelprobleme können einen Totalausfall verursachen
- Anteil nicht-relevanter Nachrichten pro Gerät steigt stetig mit Größe des Systems
- Abschlusswiderstände sind notwendig um Probleme der physischen Leitung zu kontern
## Linie / Ring
Jedes Gerät (mit Ausnahme der Linienenden) ist mit exakt zwei Geräten verbunden.
Die Verbindung zwischen erstem und letztem Gerät ist der entscheidende Unterschied zwischen Ring und Linie.
Im Gegensatz zum [Bus](#Bus) gibt es hier kein zentrales Medium
### Vorteile
- Ressourcensparend
- Leicht zu erweitern
### Nachteile
- Ausfall einer Verbindung kann das Netzwerk lahm legen
- Bei großen Systemen weite Wege für Daten
## Stern
Alle Teilnehmer sind mit einem zentralen Hub oder Switch verbunden.
### Vorteile
- Einfach aufzubauen
- Leicht zu erweitern
- Ausfall eines Computers hat keine Wirkung auf restliches Netzwerk
### Nachteile
- Hub kann zum Bottleneck werden
- Totalausfall bei Störung der zentralen Komponente
## Ring mit RLV
RLV ist eine Abkürzung für "Ringverteilungsleiter"
Der Aufbau vereint die physischen Eigenschaften des [Stern](#Stern) und die logischen Eigenschaften eines [Ring](#Linie%20/%20Ring).
![](RLV.png)
### Vorteile
- Hohe Ausfallsicherheit
- Jede Station ist ein Repeater
- Leicht zu erweitern
- Ressourcensparend
### Nachteile
- Störung der zentralen Einheit kann Totalversagen verursachen
- Hub kann zum Bottleneck werden
## Baum
Computer sind in einer hierarchischen Struktur miteinander verbunden.
Ähnlich zur [Stern-Stern](#Stern-Stern) Topologie, hier jedoch strengere Reihenfolge.
### Vorteile
- Ausfall eines Endgeräts hat keinerlei Konsequenz
### Nachteile
- Ausfall eines Verteilers legt Sub-Baum lahm
## Stern-Stern
Router werden [Stern-artig](#Stern) angeordnet, Endgeräte ebenfalls Sternmäßig mit den einzelnen Routern verbunden. Wird in der Praxis häufig für lokale Netzwerke verwendet.
![](StarStar.png)
# Übertragungsarten
## Simplex
Verbindung von $A$ nach $B$ mit Kommunikation in einer festen Richtung

## Halbduplex
Übertragung zwischen $A$ und $B$ abwechselnd in beide Richtungen (Walkie-Talkie)

## Vollduplex
Gleichzeitige Übertragung in beide Richtungen

## Multiplex
Multiplexverfahren sind eine Möglichkeit mehrere Signale zu bündeln um die Effizienz der Kommunikation zu steigern.
Dabei werden verschiedene Arten unterschieden.
### Raummultiplex
Jedes Signal erhält eine eigene Leitung. So kann ohne Interferenz oder Wartezeit gleichzeitig von mehreren Kanälen gesendet werden. Dieser Ansatz ist jedoch besonders bei sehr großen Netzwerken schwer zu skalieren.
## Zeitmultiplex
Jeder Benutzer erhält einen Zeitraum in dem er berechtigt ist Daten zu versenden. Die Kommunikation erfolgt so strikt abwechselnd. Eventuell entstehen kleine Verzögerungen.
Diese Variante ist ähnlich der [Multiplexer](De-Multiplexer.md) Schaltungen, die einen ausgewählten Kanal zur Kommunikation freigeben.
## Frequenzmultiplex
Verschiedene Sender kommunizieren auf individuellen Wellenlängen. Das entstehende Mischsignal kann durch [Fourier Transformation](https://en.wikipedia.org/wiki/Fourier_transform) wieder zerlegt werden.
## Codemultiplex
Verwendung unterschiedlicher Codierungen

# Adressierungsarten
## Unicast
Kommunikation mit einem eindeutig identifizierten Empfänger
## Broadcast
Teilnehmer einer Gruppe werden angesprochen (Radio)
## Multicast
Eine Ausgewählte Untergruppe Empfänger wird angesprochen (IPTV)
## Anycast
Ein beliebiger (nächstgelegener) Empfänger aus einer Gruppe (Drucker)

# Adressen
## MAC
Media Access Control Adressen sind 48 Bit lang und unabhängig von den logischen Adressen der [Vermittlungsschicht](ISO-OSI%20Referenzmodell.md#3%20Vermittlungsschicht). 
Sie bestehen aus 4 Abschnitten mit verschiedenen Bedeutungen.

| I/G   | U/L   | OUI    | OUA    |
| ----- | ----- | ------ | ------ |
| 1 Bit | 1 Bit | 22 Bit | 24 Bit |
- I/G
  Bit das beschreibt ob es sich um eine Individuelle (0) oder Gruppen-Adresse (1) handelt.
- U/L
  Universal (0) oder Lokale (1) Adresse
- OUI
  (Oraganizationally Unique Identifier) Herstellerkennung
- OUA
  (Organizationally Unique Address) Vom Hersteller frei Wählbar

Die höchsten 24 Bits der Adresse, also I/G, U/L und OUI werden von der IEEE vergeben.

### Spezielle Broadcast Adresse
Für Nachrichten an alle Geräte des selben physischen Netzes wird die Broadcast Adresse als Zieladresse angegeben.
`FF:FF:FF:FF:FF:FF` 
Alle der Bits der 6 Byte-Adresse sind also mit $1$ belegt. 

### MAC-Spoofing
Moderne Geräte können ihre MAC-Adresse dynamisch ändern. Sie sollte daher nicht für Authentifizierung oder sonstige Vergabe von Berechtigungen verwendet werden.

### Adress Resolution Protocoll (ARP)
Dieses Protokoll bestimmt die MAC Adresse eines Gerätes für die [Sicherungsschicht](ISO-OSI%20Referenzmodell.md#2%20Sicherungsschicht) aus der IP-Adresse der [Vermittlungsschicht](ISO-OSI%20Referenzmodell.md#3%20Vermittlungsschicht)
Dazu wird die IP Adresse des gesuchten Geräts per [Broadcast](Basics.md#Broadcast) an die [Spezielle Broadcast Adresse](#Spezielle%20Broadcast%20Adresse) gesendet. Das Gerät mit der entsprechenden Adresse antwortet dem Sender, dieser speichert die empfangene MAC Adresse.
![](AdressResolutionProtocoll.png)
Das [Betriebssystem](02%20Grundlagen.md#Definition%20Betriebssystem) führt eine Tabelle mit den ARP Einträgen. Die Tabelle enthält IP-Adressen, MAC-Adressen, Netzwerk-Interfaces.
Es existiert ein Protokoll für die Rückrichtung, das bestimmen der Netzwerkadresse aus einer MAC Adresse (RARP).
## IPv4

## IPv6
# Kommunikationsmodelle
## Client-Server
Der Server ist eine Anwendung die Daten bereit stellt.
Andere Computer, die diese Daten oder Dienste beanspruchen sind die Clients.

### Vorteile
- Einfach zu implementieren
- Gute Skalierbarkeit bei geringer Anzahl Clients
- Hohe Sicherheit durch zentrale Kontrolle
### Nachteile
- Server kann zum Bottleneck werden
- Skalierung bei vielen Clients kann komplex werden (vertikal: mehr Leistung; horizontal: Parallelisierung, weitere Server)
- Ausfall des Servers führt zu Totalausfall
## Peer to Peer (P2P)
Jeder Teilnehmer einer P2P Architektur ist gleichberechtigt und kann Dienste zur Verfügung stellen oder sie in Anspruch nehmen.
Beispielsweise können im Heimnetz große Downloads zwischen Geräten geteilt werden, statt sie aus dem Internet zu beziehen.

### Vorteile
- Hohe Skalierbarkeit
- Hohe Ausfallsicherheit
- Ressourceneffizient
  Jeder Peer kann beisteuern -> wenig Bedarf für dedizierte Infrastruktur
- Sicherheit
  Keine Zentrale Schwachstelle die von außen angegriffen werden kann
### Nachteile
- Koordinationsaufwand
- Ungleiche Ressourcen
  Koordination zur proportionalen Aufgabenverteilung nötig
- Sicherheit durch zentrale Kontrolle ist nicht gegeben
- Eingeschränkte Zuverlässigkeit
## Publish - Subscribe
Mindestens drei Teilnehmer sind notwendig - ein Sender (Publisher), ein Subscriber und ein Broker.
Alle Kommunikation findet mit dem Broker statt. Dieser koordiniert die Nachrichten und relevanten Informationen zwischen den einzelnen Geräten.
### Vorteile
- Entkopplung Publish / Subscriber
- Skalierbarkeit durch Verteilung auf mehrere Broker
- Selektivität
  Bandbreite wird sparsam verwendet, da nur angeforderte Daten tatsächlich gesendet werden.
### Nachteile
- Komplexität
- Ereignisreihenfolge
  Verlorene Nachrichten können Probleme auslösen
- Hohe Latenz

# Standards und Normen
Sind benötigt für:
- Kompatibilität
- Einheitlichkeit
- Qualität
- Sicherheit
- Kostensenkung
- Globalisierung

![](standards.png)
## Standard
- Etablierte Richtlinien
- Einheitlichkeit und Kompatibilität
## Normen
- Formal Dokumentiert
- Von Normungsorganisationen
- Rechtliche Relevanz
## Arten der Standardisierung
### Faktische Standardisierung (De-Facto Standard)
- Setzen sich ohne offizielle Anerkennung durch
- Entsteht am Markt
- Nicht unbedingt das tatsächlich beste
### Institutionell
- Standards durch (internationale) Organisationen
- z.B. ISO
### Legislative
- Gesetzliche Vorgaben
- z.B. RoHS (Restriction of the use of certain hazardous substances)

# Kabel
Unterschiedliche Arten von Kabel haben verschiedene Eigenschaften die in speziellen Anwendungsfällen besonders vor- oder nachteilhaft sind.
Die wichtigsten sind hierbei häufig:
- Kosten
- Bandbreite
- Installation und Wartungsaufwand
- Signalstärke

Bei der Verkabelung eines komplexen Systems (beispielsweise mehreren Gebäuden) sollte eine Kombination aus Kabelarten verwendet werden, um die jeweiligen Stärken optimal zu kombinieren und trotzdem wirtschaftlich zu arbeiten.
![](Strukturierte_Verkabelung.png)

## Koax
Besteht aus vier entscheidenden Komponenten
- Innenleiter aus Kupfer
- Isolierschicht
- Folie / Metall zur Abschirmung
- Äußerer Mantel

Die Kabel sind eher schwer und unflexibel, wird hauptsächlich für Kabel Internet verwendet
Übertragen von Daten geht hier mit bis zu 10Gbit/s

![](Koax.png)
## Twisted Pair
4 Kupfer-Aderpaare sind verdrillt, die namensgebende Eigenschaft.
Die Abstrahlung und Aufnahme von Interferenz wird dadurch verringert, was die Qualität des Signals verbessert.

Diese Art Kabel existiert in verschiedenen [Kategorien](https://de.wikipedia.org/wiki/Twisted-Pair-Kabel#Kategorien) die unterschiedlich hohe Geschwindigkeiten ermöglichen. Dabei wird mit variierenden Reichweiten zwischen 1Mb/s und 40Gb/s erreicht.

![](TwistedPair.png)

## Glasfaser
### Singlemode
Nur wenige Wellenlängen werden geleitet, das Signal wird so auch über lange Strecken mit extrem hoher Präzision und Qualität übertragen.
Die Kabel sind teurer und werden primär für Langstreckenverbindungen und Hochgeschwindigkeitsleitungen verwendet.
![](SingleMode.png)
### Multimode
Breiterer optisch leitender Kern überträgt viele Wellenlängen gleichzeitig.

![](MultiMode.png)

Diese Art Kabel wird zur Verbindung von Gebäuden oder Rechenzentren verwendet.

#### Dispersion
Durch die unterschiedlichen Wellenlängen werden die Lichtstrahlen in unterschiedlichen Winkeln reflektiert. Das anfangs punktuelle Signal kann so nach längerer Strecke ausgedehnt werden und sich besonders bei kurzen Pulsen mit dem nachfolgenden Puls überlagern.

![](Dispersion.png)

