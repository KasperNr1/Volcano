# Vorlesung 1 - Einführung
## Kommunikationsmodelle
Die [Kommunikationsmodelle](Basics.md#Kommunikationsmodelle) (Publish/Subscribe, Client/Server) und ihre Eigenschaften kennen

## Adressierungsarten
Die [Adressierungsarten](Basics.md#Adressierungsarten) (Unicast, Anycast, Multicast, Broadcast) und ihre Eigenschaften kennen

## Übertragungsarten
Die [Übertragungsarten](Basics.md#Übertragungsarten) (Simplex, Halbduplex, Vollduplex, Multiplex) und ihre Eigenschaften kennen

## OSI Modell
- Das ISO/OSI [ISO-OSI Referenzmodell](ISO-OSI%20Referenzmodell.md) und dessen Schichten beschreiben können
- Das TCP/IP Referenzmodell und dessen Schichten beschreiben können
- Wissen wie das OSI Referenzmodell auf das TCP/IP Referenzmodell [abgebildet](ISO-OSI%20Referenzmodell.md#Mapping%20auf%20TCP/IP) wird

## Kabel
- Die [Netzwerkkabeltypen](Basics.md#Kabel) LWL, TwistedPair und Koax auflisten können
- Eine beispielhafte strukturierte Verkabelung aufzeichnen können


# Vorlesung 2 - Layer 1
## Leitungscodes
- Verstehen warum [Leitungscodes](ISO-OSI%20Referenzmodell.md#Leitungscodes) gebraucht werden
- Die Eigenschaften und erwünschten Merkmale von Leitungscodes kennen
- Die Leitungscodes [NRZ](ISO-OSI%20Referenzmodell.md#NRZ) und Blockcodierungen mit vorgegebenen Tabellen anwenden können
- Die Vorteile von [Blockcodierungen](ISO-OSI%20Referenzmodell.md#^5feed6) beschreiben können

# Vorlesung 3 - Layer 2
- Den Anwendungszweck und die Funktionsweise von [VLANs](Basics.md#VLAN) kennen
- Die Begriffe und Vorgehensweisen der Adressierung der Sicherungsschicht kennen und beschreiben können (MAC-Adressen, ARP, Broadcast-Adressen, MAC-Spoofing)

## Prüfsummen
- Eine zweidimensionale Parität berechnen können
- CRC Prüfsummen berechnen und validieren können

# Vorlesung 4 - Layer 3
- Beschreiben können warum Adressierung auf der Vermittlungsschicht benötigt wird
- IPv4 Adressen und ihren Aufbau kennen
- Wissen was die Begriffe Netzklassen, Subnetting, Subnetzmaske, CIDR, Standard-Gateway bedeuten und ihren Zweck kennen
- IPv4 spezielle Adressen kennen (Netz- und Broadcastadresse)
- NAT und dessen Anwendungszweck erläutern können
- IPv4 Netz- und Broadcastadresse bestimmen können
- IPv4 Subnet-IDs bestimmen können
- IPv4 Subnetting anhand Netzanforderungen durchführen können
- Wissen warum IPv6 entwickelt wurde und was der IPv4 Run-Out ist
- IPv6 Adressen und ihren Aufbau kennen
- IPv6 Notationsregeln auflisten und anwenden können
- Wissen warum es in IPv6 keine Broadcasts gibt und mit was sie ersetzt werden (die Multicast-Adressen und Typen müssen Sie nicht kennen)
- Die Arten der Adresskonfiguration bei IPv4 und IPv6 nennen können
- Beschreiben für welchen Anwendungsfall das SLAAC verwendet wird
- Vorteile von IPv6 nennen können

# Vorlesung 5 - Layer 4
- Die Begriffe Routing und Forwarding erklären können
- Die Inhalte und den Zweck einer Routing-Tabelle kennen
- Den Ablauf des Forwardings innerhalb eines Routers beschreiben können
- Die gewünschten Eigenschaften von Transportprotokollen nennen können
- Wissen wie die Adressierung in der Transportschicht funktioniert (Portnummern)
- Wissen was ein Socket ist und aus welchen Bestandteilen er besteht
- Die Eigenschaften und die Anwendungsbereiche von UDP kennen
- Die Eigenschaften und die Anwendungsbereiche von TCP kennen
- Die Unterschiede von TCP und UDP kennen

# Vorlesung 6 - Layer 5-7
- Wissen für welchen Zweck die Anwendungsprotokolle DHCP, DNS, SMTP, POP3, IMAP, NFS, SMB, FTP, Telnet, SSH, NTP, SNMP jeweils eingesetzt werden können
- Erläutern können warum es bei FTP mehrere Modis gibt
- Die Unterschiede zwischen IMAP und POP3 erläutern können