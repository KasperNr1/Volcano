# Funktionale Programmierung
- Keine Globalen Variablen, Effekt kann simuliert werden durch Mitschleifen in sämtlichen Funktionen (Stichwort Monaden)
- Jede Funktion hat einen Rückgabewert
- Lazy Evaluation (Deutsch: Verzögerte Ausgabe)
  Java Equivalent sind Streams
- Funktionen können Teil der Ein oder Ausgabe einer Funktion sein
## Funktion als Eingabe
Beispiel Vektorarithmetik
- Jedes Element wird auf die Funktion angewandt
  Also die beiden Ersten Element verknüpft bilden das erste Element des Ergebnis
- Java Äquivalent sind Interfaces
- Funktionale Interfaces sind durch Lambdas implementiert
- Rekursion durch Liste über Head - Tail Konstruktion

## Funktion als Ausgabe
Beispiel Addition einer Konstanten
- Rückgabe eines Lambda Ausdrucks
- In Java einigermaßen umständlich

# Haskell
Block-Konstrukt durch Einrückung in Zeichen. Einrücken der nächsten Zeile wird als Fortsetzung der vorherigen gewertet.

> [!Warning] Häufiger Fehler
> 4 Leerzeichen sind als lvl 4 eingerückt, ein gleich aussehender Tab wird als Stufe 1 gewertet

## Let-Where-Konstrukt
Beispiel Länge einer Liste.
Funktion braucht mangels globaler Variablen Parameter um das Ergebnis rekursiv zu übergeben. Let-in Konstrukt ermöglicht "Standartwerte" Für ersten Aufruf der Hilfsfunktion

Where Konstrukt erfüllt den selben Zweck

## ! Operator
Mit einem ! kann die Lazy-Evaluation (zum Debuggen) umgangen werden.
Der Ausdruck wird sofort berechnet.
Nützlich bei Erstellung einer Liste `[a, b, a+b]` in der Elemente aus anderen berechnet werden.

## Compiling
`ghc filename.hs`


# Currying
Jede Funktion von $n$ Argumenten kann als Kette von $n$ Funktionen abgebildet werden die jeweils 2 Argumente akzeptieren und das selbe Ergebnis berechnet.

Dieser Vorgang kann auch umgekehrt stattfinden, man spricht von Un-currying

Durch Klammern kann ein Infix-Operator zur gecurryten Präfix-Variante werden.
`(+) 1 2 = 1 + 2`