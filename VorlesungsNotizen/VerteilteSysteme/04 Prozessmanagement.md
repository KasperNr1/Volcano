# Ziele
- Load Balancing
- Max-Systemleistun (Min Mittlere Antwortzeit)
- Minimale Kommunikation zwischen Knoten

# Ansätze
[Statisches](#Statisches%20Scheduling) und [Dynamisches scheduling](#Dynamisches%20Scheduling), wobei Verteilung entweder vor oder während der Ausführung geschieht.

## Statisches Scheduling
Die Zuordnung eines Jobs basiert auf seiner Struktur und Modellierung, sie wird vor der Ausführung festgelegt.

> [!NOTE] Komplexität
> Die Statische Verteilung von Aufgaben ist NP-komplex

Kommunizierende Prozesse über Graph-Partitionierung.
Nicht-Kommunizierende Prozesse Tasks: List Scheduling

### Graph-Partitionierung
![](GraphPartitioning.png)

Jede Kante symbolisiert die Kosten für die Kommunikation zwischen zwei Knoten.
Es wird versucht die Knoten aufzuteilen und die Kosten für Kommunikation zwischen den Partitionen zu minimieren.

![](GraphPartitition1.png)

![](GraphPartitition2.png)

### List Scheduling
Annahme ist, dass die Tasks nur vor / nach der Arbeit kommunizieren müssen. Während der Runtime kann minimaler Austausch stattfinden, sollte aber wenig Overhead besitzen.

Die Tasks werden als DAG modelliert.
![](ListScheduling.png)

In den Knoten steht der Name des Prozess, sowie seine Ausführungszeit.
Die Gewichte der Knoten beschreiben den Aufwand für die Kommunikation zwischen zwei Tasks.
Diese Zeitwerte werden vorrausgesetzt, sie müssen aus historischen Aufzeichnungen oder anderen Quellen stammen.

Priorisierung kann veschieden erfolgen, (High Level First with Estimated Time) oder (Earliest Time First)

#### HLFET
Ziel ist die Minimierung der Gesamtausführungszeit.

Tasks mit dem höchsten "Level" (Kritischer Pfad) werden zuerst bearbeitet.
- $w(v)$ ist die Ausführungszeit von Task $v$
- $succ(v)$ ist der Nachfolger von Task $v$

Für Endknoten ist $level(v) = w(v)$. Sonst gilt:


> [!NOTE] Endknoten
> Ein Endknoten ist der "unterste" im Graph, also der keine Nachfolger in der Ausführung besitzt


$$
level(v) = w(v) + \max_{u \in \text{succ}(v)} level(u)
$$

Tasks werden absteigend nach level sortiert und so priorisiert.
Tasks im kritischen Pfad erhalten automatisch ein hohes Level und werden bevorzugt bearbeitet.


> [!Example] Klausuraufgabe
> Prioritätenliste aus Ausführungsgraph erstellen und schedulen (Seite 265)
> Kommunikationskosten fallen nur zwischen Knoten an. (siehe lösung auf 266)

![](HlfetListScheduling.png)





## Dynamisches Scheduling
Bei dynamischem Load Balancing kann der Ausführungsort zur Erstellung des Prozess festgelegt werden. In einer anderen Variante kann er zur Laufzeit wieder verändert werden ("Prozessmigration")