Unstrukturierte Daten (Freitext in einer Überschrift) sind für einfache ML Modelle nicht verwendbar.
Strukturierte Daten müssen einem bestimmten Wertespektrum entsprechen und direkt vergleichbar sein.

![](TypesOfData.png)

## One Hot Encoding
Um Klassifikationen vergleichbar zu machen wird eine neue Spalte für jeden möglichen Eintrag hinzugefügt. Es werden also 'Flags' für die jeweiligen Optionen gesetzt.

Die letzte, redundante Spalte wird entfernt


# Statistik Wiederholung
## Satz von Bayes
Wurde in der Statistik Vorlesung bereits [behandelt](Bedingte%20Wahrscheinlichtkeit.md#Formel%20von%20Bayes)

$$
P(BW) = 0.13
$$
$$
P(S) = 0.4 \times 0.13 + 0.01 \times 0.87 = 0.0607
$$
$$
P(S \mid BW) = 0.4
$$

$$
P(BW \mid S) = \frac{P(BW) \times P(S \mid BW)}{P(S)} = \frac{0.13 \times 0.4}{0.0607} = 0,8566
$$


# Klassifikationsverfahren
## Entscheidungsbäume
Es wird wie beim Spiel "Wer bin ich" versucht Fragen zu stellen, um die Menge aller Optionen schnell abzugrenzen und in sortierte Bereiche zu trennen.

![](Entscheidungsbaum.png)

Dabei sind die Fragen nur sinnvoll, wenn sie die Datenmenge tatsächlich trennen. Eine Abfrage die in beiden Fällen auf unsortierte Daten hinausläuft ist nicht nützlich.

![](TrennLinie.png)

### Bewertung eines Baumes
Man möchte Bäume, die möglichst wenig Fehler machen und in wenigen Schritten zum Erfolg finden. Jedoch ist es nicht sinnvoll, bis zu perfekten Ergebnissen zu trainieren. Besonders hier können falsche Messungen viel unnötige Komplexität einführen.

Ein guter Baum ist also der kleinste von allen mit der selben Fehlerrate und der mit der geringsten Fehlerrate von allen mit der selben Größe.


> [!Info] Definition Größe
> Die Größe eines Baumes kann verschieden definiert sein. Es kann nach der Höhe oder der Anzahl an Blättern gezählt werden. Auch die Pfadlängensumme - also die Menge aller Entscheidungen im gesamten Baum - kann verwendet werden.

### ID3-Algorithmus
TODO - Folien ab Seite 124


> [!Example] Klausuraufgabe
> ID3-Algorithmus berechnen.
> Bzw Entropie und Information Gain verschiedener Entscheidungen vergleichen.



