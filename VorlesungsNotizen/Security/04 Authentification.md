
> [!Example] Klausuraufgabe
> Entropie eines Passworts berechnen
> Seite 14 - Foliensatz Authentifikation (Orange)
> $$
> \text{Entropie} = \log_2(\text{Zeichensatz}^{\text{Länge}}) = \text{Länge} \cdot \log_2{\text{Zeichensatz}}
> $$


> [!Example] Klausuraufgabe
> Erstellung einer Passphrase
> Seite 17
> ![](Passphrase%20Erstellung.png)

> [!Example] Klausuraufgabe RSA-Algorithmus
> Verschlüsselung durchrechnen können:
> 
> Primzahlen $p$ und $q$ sind bekannt, ebenfalls der Vorschlag für privaten Schlüssel $e$.
> Prüfung auf Gültigkeit und Berechnung des öffentlichen Schlüssels. Anwendung der Verschlüsselung und Entschlüsselung des Ciphertexts.

# RSA Algorithmus
Public-Key Basiertes Asymmetrisches Verschlüsselungsverfahren. Jede Partei erzeugt ein Paar aus zueinander passenden Schlüsseln, einer wird geheim gehalten und zum entschlüsseln verwendet, der andere ist öffentlich und kann verwendet werden um Nachrichten an diesen Empfänger zu verschlüsseln.

Die Fähigkeit der Entschlüsselung ist eine Eigenschaft besonderer Zahlenpaare bei der Berechnung von Exponenten in [Modularen Körper](Gruppen%20Ringe%20und%20Körper.md). Die Technik basiert auf [Fermants little theorem](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem). 

## Ablauf RSA
![](RSA.png)

Es werden zu Beginn zwei geheime Primzahlen $p$ und $q$ bestimmt. Diese sind beliebig und in der modernen Kryptographie typischerweise ca. 300 Stellen lang.
- $p=11$
- $q = 5$

Es wird ihr Produkt $n = p * q$ berechnet, zusammen mit $\phi(n)$, was dem Produkt der um $1$ verminderten Primzahlen entspricht. $\phi(x)$ ist demnach nur für Zahlen definiert, die das Produkt von exakt zwei Primzahlen sind.

> [!Error] Fehler
> $\Phi(n)$ Definition stimmt nicht.
> Siehe Folien zu Kryptographie

- $n=55$
- $\phi(55) = (11-1)\cdot(5-1) = 10 \cdot 4 = 40$

Nun kann das Schlüsselpaar bestimmt werden.
Dabei wird ein Schlüssel $e$ frei gewählt, unter der Bedingung, dass er zum Wert $\phi(n)$ teilerfremd ist und $1<e<\phi(n)$ gilt.
- $e = 19$

Der zweite Schlüssel $d$ ist die Zahl, für die $d \cdot e = 1 \mod \phi(n)$ gilt.
$d$ ist also das [Multiplikative Invers](Euklidischer%20Algorithmus%20&%20Diophantsche%20Gleichungen.md#Multiplikatives%20Invers) zu $e$.
Dieses Invers existiert, da die [Bedingungen für dessen Existenz](Modulare%20Arithmetik.md#Satz-Existenz) gegeben sind.
- $d=19$
  da $19*19=361 = 1 \mod 40$

Die verschlüsselte Nachricht $c$ entspricht mit dem Klartext $m$ $c=m^e \mod n$
- $c=7^{19} \mod 55 = 8$

Zum entschlüsseln wird der Chiffretext lediglich mit dem anderen, privaten Schlüssel potenziert.
 $$
 \begin{array}{ll}
 m &= c^d \mod n \\
 &= 8^{19} \mod 55 \\
 &= 7
 \end{array}
 $$

![](Modulare%20Arithmetik.md#^Rules)

# Diffie-Hellman Key-Exchange
Dieser sehr elegante Algorithmus wird verwendet um auch auf unsicheren Kommunikationskanälen einen geheimen gemeinsamen Schlüssel zu vereinbaren. Dieser kann dann für beliebige [[Symmetrische Verschlüsselungsverfahren]] genutzt werden. 
Er ist in seiner ursprünglichen Form anfällig für "Man In the Middle Attacks", was die Entwicklung einiger Varianten verursacht hat.

![](Diffie-Hellman.png)
## Ablauf Diffie-Hellman
Die beiden Partner vereinbaren öffentlich eine Primzahl $p$ und eine Basis $g$ aus dem [Galois-Körper](Gruppen%20Ringe%20und%20Körper.md#Verschiedene%20Strukturen%20von%20Mengen) $GF(p)$. 
$p$ ist also eine beliebige Primzahl und $g \in [2, p-2]$

Jeder wählt eine geheime Zufallszahl aus dem gegebenen Intervall und berechnet einen öffentlichen Wert.

Beispielsweise wurden $p=31$ und $g=9$ vereinbart.
Partner $A$ wählt nun $a = 13$ und $B$ die Zahl $b = 17$.

Es wird jeweils ein öffentlicher Wert berechnet, wobei die bekannte Basis mit der geheimen Zahl im Körper $GF(31)$ exponiert wird.

$$
\begin{array}{}
	\alpha = 9^{13} = 18 \mod 31 \\
	\beta = 9^{17} = 19 \mod 31 \\
\end{array}
$$
Diese berechnete Zahl wird nun dem jeweils anderen Partner unverschlüsselt übermittelt und erlaub es diesem den Austausch zu vollenden.
Zum Abschluss wird der finale Schlüssel $K$ berechnet, wobei nur die übermittelte Zahl mit der selben geheimen Zahl exponiert wird.
$$
\begin{array}{}
	K_A = 19^{13} = 14 \mod 31 \\ 
	K_B = 18^{17} = 14 \mod 31 \\ 
\end{array}
$$

Der Schlüssel $K$ ist nun nur den beiden Kommunikationspartnern bekannt und kann verwendet werden.




