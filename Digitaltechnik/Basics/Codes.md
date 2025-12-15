# Eigenschaften von Codes
## Bewertbarkeit
Jedem Bit ist eine Wertigkeit zugeordnet, so dass man den Informationsinhalt anhand eines Bits ansatzweise berechnen kann.

| Bewertbar                                        | Nicht Bewertbar                                                                                                |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------- |
| Dualcode, die $n$-te Stelle symbolisiert $2^n-1$ | [ASCII](https://de.wikipedia.org/wiki/American_Standard_Code_for_Information_Interchange)<br>EBCIDIC (Von IBM) |

## Mehrschrittigkeit
Nur anwendbar wenn der codierte Inhalt eine Reihenfolge besitzt.
Beschreibt die Eigenschaft des Codeworts für Element $n$ sich von dem für $n+1$ in exakt einem oder mehreren Bits zu unterscheiden, für alle Codewörter $n$

| Mehrschrittig                                                | Einschrittig                                         |
| ------------------------------------------------------------ | ---------------------------------------------------- |
| Dualcode, von $n=3 \rightarrow n=4$ ändern sich mehrere Bits | [Gray-Code](https://de.wikipedia.org/wiki/Gray-Code) |

## Fehlerumgang
Erkennen und Beheben von Fehlern ist durch geschickte Codierung zumindest teilweise möglich. Unbedingt notwendig sind hierfür Redundanzen, also ungenutzte Codewörter.

### Fehlererkennung
Durch Verwendung eines [Parity-Bits](DigitaltechnischeBegriffe.md#Parity) können Fehler erkannt werden, bei denen bis zu ein Bit getauscht wurde.

#### Zweidimensionale Parität
Die grauen Datenbits werden in einem Rechteck angeordnet und erhalten [Parity](DigitaltechnischeBegriffe.md#Parity)-Bits in jeder Zeile und Spalte (Rot).
All diese Kontrollbits werden von einem weiteren geprüft, das sich in der Ecke der Anordnung befindet.

![](2dParity.png)

Wenn sich nun 2 Werte ändern, kann das anhand der Prüfziffern erkannt werden.
![](2d2errors.png)

Zur Korrektur muss eindeutig erkennbar sein, wo der Fehler aufgetreten ist. Dann kann einfach das Betroffene Bit erneut getauscht werden. Mit diesem Schema kann ein beliebiger Fehler korrigiert werden. Bei zwei Fehlern können diese so liegen (Diagonal zu einander), dass sie nicht eindeutig identifiziert werden können. Es würden 4 Stellen in Frage kommen, von denen nur zwei tatsächlich getauscht werden müssten.

Ab vier Fehlern ist eine Konfiguration möglich, so dass diese nicht erkannt werden.
![](2d4errors.png)


### Fehlerkorrektur
Codes mit Fehlerkorrektur sind in der Lage, leicht beschädigte Daten selbst wiederherzustellen. Dafür sind sie mit besonders angeordneten Prüfziffern ausgestattet wie die berühmten **Hamming-Codes**

Hamming-Codes wie [Zweidimensionale Parität](#Zweidimensionale%20Parität) können Fehler erkennen und korrigieren.


> [!Error] Verwirrung
> [Das hier](#Zweidimensionale%20Parität) nicht Hamming codes? (Vgl. 3B1B und Algo/Datenstrukturen Vorlesung)
> Neske aus IT-Sicherheit führt sie separat von [seinen Hamming Codes](05%20Netzwerksicherheit.md#Hamming%20Codes) auf.
> Es gibt in seiner Vorlesung noch eine weitere Variante, die auch auf [Wikipedia gelistet](https://de.wikipedia.org/wiki/Hamming-Code) wird??

TODO
