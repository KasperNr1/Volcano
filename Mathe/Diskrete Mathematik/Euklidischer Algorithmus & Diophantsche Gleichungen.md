Ziel: Verbessertes Verfahren zur Bestimmung des [Modulare Arithmetik](Modulare%20Arithmetik.md#Multiplikation) in $\mathbb{Z}_n$ 
(Besser = besser als probieren)
# Euklidischer Algorithmus
Verfahren zur Bestimmung des größten gemeinsamen Teilers (ggT)

Beispiel
$ggT(217; 63) \rightarrow 1; 2; 3; 4; 5; \ldots 63$ Ausprobieren sehr aufwändig

$\frac{217}{63} = 3 R 28 \rightarrow 217 = 3 * 63 + 28$ 

$ggT(217; 63) = ggT(63; 28)$ 

$\frac{63}{28} = 2R7$ 

$ggT(217; 63) = ggT(63; 28) = ggT(28; 7)$ 

$\frac{28}{7} = 4 \Rightarrow ggT = 7$ 
## Allgemein
$ggT(a; b)$ mit $a \geq b$ 
$r_0 = a \qquad r_1 = b \qquad r_k = r_{k-2} \mod r_{k-1}$
$q_k = r_{k-2} \, DIV \, r_{k-1}$ 
Also $r_{k-2} = q_k * r_{k-1} + r_k$ 

Die Rekursion bricht definitiv ab, da spätestens $1$ ein gemeinsamer Teiler ist.
$$r_{n+1}=0\rightarrow r_n = ggT$$ 

# Diophantische Gleichung
Ziel ist es, ganzzahlige Lösungen für Gleichungen der Form
$ax+by=ggT(a;b)$ 

## Anwendung
Eine Firma hat 10.000 Material und stellt Produkte her, die jeweils 75 bzw. 38 Material in der Produktion verbrauchen. Welche Verteilung verbraucht exakt 10.000 Material?

Gesucht sind Ganzzahlige Lösungen der Gleichung $75x + 38y = 10.000$ 

## Erweiterter Euklidische Algorithmus
$ax + by =ggT(a;b)$
In jedem Schritt werden Zahlen $x_k$ und $y_k$ berechnet, mit den Anfangswerten $x_0=1 \quad y_0=0 \quad x_1=0 \quad y_1=1$ 

$$
\begin{eqnarray}
r_k = r_{k-2}\bmod r_{k-1} \\
q_k = r_{k-2} \, DIV \, r_{k-1} \\
x_k = x_{k-2} - q_k * x_{k-1} \\
y_k = y_{k-2} - q_k * y_{k-1}
\end{eqnarray}
$$
Abbruch: $r_{n+1}=0$;
für $r_n = ggT(a;b)$ und das dazugehörige $x_n$ bzw. $y_n$ gilt dann:
$x_n * a + y_n * b = ggT(a;b)$
$x_n$ und $y_n$ als Lösungen der diophantischen Gleichung

### Einschränkungen
Die Gleichung $ax+by=c$ hat genau dann ganzzahlige Lösungen, wenn $c$ ein ganzzahliges Vielfaches des $ggT(a;b)$ ist.

Ebenfalls sind Vielfache der Gleichung durch entsprechende Vielfache der Lösung abgebildet.


# Multiplikatives Invers
Berechnung des multiplikativen Invers einer Zahl $e \mod m$ 
Wenn $e$ und $m$ teilerfremd sind, dann ist die Lösung der diophantischen Gleichung $e * x + m * y = 1$ das multiplikative Invers $\frac{1}{e}$ in $\mathbb{Z}_m$ 

Diese Inverse können mit dem hier beschriebenen [Euklidischen Algorithmus](Euklidischer%20Algorithmus%20&%20Diophantsche%20Gleichungen.md) bestimmt werden. [Videobeispiel](https://www.youtube.com/watch?v=l_eIF61uTN0)
Alternativ gibt es auch die [Iterative Methode](Modulare%20Arithmetik.md#Beispiel-Invers-Suche) bei der verschiedene Zahlen probiert werden.

## Indisches Verfahren
Hier wird in einem tabellarischem Verfahren der größte gemeinsame Teiler und das Multiplikatives Invers bestimmt. 

## Startwerte
$$
\begin{array}{c c l}
n &=& \text{Zahl 1} \\
a &=& \text{Zahl 2} \\
t_{1} &=& \text{Startet immer bei 0} \\
t_{2} &=& \text{Startet immer bei 1} \\
\end{array}
$$

Wenn das Invers $d$ einer Zahl $e$ Modulo $m$ bestimmt werden soll, wird zum Start $n=m$ und $a=e$ belegt. 
Der Algorithmus terminiert in dem Schritt, in dem $a=0$ belegt ist. Der Wert $t_1$ der entsprechenden Zeile ist das Multiplikative Invers $d$.

Jeder Schritt beginnt mit der Zuweisung der Werte $n,a,t_1,t_2$. Nach der initialen Belegung werden sie durch den rechts benachbarten Wert in der vorhergegangenen Zeile belegt.

$q$ und $r$ werden mit durch Division von $n$ durch $a$ mit Rest belegt. Dabei erhält $q$ den Wert des Divisors und $r$ den Wert des Restes

$$
\begin{array}{c|c|c|c|c|c|c}
q & n & a & r & t_{1} & t_{2} & t_{1}-t_{2} \cdot q \\\hline
1 & \boxed{60} & \boxed{47} & 13 & \boxed{0} & \boxed{1} & -1 \\
3 & 47 & 13 & 8 & 1 & -1 & 4 \\
1 & 13 & 8 & 5 & -1 & 4 & -5 \\
1 & 8 & 5 & 3 & 4 & -5 & 9 \\
1 & 5 & 3 & 2 & -5 & 9 & -14 \\
1 & 3 & 2 & 1 & 9 & -14 & 23 \\
2 & 2 & 1 & 0 & -14 & 23 & -60 \\
  & \boxed{1} & 0 &   & \boxed{23} & -60 &  \\
\end{array}
$$

Mit dieser Beispiel wurde also berechnet, dass 
$$
ggT(60; 47) = 1
$$
Und
$$
\frac{1}{47} = 23 \mod 60
$$

