# Grundbegriffe
## Korpuslinguistik
Ein Bereich der Sprachwissenschaft der sich mit der empirischen Untersuchung von großer Sammlungen an Text befasst.
Wie auch maschinelles Lernen basiert die Erstellung von Modellen anhand von Beispielen, nicht anhand von festen Regeln

## Satz
Eine schriftliche Spracheinheit mit grammatikalisch geordneten Wörtern, die eine vollständige Aussage bilden und unabhängig vom Kontext sind.

## Äußerung
Eine gesprochene Spracheinheit, die kontextabhängig sein kann und auch unvollständige [Sätze](#Satz) oder Wörter und Geräusche umfassen kann.

## Wortform
Eine Wortform ist eine spezifische, [flektierte](#Flexion) Form eines Wortes

## Flexion
Besondere Form eines Wortes um eine bestimmte Information über Fall, Zahl, Geschlecht zu beinhalten.

## Typen
Bezeichnet die [Menge](Intervalle%20und%20Mengen.md) der einzigartigen Wörter in einem Korpus, unabhängig wie oft sie tatsächlich vorkommen.

## Token
Die tatsächlich vorkommenden Wörter in einem Text, bei wiederholtem Vorkommen werden auch mehrere Tokens erkannt.

## Stamm
Wortstamm eines Wortes. Der Wortstamm ist für jede [Flexion](#Flexion) eines Wortes gleich.
Der Stamm wird beim "Stemming" gebildet und ist nicht immer ein eigenständiges Wort

> [!Example] Beispiel
> - "laufend" $\to$ "lauf"
> - "glücklich" $\to$ "glück"
> - "Autos" $\to$ "Auto"
## Lemma
Ein Lemma ist die Grundform von Wörtern mit gleichem [Stamm](#Stamm), Wortart und Bedeutung

> [!Example] Beispiel
> - "laufend" $\to$ "laufen"
> - "besser" $\to$ "gut"
> - "Autos" $\to$ "Auto"


> [!Info] Unterschied [Stamm](#Stamm) und [Lemma](#Lemma)
> ![](StemmingVsLemma.jpeg)


# Wahrscheinlichkeitsmethode
Bei der klassischen "Autovervollständigung" wird meist simpel mit den [Wahrscheinlichkeitsverteilung](Einführung.md#Wahrscheinlichkeitmaß%20/%20Wahrscheinlichkeitsverteilung) der Wörter im Korpus gelernt.

![](AutoComplete.png)

# N-Gramm Modell
Ein N-Gramm bezeichnet eine Sequenz von $N$ aufeinanderfolgenden Fragmenten in einem Text
Es gibt also Unigramme, Bigramme, Trigramme usw.
Die Fragmente können Wörter oder [Tokens](#Token)
![](NGrammSplitting.png)


> [!Example] Klausuraufgabe
> Satz in Fragmente spalten.
> Beachte Beispiel für 2. und 3. :
> manche Tokens werden. mehrfach gezählt um stets vollständige Fragmente zu erhalten.
> z.B. "Ist ein" bei Trigramm



> [!Missing] Kettenregel
> Hier fehlt etwas zur Kettenregel (Seite 65)
> Es geht um die Wahrscheinlichkeit ganzer Sätze zu generieren, basierend auf der wiederholten Generation von einzelnen Wörtern in der Folge auf einander.

# Markov Ketten
Wandelt diese langen Folgen an Wahrscheinlichkeiten in Zustände um, die nur jeweils vom vorherigen Zustand abhängen. Somit wird die Berechnung deutlich erleichtert.

# Language Model Evaluation
Testdaten stammen aus der selben Quelle wie Trainingsdaten, ohne in den Trainingsdaten enthalten zu sein.

Es gibt Intrinsische und Extrinsische Bewertungen
(Seite 82)

Niedriger Perplexitätswert $\to$ Gute Vorhersage auf Testdaten

## Smoothing
Verhindert das Auftreten von Wahrscheinlichkeiten $0$ bei unbekannten Kombinationen. Somit wird die Stabilität des Modells erhöht, da alle Wahrscheinlichkeiten miteinander multipliziert werden.

Manche Nullen sind gewünscht, etwa wenn die Kombination von zwei Wörter Grammatikalisch falsch ist und nicht auftreten kann.

### Zipfsches Gesetz
Häufige Wörter kommen oft vor, seltene nur wenige Male.
Somit sind [Bigramme](#N-Gramm%20Modell) mit zwei seltenen Wörtern statistisch nicht belastbar.

Jedes N-Gramm-Trainingsmatrix ist aufgrund dieses Gesetzes dünn besetzt.


> [!Info] Hinweis
> "Dünn besetzt" bedeutet, dass die Mehrheit der Einträge Null ist

Mit verschiedenen Verfahren wird dem entgegengewirkt
(Seite 90)
- Laplace-Smoothing
- Additives Smoothing
- Good-Turing-Smoothing
- Kneser-Ney-Smoothing
