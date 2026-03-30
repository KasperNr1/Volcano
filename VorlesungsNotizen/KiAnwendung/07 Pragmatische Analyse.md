# Pragmatik und Diskursanalyse
Bezieht sich auf das Studium der Sprache im Kontext. 

Pragmatische Analyse konzentriert sich auf kontextuelle Bedeutung.
Diskursanalyse untersucht Kontext in geschriebener und Gesprochener Sprache.

# Diskurs
## Monolog
Einweg-Kommunikation zwischen einem Sprecher / Schreiber und einem Publikum.

# Dialog
Teilnehmer wechseln zwischen den Rollen "Sprecher" und "Publikum".
Erfordert mindestens zwei Teilnehmer.

## Diskursphenomäne
Werden von Menschen durch Kontext und Weltwissen oft natürlich gelöst.
Besonders die "Koreferenzauflösung" ist für Maschinen sehr schwierig.

### Koreferenzauflösung
- Identifikation linguistischer Ausdrücke, die einer realen Entität im Text entsprechen
- Erwähnungen werden durch korrekte Pronomen und Nominalphrasen ersetzt.

Beispiele:
"Jack saw Andrew in the examination hall. He looked nervous."
"Jack saw the student in the examination hall. He looked nervous."

Im ersten Satz wird "he" eher auf Andrew bezogen, im zweiten eher auf den Student.


> [!Example] Beispiel
> Standardsituation der Koreferenzauflösung
> 
> Original:
> "Jack gives Ian 1000 Dollars. He is generous"
> 
> Aufgelöst:
> "Jack gives Ian 1000 Dollars. Jack is generous"

### Weitere Phenomäne
Auf Seite 329 im Skript
- Kataphor
- Antezedens oder Referent
- Anapher


> [!NOTE] Kohäsion
> Konnektoren wie "und", "weil", "aber" verbinden Sätze und Absätze.
> Alle Teile des Diskurses sind (typischerweise) auf ein Thema ausgerichtet. Jede Information trägt teilweise zur Gesamtbedeutung bei.

# Kohärenz
Bezieht sich auf die Bedeutungsbeziehungen zwischen einzelnen Einheiten, wie Sätzen oder Aussagen.
[Koreferenz](#Koreferenzauflösung) und Kohärenz sind eng miteinander verbunden. Beide Konzepte trage dazu bei, dass Texte und Diskurse logisch und angenehm zu lesen sind.

## Entity-basierte Kohärenzmodelle
Kohärenz wird gemessen, indem zentrale Entitäten über Äußerungen hinweg verfolgt werden.


# Diskurssegmentierung
## Definition
Bestimmung der kleinsten, nicht überlappenden Diskurseinheiten, auch "Elementare Diskurseinheiten" (EDUs)

Kategorien:
- Satzsegmentierung
- Satzebenen-Diskurssegmentierung
## Ziel
Unterteilung eines Dokuments in eine Liste von Unterthemen.

## Methoden
- Unüberwachte Methoden
- Überwachte Methoden
### Unüberwachte Diskurssegmentierung
Lineare Segmentierung von Rohdaten. 

> [!NOTE] Was heißt Linear?
> Bedeutet, dass der Text in Blöcke zerteilt wird, die ein Label erhalten. Es werden nicht einzelne Sätze zu zusammenhängenden Blöcken gefasst.

Ein Kohäsionsbasierter Ansatz teilt den Text in Unterthemen. Beispiel für ein solches Verfahren ist "TextTiling" von Marti Hearst.

#### TextTiling
Basiert auf der Idee, dass längere Texte in kleinere, kohärente Abschnitte unterteilt werden können.

Dabei geht der Algorithmus davon aus, dass sich das verwendete Vokabular zwischen Absätzen deutlich ändert.

Die Verteilung ausgewählter Begriffe über den Text wird betrachtet. Dabei werden Füllwörter entfernt um eine aussagekräftige Verteilung zu erhalten.
![](TextTiling.png)

1. Der Text wird in Tokens unterteilt
	1. Entfernen von Stoppwörtern
	2. Lemmatisierung der Wörter
	3. Aufteilung in "Pseudo Sätze" (Gruppen von tokens mit fester Größe)
2. Berechnung der Wortfrequenz
	1. Für jedes Token wird die Häufigkeit im Pseudosatz bestimmt.
3. Berechnung der Ähnlichkeit
	1. Wortfrequenzen in Pseudosätzen werden als Vektoren verwendet.
	2. Verwendung von Kosinusähnlichkeit zwischen benachbarten Pseudosätzen
4. Ähnlichkeitsanalyse
	1. Ähnlichkeit benachbarter Themen wird bestimmt.
![](SimilarityDetection.png)

Stellen mit besonders niedriger Ähnlichkeit werden als Grenzen zwischen verschiedenen Themen erkannt.


## Anwendungen
- Informationsextraktion / -Abruf
- Textzusammenfassung für jedes Segment

# Rhetorische Strukturtheorie
Eine Theorie zur Organisation von Texten. Erklärt wie Teile eines Textes miteinander in Beziehung stehen. 

# Verweisende Ausdrücke
Nominalphrasen: "Die Präsidentin" "Das rote Auto"
Pronomina: "Er", "sie" "jener"
Eindeutige Identifikatoren: "Linonel Messi" "Berlin" "ISBN 0815-1234-5678"
Titel / Rollen: "Der Bürgermeister"
Demonstrativa: "Diese Theorie" "Jene Ergebnisse"

# Kohärenzrelationen
Beziehen sich auf die Eigenschaften eines Diskurses, die es ermöglichen, dass dieser im Kontext als sinnvoll oder zusammenhängend wahrgenommen wird.

Es gibt dabei fünf Haupttypen von Relationen:
- Parallelbeziehung
- Ausarbeitungsbeziehung
- Ursache und Wirkung
- Kontrastbeziehung
- Gelegenheitsbeziehung

## Parallelbeziehung
Beispiel:
"Rich man wants more power. Poor man wants more food"

## Ausarbeitungsbeziehung
Beispiel:
"Dorothy was from Kansas. She lived in the great Kansas prairies"

## Ursache und Wirkung
Beispiel:
"Jack cannot afford to buy a car. He lost his Job"

## Kontrast
Beispiel:
"Hope for the best. Prepare for the worst."

## Gelegenheit
Beispiel:
"Jack failed in the exam. He started to work hard."

---

Diskurskohärenz kann auch durch die Hierarchie zwischen Kohärenzrelationen verdeutlicht werden.

1. Jack went to town to buy a toy
2. He took a bus to the shopping mall
3. He needed to buy a toy for his child
4. It is Jane's Birthday
5. He also wanted to buy some books for weekend reading

![](RelationHierarchy.png)

# Interpretation von Pronomen
Es gibt sechs grundlegende Prinzipien von denen die Interpretation eines Pronomens beeinflusst wird.

![](PronomenInterpretation.png)

# Algorithmen zur Koreferenzauflösung
Englisch: "Coreference Resolution (CR)"
hat die Aufgabe, alle sprachlichen Verweise und Erwähnung auf Entitäten aufzulösen.

Verbreitet sind drei Algorithmen:
- Hobbs-Algorithm
- Centering-Algorithmus 
- Log-lineares Modell

## Hobbs Algorithmus
Gilt heute als Benchmark und ist in zwei Varianten verfügbar.

Verwendet nur Parsbaum und Grammatikregeln, somit ist kein Diskursmodell erforderlich.


> [!Missing] Genaue Beschreibung fehlt
> Seite 383-386 im Skript

## Centering-Algorithmus
Die Grammatikalische Rollenhierarchie ordnet syntaktische Funktionen nach ihrer Wichtigkeit im Satz.

![](GrammaticalHierarchy.png)

Der Algorithmus basiert auf der Annahme, dass jeder Diskurs einen zentralen Fokus besitzt. Dieses bleibt über mehrere Sätze hinweg konstant, bevor es wechselt.

Dieses Zentrum ist oft der Bezugspunkt der Pronomen oder Referenzen. Dabei können einige Zentren in der Zukunft und in der Vergangenheit liegen.


> [!Missing] Genaue Beschreibung
> Seite 390-399


## Log-Lineares Modell
Seite 402-403


