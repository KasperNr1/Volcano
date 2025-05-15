# Bedingte Wahrscheinlichkeiten
## Experiment: Wurf mit 2 Würfeln
$$
\begin{array}{ll}
|\Omega| &= 36 \\
A &= \text{Augensumme 8} \\
B &= \text{Beide Würfel sind gerade}
\end{array}
$$
Gesucht: 
$P(B|A) = \text{WS dass beide Würfel gerade sind, wenn die Summe 8 beträgt}$ 

$A = \{(2;6), (3;5), (4;4), (5;3), (6;2)\}$
$|A| = 5$
Von diesen $5$ Elementarereignissen führen $3$ zum Ereignis $B: \{(2;6),(4;4), (6;2)\}$   

$$P(A|B) = \dfrac{P(A \cap B)}{P(B)} = \cfrac{\cfrac{3}{36}}{\cfrac{5}{36}} = \dfrac35 $$ 
## Pfadregel
Zur Bestimmung der WS eines komplexen Ereignis werden die WS entlang des Pfades multipliziert.
![](Baumdiagramm.png)

## Vierfeldertafel
$$
\begin{array}{cccc}
& B & \overline{B} & \Sigma \\
A & P(A \cap B) & P(A \cap \overline{B}) & P(A) \\
\overline{A} & P(\overline{A} \cap B) & P(\overline A \cap \overline B) & P(\overline A) \\
\Sigma & P(B) & P(\overline B) & 1
\end{array}
$$
Definition:
Sei $(\Omega; \mathcal P(\Omega); P)$ ein WR.
$P(A) \neq 0$
Dann heißt $P(B|A) = \dfrac{P(A \cap B)}{P(B)}$ die bedingte WS von $B$ gegeben $A$.


> [!Info] Bemerkung
> $P(A|B)$ und $P(B|A)$ sind im Allgemeinen völlig verschieden.
> Beispiel:
> $A = \text{Regen}$
> $B = \text{Bewölkt}$ 
> $$P(B|A) = 1 \qquad P(A|B) << 1$$

## Beispiel
Irrelevant, nur während der VL
1. Rot: $\frac{8}{24} = \frac13$ 
2. $U_1$ wenn Rot: $\cfrac{\cfrac{5}{24}}{\cfrac{1}{3}} = \dfrac{15}{24}=\dfrac58$ 

## Satz
Seien $A_1, \dots, A_n$ Ereignisse mit $P(A_1 \cap \dots \cap A_n) > 0$
Dann gilt:
$P(A_1 \cap \dots \cap A_n) = P(A_1) * P(A_2 | A_1) * P(A_3 | A_1 \cap A_2) * \dots * P(A_n | A_1 \cap A_2 \cap \dots \cap A_{n-1})$ 

## Beispiel (Skat)
$A_i = \text{Spieler i erhält ein Ass}$ 
$P(A_1) = \dfrac{\binom{4}{1} * \binom{28}{9}}{\binom{32}{10}}$ 

$P(A_2 | A_1) = \dfrac{\binom{3}{1} * \binom{19}{9}}{\binom{22}{10}}$

$P(A_3 | A_1 \cap A_2) = \dfrac{\binom{2}{1} * \binom{10}{9}}{\binom{12}{10}}$

$P(A_1 \cap A_2 \cap A_3) = 5,56 \%$

# Totale Wahrscheinlichkeit
## Formel von Bayes
### Einführungsbeispiel
In einem Werk werden auf $4$ Maschinen Glühbirnen hergestellt.

| Maschine                   |  $M_1$  |  $M_2$  |  $M_3$  |  $M_4$  |
| -------------------------- | ------- | ------- | ------- | ------- |
| Anteil an Gesamtproduktion | $0.10$  | $0.20$  | $0.30$  | $0.40$  |
| Ausschussanteil            | $0.02$  | $0.01$  | $0.04$  | $0.02$  |

Aus der Gesamtproduktion wird zufällig eine Glühbirne entnommen.
1. Mit welcher Wahrscheinlichkeit ist die Glühbirne defekt?
2. Mit welcher WS kommt eine defekte Birne von $M_3$?

#### 1. Defekt
$$
\begin{array}{ll}
A_i &= \text{Glühbirne wurde auf $M_i$ produziert} \\
B &= \text{Birne ist defekt}
\end{array}
$$
$P(B) = 0.1 * 0.02 + 0.2 * 0.01 + \dots = 0.024$

Allgemein
$$
\begin{array}{ll}
P(B) &= \sum_{i=1}^{4} P(A_i \cap B) \\
&= \sum_{i=1}^{4} P(A_i) * P(B \mid A_i) 
\end{array}
$$
#### 2. M3 wenn defekt
$$
P(A_3 \mid B) = 0.5
$$

## Satz
Sei $(\Omega; \mathcal P(\Omega); P)$ ein WR;
$B, A_1, A_2, \dots, A_n$ Ereignisse die paarweise disjunkt sind
- Jedes Ereignis hat eine Wahrscheinlichkeit größer $0$
(Siehe Satz 2.8 und 2.9 Skript)
![](SatzDerTotalenWS.png)
![](BayesScheFormel.png)

# Stochastische Unabhängigkeit
Aus der Gleichung für $P(B \mid A)$ von [oben](#Vierfeldertafel) lässt sich ableiten:
$P(A \cap B) = P(A) * P(B \mid A)$ 
$A$ und $B$ heißen stochastisch unabhängig wenn sich die beiden Ereignisse nicht gegenseitig beeinflussen.
Es muss dazu gelten:
$P(A \cap B) = P(A) * P(B)$

## Beispiel
Abschlussklasse, 15 W 10 M

12 W und 6 M bestehen die Prüfung

$A = \text{Prüfling ist W}$ 
$B = \text{Prüfling besteht Prüfung}$

Sind $A$ und $B$ stochastisch unabhängig?

$P(A) = \frac{15}{25}$
$P(B) = \frac{18}{25}$

$P(A \cap B) = \frac{12}{25}$

$\underbrace{P(A) * P(B)}_{0.432} \neq \underbrace{P(A \cap B)}_{0.48}$ 