# MIPS
(=Machine with no interlocked Pipe stages)
Klarere Befehlssatz
Weit verbreitet außerhalb von PCs (Drucker, Router, Handys)

RISC
Einfache Load/Store Architektur
Häufige einfache Instruktionen unterstützt (load, store, add, sub, move reg-reg, shift)
Festes Instruktionsformat
Homogener Registersatz (Alle Register (fast) gleich)

Adressen werden nie mit dem [2er Komplement](DigitaltechnischeBegriffe.md#2er%20Komplement) geschrieben
2K:
Positive Zahlen mit führenden 0er, negative mit führenden 1en
Beim Umwandeln einer 16 zu 32 Bit Zahl wird das Vorzeichen der kurzen Zahl auf alle führenden Stellen der Langen Zahl kopiert (Sehr simple schaltung, 1 Ausgabe mit 16 Eingaben Gabeln)

> [!Example] Klausuraufgabe
> - Binärzahlen als 2er Komplement schreiben
> - Sign Extension

## MIPS-Register


# Floats

> [!Example] Klausuraufgabe
> Kommazahlen zwischen Dezimal und Binär umrechnen
> Aussage zur Präzision einer Binär-Kommazahl (Periode -> Unpräzise)

Kompromiss zwischen Größe des Exponenten (Range) und der Mantisse (Präzision). Over- und Underflow sind problematisch. (Exponent hat auch Vorzeichen)

Bei IEEE 754 wird zur besseren Sortierbarkeit der Exponent nicht im 2K dargestellt,  es wird um +127 verschoben (1023 bei 64 Bit)

$$
Z_D=(-1)^S \cdot (1+\text{Mantisse}) \cdot 2^{\text{Exponent} - \text{Verschiebekonstante}}
$$

Ausnahmen (Seite 26 Foliensatz 3)
Exponent nur 1er -> Scam, NaN

## Umrechnung
Dezi -> Binär
Vor und Nachkomma separat berechnen

## Runden
Der Code berechnet den auf Integer gerundeten Durchschnitt aus $n$ Werten, die eine Summe von $\text{sum}$ haben 
```
sum = ((sum << 1)/n + 1) >> 1
```
Eine Nachkommastelle hinzufügen, 1 addieren und die zusätzliche Stelle wieder weg-shiften.
Ab $x.5$ soll aufgerundet werden, also wenn die erste Nachkommastelle der Binärzahl eine $1$ ist.


> [!Example] Klausuraufgabe
> Evtl.
> Runden in Assembler
