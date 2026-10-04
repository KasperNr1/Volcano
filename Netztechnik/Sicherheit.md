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

# Physische Bedrohungen
- Naturkatastrophen
	- Erdbeben
	- Überschwemmungen
	- Tornardos
	- Blitzeinschläge

# Serverräume
## Lüftungssysteme
Rechensysteme sollten in Umgebungen aufgestellt sein in denen Temperaturen von ca. $10^\circ$ bis $32^\circ C$ gegeben sind.

Ebenfalls sollte die Luftfeuchtigkeit gering gehalten werden um Korrosion und Eintritt von Kondenswasser zu vermeiden.

Diese Faktoren können durch eigene Kühl- und Lüftunssysteme reguliert werden. Dabei empfiehlt sich eine räumliche Trennung für frische und verbrauchte Luft, um die Metriken exakter Messen und effektiver kühlen zu können.

Offene Kühlung im Raum:
![](OpenCooling.png)

Räumlich getrennte Luftschächte:
![](IsolatedCooling.png)

## Brandschutz
Durch automatische Melder wird ein Signal ausgelöst. Dabei reagieren die Melder eventuell auf Temperatur, Rauch oder Vibration. 
Fortschrittliche Anlagen verwenden Löschgassysteme, sodass der Sauerstoff vertrieben wird und die Rechner nur minimale Hitzeschäden erleiden, anstelle der schlimmeren Wasserschäden. Ebenfalls ist bei einem solchen System auch nach einer Auslösung nur wenig Aufräumarbeit notwendig.


> [!Info] Vibration
> Starke Vibrationen sind in der Lage die Lese- Schreibköpfe von Festplatten zu stören oder zu beschädigen. Daher werden solche Systeme bei starken Vibrationen ausgeschalten oder pausiert.

## Sperrbereiche
Sicherheitsbereiche dürfen nur von wenigen bestimmten Personen betreten werden. In der Praxis werden oft vier Sicherheitsstufen eingesetzt um Zugänge zu verwalten.


| Sicherheitsstufe | Beschreibung                                                                                                                                                                                             | Beispiel                                                                                                                   |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Uneingeschränkt  | Ein Bereich für den kein Sicherheitsinteresse besteht                                                                                                                                                    | Firmengelände, Parkplatz und Zufahrt.                                                                                      |
| Kontrolliert     | Ein Bereich in der Nähe des Sperrbereichs. Der Zugang ist auf Personal begrenzt, dass diesen braucht, wird jedoch nicht besonders streng kontrolliert. Das bloße Betreten stellt kein großes Risiko dar. | Firmengebäude, Zutritt nur mit Mitarbeiterausweis.<br>(Eventuell wird die Tür geöffnet ohne zu kontrollieren wer eintritt) |
| Begrenzt         | Gesperrter Bereich in unmittelbarer Nähe eines Sicherheitsbereichs. Der unkontrollierte Aufenthalt könnte den Zugang zum Sperrbereich ermöglichen.                                                       | Gerätehalle / Flur vor einem Serverraum, Vereinzelungszutritt mit (2-Faktor-) Authentifizierung.                           |
| Ausschluss       | Gesperrter Bereich für den ein Sicherheitsinteresse besteht. Aufenthalt in dieser Zone ermöglicht direkten Zugang zu diesem gesperrten Bereich.                                                          | Serverräume oder Käfige. Ständige Videoüberwachung, Zutritt nur in Begleitung                                              |

![](SecurityLayers.png)


# Ausfälle

> [!Quote] Was ist ein Ausfall?
> Eine Ausfall ist, wenn eine Komponente und auch ein System keine Daten über Schnittstellen ein- oder ausgegeben kann und sich nicht steuern lässt.
> 
> Dies gilt auch für Fehlfunktionen und fehlerhafte ausgegebene Daten

## Einzelne Komponente
Die Verfügbarkeit einer einzelnen Komponente berechnet sich als das Verhältnis aus der Funktionsfähigen Zeit und der Gesamtzeit.
$$
\text{Verfügbarkeit} = \frac{\text{Betriebszeit}}{\text{Betriebszeit} + \text{Ausfallzeit}}
$$

Wenn die Gesamtverfügbarkeit einer Gruppe von Ojekten berechnet werden soll, bestimmt sich diese ähnlich über die Anzahl der vorhandenen und verfügbaren Objekte.
$$
\text{Verfügbarkeit} = \frac{\text{Anzahl Objekte} - \text{Anzahl nicht verfügbarer Objekte}}{\text{Anzahl Objekte}}
$$


> [!Info] Allgemein
> Beide Formeln verallgemeinern sich zu folgendem Verhältnis
> $$
> \text{Verfügbarkeit} = \frac{\text{Verfügbarer Teil}}{\text{Gesamtheit}}
> $$


## Verkettete Systeme
Die Verfügbarkeit verketteter Systeme verhält sich allgemein wie der Elektrische Widerstand elektrischer Schaltungen.

### Serienschaltung
In Serie geschaltene Systeme sind nur dann Verfügbar, wenn es alle Komponenten auch sind.

![](Serienschaltung.png)
$$
V_{\text{Serie}} = \prod_{i=1}^{n} V_i = V_{K_1} \cdot V_{K_2} \cdot \ldots \cdot V_{K_n} 
$$

## Parallelschaltung
Bei einer Parallelschaltung ist die [Wahrscheinlichkeit](Einführung.md) eines beliebigen Ausfalls durch die Anzahl der Komponenten erhöht. Ein Ausfall des Gesamtsystems erfordert jedoch einen gleichzeitigen Ausfall aller Komponenten. Dies ist sehr unwahrscheinlich, wodurch das System insgesamt robust wird.

![](Parallelschaltung.png)

$$
V_{\text{Parallel}} = 1 - \prod_{i=1}^{n} (1-V_i)= 1 - (1-V_{K_1}) \cdot (1-V_{K_2}) \cdot \ldots \cdot (1-V_{K_n})
$$


> [!Info] Ausfallsicherheit vs. Verfügbarkeit
> Die Summe dieser beiden Größen ist stets $1$, da ein System sich nur in den Zuständen "Verfügbar" oder "Ausgefallen" befinden kann
> $$
> \text{Verfügbarkeit}(V) + \text{Ausfallzeit}(V) = 1
> $$


# RAID
Ein Redundant Array of Inexpensive Disks kombiniert mehrere günstige Festplatten zu einem größeren Speichersystem.

Abhängig von der Anzahl der verwendeten Platten gibt verschiedene Arten von Sicherungssystemen. Einige sind simpel und spiegeln die Daten einfach mehrmals während andere komplexere Verfahren mit Prüfsummen die Menge des effektiv verfügbaren Speichers erhöhen.
Diese Verschiedenen Varianten wurden ursprünglich von 0 bis 5 nummeriert, wurden allerdings seither erweitert.

## RAID-1
Bei dieser Variante werden alle Festplatten mit identischem Inhalt beschrieben (Mirroring). So ist die Datenmenge bis zu einem Ausfall von $(n-1)$ problemlos lesbar.

![](Raid1.png)

Das Schreiben wird mit jeder Platte langsamer, das Lesen schneller.

## RAID-0
Hier wird keine Redundanz gespeichert. Daten werden in Blöcke zerlegt und nach dem [Round-Robin-Prinzip](03%20Prozessmanagement.md#Round-Robin) auf die Festplatten verteilt (Striping).
Jede einzelne Platte enthält so nur Teile einer Datei.
Durch diese Variante sind Lese- und Schreibgeschwindigkeit sehr hoch, jedoch ist keine Sicherheit gegeben.

![](Raid0.png)

## RAID-4
Bei Raid-4 werden Daten auf die ersten $(n-1)$ Laufwerke aufgeteilt wie bei [RAID-0](#RAID-0). Das $n$-te Laufwerk dient als Paritätslaufwerk und enthält Prüfsummen für die entsprechenden Bits der anderen Laufwerke. So werden die Schnelligkeit von Raid-0 mit Ausfallsicherheit kombiniert.

![](Raid4.png)


## RAID-5
Hier wird wie bei [RAID-4](#RAID-4) die Parität zu den durch Striping getrennten Speichermedien berechnet. Allerdings ist es nicht notwendig eine eigene Festplatte für diese Kontrollbits zu führen, da die entsprechenden Datenblöcke gleichmäßig auf alle Laufwerke verteilt werden.

![](Raid5.png)

## RAID-6
Hier werden jeweils 2 Blöcke an Paritätsbits über die Laufwerke verteilt. Somit können zwei beliebige Festplatten ausfallen ohne dass Daten verloren gehen. Der Geschwindigkeitsvorteil von [RAID-0](#RAID-0) bleibt großteils erhalten.

![](Raid6.png)

## RAID-10
Ist eine Kombination aus [RAID-0](#RAID-0) und [RAID-1](#RAID-1). 
Mit mindestens 4 Platten werden Daten auf 2 Gestriped und diese beiden Platten auf die anderen gespiegelt.

![](Raid10.png)


# Datensicherung
Es gibt verschiedene Varianten Backups zu erstellen. Die häufigsten sind dabei die
- [Vollbackups](#Vollbackups)
- [Differenzielle Sicherung](#Differenzielle%20Sicherung)
- [Inkrementelle Sicherung](#Inkrementelle%20Sicherung)

## Vollbackups
Hier wird zum Zeitpunkt der Sicherung immer eine komplette Kopie des Mediums gespeichert. Diese Art verwendet viel Speicherplatz, ist dafür aber sehr simpel im Speichern und im Wiederherstellen.
Es ist empfohlen diese Art nicht als einzige zu verwenden, sondern in Kombination mit anderen speicherfreundlicheren Verfahren.

## Differenzielle Sicherung
Es wird bei jeder Sicherung alle Daten die seit der letzten [Vollsicherung](#Vollbackups) entstanden sind.
![](DifferentialBackups.png)
Beispielsweise wird jeden Montag der gesamte Datenbestand gesichert und an jedem anderen Tag nur jeweils die Daten, welche seit Montag hinzugekommen sind.

Zur Wiederherstellung muss das letzte Vollbackup und die neueste Differenz eingespielt werden.

## Inkrementelle Sicherung
Hier wird wie bei der [Differenziellen Sicherung](#Differenzielle%20Sicherung) nur selten ein Backup der gesamten Daten gemacht. An jedem anderen Tag werden nur die Daten des jeweiligen Tages gesichert.

Zur Wiederherstellung müssen so das letzte Vollbackup und alle Inkremente die seither geschrieben wurden eingespielt werden.
![](InkrementalBackup.png)

## Großvater-Vater-Sohn
Dieses Prinzip beschreibt eine Strategie um zu entscheiden, wann welche Backups gelöscht bzw. Überschrieben werden.

Am Beispiel einer [Inkrementellen Backupstrategie](#Inkrementelle%20Sicherung) wird beispielsweise das aktuellste Inkrement (der Sohn) jeden Tag überschrieben. Der Vater (das letzte Vollbackup) wird jede Woche erneuert und der Großvater jeden Monat.

![](BackupGenerations.png)


> [!Info] Sicherungssatz
> Die [Menge](Intervalle%20und%20Mengen.md#Mengen) an Sicherungen die zur vollständigen Wiederherstellung benötigt werden, bezeichnet man als Sicherungssatz.

