![](SqlToRelationalAlgebra.png)

Die drei Varianten haben drastische Unterschiede in ihrer Performance. Bei Variante 1 wird aufgrund des JOIN mit großen Tabellen eine enorme Menge an Zwischenergebnissen generiert. 

In Variante 3 wird erst gefiltert bevor der JOIN stattfindet, so kann eine um mehrere Größenordnungen bessere Ausführung erreicht werden.

Das Optimieren von Anfragen ist also durchaus sinnvoll und lohnenswert.

![](SqlCompileToRuntimeFlow.png)

Die Reihenfolge der Operationen lassen sich als Baum darstellen.
Für die folgende Abfrage werden zwei solcher Pfade gezeigt.

```SQL
SELECT M.Name, F.Name FROM Mitarbeiter M, Filiale F
	WHERE 
		M.F_Nr = F.F_Nr 
	AND
		( M.Position = ‘Manager‘
	AND 
		F.Stadt = ‘Stuttgart‘);
```

![](SqlExecutionTree1.png)

Besser ist die folgende Ablaufreihenfolge.
![](SqlExecutionTree2.png)

Dabei kann ein Ausführungsbaum anhand einiger Umformungsregeln modifiziert werden.

# Transformationsregeln
Sei
- $R, S$ und $T$ Relationen
- $R$ Attribute $\{A_1, \dots, A_n\}$
- $S$ Attribute $\{B_1, \dots, B_m\}$
- $p,q$ und $r$ Prädikate
- $L, L_1, L_2, M, M_1, M_2$ und $N$ Attributmengen

## Regel 1
Konjunktive Selektionsoperationen können in einzelne Selektionen umgewandelt werden (und umgekehrt)
$$
\sigma_{p \wedge q \wedge r}(R) = \sigma_p(\sigma_q(\sigma_r(R)))
$$

## Regel 2
Selektionsoperationen sind kommutativ
$$
\sigma_q(\sigma_r(R)) = \sigma_r(\sigma_q(R)) 
$$

## Regel 3
In einer Reihe von Projektionen wird nur die letzte berücksichtigt.
$$
\Pi_L(\Pi_M(\dots(\Pi_N(R)))) = \Pi_L(R)
$$



## Regel 4
Selektionen und Projektionen sind kommutativ
$$
\Pi_{A_1, \dots, A_m}(\sigma_p(R)) = \sigma_p(\Pi_{A_1, \dots, A_m}(R))
$$

## Regel 5
(Theta-)Verbund und kartesisches Produkt sind kommutativ

## Regel 6
Selektion und (Theta-)Verbund  sind distributiv
Selektion und kartesisches Produkt sind distributiv

## Regel 7
Projektion und (Theta-)Verbund sind distributiv
Selektion und kartesisches Produkt sind distributiv

Wenn $L_1$ nur Attribute aus $R$ und $L_2$ nur Attribute aus $S$ umfasst, dann gilt:

En
> [!MISSING] Lange regel
> Contents


## Regel 8
Vereinigung und Schnitt sind kommutativ


> [!NOTE] Differenzoperator
> Der Differenzoperator ist nicht kommutativ


## Regel 9
Selektion und Mengenoperationen sind distributiv

## Regel 10
Projektion und Vereinigung sind distributiv

## Regel 11
(Theta-)Verbund und kartesisches Produkt sind assoziativ

## Regel 12
Vereinigung und Schnitt sind assoziativ

> [!NOTE] Differenzoperator
> Der Differenzoperator ist nicht assoziativ


# Heuristiken
## Heuristik 1
Splitte mehrfache Verbunde/Kartesische Produkte Auf
Es entsteht eine Folge einfacherer Operationen

[Regel 11](#Regel%2011)
## Heuristik 2
Splitte Konjunktive Selektionen in Einzelselektionen
Erlaubt großen Freiheitsgrad bei der Wahl des Ausführungszeitpunkts von Selektionen
[Regel 1](#Regel%201)

## Heuristik 3
Führe Selektionen so früh wie möglich aus.
Reduziert Größe der Zwischenresultate
[Regel 2](#Regel%202), [Regel 4](#Regel%204), [Regel 6](#Regel%206) und [Regel 9](#Regel%209)

## Heuristik 4
Durch [Heuristik 3](#Heuristik%203) ist die Selektion stets direkt vor einem Produkt.
Kombiniere diese Selektion mit dem Produkt als Prädikatsverbindung.


## Heuristik 5
Nutze Assoziativität der binären Operationen um restriktivere Operationen zuerst auszuführen

[Regel 11](#Regel%2011) und [Regel 12](#Regel%2012)

## Heuristik 6
Führe Projektionen so früh wie möglich aus.
Projektionen reduzieren das Volumen des Resultats


## Heuristik 7
Berechne gemeinsame Ausdrücke nur einmal

Caching soll verwendet werden falls Ergebnisse wiederverwendet werden.


> [!Example] Klausuraufgabe
> - Ausführungsbaum selber optimieren (Ganz oder Teilschritte)
>   Seite 8-31 bis 8-38
> - Vergleich mehrerer unterschiedlich optimierter Ausführungsbäume

Wenn die logischen Operationen angeordnet sind, kann noch deren technische Implementierung ausgewählt werden. 
Die Erstellung dieses idealen Ausführungsplans ist aber aufgrund der großen Menge an Aktionen unrealistisch.


Interessante Sortierreihenfolge:
Mindestens eine Bedingung erfüllt, nicht zwingend alle.
