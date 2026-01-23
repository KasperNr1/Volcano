Intelligentes Verhalten kann in einer Gruppe auch dann entstehen, wenn diese nach nur simplen Regeln agiert.

# Partikelschwarmoptimierung
Ist ein **heuristischer** Algorithmus zur Suche nach Lösungen in vieldimensionalen, komplexen Lösungsräumen und ist nicht rein mathematisch fundiert.
Daher kann er auch eingesetzt werden, wenn die Funktion nicht exakt mathematisch definiert werden kann oder ungünstige Eigenschaften besitzt (also z.B. nicht [stetig](Funktionen.md#Stetig) oder [differenzierbar](Differentialrechnung.md#Ableitung) ist)

## Ablauf
Jeder Partikel ([Agent](09%20Reinforcement%20Learning.md#Software%20Agenten)) verfügt über eine eigene Position und Geschwindigkeit. Diese Werte werden iterativ auf Basis der eigenen Erfahrung und der der Gruppe angepasst.

Die Partikel werden zufällig verteilt und aktualisieren ihre Attribute nach folgendem Schema:
$$
v_i(t+1) = \omega \cdot v_i(t) + c_1 \cdot r_1 \cdot \left(p_{\text{best}, i} - x_i(t)\right) + c_2 \cdot r_2 \cdot \left(g_{\text{best}} - x_i(t)\right)
$$
$$
x_i(t+1) = x_i(t) + v_i(t+1)
$$
Dabei sind:
- $v_i(t)$ die Geschwindigkeit eines Partikels zum Zeitpunkt $t$
- $x_i(t)$ die Position eines Partikels zum Zeitpunkt $t$
- $\omega$ eine Trägheitskonstante die den Einfluss der aktuellen Geschwindigkeit steuert
- $c_1, c_2$ Beschleunigungskoeffizienten für eigene und soziale Komponente
- $r_1, r_2$ Zufallszahlen aus dem [Intervall](Intervalle%20und%20Mengen.md#Intervalle) $[0, 1]$ 
- $p_{\text{best}, i}$ die beste gefundene Position von Partikel $i$
- $g_{\text{best}}$ die beste gefundene Position aller Partikel

Die Partikel werden also von ihrem eigenen besten Ergebnis und dem global besten Ergebnis angezogen. Durch ihre Zufällige Startposition und Trägheit werden viele Punkte erkundet die in der Nähe der Lösungsräume sind. So wird die nähere Umgebung um gute Werte genauer getestet.
Die Zufallszahlen erhöhen die Diversität innerhalb des Schwarms, sie bestimmen wie sehr sich einzelne Partikel beeinflussen lassen.

## Einsatz
Der Algorithmus eignet sich besonders zur Lösungsfindung in komplexen Umgebungen und ist auch in der Lage eine große Anzahl lokaler Minima zu umgehen.
Im Gegensatz zu klassischen Methoden wie dem [Gradientenabstieg](07%20Neural%20Nets.md#Gradientenabstieg) müssen die Funktionen nicht mathematisch wohldefiniert sein.

# Ähnliche Verfahren
- Artificial Bee Colony (ABC) [Wikipedia](https://en.wikipedia.org/wiki/Artificial_bee_colony_algorithm)
- Ant Colony System [Wikipedia](https://en.wikipedia.org/wiki/Ant_colony_optimization_algorithms)
- Evolutionary Algorithms [Wikipedia](https://en.wikipedia.org/wiki/Evolutionary_algorithm)

