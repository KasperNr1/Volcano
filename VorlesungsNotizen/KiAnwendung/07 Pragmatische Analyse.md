# Pragmatik und Diskursanalyse
Bezieht sich auf das Studium der Sprache im Kontext. 

Pragmatische Analyse konzentriert sich auf kontextuelle Bedeutung.
Diskursanalyse untersucht Kontext in geschriebener und Gesprochener Sprache.

# Diskurs
Mehrere Sätze werden durch thematische Ähnlichkeit oder mithilfe von Konnektoren ("und", "aber", "weil", ...) verbunden. Idealerweise trägt jede Information zur Gesamtbedeutung des Textes bei.

> [!NOTE] Kohäsion
> Ist ein Maß mit dem gemessen werden kann, wie sehr Sätze innerhalb eines Textes zusammenhängen.

## Monolog
Einweg-Kommunikation zwischen einem Sprecher / Schreiber und einem Publikum.

# Dialog
Teilnehmer wechseln zwischen den Rollen "Sprecher" und "Publikum".
Erfordert mindestens zwei Teilnehmer.
- Mensch zu Mensch: Tägliche Gespräche
- Mensch zu Computer (HCI): Interaktion mit Chatbots
- Computer zu Computer (CCI)

## Diskursphenomäne
Werden von Menschen durch Kontext und Weltwissen oft natürlich gelöst.
Besonders die "[Koreferenzauflösung](#Koreferenzauflösung)" ist für Maschinen sehr schwierig.

### Koreferenzauflösung
Identifikation linguistischer Ausdrücke, die einer realen Entität im Text entsprechen. Erwähnungen werden durch korrekte Pronomen und Nominalphrasen ersetzt.

1. "Jack saw Andrew in the examination hall. He looked nervous."
2.  "Jack saw the student in the examination hall. He looked nervous."

Im ersten Satz wird "he" eher auf Andrew bezogen, im zweiten eher auf den Student.


> [!Quote] Beispiel
> Standardsituation der Koreferenzauflösung
> 
> Original:
> "Jack gives Ian 1000 Dollars. He is generous"
> 
> Aufgelöst:
> "Jack gives Ian 1000 Dollars. Jack is generous"

### Weitere Phänomene
- Kataphor
  Verweis eines Ausdrucks auf eine erst später auftretende Instanz
  "Wenn $\boxed{\text{er}}$ kommt, wird $\boxed{\text{Peter}}$  glücklich sein"
- Antezedens oder Referent
  Verweis auf eine zuvor genannte Instanz.
  "$\boxed{\text{Peter}}$ wird glücklich sein, wenn $\boxed{\text{er}}$ kommt"
- Anapher
  Wiederholung eines Ausdrucks am Anfang aufeinanderfolgender Sätze
  "$\boxed{\text{Peter}}$ ist glücklich. $\boxed{\text{Peter}}$ hat einen Hund."

# Kohärenz
Bezieht sich auf die Bedeutungsbeziehungen zwischen einzelnen Einheiten, wie Sätzen oder Aussagen.
[Koreferenz](#Koreferenzauflösung) und Kohärenz sind eng miteinander verbunden. Beide Konzepte trage dazu bei, dass Texte und Diskurse logisch und angenehm zu lesen sind.

## Entity-basierte Kohärenzmodelle
Kohärenz wird gemessen, indem zentrale Entitäten über Äußerungen hinweg verfolgt werden.

1. Helen ging zum Supermarkt, um ein Cello zu kaufen.
2. Sie hatte den Laden schon lange besucht.
3. Sie war erfreut, endlich das Cello zu kaufen.
4. Sie stellte gerade fest, dass der Laden geschlossen ist.
5. Es war der Laden, den Helen schon lange besucht hatte.
6. Sie war erfreut, dieses Cello zu kaufen.
7. Der Klang, des es erzeugt, ist wunderschön.
8. Es war geschlossen, als Helen ankam.

Die zentrale Entität (CE) beginnt in 1-4 bei Hellen, wechselt dann vom Supermarkt zum Cello, bis sie in 8. wieder beim Laden endet.

# Diskurssegmentierung
## Definition
Bestimmung der kleinsten, nicht überlappenden Diskurseinheiten, auch "Elementare Diskurseinheiten" (EDUs)

Kategorien:
- Satzsegmentierung
- Satzebenen-Diskurssegmentierung
## Ziel
Unterteilung eines Dokuments in eine Liste von Unterthemen.

## Methoden
- [Unüberwachte Methoden](08%20Unüberwachtes%20Lernen.md)
- [Überwachte Methoden](01%20Grundidee.md#^cf5d0b)
### Unüberwachte Diskurssegmentierung
Lineare Segmentierung von Rohdaten. 

> [!NOTE] Was heißt Linear?
> Bedeutet, dass der Text in Blöcke zerteilt wird, die ein Label erhalten. Es werden nicht einzelne Sätze zu zusammenhängenden Blöcken gefasst.

Ein Kohäsionsbasierter Ansatz teilt den Text in Unterthemen. Beispiel für ein solches Verfahren ist "[TextTiling](#TextTiling)" von Marti Hearst.

#### TextTiling
Basiert auf der Idee, dass längere Texte in kleinere, kohärente Abschnitte unterteilt werden können.

Dabei geht der Algorithmus davon aus, dass sich das verwendete Vokabular zwischen Absätzen deutlich ändert.

Die Verteilung ausgewählter Begriffe über den Text wird betrachtet. Dabei werden Füllwörter entfernt um eine aussagekräftige Verteilung zu erhalten.
![](TextTiling.png)

1. Der Text wird in Tokens unterteilt
	1. Entfernen von Stoppwörtern
	2. [Lemmatisierung](02%20N-Gramm.md#Lemma) der Wörter
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

# Überwachte Diskurssegmentierung
Verwendet unterschiedliche Modelle wie [Support Vector Machines](05%20SVM.md#Support%20Vector%20Machines), [Naiver Bayes](04%20Wälder.md#Naiver%20Bayes) oder andere um zu bestimmen ob Satzgrenzen auch Absatzgrenzen sind.

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

### Hobbs-Ablauf
1. Startpunkt:
   Beginne mit dem Knoten der [Nominalphrase (NP)](04%20Syntax.md#Nominalphrasen)  die das Pronomen direkt dominiert
2. Aufwärtsbewegung:
   Gehe den Baum hinauf zum ersten besuchten NP- oder Satzknoten (S), benenne diesen Knoten als $X$ und den Weg dorthin als $p$
3. Seitliche Suche:
   Besuche alle Äste unter Knoten $X$ links von Pfad $p$, von links nach rechts und betrachte jeden gefundenen NP-Knoten als [Antezendens](#Weitere%20Phänomene), wenn dazwischen ein NP- oder S-Knoten liegt.
4. Satzübergreifende Suche:
   Wenn $X$ der höchste S-Knoten im Satz ist, besuche die Parsbäume vorheriger Sätze, beginnend mit dem neuesten, von links nach rechts und in Breite. Empfohlene NP-Knoten werden als Antezedens betrachtet
5. Weiteres Aufsteigen:
   Steige weiter von Knoten $X$ zum ersten NP- oder S-Knote auf und benenne diesen neuen Knoten als $X$
6. NP-Überprüfung:
   Wenn $X$ ein NP-Knoten ist, und der Pfad $p$ nicht durch einen nominalen Knoten direkt unter $X$ verläuft, wird $X$ als Antezedens bezeichnet
7. Breitensuche:
   Besuche alle Äste unter Knoten $X$ links von $p$, von links nach rechts und betrachte jeden NP-Knoten als Antezedens
8. Rechte Suche bei S:
   Besuche alle Äste von Knoten $X$ rechts von Pfad $p$, von links nach rechts, aber gehe nihct unter NP- oder S-Kntoen die als Antezedens betrachtet werden
9. Wiederholung:
   Gehe zu Schritt 4 zurück

### Hobbs-Beispiel
Im folgenden Beispiel wird der Ablauf veranschaulicht. Im Satz `"The castle in Camelot remained the residence of the king until 536 when he moved it to London"` wird das `it` am Ende des Satzes aufgelöst.

1. Start
   Beginne bei $NP_1$, gehe in Schritt 2 zu $S_1$ hoch
2. Seitliche Suche
   Die linke Seite von S1 wird durchsucht, findet jedoch keine geeigneten NP-Knoten
3. Satzübergreifende Suche:
   Nicht Anwendbar
4. Weiteres Aufsteigen:
   Gehe zu $NP_2$ das in Schritt 6 '536' als Antezedens von 'it' vorschlägt.
5. Verbesserung durch Einschränkungen:
   Daten können sich nicht bewegen; Große oder feste Objekte können sich nicht bewegen.
6. Ablehnung von $NP_2$:
   Schritte 7 und 8 finden nichts, Kontrolle kehrt zu Schritt 4 zurück
7. Weiteres Aufsteigen zu $S_2$
   Schritt 6 ist nicht anwendbar
8. Breitensuche
   $NP_3$ 'the castle' wird aufgrund der Einschränkung in 5. abgelehnt
9. Weiter zu $NP_4$
   Empfiehlt korrekt "the residence" als Antezedens

![](HobbsAlgorithmExample.png)

Der Algorithmus berücksichtigt keine [Diskurssegmentierung](#Diskurssegmentierung), somit werden gelegentlich auch weit zurückliegende Textstellen vorgeschlagen.
Mit einer Genauigkeit von $ca. 72\%$ ist der Ansatz ein wichtiger Benchmark in der Forschung.

## Centering-Algorithmus
Die Grammatikalische Rollenhierarchie ordnet syntaktische Funktionen nach ihrer Wichtigkeit im Satz.

![](GrammaticalHierarchy.png)

Der Algorithmus basiert auf der Annahme, dass jeder Diskurs einen zentralen Fokus besitzt. Dieses bleibt über mehrere Sätze hinweg konstant, bevor es wechselt.

Dieses Zentrum ist oft der Bezugspunkt der Pronomen oder Referenzen. Dabei können einige Zentren in der Zukunft und in der Vergangenheit liegen.

### Centering-Ablauf
Der Algorithmus besteht aus drei Teilen:
- Anfangseinstellungen
- Einschränkungen
- Regeln und Algorithmus

#### Anfangseinstellungen
Seien $U_n, U_{n+1}$ zwei aufeinanderfolgende Äußerungen. 
Das rückblickende Zentrum von $U_n$, geschrieben als $C_b(U_n)$ bezeichnet den Fokus nach der Interpretation von $U_n$.
Vorausblickende Zentren von $U_n$, geschrieben als $C_f(U_n)$ bilden eine geordnete Liste von Entitäten in $U_n$, die als $C_b(U_{n+1})$ dienen können.
$C_b(U_{n+1})$ ist das höchstrangige Element von $C_f(U_n)$, das in $U_{n+1}$ erwähnt wird.
Reihenfolge der Entitäten in $C_f(U_n)$: Subjekt > Existenzprädikat Nominal > Objekt > indirektes Objekt > abgrenzende adverbiale Präpositionalphrase
Sei $C_p(U_{n+1})$ das höchstrangige vorausblickende Zentrum.

#### Einschränkungen
Für jede Äußerung $U_i$ mit $i = 1 \ldots m$ in einem Diskurssegment $D$:
- Es gibt genau ein $C_b$
- Jedes Element der $C_f$-Liste für $U_i$ muss in $U_i$ realisiert werden, d.h. es muss dort explizit erwähnt oder referenziert werden.
- Das Zentrum $C_b(U_i,D)$ ist das höchstrangige Element von $C_f(U_{i-1}, D)$, das durch $U_i$ realisiert wird.

#### Algorithmus
Für jede Äußerung $U_i$ mit $i = 1 \ldots m$ in einem Diskurssegment $D$:
- Regel 1:
  Wenn einige Elemente von $C_f(U_{i-1}, D)$ als Pronomen in $U_i$ realisiert werdren, dann auch $C_b(U_i, D)$ 
- Regel 2:
  Übergangszustände sind so geordnet, dass die Abfolge von `Continue` über `Retains`, `Smooth-Shift` und `Rough-Shift` bevorzugt wird.

Die Beziehungen zwischen $C_b$ und $C_p$ zweier Äußerungen bestimmt die Kohärenz zwischen zwei Worten. Die Centering Theory stuft die Kohärenz benachbarter Äußerungen mit Übergängen, die durch folgende Kriterien bestimmt werden:
- $C_b$ bleibt von $U_{n-1}$ zu $U_n$ gleich oder nicht
- Diese Entität stimmt mit dem höchstrangigen vorausblickenden Zentrum $C_p$ von $U_n$ überein oder nicht


Die folgende Übergangstabelle beschreibt die Handlungen in den möglichen Situationen

|                                  | $C_b(U_{n+1}) = C_b(U_n) \; \text{OR} \; \text{undefined} \; C_b(U_n)$ | $C_b(U_{n+1}) \neq C_b(U_n)$ |
| -------------------------------- | ---------------------------------------------------------------------- | ---------------------------- |
| $C_b(U_{n+1}) = C_p(U_{n+1})$    | Continue                                                               | Smooth-Shift                 |
| $C_b(U_{n+1}) \neq C_p(U_{n+1})$ | Retain                                                                 | Rough-Shift                  |

Der Algorithmus, basierend auf diesen Regeln und Bedingungen wird wie folgt definiert:
1. Erstelle alle möglichen $C_b - C_f$ Kombinationen
2. Filtere diese Kombinationen durch Einschränkungen und Centering-Regeln
3. Ranke verbleibende Kombinationen nach Übergängen


### Centering-Beispiel
Betrachtet werden folgende Sätze:
- $U_1$: Jane heard some beautiful music at the CD Store
- $U_2$: She played it to Mary
- $U_3$: She bought it

Die Zentren für $U_1$ sind entsprechend:
- $C_f(U_1)$: {Jane, music, CD Store}
- $C_p(U_1)$: Jane
- $C_b(U_1)$: Undefined

$U_2$ hat zwei Pronomen: "She" und "it". "She" ist syntaktisch nur mit "Jane" kompatibel, "It" nur mit "Music" oder "CD-Store".
Wenn "It" auf "Music" bezogen wird, lautet das Ergebnis:
- $C_f(U_2)$: {Jane, music, Mary}
- $C_p(U_2)$: Jane
- $C_b(U_2)$: Jane
$\to$ `Continue`, da $C_p(U_2) = C_b(U_2)$ und $C_b(U_1)$ nicht definiert ist.

Wenn "it" auf "CD Store" bezogen wird ändert sich  $C_f(U_2)$
- $C_f(U_2)$: {Jane, CD Store, Mary}
- $C_p(U_2)$: Jane
- $C_b(U_2)$: Jane
$\to$ `Continue`, da $C_p(U_2) = C_b(U_2)$ und $C_b(U_1)$ nicht definiert ist.

Da beide auf `Continue` abbilden, wird auf "music" statt auf "CD Store" verwiesen.

Nun wird $U_3$ betrachtet:
"She" ist entweder mit "Jane" oder "Mary" kompatibel, während "it" mit "music" kompatibel ist.
Wenn "She" sich auf "Mary" bezieht ($C_p(U_3) = \text{Mary}$) lautet das Ergebnis:
- $C_f(U_3)$: {Mary, music}
- $C_p(U_3)$: Mary
- $C_b(U_3)$: Mary
Ergebnis ist `Smooth-Shift` da $C_p(U_3) = C_b(U_3)$ aber $C_b(U_3) \neq C_b(U_2))$ 

Da  `Continue` gemäß [Regel 2](#Algorithmus) gegenüber `Smooth-Shift` bevorzugt wird, sollte "Jane" als Referent zugewiesen werden, sodass der Centering-Algorithmus in dieser Situation funktioniert.

## Log-Lineares Modell
Ist ein [Klassifikationsmodell](01%20Grundidee.md#Klassifikation) um Paaren von Pronomen und Entitäten (Antezedenspaaren) vorherzusagen, ob sie koreferieren (1) oder nicht (0)

Berücksichtigt die grammatikalischen Rollen, Satzdistanz, Geschlechts- und Zahlübereinstimmungen.
Das Modell bietet eine Datengetriebene Methode zur Verbesserung der Genauigkeit bei der Bestimmung von Pronomenreferenzen.
