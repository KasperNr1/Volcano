# Hamming Codes
Vielleicht anders als die [Hamming Codes aus Digitaltechnik](Codes.md#Fehlerkorrektur), hier werden Datenwörter immer $4$ Bit Länge besitzen und mit $3$ Bit korrigiert.

$$
\begin{array}{c | c | c | c}
a_3 & a_2 & a_1 & a_0
\end{array}
$$
Über eine Generatorfunktion werden drei [Parity](DigitaltechnischeBegriffe.md#Parity)-Bits berechnet und dem Wort angehängt.

$$
\begin{array}{l}
r_0 = a_2 + a_1 + a_0 \mod 2 \\
r_1 = a_3 + a_2 + a_1 \mod 2 \\
r_2 = a_1 + a_0 + a_3 \mod 2
\end{array}
$$

Übertragen wird also
$$
\begin{array}{c | c | c | c | c | c | c}
a_3 & a_2 & a_1 & a_0 & r_2 & r_1 & r_0
\end{array}
$$

Durch die Fehleranfällige Übertragung werden möglicherweise andere Bits empfangen als versendet wurden. Es wird aus den Empfangenen Bits ein Syndrom berechnet, das in der Lage ist eventuelle Fehler zu korrigieren.
$$
\begin{array}{l}
s_0 = a_2 + a_1 + a_0 + r_0 \mod 2 \\
s_1 = a_3 + a_2 + a_1 + r_1 \mod 2 \\
s_2 = a_1 + a_0 + a_3 + r_2 \mod 2
\end{array}
$$

Anhand des Syndroms $s_2 s_1 s_0$ kann aus dieser Tabelle bestimmt werden, welches Bit falsch übertragen wurde. Bei schwerwiegenden Fehlern mit vielen falschen Bits ist dieses Verfahren nicht mehr anwendbar, es wird nur ein einzelner Fehler korrekt erkannt und korrigiert.

$$
\begin{array}{l | l| l| l| l| l| l| l| l}
\text{Syndrom} & 000 & 001 & 010 & 011 & 100 & 101 & 110 & 111 \\ \hline
\text{Fehler} & \text{None} & r_0 & r_1 & a_2 & r_2 & a_0 & a_3 & a_1 
\end{array}
$$
