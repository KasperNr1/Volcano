# Motivation: Access Gap
Puffer werden benötigt da die Lesegeschwindigkeit unterschiedlicher Speichermedien drastisch variiert.

![](AccessGap.png)

Selbst schnelle SSDs brauchen $10^4$ CPU-Schritte um Daten zu laden.

Datenbank wird in "Frames" unterteilt.
Einige Frames können im Hauptspeicher gehalten werden um die Zugriffszeiten zu reduzieren.
Da der Puffer signifikant kleiner ist als die Datenbank selbst, müssen gepufferte Frames häufig ersetzt werden. Hier kann mit verschiedenen Ersetzungsstrategien gearbeitet werden.

![](PufferFrames.png)

Es werden einige Meta-Informationen  zu den Frames gespeichert
- `Id`: Nummer des Frames
- `pageID`: ID der Seite
- `pin_count`: Pinning-Zähler
- `dirty`: Flag, wird gesetzt falls geschrieben wurde
- `time_first_read`:  erster Zugriff
- `time_last_read`:  aktuellster Zugriff

# Pinning
Zählt wie viele Anwendungen die Seite im Gebrauch haben.


> [!NOTE] 5-Minuten Regel
> Alle Daten die mehr als ein Mal pro 5 Minuten verwendet werden, sollten im Puffer sein.
> 
> Heute weniger anwendbar aufgrund der Veränderung in Verwendungszwecken / Hardwarepreisen- und Kapazitäten. 
> Training von KI oder Analyse von großen Mengen sind heute häufiger als damals.


## Lesen
```
pin(P)
	...
	'Read Data on P'
	...
unpin(P)
```

## Schreiben
```
pin(P)
	...
	'Read and write data on P'
	...
unpin(P, dirty=true)
```

# Pufferallokation
Ideale Seitengröße hängt von Verwendungszwecken ab. 

Verwendung unterschiedlicher Seitengrößen ist möglich, bringt aber neue Probleme.

## Lokal
- Eigene Puffer für einzelne Transaktionen
- Keine Berücksichtigung konkurrierender Transaktionen
- Mechanismus zur Verwaltung gemeinsam genutzter Seiten nötig
- Dynamische Speicheranpassung pro Transaktion möglich

- Alle Transaktionen werden gleich behandelt
- Transaktionen können sich nicht gegenseitig verletzen 
- Mögliche schlechte Gesamtnutzung des Gesamtpuffers

## Global
Ein Pufferpool für alle Transaktionen.
Pufferframe wird für Seiten aller aktuell laufenden Transaktionen allokiert.

- Jeder Zugriff erfordert Einlagerung in Puffer
- (Fast) alle Seiten im Puffer werden ersetzt
- Andere Transaktionen müssen neu laden


## Ein Puffer
Fragmentierung, Speicherplatz wird insgesamt effizienter genutzt

## Mehrere Puffer
Schlechtere Speicherausnutzung, keine Fragmentierung


# Seitenersetzung
Wenn eine neue Seite geladen werden soll, der Puffer aber voll ist, muss eine Seite ersetzt werden.
Beim Ersetzen einer Seite muss diese auf die Platte zurückgeschrieben werden fall `dirty`gesetzt ist. Sonst kann der Speicher einfach überschrieben werden.

Kandidaten für Ersetzung könnten z.B. alle Seiten mit `pin_count = 0` sein. Es gibt jedoch diverse Algorithmen mit unterschiedlichen Komplexitäten.

## Bewertung
Allgemein werden Ersetzungsstrategien anhand der sog. Pagefaults bewertet.
Gemeint ist damit die Anzahl der Zugriffe auf eine Seite, die nicht im Puffer liegt.

## Tests
Es wird in einen Puffer der Größe 3 nacheinander eine Reihe an Zugriffen versucht.
```
A B C A B D A D B C B
```

### Optimaler Algorithmus
Der nicht-implementierbare Algorithmus $A_O$ liefert optimale Resultate. Er kann die Zukunft sehen und ersetzt immer den Eintrag, der am weitesten in der Zukunft erneut referenziert wird.

In diesem Beispiel bietet der Puffer Platz für drei Seiten. Er ist zu Beginn leer.
Aufgrund der [Geschwindigkeitsunterschiede](#Motivation%20Access%20Gap) wird jede Seite zur Bearbeitung immer erst in den Puffer verschoben.
![](ReplacementOptimal.png)
- 5 Page Faults

Dieser Algorithmus ist zwar nicht praktisch umsetzbar, dient aber als Hilfe bei der Bewertung anderer Algorithmen.
In diesem Beispiel werden also mindestens $5$ Anfragen nicht auf Seiten zugreifen, die bereits im Puffer sind. Das schlechteste mögliche Ergebnis, bei dem jeder Zugriff ein Page-Fault ist hat in diesem Fall in allen $11$ Zugriffen die falschen Werte im Puffer.

### FIFO
Ersetzt immer die am längsten im Puffer befindliche Seite

![](ReplacementFIFO.png)
- 7 Page Faults


> [!Info] FIFO-Anomalie
> Ein Vergrößern des Puffers kann zu einer Verschlechterung der Performance führen.
> 
> Auch als Belady's Anomalie bekannt
> 
> ```A B C D A B E A B C D E```
> - 9 Faults bei Puffergröße 3
> - 10 Faults bei Größe 4

### LIFO
Ersetzt immer die am kürzesten im Puffer befindliche Seite

![](ReplacementLIFO.png)
- 5 Page faults
- Für dieses Beispiel eine optimale Lösung

### LRU
Least Recently Used - Ersetzt die am längsten nicht referenzierte Seite.
![](ReplacementLRU.png)
- 5 Page Faults
- Ebenfalls optimal für dieses Beispiel

Im Screenshot wurden die Pufferplätze zur besseren Lesbarkeit so verschoben, dass immer der oberste Eintrag entfernt wird. Bei einer echten Implementierung ist dies hochgradig ineffizient.  

### NRU
Jede Seite hat ein `Referenced-Bit` und ein `Dirty-Bit`

Setzen bei Schreib- und Lesezugriff.
Lesezugriff wird in "gewissen" Zeitabständen zurückgesetzt.

Die Einträge lassen sich somit in vier Klassen einteilen
![](ReplacementNruClasses.png)

Ersetzt werden die Einträge mit der niedrigsten Klasse.


> [!Info] Annahme
> - Die `Reference_Bits` werden alle $2$ Zeitschritte zurückgesetzt. Das wird durch die blaue Senkrechte symbolisiert
> - Jeder Dritte Zugriff ist Schreibend (Kennzeichnung mit tiefergestelltem $_W$)

![](ReplacementNru.png)
- 6 Page Faults

Bei $t_6$ haben $B$ und  $C$ die Zustände $(1,0)\text{Klasse 3}$ und $(0,1)\text{Klasse 2}$. Ersetzt wurde in $t_7$ jedoch $B$, der Eintrag mit der höheren Klasse. Grund ist das Zurücksetzen des `Reference_Bits`. Nach dem Zurücksetzen wird $B$ zu einem Eintrag der Klasse 1, C bleibt unverändert in 2

### Clock-Algorithmus
Ringbuffer mit Referenzbits.

``` Python
Seite in Puffer:
	Seite.ref = true
	
Seite not in Puffer:
	while True:
		current = Puffer.nextpage() # Zyklisch da ein Ringbuffer verwendet wird
		if current.ref:
			current.ref = false
		else:
			current.replace
```


![](ReplacementClock.png)
- 5 Page Faults

### Counter-Based
Zähler für die Anzahl der Referenzierungen
#### LFU (Least Frequently used)
Problem: In der Vergangenheit häufig verwendete Seite bleibt ewig im Speicher
Abhilfe: Periodisches Herabsetzen der Zähler

#### MFU
Ersetzt Seite mit größtem Zähler

Schlecht wenn Seiten oft angefragt werden


### LRU-K
Wie [LRU](#LRU), berücksichtigt aber die letzten $k$ Zugriffe.

#### Naive LRU-K
In $LU$ ist eine Liste der letzten $k$ Zugriffszeitpunkte gespeichert.
$$
\text{LU} = (t_k, t_{k-1}, \dots, t_1)
$$
Ersetzt werden soll die Seite, mit der größten $kB$ ($k$-Backwards Distance).
Also die Seite deren ältester Zugriff am längsten vergangen ist.

![](LruKExample1a.png)
Aufruf von $C$ in nächstem Schritt $16$ ist problemlos möglich. $16$ wird ebenfalls in die LU-Liste eingetragen.
![](LruKExample1b.png)

---

Aufruf von $F$ in Schritt $16$ erfordert Ersatz von $A$, da $A$ mit Zugriff in Schritt $1$ am längsten im Puffer liegt.
Neuer Zustand:
![](LruKExample2.png)

Wenn in diesem Zustand im nächsten Zeitschritt $t_{17}$ eine neue Seite angefordert wird, so würde die eben eingelagerte Seite ersetzt werden, da ihr 'letzter Zugriff' mit $0$ initialisiert wurde.

---
Wenn eine eben ausgelagerte Seite wieder angefordert wird, muss entschieden werden wie ihre Historie initialisiert wird. Sie kann den Standardwert $0$ erhalten oder ihre alte Historie weiterverwenden.
Allgemein ist es sinnvoller die Historie wiederzuverwenden, dazu muss diese jedoch separat gespeichert sein um beim Auslagern nicht verloren zu gehen.

---
Ein weiterer Sonderfall ist die Behandlung von wiederholten Aufrufen der selben Seite. Da beide Aufrufe zur 'selben Operation' gehören, ist es sinnvoll den letzten Zugriff von der LU-Kette abzutrennen.

#### LRU-K Smart History
Somit hat die Kette folgende Struktur:
$$
\text{LU} = (\underbrace{t_k, t_{k-1}, \dots, t_1}_{\text{Historie}} \mid \underbrace{t}_\text{True last})
$$
In $t$ wird der wahre letzte Zugriff gespeichert. Ebenfalls wird eine `Correlated_Reference_Period` geführt. Der Wert beschreibt die Maximale zeitliche Distanz zwischen zwei Zugriffen auf die selbe Ressource, so dass diese noch als korreliert gelten.

Die Korrelationsperiode sei für die folgenden Beispiele $5$.
Wenn in diesem Zustand zum Zeitpunkt $t=18$ die Seite $C$ angefragt wird, ist sie noch im Puffer.
![](LruKExampleCase1.png)
Die Historie von $C$ wird angepasst.
$$
\text{LU}(C) = (5,9,18 \mid 18)
$$


Wird stattdessen zum Zeitpunkt $18$ die Seite $E$ angefragt, so muss nur der wahre letzte Zugriff aktualisiert werden, da er noch weniger als $5$ Zeitschritte vergangen ist.
$$
\text{LU}(E) = (6, 11, 15 \mid 18)
$$


Falls zum Zeitpunkt $18$ alternativ Seite $H$ angefragt wird, die nicht bereits im Puffer liegt, so wird $C$ ersetzt und die Historie von $H$ neu angelegt, da sie nicht bereits aus vorherigen Operationen bekannt ist.
$$
\text{LU}(H) = (0, 0, 18 \mid 18)
$$
Falls für $H$ bereits die Historie $LU(H) = (4, 7, 12)$ bekannt ist, würde sie wiederverwendet werden und der Eintrag mit der Aktualisierung abgespeichert werden.
$$
\text{LU}(H) = (7, 12, 18 \mid 18)
$$


> [!NOTE] Performance
> Größere Werte für $k$ erlauben das Speichern von längeren historischen Zusammenhängen, verwenden aber auch mehr Speicherplatz.
> Untersuchungen haben gezeigt dass bereits ein Wert von $k=2$ nahezu ideale Werte liefert. 
> Mit größeren Werten können die Ergebnisse nur marginal verbessert werden.


# Suchen im Puffer
Unsortierte Tabellen können nur sequentiell durchsucht werden, bei vorhandener Sortierung kann mit [Binary Search](Suchalgorithmen.md#Binary%20Search) gearbeitet werden.

Es können auch Verkettungsbasierte Strategien oder [Hashing](Hashing.md) verwendet werden.
![](SearchingInDbBuffer.png)

In der Realität werden meist Hash-basierte Techniken verwendet die eventuelle Überläufer verketten.
![](SearchingInDbBuffer2.png)

> [!Missing] Fehlt
> Hier fehlt 3-55 bis 3-59