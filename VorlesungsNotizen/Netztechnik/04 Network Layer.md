# Aufgaben
Routing
Weiterleiten
## Sender
Segmente in Pakete unterteilen
## Empfänger
Pakete Erkennen

## Protokolle
IPV4
IPV6
ICMP

# Geräte
Router:
Leitet Pakete zwischen Adressbereichen weiter

Layer 3 Switch:
Router ohne WAN Schnittstelle

Gateway
Sind Protokollumsetzer.
Ermöglich Kommunikation zwischen Systemen mit unterschiedlichen Protokollen.
Fast unnötig da fast alle mit IP arbeiten

Router und L3 Switche unterteilen Kollisionsdomäne ebenfalls

# Adressierung
Globales Addressieren über physische MAC Adressen nicht sinnvoll
IP Adressen sind logisch und Hardware-unabhängig

# Internet Protocoll
Internet ist eine Sammlung Teilnetze
IP ist verbindungslos und unzuverlässig (Keine Empfangsgarantie, so gut wie möglich)
Zuverlässige Verbindungen werden von Schicht 4 gewährleistet

## Aufbau eines Pakets
- Version des Protokolls
- Header Length
- Service Feld (Priorisierung)
- Paketlänge
- Kennung (eindeutiger Identifier)
- Flags (Fragmentierung erlaubt ja/nein)
- TimeToLive
	- Zahl maximaler Hops
	- Jeder Router verringert um 1
	- Verhindert unsterbliche Pakete
- Protokoll-ID
	- Nummer des übergeordneten Pakets in Transportschicht
- Prüfsumme
- IP Adresse (Sender)
- Füllbits

Adresse ist 32 Bit Lang (4.294 Mia. Kombinationen)

Besteht aus Netz- und Hostadresse

Class A,B,C Netze tauschen Platz für Host und Netzadressen

## Subnetting
Wird genutzt um phyische Netze in logische Teilnetze zu unterteilen

Günde:
- Trennen von Netzen nach
	- Gebäude
	- Abteilung
	- Topologie
- Trennen sensibler Bereiche
Kommunikation zwischen Subnets nur über Router

### Subnetzmaske
Alle Knoten im Netz bekommen Netzmaske (32 Bit)
Hostadresse der IP-Adresse wird und Subnetznummer und Hostadresse geteilt

## Spezielle Adressen
Netz Adresse -> (Host = 0)
Broadcast Adresse -> (Netz = 1)

### Private Adressen
Auch im LAN werden Adressen vergeben, darf nicht mit "echten" kollidieren

0.0.0.0/8 Wird als wildcard verwendet 

127.0.0.1 Lokalhost

Adressen in diesem Bereich werden grundsätzlich nicht geroutet, dürfen nicht in öffentliche geroutet werden.

## Adressvergabe
- Manuell (Schlecht)
- DHCP (Spätere Vorlesung)
- BootP (Veraltet)


> [!Example] Klausuraufgaben
> Subnetze berechnen, aus IP-Adressbereichen Menge an Subnetze und Geräten bestimmen


# NAT
Jeder Haushalt kann mit einer IP Adresse pro router auskommen und über private Netze alle Geräte mit dem Internet verbinden.
Router tauscht Private Adresse des Geräts gegen öffentliche IP und einen Port.

# IPv6
128 Bit
Geschrieben in 16 Bit Hex Blöcke die durch : getrennt werden
Bsp.: 2001:0db8:85a3:08d3:1319:8a2e:0370:7344

- Führende Nullen in Blöcken werden weggelassen
- Höchstens eine Gruppe aus reiner 0 Blöcke darf durch einen : ersetzt werden

## Aufbau
- Präfix (Kennzeichnet Netz)
- Interface ID (kennzeichnet Gerät)
- Subnetting durch Reduktion des Präfix
- 