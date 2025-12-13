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






---

# Einführung
- Was ist Security?
- Wer sind die Angreifer?
- Warum greift man an?


# Recht
Strafrechtlich Relevante Aktionen
- Unbefugter Zugriff
- Umgehen von Hürden
- Löschen oder Sabotieren von Einträgen

