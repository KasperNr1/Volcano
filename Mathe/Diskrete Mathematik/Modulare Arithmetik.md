# Grundbegriffe 
Zwei ganze Zahlen heißen "kongruent modulo $m$ ", wenn sie bei Division durch $m$ den gleichen Rest haben.

**Beispiel** 
$a = b \mod m$
$24 = 4 \mod10$ 

$\{19; 23; 27; 31; 35;...\}$ sind alle $\mod 4 =5$ 
Sie sind Teil einer __Restklasse__
Es gibt immer $m$ Restklassen bei Modulo $m$ 

## Satz-Mod-Regeln
Wenn $a=b \mod m$ und $c=d \mod m$ dann gilt:
- $a+c=b+d \mod m$
- $a * c=b * d \mod m$
Dabei ist nicht erforderlich, dass $a$ und $c$ der gleichen Restklasse angehören.
		
# Anwendungen
1. [Hash](Hashing.md)-Funktionen
2. Prüfziffern (ISBN, EAN, IBAN, $\dots$ )

# Addition und Multiplikation in $\Bbb{Z}_n$ 
## Definition
$$\Bbb{Z}_n = \{ 0;1;2;3;4;\dots;(n-1)\}$$
Ist die Menge aller möglichen Reste
$\Bbb{Z}_2 = \{0;1\}$ 

## Addition und Multiplikation in $\Bbb{Z}_5$ 
Damit die Ergebnisse auch innerhalb des erlaubten Zahlenbereichs sind, werden sie $\mod5$ genommen. Für $\Bbb{Z}_5$ entsteht so folgende Verteilung

| **+** | **0** | **1** | **2** | **3** | **4** |
| ----- | ----- | ----- | ----- | ----- | ----- |
| 0     | 0     | 1     | 2     | 3     | 4     |
| 1     | 1     | 2     | 3     | 4     | 0     |
| 2     | 2     | 3     | 4     | 0     | 1     |
| 3     | 3     | 4     | 0     | 1     | 2     |
| 4     | 4     | 0     | 1     | 2     | 3     |

| *   | **0** | **1** | **2** | **3** | **4** |
| --- | ----- | ----- | ----- | ----- | ----- |
| 0   | 0     | 0     | 0     | 0     | 0     |
| 1   | 0     | 1     | 2     | 3     | 4     |
| 2   | 0     | 2     | 4     | 1     | 3     |
| 3   | 0     | 3     | 1     | 4     | 2     |
| 4   | 0     | 4     | 3     | 2     | 1     |
### Addition
Man erkennt $4+1=0 \mod 5$ 
Daher betrachtet man $1$ als das Negative Element zu $4$.

#### Definition
Für eine Zahl $e \in \Bbb{Z}$ ist die Zahl $d$ das additive Invers zu $e$, wenn $e+d=0 \mod m$ und $d \in \Bbb{Z}_n$ 
Es gilt $d = n-e$ 
Es kann Zahlen geben die ihr eigenes  Invers sind.

### Multiplikation

> [!Tip]+ Rechenregeln ^Rules
> Im Taschenrechner lassen sich zu große Exponenten schlecht oder nicht berechnen. Die Werte können zerlegt werden
> $$
> 20^{69} = 20^{6*10+9} = \left(20^{10}\right)^{6}*20^{9}
> $$
> Es ist möglich, die Modulo Operation auch in diesen einzelnen Faktoren durchzuführen
> $$
> \left(20^{10}\right)^{6}*20^{9} = (31)^{6}*5 \mod 69
> $$
> Durch
> - $20^{10}  = 31 \mod 69$
> - $20^{9} = 5 \mod 69$ 
> 
> gilt also 
> $$
> 20^{69} = 31^{6}*5 = 65 \mod 69
> $$
#### Definition
Wenn es zu $e\in \Bbb{Z}_n$ eine Zahl $d$ gibt mit $d \in \Bbb{Z}_n$ und $d*e=1$ so heißt $d$ Kehrwert von $e$ oder auch multiplikatives Invers.
Man schreibt auch $d = e^{-1} = \dfrac1e$ 

In $\Bbb{Z}_5$ ist also mit $\dfrac12$ die Zahl $3$ gemeint.

Nicht jede Zahl hat ein Multiplikatives Invers:
$0 * d = 0 \neq 1$ 

#### Satz-Existenz
Für $e \neq 0 \in \Bbb{Z}_n$ hat $e$ genau dann einen Kehrwert, wenn $e$ und $n$ koprim, also teilerfremd sind.

#### Beispiel-Invers-Suche
$4^{-1} \in \Bbb{Z}_9$ "Erweitern" in gleicher Restklasse
$$
\frac{1}{4} \rightarrow \frac{1 + 9}{4} \rightarrow \frac{1 + 2 * 9}{4} \rightarrow \frac{1 + 3 * 9}{4} = 7
$$

## Gleichungen
### Addition
$$
\begin{array}{l}
4 + x = 3 & \mod 6 \\
x = -1 & \mod 6 \\
x = 5 & \mod 6
\end{array}
$$
### Multiplikation
$$
\begin{array}{l}
5 * x = 2 & \mod 12 \\
x = \frac{1}{5} * 2 & \mod 12 & \frac{1}{5} \rightarrow \frac{1 + 12}{5} \rightarrow \frac{1 + 2 * 12}{5} = \frac{25}{5} = 5 \\
x = 5 * 2 & \mod 12 \\
x = 10 & \mod 12
\end{array}
$$

---

$2*x=3 \mod 6 \rightarrow$ 2 und 6 sind nicht teilerfremd, probieren statt rechnen

| $2*0=0$ | ##  |
| ------- | --- |
| $2*1=2$ | ##  |
| $2*2=4$ | ##  |
| $2*3=0$ | ##  |
| $2*4=2$ | ##  |
| $2*5=4$ | ##  |
$\rightarrow$ Keine Lösung

---
$2*x=0 \mod 6$
vgl. oben, $\rightarrow 2$ Lösungen $(0|3)$

### Lösungsmengen
#### Addition
$$
a + x = b
$$
Besitzt immer eine eindeutige Lösung.
Addition des additiven Invers $-a$ von $a$ 

#### Multiplikation
Wenn $a$ und $m$ teilerfremd sind, besitzt $a*x=b \mod m$ genau eine Lösung in $\Bbb{Z}_m$.
Sonst existieren $0$ oder mehrere Lösungen.
Die Anzahl lässt sich mit Hilfe des größten gemeinsamen Teilers $t$ von $a$ und $m$ feststellen. Wenn $t$ auch Teiler von $b$ ist, so existieren genau $t$ Lösungen.
Sonst gibt es $0$ Lösungen.

$\Bbb{Z}_m^* = \{a \in \Bbb{Z}_m \mid ggT(a;m) =1 \}$  
Diese Menge ist also die Menge aller Zahlen aus $\Bbb{Z}_m$, für die ein multiplikatives Invers existiert. Alle diese Zahlen sind zu $m$ teilerfremd.
