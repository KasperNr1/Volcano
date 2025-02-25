# Vektoren
Ein m-Tupel $\begin{pmatrix} a_1 \\ a_2 \\ a_3 \end{pmatrix} \in \mathbb{R}^n$ heißt Vektor.
Die $a_i$ heißen Koordinaten des Vektors, $\mathbb{R}^n$ ist der Vektorraum.

## Rechenoperationen
- Addition $\vec{a} + \vec{b} = \begin{pmatrix} a_1 + b_1 \\ a_2 + b_2 \\ a_3 + b_3 \end{pmatrix}$ 
- Skalare Multiplikation $k * \vec{a} = \begin{pmatrix} k * a_1 \\ k * a_2 \\ k * a_3 \end{pmatrix}$ 
## Linearkombinationen und Basis
Gegeben sind die Vektoren $a_1 = \begin{pmatrix} 2 \\ 1  \end{pmatrix} \quad a_2 = \begin{pmatrix} -2 \\ 2 \end{pmatrix} \quad b = \begin{pmatrix} 1 \\ 5 \end{pmatrix}$ 
$b$ lässt sich als Linearkombination von $a_1$ und $a_2$ ausdrücken, $b = 2 * a_1 + 1.5 * a_2$ 

### Definition Lineare (un-)abhängigkeit
Wenn $k_1; k_2; k_3; \ldots; k_m = 0$ die einzige Möglichkeit ist, die Gleichung $k_1 * \vec{a_1} + k_2 * \vec{a_2} + \cdots = \vec{O}$ zu erfüllen, so sind die Vektoren $a_1; a_2; \ldots$ linear unabhängig.
Sonst nennt man sie linear abhängig.
Durch Umstellen der Gleichung ist ersichtlich, dass kein Vektor einer linear unabhängigen Menge durch eine beliebige Kombination der anderen Vektoren ausgedrückt werden kann.

### Definition Maximale Menge an Vektoren
Eine Menge linear unabhängiger Vektoren heißt maximal, wenn kein weiterer Vektor hinzugefügt werden kann, ohne dass die Lineare Unabhängigkeit verloren geht.

Die Basis eines Vektorraumes entspricht einem "Minimalen Erzeugenden-System"

| **minimal**           | Basis besteht aus so wenig Vektoren wie möglich                                                                                                                                                                                 |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erzeugendensystem** | Menge an Vektoren die durch Linearkombination jeden beliebigen Vektor erzeugen können.                                                                                                                                          |
| **Dimension**         | Maximale Anzahl von linear unabhängiger Vektoren eines Vektorraums $V$<br><br>Für jeden $m$-dimensionalen Vektorraum ist die Menge von $m$ linear unabhängigen Vektoren eine Basis. Umgekehrt hat jede Basis genau $m$ Vektoren |
