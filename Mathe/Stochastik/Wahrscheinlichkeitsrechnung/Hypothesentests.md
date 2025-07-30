# Hypothesentests
Stichprobe $10$ Nägel
$$
\begin{array}{c|c|c|c|c|c|c|c|c|c|c}
i & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 \\ \hline
\text{Länge in mm} & 20 & 22 & 19 & 22 & 18 & 21 & 18 & 19 & 21 & 20
\end{array}
$$
Annahme: 
Länge ist normalverteilt mit $\sigma^2 = 9mm^2$

- Wir gehen davon aus, dass die Angaben tatsächlich zutreffen (Nullhypothese $H_0$)
- Wir stellen die Angaben zur Diskussion (Alternativhypothese $H_1$) 

Mathematische Schreibweise:
- Nullhypothese $H_0 : \vartheta = \vartheta_0$
- Alternativhypothese $H_1 : \vartheta \neq \vartheta_0$ (Zweiseitiger Test)

## Beispiel
$H_0 :\mu = \mu_0 = 22$ 
$H_1 :\mu \neq \mu_0 = 22$ 

Signifikanzniveau wird gewählt, $\alpha = 1\%$

> [!Info] Signifikanzniveau
> Auch "Irrtumswahrscheinlichkeit" Ist die Wahrscheinlichkeit für bestimmte Fehlentscheidungen, die man in Kauf nehmen muss. Man spricht von der Wahrscheinlichkeit, dass die Nullhypothese $H_0$ abgelehnt wird, obwohl sie richtig ist.
> In der Praxis wird diese Wahrscheinlichkeit oft mit $\alpha = 5\%$ oder $\alpha = 1\%$ gewählt

Bestimme die Testvariable 
$$
T = g(X_1, \dots, X_n)
$$
abhängig von $n$ bis [iid.](Statistik.md#Einführungsbeispiel) Zufallsvariablen $X_1, \dots, X_n$
$$
T = \cfrac{\cfrac{1}{10} \displaystyle  \sum_{i=1}^{10} x_i - \mu_0}{\cfrac{\sigma}{\sqrt{10}}} \sim \mathbb{N}(0;1)
$$
![](Rechenschritte.png)

Bestimmen der kritischen Grenze $c_k, c_0$:
Nach der Wahl der Irrtumswahrscheinlichkeit lässt sich nun eine Konstante $c$ (kritischer Wert) so bestimmen, dass die Testgröße bei richtiger Nullhypothese mit der statistischen Sicherheit $\boxed{\gamma = 1-\alpha}$ in das symmetrische Intervall fällt.


![[HypoTest.png]]

$$
\begin{array}{l}
P(-c \leq T \leq c) &
= P(T \leq c) - P(T \leq -c) \\
&= \Phi(c) - \Phi(-c) \\
&= \Phi(c) - (1-\Phi(c)) \\
&= 2 \cdot \Phi(c) - 1 = 0.99 \\
\text{In Tabelle schauen} &\Rightarrow c = 2.575
\end{array}
$$
$$
\underbrace{-2.575}_{c_k} \leq t \leq \underbrace{2.575}_{c_0}
$$

Berechne Testwert $\hat{t}$ der Testvariablen $T$ aus einer konkreten Stichprobe $x_1, \dots, x_n$
$\hat{t} = g(x_1, \dots, x_n)$ 

Bsp.
$$
\hat{t} = \cfrac{\cfrac{1}{10} \sum_{i=1}^{10}x_i-22}{\cfrac{3}{\sqrt{10}}} = -2.108
$$
Testentscheid:
Fällt der Wert $\hat{t}$ in den Annahmebereich, dann wird $H_0$ nicht verworfen. Es wurde allerdings statistisch nicht bewiesen. Es kann sein, dass $H_0$ weiterhin gilt.

$\hat{t} = -2.108$ fällt in den Annahmebereich. $H_0$ kann nicht verworfen werden.


> [!info] Hinweis
> Sollte der Prüfwert in den kritischen Bereich fallen, dann ist die Nullhypothese $H_0$ nicht haltbar, wir müssen sie zu Gunsten von $H_1$ verwerfen.


