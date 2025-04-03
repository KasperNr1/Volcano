Open-Systems-Interconnection Modell und Notation ist eine Standardisierungsinitiative der [ISO](Basics.md#Institutionell).
# Ziel
- Festlegungen zur Kommunikation von Hard- und Software unterschiedlicher Hersteller
- Vereinfachte Standardisierung durch klare Trennung in der Funktion jeder Schicht
- Grundlage zur Bildung neuer Standards

![](Schichtenbildung.png)
# Abstraktes Schichtenmodell

![](Abstraktes%20Schichtenmodell.png)

## Dienste
Funktionalität einer Schicht ist die Menge ihrer Dienste.
Der Datenaustausch erfolgt dabei an den SAPs (Service-Access-Points) über definierte Protokolle.
Diese Dienste werden anhand ihrer Kommunikation unterschieden zwischen "Unbestätigt" und "Bestätigt"

# Schichtmodell

![](Schichtmodell.png)
## 1 Physical Layer
Verwaltet die bloße Übertragung der Daten. Es findet keine  [Fehlererkennung oder Korrektur](Codes.md#Fehlerumgang) statt.

### Aufgaben
- Bitübertragung
- Synchronisierung Sender und Empfänger
- Festlegung der Übertragunsmodi
- Steuerung der Datenrate
- Umwandlung von Daten und [Signalen](Basics.md#Signal)
- Physische Übertragung von Signalen
Physische Übertragung zwischen Systemen
Enthält Umwandlung von Daten zu Signalen
Ungesicherte Verbindung, keine Fehlerkorrektur
### Geräte
#### Repeater
Leiten Signale weiter und reinigen diese von Jitter oder Rauschen. Die Reinigung von Signalen ist nicht das selbe wie eine [Fehlerkorrektur](Codes.md#Fehlerkorrektur). Die Bedeutung des [Signals](Basics.md#Signal) wird nicht untersucht.
#### Hubs
Sind [Repeater](#Repeater) mit mehr als zwei Schnittstellen. Jedes Signal das am Hub ankommt wird an alle anderen angeschlossenen Geräte weitergeleitet.
Hubs kommunizieren nur über [Halbduplex](Basics.md#Halbduplex).
Die Übertragungsrate ist darum auf etwa 100MBit begrenzt. Außerdem können Kollisionen auftreten.

### Leigungscodes
TODO
[02 Bitübertragunsschicht](02%20Bitübertragunsschicht.md)

## 2 Sicherungsschicht
Gliederung des Bitstroms in Rahmen (Frames)
Zugriffskontrolle
Adressierung (Eindeutige Hardwarekennung - MAC Adresse)
Flusssteuerung zur Vermeidung von Überlastung
Puffern auf Sender und Empfängerseite
Erkennung und Behebung von Fehlern in Bitübertragung

## 3 Vermittlungsschicht
Wegewahl für Ende-zu-Ende Kommunikation
Hierarchische Adressierung
Multiplexen

## 4 Transportschicht
Übertragen von Daten zwischen Anwendungen
Aufwendige Fehlererkennung und Behebung
Fluss- und Staukontrolle
Pufferung bei Sender und Empfänger
Adressierung zur Unterscheidung der Anwendung durch Ports

## 5 Sitzungsschicht
Sorgt für gesicherte Prozesskommunikation
Einführung von Wiederaufsetzpunkte für Sitzungs-Synchronisation nach Ausfall einer Transportverbindung
In der Praxis eher in der Anwendung umgesetzt

## 6 Darstellungsschicht
Legt fest, wie Informationen in einer Sprache auszutauschen sind.
Aushandlung einer Transfersyntax
Umwandlung Little / Big Endian
Verschlüsselung
Kompression

## 7 Anwendungsschicht
Enthält Protokolle für Anwendungsfunktionalität, beispielsweise FileTransfer, HTTP, Email

Die eigentliche Anwendung (Source Code) zählt nicht zu dieser Schicht, nutzt aber das Anwendungsprotokoll

## Anwendung
![](AnwendungAllgemein.png)![](AnwendungBrief.png)

# Mapping auf TCP/IP
TCP/IP ist eine weiteres Referenzmodell.
[OSI-Schichten](#Schichtmodell) werden Teilweise zusammengefasst.

Schichten 1 bis 3 werden als physisches Medium zusammengefasst
Ebenfalls kommen Schicht 5-7 in der Applikation zusammen.
![](OSI-TCP.png)
![](Zsmfsg%20Schichtmodell.png)
# Schicht 0
Die physischen Verbindungen, also [Kabel](Basics.md#Kabel), Verteilerkasten und das tatsächlich verbaute Material sind nicht offiziell im [Schichtmodell](#Schichtmodell) enthalten.

