# Klausur
## Hilfsmittel
Klausur mit 4 Seiten (2 Blatt Papier) als Hilfsmittel

## Inhalt
[01 Einführung](VorlesungsNotizen/KiAnwendung/01%20Einführung.md) bis einschließlich [10 LLMs](10%20LLMs.md)
(Seite 628)

# Fragen
## Markov Ketten
[Markov Ketten](02%20N-Gramm.md#Markov%20Ketten) anschauen (Skript Seite 68-80)

## Kasusrollen - NPs
Was sind NPs in [Regeln der Kasusrollen](05%20Bedeutungsdarstellung.md#Regeln%20der%20Kasusrollen) (Skript Seite 227)

## Hobbs-Algorithmus
Wann terminiert der [Hobbs-Algorithmus](#Hobbs-Algorithmus)?
Beim Fund der ersten Antezedens? Konflikt mit der Bedingung in Schritt 8

Nicht In Klausur relevant.

## Centering-Algorithmus
Wie ist die Rangordnung von Worten festgelegt?

Warum wird im [Centering-Beispiel](07%20Pragmatische%20Analyse.md#Centering-Beispiel) bei $U_3$ nicht auch der Fall betrachtet, bei dem "She" sich auf "Jane" bezieht?
(Skript Seite 398)

Wird betrachtet, nur nicht explizit auf der Folie (Smooth Shfit > Continue) Als Anmerkung zu den Ergebnissen

## RNN
### Modell Dimensionen
Was ist die Embedding-Dimension und die Verborgene Dimension? Und warum ist es hilfreich anzunehmen, dass sie gleich groß sind.
[Architektur](08%20Transformer.md#Architektur)
Skript Seite 461

Embedding-Dimension ist die Dimension des Embedding-Raums.
Verborgene Dimension ist die Anzahl d. Neuronen im Versteckten Layer

### Layers
Inwieweit wird mit Schichten aus Neuronen gearbeitet?
Es ist teilweise die Rede von 'einer internen Zelle' bei [Long Short-Term Memory (LSTM) Network](08%20Transformer.md#Long%20Short-Term%20Memory%20(LSTM)%20Network) und [Gated Recurrent Unit (GRU)](08%20Transformer.md#Gated%20Recurrent%20Unit%20(GRU))

Ein Wert pro LSTM-Neuron (Können auch mit normalen Neuronen kombiniert werden)

## Transformer
Layer-Normalisierung
Wird auf Seite 511 als Bestandteil der [Encoder](09%20More%20Transformer.md#Encoder) genannt.
Was ist damit gemeint?

## Encoder
Warum sind alle Sublayer genau gleich?
Müssen sie das zwingend sein?
[Encoder](09%20More%20Transformer.md#Encoder)
Skript Seite 512

In der Standardarchitektur nicht vorgesehen, prinzipiell möglich.
