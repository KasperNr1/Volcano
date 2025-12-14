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

