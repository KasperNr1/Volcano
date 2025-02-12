Ziel: Verbessertes Verfahren zur Bestimmung des [multiplikativen Invers](Gruppen%20Ringe%20und%20Körper.md) in $\mathbb{Z}_n$ 
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
$r_0 = a \qquad r_1 = b \qquad r_k = r_{k-2} (mod \, r_{k-1})$
$q_k = r_{k-2} \, DIV \, r_{k-1}$ 
Also $r_{k-2} = q_k * r_{k-1} + r_k$ 

Die Rekursion bricht definitiv ab, da spätestens $1$ ein gemeinsamer Teiler ist.
$$r_{n+1}=0\rightarrow r_n = ggT$$ 
# Diophantische Gleichung
TODO