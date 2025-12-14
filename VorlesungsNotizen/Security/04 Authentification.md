# Begriffe
## Identifizierung
- Wer ist diese Person

## Authentifizierung
- Ist das die Person die sie behauptet zu sein?

## Authorisierung
- Darf diese Person das?


# Authentifikation
Die Identität einer Person kann nicht direkt durch einen Computer überprüft werden. Aus diesem Grund greift man auf andere Kriterien zurück, die eine ausreichende Überzeugen erreichen.
Dabei kann besonderes Wissen, der Bestitz von Gegenständen oder Biometrie abgeprüft werden.

## Durch Wissen
Das Klassische Passwort oder Sicherheitsfragen landen in dieser Kategorie. Wenn sie geheim gehalten wurden kann sie nur der Besitzer kennen. 
Jedoch hängt die Sicherheit hier auch von der Länge und Komplexität der Passwörter ab. Zusätzlich können sie gestohlen werden, wenn Angreifer durch Beobachten oder durch Keylogger / Phishing in der Lage sind die Passwörter zu lernen.

![](PasswordCheckFlow.png)

In der [Datenbank](Grundlagen.md#Datenbank) einer Anwendung ist zu jeder UserID ein Passwort gespeichert. Für erweiterte Sicherheit ist das Passwort nicht im Klartext gespeichert, sondern nur der [Hashwert](Hashing.md) des Passworts. Zum Abgleich wird das eingegebene Passwort gehasht und das Ergebnis mit dem hinterlegten Eintrag verglichen.


### Überprüfung
#### Salz
Durch Speichern von Hashwerten sind die Passwörter nicht in der Datenbank enthalten. Ein Angreifer kann trotzdem die Hashwerte bekannter Passwörter abgleichen. Um dies zu verhindern wird ein sog. 'Salt' eingesetzt. Es ist eine zusammen mit dem Hash abgespeicherte, zufällige Zeichenfolge die dem eingegebenen Passwort angehängt wird, bevor der Hash berechnet wird. So werden auch dann unterschiedliche Hashes gespeichert, wenn zwei Nutzer das selbe Passwort verwenden.

#### Pfeffer
Bei 'Pepper' ist die Idee ähnlich, jedoch handelt es sich hier um eine für alle Nutzer gleiche, geheime Zeichenfolge.
Der Wert des Peppers kann jedoch nicht geändert werden, ohne dass sich der Benutzer einloggen muss. Erst bei einem erfolgreichen Login kann mit einem neuen Pepper der erwartete Hashwert aktualisiert werden. 

### Sicherheit eines Passworts
Die Entropie eines Passworts gibt an, wie komplex es ist. Komplexere Passwörter sind im Allgemeinen sicherer. 
$$
\text{Entropie} = \log_2(\text{Zeichensatz}^{\text{Länge}}) = \text{Länge} \cdot \log_2{\text{Zeichensatz}}
$$

Passwörter gelten als ausreichen sicher, wenn sie mindestens $80$ Bit Entropie enthalten.


> [!Example] Klausuraufgabe
> Erstellung einer Passphrase
> Seite 17
> ![](Passphrase%20Erstellung.png)

## Durch Besitz
Verschiedene Magnetstreifen- oder Chipkarten existieren, die geheime Tokens an spezielle Lesegeräte übertragen können. Auch USB-Tokens wie Yubee-Keys sind geeignet. Sie bieten zusätzlich den Vorteil, dass sie kein besonderes Lesegerät benötigen und auch als regulärer Speicher verwendet werden können.

Es gibt auch OTP-Geräte, die in der Lage sind kurzzeitig gültige Tokens zu generieren. Selbst wenn ein Angreifer das Token aufzeichnet, kann es nicht verwendet werden, da sie nur für einzelne Aktionen gültig sind.

## Durch Biometrie
- Fingerabdruck
- Gesicht
- Iris
- Hand
- Unterschrift
- Stimme
- Gangart
- Tattoo

Dabei müssen die Merkmale einige Eigenschaften erfüllen
- Universalität (Jede Person sollte es besitzen)-
- Einzigartigkeit
- Permanenz
- Messbarkeit
- Fälschungssicherheit

### Prüfung
Die Leistungsfähigkeit wird anhand der Fehler bestimmt

**False Acceptance Rate (FAR)**
$$
\text{FAR} = \frac{\text{Anzahl fälschlich Akzeptierer Versuche}}{\text{Anzahl ungültiger Versuche}}
$$
**False Rejection Rate (FRR)**
$$
\text{FRR} = \frac{\text{Anzahl fälschlich abgelehnter Versuche}}{\text{Anzahl gültiger Versuche}}
$$

## Vergleich

|           | Wissen                                                                                         | Besitz                                                                                                | Biometrie                                                                                            |
| --------- | ---------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Vorteile  | - Einfach<br>- Theoretisch Sicher<br>- Keine zusätzliche Technik                               | - Kein Merken<br>- Hohe Sicherheit<br>- Benutzerfreundlich                                            | - Hohe Sicherheit<br>- Kein Transport notwendig                                                      |
| Nachteile | - Effektivität variabel<br>- Viele Passwörter werden unübersichtlich<br>- Leicht zu übertragen | - Schnittstelle muss vorhanden sein<br>- Aufwendige Umsetzung<br>- Hardware muss transportiert werden | - Aufwendige Umsetzung<br>- Zusätzliche Hardware<br>- Hohe Kosten<br>- Wertlos nach Kompromittierung |
Es sollte eine Kombination von Merkmalen verwendet werden, beispielsweise eine Kombination von Besitz und Biometrie (Fingerabdruck auf einem bestimmten Handy) oder Passwörter mit 2FA-Codes.


# RSA Algorithmus
Public-Key Basiertes Asymmetrisches Verschlüsselungsverfahren. Jede Partei erzeugt ein Paar aus zueinander passenden Schlüsseln, einer wird geheim gehalten und zum entschlüsseln verwendet, der andere ist öffentlich und kann verwendet werden um Nachrichten an diesen Empfänger zu verschlüsseln.

Die Fähigkeit der Entschlüsselung ist eine Eigenschaft besonderer Zahlenpaare bei der Berechnung von Exponenten in [Modularen Körper](Gruppen%20Ringe%20und%20Körper.md). Die Technik basiert auf [Fermants little theorem](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem). 

> [!Example] Klausuraufgabe RSA-Algorithmus
> Verschlüsselung durchrechnen können:
> 
> Primzahlen $p$ und $q$ sind bekannt, ebenfalls der Vorschlag für privaten Schlüssel $e$.
> Prüfung auf Gültigkeit und Berechnung des öffentlichen Schlüssels. Anwendung der Verschlüsselung und Entschlüsselung des Ciphertexts.
## Ablauf RSA
![](RSA.png)

Es werden zu Beginn zwei geheime Primzahlen $p$ und $q$ bestimmt. Diese sind beliebig und in der modernen Kryptographie typischerweise ca. 300 Stellen lang.
- $p=11$
- $q = 5$

Es wird ihr Produkt $n = p * q$ berechnet, zusammen mit $\phi(n)$, was dem Produkt der um $1$ verminderten Primzahlen entspricht.

> [!Info]- $\Phi$-Funktion
> Die eulersche $\Phi$-Funktion gibt zu jeder natürlichen Zahl $n$ an, wie viele teilerfremde natürliche Zahlen es gibt, die kleiner sind als $n$
> 
> - $1$ ist ein Sonderfall, da die Zahl nicht prim ist und auch nicht als Produkt von Primzahen dargestellt werden kann.
>   $\Phi(1)=1$
> - $6$ ist zu zwei Zahlen teilerfremd ($4;5$)
>   $\Phi(6) = 2$
> - $13$ ist als Primzahl zu allen kleineren Zahlen teilerfremd. Es gilt allgemein $\Phi(p) = p-1$
>   $\Phi(13) = 12$
> 
> Für zwei Primzahlen $p$ und $q$ mit $p \neq q$ gilt $\Phi(p \cdot q) = (p-1) \cdot (q-1)$

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

Dieses Zahlenbeispiel führt zu einem Sonderfall. Beide Schlüssel sind identisch. Bei größeren Zahlen die tatsächlich für kryptographische Berechnungen verwendet werden ist dies deutlich seltener. Man könnte an dieser Stelle auch neue Schlüssel berechnen in dem man das gewählte $e$ tauscht um ein Paar nicht-identischer Schlüssel zu generieren. Dieses Beispiel verzichtet darauf und verwendet die beiden identischen Schlüssel.

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

### RSA-Signaturen
Eigenschaften einer Digitalen Signatur sollen sein:
- Zweifelsfreie Identität (Eine Person wird eindeutig bestätigt)
- Keine Wiederverwendbarkeit (Signatur soll nicht vom Dokument gelöst werden können)
- Unveränderbarkeit
- Verbindlichkeit

#### Ablauf RSA-Signatur
Wie auch bei der [RSA-Verschlüsselung](#RSA%20Algorithmus) werden aus zwei geheimen Primzahlen ein Paar an Schlüsseln erzeugt.

Die Nachricht wird mit dem privaten Schlüssel "verschlüsselt" und unverändert zusammen mit der "verschlüsselten" Nachricht und dem öffentlichen Schlüssel übertragen.

Der Empfänger kann die "verschlüsselte" Nachricht mit dem öffentlichen Schlüssel entschlüsseln und prüfen, ob sein Ergebnis mit der Unverschlüsselt übertragenen Nachricht übereinstimmt. Falls dies der Fall ist, ist die Nachricht definitiv unverändert und vom erwarteten Absender. 

![](RsaSignature.png)

#### Beispiel RSA-Signatur
Wählen der geheimen Primzahlen
- $p=3$
- $q=11$
- $n=p \cdot q = 3 \cdot 11 = 33$
- $\phi(n) = \phi(33) = (3-1)\cdot(11-1) = 20$
- Wähle $e=3$ wobei $ggT(e, \phi(n)) = 1$ sein muss
- Berechne $d = e^{-1} \mod \phi(n) = 3^{-1} \mod 20 = 7$

Die Nachricht $x=4$ wird nun signiert.
Die Signatur $sig$ besteht aus der Nachricht $x$ und dem Signaturwert $s$. Dieser berechnet sich wie folgt:
$$
\begin{array}{rl}
s &= x^{d} \mod n \\ &= 4^7 = 16 \mod 33
\end{array}
$$
Somit ist die Signatur
$$
\text{sig} = (x, s) = (4, 16)
$$
Der Empfänger erhält also
- Die öffentlichen Teile der Verschlüsselung
	- $n=33$
	- $e=3$
- Die Signatur $(x, s) = (4, 16)$

Er verifiziert sie indem er den Signaturwert mit dem Schlüssel exponiert.
$$
\begin{array}{ll}
x^{\prime} &= s^e \mod n \\
&= 16^3 \mod 33 \\
&= 4
\end{array}
$$
Da $x = x^{\prime}$ ist die Signatur gültig.


# Diffie-Hellman Key-Exchange
Dieser sehr elegante Algorithmus wird verwendet um auch auf unsicheren Kommunikationskanälen einen geheimen gemeinsamen Schlüssel zu vereinbaren. Dieser kann dann für beliebige [[Symmetrische Verschlüsselungsverfahren]] genutzt werden. So ist es nicht nötig, für jedes Paar an Kommunikationspartnern einen eigenen Schlüssel zu verwenden und speichern.
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


# Homomorphe Verschlüsselung
Eine Verschlüsselung heißt dann homomorph, wenn sie bestimmte Operationen auf den verschlüsselten Daten erlaubt. Beispielsweise können so Drittanbieter eingesetzt werden um sensible Daten zu verarbeiten, ohne dass sie in der Lage sind diese zu lesen oder durch Datenlecks zu veröffentlichen.

## Ablauf Homomorphe Verschlüsselung
![](HomomorpheVerschlüsselung.png)

Die Verschlüsselung ist sehr simpel. Es wird eine Primzahl $p$ und eine Zufallszahl $r$ gewählt. Der Klartext $m$ wird in den Chiffretext $c$ umgewandelt.
$$
c = m + p \cdot r
$$
Mit den Chiffretexten können nun beliebige Additionen oder Multiplikationen durchgeführt werden. Diese Eigenschaft ist besonders, typischerweise ist höchstens eine der beiden Operationen möglich.
Der Klassische [RSA Algorithmus](#RSA%20Algorithmus) ist multiplikativ homomorph, jedoch nicht additiv.

Zur Entschlüsselung wird der verschlüsselte Text $c$ [Modulo](Modulare%20Arithmetik.md#Modulo) $p$ verrechnet, der Effekt aus Zufalls- und Primzahl wird dadurch entfernt. 

$$
m = c \mod p
$$

## Beispiel Homomorph
Wir wählen die folgenden Werte
$$
\begin{array}{l l}
p &= 97 \\
r &= 48 \\
m_1 &= 5 \\
m_2 &= 2 \\
\end{array}
$$

Nach der Verschlüsselung ergeben sich die folgenden Chiffretexte.
$$
\begin{array}{l l l}
c_1 &= 5 + 97 \cdot 48 &= 4661 \\
c_2 &= 2 + 97 \cdot 48 &= 4658 \\
\end{array}
$$

Wir führen zwei Berechnungen mit den verschlüsselten Werten durch.
$$
\begin{array}{l l l}
e_1 &= c_1 + c_2 &= 4661 + 4658 &= 9.319 \\
e_2 &= c_1 \cdot c_2 &= 4661 \cdot 4658 &= 21.710.938 \\
\end{array}
$$
Die erwarteten Ergebnisse $5+2 = 7$ und $5 \cdot 2 = 10$ stimmen mit den entschlüsselten Berechnungen überein.
$$
\begin{array}{l r l}
m_1 =& 9.319 \mod 97&= 7 \\
m_2 =& 21.710.938 \mod 97 &= 10 \\
\end{array}
$$


# Kryptographische HASH-Funktionen
Eine Hash Funktion akzeptiert einen beliebigen Input und liefert einen Output fester Länge.
Eine gute Hash-Funktion hat einige Eigenschaften
- Unumkehrbarkeit
- Kollisionsfreiheit
- Geschwindigkeit

Es muss also schnell möglich sein, einen Hashwert zu berechnen. Gleichzeitig darf von einem Hashwert nicht auf die Eingabe geschlossen werden können.


> [!Info] Kollisionsfreiheit
> Da die Menge der Ausgaben auf eine feste Länge begrenzt ist, gibt es nur endlich viele Ausgabewerte.
> Da unendlich viele Werte eingegeben werden können, gibt es in jeder Hashfunktion mehrere Werte, die zur selben Ausgabe führen.
> Mit Kollisionsfreiheit ist daher gemeint, dass auch sehr ähnliche Eingaben stark verschiedene Ausgaben liefern. 

$$

$$
