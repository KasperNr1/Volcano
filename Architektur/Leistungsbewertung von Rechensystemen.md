# Vergleichskriterien
Je nach Anwendungsfall kann die Menge an zu betrachtender Kriterien stark variieren.
Häufig sind jedoch die folgenden vertreten:
- Preis
- Größe
- Gewicht
- Stromverbrauch
- Bandbreite
- Durchsatz
- Geschwindigkeit

> [!NOTE] Bandbreite vs. Durchsatz
> Am Beispiel einer Supermarktkasse können die beiden Begriffe gut veranschaulicht werden.
> Die Menge der Verbauten Kassen ist die Bandbreite. Sie bestimmt den maximal möglichen Durchsatz.
> Dieser entspricht der Anzahl tatsächlich geöffneter Kassen.

Ebenfalls ist die Perspektive des Betrachters für einen Vergleich relevant.
Ein Benutzer wird primär auf die Antwortzeit des Systems achten, während für den Anbieter eines Service eher die Bandbreite im Vordergrund steht.
Wichtig für alle ist jedoch die Ausführungszeit.

# Leistungsmessung
Ein Rechner $A$ der die selbe Arbeit in weniger Zeit vollbringt ist schneller als ein Rechner $B$.
Ausführungszeit und Leistung sind invers zu einander.
$$
\text{Leistung} = \frac{1}{\text{Ausführungszeit}}
$$

## Ausführungszeit
Mit Ausführungszeit können verschiedene Messungen gemeint sein. 

### Laufzeit
Beschreibt die gesamte benötigte Zeit.
In dieser Messung sind auch I/O und Speicherzugriffe enthalten. Ebenso eventuelle Wartezeiten die vom [Scheduler](Paraprog-Basics.md#Scheduler) verursacht sind.
Auch die vom Betriebssystem selbst verbrauchte Leistung wird im Ergebnis reflektiert und nicht rausgerechnet.

### CPU Zeit
Hier werden die Wartezeiten auf andere Programme und Betriebssystem mathematisch korrigiert. Der Wert spiegelt also nur die Zeit wieder, in der der zu messende Code auch tatsächlich im CPU verbracht hat um ausgeführt zu werden.

### User CPU Zeit
Sehr idealisierte Zeit in der nur die Ausführungszeit des Quellcodes enthalten ist. Verzögerungen, die durch das Betriebssystem entstehen, sind nicht enthalten.

## Leistungsdefinitionen
Bei einer Leistungsmessung geht man zur besseren Vergleichbarkeit von einem unbelasteten System aus. Ein Mehrprogrammbetrieb ist nicht erwünscht.
Um Unabhängigkeit von IO und OS zu gewährleisten wird die [User CPU Zeit](#User%20CPU%20Zeit) verwendet.

## Programmwahl
Es sollten immer reale Programme gemessen werden.
Aufgrund der großen Unterschiede zwischen möglichen Nutzungsprofilen eines Rechners ist es wichtig verschiedene Arten von Last zu testen (Spiele, Simulationen, Textbearbeitung, Browser)
Mögliche Programmtypen:
- Reale Applikationen
- Geskriptete Applikationen
  Benutzereingaben sind hier mit Skripts automatisch simuliert
- Kernels
  Sind kleine Teile realer Applikationen und dienen nur zur Leistungsmessung
- Spiel Benchmarks
- Tante Erna Test
  Zeit von Spannungsversorgung bis absenden einer Email

Es gibt eine Reihe an offizieller Benchmarks die versuchen alle Anwendungsbereiche bestmöglich abzudecken. (SPEC oder TPC-C)
Diese Mischbewertung passt oft sehr gut.

## Vergleich von Leistungsmessungen
Beispiel: Für die Rechner $A$, $B$, $C$ wurden jeweils die Programme $P_1$ und $P_2$ getestet.

| Zeit in Sekunden | Rechner $A$ | Rechner $B$ | Rechner $C$ |
| ---------------- | ----------- | ----------- | ----------- |
| Programm $P_1$   | $1$         | $10$        | $20$        |
| Programm $P_2$   | $1000$      | $100$       | $20$        |
| Gesamtlaufzeit   | $1001$      | $110$       | $40$        |

Es kann nicht sofort eine Gesamtleistung der Systeme erkannt werden.
Man kann mit Bezug auf konkrete Programme Vergleichen:
- $A$ ist $20$ mal schneller als $C$ um $P_1$ zu berechnen
- $B$ brauch $5$-mal länger für $P_2$ als $C$
- $\dots$

In der zu erwartenden Belastung werden nicht alle Programme gleich oft verwendet werden. Man berechnet eine gewichtete Summe.
$$
\sum_{i=1}^{n} \text{Gewicht}_i * \text{Laufzeit}_i
$$
Gewichtung könnte hier nach der Frequenz des Programms im System gewählt werden.

$$
\text{Gewicht}_i = \frac{1}{\text{Laufzeit}_i * \sum_{j=1}^{n} \frac{1}{\text{Laufzeit}_j}}
$$

Es kann sinnvoll sein die Ausführungszeit auf eine Referenzmaschine zu normalisieren. Bei SPEC wird hier die [SPARCstation](https://de.wikipedia.org/wiki/SPARCstation) verwendet.

Hier ist es von Vorteil den [Geometrischen Mittelwert](Folgen.md#Geometrisches%20Mittel) der Laufzeitverhältnisse anzugeben.
$$
\sqrt[n]{\prod_{i=1}^{n} \frac{\text{Laufzeit}_i}{\text{Referenzlaufzeit}_i}}
$$

### Beispiel
Gezeigt sind die Messwerte für beide Programme auf allen Maschinen. (Oben Links)
In den Mittleren Reihen sind die Verhältnisse zur Geschwindigkeit einer Referenzmaschine gegeben. Links mit $\text{Ref} = A$ und rechts mit $\text{Ref} = C$ 
In den Letzten Reihen werden jeweils die Mittelwerte der Verhältnisse berechnet.

|                  |   A    |   B    |    C    |    A    |   B    |   C   |                  |
| :--------------: | :----: | :----: | :-----: | :-----: | :----: | :---: | :--------------: |
|      $P_1$       |  $1$   |  $10$  |  $20$   |         |        |       |                  |
|      $P_2$       | $1000$ | $100$  |  $20$   |         |        |       |                  |
| $\dfrac{P_1}{A}$ | $1.0$  | $10.0$ | $20.0$  | $0.05$  | $0.5$  | $1.0$ | $\dfrac{P_1}{C}$ |
| $\dfrac{P_2}{A}$ | $1.0$  | $0.1$  | $0.02$  | $50.0$  | $5.0$  | $1.0$ | $\dfrac{P_2}{C}$ |
|   Arithmetisch   | $1.0$  | $5.05$ | $10.01$ | $25.03$ | $2.75$ | $1.0$ |                  |
|   Geometrisch    | $1.0$  | $1.0$  | $0.63$  | $1.58$  | $1.58$ | $1.0$ |                  |

---

Vorteil der Verwendung des geometrischen Mittels ist die Unabhängigkeit von der Referenzmaschine. Besonders beim Arithmetischen Mittel dieser Größen ist das nicht der Fall.
Allerdings kann aus diesen Ergebnissen keine tatsächliche Vorhersage zur Laufzeit gemacht werden. Ebenfalls haben Verbesserungen einen Effekt auf das Gesamtergebnis das proportional zur Größe des Problems.
Eine Verbesserung von $2s \to 1s$  würde gleich bewertet wie $1000s \to 500s$.

# CPU Leistungsgleichung
Rechner arbeiten mit einer Konstanten Taktrate. 
$$
\begin{array}{ll}
\text{CPU-Zeit} &= \text{Zykluszeit} * \text{CPU-Taktzyklen} \\
&= \dfrac{\text{CPU-Taktzyklen}}{\text{Taktrate}}
\end{array}
$$

Instruction Count (IC) ist die Menge der ausgeführten Instruktionen.
$$
\text{Taktzyklen pro Programm} = \text{IC} * \text{CPI}
$$
$$
\text{CPU-Zeit} = \text{IC} * \text{CPI} * \frac{1}{\text{Taktrate}}
$$
$$
\text{CPU-Zeit} = \frac{\text{Instruktionen}}{\text{Programm}} * \frac{\text{Taktzyklen}}{\text{Instruktion}} * \frac{\text{Sekunden}}{\text{Taktzyklen}}
$$
# Prinzip der Lokalität
Eigenschaft von Programmen:
- Blinde Wiederverwendung von Code & Daten (Cache) die kürzlich verarbeitet wurden (Kontrolle im Hintergrund)
- 10% Code werden in 90% der Zeit tatsächlich verwendet

Örtliche Lokalität (Nah beinander) vs. Temporale Lokalität (Vor kurzem verwendet)

## Mögliche Irrtümer
- Gleicher Befehlssatz der CPU ist bedeutet nicht, dass diese Rechner nur anhand der Taktrate vergleichbar sind.
- Instructions per Second variiert stark je nach Programm.

Außerdem stark abhängig vom Befehlssatz