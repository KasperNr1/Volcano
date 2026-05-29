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

# Implementierung der Selektion
Basierend auf der Dateiorganisation und der möglichen Indexierung der Attribute in der Selektionsbedingung kann zwischen vielen bekannten Verfahren entschieden werden.


> [!MISSING] TODO
> Formeln für Kosten der Operationen einfügen

## Lineare Suche
Wenn die Datei nicht sortiert ist und kein Index existiert, so muss linear jeder Wert geprüft werden.

Falls die Werte eindeutig sind, so ist im Mittel der Zugriff auf $\dfrac{n}{2}$ der Werte nötig.
Falls Werte nicht-Eindeutig sind muss auf alle $n$ Werte zugegriffen werden.

## Binäre Suche
Wie auch [Binary Search](Suchalgorithmen.md#Binary%20Search) für das durchsuchen des Hauptspeichers halbiert dieses Verfahren mit jedem Schritt den Suchraum.
Der Inhalt der Blöcke muss dabei gemäß dem Suchkriterium und über Blöcke hinweg sortiert sein.
So kann mit logarithmischen Kosten der passende Block gefunden werden.

## Gleichheit auf Hashschlüssel
Falls das gesuchte Attribut $A$ ein Hashschlüssel ist, so kann dieser zur Berechnung der Zieladresse verwendet werden.
Der Aufwand zur Suche ist damit Konstant.

## Gleichheit auf Primärschlüssel
Für eine Bedinung $A = x$ auf dem Primärschlüsselattribut $A$ kann der [Primärindex](02%20Dateiorganisation.md#Primärindex) zur Suche verwendet werden. 
Somit ist zur Suche ein Schritt für jedes Level im Indexbaum notwendig.

Bei Ungleichheit kann zuerst nach dem Tupel mit exakt gleichen Wert gesucht werden. Im sortierten Index sind alle Werte davor oder danach größer oder kleiner.

## Gleichheit auf (Sekundärem) Clusterindex
Wenn das Prädikat eine Gleichheitsbedingung über $A$ formuliert, das nicht Primärschlüssel ist, für das aber ein sekundärer [Clusterindex](02%20Dateiorganisation.md#Clusterindex) definiert ist, kann dieser Index verwendet werden.

Es wird mit dem Index der Grenzwert gefunden bei dem die Bedingung zum ersten Mal erfüllt ist, die folgenden Blöcke werden linear durchsucht um das Ende des Clusters zu finden.

## Gleichheit auf (Sekundärem) Nicht-Clusterindex
In einem nicht geclusterten [Sekundärindex](02%20Dateiorganisation.md#Sekundärindex) kann die Eigenschaft der Sortierung nicht verwendet werden.

Es müssen alle Einträge gelesen werden. Da die Daten nicht nach dem Indexattribut sortiert sind, muss angenommen werden, dass sie sich in jeweils unterschiedlichen Blöcken befinden.

## Ungleichheit auf B+ Baum-Index
Im [B+ Bäume](03%20Baumbasierte%20Indexstrukturen.md#B+%20Bäume) muss in jedem Knoten im Mittel die Hälfte der Einträge gelesen werden um zum nächsten Knoten zu gelangen. Nachdem jedes Level des Baumes durchlaufen ist, gelangt man beim Datenpunkt an.


# Zusammengesetzte Prädikate
## Konjunktive Selektionen
Bei Anfragen der Art $A = x \wedge B = y \wedge C = z$ kann durch die Wahl der Reihenfolge optimiert werden.
Attribute mit Index oder Sortierung sollen dabei bevorzugt werden. Auch sollen stärker selektierende Attribute vor solchen bevorzugt werden, die schwächer selektieren und somit größere Zwischenergebnisse liefern würden.

> [!Info] Sortierung Großer Relationen
> Wenn Relationen sehr groß werden können sie nicht mehr mit klassischen Sortieralgorithmen sortiert werden, da diese aufgrund der langsamen Zugriffszeiten auf den Sekundärspeicher nicht optimal sind.
> 
> Stattdessen werden spezialisierte Algorithmen wie [Externes Sort-Merge](Sortieralgorithmen.md#Externes%20Sort-Merge) verwendet.

Fall im genannten Beispiel ein Index über $A$ und $B$ existiert und $\text{ndistinct}_A(R) < \text{ndistinct}_B(R)$ gilt, so würde in der folgenden Reihenfolge gearbeitet werden:
![](SqlSelectionExecutionOrderExample.png)

Alternativ könnten die beiden Indexe durchsucht werden und die Schnittmenge der Zeiger als Zwischenresultat weitergegeben werden.
![](SqlSelectionThroughIndexCombination.png)

## Disjunktive Selektionen
Bei Anfragen der Art $A = x \vee B = y \vee C = z$ muss immer linear gesucht werden, falls mindestens eines der Attribute nicht sortiert ist oder über einen Index verfügt.
Es ist möglich alle Bedingungen [parallel](Paraprog-Basics.md#Aufgabenparallelismus) abzuarbeiten.

Falls Indexe oder Sortierungen für alle Attribute vorhanden sind, kann wie im zweiten Beispiel zur [Konjunktiven Selektion](#Konjunktive%20Selektionen) gearbeitet werden, hier wird aber die Vereinigung anstelle der Schnittmenge gebildet.

