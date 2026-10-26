---
course: "[[Modellierung und Simulation 1]]"
lecture: "2"
source: https://unitc-my.sharepoint.com/personal/iinme01_cloud_uni-tuebingen_de/_layouts/15/stream.aspx?id=%2Fpersonal%2Fiinme01%5Fcloud%5Funi%2Dtuebingen%5Fde%2FDocuments%2FTeaching%2DGITs%2Fmodellierung%5Fund%5Fsimulation%2FOnline%2FVideos%2FMuS%5F2%2D2%5F3%2D1%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E7ae80536%2Df81a%2D495a%2D8805%2D9692ea06d4bc
date: 2026-10-25
tags:
  - lecture
---
Die Abbildgung zeigt die verschiedenen Klassen von Simulationsmodellen.
Die Präzisesten Werte liefert Messung am echten System, wobei der Aufwand höher ist die Messungen alle exakt durchzuführen.
In Abstrakten Modellen wird die Simulation auf einige wenige Kernelemente des Systems beschränkt und ist damit deutlich einfacher.

![](KategorienVonSimulationen.png)


> [!Info] Vorlesungsinhalt
> In der Vorlesung MuS wird der Fokus auf System- und abstrahierende Modelle gelegt


# Warteschlangenmodelle
In einem Warteschlangenmodell werden ankommende Anforderungen / Ankünfte / Kunden von Bedieneinheiten (oftmals nur eine einzelne) abgearbeitet.
Bei mehr als $0$ freien Bedieneinheiten kann jeder neue Kunde sofort bedient werden.
Falls keine Bedieneinheiten verfügbar sind, müssen neue Anfragen in einem Warteraum warten. Dieser Warteraum kann endlich groß, unendlich groß oder nicht vorhanden sein.

Bei endlich großen Warteräumen kann der Raum voll sein. Neue Anfragen werden dann abgewiesen. Man spricht auch von der Blockierwahrscheinlichkeit um zu beschreiben wie viele Anfragen nicht aufgenommen werden können.

Die Wartezeit und Bearbeitungszeit zusammen ergeben die Durchlaufzeit einer Anforderung.

## Kendall Notation
Spezielle Schreibweise um die gebräuchlichsten Modelle zu beschreiben.

> [!Info]- Nicht in Notation darstellbares Beispiel
> Warteschlangenmodell mit Blockabfertigung. Z.b. IP-Pakete bei Live-Übertragung oder Achterbahnen. Die Bedieneinheit soll bei geringen Anfrageaufkommen möglichst warten um viele Anfragen gleichzeitig zu bearbeiten. Gleichzeitig soll eine maximale Wartedauer für einzelne Anfragen sichergestellt werden.
> 
> Diese Zeitliche Schranke lässt sich beispielsweise nicht in der Notation darstellen.

$$
\text{GI}^{[X]} / \text{GI} / n-S
$$
- Dabei ist mit $\text{GI}$ eine ‘general independant’ also unabhängige Zufallswahrscheinlichkeit beschrieben.
- Das $[X]$ beschreibt die Größe eines `batches` wenn neue Anforderungen nicht einzeln, sondern in Gruppen eintreffen.
- Das zweite $\text{GI}$ beschreibt die Verteilung bei der Bearbeitung einer einzelnen Anfrage.
- $n$ beschreibt die Anzahl der Bedieneinheiten
- $s$ ist die Anzahl der Warteplätze. Bei einem endlichen Wert spricht man auch von einem `Verlustsystem`

Anstelle der $\text{GI}$ Verteilung ist auch $\text{D}$ für Deterministisch, $\text{M}$ für Markov (Also [exponentiell verteilt](1%20Wahrscheinlichkeiten%20und%20Verteilungen.md#Exponentialverteilung). Ein M-Ankunftsprozess ist dementsprechend ein [Poisson](Spezielle%20Verteilungen.md#Poissonverteilung)-Prozess), $\text{E}_k$ für Erlang-k und $\text{H}_k$ für Hyperexponentiell k-ter Ordnung verteilt.

# Ereignistreue Simulationen
Beispielhaft wird ein einstufiges GI/GI/1-S Wartesystem gezeigt.
Das Ausgehende Interface eines [Routers](04%20Network%20Layer.md#Geräte) ist ein System mit solchen Eigenschaften.
Es fallen einzelne Anfragen mit unterschiedlichen Zeitabständen an und werden von einer Bedieneinheit in unterschiedlichen Zeiten bearbeitet. Dabei gibt es einen endlich großen Speicher um Anfragen zu halten.

Der Systemzustand $X(t)$ beschreibt die Anzahl der zum Zeitpunkt $t$ im System enthaltenen Pakete (Aktive in Bearbeitung + Aktuell Wartende).
Der Zustand kann sich durch Ankunfts- und Bedienereignisse verändern.

![](EinführungsbeispielEreignistreueSimulation.png)

Der Zustand wird beim Eintreffen eines neuen Pakets inkrementiert. Das Abarbeiten eines Pakets reduziert den Zustand um eins.

# Discrete Event Simulation (DES)

> [!Tip] Definition
> Eine Ereignistreue Simulation (Event Discrete Simulation) ist die Modellierung der zeitlichen Entwicklung eines Systems durch eine Darstellung, bei der sich die Zustandsvariablen des Systems an diskreten Zeitpunkten augenblicklich ändern. Diese Zeitpunkte werden als ‘Ereignisse’ bezeichnet.

Es gibt allerdings auch Ereignisse, die nicht zu Zustandsänderungen führen.


## Bestandteile
- Simulation Clock
  Bestimmt die Zeitpunkte in denen sich das System befindet. Abhängig vom Kontext kann hier Echtzeit, diskrete Schritte mit Tages-Präzision oder beliebige andere Größen verwendet werden.
  Häufig wird zur Implementierung ein `long int` verwendet um große fortlaufende Zeitbereiche beschreiben zu können.
- Events
  Sind mit diskreten Simulationszeitpunkten assoziiert.
  Zu diesem Zeitpunk wird eine Event Routine ausgeführt, die eine Aktion im System verursacht und z.B. den Systemstatus verändern kann.
  Die `Event Chain` verwaltet diese Ereignisse
- Statistic Counters
  Sind Variablen zur Speicherung von statistischen Informationen über das System
	- Diskrete Zähler, z.B. Paketgrößen
	- Time-weighted Counters, z.B. Warteschlangenlängen
	- [Momente](1%20Wahrscheinlichkeiten%20und%20Verteilungen.md#Zentrale%20Momente), Konfidenzintervalle, Output-Generierung
- Hauptprogramm
  Definition und Initialisierung des Systemzustands
  Kontrolle und Abarbeitung der Event-Chain, Bestimmung der nächsten Ereignisse und Verwaltung der Simulationsuhr.
  Ausführung von Event Routinen und Kontrolle der Simulationsdauer.
- Report Generator
  Erstellung einer verständlichen Ausgabe der Simulationsergebnisse am Ende der Simulation.
  Leistungsmaße auf Basis der statistic Counters

## Hauptmodellierungsansätze
- Ereignisorientiert (Event-Scheduling-Approach)
  - Sequentielle Abarbeitung der Ergebnisse nach obigem Konzept
  - Fortschreiten der Simulationszeit nur bei Ankunft und Bearbeitung von Anfragen
- Prozessorientiert
  - Fokus der Betrachtung ist ein Objekt (z.B. die Warteschlange)
  - Simulationszeit kann während einem Prozess fortschreiten
  - Wegen dem Einfachen Aufbau wird dieser Ansatz zur Modellbeschreibung auch in Simulationssprachen wie OpNet verwendet
  - Ein Beispiel ist die prozessorientierte Modellbeschreibung eines $GI/GI/1-\infty$ Warteschlangensystems

Das Ablaufdiagramm zeigt eine Prozessorientierte Sichtweise.
![](ProzessorientiertesBeispielZustandsgraph.png)


# Klassifikation von Simulationsmodellen
Modelle können stochastisch oder deterministisch sein. Bei Stochastischen Systemen muss generell länger oder öfter simuliert werden, um Aussagen über den [Erwartungswert](Zufallsvariablen.md#Erwartungswert) treffen zu können.

Auch die Unterscheidung zwischen kontinuierlichen und Diskreten Zeitschritten ist sehr wichtig. Z.B. Chemische Reaktionen sind kontinuierlich während Lagebestände nur an einzelnen Tagen bestimmt werden.
Innerhalb dieser Vorlesung werden nur diskrete Simulationen betrachtet.

Statische Simulationen haben maximal einen relevanten Zeitpunkt. Es kann auch Simulationen geben die ohne Zeit stattfinden. Z.B. das Bestimmen von stochastischen Werten beim Wurf von Würfeln.
Dynamische Simulationen hingegen entwickeln sich im Verlauf einer Zeit.

# Fokus von Simulationen
Die Fragestellungen die mit einer Simulation beantwortet werden soll können sehr unterschiedlich sein und bedürfen verschiedener Modelle und Simulationen.
- Bestimmung der Durchlaufzeit eines Produkts in einer Fabrik bei einem bestimmten Produktmix
- Vergleich unterschiedlicher [Scheduling](Middleware.md#Scheduling)-Mechanismen in einer Maschine

# Bestandteile einer Simulationsstudie
1. Formulierung des Problems (Meist ist die zu Beginn noch nicht fest / final)
2. Sammeln von Daten und Erstellung eines konzeptionellen Modells
3. Verifizierung des Modells (Bei Fehlern weiter mit Schritt 2)
4. Implementierung des Modells in einem Computerprogramm
5. Erste Läufe des Programms
6. Validierung der Programm-Outputs (Bei Fehlern zurück zu Schritt 2)
7. Design der Experimente
8. Durchführen der Experimente
9. Analyse der Ausgabedaten
10. Dokumentation, Präsentation und Verwendung der Ergebnisse

> [!Info] Anwendung in der Praxis
> Die Kenntnis des Modells wächst mit dem Verlauf der Zeit.
> In der Praxis werden daher oft mehrere Iterationen durchgeführt um das Modell zu verfeinern
