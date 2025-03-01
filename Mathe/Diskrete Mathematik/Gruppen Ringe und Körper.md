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
