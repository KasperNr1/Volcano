# Threads
Die JVM unterscheidet zwischen "Green Threads" und "Native Threads".
Dabei sind mit green Threads keine echten Threads angelegt, stattdessen wird das Verhalten nur von der JVM simuliert.
Da keine Kommunikation mit dem Betriebssystem stattfinden muss, sind sie schneller in der Erstellung. Außerdem sind diese Art von Threads durch die Portabilität der JVM auch auf Betriebssystemen möglich, die keine echten [Threads](Paraprog-Basics.md#Threads) unterstützen.

## Thread-Stopper
### Thread.interrupt()
Warteoperationen wie sleep() werden ignoriert und werfen eine Exception.
Das Programm innerhalb der Threads muss beendbar programmiert sein, also die Behandlung der InterruptedException entsprechend gestalten. Den Threads wird nur  ein Ende signalisiert, es gibt kein erzwungenes Abbrechen.

### Thread.stop()
Die Ausführung des Threads wird mit einer ThreadDeathException sofort beendet.
Diese Funktion sollte in der Regel nicht verwendet werden, da bei ihrem Aufruf nicht klar ist, an welcher Stelle abgebrochen wurde. Somit ist nicht erkennbar, welche Daten korrupt oder (un-)vollständig sind.

# Happens-Before-Semantik
![](Happens_Before.png)
Das Bild stellt drei Java-Threads symbolisch dar, die gemeinsam auf die beiden Werte $a$ und $b$ zugreifen. 
Die JVM ist in der Lage die Reihenfolge von Befehlen beliebig zu vertauschen, falls dies das Endergebnis nicht beeinflusst um Performancegewinne zu erzielen. Bei geteilten Ressourcen kann das zu unerwarteten Effekten führen.
Zu Beginn sind die Werte beide mit $0$ initialisiert. Thread 1 verändert sie und gibt die Summe aus, Thread 2 gibt sofort die Summe aus.
Die JVM kann die Zuweisungsreihenfolge vertauschen, also erst ``b = 10`` und dann ``a = 5`` berechnen. Falls zwischen diesen beiden Schritten der Zugriff von Thread 2 erfolgt, kann also als Summe der unmöglich erscheinende Wert $10$ ausgegeben werden.

# Synchronised
## Sync-Blöcke
```
synchronized(Object){
	doSmth();
	smth_else();
}
```
In einem synchronized-Block wird nicht unterbrochen. Ebenfalls kann nur ein Thread in einem Block ausführen. Ein Synchronisationsobjekt wird festgelegt, und dient als Markierung. Es funktioniert als "Rede-Ball". Nur der Thread der die Blockierung gerade hält darf arbeiten.
## Sync-Funktionen
Methoden können als synchronized deklariert werden.
```
public Class Demo{
	public synchronized someMethod(){
		\\ Implementation
	}
}
```
Dabei wird effektiv ein Synchronized [Block](#Sync-Blöcke) auf das aufrufende Objekt erzeugt.
Es kann also pro Instanz eines Objektes nur eine einzelne synchronized Methode gleichzeitig aufgerufen werden.

Der Effekt ist identisch mit folgendem Beispiel
```
public Class Demo{
	public someMethod(){
		synchronized(this){
			\\ Implementation
		}
	}
}
```

# Futures
Dienen als Speicher für Ergebnisse von Hintergrundprozessen.
Das Future-Objekt kann übergeben werden und besitzt eine `future.get()` Methode die auf den tatsächlichen Wert zugreift.
Berechnet wird dieser zu einem beliebigen Zeitpunkt ab der Instanziierung des Objekts, wenn der [Scheduler](Paraprog-Basics.md#Scheduler) ihm Rechenzeit zuweist.
Spätestens beim Aufruf von `get()` wird jedoch definitiv bestimmt.
