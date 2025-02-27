# Definition
Eine Zahl $g$ ist dann [Grenzwert](Funktionen.md#Grenzwert) einer [Folge](Folgen.md), wenn zu jedem $\varepsilon > 0$ eine Zahl $n_0$ existiert, so dass $|a_n-g| < \varepsilon$ für jedes $n > n_0$.

Die Folge kann also einen beliebigen, stetig kleiner werdenden Abstand zu $g$ erreichen.

## Beispiel
$a_n = (-1)^n * \frac{1}{n} + 2; \quad \varepsilon = 0.15$

$$ 
\begin{matrix}
\left| \left( \left( -1 \right)^n * \frac{1}{n} + 2 \right) -2 \right| < 0.15 \\
\rightarrow n > 6 \frac{2}{3} = 6.\overline{6} \\
\rightarrow n_0 = 7
\end{matrix}
$$

## Sonderfall
$$a_n=1+(-1)^n + \frac{1}{n}$$
Diese Folge scheint 2 Grenzwerte zu besitzen, jedoch ist durch die $\varepsilon$-Definition dieser Fall nicht als Grenzwert kategorisiert. Stattdessen spricht man von 2 "Häufigkeitspunkten"
