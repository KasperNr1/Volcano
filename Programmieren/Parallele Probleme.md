# Race-Conditions
Treten bei gleichzeitiger Verwendung einer Ressource auf, Puffer von Dateien werden unkontrolliert aufgeteilt. 
Wenn mehrere Threads zeitgleich in eine Datei schreiben wollen, entsteht eine Durchmischung der beiden Ergebnisse.
Ebenfalls können "dirty-Reads" vorkommen, bei denen gelesen wird bevor das Ende einer Schreiboperation beendet ist.
Sie können durch den Einsatz passender [Kontrollstrukturen](Prozessverwaltung.md#Kontrollstrukturen) verhindert werden.
![](KnockKnockRaceCondition.webp)
# Sichtbarkeitsprobleme
RAM und Cache sind nicht unbedingt immer synchronisiert.
So kann also auch bei sequentiellem Zugriff auf Daten ein alter Wert erhalten werden, da das aktualisiert Ergebnis nur im Cache liegt. 

# Deadlocks
Ein Deadlock beschreibt eine Gruppe Threads, die alle auf eine Ressource warten, die ein jeweils anderer der Gruppe bereits für sich beansprucht hat. 
Sie können mit einem sog. "Wartet-Auf-Graph" erkannt werden:
![](WaitingForGraph.png)
Die Prozesse $i; j; k$ teilen sich die Objekte $x;y;z$.
Ein Pfeil $P_j \overset{y}{\rightarrow} P_k$ bedeutet hier, dass $P_j$ auf $y$ wartet, was aber bereits von $P_k$ verwendet werden könnte.
Ein Zyklus beliebiger Größe in einem solchen Diagramm zeigt die Möglichkeit eines Deadlocks auf.

