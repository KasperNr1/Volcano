# Verteilte Mutexe
Soll exklusive Ressourcen konfliktfrei nutzen können.
Latenz, fehlende gemeinsame Uhr und Netzwerkausfälle sind dabei Probleme die Liveness und Fairness erschweren.

> [!NOTE] Begriffe
> Liveness:
> Die Eigenschaft, dass eingehende Anfragen auch erhalten werden.
> 
> Fairness:
> Anfragen werden fair behandelt

Lösungsansätze sind
- Zentralisierte Server
- Verteilte Algorithmen
- Token-Ring

## Zentraler Server
Ein Koordinator verwaltet die Ressource und eine Warteschlange. Dieser wird z.B. per [Wahlalgorithmus](05%20Logische%20Uhren.md#Wahlalgorithmen) bestimmt.
Dieser bestimmt die Vergabe und Reihenfolge des Zugriffs auf die Ressource.

1. Prozess $P$ sendet Request
2. Antwort des Koordinators
	- Ressource frei
	  `ok` Nachricht, $P$ erhält Zugriff
	- Ressource verwendet
	  $P$ wird in die Warteschlange aufgenommen
3. Prozess ist fertig
   Sendet `release` Signal an Koordinator
4. Koordinator sendet `ok` an nächsten Prozess.

Da der Ausfall des Koordinators das System lähmt, ist es sinnvoll mit negativen Bestätigungen zu arbeiten, statt zu schweigen.
Auch Mechanismen wie Heartbeats sind sinnvoll, es sollte per Wahl ein neuer Koordinator bestimmt werden können.

## Verteilter Algorithmus
Ein anfordernder Prozess schickt eine Anfrage an alle anderen und darf erst in den kritischen Abschnitt, wenn er von allen anderen ein `ok` bekommt.

Anfragen werden mit einem Zeitstempel versehen, ein Prozess der die Ressource nicht möchte sendet `ok`, einer der sie möchte vergleicht die Zeitstempel der eingehenden und seiner eigenen Anfrage und sendet ggf. `ok`.
Andernfalls wird die eingehende Anfrage in die lokale Queue aufgenommen.

Nach Ende des eigenen Zugriffs auf die Ressource sendet der Knoten an alle Prozesse in der lokalen Queue.

![](DistributetMutexAlgorithm.png)

$P_1$ und $P_3$ senden ihre Anfragen zu den Zeiten $(8,1)$ und $(12,3)$

![](DistributetMutexAlgorithmSteps.png)

## Token-Ring-Algorithmus
Prozesse bilden einen logischen Ring, ein Token zirkuliert im Ring und autorisiert den Ressourcenzugriff.

Beim Erhalt des Tokens prüft ein Prozess ob er die Ressource braucht. 
- Ja: Nutzen
- Nein: Token weitergeben

Sehr simples Verfahren, jedoch eventuell problematisch mit Verzögerungen bei langen Ketten.
Der Ausfall eines Knoten mit Token muss erkannt werden um ein neues Token einzuführen.

---

![](DistributedMutexCompare.png)


# Multicast
Wie kann man den Empfang von Nachrichten in der korrekten Reihenfolge erreichen?
Wie kann man den Erhalt bei allen Empfängern zu sichern?

- Unreliable Multicast
  Pakete können verloren gehen, keine Garantie oder automatische Wiederholung.
- Reliable Multicast
  Zustellung an alle (Außer Netzausfall)
  Realisiert durch `ACK` und `NACK` + automatische Wiederholung. Erhöht Traffic und Latenz
- Atomic Multicast
  Starke Garantie: Nachrichten werden entweder von allen Empfängern oder keinem erhalten. Zusätzlicher Aufwand für synchrone Zustände.

Trade-Off zwischen Empfangsgarantie und Koordinationsaufwand.

## Empfangsreihenfolge
Unordered:
Empfangsreihenfolge ist undefiniert und kann zwischen Prozessen variieren.
![](UnorderedCommunication.png)

FIFO order:
Nachrichten vom selben sender werden bei allen Prozessen in der selben Reihenfolge empfangen
![](FifoOrderCommunication.png)

Causal Order:
Falls eine Nachricht $m'$ kausal von $m$ abhängt $(m \to m')$ erhalten alle Prozesse $m$ vor $m'$ 
![](CausalOrderCommunication.png)

Total Order:
Alle Nachrichten werden bei allen Prozessen in exakt der selben Reihenfolge empfangen
![](TotalOrderCommunication.png)


> [!NOTE] Woher totale Ordnung?
> Um global eindeutige Sequenznummern zu erhalten, muss ein erheblicher Aufwand betrieben werden.
> Hier kann wie bei [Verteilte Mutexen](#Verteilte%20Mutexe) auf zentrale Vergabe oder verteilte Algorithmen gesetzt werden.

# Tansaktionen in verteilten Systemen
Werden nicht nur in Datenbanken eingesetzt, auch bei verteilten Diensten wie Reservierungs- und Koordinationsprotokollen.
Wie können die [ACID](Transaktionen.md#ACID) Prinzipien eingehalten werden?

Besonders die Isolation ist problematisch, da eine vollständige Isolation zu restriktiv ist und Risiken für Deadlocks steigert und die Performance drastisch reduziert.
Es werden verschiedene [Isolationslevel](05%20Transaktionssteuerung.md#Isolationslevel) verwendet.

## Verschachtelte Transaktionen
In einer Transaktion können beliebig viele Subtransaktionen durchgeführt werden.
Ein Commit einer "äußeren" Transaktion macht die Inhalte der inneren dauerhaft.
Ein Fehler der Sub-Transaktion kann erneut versucht werden, die Parent-Transaktion kann weiterlaufen.

Ein Fehler der Parent-Transaktion führt zum Abbruch aller Subtransaktionen.

Beispiel wäre die Buchung eines Urlaubs mit Flug und Hotel. Das gesamte Buchen ist eine Aktion, Flug und Hotel selbst sind aber auch komplex. Falls das Hotel scheitert, kann der gebuchte Flug beibehalten werden um Arbeit zu sparen.

![](NestedTransactionExample.png)


## Verteilte Transaktion
In verteilten Datenbanksystemen sind verteilte Transaktionen notwendig.
Mehrere Ressourcen sollen atomar verwaltet werden.

Es gibt ein verbreitetes System mit verschiedenen Rollen. Ressourcenmanager und Koordinator.

1. Applikation startet Transaktion
2. Transaction Manager (TM) koordiniert Lebenszyklus und Abstimmungsprotokolle
3. Ressource Manager (RM) führt lokale Transaktion aus. Zuständer werden geloggt und mit dem TM kommuniziert.
4. TM prüft kompatibilität der Transaktion mit den Zuständen aller RMs und ruft zum globalen Commit oder zum Abort auf.

![](TwoPhaseCommit.png)


> [!Info] Zwei Phasen
> Phase 1: Prepare
> Der TM fragt alle RMs nach Commit-Wille ab.
> Sie stimmen für `commit` oder `abort`.
> Nur falls kein Problem erkannt wird, fahren alle RMs in Phase 2 mit dem Commit fort.
> 
> Phase 2: Finalisation
> TM sendet commit, alle speichern ihn ab.
> TM sendet abort, RMs rollen lokal zurück und bestätigen.

