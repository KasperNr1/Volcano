# Klausur
Komplettes Skript / Mitschriebe erlaubt
Tilmann.Wendel@Advantest.com
twendel@hb.dhbw-stuttgart.de
Geschichten aus der Geschichte Daniel Messner und Richard

# Architektur nach von Neumann
![](vonNeumann.png)
Rechner besteht aus Funktionseinheiten
- Rechenwerk
- Steuerwerk
- Speicherwerk
- Eingabe / Ausgabe

Bus-System als Bottleneck (Von Neumannscher Flaschenhals)
Struktur ist unabhängig vom Problem

> [!NOTE] Sicherheit
>Anweisungen, Daten und Zwischenergebnisse liegen im selben Speicher, Eingabedaten können nicht unbedingt vom Programmcode unterschieden werden
>
>`a')´ drop table --` 
>
>Versucht die Trennung zu umgehen

- Nur ein Bus ist zur Datenübertragung notwendig
- Reihenfolge der Befehle wird durch Sprungbefehle realisiert
- Bitvektoren enthalten keine Angaben über ihren eigenen Typ
Streng Sequentieller Ablauf ist vorteilhaft gegenüber parallelen Architekturen, da das Programmieren leichter und weniger fehleranfällig ist.

# Harvard Architektur
![](HarvardArchitektur.png)
- Gleichzeitiges Lesen und Schreiben von Daten und Befehlen möglich
- Einfache Verwaltung von Zugriffsrechten und Speicherschutz

> [!Warning] Nachteile gegen von Neumann
> Race Conditions sind möglich
> Kein Deterministischer Ablauf

Getrennter Speicher für Daten und Code -> separate Busse zur Übertragung

Qualcom Aktie

# Leistungsvergleich von Systemen
Welche Kriterien werden verglichen?
- Preis
- Geschwindigkeit
- Bandbreite (Menge an Kassen)
- Durchsatz (Tatsächlich offene Kassen)
- Stromverbrauch
- Größe
- Gewicht

Benutzersicht
- Antwortzeit
Anbietersicht
- Durchsatz vs. Bandbreite
Beide
- Ausführungszeit

## Leistungsmessung
### Definitionen
- Laufzeit
- CPU Zeit
- User CPU Zeit
- TODO
$$
\text{Leistung} = \frac{1}{\text{Ausführungszeit}}
$$
Sinnvolle Leistungsdefinitionen
- Systemleistung (Laufzeit in einem unbelasteten System)
- CPU-Leistung Betrachtung unabhängig von I/O und OS
Was messen? 
- Reale Programme

Eindeutige Leistungsmessung sehr schwierig (Stark Use-Case abhängig)

Mögliche Programm Typen:
- Reale Applikationen
	- Text
	- Bild
	- Datenbank
	- Problem: Portabilität, Interaktivität
- Skript Applikationen
	- Simulation von PC-Verwendung
- Spiel Benchmarks
- Tante Erna Test
Mischbewertung passt oft gut

### Dokumentation
Reproduzierbarkeit, genaue Angaben
- Getestetes System
- Hardware Konfiguration
- Software Einstellungen (Compiler Optionen)

Verwendung mehrerer Benchmark Suiten?
- Summe
- Mittelwert (gewichtet?)
  Benchmark $A$ entspricht tatsächlichem UseCase besser als $B$

### Berechnung
Arithmetisches vs. Geometrisches Mittel
TODO

### Optimierung

Geometrisches Mittel:
$2s \rightarrow 1s$ scheint gleich wie $1000s \rightarrow 500s$ 

> [!Info] Make The Common Case Fast
> Tatsächliche Zeitersparnis besser bei Optimierung tatsächlich häufig verwendeter Berechnungen

$$
\text{Speedup} = \frac{\text{Zeit ohne Optimierung}}{\text{Optimierte Zeit}}
$$

Gesamtspeedup bei Optimierung eines Teilsystems (Beide Gleichungen verwandt und in einander umformbar)
$$
S_{tot} = \frac{1}{(1-P)+\frac{P}{S}}
$$
Amdahls Law! (TODO)

> [!Example] Klausuraufgabe
> Foliensatz 1, Seite 40 (Amdahls Law IV)
> Vergleich große Optimierung seltenes Feature - Weniger Starke Optimierung Common Case 

## CPU Leistungsmessung
- CPU Zeit = Zykluszeit * CPU-Zyklen für Programm
- CPU Zeit = IC * CPI * (1/Taktrate)
$$
\text{CPU-Zeit} = \frac{\text{Instruktionen}}{\text{Programm}} * \frac{\text{Taktzyklen}}{\text{Instruktionen}} * \frac{\text{Sekunden}}{\text{Taktzyklus}}
$$

## Prinzip der Lokalität
Eigenschaft von Programmen:
- Blinde Wiederverwendung von Code & Daten (Cache) die kürzlich verarbeitet wurden (Kontrolle im Hintergrund)
- 10% Code werden in 90% der Zeit tatsächlich verwendet

Örtliche Lokalität (Nah beinander) vs. Temporale Lokalität (Vor kurzem verwendet)

## Mögliche Irrtümer
- Gleicher Befehlssatz der CPU ist bedeutet nicht, dass diese Rechner nur anhand der Taktrate vergleichbar sind.
- Instructions per Second variiert stark je nach Programm.
  Außerdem stark abhängig vom Befehlssatz

## Programmiermodelle
- Desktop -> Viel Integer / Floating Point
- Server -> Integer / Strings
- Embedded -> Codegröße & Stromverbrauch

## Entwurfsmodelle
1. Simple gets regular
2. Small is fast
3. Make the Common Case Fast
4. Good Design means Compromises

# Übungen
## 2
### 2.1
3x1280x1024

### 2.2
250MB / (0.9 * 10^9)

## 3
### 3.1
IC kürzt sich raus, Rest gegeben mit [CPU Leistungsmessung-Gleichung](#CPU%20Leistungsmessung)
- [ ] Nicht gewählt
- [x] COole Liste


> [!example] Klausurfrage
> CPI und Takt nutzen um Rechner zu vergleichen


