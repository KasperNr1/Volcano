
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

Es werden zu Beginn zwei geheime Primzahlen $p$ und $q$ bestimmt. Diese sind beliebig und in der modernen Kryptographie typischerweise ca. 300 Stellen lang.
- $p=11$
- $q = 5$

Es wird ihr Produkt $n$ berechnet, zusammen mit $\phi(n)$, was dem Produkt der um $1$ verminderten Primzahlen entspricht. $\phi(x)$ ist demnach nur für Zahlen definiert, die das Produkt von exakt zwei Primzahlen sind.
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
- $c=7^{19} \mod 40 = 23$

Zum entschlüsseln wird der Cyphertext lediglich mit dem anderen, privaten Schlüssel potenziert.
- $m = c^d \mod n = 23^{19} \mod 40 = 7$


> [!Tip]+ Rechenregeln
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


