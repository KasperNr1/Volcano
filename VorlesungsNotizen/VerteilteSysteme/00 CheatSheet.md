# Arten
## Cluster
Ähnliche Workstations, High-Speed-LAN
## Grid-Computing
Diverse Rechner, weite Strecken

1. Anwendungsschicht (Nutzt Ressourcen durch Schnittstellen)
2. Kollektive Ebene (Bietet Schnittstellen für Zugriff)
3. Verbindungs- und Ressourcenebene
	- Verbindungsebene (Anwendung von Kommunikationsprotokollen und Sicherheitsmaßnahmen)
	- Ressourcenebene (Verwaltung einzelner Ressourcen)
4. Infrastruktur (Stellt Schnittstellen zu lokalen Ressourcen dar)

# Cloud-Computing
1. Anwendung
2. Daten
3. Runtime
4. Middleware
5. Betriebssystem
6. Virtualisierung
7. Server
8. Storage
9. Netzwerk

|                           | On-Premise | IaaS | PaaS | SaaS |
| ------------------------- | ---------- | ---- | ---- | ---- |
| Verwaltung durch Kunde    | 1-9        | 1-5  | 1-2  | -    |
| Verwaltung durch Provider | -          | 6-9  | 3-9  | 1-9  |

# Verteilte Informationssysteme
Integrieren Anwendungen zu einem firmenweiten System. Bereitstellung i.d.R. durch einige wenige Server.

# Allgegenwärtige Systeme
Pervasive: Smart Devices in die Umwelt integriert, Kommunikation typisch ohne UI.
Ubiquitous: Unsichtbar im Hintergrund - Klimatisierung ohne Interaktion
# Transparenz
- Zugriffstransparenz
  Gleiches Verhalten bei Zugriff auf Lokale und entfernte Ressourcen
- Positionstransparenz
  Zugriff ohne Kenntnis über den Standort
- Nebenläufigkeitstransparenz
  Mehrere Prozesse beinträchtigen sich gegenseitig nicht
- Replikationstransparenz
  Nutzung mehrerer Instanzen ohne dass diese Repliken sichtbar sind
- Fehlertransparenz
  Fehler werden verborgen, Nutzer können weiterarbeiten
- Mobilitätstransparenz
  Ressourcen und Clients können verschoben werden ohne dass Nutzer dies merken
- Leistungstransparenz
  Systemoptimierung bei Laständerungen bleiben für Nutzer unsichtbar
- Skalierungstransparenz
  Das System kann wachsen, ohne dass Änderungen an der Architektur oder den Anwendungsalgorithmen notwendig sind

# Dienste
## Namensdienst
Zuordnung von Namen zu Referenzen / Adressen. Name als eindeutiger Identifier.
Clients fragen Dienste über Namen an, somit sind Adresswechsel möglich.

Entkoppelt Client von Server.

## Session Management
Jede Client Instanz erhält eine Session (User ID, Warenkorb)

Session Daten können transient oder persistent sein.
Speichern Serverseitig oder client-seitig (Cookies)

Middleware sorgt für transparente Zuordnung von Requests zu Sessions

## Transaktionsverwaltung
[Bildet eine Folge von Aktionen als atomare Operation](Transaktionen.md) ab.
1. Daten Holen
2. Modifizieren
3. Zurückschreiben

## Persistenzservice
Intelligente Schnittstelle zur Datenbank.

Häufigst als "Object-Relational-Mapper" (ORM)
Dabei werden Klassen als Tabellen, Attribute als Spalten und Objekte als Zeilen dargestellt.

# Scheduling
## Graph-Schedule
Graph-Scheduling für Kommunizierende Prozesse. Es wird versucht die Kommunikationskosten zu minimieren.
![GraphPartitition2](GraphPartitition2.png)

## List-Schedule
List Scheduling wird verwendet wenn Tasks nur vor / Nach der Arbeit kommunizieren müssen. Austausch zur Laufzeit ist nicht verboten, sollte aber minimal sein, da es beim Scheduling nicht beachtet wird.
Tasks werden im DAG (Directed Acyclical Graph) modelliert
![HlfetListScheduling](HlfetListScheduling.png)

Beim ETF (Earliest Time First) werden Prozesse bevorzugt, die einen möglichst frühen Startzeitpunkt haben.

Beim HLFET (High Level First with Estimated Times) werden Kritische Prozesse bevorzugt.

Für Endknoten ist $level(v) = w(v)$. Sonst gilt:

$$
level(v) = w(v) + \max_{u \in \text{succ}(v)} level(u)
$$

# Zeitstempel
![](LamportTimestamps.png)

Bei Vektoruhren wird nach jeder Nachricht der Maximale Wert jeder Koordinate übernommen. Bei lokalen Ereignissen wird der lokale Zähler erhöht.
![](VectorClocks.png)


# Consistent Cuts

![](ConsistentCuts.png)

Nachrichten dürfen "Ins Leere" verschickt werden, aber nie aus dem nichts auftauchen.
Ein Zustand ist dabei alles "links" der Schnittkante.

## Snapshot Algorithmus nach Chandy & Lamport
Ziel ist die Erstellung eines konsistenten globalen Zustands in einem verteilten System, ohne die Prozesse zu blockieren.
Vorraussetzung dafür sind zuverlässige FIFO Kanäle und starker Zusammenhang des Prozessgraphen. Jeder Prozess kann einen Snapshot initiieren.

> [!NOTE] Starker Zusammenhang
> Bedeutet, dass im gerichteten Graph jeder Knoten von jedem Startpunkt erreichbar ist.

1. Ein Prozess $P$ startet einen Snapshot
2. $P$ Speichert sofort seinen lokalen Zustand (Speicher, Variablen, Queue-Zustand)
3. $P$ Sendet über jeden ausgehenden Kanal eine spezielle *Marker*-Nachricht
4. Marker signalisiert anderen Prozessen: "Alles aus diesem Kanal gehört zum Snapshot vor oder nach diesem Marker"
5. Jeder andere Prozess $Q$ der die Nachricht empfängt, speichert seinen eigenen Zustand und sendet den Marker ebenfalls an alle Kanäle weiter.
6. Alle noch eingehenden Nachrichten werden als Zugehörig zum aktuellen Snapshot gespeichert.
7. Der Snapshot ist für einen Knoten vollständig, wenn auf jedem Kanal ein Marker empfangen wurde.

# Multicast Reihenfolgen
1. Unordered: Reihenfolge ist nicht definiert und kann zwischen Prozessen variieren.
2. FIFO: Nachrichten vom selben Absender kommen bei allen in der richtigen Reihenfolge an.
3. Causal Order: Eine Nachricht $B$ die von $A$ Abhängt wird in allen Prozessen nach $A$ empfangen.
4. Total Order: Alle Nachrichten sind überall in der selben Reihenfolge

## Sequentielle Konsistenz
Ein Datenspeicher ist sequentiell konsistent, wenn jede Programmausführung so erscheint, als ob:
- alle Lese- und Schreiboperationen aller Prozesse in einer beliebigen Reihenfolge ausgeführt werden.
- Die Operation eines Prozess hält die im Programm vorgegebene Reihenfolge ein.

## Linearisierbarkeit
Ist noch stärker als Sequentielle Konsistenz.
Vorrausgesetzt ist hierbei eine globale Uhrzeit die in allen Prozessen gelesen werden kann.
Die Reihenfolge der Operationen muss hier mit der Reihenfolge ihrer Zeitstempel konsistent sein.
Sehr schwer zu implementieren, oft nur für formale Verifikation von nebenläufigen Algorithmen verwendet.

## Kausale Konsistenz
Kausal abhängige Schreiboperationen müssen für alle Prozess in der selben Reihenfolge sichtbar sein.
Unabhängige Writes können in verschiedenen Reihenfolgen gelesen werden.

Notation: $W(x) a$ "Schreibe den Wert $a$ in Variable $x$"
Notation: $R(x) a$ "Lese Variable $x$, Ergebnis war $a$"

![](CausalConsistency.png)

Obwohl $c$ nach $b$ in $x$ geschrieben wurde, kann $P_3$ erst den Wert $c$ lesen. Lediglich das ursprüngliche $a$ darf nicht mehr sichtbar sein nachdem ein $b$ oder $c$ gelesen wurde.

Diese Kausale Inkonsistenz ist im zweiten Beispiel in $P_3$ zu sehen.

## Schwache Konsistenz
Zugriff auf geteilte Ressourcen wird über Synchronisationsvariablen koordiniert.

![](WeakConsistency.png)

Bei der Synchronisation $S$ werden vorherige Writes global sichtbar gemacht.

## Freigabekonsistenz
Eine Variante der schwachen Konsistenz mit Mutexen.

![](MutexConsistency.png)

Für kritische Blöcke kann nur ein Prozess arbeiten, so wird die Datensicherheit gewährt. Bei weniger sensiblen Operationen wie in $P_3$ kann auch ein alter Wert gelesen werden um die Geschwindigkeit zu erhöhen.

## Vergleich
![](ConsistencyComparison.png)

# Monotone Operationen
## Monotonic Reads
Ein Alter Wert wird niemals gelesen nachdem bereits ein neuerer gelesen wurde.

## Monotonic Writes
Eine Ältere Schreiboperation wird niemals sichtbar nachdem eine neuere stattgefunden hat.

# Grundbegriffe
- Failure|
  Beobachtetes Fehlverhalten, System reagiert nicht wie erwartet
- Error
  Inkorrekter interner Zustand (Nicht beobachtet)
- Fault
  Physikalischer Defekt, Periodisch oder Dauerhaft
- Fault Tolerance
  System fällt trotz Fault nicht aus.