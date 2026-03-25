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

- Information Policy (Wann wird Balanciert)
- Transfer Policy (Schwellenwert-Entscheidung)
- Location Policy (Wie wird das Ziel gefunden? Polling / Broadcast / Zufällig)
- Selection Policy (Welche Tasks werden verschoben?)

### Typische Ansätze
- Sender Initiated
	- Überlastete Knoten suchen aktiv nach Unterstützung
- Receiver Initiated
	- Unterausgelastete Knoten fragen andere gezielt nach Aufgaben
- Kombiniert

### Code Migration
Weak und Strong Mobility

#### Weak
Nur Code-Segmente, wie Java-Klassen und javascript


#### Strong
Code und gesamter Ausführungszustand. (Stack, Heap, Code)
Hier wird der gesamte Prozess migriert.

Sicherheit, Heterogenität und externe Ressourcen sind dabei Herausforderungen.


Nach der Migration eines Prozess kann auf dem Ursprungsrechner ein "Shadow-Prozess" verbleiben. Er dient dazu, Systemaufrufe des migrierten Prozesses zu verwalten, die sich noch auf lokale Ressourcen (Dateien / Sockets) beziehen. Aufrufe und Daten werden ggf. an den neuen Standort des Prozess weitergeleitet.
Der Shadow Prozess wird eventuell gelöscht, wenn keine Weiterleitung mehr erforderlich ist.

Adressräume können auf mehrere Arten migriert werden
- Eager
  Alles wird auf einmal migriert
- Precopy
  Prozess läuft weiter, während Seiten übertragen werden. Modifizierte Seiten werden nachgesendet
- Eager (Dirty) 
  Nur geänderte Seiten werden übertragen. Rest nur bei Zugriff (Copy-on-Reference)
- Flushing
  Alle Seiten auf Disk speichern, dann Copy-on-reference beim Ziel

# Koordination
In verteilten Systemen wird [Parallel](Paraprog-Basics.md#Parallel%20vs%20Nebenläufig) gearbeitet. Daher gibt es keine gemeinsame Uhr, was einige Schwierigkeiten bringt.

Es werden Logiken wie "Vektoruhren" "TimeStamps" oder konsensbasierte Protokolle nötig.

Jeder Knoten besitzt eine lokale Uhr, Ereignisse können nur in Bezug auf eine solche Uhr eindeutig zugeordnet werden.

Aufgrund von unterschiedlichen Übertragungszeiten können Ereignisse in unterschiedlichen Reihenfolgen erscheinen, als sie tatsächlich geschehen sind.

![](ObserverOrder.png)

Besonders bei schreibenden Zugriffen kann dieser Umstand zu verschiedenen [Probleme](Parallele%20Probleme.md) führen.

Lösungen sind Logische Uhren. Sie erlauben Schlüsse über 
"[Happened-Before](#Happened-Before)". Also die Reihenfolge von Ereignissen, anstatt zwingend einer exakten Globalen Zeit.

## Zeitsynchronisation
### Cristians Algorithmus
Client notiert eigene Zeit und sendet Anfrage an vertrauenswürdigen Server. Nach Erhalt der Antwort berechnet der Client die gesamte Differenz zwischen Anfrage und Antwort und setzt seine Eigene Zeit $t$ auf den Wert der Antwort + die Hälfte der Round Trip Time der Anfrage.

![](CristiansAlgorithm.png)

Dieses Verfahren basiert auf 3 Annahmen.
- Der Server ist vertrauernswürdig
- Der Server braucht nahezu $0$ Zeit um die Anfrage zu beantworten
- Die im Netzwerk verbrachte Zeit sind auf Hin- und Rückweg gleich.

Typischerweise werden hier mehrere Anfragen gesendet um nicht auf einer einzelnen Antwort zu basieren.

### Zeitanpassung
Wenn die aktuelle Uhrzeit eines Systems angepasst werden muss, darf nicht direkt der neue, korrekte Wert eingetragen werden.
Stattdessen soll die Uhr vorrübergehend schneller oder langsamer laufen, um zeitliche Monotonie zu gewährleisten.

## Happened-Before
In zwei Basisfällen lässt sich die Reihenfolge von Ereignissen klar bestimmen.
1. Sie sind im selben Prozess
   Innerhalb eines lokalen Prozess gibt es eindeutige Reihenfolgen
2. Nachrichtenübertragung
   Wenn eine Nachricht gesendet wird, muss das Senden vor dem Empfangen Stattgefunden haben
Diese Regeln bilden die "happened-before" Relation $\rightarrow$


> [!NOTE] Formale Definition
> 1. Für $a$ und $b$ im selben Prozess $i$
>    $t_i(a) < t_i(b)$ dann gilt $a \rightarrow b$
> 2. Ist $a$ das Senden und $b$ das Empfangen derselben Nachricht, dann gilt $a \rightarrow b$
> 3. Transitivität
>    $a \rightarrow b$ und $b \rightarrow c$ dann $a \rightarrow c$

![](HappenedBefore.png)


