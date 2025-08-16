Hier sind die Befehle des MIPS-Assembly gezeigt. MIPS steht für "Machine with no Interlocked Pipe stages" und ist ein verbreiteter Vertreter der [Load-Store-Architekur](Rechnerarchitekturen.md#Registerarchitektur%20Load-Store).
# MIPS Registerkonventionen
![](RegisterKonvention.png)

# Assembly-Befehle
![](AsmI.png)![](AsmII.png)![](AsmIII.png)

# Kommunikation mit OS
Jeder Prozessor und damit jeder Assembly Code arbeitet mit einem Betriebssystem. Nur dieses darf privilegierte Operationen durchführen. Um die Funktionen des Betriebssystems aufzurufen werden diese nummeriert. Die Nummer der gewünschten OS-Operation wird in `$v0` gespeichert und mit dem Aufruf von `syscall` angefragt. Das OS prüft ob der Prozess über die notwendigen Rechte verfügt und führt ggf. die Anfrage aus.

![](SpimSyscalls.png)