# Halbaddierer
Diese Schaltung soll zwei Bits $A$ und $B$ addieren können. Ausgegeben werden ihre Summe $\Sigma$ und ihr Übertrag $C$.


| $B_0$ | $A_0$ | $\Sigma$ | $C_1$ |
| ----- | ----- | -------- | ----- |
| 0     | 0     | 0        | 0     |
| 0     | 1     | 1        | 0     |
| 1     | 0     | 1        | 0     |
| 1     | 1     | 0        | 1     |
$$
\begin{array}{ll}
\Sigma &= A \; XOR \; B \\
C &= A \wedge B
\end{array}
$$

# Volladdierer
Funktioniert wie ein [Halbaddierer](#Halbaddierer) der zusätzlich einen Übertrag der vorherigen Stelle auswerten kann.

| $C_n$ | $B_n$ | $A_n$ | $\Sigma_n$ | $C_{n+1}$ |
| ----- | ----- | ----- | ---------- | --------- |
| 0     | 0     | 0     | 0          | 0         |
| 0     | 0     | 1     | 1          | 0         |
| 0     | 1     | 0     | 1          | 0         |
| 0     | 1     | 1     | 0          | 1         |
| 1     | 0     | 0     | 1          | 0         |
| 1     | 0     | 1     | 0          | 1         |
| 1     | 1     | 0     | 0          | 1         |
| 1     | 1     | 1     | 1          | 1         |
$$
\begin{array}{ll}
\Sigma_n &= A\overline{B} \,\overline{C} \vee \overline{A}B\overline{C} \vee \overline{A} \, \overline{B} C \vee ABC \\
C &= A \wedge (B \vee C) \vee BC \\
\end{array}
$$
$C$ ist hier exakt die [2 aus 3 Schaltung](Boolsche%20Algebra.md#2%20aus%203%20Schaltung).

TODO