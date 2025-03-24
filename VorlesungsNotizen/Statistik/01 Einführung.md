# Klausur
- Taschenrechner
- Formelsammlung
- 1 Zettel DINA4 Handschriftlich (Nicht getippt) vor/Rückseite
- Extra Zettel zu Gauß'scher Verteilung

# Wahrscheinlichkeitsraum
Ist die mathematische Beschreibung eines Experiments mit zufälligen Ausgang und umfasst exakt 3 Elemente
$$
\begin{array}{ll}
\Omega & \text{Grundraum} \\
\mathcal{P} & \text{Ereignisfeld} \\
(\Omega); P & \text{Wahrscheinlichkeitsmaß}
\end{array}
$$
## Grundraum $\Omega$
[Menge](Intervalle%20und%20Mengen.md) aller möglichen Ergebnisse $\omega$
### Beispiel
Einmaliges Würfeln $\Omega = \{1; 2; 3; 4; 5; 6 \}$

## Ereignisfeld $\mathcal{P}$
Menge aller beobachtbaren Ereignisse.
Ein Ereignis ist eine Teilmenge des [Grundraums](#Grundraum%20$%20Omega$)
Also:
$$
\begin{array}{lll}
\text{Ereignisfeld} &= \mathcal{P}(\Omega) &=\text{Potenzmenge von } \Omega \\
&= \{A \mid A \subseteq \Omega\}
&= \{\Phi, \Omega, \dots\}
\end{array}
$$

## Wahrscheinlichkeitmaß / Wahrscheinlichkeitsverteilung
Dies ist eine Funktion 
$P : \mathcal{P}(\Omega) \rightarrow [0;1]$ 
$A \mapsto P(A) \in [0;1]$ 

$P(A)=$ Wahrscheinlichkeit dass das Ereignis $A$ eintritt
### Definition
Eine Funktion $P : \mathcal{P}(\Omega) \rightarrow [0;1]$ heißt Wahrscheinlichkeitsmaß, falls:
- $P(\Omega) = 1$
- $P(A \dot\cup B) = P(A) + P(B)$
  Falls A und B keine Schnittmenge haben 
Ein Tripel $(\Omega; \mathcal(P)(\Omega); P)$ heißt Wahrscheinlichkeitsraum (WR)

### Beispiel
$$
\begin{array}{ll}
\Omega &= \{1; 2; 3; 4; 5; 6\} \\
e_1 &= \{1\} \subseteq \Omega \\
e_k &= \{k\} \\
P(\{k\}) &= \frac16
\end{array}
$$

## Satz (Rechenregeln)
Sei $(\Omega; \mathcal{P}(\Omega); P)$ ein Wahrscheinlichkeitsraum

1. $P(\emptyset) = 0$
   Unmögliches Ereignis
2. $P(\overline{A}) = 1-P(A)$
   Gegenereignis
3. $A\subseteq B \rightarrow P(A) \leq P(B)$
4. $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
   Additionssatz

### Beweis
1.Unmögliches Ereignis
$$
\begin{array}{ll}
\Omega &= \Omega \dot\cup \emptyset \\
P(\Omega) &= 1 \\
1 &= P(\Omega) + P(\emptyset) \\
P(\emptyset) &= 0
\end{array}
$$

 2-4:
 Siehe [Skript](C:\Users\dh10mbo\OneDrive - Durr Group\Documents\Uni\Vorarbeit\statistikSkript.pdf) Seite 12

# Laplace'scher Wahrscheinlichkeitsraum
$$
\begin{array}{ll}
A \subset \Omega & |A| = \text{Anzahl der Elemente die zu A gehören}
\end{array}
$$
Ein WR mit $|\Omega| < \infty$ heißt **endlicher Wahrscheinlichkeitsraum**
## Definition
Ein endlicher WR heißt Laplace'scher WR fall die Elementarereignisse gleich wahrscheinlich sind. D.h.
$$
\mathcal P(\{\omega\}) = \frac{1}{|\omega|}
$$
## Beispiel Zweimaliges Würfeln
$w = (i;j)$, $i$ = Augenzahl erster Wurf; $j$ = Augenzahl zweiter Wurf
$$
\begin{array}{cl}
\Omega &= \{(i;j) : 1 \leq i; j \leq 6 \}$ \\
|\Omega| &= 6^2 = 36
\end{array}
$$

$$
\begin{array}{ll}
P &: \text{Gleichverteilung} \\
A &= \text{Augensumme} \geq 10 \\
A &= \{(6,6); (6,5); (5,6); (6,4); (4,6); (5,5)\} \\
|A| &= 6 \\
P(A) &= \frac{6}{36} = \frac16
\end{array}
$$

## Beispiel Geburtstagsproblem
Gesucht ist die Wahrscheinlichkeit dass von $n$ zufälligen Personen mindestens $2$ am selben Tag Geburtstag haben.

$$
	\mathcal P(A) = 1 - \frac{\prod_{i = 1}^{i = n} (365 - i + 1) }{365^n}
$$
$$
P(A) =\left\{
\begin{array}{ll}
11,7\% & n=10 \\
50,7\% & n=23 \\
97,0\% & n=50 \\
99,994 \% & n=80
\end{array}
\right.
$$
# Einfache Urnenmodelle
Gegeben ist eine Urne mit exakt $n$ Elementen. Wir entnehmen der Urne $k$ Elemente zufällig und modellieren verschiedene Arten von Lösungsvorgängen.

## Stichprobe mit Reihenfolge und Zurücklegen
Es gibt $k$ verschiedene Elemente (Würfel) die jeweils $n$ Varianten besitzen
$$
\begin{array}{cl}
\Omega_I &= \{w = (w_1, \dots, w_k) \mid w_i \in \{1; \dots; n\}\} \\
|\Omega_I| &= n^k 
\end{array}
$$

## Stichprobe mit Reihenfolge ohne Zurücklegen
$$
\begin{array}{cl}
\Omega_{II} &= \{w = (w_1, \dots, w_k) \mid w_i \in \{1; \dots; n\} \mid w_i \neq w_j \text{ für } i\neq j\} \\
\text{Stufe 1:} & n \text{ Möglichkeiten} \\
\text{Stufe 2:} & n-1 \text{ Möglichkeiten} \\
\text{Stufe k:} & n-h+1 \text{ Möglichkeiten} \\
|\Omega_{II}| &= \frac{n!}{(n-k)!} \mid (\text{nPr})
\end{array}
$$

### Beispiel Fußball-EM
Es stehen 8 Mannschaften im Viertelfinale, von denen 3 eine Medaillie gewinnen werden. Vergleicht man nun die 3 Medaillien mit der Anzahl der zu ziehenden Kugeln $(k)$ und die $8$ Mannschaften mit der Gesamtzahl der Kugeln $(n)$, erhält man folgende Möglichkeiten:
$$
\frac{8!}{(8-3)!} = \frac{8!}{5!} = 8 * 7 * 6 = 336
$$
## Stichprobe ohne Reihenfolge ohne Zurücklegen
$$
\begin{array}{cl}
\Omega_{III} &= \{w = (w_1, \dots, w_k) \mid w_i \in \{1; \dots; n\} \mid w_1 < w_2 < \dots < w_k\} \\
|\Omega_{III}| &= \frac{n!}{(n-k)!*k!} =: \binom{n}{k} \mid  (\text{Binomialkoeffizient nCr})
\end{array}
$$
### Beispiel Lotto
$n = 49; \quad k = 6$

#### Wahrscheinlichkeit für 6 Richtige 
$$
|\Omega| = \binom{49}{6} = \frac{49!}{(49-6)!*6!} = 13.983.816
$$
$$
\begin{array}{cl}
A &= \text{6 Richtige} \\
|A| &= 1 \\
P(A) &= \frac{|A|}{|\Omega|} = \frac{1}{\binom{49}{6}} = \frac{1}{13.983.816}
\end{array}
$$

#### Wahrscheinlichkeit für mindestens 4 Richtige
$A_i$ = genau $i$ Richtige $(i = 4; 5; 6)$

$$
\begin{array}{cl}
P(A_4 \dot\cup A_5 \dot\cup A_6) &= P(A_4) + P(A_5) +P(A_6) \\
\\
|A_4| &= \binom{6}{4} * \binom{43}{2} \\
|A_5| &= \binom{6}{5} * \binom{43}{1} \\
|A_6| &= \binom{6}{6} * \binom{43}{0}\\
\\
\displaystyle
P(A_4 \dot\cup A_5 \dot\cup A_6) &= \frac{\binom{6}{4} * \binom{43}{2} + \binom{6}{5} * \binom{43}{1} + \binom{6}{6} * \binom{43}{0}}{\binom{49}{6}}
\end{array}
$$

