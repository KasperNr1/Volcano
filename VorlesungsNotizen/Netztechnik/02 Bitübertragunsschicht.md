# Aufgaben
Bitübertragung, Steuerung der Kommunikation
- Synchronisierung Sender und Empfänger
- Steuerung der Datenrate
- Festlegung der Übertragungsmodi

Repeater / Hubs

# Repeater
Leitet Signale weiter, reinigen von Jitter oder Rauschen
Untersuchen die Bedeutung der Signale nicht

# Hubs
- Sind [Repeater](#Repeater) mit mehr als 2 Schnittstellen, leiten Signale an alle angeschlossenen Geräte weiter
- Nur Halb-Duplex
- Nur bis 100MBit aufgrund von Halb-Duplex und Kollisionen

# Kollisionen
- Nur bei [Halbduplex](01.md#Halbduplex) möglich
- Zu viele Kollisionen können Netzwerkausfälle verursachen
- Protokolle zur Behandlung von Kollisionen

## Kollisionsdomäne
- Ist Teil eines Netzwerks in dem mehrere Geräte ein gemeinsames Medium nutzen
- [Hubs](#Hubs) vergrößern sie

# Signale
Messbare Zeitabhängige physikalische Größen

## Klassifizierung
![](Signalklassifizierung.png)

## Amplitude
- Maximale Auslenkung von der "Mitte" aus, stark abhängig vom physischen Medium

## Frequenz
Wiederholungen des Signals pro Sekunde

## Phase
Genaue "Position" des Signals innerhalb einer Periode

## Bandbreite
Frequenzbereich in dem ein Signal effektiv übertragen werden kann

## Baudrate
Geschwindigkeit mit der Symbole übertragen werden.
Wird verwendet um beim Dekodieren die Richtige Menge Bits zu Messen und zu verarbeiten

## Bitrate
Menge an übertragener Bits pro Sekunde, meist gleich wie [Baudrate](#Baudrate)
Szenarien sind möglich bei denen die Bitrate höher ist.

![](BitVsBaud.png)

# Leitungscodes
## NRZ
Direkte Umwandlung Bits zu Signalpegel

## NRZI
Senden von 1 -> Signal wechseln
Senden von 0 -> Beibehalten

## MLT-3
3 Pegel:
- "+"
- "-"
- 0

## RZ
Ebenfalls 3 Pegel
Nach jedem Bit wird das Signal auf 0 zurückgesetzt.
Information ist in der Flanke enthalten

## Unipolar RZ
2 Pegel
Nach jeder 1 zurück zu 0
Übertragen von 0 durch Beibehalten

## AMI
3 Pegel
0 durch Mittleren Pegel codiert,
1 immer abwechselnd über + und -

## B8ZS
Modifiziert [AMI](#AMI) um lange Ketten von 0er besser zu übertragen
Nicht mögliche Codewörter werden an Stelle von 8er Ketten aus 0 verwendet

## Manchester
2 Pegel
- 1 als Steigende Flanke
- 0 als fallende Flanke

## Manchester 2
Wie [Manchester](#Manchester) mit vertauschten Flanken

## 4B5B
4 Nutzerdaten auf 5 Bit Übertragung, 16 Kombinationen werden für Steuerung frei

## 5B6B

## 8B6T
