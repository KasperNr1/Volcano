Unstrukturierte Daten (Freitext in einer Überschrift) sind für einfache ML Modelle nicht verwendbar.
Strukturierte Daten müssen einem bestimmten Wertespektrum entsprechen und direkt vergleichbar sein.

![](TypesOfData.png)

## One Hot Encoding
Um Klassifikationen vergleichbar zu machen wird eine neue Spalte für jeden möglichen Eintrag hinzugefügt. Es werden also 'Flags' für die jeweiligen Optionen gesetzt.

Die letzte, redundante Spalte wird entfernt


# Statistik Wiederholung
## Satz von Beyes
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

