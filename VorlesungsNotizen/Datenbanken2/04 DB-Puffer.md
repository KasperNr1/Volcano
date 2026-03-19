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
unpin(P, set_dirty=false)
```

## Schreiben
```
pin(P)
	...
	'Read and write data on P'
	...
unpin(P, set_dirty=true)
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
Gemeint ist damit die Anzahl der Zugriffe auf eine Seite, die nicht im Puffe liegt.

## Tests
Es wird in einen Puffer der Größe 3 nacheinander eine Reihe an Zugriffen versucht.
```
A B C A B D A D B C B
```

### Optimaler Algorithmus
Der nicht-implementierbare Algorithmus $A_O$ liefert optimale Resultate. Er kann die Zukunft sehen und ersetzt immer den Eintrag, der am weitesten in der Zukunft erneut referenziert wird.

![](ReplacementOptimal.png)
- 5 Page Faults

Dieser Algorithmus ist zwar nicht praktisch umsetzbar, dient aber als Hilfe bei der Bewertung anderer Algorithmen.

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

Im Screenshot wurden die Pufferplätze so verschoben dass immer der oberste entfernt wird. Bei einer echten Implementierung ist dies hochgradig ineffizient.

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

![](LruKExample1.png)
Aufruf von $C$ in nächstem Schritt $16$ ist problemlos möglich. $16$ wird ebenfalls in die LU-Liste eingetragen.

---

Aufruf von $F$ in Schritt $16$ erfordert Ersatz von $A$, da $A$ mit Zugriff in Schritt $1$ am längsten im Puffer liegt.
Neuer Zustand:
![](LruKExample2.png)

---


> [!Missing] Fehlt
> Hier fehlt 3-36 bis 3-55
> Hab die Funktion $kB$ nicht verstanden

LRU-2 Ist praktisch optimal

# Suchen im Puffer

> [!Missing] Fehlt
> Hier fehlt 3-55 bis 3-59