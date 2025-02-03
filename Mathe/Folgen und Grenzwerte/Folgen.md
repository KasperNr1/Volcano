# Begriff
## Definition
Eine Zuordnung mit der Definitionsmenge $D = \mathbb{N}$ heißt Folge

## Schreibweise
$(a_{n}); \qquad a_{5}: 5\text{-tes Folgeglied}$

z.B. Folge $(a_{n}) \text{mit} (a_{n}) = 2n+3 \rightarrow a_{5}=2 \cdot 5 + 3 = 13$

## Hintergrund "Mittelwerte"
- Arithmetisches Mittel:
	- "Klassischer Durchschnitt"
	- Quotient der Summe aller Elemente und der Menge an Elementen
	- Klausurnoten
- Geometrisches Mittel:
	- $n \text{-te}$ Wurzel des Produkts aller Werte $n=\text{Menge an Werten}$
	- Beispiel Zinseszins aus verschiedenen Zinssätzen als konstanten Zinssatz angeben
	- $2\%$, $7\%$ und $5\%$  ist gleich $4,6464\%$ für $3$ Jahre da $\sqrt[3]{1.02 \cdot 1.07 \cdot 1.05} \approx 1.046464$

## Explizite Darstellung
Eine Folge in der jeder Wert allein, ohne Kenntnis über andere Werte berechnet werden kann ist "explizit" dargestellt.  
Die Folge $(a_{n})$ mit $(a_{n}) = a+dn$ ist einer arithmetische Folge mit dem Anfangswert $a$  und der Differenz $d$ .  
Jeder Wert $(a_{n})$ ist die arithmetische Mitte seiner Nachbarn $(a_{n+1})$ und $(a_{n-1})$ .

$(b_{n})$ mit $(b_{n}) = b \cdot q^{n}$  ist eine geometrische Folge mit dem Anfangswert $b$ und dem Quotient $q$.  
Hier ist jeder Wert das geometrische Mittel seiner Nachbarn.

### Beispiel Quadratpflanze
![](quadratpflanze.png)
$$U_{n}=4+2n$$
$$A_{n}=\sum_{i=0}^{n}{\frac{1}{3^{i}}} = \frac{3}{2}-\frac{1}{2} \left(\frac{1}{3}\right)^{n}$$

### Schaubild einer Folge
$$ a_{n} \text{ mit } a_{n} = \frac{2n}{n+1}$$
![](schaubildFolge.png)

### Gesuchte Folge
$a_{n}$ mit ${0; \frac{1}{2}; \frac{2}{3}; \frac{3}{4}; \frac{4}{5}}$

## Rekursive Darstellung
Eine Folge ist rekursiv, wenn es mindestens einen Startwert gibt, und $a_{n+1}$ durch z.B. $a_{n}$ berechnet wird.
Bsp. Sparschwein: Jeden Monat die Hälfte des Inhalts dazu und $2$ Euro entnehmen bei $10€$ Startwert
- $b_0 = 10 \quad b_n=b_{n-1}\cdot1.5-2$
- $10;13;17.5;24;25 \ldots$

## Eigenschaften von Folgen
- (Streng-) Monotonie wie bei Funktionen
- Beschränkheit nach oben/unten wenn es ein $S/s$ gibt, dass nie über-/unterschritten wird
- "Beschränkt" nur bei Existenz beider Schranken

## Nachweis von Monotonie / Beschränktheit

### Ansatz über Differenz benachbarter Werte
$$a_n=\frac{4n}{n+3}$$
**Behauptung: $a_n$ ist SMS (Streng-Monoton-Steigend)**
 
Beweis dass $a_{n+1}-a_n>0$
$$ \frac{4(n+1)}{(n+1)+3} - \frac{4n}{n+3} = \frac{4(n+1)\cdot(n+3)}{(n+4)\cdot(n+3)} - \frac{4n\cdot (n+4)}{(n+3) \cdot (n+4)} = \frac{12}{(n+3)(n+4)} > 0$$

### Geschicktes Abschätzen
