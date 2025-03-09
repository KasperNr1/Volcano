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