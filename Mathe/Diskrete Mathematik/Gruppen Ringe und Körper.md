# Verschiedene Strukturen von Mengen
## Gruppe
Sei $G$ eine [Menge](Intervalle%20und%20Mengen.md) und $\circ$ eine Verknüpfung, die je zwei Elemente $a,b \in G$ ein Element $a \circ b \in G$ zugeordnet.
$(G,\circ)$ heißt "Gruppe" wenn gilt:
1. $(a \circ b) \circ c = a \circ (b \circ c)$ für alle $a,b,c \in G$ 
2. Es existiert ein neutrales Element $n \in G$ für das gilt:
   $n \circ a = a \circ n = a$ für alle $a \in G$ 
3. Zu jedem $a \in G$ existiert ein inverses Element $i(a) \in G$ für dass gilt:
   $a \circ i(a) = i(a) \circ a = n$ 
4. Gilt zusätzlich
   $a \circ b = b \circ a$ für alle $a,b \in G$ so heißt $(G, \circ)$ "kommutative Gruppe" bzw. "abelsche Gruppe"

## Feld
Eine Menge $G$ mit den Operatoren $+, \cdot : F\times F \to F$ wird Feld genannt, wenn die folgenden Bedingungen erfüllt sind:
1. $(F,+)$ ist eine [Kommutative Gruppe](#Gruppe), mit dem neutralen Element $0$
2. $(F,\cdot)$ ist eine [Kommutative Gruppe](#Gruppe), mit dem neutralen Element $1$
3. Distributivgesetz: $\forall a,b,c \in F: a \cdot (b+c) = a \cdot b + a \cdot c$


## Beispiele
### Verknüpfung: Addition
- $(\Bbb{Z}, +)$ ist eine kommutative Gruppe, denn
  1. $a+(b+c) = (a + b) + c$
  2. $n=0: \; a+0=0+a=a$ 
  3. $i(a) = -a: \; a+(-a) = (-a)+a = 0$
  4. $a+b = b+a$
- $(\Bbb{Z}_m, +)$ $m$ beliebig, $(\Bbb{Q},+); (\Bbb{R}, +)$ 
- $(\Bbb{N}_0,+)$ keine Gruppe, da inverse Elemente fehlen
- gerade Zahlen $h = \{2n \mid n \in \Bbb{Z}\} \subset \Bbb{Z}$ bilden eine Untergruppe $(h,+)$ von $(\Bbb{Z}, +)$ 
### Verknüpfung Multiplikation
- $(\Bbb{Q},*)$ ist eine komplexe Gruppe, da
  1. $a * (b * c) = (a * b) * c$
  2. $n=1: \; a * 1 = 1 * a = a$
  3. $i(a) = \dfrac1a: \;$ da $\dfrac1a * a = a * \dfrac1a = 1$ für $a \neq 0$ 
  4. $a * b = b * a$
- $(\Bbb{Z}_p \setminus \{0\}, *) p=$ Primzahl und $(\Bbb{R}\setminus , * )$ sind kommutative Gruppen
- $(\Bbb{N}, * )$ ist keine Gruppe, da keine Inversen Elemente existieren
  Bsp: $a=3 \quad i(a)=\frac13 \notin \Bbb{N}$ 

# Relationen
## Injektiv
Unterschiedliche Elemente werden durch die Abbildung auf unterschiedliche Abbildungselemente übertragen.
Es gilt:
$$
f(x) = f(y) \Longrightarrow x = y
$$
Keine zwei Eingaben teilen sich einen Output.
## Surjektiv
Jedes Element der Zieldomäne $B$ wird von mindestens einem transformierten Element der Ausgangsdomäne $A$ erreicht. Es gibt durch das Mapping keine unerreichbaren Punkte.
$$
\forall_{b \in B} \;\exists_{a \in A} \; f(a) = b
$$
## Bijektiv
Beschreibt das gleichzeitige Vorhandensein von [Injektivität](#Injektiv) und [Surjektivität](#Surjektiv).
Jedem Element beider Mengen ist exakt ein Element der jeweils anderen Menge zugeordnet.

Bijektivität garantiert die Existenz einer inversen Funktion $f^{-1}$.
Ebenfalls haben beide Domänen dieselbe Kardinalität / Größe.
