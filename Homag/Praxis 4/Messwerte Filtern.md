https://stats.stackexchange.com/questions/16207/correcting-for-outliers-in-a-running-average
# Algorithmus
## Daten
Speichern der letzten $n$ Ergebnisse, vermutlich als Ringbuffer um Speicherplatz zu begrenzen. Beim Start entweder alle Werte zulassen bis der Buffer zum ersten Mal gefüllt ist, oder Initiale Werte festlegen.

Mehr gespeicherte Ergebnisse sind bei stärkerer Schwankung der korrekten Daten sinnvoll, da $\sigma$ dann größer wird.

## Berechnung
Berechnen von Mittelwert $\mu$ und Standardabweichung $\sigma$ .

### Mittelwert (Arithmetisch)

$$
\mu = \frac{1}{n} \cdot \sum_{i=0}^{n-1} x_i 
$$
Wobei $n$ die Anzahl der gespeicherten Werte ist und jedes $x_i$ für einen einzelnen Wert steht.
### Standardabweichung
$$
\sigma = \frac{1}{n} \cdot \sum_{i=0}^{n-1} \left(\mu - x_i \right)^2
$$
Also die Quadratsumme der Differenzen jedes Messwerts zum Mittelwert, skaliert mit der Anzahl der Messwerte.
## Entscheidung
Einen neuen Wert $x$ nur in den Buffer aufnehmen wenn 
$$
\left| \sigma - x \right| < a \cdot \sigma
$$
Also der Messwert um maximal $a$ Standardabweichungen vom bisherigen Mittelwert abweicht.
Je größer $a$ gewählt wird, desto größere Abweichungen werden als "gültig" zugelassen, bester Wert müsste mit echten Daten experimentell bestimmt werden.