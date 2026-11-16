Rechenregeln Skript 1.3.6

# Vorlesung 2
Definition [Discrete Event Simulation (DES)](2%20Simulationsmodelle.md#Discrete%20Event%20Simulation%20(DES))

[Kendall Notation](2%20Simulationsmodelle.md#Kendall%20Notation) für einfache Warteschlangenmodelle anwenden können.

[Bestandteile](2%20Simulationsmodelle.md#Bestandteile) eines Simulationsmodells beschreiben und erklären können.
Insbesondere die Simulationszeit / Echtzeit (Darstellung von Zeit als Int um gleichbleibende Abstände zu sichern)

Diagramm aus [Hauptmodellierungsansätze](2%20Simulationsmodelle.md#Hauptmodellierungsansätze) lesen und für einfache Systeme erstellen können.

[Klassifikation von Simulationsmodellen](2%20Simulationsmodelle.md#Klassifikation%20von%20Simulationsmodellen)

# Vorlesung 3?
Accept-Reject Methode Herleiten, erklären und verwenden

Majorante?

Bedeutungen der Verteilungen (Gleichungen weniger wichtig aber auch relevant)
3.2.1 Alles außer Varianz
3.2.2 Verteilungs(dichte)funktion, Erwartungswert, Variationskoeffizient

Zusammenhang zwischen Begriff “Rate” und Parameter $\lambda$ in Exponentialverteilung erklären

Was modelliert die Erlang K Verteilung?
- Die Summe von K exponentiell verteilten Zufallsvariablen
Wertebereich, Mittelwert (Dichte-Funktionen sind nicht relevant)

Was ist eine $\text{H}_2$
- Hyperexponentiale Verteilung 2ter Ordnung

# Vorlesung 4
Gesamtes Kapitel 3 ([3 Verteilungsfunktionen](3%20Verteilungsfunktionen.md) und [4 Diskrete Verteilungen](4%20Diskrete%20Verteilungen.md)) sehr relevant für Klausur, besonders die Wahl von Verteilungsfunktionen um verschiedene Systeme zu modellieren und die Übertragbarkeit von diskreten auf stetige Verteilungen.

Vergleichsdiagramm [Vergleich](3%20Verteilungsfunktionen.md#Vergleich) beschriften können und die Verwandtschaft zwischen den Verteilungen kennen.

Wissen, dass Normalverteilung per Accept-Reject erzeugt wird. Algorithmus muss nicht exakt auswendig gewusst sein.

Erzeugungsalgorithmus [Beliebige Diskrete Verteilung](4%20Diskrete%20Verteilungen.md#Beliebige%20Diskrete%20Verteilung)

Summe einer unendlichen Reihe mit unendlich vielen Termen

Erzeugungsalgorithmus der Poisson-Verteilung durch Quasi-Komponente

Konfidenzintervalle (Sehr wichtig)
Unterschied Standardabweichung und Standardfehler, beide Begriffe existieren Separat

Begriffe
- Freiheitsgrade
- Quantile
- OneSided
- TwoSided

# Vorlesung 5
Konfidenzintervalle, Herleitung und Bedeutung

Gleichung zur empirischen Berechnung der [Autokovarianz](5%20Fehler%20und%20Konfidenzintervalle.md#Autokovarianz) wiedergeben.
Ebenfalls Gleichungen zu [Korrelation](5%20Fehler%20und%20Konfidenzintervalle.md#Korrelation) und [Kovarianz](5%20Fehler%20und%20Konfidenzintervalle.md#Kovarianz) angeben können (Jeweils Zufallsvariable und Empirisch zu Zeitreihen).

# Vorlesung 6
Batch Mean Verfahren
Warum kann man die normale Statistischen methoden nicht verwenden? (Korrelation der einzelnen Werte - Für viele Methoden wird unabhängigkeit angenommen)
Replicate-Delete-Verfahren
Vor- und Nachteile kennen
Vorteile
- Einfach
- Nicht anfällig gegen Korrelation
- In Software breit als Packages Verbreitet
Nachteile
- Korrekte Bestimmung der Transienten Phase ist notwendig
- Dadurch höherer simulationsaufwand

Bei Batch-Mean Verfahren sind Vor-und Nachteile exakt gegenteilig

Check-Knife Estimator verstehen, nicht auswendig

Definitionen Zeit-Mittel und Ensemble-Mittel

Was ist ein (Nicht)-Ergodischer Prozess?
Jeweils Beispiele

Ein Unterschied zwischen zwei Systemen ist statistisch Relevant wenn die 0 nicht im Konfidenzintervall der Differenz liegt.
Diese Erkenntnis ist essentiell und leicht zu berechnen.

6.8.2.3
Argumentation verstehen
Vergleichbare Bedingungen -> Kleine Varianz -> Schmaleres Konfidenzintervall -> Kürzere Simulation notwendig bis 0 nicht im Konf.Intervall liegt.



