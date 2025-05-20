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
- Festlegung der Übertragungsmodi
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

### Leitungscodes
Ein Leitungscode hat folgende Eigenschaften
- Anzahl an Signalstufen (2 - Binär; 3 - ternär; ...)
- Anzahl codierter Bits pro Symbol
- Schrittgeschwindigkeit ([Bitrate](Basics.md#Bitrate) oder [Baudrate](Basics.md#Baudrate))

Erwünscht sind außerdem:
- Hohe Effizienz
  Möglichst gleiches Verhältnis zwischen Bitrate und Baudrate
- [Fehlererkennung](Codes.md#Fehlererkennung)
  Aus wenigen übertragenen Daten feststellen ob Fehler vorliegen
- Mögliche Taktrückgewinnung
  Sender und Empfänger sollen durch die Codierung synchron gehalten werden, falls der Takt auseinander läuft.
  Ein einheitlicher Takt ist notwendig um dem Sender die Fähigkeit zu geben die korrekten Zeitpunkte zu bestimmen, in denen er das [Signal](Basics.md#Signal) abtasten muss.
- Gleichstromfreiheit
  Längere Folgen von übertragenen Nullen oder Einsen sollen vermieden werden, da einige physische Komponenten nicht gut mit Gleichstrom umgehen können.
#### NRZ
Bits der Nachricht werden direkt in Signalpegel umgewandelt
![](NRZ.png)

| Durchschnittsverschiebung | Taktrückgewinnung | Effizienz |
| ------------------------- | ----------------- | --------- |
| Ja                        | Nein              | 100%      |

#### NRZI
Um eine 1 zu Senden wird das Signal invertiert, für eine 0 wird der aktuelle Pegel beibehalten
![](NRZI.png)

| Durchschnittsverschiebung | Taktrückgewinnung | Effizienz |
| ------------------------- | ----------------- | --------- |
| Ja                        | Nein              | 100%      |

#### MLT-3
Drei verschiedene Pegel
- "+"
- "-"
- 0
Nuller werden durch Beibehalten codiert, eine 1 löst einen Wechsel aus. Dabei wird in einer festen Reihenfolge gewechselt um den Durchschnitt neutral zu halten 

![](MLT-3.png)

| Durchschnittsverschiebung | Taktrückgewinnung | Effizienz |
| ------------------------- | ----------------- | --------- |
| Ja                        | Nein              | 100%      |

#### RZ (Return to Zero)
Verwendet ebenfalls 3 Signalpegel.
Um eine 1 zu senden wird für einen halben Takt das positive Signal übertragen, für eine Null das negative.
Nach jedem ganzen Takt wird wieder der mittlere Pegel erreicht.
![](RZ.png)
Dem Empfänger ist es jederzeit möglich den Takt zu erkennen. Allerdings können lange Folgen von 0 oder 1 beide den Durchschnitt verschieben. Außerdem werden nur 50% der Zeit tatsächlich Informationen übertragen.

| Durchschnittsverschiebung | Taktrückgewinnung | Effizienz |
| ------------------------- | ----------------- | --------- |
| Ja                        | Ja                | 50%       |

##### Unipolar RZ
Ist ein Sonderfall bei dem nur 2 Signalpegel verwendet werden.
Um eine 0 zu senden wird einen ganzen Takt lang Pegel 1 verwendet, um eine 1 zu senden wird einen halben Takt auf Pegel 2 geschalten.
![](Uni-RZ.png)

| Durchschnittsverschiebung | Taktrückgewinnung | Effizienz |
| ------------------------- | ----------------- | --------- |
| Ja                        | Nein              | ? %       |

#### AMI
(Alternate Mark Inversion)
Verwendet 3 Pegel, der mittlere wird verwendet um eine 0 zu übertragen. Für 1er wird abwechselnd der positive und negative Pegel übertragen.

![](AMI.png)

Durchschnittsverschiebungen sind ausgeschlossen, eine Taktrückgewinnung ist nicht möglich. 
Da einige Kombinationen nicht erscheinen können, ist eine teilweise [Fehlererkennung](Codes.md#Fehlererkennung) möglich.
Die folgenden Signale werden niemals gesendet werden:
- "++"
- "--"
- "+0+"
- "-0-"

| Durchschnittsverschiebung | Taktrückgewinnung | Effizienz |
| ------------------------- | ----------------- | --------- |
| Nein                      | Nein              | 100%      |

##### B8ZS
Wegen Problemen bei längeren Reihen von Nullen wird eine spezielle Variante verwendet. 
- "+00.000.000" wird codiert als "+000+-0-+"
- "-00.000.000" wird codiert als "-000-+0+-"
So ist das eindeutige Muster immer noch erkennbar, ohne die Nachteile der längeren Gleichstromphase mit sich zu führen. Ebenfalls sind gleich viele "+" und "-" Pegel vorhanden um den Durchschnitt des Signals weiterhin neutral zu halten.

| Durchschnittsverschiebung | Taktrückgewinnung | Effizienz |
| ------------------------- | ----------------- | --------- |
| Nein                      | Ja                | 100%      |

#### Manchester
Verwendet 2 Pegel, die Information wird durch die gesendete Flanke codiert. Eine Fallende Flanke symbolisiert eine 0, Einser werden als steigende Flanke codiert.

![](Manchester.png)

Es gibt eine Variante mit inversen Belegungen, die restlichen Eigenschaften verändern sich hierdurch nicht.

| Durchschnittsverschiebung | Taktrückgewinnung | Effizienz |
| ------------------------- | ----------------- | --------- |
| Nein                      | Ja                | 50%       |

##### Differentiale Manchester
Für Einser wechselt der Pegel ein Mal in der Mitte der Bitzelle, für Nullen einmal zusätzlich auch zu Beginn.

![](ManchesterDiff.png)

---

Alle bisherigen Codierungen haben signifikante Nachteile.
Außerdem können Sonderfälle wie Start/Stop/Idle nicht direkt kommuniziert werden.
Eine Möglichkeit ist, sie über sonst nicht verwendete Code-Kombinationen zu übermitteln. Start einer Nachricht könnte eine definierte Sequenz (Präambel) sein.
Besser ist die Verwendung von dedizierten Steuerzeichen. Informationsbits werden zu Blöcken zusammengefasst und mit Steuerbits verlängert. Es werden immer Blöcke mit einer festen Größe übertragen. ^5feed6

#### 4B5B
Vier Nutzdaten werden mit einem Steuerbit auf Fünfer-Blöcke erweitert. Von den 32 möglichen Kombinationen werden 16 für Daten verwendet, die restlichen dienen der Steuerung.

Es gibt eine einheitliche [Tabelle](https://de.wikipedia.org/wiki/4B5B-Code) zu den Bedeutungen der Datenwörter.

| Durchschnittsverschiebung | Taktrückgewinnung | Effizienz |
| ------------------------- | ----------------- | --------- |
| Ja                        | Ja                | 80%       |

#### 5B6B
5 Nutzdaten werden auf 6 Bits abgebildet.
Ziel ist die Durchschnittsverschiebung aufzuheben. Es werden von 32 Möglichen 5 Bit Wörtern die mit ähnlicher Zahl Nullen und Einser mit einem 6. Bit ausgeglichen. Die restlichen Codewörter werden in 2 jeweils Inversen Kombinationen abgebildet. Diese positiven oder negativen Varianten werden immer abwechselnd gesendet.

Auch hierzu gibt es eine Tabelle

| Durchschnittsverschiebung | Taktrückgewinnung | Effizienz |
| ------------------------- | ----------------- | --------- |
| Nein                      | Ja                | 83.3%     |

#### 8B10B
8 Nutzdaten werden auf 10 Bits Nachricht kodiert. Dabei enthält jede Kombination immer genau 5 und 5 Nullen und Einser, oder genau 4 und 6. So ist die Durchschnittliche Spannung neutral ohne zu viele Nachteile mitzuführen.

| Durchschnittsverschiebung | Taktrückgewinnung | Effizienz |
| ------------------------- | ----------------- | --------- |
| Nein                      | Ja                | 80%       |

#### 8B6T
8 Binary, 6 Ternary.
Hilfreich bei Verwendung von mehr als 2 Signalpegeln. Die Binärdaten werden durch die erhöhte Zahl an Zuständen in kleineren Codewörtern übertragen. Die Kodierung selbst erfolgt ebenfalls anhand einer Tabelle.


| Durchschnittsverschiebung | Taktrückgewinnung | Effizienz |
| ------------------------- | ----------------- | --------- |
| Nein                      | Ja                | 80%       |


## 2 Sicherungsschicht
### Aufgaben
Gliederung des Bitstroms in Rahmen (Frames)
Zugriffskontrolle
Adressierung (Eindeutige Hardwarekennung - MAC Adresse)
Flusssteuerung zur Vermeidung von Überlastung
Puffern auf Sender und Empfängerseite
Erkennung und Behebung von Fehlern in Bitübertragung

### Geräte
#### Bridge
Leiten Frames zwischen physischen Netzen weiter. Wenn mehr als 2 Schnittstellen vorhanden sind spricht man von "Layer-2-Switch" oder "Multiport-Bridge"

![](Multiport-Bridge.png)

Die gesendeten Frames werden anhand ihrer Prüfsummen verifiziert und sonst nicht weiter gelesen / verstanden.

#### WLAN-Bridge
WLAN zu LAN Adapter
![](WlanBridge.png)

#### Transparente Bridges
![](TransparentSwitch.png)
Es ist nicht sinnvoll alle Frames die an der Bridge ankommen weiterzuleiten. Beispielsweise Nachrichten von A nach B sind auf der selben Seite.

##### Kreise
Wenn Teile des Netzes einen [Ring](Basics.md#Linie%20/%20Ring) darstellen können Frames eventuell endlos im Kreis geleitet werden. Dies passiert, wenn die Bridges nicht wissen welche Geräte an welchem Port liegen und im Ethernet keine Time To Live oder Bestätigung vorsieht.
Das Spanning Tree Protokoll löst die Problematik. Das Netzwerk wird hierbei zu einem [Spannbaum](Bäume.md#Spannbäume) geformt um die Kreise zu eliminieren.

## 3 Vermittlungsschicht
Wegewahl für Ende-zu-Ende Kommunikation
Hierarchische Adressierung
Multiplexen

### Geräte
#### Switches

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

