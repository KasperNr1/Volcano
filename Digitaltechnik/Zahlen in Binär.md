Zahlen können beliebig in verschiedenen Zahlensystemen dargestellt werden. Zur Umrechnung gibt es einen speziellen [Algorithmus](Umrechnung%20von%20Zahlensystemen.md)

# Integers
## Positive Ganzzahlen
Im Binärsystem werden die positiven Ganzzahlen simpel dargestellt. Jede Ziffer einer Binärzahl hat den Wert $0$ oder $1$.
Jede Stelle stellt eine andere Zweierpotenz dar, die Ziffer an dieser Stelle beschreibt jeweils wie oft diese Potenz addiert werden muss um die codierte Zahl zu berechnen.

Die Zahl $11_{10}$ wird in Binär dargestellt als $1011_2$

| $2^3 = 8$ | $2^2 = 4$ | $2^1 = 2$ | $2^0 = 1$ |
| --------- | --------- | --------- | --------- |
| 1         | 0         | 1         | 1         |
Da 
$$
11 = 1 * 2^3 + 0*2^2 + 1 * 2^1 + 1 * 2^0
$$

Nach dem selben Prinzip lässt sich jede beliebige Zahl als Basis eines Zahlensystems verwenden.


## Negative Zahlen
Binärzahlen sollen so codiert werden, dass kein zusätzliches Vorzeichen notwendig ist um negative Zahlen zu unterscheiden.
Es werden 3 intuitive Varianten verglichen um den heute geläufigen Standard herzuleiten.


| $D$ | $C$ | $B$ | $A$ | $Y_1$ | $Y_2$ | $Y_3$ |
| --- | --- | --- | --- | ----- | ----- | ----- |
| 0   | 0   | 0   | 0   | 0     | 0     | 0     |
| 0   | 0   | 0   | 1   | 1     | 1     | 1     |
| 0   | 0   | 1   | 0   | 2     | 2     | 2     |
| 0   | 0   | 1   | 1   | 3     | 3     | 3     |
| 0   | 1   | 0   | 0   | 4     | 4     | 4     |
| 0   | 1   | 0   | 1   | 5     | 5     | 5     |
| 0   | 1   | 1   | 0   | 6     | 6     | 6     |
| 0   | 1   | 1   | 1   | 7     | 7     | 7     |
| 1   | 0   | 0   | 0   | -0    | -7    | -8    |
| 1   | 0   | 0   | 1   | -1    | -6    | -7    |
| 1   | 0   | 1   | 0   | -2    | -5    | -6    |
| 1   | 0   | 1   | 1   | -3    | -4    | -5    |
| 1   | 1   | 0   | 0   | -4    | -3    | -4    |
| 1   | 1   | 0   | 1   | -5    | -2    | -3    |
| 1   | 1   | 1   | 0   | -6    | -1    | -2    |
| 1   | 1   | 1   | 1   | -7    | -0    | -1    |
| $D$ | $C$ | $B$ | $A$ | $Y_1$ | $Y_2$ | $Y_3$ |
Alle Codierungen verwenden das MSB als Vorzeichenbit. Dabei gilt $0=+$ und $1=-$ 

$Y_1$ Verwendet für alle Zahlen die selbe Codierung, so entsteht eine zweite $0$ und Schwierigkeiten bei Berechnungen mit den negativen Zahlen. Möchte man beispielsweise $1+(-2)$ berechnen erhält man folgende Lösung
$$
\begin{array}{rr}
1 & 0001 \\
-2 & 1010 \\
\\
& 0001 \\
+ & 1010 \\
\hline 
-3 & 1011
\end{array}
$$


$Y_2$ Ordnet die negativen Werte dem binären [1er-Komplement](DigitaltechnischeBegriffe.md#1er-Komplement) zu. 
So sind die Ergebnisse der Berechnungen nicht völlig falsch, jedoch bleiben sie um exakt 1 verschoben und belegen weiterhin eine Kombination mit $-0$.

$Y_3$ Löst beide dieser Probleme in dem die Idee beibehalten wird, aber die negativen Zahlen jeweils um $1$ vermindert werden. So wird gleichzeitig die Rechenverschiebung und die überflüssige $0$ verhindert.

Mit dieser Codierung kann eine $n$-stellige Binärzahlen Werte zwischen $\dfrac{2^n-1}{2}$ und $-\dfrac{2^n}{2}$ darstellen. MSB bleibt dabei das Vorzeichenbit mit $0=+$ 


# Floats
Kompromiss zwischen Größe des Exponenten (Range) und der Mantisse (Präzision). Over- und Underflow sind problematisch. (Exponent hat auch Vorzeichen)

```
package RandomJavaTesting;

public class Floats {
    public static void main(String[] args) {
        /*
        Floats sind bei großen Zahlen auch im Vorkomma-Bereich unpräzise.
        30 Mil + 1 ist auf +- 1 ungenau
        300 Mil auf +- 10
         */
        float a = java.lang.Float.NaN;
        float b = 20_000_001;
        System.out.println(a);
        System.out.println(b);


        for (int i = 0; i < 15; i++) {
            // Inkrement ist zu klein um gespeichert zu werden
            b = b+1;
            System.out.println(b);
        }
    }
}
```

## IEEE 754
Bei IEEE 754 wird zur besseren Sortierbarkeit der Exponent nicht im 2K dargestellt,  es wird um +127 verschoben (1023 bei 64 Bit)  
$$
Z_D=(-1)^S \cdot (1+\text{Mantisse}) \cdot 2^{\text{Exponent} - \text{Verschiebekonstante}}
$$
Ausnahmen (Seite 26 Foliensatz 3)
Exponent nur 1er -> Scam, NaN
