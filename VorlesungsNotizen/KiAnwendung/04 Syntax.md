# Definition
Sind die Regeln mit denen Wörter zu Phrasen, Satzteilen und Sätzen kombiniert werden.
Die Syntax bietet eine strukturierte Methode um sinnvolle Sätze zu bilden.

Die Anordnung von Wortarten ([Part Of Speech](03%20PartOfSpeech.md#Part%20Of%20Speech)) folgt typischerweise festen Mustern.
Dabei kann es innerhalb einer Sprache beliebig komplexe Syntaxmuster geben.

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

Es können Parsbäume erstellt werden. Aufgrund von Mehrdeutigkeiten in natürlicher Sprache sind diese jedoch nicht immer eindeutig. Lösung hierfür ist das [Probabilistische Parsing](#Probabilistisches%20Parsing)

# Probabilistisches Parsing
In einer Probabilistischen, kontextfreien Grammatik (PCFG) hat jede Produktionsregel die Form $A \to \beta[p]$.
Dabei gibt $p$ die Wahrscheinlichkeit an, dass $a \to \beta$ verwendet wird.

Die Summe der Wahrscheinlichkeiten für alle Produktionsregeln aus $A$ muss $1$ ergeben. Exakte Werte für die Produktionsregeln können aus dem Korpus ermittelt werden.

![](ProbabilisticParsing.png)

In diesem mehrdeutigen Beispiel kann "Starbucks Coffee" als Markenname interpretiert werden. Alternativ ist "Starbucks" der Name einer Person der ich Kaffee kaufe.
![](StochasticParseTrees.png)

Die Wahrscheinlichkeiten der beiden möglichen Parsbäume werden verglichen. Dazu werden die Einzelwahrscheinlichkeiten der Produktionen multipliziert.
Beispielsweise könnten die Resultate wie folgt aussehen:
- Baum 1: $3,2 \cdot 10^{-6}$
- Baum 2: $1,4 \cdot 10^{-5}$

Entsprechend würde Baum 2 ausgewählt werden, da dieser mit höherer Wahrscheinlichkeit korrekt ist.

## Limits
Einschränkung dieser Methode sind spezielle Bedeutungen einiger Wörter.

"I ate Pizza with olives" und "I ate Pizza with friends" sind grammatikalisch sehr ähnlich, wobei Oliven als Zutat und Freunde als Begleitung interpretiert werden sollten.

Diese Abhängigkeit wird ignoriert, die Bäume werden nur nach den Häufigkeiten im Korpus gebildet.

Eine weitere Hürde ist die große Menge der benötigten Trainingsdaten. Um Anomalien in den gemessenen Wahrscheinlichkeiten zu minimieren, sind sehr viele Messwerte notwendig.
Entsprechend hat das Modell Schwierigkeiten im Umgang mit neuartigen oder ungewöhnlichen Satzkonstruktionen.