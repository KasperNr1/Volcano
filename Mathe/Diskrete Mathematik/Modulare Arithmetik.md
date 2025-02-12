# Grundbegriffe 
Zwei ganze Zahlen heißen "kongruent modulo $m$ ", wenn sie bei Division durch $m$ den gleichen Rest haben.

**Beispiel** 
$a = b (mod \, m)$ 
$24 = 4 (mod \, 10)$ 

$\{19; 23; 27; 31; 35;...\}$ sind alle $(mod \, 4) =5$ 
Sie sind Teil einer __Restklasse__
Es gibt immer $m$ Restklassen bei Modulo $m$ 

## Satz
Wenn $a=b (mod\,m)$ und $c=d (mod\,m)$ dann gilt:
- $a+c=b+d (mod \, m)$
- $a * c=b * d (mod \, m)$
Dabei ist nicht erforderlich, dass $a$ und $c$ der gleichen Restklasse angehören.

# Anwendungen
1. [Hash](Hash.md)-Funktionen
2. Prüfziffern (ISBN, EAN, IBAN ...)
