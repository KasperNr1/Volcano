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
| Programm $P_1$   | $1$           | $10$          | $20$          |
| Programm $P_2$   | $1000$        | $100$         | $20$          |
| Gesamtlaufzeit   | $1001$        | $110$         | $40$          |

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