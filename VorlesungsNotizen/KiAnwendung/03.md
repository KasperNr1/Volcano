# Part Of Speech
Auch "Wortarten".
Wörter derselben Part of Speech zeigen ähnliche Syntaktische Rollen in Sätzen.

## Morphologische Eigenschaften
[Part Of Speech](#Part%20Of%20Speech)-Wörter werden durch dieselben grammatikalischen Regeln verändert

## Flexion
Ist ein Prozess der Wortbildung. Zur Grundform eines Worts werden bestimmte Endungen hinzugefügt um grammatische Bedeutung zu vermitteln.

Beispiel
- "-s" im Englischen zeigt Plural an
- "gets" zeigt dritte Person Singular

## Verwendung in NLU
Die [Part Of Speech](#Part%20Of%20Speech) ist wichtig zur Kategorisierung und Verwendung von Wortarten.

Auch automatische Übersetzung benötigt die Information. Beispielsweise könnte das Englische "run" sonst nicht unterschieden werden. Es kann "der Lauf" oder "rennen" bedeuteten.

Auch die Betonung bei der Aussprache kann sich unterscheiden.
Bsp.
- PERfect (Adjektiv)
- perFECT (Verb)

- umFAHREN
- UMfahren


## PoS Tagging
Part of Speech Tagging ist die Zuordnung von Wörtern zu ihren Wortarten.
Eine einfache Version wird häufig im Schulunterricht erlernt.

![](PosTagging.png)

Die "Penn Treebank PoS Tags" sind eine Sammlung an Tags um Sprache in 45 Tags klassifizieren zu können.

# Automatisches Tagging
Kann Regelbasiert passieren oder Stochastisch durch machine Learning.

## Regelbasiert
Regeln können manuell definiert werden, oder auch aus einem [Korpus](02%20N-Gramm.md#Korpuslinguistik) abgeleitet werden.
Manuelle Erstellung liefert verständlichere und besser Erklärbare Regeln, ist aber sehr arbeitsintensiv.

## Stochastisch
Der HMM (Hidden Markov Model) arbeitet mit [N-Gramm Häufigkeiten](02%20N-Gramm.md#N-Gramm%20Modell) und maximiert die Wahrscheinlichkeit, dass ein aktuelles Tag im aktuellen Kontext zum aktuellen Wort passt.

## Hybrid
Mit "Brill Taggern" werden beide Ansätze kombiniert.

1. Initiales Tagging anhand von einem einfachem Lexikon
2. Regelgenerierung, es werden häufige Fehler mit Regeln korrigiert die manuell erstellt sind oder aus dem Korpus gelernt wurden.
3. Transformation:
   Spezifische Anpassung zur Fehlerkorrektur
4. Iterative Verfeinerung

## Evaluation von Taggern
- Angemessenheit bewerten
- Ursprung von Fehlern identifizieren
- Häufige Fehler werden mit [Konfusionsmatrix](04%20Wälder.md#Konfusionsmatrix) erkannt
- 