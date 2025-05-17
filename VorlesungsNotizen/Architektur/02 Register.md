# Invers Polish Notation - StackArchitektur
Folge von Befehlen werden auf Stack gespeichert oder verrechnen die letzten $n$ Werte im Stack
$$
(3 + 4) * 5
$$
In klassischer Infix-Notation wird zu
$$
3; 4; +; 5; *
$$
So entfällt der Bedarf für Klammern

# Akkumulator Architektur
Ergebnis wird immer in Register gelagert,
Wie Taschenrechner -- Weitere Berechnungen mit vorher. Ergebnis möglich

# Registerarchitektur
Mehrere Universalregister,
x86

## Load-Store
Keine Speicher-oparanden (Nur über Load/Store)
Typische RISC Architektur
Mit Abstand das effizienteste Modell
Zwischenergebnisse können gespeichert werden

# ARM (Acorn Risc machines)

> [!Example] Klausuraufgabe
> Zahl als Fließkomma darstellen
> IEEE 754

# Vor/Nachteile Registertypen
Foliensatz 2 Seite ~17

# Speicher-Alignment
Ein Datum mit einer Größe von $S$ Bytes ist an der Adresse $A$ genau dann aligned, wenn 
$$
A = 0 \mod S
$$

Foliensatz 2 Seite 31
