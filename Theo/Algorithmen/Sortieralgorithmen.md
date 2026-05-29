Sortierte Mengen können mit [Suchalgorithmen](Suchalgorithmen.md) sehr schnell und effizient durchsucht werden. 

Verschiedene Sortierverfahren haben unterschiedliche Eigenschaften. Relevant sind neben der Geschwindigkeit beispielsweise die Fähigkeit von Vorsortierung zu profitieren oder das Beibehalten relativer Positionen wenn nacheinander anhand unterschiedlicher Kriterien sortiert wird.

# Simple Algorithmen

## Bubble-Sort
Es wird mit quadratischer Laufzeit über alle Elemente iteriert. Dabei wird jeder Wert mit seinem direkten Nachbar verglichen. Falls das Wertepaar nicht korrekt sortiert ist, wird es getauscht.


## Insertion-Sort

## Selection-Sort

# Schnelle Algorithmen 

## Comb-Sort

## Shell-Sort

## Merge-Sort

## Quick-Sort

# Sortierung großer Datenmengen
Die bisher beschriebenen Algorithmen basieren auf der Annahme, dass die zu sortierenden Daten alle im Hauptspeicher liegen.
Aufgrund des [Access Gap](04%20DB-Puffer.md#Motivation%20Access%20Gap) beim Zugriff auf sekundäre Speichermedien muss für größere Datenmengen anders gearbeitet werden.
## Externes Sort-Merge
Sei $M$ die Speichergröße in Seiten.
### Phase 1: Sortierte Läufe
- $i= 0$
1. Lese $M$ Blöcke der Daten in den Hauptspeicher
2. Sortiere diese Daten mit internen Sortierverfahren wie [Quick-Sort](#Quick-Sort)
3. Speichere Ergebnis als sortierten Lauf $R_i$ auf Platte
4. Inkrementiere $i$
5. Wiederhole Ab Schritt 1.
- $N=i$

### Phase 2: N-Wege-Mischen
#### 1. Fall: N < M
Falls $N<M$ gilt, kann in $N$ Blöcken jeweils der erste Block aus den Zwischenergebnissen von [Phase 1](#Phase%201%20Sortierte%20Läufe) gespeichert werden. Ein weiterer Block dient als Puffer für die endgültige Ausgabe.

Der jeweils kleinste/größte Eintrag aus den Eingabeblöcken wird an die Ausgabe angehängt, bis der Puffer leer ist. 
Nachdem keine neuen Läufe mehr nachgeladen werden können, ist der Datensatz sortiert.

#### 2. Fall: N $\geq$ M
In diesem Fall sind mehrere Mischphasen notwendig.
Es werden in jeder Phase $M-1$ benachbarte Gruppen gemischt. So reduziert sich die Anzahl der Läufe um den Faktor $M-1$ und erzeug Läufe die maximal um diesen Faktor angewachsen sind.

Das Verfahren lässt sich wiederholen bis die Zahl der Läufe gering genug ist um wie in [Fall 1](#1.%20Fall%20N%20<%20M) behandelt zu werden.

![](ExternalSortMerge.png)


















