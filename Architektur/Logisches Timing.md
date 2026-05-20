# Koordination
In verteilten Systemen wird [Parallel](Paraprog-Basics.md#Parallel%20vs%20Nebenläufig) gearbeitet. Daher gibt es keine gemeinsame Uhr, was einige Schwierigkeiten bringt.

Es werden Logiken wie "[Vektor Uhren](05%20Logische%20Uhren.md#Vektor%20Uhren)" "[TimeStamps](05%20Logische%20Uhren.md#Lamport%20Timestamp)" oder [konsensbasierte Protokolle](05%20Logische%20Uhren.md#Konsensbasierte%20Ansätze) nötig.

Jeder Knoten besitzt eine lokale Uhr, Ereignisse können nur in Bezug auf eine solche Uhr eindeutig zugeordnet werden.

Aufgrund von unterschiedlichen Übertragungszeiten können Ereignisse in unterschiedlichen Reihenfolgen erscheinen, als sie tatsächlich geschehen sind.

![](ObserverOrder.png)

Besonders bei schreibenden Zugriffen kann dieser Umstand zu verschiedenen [Probleme](Parallele%20Probleme.md) führen.

Lösungen sind Logische Uhren. Sie erlauben Schlüsse über 
“[Happened-Before](#Happened-Before)". Also die Reihenfolge von Ereignissen, anstatt zwingend einer exakten Globalen Zeit.

## Zeitsynchronisation
### Cristians Algorithmus
Client notiert eigene Zeit und sendet Anfrage an vertrauenswürdigen Server. Nach Erhalt der Antwort berechnet der Client die gesamte Differenz zwischen Anfrage und Antwort und setzt seine Eigene Zeit $t$ auf den Wert der Antwort + die Hälfte der Round Trip Time der Anfrage.

![](CristiansAlgorithm.png)

Dieses Verfahren basiert auf 3 Annahmen.
- Der Server ist vertrauenswürdig
- Der Server braucht nahezu $0$ Zeit um die Anfrage zu beantworten
- Die im Netzwerk verbrachte Zeit sind auf Hin- und Rückweg gleich.

Typischerweise werden hier mehrere Anfragen gesendet um nicht auf einer einzelnen Antwort zu basieren.

### Zeitanpassung
Wenn die aktuelle Uhrzeit eines Systems angepasst werden muss, darf nicht direkt der neue, korrekte Wert eingetragen werden.
Stattdessen soll die Uhr vorübergehend schneller oder langsamer laufen, um zeitliche Monotonie zu gewährleisten.

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

Physikalische Uhren sind nicht exakt synchronisierbar. Daher sind sie nicht geeignet um die Reihenfolge von Ereignissen sicher zu bestimmen.
Mit logischen Uhren kann die Reihenfolge von Ereignissen mithilfe der [Happened-Before](04%20Prozessmanagement.md#Happened-Before) Kausalität bestimmt werden. Die realen Zeitpunkte der Ereignisse sind dabei nicht in fester Beziehung.

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
6. Alle noch eingehenden Nachrichten werden als Zugehörig zum aktuellen Snapshot gespeichert.
7. Der Snapshot ist für einen Knoten vollständig, wenn auf jedem Kanal ein Marker empfangen wurde.

![](StartStateConsistentCutExample.png)
In diesem Beispiel möchte Prozess $P1$ zum aktuellen Zeitpunkt einen Snapshot initiieren.

Die Sequenzdarstellung der Situation ist die folgende:
![](ConsistentCutExampleStartStateInSequenceForm.png)

Nach Ende des Algorithmus wurde folgender Schnitt gefunden:
![](ConsitentCutExampleEndState.png)

In dieser Darstellung sind die genauen Einträge im Speicher besser erkennbar
![](ConsistentCutExampleFinalState.png)
