Physikalische Uhren sind nicht exakt synchronisierbar. Daher sind sie nicht geeignet um die Reihenfolge von Ereignissen sicher zu bestimmen.

# Lamport Timestamp
Jeder Prozess $i$ hat einen Lamport-Timestamp $L_i$ .
Die kausale Reihenfolge wird respektiert.
$$
a \to b \Rightarrow L(a) < L(b)
$$
Dies ist nicht zwingend invertierbar.
Aus $L(a) < L(b)$ kann nicht $a \to b$ geschlossen werden.

Für lokale Ereignisse wird der eigene Zeitstempel inkrementiert.
Beim Senden von Nachrichten wird der Lokale Zeitstempel mitgesendet.
Beim Empfangen einer Nachricht mit Zeitstempel $t$ wird der lokale Zeitstempel auf $\max(L_i; t) + 1$ gesetzt. Dabei ist $L_i$ der vorherige lokale Zähler des Empfängers.

![](LamportTimestamps.png)

# Vektor Uhren
Ziel ist ein Zeitstempel für den gilt:
$$
a \to b \Leftrightarrow V(a) < V(b)
$$
In einem System mit $N$ Prozessen ist eine Vektoruhr ein Vektor mit $N$ ganzen Zahlen.

Jeder Prozess $i$ besitzt einen eigenen Vektor $V_i$.

$V_i[i]$ ist die Anzahl der bisher im Prozess $i$ aufgetretenen Ereignisse.

Für ein lokales Ereignis gilt in Prozess $i$:
$$
V_i[i] \leftarrow V_i[i] + 1
$$

Beim Senden einer Nachricht wird der gesamte Vektor mitgesendet.

Beim Empfangen einer Nachricht wird für jedes Element des eigenen und des Empfangen Vektors der größere Wert gewählt.
$$
V_i[j] \leftarrow \max(V_i[j], t[j])
$$
Zusätzlich wird der Wert für den eigenen Prozess inkrementiert.

![](VectorClocks.png)

Ein Ereignis $A$ ist vor einem Ereignis $B$ geschehen, wenn für jedes Element $i$ der Vektoren gilt:
$$
V_A[i] \leq V_B[i]
$$

# Globaler Zustand
Wann kann die Anwendung terminieren?
Auch wenn kein Prozess arbeitet können noch Nachrichten unterwegs sein.

Die Fragestellung ist anwendbar für verteilte Garbage-Collection, verteilte Deadlock-Erkennung, System-Recovery usw.

Für den Garbage-Collector ist ein Objekt Garbage, wenn es in keinem Prozess und in keiner Nachricht referenziert wird.
Für den Globalen Zustand ist es also nötig die lokalen Zustände und die Kanalzustände zu kennen.

Zur Fehlerdiagnose kann es hilfreich sein, einen globalen Snapshot zu erstellen. Auch für Recovery bei Fehlern wird ein sicherer Gesamtzustand gebraucht.

Naive Idee ist die Vereinigung aller Prozesszustände. Dabei werden die Messages "in Transit" nicht beachtet. Außerdem gibt es keinen eindeutigen globalen Zeitpunkt $t$

## Konsistente Schnitte
Prozesszustände beziehen sich immer auf lokale (unterschiedliche) Zeiten.
Zur Bestimmung eines wohldefinierten Zustands nutzt man "Consistent Cuts".
Bedingung ist dabei: Ist das Empfangen einer Nachricht im Schnitt enthalten, so muss auch das Senden der Nachricht enthalten sein. 

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

Beispiel auf Seite 333 und vorherige

# Wahlalgorithmen
Verteilte Algorithmen benötigen einen Koordinator oder Leader, der spezielle Aufgaben übernimmt.
Ziel der Wahlalgorithmen ist es einen solchen Leader zu bestimmen.

Annahmen:
- Jeder Prozess im System hat eine eindeutige ID
- Jeder Prozess kennt die IDs aller anderen Prozesse
- Üblich wird ein Prozess nach willkürlichem Kriterium als Koordinator gewählt (Höchste / Geringste ID o.ä.)

Algorithmus muss schnell ein Ergebnis liefern das allen Teilnehmern der Wahl bekannt ist, wobei er robust gegen Ausfälle während der Wahl sein muss.

Verschiedene Wahlverfahren sind
- [Heartbeat](#Heartbeat)
- [Ringalgorithmen](#Ringalgorithmen)
- [Heartbeat](#Heartbeat)
- [Konsensbasierte Anätze](#Konsensbasierte%20Anätze)


## Bully Algorithmus
Wenn die Koordinatorlosigkeit festgestellt ist, wird ein Wahlprozess gestartet. Dabei wird der Prozess zum Koordinator, der während der Wahl die höchste ID hat.

Ein Prozess startet den Wahlprozess und fragt alle anderen Prozesse mit höherer ID ob sie Koordinator sein wollen.
Falls er nach einer gewissen Zeit keine Antwort erhält, ernennt sich der Prozess selbst zum Koordinator.

Fall ein Prozess antwortet beendet der Initiator seine Wahl, der antwortende höhere Prozess startet seinerseits eine Wahl.

![](BullyCoordinatorExample.png)

## Ringalgorithmen
Annahme ist, dass jeder Prozess in einem logischen Ring angeordnet ist und seine Nachbarn kennt.


> [!NOTE] Sichtbarkeit
> Alle Knoten kennen alle anderen Knoten, so kann auch bei fehlenden Antworten auf den nächsten Prozess weitergeleitet.
> Die Beschränkung auf Kommunikation mit dem Nachbarn kommt nur aus dem Algorithmus


Wahl läuft ab, indem eine Nachricht mit eigener Prozess ID an Nachbar geschickt wird. Wenn der Nachbar aktiv ist, fügt er seine eigene ID zur Nachricht hinzu und leitet sie weiter an seinen Nachfolger. Wenn ein Knoten nicht antwortet, wird die Nachricht unverändert an den nächsten Knoten weitergeleitet.

Sobald die Nachricht beim Absender ankommt, enthält sie eine Liste aller aktiven Prozesse. Der Prozess mit höchster ID wird als Koordinator bestimmt, diese Nachricht wird entsprechend an die Nachfolger übermittelt.

## Heartbeat

## Konsensbasierte Ansätze