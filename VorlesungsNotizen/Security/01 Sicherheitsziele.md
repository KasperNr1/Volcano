# Sicherheitsattribute
Sind Sicherheitsziele die ein Datenbesitzer für seine Daten hat.
Die CIA-Triade ist eine häufige Menge an Sicherheitsattributen. Sie umfasst:
- Vertraulichkeit
- Integrität
- Verfügbarkeit

## Vertraulichkeit
Überbegriff für zwei Konzepte die Daten von Zugriff durch unbefugte Personen oder Prozesse schützen
### Datenvertraulichkeit
Gewährleistet, dass Daten nicht an unbefugte Personen weitergegeben werden.

### Privatsphäre 
Beschreibt, dass ein Einzelner kontrollieren kann welche ihn betreffenden Informationen gesammelt werden und wer diese einsehen / weitergeben kann.

## Integrität
### Datenintegrität
Informationen und Programme können nur auf festgelegte Arten verändert werden.
##  Systemressourcen
- Hardware
- Software
- Kommunikationseinrichtungen
- Daten

### Systemintegrität
Ein System kann seine beabsichtigte Funktion erfüllen, unabhängig von Fehlern in Hardware / Datenübertragung oder (böswilliger) Manipulation

## Verfügbarkeit
Stellt sicher dass Systeme zeitnah funktionieren und zur Verfügung stehen.
Hochverfügbarkeitssysteme müssen immer in der Lage sein zu funktionieren.

## Ergänzende Ziele
- Authentizität (Eigentümerschaft über Daten beweisen)
- Besitz / Kontrolle (Zugang zu Daten selbst kontrollieren)
- Nutzen (Daten verwenden können {Nicht verschlüsselt sein})
- Nachweisbarkeit (Nichtabstreitbarkeit von vergangenen Handlungen)

|               | Verfügbarkeit                                                      | Vertraulichkeit                                            | Integrität                                                                                             |
| ------------- | ------------------------------------------------------------------ | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Hardware**  | Geräte werden gestohlen, deaktiviert oder zerstört                 | Ein unverschlüsseltes Laufwerk wird gestohlen / ausgelesen | - / -                                                                                                  |
| **Software**  | Programme werden gelöscht oder Berechtigungen von Nutzern entfernt | Eine unerlaubte Kopie wird erstellt                        | Ein bestehendes Programm wird verändert um es zu Abstürzen zu bringen oder falsche Ausgaben zu liefern |
| **Daten**     | Dateien werden gelöscht oder Personen der Zugriff verweigert       | Unerlaubtes Auslesen / Kopie erstellen                     | Bestehende Daten werden geändert oder neue erstellt.                                                   |
| **Netzwerke** | Nachrichten werden zerstört oder gelöscht                          | Nachrichten werden gelesen und ausspioniert                | Nachrichten werden geändert oder neue unechte Nachrichten werden übertragen                            |



# Systemressourcen
- Hardware
- Software
- Kommunikationseinrichtungen
- Daten

# Begriffe
## Cybercrime
Es wird unterschieden zwischen dem **engeren** und dem **weiteren** Sinn

| Engerer Sinn                                                                     | Weiterer Sinn                                            |
| -------------------------------------------------------------------------------- | -------------------------------------------------------- |
| Delikte bei denen Informations- / Kommunikationsgeräte als Ziel  betroffen waren | Alle Delikte die unter Einsatz des Internets stattfinden |

## Angriff
Jede Art von Böswilliger Aktivität, die versucht Systeme oder deren Informationen zu stehlen / stören oder beeinträchtigeno

## Gegenmaßnahme
Eine Technik oder ein Gerät dass die Wirksamkeit gegnerischer Handlungen einschränken soll

## Risiko
Maß für die Bedrohung durch ein Ereignis. Wird meißt dargestellt als das Produkt aus Schaden und Eintrittswahrscheinlichkeit
$$
\text{Risiko} = \text{Potentieller Schaden} \cdot \text{Eintrittswahrscheinlichkeit}
$$

## Sicherheitsregelung
Beschränkungen um die [Sicherheitsattribute](#Sicherheitsattribute) zu gewährleisten

## Bedrohung
Jeder Umstand oder jedes Ereignis das in der Lage ist negativen Einfluss auf das Vermögen, den Betrieb oder Ruf einer Firma oder Person zu nehmen.


## Angriff
Wird unterschieden in 
**Passiver Angriff**:
Ein Versuch Informationen zu erhalten und zu nutzen der keine Auswirkungen auf die reguläre Funktion des Systems hat.

**Aktiver Angriff**:
Ein Versuch Systemressourcen zu verändern oder ihren Betrieb zu beeinflussen.

Es wird auch nach dem Ursprung eines Angriffs unterschieden.
**Innerer Angriff**:
Initiiert von einem *Insider* (Jemand der berechtigt ist auf Daten zuzugreifen und diese ohne Genehmigung verwendet)

**Äußerer Angriff**:
Der Angriff wird von einer externen Quelle verursacht die keine eigenen bestehenden Berechtigungen ausnutzt.

## Computer vs IT-Sicherheit
Computersicherheit beschreibt die Sicherheit einzelner Rechner vor Abstürzen oder unerlaubtem Zugriff.
IT-Sicherheit ist eine [Obermenge](Intervalle%20und%20Mengen.md#Mengen) und umfasst auch die Sicherheit von allen anderen Systemen und digitalen Objekten die miteinander kommunizieren und arbeiten.
Gänzlich umfassend ist die **Informationssicherheit**. Sie ist nicht auf Digitales begrenzt und umfasst die Sicherheit in allen Bereichen die [Bedrohungen](#Bedrohung) ausgesetzt sind.

# Computerstrafrecht
![Cybercrime](#Cybercrime)

## Anwendbarkeit
- In Deutschland
- Auf Deutschen Schiffen / Flugzeugen
- Bei Straftaten durch oder Gegen Deutsche Bürger

![](RightsApplicability.png)

## StGB 202 Verletzung des Briefgeheimnisses
(1) Wer unbefugt 
1. einen verschlossenen Brief oder ein anderes verschlossenes Schriftstück, die nicht zu seiner Kenntnis bestimmt sind, öffnet oder

2. sich vom Inhalt eines solchen Schriftstücks ohne Öffnung des Verschlusses unter Anwendung technischer Mittel Kenntnis verschafft,

wird mit Freiheitsstrafe bis zu einem Jahr oder mit Geldstrafe bestraft, wenn die Tat nicht in § 206 mit Strafe bedroht ist.

(2) Ebenso wird bestraft, wer sich unbefugt vom Inhalt eines Schriftstücks, das nicht zu seiner Kenntnis bestimmt und durch ein verschlossenes Behältnis gegen Kenntnisnahme besonders gesichert ist, Kenntnis verschafft, nachdem er dazu das Behältnis geöffnet hat.

(3) Einem Schriftstück im Sinne der Absätze 1 und 2 steht eine Abbildung gleich.

### 202a Ausspähen von Daten
(1) Wer unbefugt sich oder einem anderen Zugang zu Daten, die nicht für ihn bestimmt und die gegen unberechtigten Zugang besonders gesichert sind, unter Überwindung der Zugangssicherung verschafft, wird mit Freiheitsstrafe bis zu drei Jahren oder mit Geldstrafe bestraft.

(2) Daten im Sinne des Absatzes 1 sind nur solche, die elektronisch, magnetisch oder sonst nicht unmittelbar wahrnehmbar gespeichert sind oder übermittelt werden.

### 202b Abfangen von Daten
Wer unbefugt sich oder einem anderen unter Anwendung von technischen Mitteln nicht für ihn bestimmte Daten (§ 202a Abs. 2) aus einer nichtöffentlichen Datenübermittlung oder aus der elektromagnetischen Abstrahlung einer Datenverarbeitungsanlage verschafft, wird mit Freiheitsstrafe bis zu zwei Jahren oder mit Geldstrafe bestraft, wenn die Tat nicht in anderen Vorschriften mit schwererer Strafe bedroht ist.

### 202c Vorbereiten des Ausspähens und Abfangens von Daten
(1) Wer eine Straftat nach § 202a oder § 202b vorbereitet, indem er 

1. Passwörter oder sonstige Sicherungscodes, die den Zugang zu Daten (§ 202a Abs. 2) ermöglichen, oder

2. Computerprogramme, deren Zweck die Begehung einer solchen Tat ist,

herstellt, sich oder einem anderen verschafft, verkauft, einem anderen überlässt, verbreitet oder sonst zugänglich macht, wird mit Freiheitsstrafe bis zu zwei Jahren oder mit Geldstrafe bestraft.

### 202d Datenhehlerei
(1) Wer Daten (§ 202a Absatz 2), die nicht allgemein zugänglich sind und die ein anderer durch eine rechtswidrige Tat erlangt hat, sich oder einem anderen verschafft, einem anderen überlässt, verbreitet oder sonst zugänglich macht, um sich oder einen Dritten zu bereichern oder einen anderen zu schädigen, wird mit Freiheitsstrafe bis zu drei Jahren oder mit Geldstrafe bestraft.

(2) Die Strafe darf nicht schwerer sein als die für die Vortat angedrohte Strafe.

(3) Absatz 1 gilt nicht für Handlungen, die ausschließlich der Erfüllung rechtmäßiger dienstlicher oder beruflicher Pflichten dienen. Dazu gehören insbesondere 

1. solche Handlungen von Amtsträgern oder deren Beauftragten, mit denen Daten ausschließlich der Verwertung in einem Besteuerungsverfahren, einem Strafverfahren oder einem Ordnungswidrigkeitenverfahren zugeführt werden sollen, sowie

2. solche beruflichen Handlungen der in § 53 Absatz 1 Satz 1 Nummer 5 der Strafprozessordnung genannten Personen, mit denen Daten entgegengenommen, ausgewertet oder veröffentlicht werden.

## Weitere Paragraphen
- 263a Computerbetrug
- 265a Erschleichen von Leistung
- 267 Urkundenfälschung
- 268 Fälschung technischer Aufzeichnungen
- 269 Fälschung beweiserheblicher Daten
- 270 Täuschung im Rechtsverkehr
- 303a Datenveränderung (Verfolgung nur auf Antrag)
- 303b Computersabotage (Verfolgung nur auf Antrag)
- 317 Störung von Telekomunikationsanlagen
