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







> [!Example] Klausuraufgabe
> Verfügbarkeit von verketteten Systemen ausrechnen
> (Seite 17-21)

# Sicherungsmethoden
- Verschiedene RAID Systeme / Strategien (Striping / Mirroring / Parity)
- Backup-Strategien (Voll-Backups / Inkrementelle Sicherung)
- Schadsoftware