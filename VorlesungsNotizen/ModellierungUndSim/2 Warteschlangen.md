---
course: "[[Modellierung und Simulation 1]]"
lecture: "2"
source: https://unitc-my.sharepoint.com/personal/iinme01_cloud_uni-tuebingen_de/_layouts/15/stream.aspx?id=%2Fpersonal%2Fiinme01%5Fcloud%5Funi%2Dtuebingen%5Fde%2FDocuments%2FTeaching%2DGITs%2Fmodellierung%5Fund%5Fsimulation%2FOnline%2FVideos%2FMuS%5F2%2D2%5F3%2D1%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E7ae80536%2Df81a%2D495a%2D8805%2D9692ea06d4bc
date: 2026-10-25
tags:
  - lecture
---
In einem Warteschlangenmodell werden ankommende Anforderungen / Ankünfte / Kunden von Bedieneinheiten (oftmals nur eine einzelne) abgearbeitet.
Bei mehr als $0$ freien Bedieneinheiten kann jeder neue Kunde sofort bedient werden.
Falls keine Bedieneinheiten verfügbar sind, müssen neue Anfragen in einem Warteraum warten. Dieser Warteraum kann endlich groß, unendlich groß oder nicht vorhanden sein.

Bei endlich großen Warteräumen kann der Raum voll sein. Neue Anfragen werden dann abgewiesen. Man spricht auch von der Blockierwahrscheinlichkeit um zu beschreiben wie viele Anfragen nicht aufgenommen werden können.

Die Wartezeit und Bearbeitungszeit zusammen ergeben die Durchlaufzeit einer Anforderung.

# Kendall Notation
Spezielle Schreibweise um die gebräuchlichsten Modelle zu beschreiben.
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

![](Pasted%20image%2020261025184638.png)

Der Zustand wird beim Eintreffen eines neuen Pakets inkrementiert. Das Abarbeiten eines Pakets reduziert den Zustand um eins.

# Discrete Event Simulation (DES)
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
