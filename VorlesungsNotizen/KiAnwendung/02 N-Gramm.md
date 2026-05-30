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

## N-Gramm Modell
Ein N-Gramm bezeichnet eine Sequenz von $N$ aufeinanderfolgenden Fragmenten in einem Text
Es gibt also Unigramme, Bigramme, Trigramme usw.
Die Fragmente können Wörter oder [Tokens](#Token) sein.
![](NGrammSplitting.png)


> [!Example] Klausuraufgabe
> Satz in Fragmente spalten.
> Beachte Beispiel für 2. und 3. :
> manche Tokens werden. mehrfach gezählt um stets vollständige Fragmente zu erhalten.
> z.B. "Ist ein" bei Trigramm


### Vorhersage
Um ein kommendes Wort vorherzusagen, wird der bisherige Text und die [bedingte Wahrscheinlichkeit](Bedingte%20Wahrscheinlichtkeit.md#Bedingte%20Wahrscheinlichkeiten) der jeweiligen Fortsetzung verwendet.

Da die jeweiligen [Pfade](Bedingte%20Wahrscheinlichtkeit.md#Pfadregel) sehr spezifisch sind, ist die Wahrscheinlichkeit einer bestimmten Fortsetzung fast immer $0$.

$$
P(\text{that} \mid \text{The garden is so beautiful}) = \frac{P(\text{The garden is so beautiful that})}{P(\text{The garden is so beautiful})} \approx 0.0
$$

Der lange Kontext kann in eine Reihe kleinerer Tokens aufgeteilt werden. So steigt die Häufigkeit mit der Tokens in mehreren Kontexten verwendet werden können.

Es gilt [die Kettenregel der Wahrscheinlichkeitsrechnung](Bedingte%20Wahrscheinlichtkeit.md#Satz):
$$
P(x_1 \wedge x_2 \wedge \dots \wedge x_n) = P(x_1) \cdot P(x_2 \mid x_1) \cdot \dots \cdot P(x_n \mid x_1, x_2, \dots, x_{n-1})
$$

Somit lässt sich die obige Vorhersage also auch ausdrücken als:
$$
P(\text{The garden is so beautiful that}) = P(\text{The}) \cdot P(\text{garden} \mid \text{The}) \cdot \ldots \cdot P(\text{that} \mid \text{The garden is so beautiful})
$$

Diese Berechnung ist allerdings sehr mühsam. Mithilfe von [Markov Ketten](#Markov%20Ketten) kann das Problem gelöst werden.

## Markov Ketten
Wandelt diese langen Folgen an Wahrscheinlichkeiten in Zustände um, die nur jeweils vom vorherigen Zustand abhängen. Somit wird die Berechnung deutlich erleichtert

Es entsteht für beliebig komplexe Pfade durch die gegebenen Zustände jeweils ein Produkt aus den Übergangswahrscheinlichkeiten, das leicht berechnet werden kann.

![](MarkovChain.png)

Während die Berechnung der Einzelwahrscheinlichkeiten der jeweiligen Fortsetzung korrekt ist, ist die Bestimmung dieser Wahrscheinlichkeiten aufgrund der Vielzahl möglicher Kombinatinoen extrem mühsam.
Wenn diese Wahrscheinlichkeiten aus einem Text erlernt werden sollen, müsste ein enorm riesiges Volumen an Trainingsdaten verwendet werden, um auch die seltenen Kombinationen sinnvoll abzubilden.

Markov hat gezeigt, dass sich diese Wahrscheinlichkeiten mit einem deutlich simpleren Verfahren approximieren lassen.
$$
P(w_n \mid w_1^{n-1}) \approx P(w_n \mid w_{n-N+1}^{n-1})
$$
Dabei ist mit $w_a^b$ die Wortfolge von $a$ bis $b$ und mit $N$ die Länge des von Markov verwendeten Kontexts gemeint.
Im linken Term wird jeweils der gesamte Kontext verwendet, im rechten nur die letzten $N$ Wörter. Somit skaliert das Verfahren deutlich besser.
Allgemein lässt sich für die Wahrscheinlichkeit einer Wortfolge somit sagen:
$$
P(n_1^n) \approx \prod_{k=1}^{n}P(w_k \mid w_{k-1})
$$
Die Ursprünglich komplexe Wahrscheinlichkeit kann also durch eine Folge von Bigrammen berechnet werden.

# Language Model Evaluation
Testdaten stammen aus der selben Quelle wie Trainingsdaten, ohne in den Trainingsdaten enthalten zu sein.

Es gibt Intrinsische und Extrinsische Bewertungen
Bei der intrinsischen Bewertung wird die Leistung des Modells automatisch bestimmt, anhand verschiedener linguistischer oder statistischer Merkmale.
Extrinsische Evaluation erfolgt anhand der Qualität von Übersetzungen oder anderen Arbeiten durch Menschen oder [LLMs](10%20LLMs.md).

Ein solche automatisch bestimmbarer Wert ist die 'Perplexity'. Er beschreibt dabei, wie "überrascht" das Modell von den Trainingsdaten ist, während es versucht diese vorherzusagen. Ein geringer Zahlenwert bedeutet, dass die Vorhersage akkurat ist.

$$
\text{Perplexity} = 2^{-\frac{1}{N} \sum_{i=1}^{N} \log_2 \left(P(w_i)\right)}
$$
Seien für den Satz "Der Hund bellt" die Worte mit einer Wahrscheinlichkeit von $0.3; 0.4; 0.2$ vorhergesagt worden, so ist die Perplexity:
$$
\text{Perplexity} = 2^{-\frac{1}{3}\left( \log_2 0.3 + \log_2 0.4 + \log_2 0.2 \right)} \approx 3.4668
$$

Mit diesem Wert können Modelle relativ zueinander verglichen werden.

## Smoothing
Verhindert das Auftreten von Wahrscheinlichkeiten $0$ bei unbekannten Kombinationen. Somit wird die Stabilität des Modells erhöht, da alle Wahrscheinlichkeiten miteinander multipliziert werden.

Manche Nullen sind gewünscht, etwa wenn die Kombination von zwei Wörter Grammatikalisch falsch ist und nicht auftreten kann.

### Zipfsches Gesetz
Häufige Wörter kommen oft vor, seltene nur wenige Male.
Präziser ausgedrückt erscheint das Wort das auf Platz $n$ der Häufigkeitsrangliste mit einer Wahrscheinlichkeit von $\dfrac{1}{n}$ an einer beliebigen Stelle im Text.

![](ZipfDistribution.png)

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
