# Datenbankstatistiken
Besonders die [Kostenbasierte Optimierung](10%20%20Abfrageoptimierung.md#Kostenbasierte%20Optimierung) benötigt verschiedenen Informationen.

## Statistiken für Relationen
Für jede Relation $R$ werden gespeichert:
- Die Anzahl der Tupel in der Relation $R$ $\text{ntupels}(R)$
- Der Blockungsfaktor $\text{bfactor}(R)$ der beschreibt wie viele Tupel in einen Block passen
- Die Anzahl der Blöcke $\text{nblocks}(R)$ die zur Speicherung von $R$ verwendet werden.
Falls die Blöcke physikalisch zusammenhängend gespeichert werden gilt:
$$
\text{nblocks}(R) = \left\lceil \frac{\text{ntuples(R)}}{\text{bfactor}(R)} \right\rceil
$$

## Statistiken für Attribute
Für jedes Attribut $A$ der Basisrelation $R$ wird gespeichert:
- Die Anzahl unterschiedlicher Werte $\text{ndistinct}_A(R)$
- Minimaler und Maximaler Wert von $A$ in $R$
- Die Selektionskardinalität $\text{SC}_A(R)$. Sie beschreibt wie viele Tupel im Mittel eine Gleichheitsbedingung mit $A$ erfüllen.
Falls die Werte von $A$ gleichverteilt sind entspricht die Selektionsbedingung dem Anteil der Tupel mit einem bestimmten Wert.
$$
\text{SC}_A(R) = \left \{ \begin{array}{c l} 1 & \text{Falls $A$ Schlüsselattribut in $R$ ist} \\ \left[ \frac{\text{ntuples}(R)}{\text{ndistinct}_A(R)} \right] & \text{sonst} \end{array} \right.
$$

Für Ungleichheitsbedingungen kann die Selektionskardinalität auch abgeschätzt werden.
$$
\text{SC}_{A>c}(R) = \left \lceil \text{ntuples}(R) \cdot \left( \frac{\max_A(R) - c}{\max_A(R) - \min_A(R)} \right) \right \rceil
$$
Entsprechendes gilt auch für Ungleichheiten der Form $A<c$
$$
\text{SC}_{A<c}(R) = \left \lceil \text{ntuples}(R) \cdot \left( \frac{c - \min_A(R)}{\max_A(R) - \min_A(R)} \right) \right \rceil
$$
Wenn $A$ exakt mit einem Wert einer [Menge](Intervalle%20und%20Mengen.md#Mengen) entsprechen soll gilt:

$$
A \in \{c_1, c_2, \dots, c_n \} : \left\lceil \frac{\text{ntuples(R)}}{\text{ndistinct}_A(R)} \cdot n \right\rceil
$$

Wenn mehrere Bedingungen verwendet werden kann auch dies abgeschätzt werden.
$$
A \wedge B : \frac{\text{SC}_A(R)}{\text{ntuples}(R)} \cdot \frac{\text{SC}_B(R)}{\text{ntuples}(R)} \cdot \text{ntuples}(R) = \frac{\text{SC}_A(R)-\text{SC}_B(R)}{\text{ntuples}(R)}
$$
Für das [Logische Oder](Boolsche%20Algebra.md#OR) gilt:
$$
A \vee B : \left(\frac{\text{SC}_A(R)}{\text{ntuples}(R)} + \frac{\text{SC}_B(R)}{\text{ntuples}(R)}\right) \cdot \text{ntuples}(R) - \underbrace{\frac{\text{SC}_A(R)-\text{SC}_B(R)}{\text{ntuples}(R)}}_{A \wedge B}
$$

## Statistiken für Indexe
Für einen [Index](02%20Dateiorganisation.md#Index) wird gespeichert:
- Die Anzahl der Ebenen $\text{nlevels}_A(I)$ im Baum
- Die Anzahl der Blöcke in jedem Blatt $\text{nlfblocks}_A(I)$


## Beispielstatistik
![](DatabaseStatisticsExample.png)

Für die Berechnungen wurde eine Gleichverteilung angenommen. Die Attribute $A$ und $B$ sind tatsächlich gleichverteilt, $C$ und $D$ jedoch nicht.

So ergibt sich für die Selektionskardinalität ein Fehler von $\pm 50 \%$ bei $C$ und für eine Abfrage $D = \text{'K'}$ mit einer Schätzung von $3$ bei $9$ echten Ergebnissen eine Abweichung von $300\%$ 

> [!NOTE] Vermeidung
> In echten Datenbanksystemen wird die Selektionskardinalität nicht direkt gespeichert. Öfter wird ein Histogramm der tatsächlichen Verteilung abgespeichert.


