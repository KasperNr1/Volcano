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

### Fehlerkorrektur
Hamming-Codes.
TODO
