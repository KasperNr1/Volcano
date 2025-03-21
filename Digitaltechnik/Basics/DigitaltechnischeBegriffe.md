# Disjunktiv
Zwei Variablen heißen disjunktiv verknüpft, wenn sie mit einem [ODER](Boolsche%20Algebra.md#OR) verbunden sind.
Bei Längeren Ketten wie 
$$
A \vee B \vee C \vee D \vee E \vee \dots
$$
werden die einzelnen Variablen als Disjunkte bezeichnet.

# Konjunktiv
Analog zu [Disjunktiv](#Disjunktiv).
Konjunkte sind Variablen die mit einem [UND](Boolsche%20Algebra.md#AND) verknüpft sind. Dies gilt auch bei längeren Ketten
$$
A \wedge B \wedge C \wedge D \wedge E \wedge \dots
$$
# Normalform
Zu jeder Belegungstabelle existieren exakt eine [Konjunktive](#Konjunktiv) und eine [Disjunktive](#Disjunktiv) Normalform (KNF bzw. DNF)
Gemeint ist damit die Form der die Tabelle beschreibenden Schaltung die jede Belegung der Ausgabe in einem Zustand explizit enthält.

Dabei werden für die KNF alle Terme mit dem Ergebnis 0 gesammelt.
Die einzelnen Literale einer Belegung werden disjunktiv Verknüpft, und die Menge an Kombinationen untereinander konjunktiv.
So erhält man eine große Konjunktion, wobei jeder einzelne Term leicht zu erfüllen ist, da ein einzelnes Literal den Term bereits gültig machen kann.

Die DNF funktioniert exakt umgekehrt, alle Terme die zu einer 1 führen, werden konjunktiv vereint und als ganzes disjunktiv verknüpft.
Man erhält einen langen Term aus schwer erfüllbaren Konditionen, wobei ein einzelner ausreicht um den gesamten Term positiv auszuwerten.

Die Belegung der KNF wird als Wahr ausgewertet, wenn das Ergebnis in der Tabelle eine 0 ist.
Also sind die so entstehenden Terme exakte Gegenteile. Um Äquivalenz zu erreichen muss einer der beiden negiert werden.

## Beispiel

| A   | B   | C   | Y   |
| --- | --- | --- | --- |
| 0   | 0   | 0   | 0   |
| 0   | 0   | 1   | 0   |
| 0   | 1   | 0   | 1   |
| 0   | 1   | 1   | 1   |
| 1   | 0   | 0   | 1   |
| 1   | 0   | 1   | 0   |
| 1   | 1   | 0   | 1   |
| 1   | 1   | 1   | 0   |
Für diese Tabelle lautet die DNF:
$$
(\overline{A}B\overline{C}) \vee (\overline{A}BC) \vee (A\overline{B} \, \overline{C}) \vee (AB\overline{C})
$$
KNF:
$$
(A \vee B \vee C) \wedge (A \vee B \vee \overline{C}) \wedge (\overline{A} \vee B \vee C) \wedge (\overline{A} \vee \overline{B} \vee C)
$$

# Komplement
Beschreibt das fehlende hin zu einem Ganzen, z.B. Komplementärfarben.

## 1er-Komplement
Ist eine arithmetische Operation bei der die Bits / Ziffern einer Zahl umgekehrt werden.
Die Umkehrung einer Ziffer $Z$ die Ziffer $z$, bei der gilt $Z + z =b-1$.
Dabei ist $b$ die Basis des [Zahlensystems](Umrechnung%20von%20Zahlensystemen.md#Zahlensysteme).
Vergleichbar ist die Operation mit dem [additiven Invers](Modulare%20Arithmetik.md#Addition) in $\Bbb{Z}_n$

Für $110001_2$ ist das 1er-Komplement also $001110_2$ oder $1110_2$
Bei $123890_{10}$ ist es $876109_{10}$ da die beiden Zahlen jeweils $111111_2$ oder $999999_{10}$ als Summ haben.

## 2er Komplement
TODO

# Parity
