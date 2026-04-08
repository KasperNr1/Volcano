Für größere Fehlertoleranz und Verfügbarkeit werden Daten oft repliziert. Dabei werden mehrere (Idealerweise) identische Kopien der Daten an verschiedenen Orten gespeichert. 
Mehrere Prozesse können parallel auf unterschiedliche Repliken zugreifen, somit wird eine höhere Performance möglich. Herausforderung ist dabei die Sicherstellung von Konsistenz.
Auch die Latenz kann verbessert werden, indem Anfragen an Kopien geleitet werden, die dem Client am nächsten sind.

# Konsistenz
Bei Änderungen müssen alle Repliken konsistent bleiben. Dies kann simpel durch [total geordnete atomare Multicasts](06%20Verteilte%20Mutexe.md#Multicast) erreicht werden. Dabei wird allerdings ein großer Teil der Performance geopfert.

Man wählt oft andere Konsistenzformen wie 'eventual Consistency'.

## Datenzentrische Konsistenzmodelle
Mehrere Clients greifen auf eine logische gemeinsame Datenbasis zu.
![](DatacentricConsistency.png)

Daten sind physisch verteilt und über mehrere Knoten repliziert. Dabei hat jeder Knoten eine lokale Kopie für Lese und Schreibzugriffe.
Trotz Verteilung und Replikation soll Konsistenz erreicht werden.


## Sequentielle Konsistenz
Ein Datenspeicher ist sequentiell konsistent, wenn jede Programmausführung so erscheint, als ob:
- alle Lese- und Schreiboperationen aller Prozesse in einer beliebigen Reihenfolge ausgeführt werden.
- Die Operation eines Prozess hält die im Programm vorgegebene Reihenfolge ein.

Alle Prozesse beobachten Schreibzugriffe in der selben Reihenfolge
![](SequentialConsistency.png)

Die Operationen aller Prozess werden zu einer globalen Reihenfolge zusammengeführt. Alle Prozess greifen auf einen logischen Speicher zu, auch wenn dieser physisch verteilt ist.

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


## Client-Zentrische Konsistenzmodelle
Hier liegt der Fokus darauf, jedem Client eine für ihn konsistente Sicht auf die Daten zu bieten.

Diese Art von Konsistenz bietet sich nur unter bestimmten Bedingungen an.
- Client-Unabhängigkeit
  Es gibt nur selten eine direkte Kommunikation zwischen zwei Clients
- Read-dominierte Workloads
  Schreibzugriffe erfolgen selten, die meisten Operationen sind nur lesend.

Szenarien sind beispielsweise
- DNS Caches
- Content-Delivery-Networks

### Eventual Consistency
Änderungen werden asynchron an Repliken verteilt. Das geschieht nicht direkt, sondern meist in Ruhephasen durch Hintergrundmechanismen.
Die Repliken konvergieren zu einem gemeinsamen Stand.

Wenn Clients dieselbe Replik für mehrere Arbeiten verwenden funktioniert dies gut. Beim Einsatz mehrerer Geräte oder mobilen Einsatz-szenarien können Probleme auftreten.

![](ClientCenteredConsistencyProblem.png)

### Monotonic Reads
Sind gegeben, wenn ein Lesen eines Wertes immer Werte liefert, die dem letzten Wert entsprechen oder neuer sind. 
Ein Prozess sieht nie alte Versionen nachdem er bereits eine neuere gesehen hat.
Der Client bewegt sich logisch nur vorwärts in der Zeit.


> [!Missing] Schreibweise
> Für das unten stehende Beispiel relevant.
> Beschrieben auf Seite 460


![](MonotonicReads.png)

### Monotonic Writes

> [!Missing] Fehlt
> Seite 463-465


# Verteilungsprotokolle
Wo wann und von wem werden Replikate erstellt?

Platzierung und Verteilungsstrategie beeinflussen Verfügbarkeit, Latenz, Bandbreite, Konsistenz und Kosten.
Trade-Off zwischen ressourcenintensiverer, proaktiver Replikation und reaktivem Kopieren. Hier entsteht potentiel eine größere Latenz.

## Server Initiierte Replikate
Permanente Replikate:
Fest vorgegebene Kopien auf Serverseite für hohe Verfügbarkeit und Lastverteilung.

Push Cache:
Server entscheidet proaktiv, wo/wann Replikate erstellt werden.

## Client initiiertes Caching
Clients speichern häufig genutzte Daten lokal, Ziel sind dabei schnellere Zugriffszeiten.
Haltedauer ist meist zeitlich begrenzt um veraltete Informationen nicht zu nutzen.

## Verteilungsmechanismen
Wann werden Updates übertragen?
- Push / Pull
- Transport per Unicast / Multicast
- Heartbeat-Nachrichten

Wenn ein Update verteilt wird, kann dies auf verschiedene Arten geschehen. Sie verwenden unterschiedlich viel Bandbreite und empfehlen sich abhängig vom Lese- zu Schreib Verhältnis.

- Neues Objekt wird vollständig übertragen
- Update Operation. Nur die Änderung wird gesendet.
- Invalidation. Es wird nur benachrichtigt, dass die Daten verändert sind. Beim nächsten Zugriff wird neu angefordert.

# Konsistenzprotokolle
Primary-Basierte Protokolle:
Schreiben findet nur auf einem bestimmten Replikat statt. Simpler zu koordinieren, aber single Point of Failure und gesteigerte Last.

Replicate Write Protokolle:
Writes werden an mehreren Replikaten ausgeführt.

## Primary-basiert
Reads sind auf allen Kopien möglich.
Writes müssen auf bestimmten Primaries geschehen.

Remote Write:
Der Schreiber leitet die Operation an einen festen Primary weiter. Dieser ändert sich nicht.

![](RemotePrimary.png)
1. Write Anfrage wird gestellt
2. Anfrage wird an Primary weitergeleitet
3. Schreiben wird ausgeführt
4. Neuer Zustand an andere Replikate übertragen
5. Bestätigung des neuen Zustands
6. Bestätigung des Schreibens an ursprünglichen Server
7. Bestätigung an Client


Local-Write:
Der Schreiber wird selbst primary, dann führt er das Update lokal aus.
![](RemoteWriteExample.png)
1. Schreibanfrage
2. Server macht sich selbst blockierend zum Primary
3. Erhält Primary Status
4. Schreibt Änderungen
5. Sendet neuen Stand an alle Kopien
6. Empfang wurde von allen Kopien bestätigt
7. Bestätigung an Client, Nächste Replikation darf nun Primary werden

# Replicated Write Protokolle

## Quorum basierte Protokolle
Bei $N$ Replikaten muss jede Schreiboperation von $N_W$ und jede Leseoperation von $N_R$ Knoten bestätigt werden. Dabei muss $N < N_W + N_R$ gelten, um stets eine Mehrheitliche Antwort zu gewährleisten. Bei jedem Schreiben wird eine Versionsnummer für den aktuellen Zustand vergeben, bei unterschiedlichen Antworten auf ein Lesen, wird der Wert mit der höchsten Versionsnummer verwendet.

Bessere Verfügbarkeit und Schreib-Skalierbarkeit auf Kosten einer komplexeren Quorum Wahl und Lese-Kosten.
 ![](QuorumBasedProtocoll.png)

