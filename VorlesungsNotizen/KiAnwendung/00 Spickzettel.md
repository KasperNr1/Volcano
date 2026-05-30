## Typen
Bezeichnet die [Menge](Intervalle%20und%20Mengen.md) der einzigartigen Wörter in einem Korpus, unabhängig wie oft sie tatsächlich vorkommen.

> [!Info] Unterschied [Stamm](#Stamm) und [Lemma](#Lemma)
> ![](StemmingVsLemma.jpeg)

> [!Example] Klausuraufgabe
> Satz in Fragmente spalten.
> Beachte Beispiel für 2. und 3. :
> manche Tokens werden. mehrfach gezählt um stets vollständige Fragmente zu erhalten.
> z.B. "Ist ein" bei Trigramm


# Language Model Evaluation
Bei der intrinsischen Bewertung wird die Leistung des Modells automatisch bestimmt, anhand verschiedener linguistischer oder statistischer Merkmale.
Extrinsische Evaluation erfolgt anhand der Qualität von Übersetzungen oder anderen Arbeiten durch Menschen oder [LLMs](10%20LLMs.md).
$$
\text{Perplexity} = 2^{-\frac{1}{N} \sum_{i=1}^{N} \log_2 \left(P(w_i)\right)}
$$
Seien für den Satz "Der Hund bellt" die Worte mit einer Wahrscheinlichkeit von $0.3; 0.4; 0.2$ vorhergesagt worden, so ist die Perplexity:
$$
\text{Perplexity} = 2^{-\frac{1}{3}\left( \log_2 0.3 + \log_2 0.4 + \log_2 0.2 \right)} \approx 3.4668
$$

Mit diesem Wert können Modelle relativ zueinander verglichen werden.

# Part Of Speech
Auch "Wortarten".
Wörter derselben Part of Speech zeigen ähnliche Syntaktische Rollen in Sätzen.

## PoS Tagging
Part of Speech Tagging ist die Zuordnung von Wörtern zu ihren Wortarten.

![](PosTagging.png)

Die "Penn Treebank PoS Tags" ist eine Sammlung an Tags. Mit ihr kann Sprache in 45 Tags klassifiziert werden.

![](PennTreebankPosTags.png)

# Automatisches Tagging
## Stochastisch
Der HMM (Hidden Markov Model) arbeitet mit [N-Gramm Häufigkeiten](02%20N-Gramm.md#N-Gramm%20Modell) und maximiert die Wahrscheinlichkeit $P(t_i \mid w_i)$, dass ein aktuelles Tag im aktuellen Kontext zum aktuellen Wort passt.

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

![](PosTagsConfusionMatrix.png)

Die Matrix ist groß, da viele Tags vergeben werden können, es wird jeweils die Rate eingetragen mit der ein Paar an Tags verwechselt wird.
So können Fehler präzise erkannt und gezielt ausgebessert werden.

# Definition: Syntax
Die Anordnung von Wortarten ([Part Of Speech](03%20PartOfSpeech.md#Part%20Of%20Speech)) folgt typischerweise festen Mustern.
![](SyntaxPatterns.png)
![](SyntaxPatterns2.png)

# Satzglieder
Satzglieder können durch hinzufügen verschiedener Details länger oder kürzer werden.
- "$\boxed{\text{The cat with orange fur}}$ is playing"
- "$\boxed{\text{It}}$ is playing"
## Nominalphrasen
Bestehen nur aus einem Nomen und seinen Begleitern
- "The big house"
- "A beautiful garden"
- "Robert"
## Verbalphrasen
Sind Phrasen die ein Verb in einer beliebigen Form enthalten.
Im Englischen gibt es neun häufige Typen von Verbalphrasen.
![](Verbalphrasen.png)
![](VerbalphrasenSubcategories.png)

# Chomsky Hierarchie
0. Rekursiv aufzählbare Sprachen
   Von Turingmaschine akzeptiert
1. Kontext-sensitive Sprachen
   Von Linear beschränkten Turingmaschine akzeptiert
2. Kontextfreie Sprachen
   Von Kellerautomaten akzeptiert
3. Reguläre Sprachen
   Von deterministisch endlichen Automaten akzeptiert

Die natürlichen Sprachen können mit Kategorie 2, den Kontextfreien Sprachen abgebildet werden. Dabei sind die Terminalsymbole $T$ die [PoS Tags](03%20PartOfSpeech.md#PoS%20Tagging) und die Nicht-terminale $N$ sind u.A. die verschiedenen [Satzglieder](#Satzglieder) und deren Unterklassen.
# Probabilistisches Parsing
In einer Probabilistischen, kontextfreien Grammatik (PCFG) hat jede Produktionsregel die Form $A \to \beta[p]$.
Dabei gibt $p$ die Wahrscheinlichkeit an, dass $a \to \beta$ verwendet wird.

Die Summe der Wahrscheinlichkeiten für alle Produktionsregeln aus $A$ muss $1$ ergeben. Exakte Werte für die Produktionsregeln können aus dem Korpus ermittelt werden.

![](ProbabilisticParsing.png)
## Limits
“I ate Pizza with olives" und "I ate Pizza with friends" sind grammatikalisch sehr ähnlich, wobei Oliven als Zutat und Freunde als Begleitung interpretiert werden sollten. Diese Abhängigkeit wird ignoriert, die Bäume werden nur nach den Häufigkeiten im Korpus gebildet.

Dabei ist die Bedeutung oft eine andere als die bloße Summe der einzelnen Wörter.
“Jemandem einen Bären aufbinden"

# Typen von Bedeutungsrepräsentation
Es gibt fünf Typen von Bedeutung
1. Kategorien
   Spezifische Objekte oder Entitäten
   Firmennamen, Standorte oder Gegenstände
2. Ereignisse
   Handlungen oder erlebte Phänomene
   'einen Film ansehen'
3. Zeit
   Genaue oder Referenzzeitpunkte
   Nächste Woche, 9:30 Uhr
4. Aspekte
   Darstellen von Fakten oder Beschreiben von Aktionen
   'Jane läuft', 'Das Buch ist interessant'
5. Überzeugungen / Wünsche und Absichten
   'Ich halte deine Aussage für realistisch'

# Semantische Verarbeitung
Unterschiedliche Fragen benötigen für eine sinnvolle Antwort eine große Menge an Semantischer Verarbeitung.
Bei korrekter Umsetzung kann ein System auch Schlussfolgerungen aus Wissen ziehen um unbekannte Aussagen zu bewerten.
`If John is in the classroom, and Mary is sitting next to him, then Mary is also in the Classroom`

## Kenntnis eines Konzepts
“What is the Meaning of NLP"

## Hintergrundwissen eines Konzepts
“How does the N-gram model work"

## Kenntnis eines Konzepts und unterschiedliche Relevanz zu verschiedenen Zeitpunkten
“Does the Turing Test still exist"

## Einbindung von Weltwissen neben Informationen zum Subjekt
“Why do we need to study self-awareness in AI"

## Wissen um Umstände des Nutzers neben Welt- und Faktenwissen
“Should I study AI"

# Darstellung von Bedeutung
Um eine effektive Repräsentation zu gewährleisten müsse drei Faktoren erfüllt sein.
- Verifizierbarkeit
  Aussagen können durch Vergleiche mit anderem Weltwissen oder durch logische Schlussfolgerungen als Wahr oder Falsch erkannt werden.
- Umgang mit Mehrdeutigkeit
  Die Fähigkeit die richtige der möglichen Bedeutungen zu erkennen.
- Vagheitsüberlegungen
  Manche Begriffe wie 'groß' haben keine klaren Grenzen. In unterschiedlichen Situationen kann die selbe Länge groß und klein sein.

## FOPL
Die Aussage "Jack fährt einen Mercedes" lässt sich mittels Prädikatenlogik wie folgt darstellen
$$\exists y (Person(Jack) \wedge Fährt(Jack, y) \wedge Auto(y) \wedge Marke(y, Mercedes)) $$


## Semantische Netzwerke
![](SemanticNetwork.png)

## Konzeptuelles Abhängigkeitsdiagramm
![](ConceptualDependencyDiagram.png)

## Frame-Based Representation
![](FrameBasedRepresentation.png)


# Kanonische Form
Eine kanonische Form bezieht sich auf eindeutig identifizierbare Objekte, die auf mehr als eine Weise dargestellt werden können. 
Eine dieser Möglichkeiten wird als die bevorzugte (kanonische) Standard-Form (wie bei [digitaltechnischen Schaltungen](DigitaltechnischeBegriffe.md#Normalform)) bezeichnet.

In der Sprachverarbeitung können verschiedene Sätze mit identischer Bedeutung somit auch in einer Standardform gespeichert werden.
- Jack eats KitKat
- KitKat is what Jack eats
- What Jack eats is KitKat
# Schlussfolgerungen
## Inferenz
Das Ableiten von neuen Erkenntnissen aus vorhandenen Informationen.

Teilt sich in [Deduktion](#Deduktion) und [Induktion](#Induktion).

Eine Inferenz ist im Allgemeinen gültig, wenn sie durch korrekte Schlussfolgerungen logisch aus Beweisen abgeleitet wird.
# Kasusgrammatik
Die gleiche Bedeutung kann in unterschiedlichen Sprachen mit verschieden Strukturen und Wörtern codiert werden.
Die Kasusgrammatik ist ein System das die Beziehungen zwischen Subjekten, Objekten und der [Valenz](#Valenz) von Verben analysiert.

Die Grundlegenden Rollen einer Aussage bleiben gleich, unabhängig von der Sprache die verwendet wird um diese Information auszudrücken. Man spricht auch von [Semantischen Rollen](#Semantische%20Rollen).

## Valenz
Verben verlangen eine unterschiedliche Anzahl von Argumenten oder Satzteilen.
## Kasusrollen
Laut Fillmores Theorie gibt es sechs Hauptrollen
- Agent: Absichtlich Handelnder
- Experiencer: Der Handelnde ohne Absicht
- Theme: Das Objekt, das eine Veränderung erfährt
- Instrument: Das Werkzeug mit dem die Handlung ausgeführt wird
- Beneficiary: Person oder Objekt für die eine Handlung ausgeführt wird
- To/At/From Loc/Poss/Time: Bezieht sich auf den Besitz von Dingen, Orten oder Zeiten

### Komplikationen
Eine Syntaxeinheit kann mehrere Rollen annehmen
“Jack cut the Fish" mit 'Jack' als Agent vs. "A Knife cut the Fish" mit 'A Knife' als Instrument.

Ebenfalls können unterschiedliche Strukturen die selbe Rollenverteilung behalten.

### Regeln der Kasusrollen
- Es gibt Ausnahmen
- Eine Kasusrolle pro Konstituente (Pro Subjekt / Objekt nur eine Rolle)
- Keine doppelten Rollen.
  Innerhalb einer Regel darf keine Rolle mehrfach erscheinen
- Koordinierung von NPs: Nur NPs derselben Kasusrolle können kombiniert werden. In "Der Lehrer und die Schüler sind hier" sind beide Subjekte Agenten

# Semantische Analyse
Wörter können falsch interpretiert werden, dadurch wird die Verarbeitung deutlich erschwert.
Im Englischen gibt es für jedes Substantiv ca. 5-8 Synonyme.
Hat das Ziel ein tieferes Verständnis für die Struktur und Funktion von Wörtern innerhalb der Sprache zu entwickeln.


> [!MISSING] Lesezeichen
> Contents


# Lexikalische Einheit
Umfasst Wörter, Wortbestandteile und Affixe (Präfixe und Suffixe) sowie zusammengesetzte Wörter und Phrasen

## Lexikon einer Sprache
Ist ein Katalog aller [Lexikalische Einheiten](#Lexikalische%20Einheit) einer Sprache.

# Lexikalische Beziehungen
Manche Wörter stehen in festen Beziehung zueinander.
Im folgenden sind einige der Beziehungsarten gelistet.
## Homonymie
Wörter die gleich klingen, aber verschiedene Bedeutungen haben

> [!Quote] Beispiel
> "Bank" als Geldinstitut vs. "Bank" als Sitzgelegenheit

## Polysemie
Mehrdeutigkeiten desselben Wortes

> [!Quote] Beispiel
> "Kopf" kann das Körperteil bedeuten, oder den Anführer einer Gruppe meinen

## Metonymie
Übertragung der Bedeutung durch Assoziation

> [!Quote] Beispiel
> "Das Weiße Haus" als Begriff für die US-Regierung

## Synonyme und Antonyme
Wörter mit sehr ähnlicher oder gegenteiliger Bedeutung

> [!Quote] Beispiel
> "Auto" oder "Fahrzeug" als Synonyme,
> "Heiß" und "Kalt" als Antonyme

## Hyponyme und Hypernyme
Unter- und Oberbegriffe

> [!Quote] Beispiel
> "Apfel" als Hyponym von "Frucht"
> "Frucht" als Hypernym von "Apfel"

# Komplexe Spracheinheiten
Die Bedeutung von Aussagen basiert neben der Bedeutung der einzelnen Wörter auch auf ihren syntaktischen Verbindungen.

`Andrew likes Jane` $\to \text{likes}(Andrew, Jane)$ 
`Jane likes Andrew` $\to \text{likes}(Jane, Andrew)$  

Nur durch Ändern der Reihenfolge erhält der Satz eine andere Bedeutung.
Ziel ist es, die Informationen in formale Repräsenationen zu transformieren. 

## Symbolische Repräsentation
Stellt Logische Formeln durch inferelle oder Graphenbasierte Mechanismen dar.

## Vektorielle Darstellung
![](WordVector.png)

Ordnet Wörter in einem hochdimensionalen Raum an, sodass Beziehungen als Abstände codiert werden. Beispielsweise ist der Verbindungsvektor zwischen Frankreich und Paris sehr ähnlich zu dem, der Deutschland und Berlin verbindet.

Diese Technik wird in aktuellen Modellen am häufigsten verwendet.


> [!NOTE] Word Sense
> Die Wortbedeutung ist entscheidend für die Position im [Vektorraum](Vektoren%20und%20Vektorräume.md). Bei [Homonymen](#Homonymie) würden beide Bedeutungen des Wortes separat im Raum positioniert werden.


# Word Sense Disambiguation (WSD)
Syntaktische Mehrdeutigkeit wird durch [PoS Tagging](03%20PartOfSpeech.md#PoS%20Tagging) aufgelöst, WSD ist für die semantische Mehrdeutigkeit zuständig.

Ein Problem für die WSD sind die Unterschiedlichen Definitionen von Wörtern in verschiedenen Wörterbüchern.

PoS Tagging basiert auf der unmittelbaren Umgebung von Wörtern während WSD auch weiter entfernte Kontexte berücksichtigen kann.


> [!NOTE] Inter-Judge Variance
> Beim Vergleich von WSD Ergebnissen mit menschlichen Einordnungen von Wörtern fallen Unterschiede auf.
> Allerdings werden die von Menschen Labels von äußeren Faktoren wie Stimmung, Tageszeit und persönlichen Vorlieben beeinflusst.
> 
> Menschen sind insgesamt besser in der groben Unterscheidung als in der feingranularen Analyse der Bedeutungen


## Methoden
### Wissensbasierte Methode
Rechnerisch Intensiv, benötigt aber keine Korpusevidenz.

#### Lesk-Methode
1. Für jedes Wort im Kontext werden alle möglichen Bedeutungen aus einem Wörterbuch extrahiert
2. Gemeinsame Wörter in den Definitionen des aufzulösenden Wortes und den umgebenen Wörtern werden gezählt
3. Die Bedeutung mit der größten Überlappung wird akzeptiert.

Die Qualität der Ergebnisse hängt stark von der detailreiche der Definitionen im verwendeten Wörterbuch ab. Bei sehr komplexem Kontext kann die Genauigkeit ebenfalls sinken. 

### Überwachtes Lernen
Intensive Rechenressourcen und Korpusevidenz

Eine [SVM](05%20SVM.md#Support%20Vector%20Machines) kann eine Trennlinie zwischen den Bedeutungen eines Wortes finden. Hohe Genauigkeit wenn Trainingsdaten in ausreichender Menge vorhanden sind.

### Semi-Überwachtes Lernen
Kombiniert geringere rechnerische Intensität mit Korpusevidenz

Kombiniert gelablelte und ungelablete Daten.
Beim "Bootstrapping" wird mit einer kleinen Menge Trainingsdaten gestartet und die Vorhersagen für unbekannte Wörter ebenfalls in die Trainingsdaten aufgenommen.

Hier besteht die Gefahr dass sich Fehler sehr großflächig  fortpflanzen können.

### Unüberwachtes Lernen
Unabhängig von Korpusevidenz und rechnerisch effizient

Keine Notwendigkeit für manuelle Annotation, die Bedeutung von Wörtern wird anhand von Ähnlichkeiten in Strukturen erkannt.

Da keine definierten Trainingsdaten vorhanden sind, kann hier die Genauigkeit des Modells nur schwer validiert werden.

# Synsets
![](Synset.webp)

"Synonym Sets" sind Graphen die jeweils Synonyme mit einander verbinden

## Pfadbasierte Ähnlichkeit
Der Abstand in der Bedeutung zweier Wörter kann anhand der Abstände in einem [Synset](#Synsets) erkannt werden.

![](PathBasedWordDistance.png)

Jedes Wort hat zu sich selbst den Abstand $1$

Die Pfad-basierte Ähnlichkeit $\text{simpath}(c_1, c_2)$ von zwei Knoten berechnet sich wie folgt:
$$
\text{simpath}(c_1, c_2) = \frac{1}{\text{pathlen}(c_1, c_2)}
$$
Die Wortähnlichkeit berücksichtigt auch die verschiedenen Bedeutungen von Wörtern. Es wird die maximale Distanz aller Kombinationen von Definitionen verwendet.
$$
\text{wordsim}(w_1, w_2) = \max \left( \text{simpath}(c_1, c_2) \right) \qquad \forall c_1 \in \text{senses}(w_1), c_2 \in \text{senses}(w_2)
$$

Schwächen dieses Ansatzes sind die konstanten Abstände innerhalb des Graphen. Daher werden Ähnlichkeiten zu abstrakteren Worten tendenziell immer als größer berechnet. 

# Term Dokument Matrix
Zeigt die Häufigkeit und Verteilung von Begriffen in einem Dokument.

Zeilen symbolisieren Wörter oder Begriffe die im Dokument vorkommen.
Spalten Repräsentieren Dokumente oder Sätze, die analysiert werden.
Zellen zeigen die Anzahl an Vorkommnissen eines Begriffs in einem Dokument.

|         | As you Like it | Twelfth Night | Julius Caesar | Henry V | Sherlock Holmes | Moby Dick |
| ------- | -------------- | ------------- | ------------- | ------- | --------------- | --------- |
| Battle  | 1              | 1             | 8             | 15      | 1               | 20        |
| Soldier | 2              | 2             | 12            | 36      | 0               | 4         |
| Fool    | 37             | 58            | 1             | 5       | 3               | 7         |
| Trick   | 1              | 3             | 1             | 1       | 3               | 3         |

Zwei Dokumente gelten als ähnlich, wenn sie ähnlich Wortverteilungen haben. Z.B. Julius Caesar und Henry V haben vergleichbare Worthäufigkeiten.

Einzelne Zeilen nennt man "Wort-Vektoren".
Zwei Dokumente sind ähnlich, wenn sie ähnliche Wort-Vektoren haben.

## Metriken
### Pointwise mutual Information (PMI)
Vergleicht die Wahrscheinlichkeiten dass zwei Ereignisse gemeinsam auftreten mit der Wahrscheinlichkeit, dass sie unabhängig erscheinen.
$$
\text{PMI}(x; y) = \log_2 \left( \frac{p(x,y)}{p(x) \cdot p(y)} \right)
$$
Dabei ist $p(x,y)$ die Wahrscheinlichkeit, dass die Wörter gemeinsam auftreten und $p(x)$ die Wahrscheinlichkeit der Wörter im Text vorzukommen.

Worte die nur gemeinsam auftreten erhalten große positive Werte, während Worte die nur selten oder nie zusammen auftreten mit kleineren oder negative Zahlen versehen werden.

#### Positive Pointwise Mutual Information (PPMI)
Ist eine Variante von [Pointwise mutual Information (PMI)](#Pointwise%20mutual%20Information%20(PMI)), wobei negative Werte ausgeschlossen durch $0$ ersetzt werden und somit ausgeschlossen sind.

$$
\text{PPMI}(x;y) = \max \left( \text{PMI}\left(x,y\right), 0 \right)
$$
Grund ist, dass mit negativen Werten in vielen Modellen nur schlecht umgegangen werden kann.
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
Transfer Learning gilt als Schlüssel zur Leistungsfähigkeit großer Sprachmodelle.

# Transfer Learning in LLMs
![](TransferLearningStepsInLlm.png)

Beim Finetuning werden ggf. Firmeninterne Dokumente zum Training verwendet. So kann sich ein Modell an den Kontext bestimmter Aufgaben anpassen.

Transfer Learning ist deutlich effizienter als Modelle für jeden Kontext von Grund auf neu zu trainieren. Das teure Basismodell kann flexibel auf verschiedene Aufgaben spezialisiert werden.

Mit diesem Ansatz ist es lohnenswert das Basismodell mit mehr Daten zu trainieren, da es für verschiedene Aufgaben weiterverwendet werden kann.
![](TransferLearningTraningData.png)

Beispielsweise könnte ein auf Buchrezensionen trainiertes Basismodell auf Filmrezensionen spezialisiert werden, da die Anwendungen ähnlich sind.

# Randwahrscheinlichkeit
Die [Randwahrscheinlichkeit](Mehrdimensionale%20Verteilungen.md#Mehrdimensionale%20WS-Verteilungen) beschreibt die Wahrscheinlichkeit eines Datenpunktes zu einer bestimmten Klasse zu gehören, unabhängig von anderen Parametern.

$P(\text{Katze})$ Ist die Wahrscheinlichkeit dass ein zufällig ausgewähltes Bild eine Katze zeigt, ohne weitere Merkmale zu beachten.

# Transfer Learning
## Homogenes Transfer Learning
Quell- und Zieldomäne haben ähnliche Aufgaben und Daten. Die erlernten Merkmale und Strukturen lassen sich effizienter übertragen und liefern mit kleinen Anpassungen bereits gute Resultate.

## Heterogenes Transfer Learning
Hier sind Daten und Aufgaben sehr verschieden. Beispielsweise wenn ein Basismodell auf die Klassifikation von Bildern trainiert wurde und nun zur Generierung von Texten genutzt werden soll.

Die Unterschiede erschweren die Anwendbarkeit des Basismodells, es sind umfangreiche Anpassungen nötig.


> [!Info] Warum ist das besser als eine untrainiertes Modell?
> Auch wenn die Art der Aufgaben sehr unterschiedlich ist, kann ein Teil der Muster übereinstimmen. 
> Beim weiteren Training kann eine Art "Converter" entstehen um die zunächst inkompatiblem Formate an Informationen ineinander zu wandeln

## Domänenunterschiede
Die Unterschiede zwischen den Domänen werden mit vier grundlegenden Ansätzen reduziert.

- Instanzbasiert
- Merkmalbasiert
- Parameterbasiert
- Relationalbasiert

### Instanzbasiert
Proben aus der Quelldomäne werden durch Gewichtung angepasst um sie in der Zieldomäne besser nutzen zu können.
Die Datenpunkte werden als unterschiedlich gewichtet, entsprechend ihrer Anwendbarkeit für die Zieldomäne.

Diese Strategie ist Modell- und Datentypsunabhängig. Sie lässt sich sehr gut an verschiedene Aufgaben anpassen.

### Merkmalbasiert
Modifikation einer Domäne um die Lücke zwischen Quelle und Ziel zu verringern. Anwendbar wenn die Zielvariablen identisch sind.

Asymmetrische Merkmalsumwandlung (Für Sentiment-Analyse):
Beispielsweise die Wandlung eines auf Filmrezensionen trainierten Modells auf Produktbewertungen. Das Modell soll in beiden Fällen die Stimmung der Kunden aus den Bewertungen erkennen.

Symmetrische Merkmalsumwandlung (Für Dokumentenklassifikation):
Trainiert auf Nachrichten, soll auch mit wissenschaftlichen Artikeln arbeiten.
Es werden beide Domänen in einen gemeinsamen Merkmalsraum transformiert (symmetrisch)

### Parameterbasierte Methoden
Basiert auf der Annahme, dass ähnliche Aufgaben auch ähnliche Modellstrukturen aufweisen.
Wissen wird übertragen, indem Parameter zwischen den Modellen der Quell- und Zieldomäne geteilt werden.

![](TransferLearningParameterBased.png)

### Relationalbasierte Methoden
Relationale Methoden übertragen Wissen, indem sie Muster in den Strukturen von Quell- und Zieldaten erkennen. Trotz Unterschiede in den Inhalten selbst können die Beziehungen ähnlich sein.

![](RelationalBasedMethod.png)


# Rekurrente Neuronale Netze (RNNs)
Sprache enthält einen fundamentalen Aspekt der Zeit. Sowohl gesprochene Sprache, als auch schriftliche Texte enthalten eine zeitliche Reihenfolge.
Bisher beschriebene Modelle berücksichtigen diesen Aspekt nicht, alle Eingaben werden gleichzeitig verarbeitet.

Bei [Feed-Forward Netzen](07%20Neural%20Nets.md#Neural%20Nets) wird mit einem Sliding-Window gearbeitet, damit nur eine begrenzte Anzahl von Wörtern betrachtet wird um Vorhersagen zu treffen.

In RNNs ist ein Mechanismus integriert, der direkt mit der sequenziellen Natur der Sprache umgeht und sie ohne willkürlich festgelegten Fenstergrößen behandelt. 
Durch Rückkopplung können sie vorherige Kontexte repräsentieren, somit können Entscheidungen auch aufgrund von vorherigen Entscheidungen getroffen werden.

![](RnnCycle.png)

Typische Anwendung von RNNs sind
- Sprachmodellierung:
  Vorhersage von Wortfolgen basierend auf vorherigem Text
- Textklassifikation
  Aufgaben wie Sentimentanalyse
- Sequenzmodellierung
  Aufgaben wie [PoS Tagging](03%20PartOfSpeech.md#PoS%20Tagging)

Die zyklische Struktur mach RNNs besonders leistugsstark bei der Verarbeitung zeitlicher Daten, birgt jedoch auch einige Herausforderungen.
Die Struktur erschwert das Verständnis der Funktionsweise des Netzwerks.
Auch das Training ist schwieriger, da bei besonders langen Sequenzen der [Gradient](07%20Neural%20Nets.md#Gradientenabstieg) verschwinden oder explodieren kann (Diminishing and Exploding Gradients)

## Elman-Netze
Auch "einfache rekurrente Netze" sind eine eingeschränkte Architektur die sich für die Sprachverarbeitung als äußerst effektiv erwiesen haben.

![](ElmanNetsVsFullyConnectedRnn.png)

Links dargestellt ist ein Elman-Netz, bei dem nur die [Neuronen](07%20Neural%20Nets.md#Neuronen) in einer versteckten Schicht rekurrent verbunden sind. Rechts in der Abbildung ist ein vollständig verbundenes rekurrentes neuronales Netz dargestellt.
Da deutlich weniger Verbindungen vorhanden sind ist das Training und die Nachvollziehbarkeit von Ergebnissen erleichtert.

Bei der Berechnung eines Ergebnis werden dabei die neuen Eingaben mit Informationen aus vorherigen Zeitpunkten kombiniert.
Dabei kann der Kontext bis zum Beginn der Sequenz zurückreichen.

![](RecurrentNeuralNet.png)

Um $h_t$ zu berechnen, wird der Eingang $x_t$ mit der Gewichtsmatrix $W$ multipliziert und die versteckte Schicht des vorherigen Zeitschritts $h_{h-1}$ mit der Gewichtsmatrix $U$.
Diese Werte werden addiert und durch eine gewählte [Aktivierungsfunktion](07%20Neural%20Nets.md#Aktivierungsfunktion) $g$ geleitet um den Aktivierungswert der aktuellen versteckten Schicht $h_t$ zu erhalten.

$$
h_t = g(U \cdot h_{t-1} + W \cdot x_t)
$$
$$
y_t = f(V \cdot h_t)
$$

Um die Rekurrenz zu eliminieren kann man das Netz "entrollt" darstellen. 
![](UnrolledRnn.png)
In der Darstellung sind $x_i$ die jeweiligen Eingaben aus der Eingabesequenz.
Die $h_i$ sind das Feedback aus allen vorherigen Schritten.

### Wortschatz
Der Wortschatz $V$ eines Modells ist die [Menge](Intervalle%20und%20Mengen.md#Mengen) aller einzigartigen Wörter die verwendet werden.
Die Größe des Wortschatzes wird mit $|V|$ dargestellt. Sie gibt die Anzahl der in Trainings- und Testdatensatz vorkommenden Wörter an.

Dabei hat jedes Wort im Wortschatz ein zugehöriges [Embedding](#Embedding) die in der [Embedding Matrix](#Embedding%20Matrix) gespeichert ist. Die Dimension der Embedding ist in der Regel sehr viel kleiner als die Dimension des Wortschatzes selbst.


### Embedding Matrix
Repräsentiert die Einbettung der Wörter im Wortschatz. Jedes Wort wird durch einen [Vektor](Vektoren%20und%20Vektorräume.md#Vektoren) in einem kontinuierlichen Raum dargestellt.

Bei einem Wortschatz der Größe $|V|$ und einer Embedding-Dimensinon $d$ hat die Embedding-Matrix die Dimension $|V| \times d$.
Jede Spalte der Matrix stellt den Embedding Vektor eines bestimmten Wortes dar.

Bei der Verarbeitung einer Eingabesequenz wird der entsprechende Embedding-Vektor von jedem Wort abgerufen. 
Dabei haben ähnliche Worte auch ähnliche Vektoren, um semantische Beziehungen zu erfassen.
Während dem Training wird auch die Embedding-Matrix optimiert, um Beziehungen besser abzubilden. 
Die [Matrix](Matrizen.md#Definition) spielt dabei eine entscheidende Rolle um die diskreten Eingabeworte in stetige Zahlenwerte umzuwandeln, die für die Verarbeitung durch das [neuronale Netz](07%20Neural%20Nets.md#Neural%20Nets) notwendig sind.

### Architektur
Die Eingabe $X = (x_1, x_2, \dots, x_n)$ besteht dabei aus einer Reihe aus Wörtern $x_i$, jedes dargestellt als ein [One-Hot-Vektor](02%20Modellauswahl.md#One%20Hot%20Encoding) der Größe $|V|$.
Die [Embedding Matrix](#Embedding%20Matrix) $E$ enthält die Embeddings $e_t$ für alle Wörter $x_t$. 
![](RnnArchitecture.png)
Das Embedding wird mit der Gewichtsmatrix $W$ multipliziert und zum versteckten Layer des vorherigen Schritts (gewichtet durch die Gewichtsmatrix $U$) addiert, um einen neuen versteckten Layer zu berechnen.
Der neue versteckte Layer wird verwendet, um eine Ausgabeschicht zu erzeugen, die durch eine Softmax-Schicht geleitet wird um eine [Wahrscheinlichkeitsverteilung](Einführung.md#Wahrscheinlichkeitmaß%20/%20Wahrscheinlichkeitsverteilung) über den gesamten Wortschatz zu generieren.
Die Wahrscheinlichkeit, dass das Wort am Index $k$ das nächste Wort ist, beträgt $\hat{y}_t[k]$ 

- $e_t = E \cdot x_t$
- $h_t = g(U\cdot h_{t-1} + W \cdot e_t)$
- $\hat{y}_t = \text{Softmax}(V \cdot h_t)$


> [!NOTE] Modell-Dimensionen
> Bei der Sprachmodellierung mit RNNs nehmen wir an, dass die Embedding-Dimension $d_e$ und die verborgene Dimension $d_h$ gleich sind. Wir bezeichnen beide als Modell-Dimension $d$

### Bewertung
RNNs sind besonders gut im Umgang mit Sequenzdaten, wie Sprache, Zeitreihen oder Musik.
Sie können Eingaben beliebiger Länge verarbeiten, was sie von den klassischen Neuronalen Netzen mit fester Eingabegröße abhebt.

Durch das Vanishing Gradient Problem haben diese Modelle teilweise Schwierigkeiten von langfristigen Abhängigkeiten zu lernen. Sie werden aufgrund ihrer Natur nicht parallelisiert trainiert, da jeder Schritt auf dem vorherigen aufbaut.
Auch neigen sie besonders zu Overfitting, insbesondere bei kleineren Datensätzen.


## Long Short-Term Memory (LSTM) Network
Ist eine besondere Art von RNN um das Problem der explodierenden oder verschwindenden Gradienten zu umgehen.
Bei längeren Sequenzen zeigt diese Architektur bessere Leistungen als ein naives RNN.

Es werden spezielle Speicherzellen eingesetzt, um Informationen auch über längere Zeiträume zu behalten.
Im Gegensatz zu klassischen RNNs wird eine innere Zelle und drei spezielle "Gates" eingesetzt.
- Eingangsgate
  Bestimmt wie stark ein neuer Wert in die Zelle einfließt
- Vergessensgate
  Bestimmt, wie viel eines Wertes in der Zelle verbleibt
- Ausgangsgate
  Kontrolliert, wie stark der Zellwert für die nächste Berechnung verwendet wird

![](LstmArchitecture.png)
![](LstmArchitectureForgetGate.png)

Alle Gates werden durch die Eingangsdaten aktiviert oder deaktiviert. Dabei werden ebenfalls Gewichte berechnet, die während dem Training angepasst werden.

Die Zustände des Gates werden aus den Vektoren $x_t$ und $h_{t-1}$ berechnet.
Dabei hat das Netz drei logische Eingaben:
- Die aktuelle Eingabe $x_t$
- Den bisherigen Verborgenen Zustand $h_{t-1}$
- Der Kontext-Wert $c_{t-1}$ aus der Speicherzelle

![](LstmCalculationGraph.png)

### Gate-Berechnungen
Jedes Gate ist ein Vektor. Es wird berechnet als die gewichtete Summe der Eingabedaten $x_t$ und $h_{t-1}$ die dann in eine [Aktivierungsfunktion](07%20Neural%20Nets.md#Aktivierungsfunktion) $\in \text{Abb}(\mathbb{R}^n \to \mathbb{R}^n)$ (z.b. Sigmoid) gegeben werden.

- Forget Gate: $f_t = \sigma(U_fh_{t-1} + W_fx_t)$
- Input Gate: $i_t = \sigma(U_ih_{t-1} + W_ix_t)$
- Output Gate: $o_t = \sigma(U_oh_{t-1} + W_ox_t)$

Dabei sind mit $U$ und $W$ jeweils die beim Training erlernten Gewichtsmatrizen gemeint.


Bei jeder Berechnung werden zuerst die eigentlichen Eingabedaten aus dem neuen Input und dem bisherigen Zustand berechnet.
$$
g_t = \tanh (U_gh_{t-1} + W_gx_t)
$$
Es wird der Kontextzustand aktualisiert um die neuen Informationen zu berücksichtigen
$$
c_t = f_t \odot c_{t-1} + i_t \odot g_t
$$

Schließlich wird der neue verborgene Zustand $h_t$ unter Verwendung des aktuellen Kontextzustands und des neuen Output Gates berechnet
$$
h_t = o_t \odot \tanh (c_t)
$$
Hier sind $U_g$ und $W_g$ wieder trainierte Matrizen.
Das Symbol $\odot$ steht führ die elementweise Multiplikation zweier Vektoren. (["Hadamard-Produkt"](Vektoren%20und%20Vektorräume.md#Rechenoperationen)) 


## Gated Recurrent Unit (GRU)
Sind eine Art von [RNN](#Rekurrente%20Neuronale%20Netze%20(RNNs)).
Sie lösen ebenfalls das Problem der exploding Grandients und sind eine neuere und vereinfachte Variante der [LSTMs](#LSTM).
Die Funktion von Forget-Gates und Input Gates wird in einem einzelnen Gate kombiniert.

![](GruArchitecture.png)

Eine GRU-Einheit hat zwei Hauptzustände:
- $h_t$: Der verborgene Zustand zur Zeit $t$
- $r_t$: Der Reset-Zustand. Er bestimmt, wie viel vom vorherigen Zustand beibehalten wird.

Die Werte werden nach folgenden Vorschriften berechnet
- Update-Gate: $z_t = \sigma(W_zx_t + U_zh_{t-1})$
- Reset-Gate: $r_t = \sigma(W_rx_t + U_rh_{t-1})$
- Neuer Zustand: $\tilde{t}_t = \tanh(Wx_t + U(r_t \odot h_{t-1}))$
- Ausgabe: $h_t = (1-z_t) \odot h_{t-1} + z_t \odot \tilde{h}_t$

> [!INFO] Was ist $1$?
> Mit $1$ in der Gleichung des Ausgabe-Gates ist der Vektor gemeint, der die Dimension von $z_t$ hat und nur Einsen enthält.

GRU-Netze sind aufgrund der einfacheren Architektur leichter zu trainieren als [LSTMs](#Long%20Short-Term%20Memory%20(LSTM)%20Network), zeigen aber oft vergleichbare oder bessere Leistungen.
Sie sind also eine leistungsfähige und effiziente Alternative zu LSTM-Netzen.

# Transformer
Bestehen aus zwei Hauptkomponenten, Encoder und Decoder.

![](TransformerEncoderDecoder.png)

Sie wandeln jeweils von oder in eine interne Informationsdarstellung um. Der Encoder verwendet dabei [Attention](#Attention-Mechanismus) um Informationen zu gewichten, bevor sie in der internen Darstellung gespeichert werden.

## Attention-Mechanismus
Mit Attention können Modelle bestimmte Teile der Eingabe stärker gewichten. Dadurch bleibt der Fokus auf relevanten Informationen.

Welche Teile im Fokus stehen hängt dabei von der Eingabe selbst ab.

### Self-Attention
1. Eingaberepräsentation
   Jedes Wort oder Token wird als Vektor dargestellt. Dieser wird typischerweise aus [Einbettungen](#Embedding) abgeleitet
2. Abfrage-, Schlüssel- und Wertvektoren
   Für jedes Wort der Eingabe werden drei Vektoren erzeugt
	1. Abfragevektor $Q$
	   Repräsentiert das Wort für das Informationen gefunden werden sollen
	2. Schlüsselvektor $K$
	   Repräsenstiert potentielle Wörter, die relevante Informationen liefern könnten
	3. Wertvektor $V$
	   Enthält die tatsächlichen Informationen die aus den Attention Scores aggregiert wurden
3. Berechnung der Attention-Scores
   Der Attention Score zwischen einem Abfragevektor und allen Schlüsselvektoren wird in der Regel durch ein [Skalarprodukt](Vektoren%20und%20Vektorräume.md#Rechenoperationen) berechnet.
   Der Score misst dabei die Ähnlichkeit zwischen einer Abfrage und einem Schlüssel
4. Normalisierung der Werte mit Softmax
   Die Werte werden vor der weiteren Verarbeitung normalisiert
5. Gewichtete Summe der Wertvektoren
   Endgültiger Output für jedes Wort wird als gewichtete Summe der Wertvektoren berechnet. Gewicht sind dabei die Aufmerksamkeitswerte

#### Embedding
Eingabewörter werden mit einem vortrainierten Word Embedding in Vektoren umgewandelt.
![](EmbeddingSteps.png)

Zur Verarbeitung werden alle Vektoren zu einem [Tensor](11%20Deep%20Learning.md#Tensoren) zusammengefasst. 
Jede Zeile des Eingabetensors $X$ entspricht so einem Embedding-Vektor.
All diese Vektoren haben die selbe Länge.

#### Einzelschritte: Query, Key und Value
Diese Vektoren werden verwendet um die Wichtigkeit des Tokens im Verhältnis zu anderen Tokens zu bestimmen. Dabei werden alle drei Vektoren gleichzeitig für alle Eingaben berechnet, indem der Eingabetensor mit lernbaren Gewichtsmatrizen multipliziert wird.

Jede Zeile des resultierenden Tensors entspricht dabei dem Vektor eines Eingabetokens.

#### Attention Score
Man berechnet das [Skalarprodukt](Vektoren%20und%20Vektorräume.md#Rechenoperationen). zwischen jedem Abfrage- und jedem Schlüsselvektor. Anschließend werden die Werte mit "SoftMax" normalisiert.
Diese Operation wird als Matrixmultiplikation der $Q$ und $K$ [Tensoren](11%20Deep%20Learning.md#Tensoren) realisiert. Jeder Wert der Ausgabematrix entspricht einem Skalarprodukt.

![](AttentionScoreCalculation.png)

Die Werte in der Produktmatrix werden durch $\sqrt{d_k}$ geteilt um die Größe der Zahlen zu begrenzen.
Dabei ist $d_k$ die Dimension des Key-Vektors. (Also die Anzahl Spalten der untransponierten $K$-Matrix)

#### Attention Heads
Sind eine Möglichkeit gleichzeitig mehrere Aspekte der Eingabedaten zu analysieren.

- Lernfähige Gewichtsmatrizen
  Jeder Head besitzt eigene Gewichtsmatrizen die beim Training optimiert werden.
- Parallele Verarbeitung
  Die Berechnungen lassen sich gleichzeitig ausführen
- Vielfältige Informationsaufnahme
  Verschiedene Merkmale können fokussiert werden. (Syntax / Semantik)
- Aggregation der Resultate
  Ausgabe aller Heads werden zusammengeführt um eine umfassende Repräsentation zu erzeugen.
- Erweiterte Modellkapazität
  Mehrere Heads erhöhen die Fähigkeiten des Modells, ohne die Gesamtzahl der Parameter stark zu erhöhen


![](SelfAttentionSummary.png)


## Fazit
[Self-Attention](#Self-Attention) mit mehreren Heads ermöglicht es mehrere Aspekte des Kontext zu berücksichtigen. Auch die Berechnung lässt sich im Gegensatz zu den [RNNs](#Rekurrente%20Neuronale%20Netze%20(RNNs)) parallelisieren und ist somit deutlich effizienter beim Training mit großen Daten.
Der Mechanismus ist grundlegend für die Leistung von Modellen wie GPT oder [BERT](09%20More%20Transformer.md#BERT), da er ihnen die Möglichkeit gibt menschenähnlichen Text zu verstehen und zu generieren.

# Feed-Forward-Netze
Werden in den Encoder- und [Decoder](#Decoder)-Teilen der [Transformer](08%20Transformer.md#Transformer)-Architektur verwendet.
Dabei lernen die Netze Beziehungen zwischen den Eingabe- und Ausgabesequenzen.

## Residuenverbindungen
Auch "Skip-Verbindungen" umgehen Schichten in einem [Neuronalen Netz](07%20Neural%20Nets.md#Neural%20Nets) um einen einfacheren Informationsfluss zu ermöglichen.
In der Transformer Architektur werden solche Verbindungen im Encoder- und im Decoder Teil verwendet.

In tieferen Netzen wird so die Informationspropagation durch das Netz verbessert und somit die Lernfähigkeit erhöht.

![](SkipLayersInTransformer.png)

Das Lernen komplexer Zuordnungen zwischen Eingabe- und Ausgabesequenzen wird erleichtert, das Lernen allgemeiner Merkmale wird gefördert.
Modelle mit diesen Skip-Layern sind weniger zu Overfitting geneigt und verallgemeinern besser auf neuen Daten.

# Encoder
Wie auch der Decoder enthält der Encoder die folgenden Komponenten:
- [Multi-Head Attention Schichten](08%20Transformer.md#Attention%20Heads)
- [Feed-Forward-Netze](#Feed-Forward-Netze)
- [Residualverbindungen](#Residuenverbindungen)
- Layer Normalisierung

![](EncoderAndDecoder.png)

Der Encoder nimmt eine Sequenz von [Token](02%20N-Gramm.md#Token) als Eingabe und berechnet eine Sequenz von Vektoren, die eine Codierung der Eingabe darstellen.

Er besteht aus einem Stapel von $N$ identischen Schichten. Jede Schicht enthält folgende Sublayer:
- [Multi-Head Attention Schicht](08%20Transformer.md#Attention%20Heads)
- [Feed-Forward-NN-Schicht](#Feed-Forward-Netze)
- [Residualverbindungen](#Residuenverbindungen)

## Encoder: Feed-Forward-Netz-Schicht
Die Eingabe dieser Schicht besteht aus Vektoren, die aus der vorhergegangenen [Multi-Head-Self-Attention-Schicht](08%20Transformer.md#Attention%20Heads) stammen. In diesen Vektoren sind bereits Informationen über die Eingabesequenz enthalten.

Erst wird der Eingabevektor in einen höherdimensionalen Raum umgewandelt um mehr Kapazität für Repräsentationen zu erreichen.
In diesem Raum wird eine nicht lineare Transformation wie [ReLU](07%20Neural%20Nets.md#Aktivierungsfunktion) durchgeführt um auch komplexe Muster zu erkennen.
In einer zweiten Transformation wird der Vektor wieder auf seine ursprüngliche Dimension reduziert.
Ausgabe ist somit ein Vektor, der eine nicht-lineare Transformation widerspiegelt und an die nächste Schicht weitergegeben werden kann.

Nach jedem Sublayer (wie der Attention-Schicht oder dem FFN) wird die Eingabe des Sublayers mit seiner Ausgabe addiert.
Diese Addition ist die Anwendung der [Residualverbindung](#Residuenverbindungen).

## Layer-Normalisierung
Um die Trainingsstabilität zu verbessern wird dieser Schritt auf den Eingaben jeder Schicht angewandt.
Dabei wird der Mittelwert $\mu$ und die Standardabweichung $\sigma$ der Elemente des Eingabevektors berechnet.
Die Normalisierung erfolgt abhängig von beiden Zahlen:
$$
\text{Norm}(X) = \frac{X - \mu}{\sigma - \mathcal{E}}
$$

Durch die Normalisierung ist das Modell weniger empfindlich gegenüber den Initialisierungswerten und trainiert somit stabiler. 
Da die Eingaben jeder Schicht eine ähnliche Verteilung erhalten, kann die Konvergenz beschleunigt werden.

# Decoder
Erhält als Eingabe die Ausgabe des [Encoders](#Encoder), zusammen mit dem bisher generierten Ausgabetext.
Alle Generierten Wörter $0$ bis $i-1$ wird verwendet um Wort $i$ zu generieren.
Zu Beginn wird ein Token `<start>` übergeben, das Vorgehen wiederholt sich, bis ein spezielles Token `<eos>` (End Of Sequence) erzeugt wurde.

Dabei wird bei der Berechnung der Attention mit Maskierung gearbeitet, so dass nur die bereits generierten Tokens mit in die Berechnung einfließen. Da die zukünftigen Token noch nicht existieren, ist es nicht sinnvoll sie in diesem Schritt zu beachten.

Die Sublayer funktionieren identisch zu [denen der Encoder](#Encoder%20Feed-Forward-Netz-Schicht). Nicht-Lineare Transformationen und [Skip-layer](#Residuenverbindungen) mit Normalisierung.

# Grenzen der Transformer
Hauptproblem ist die Skalierung des 'self-Attention-Mechanismus'. Da jedes Token mit jedem anderen kombiniert werden muss, liegt hier eine Quadratische Abhängigkeit in Größe und Rechenzeit vor.

Bei sehr langen Sequenzen werden erhebliche Mengen Speicher und Rechenzeit zur Verarbeitung notwendig. Aus diesem Grund sind Kontextfenster in ihrer Größe begrenzt.

## Optimierungsansätze
Effizientere Implementierung:
Bessere Soft- und Hardware zur Verarbeitung dieser (Matrix-) Berechnungen. Spezialisierte Techniken wie 'Batch-Verarbeitung' oder andere Algorithmen um die Speicherverwendung zu optimieren.

Sparse Attention Mechanismen:
Statt alle Kombinationen zu erlauben, reduziert dieser Ansatz die Zahl der erlaubten Kombinationen. Nur eine Teilmenge der Tokens wird miteinander in Beziehung gesetzt.
Für die genaue Einschränkung gibt es verschiedene Ansätze.
![](SparseAttention.png)

# Training von Transformern
Vielfältige Daten:
- Bücher
- Artikel
- Webseiten
- Dialoge

Hohe Qualität und Menge notwendig für effektives Lernen. 
Vermeidung von Verzerrungen durch ausgewogene Datensätze, diese müssen zuvor bereinigt und tokenisiert werden.

Beim [Pretraining](10%20LLMs.md#Pretraining) wird durch die
Nutzung großer Mengen ungelabelter Daten ein Verständnis für grundlegende Sprachmuster und Kontextinformationen erlernt.

## Fine-Tuning
Anpassung des vortrainierten Modells auf spezifische Anwendungen durch weiteres Training mit speziell gelabelten Daten. So wird die Leisungsfähigkeit und Genauigkeit bei einzelnen Aufgaben erhöht.

## Masked Language Modeling (MLM)
Training von Modellen um maskierte Wörter in einem Text zu erkennen und vorherzusagen.

Beispiel:
`Das Wetter ist <MASK>`, Modell sagt "schön"

Einfaches füllen eines Lückentextes. Ermöglicht das Erlernen kontextueller Beziehungen und semantischer Bedeutungen.

## Autoregressives Lernen
Modell sagt Tokens für das Ende der gegebenen Sequenz vorher. 
Wiederholte Anwendung kann ganze Texte generieren.

# BERT
Bidirectional Encoder Representation from Transcoders ist ein Vortrainiertes Modell von Google.

Bietet eine umfassende Kontextanalyse durch sein Vortraining mit [MLM](#Masked%20Language%20Modeling%20(MLM)).

Nach dem Vortraining kann das Modell auf spezifische Anwendungsarten trainiert werden

Wie auch einfache N-Gramm Modelle werden bei Large Language Models Wahrscheinlichkeiten an Wortsequenzen zugewiesen. Unterschied ist das Training. Bei LLMs wird mit Maskierung gearbeitet um ein Folgewort einer Sequenz vorherzusagen. Bei N-Grammen wird nur mit den Häufigkeitswerten gearbeitet.
Obwohl  nur trainiert wird einzelne Worte vorherzusagen, wird nützliches Sprachwissen erworben.

# Architekturen
![](LlmArchitekturen.png)

## Encoder only
Diese Architektur ist besonders gut geeignet für Aufgaben bei denen keine großen Sequenzen generiert werden müssen. Für [Klassifikationsaufgaben](01%20Grundidee.md#Klassifikation) ist die Fähigkeit nützlich, große Texte umfassend zu analysieren und zu verstehen.

## Encoder-Decoder
Besteht aus einem [Encoder](09%20More%20Transformer.md#Encoder) und einem [Decoder](09%20More%20Transformer.md#Decoder). Eignet sich für Aufgaben bei denen Inputsequenzen in Ausgabesequenzen umgewandelt werden müssen. Beispielsweise in der maschinellen Übersetzung sind diese Modelle beliebt.
Auch Anwendungen wie die Erkennung gesprochener Sprache, also die Transformation von Akustik zu Wörtern ist ein beliebtes Einsatzgebiet.

Da sie sehr ressourcenintensiv sind, ist es für kleinere Ideen sinnvoller sparsamere Modell zu verwenden.

## Decoder Only
Modelle wie GPT oder auch "Left-To-Right LLMs" oder "Autoregressive LLMs" generieren Text von 'links' nach 'rechts'. Es wird stets die aktuelle Sequenz vervollständigt.

Auch solche Sequenzgenerierungsmodelle können für [Klassifikationsaufgaben](01%20Grundidee.md#Klassifikation) verwendet werden. Dazu wird die Wahrscheinlichkeit der verschiedenen Optionen verglichen.
![](LlmForClassification.png)

Auch Zusammenfassungen sind mit diesem Modell möglich. Es wird gelernt nach einem speziellen Delimiter z.B.`tldr` den vorherigen Text zusammenzufassen.
![](DecoderForTldr.png)

Das Modell generiert in jedem Schritt eine [Wahrscheinlichkeitsverteilung](Einführung.md#Wahrscheinlichkeitmaß%20/%20Wahrscheinlichkeitsverteilung) über alle Worte im [Korpus](02%20N-Gramm.md#Korpuslinguistik).
Mittels [Sampling](#Sampling) wird aus den wahrscheinlichsten Worten eines ausgewählt und als Ausgabe verwendet.

### Sampling
Beim Sampling wird zur Erstellung natürlicherer Texte ein Teil der Ausgabetokens zufällig gewählt. Es wird nicht das wahrscheinlichste Wort gewählt sondern eine seltenere Fortsetzung der Sequenz gewählt.
So kann die Ausgabe vielfältiger und lebendiger wirken, opfert aber eventuell Genauigkeit der Ergebnisse.

Es kommt häufig vor, dass auch sehr unwahrscheinliche Worte vorhergesagt werden. Grund ist, dass im sog. 'Tail' der Verteilung extrem viele, sehr unwahrscheinliche Worte liegen.
Um dem entgegenzuwirken kann die Berechnung in zwei Schritten, mittels einer engeren Auswahl erfolgen.

#### Top-k Sampling
Es wird die Liste der Top $k$ wahrscheinlichsten Worten in eine engere Auswahl genommen. Mit nach einer Normierung der Wahrscheinlichkeiten wird eine gültige Verteilung erreicht, die aber Unterschiede in den Wahrscheinlichkeiten beibehält.

#### Top-p Sampling
Statt einer festen Anzahl Wörter wie bei [Top-k Sampling](#Top-k%20Sampling) soll eine dynamische Zahl Wörter verwendet werden, sodass eine feste Menge der Gesamtwahrscheinlichkeit enthalten ist.

Für eine Verteilung $P(w_t \mid w_{<t})$ ist das Top-p-Vokabular $V(p)$ die kleinste Menge von Wörtern mit 
$$
\sum_{w \in V(p)} P(w \mid w_{<t}) \geq p
$$
#### Temperature Sampling
Statt die Verteilung abzuschneiden wird sie hier umgeformt. Beim Sampling mit 'niedriger' Temperatur $(\tau \leq 1)$ wird die Wahrscheinlichkeit der wahrscheinlichsten Wörter erhöht, während die der seltenen Wörter verringert wird. 

Statt $\text{softmax}(u)$ wird $\text{softmax}\left(\dfrac{u}{\tau}\right)$ berechnet.

Werte nahe $\tau = 0$ resultieren in einer weniger explorativen, nahezu deterministischen Wortwahl. Große Werte $(\tau > 1)$  bevorzugen die Wahl von selteneren Fortsetzungen und erhalten so eine vielfältige Sprache, opfern jedoch einen Teil der [Kohärenz](07%20Pragmatische%20Analyse.md#Kohärenz).

# Pretraining
Zentrale Idee ist das Training in zwei Stufen. Im ersten Schritt werden auf breiter Datenbasis allgemeine Muster und Sprachverständnis erlernt. In einem [zweiten Training](#Finetuning) wird das Modell speziell auf eine Aufgabe vorbereitet.

Das Pretraining ist selbstüberwacht, dh. das keine explizit gelabelten Daten eingesetzt werden. Das Modell verwendet stattdessen immer das nächste Token als Label und versucht dieses vorherzusagen.

Als [Loss-function](07%20Neural%20Nets.md#^522bcc) wird "Cross Entropy Loss" verwendet.
Dabei ist $y_t$ die korrekte Wahrscheinlichkeitsverteilung und $\hat{y}_t$ die vorhergesagte Verteilung.
Der Gesamtfehler berechnet sich nach folgender Vorschrift:
$$
L_{CE} = - \sum_{w \in V}y_t[w] \cdot \log(\hat{y}_t[w])
$$
Da die korrekte Verteilung das nächste Wort kennt, ist die Wahrscheinlichkeit für alle Wörter außer dem korrekten $0$.
Somit vereinfacht sich die Berechnung in diesem Anwendungsfall:
$$
L_{CE} = - \log(\hat{y}_t[w])
$$

Es wird erlernt wie semantische Beziehungen in Sprachen funktionieren. Dabei wird auch der Wortschatz des Modells entwickelt.
Kontextuelle Nuancen wie die Ähnlichkeit von 'kalt' und 'eisig' können erlernt werden, wenn die Begriffe oft genug im selben Kontext gesehen werden.
Faktenwissen wie Autorenschaft oder kulturelle Referenzen werden erfasst.
Mathematische und logische Zusammenhänge werden grundlegend erlernt, wobei diese Beziehungen deutliche Schwierigkeiten bei komplexen Aufgaben haben können.


> [!Info] How-To-Mathe
> Wenn Chatbots Berechnungen durchführen sollen, so generieren sie teilweise Pythonprogramme. Diese Programme können die Berechnung ausführen und liefern die Ergebnisse an das Sprachmodell.

## Teacher Forcing
An jeder Position $t$ sind die korrekten Tokens $w_{1:t}$ bekannt. Es wird der loss ($- \log \text{Wahrscheinlichkeit})$ für das nächste Token $w_{t+1}$ berechnet. Nach jeder Vorhersage wird das generierte Token bewertet und verworfen. Nur das bekannte korrekte Token wird angehängt und fortgefahren.

## Datenquellen 
Große Textsammlungen wie Wikipedia und StackExchange, verschiedene Bücher und wissenschaftliche Publikationen sind in 'The Pile' zusammengefasst. Dieser Datensatz bildet in knapp 800GB ein breites Spektrum von Themen und Sprachstilen ab.

![](ThePileComposition.png)

Dabei ist es wichtig Duplikate zu entfernen und anstößige Inhalte zu filtern. Herausforderung ist der Umgang mit Dialekten, verschiedene Ausdrücke könnten in einem Dialekt verfasst sein und fälschlicherweise als problematischer Inhalt erkannt werden.

# Finetuning
Fine-tuning hat vier verschiedene Bedeutungen. Dabei wird in allen Fällen ein Teil der Parameter an neue Daten angepasst werden.

## Fortgesetztes Pretraining
Alle Parameter des Modells werden mit neuen Daten weiter trainiert.
Unter Verwendung derselben [Loss-function](07%20Neural%20Nets.md#^522bcc) und Methodik wie im [Pretraining](#Pretraining) wird so gehandelt, als ob der ursprüngliche Datensatz erweitert wurde.

## Parametereffizientes Finetuning (PEFT)
Es werden aufgrund der großen Menge an Parametern nur ein Teil der Gewichte weiter Trainiert. Alle anderen werden 'eingefroren' und beibehalten.

## Low Rank Adaptation LoRA
Sei $W$ eine Matrix der Form $[N \times d]$  die aktualisiert werden muss. Diese wird in zwei Matrizen $A [N \times r]$ und $B [r \times d]$ zerlegt. Da $r$ gewählt wurde um klein zu sein (z.B. 1 oder 2) ist die Berechnung der Optimierung deutlich schneller. 
Der Effekt wird durch das spätere Zusammenführen auf mehrere Gewichte angewendet. So ist das Training weniger präzise, aber deutlich schneller.

# Bewertung von LLMs
## Perplexität
Misst wie 'verwirrt' das Modell ist, wenn es versucht, den nächsten Teil des Textes vorherzusagen. Bei niedrigen Werten ist das Modell in der Lage Vorhersagen zu machen, die sinnvoll sind und gut zueinander passen.
Hohe Werte zeigen, dass der Text für das Modell unverständlich ist. 

Da die Perplexität sensibel gegenüber Länge von Eingaben und Tokens ist, funktioniert sie am besten wenn ähnliche Modelle verwendet werden.

## Andere Faktoren
- Größe: Die verwendete Menge an Speicherplatz und GPU Verbrauch
- Energieverbrauch: Kann in kWh gemessen werden, oder in ausgestoßenem CO2
- Fairness: Prüft das Vorhandensein von Stereotypen


# Skalierung
Die Leistung von großen Modellen hängt von ihrer Größe ab. Mit mehr Parametern und größeren Trainingsdatensätzen steigt die Qualität der Modelle. 


> [!Info] LLM Overfitting
> Die Grenze zum Overfitting ist noch nicht erreicht. Aufgrund der hohen Kosten wird typischerweise das Training bereits beendet, wenn eine Konvergenz annähernd erreicht ist.

Es wird unterschieden zwischen reinen Chatbots und (Aufgabenbasierten) Dialogsystemen unterschieden.
Während die Chatbots nur für Unterhaltungen gebraucht werden können, sind die Agenten auch in der Lage mit Schnittstellen von Autos/Robotern oder anderen Smarten Geräten zu kommunizieren.

# Aufgabenbasierte Dialogagenten
Bisherige Systeme verwenden eine Rahmenbasierte Architektur, bei der die Struktur der Aufgabe fest vorgegeben ist und gewisse Slots mit dynamischen Werten gefüllt werden.

![](FrameArchitecture.png)

# Konversationsregeln
Da Konversationen abwechselnde Handlungen der beiden Partner erfordern, ist es wichtig diese Wechselpunkte im Gespräch zu erkennen.

![](LengthOfSpeechTurns.png)

Dabei kann die Länge eines vollständigen "Zugs" stark variieren.
Auch sind Pausen im Satz häufig, wenn ein Teilnehmer innehält um beispielsweise seine nächsten Worte zu wählen.


> [!QUOTE] Sprache als Aktion
> Each turn in a dialogue is a kind of action.


## Sprechakte
- Konstative Akte
  Beschreiben oder informieren über einen Sachverhalt
- Direktive Akte
  Fordern den Hörer zu einer bestimmten Handlung auf.
- Kommissive Akte
  Verpflichten den Sprecher zu einer zukünftigen Handlung
- Expressive Akte
  Äußern Gefühle oder emotionale Zustände
## Grounding
Bezeichnet den Prozess, durch den Gesprächspartner sicherstellen, dass sie ein gemeinsames Verständnis über Inhalt und Verlauf ihres Dialogs haben.

In Gesprächen wird dies durch direkte Bestätigungen ('ja', 'genau' etc.) oder Wiederholungen und Paraphrasen erreicht. 
Auch Nonverbale Signale wie Kopfnicken haben diesen Effekt.

In anderen Mensch-Maschine-Interaktionen wird Grounding auch verwendet. Beispielsweise bei Aufzugknöpfen. Das Leuchten nach der Betätigung dient nur dazu, dem Nutzer die Aktivierung zu bestätigen.

![](ElevatorButton.png)

## Konversationsstruktur
Bestimmte Strukturen sind sehr häufig. Beispielsweise folgt auf eine Frage meist eine Antwort, auf einen Vorschlag eine Akzeptanz oder eine Ablehnung.
Diese Muster helfen Systemen dabei, geeignete Aktionen zu bestimmen.

### Subdialoge
Beide Gesprächspartner können einen Subdialog starten, um Missverständnisse schnell aufzulösen oder fehlenden Kontext zu erfragen damit mit einer ursprünglichen Frage weitergearbeitet werden kann.
![](CorrectionSubdialogue.png)

![](ClaritySubdialogue.png)

### Präsequenzen
Manche Fragen werden durch eine Präsequenz eingeleitet
``` Text
A: Can you make train reservations?
B: Yes I can.
A: Great, please reserve ...
```

### Schlussfolgerungen
Manche Informationen sind implizit im Kontext enthalten. Diese zu extrahieren ist für Maschinen sehr schwierig.

``` Text
A: And what day in May did you want to travel
B: Ugh, I need to be there for a meeting from the 12th to the 15th.
```

Die gewünschte Reisezeit ist vermutlich einen Tag vor dem Termin des Meetings.

# Chatbots
## Regelbasierte Chatbots
### ELIZA
ELIZA basierte auf simplen REGEX, um die Aussagen der Probanten näher zu hinterfragen.
Dabei folgte auf ein `feel like X` stets ein `why do you feel like X`. Durch die Stellung als Psychater ist eine Stellung akzeptabel, bei der kein Weltwissen vorhanden ist und quasi nur mit Fragen gearbeitet wird.

Obwohl nur feste Regeln befolgt werden, verknüpften einige Benutzer menschliche Attribute mit dem System.

### PARRY
Verwendet Variablen um einen internen Zustand für Angst, Wut und Mistrauen zu halten. Alle Werte starten niedrig und werden durch bestimmte Schlüsselworte verändert um einen paranoiden Menschen zu simulieren.

Dieser Chatbot konnte erstmals eine Form des Turing-Test bestehen.

## Korpusbasierte Chatbots
Sie benötigen keine explizite Programmierung der Antwortregeln. 
Aus einem Korpus werden Muster erkannt, um Gespräche zu vervollständigen.

Da die Trainingsprozesse sehr datenintensiv sind, ist es nötig eine große Menge von Gesprächen aus Telefonaten / Filmen / Büchern zu verwenden.

### Information Retrieval

> [!Missing] Fehlt
> Seite 687-693


## Bewertung
Gut für enge, skriptbare Anwendungen. 
Für Nutzer kann die Illusion des Verständnis problematisch sein.
Regelbasierte Chatbots sind sehr aufwändig zu implementieren, [IR](#Information%20Retrieval)-basierte Modelle spiegeln nur ihre Trainingsdaten wieder.

Nächste Schritte sind die Integration der Chatbots in frame-basierte Agenten. Damit können Anfragen frei formuliert werden, die Chatbots formen diese dann in die entsprechende Zielstruktur um.

# Frame-basierte Dialogagenten
Grundlegend in einer von zwei Architekturen:
1. GUS-Architektur
   Auch als "Frame-Basierte Architektur" bekannt.
   Wird in den meisten industriellen Anwendungen verwendet
2. Dialogzustandarchitektur
   Erweiterung von GUS
   Häufiger in Forschungssystemen

Das System stellt dem Benutzer fragen, um die Slots zu füllen. Dabei können aus einer Antwort mehrere Informationen extrahiert werden.

![](GusInference.png)
 Auch einfache Inferenzen sind mit Hilfe von [NLP](VorlesungsNotizen/KiAnwendung/01%20Einführung.md#Natural%20Language%20Processing)möglich.
![](NlpToFillSlots.png)


Problem bei solchen Systemen ist der Recall. Eventuell werden nicht alle relevanten Daten direkt erkannt oder nicht korrekt aus dem Kontext erschlossen.

## Dialogakte
Die Ideen von Sprechakten und Grounding werden in einer einzelnen Repräsentation kombiniert.
![](Dialogakte.png)

### BIO-Tagging
BIO-Tagging ist eine Methode um Slots besser zu füllen. Jedes Wort im Satz erhält eine der folgenden Kategorien:
- B (Beginning) Anfang eines Slot-Fillers
- I (Inside) Teil derselben Slot-Filler-Einheit
- O (Outside) Kein Teil eines Slot-Fillers

Somit soll die Information präzise aus Benutzeräußerungen extrahiert werden.

![](Bio-Tagging.png)

Dieses Tagging kann durch einen eigens dafür trainierten [Klassifikator](01%20Grundidee.md#Klassifikation) erfolgen.

## Erkennung von Korrekturen
Korrekturen in der gesprochenen Sprache werden deutlich häufiger missverstanden als normale Anweisungen. 
Aufgrund der Tendenz zur Hyperartikulation (BAL-TI-MORE statt Baltimore) haben Systeme Schwierigkeiten, da sie auf normaler Aussprache der Worte trainiert wurden.

Typische Merkmale von Korrekturen sind die Einleitung durch spezifische Worte ("NEIN" oder "Ich meinte") oder Wiederholungen.

Um Fehler frühzeitig zu erkennen wird mit verschiedenen Bestätigungen gearbeitet. Aussagen die sehr extrem vom bisherigen Kontext abweichen, können stärker misstraut werden als solche, die sehr ähnlich zur vorherigen Aussage sind.

Diese Bestätigungen können auch implizit geschehen, um den Gesprächsfluss weniger stark zu bremsen.
![](ImpliciteConfirmation.png)

Bei Eingaben in denen kein eindeutiger Inhalt erkannt wird, kann die wahrscheinlichste Möglichkeit bestätigt werden, oder mit einer Ablehnung gearbeitet werden.
"Ich suche nach X" vs. "Das habe ich leider nicht verstanden"

Diese Techniken können auch kombiniert werden, um einen Kompromiss aus Korrektheit und Geschwindigkeit zu erhalten und nicht bei Problemen stecken zu bleiben.
![](FehlerbehandlungsKompromiss.png)

Es kann auch konkret nach den Informationen gefragt werden, falls sie nicht im Text erkannt wurden.
![](PreciseQuestionAfterProblem.png)

Wenn mit einem Konfidenzscore gearbeitet wird, kann dynamisch zwischen den verschiedenen Möglichkeiten der Fehlererkennung gearbeitet werden. So wird bei eindeutigen Aussagen nicht unnötig oft nachgefragt oder bestätigt.

# Bewertung von Chatbots
Um die Qualität eines Systems zu bestimmen, wird bei Chatbots mit direkten Fragen an den Benutzer gearbeitet. 
Anhand verschiedener Metriken wie 
- Wiederholungen
- Flüssigkeit
- Neugier
- Unterhaltsamkeit

Wird die Performance des Systems bewertet.

Für Aufgabenbasierte Systeme kann die Erfolgsrate und Dauer der Bearbeitung einer Aufgabe gemessen und automatisch verglichen werden.

![](TaskSuccessEvaluation.png)