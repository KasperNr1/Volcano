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


## Zusammengesetzte Prädikate
### Konjunktive Selektionen
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

### Disjunktive Selektionen
Bei Anfragen der Art $A = x \vee B = y \vee C = z$ muss immer linear gesucht werden, falls mindestens eines der Attribute nicht sortiert ist oder über einen Index verfügt.
Es ist möglich alle Bedingungen [parallel](Paraprog-Basics.md#Aufgabenparallelismus) abzuarbeiten.

Falls Indexe oder Sortierungen für alle Attribute vorhanden sind, kann wie im zweiten Beispiel zur [Konjunktiven Selektion](#Konjunktive%20Selektionen) gearbeitet werden, hier wird aber die Vereinigung anstelle der Schnittmenge gebildet.

# Implementierung des Verbunds
## Kardinalität des Verbunds
Beim [Kartesischen Produkt](Relationenalgebra.md#Kartesisches%20Produkt) von $R$ und $S$ gilt:
$$
\text{card}_{R\times S} = \text{ntuples}(R) \cdot \text{ntuples}(S)
$$
Die Berechnung der exakten Kardinalität ist komplex, häufig wird von diesem 'worst-Case' des Kreuzprodukts ausgegangen.
$$
\text{card}_{R\bowtie_{R.a = S.b} S} \leq \text{ntuples}(R) \cdot \text{ntuples}(S)
$$
Im Allgemeinen ist diese Aussage zu pessimistisch.
Unter der Annahme von Gleichverteilung der Attributwerte in beiden Relationen können teilweise bessere Abschätzungen getroffen werden.

Falls $A$ ein Schlüsselattribut ist, so kann ein Tupel aus $S$  maximal einem Tupel aus $R$ gleich sein.
$$
\text{ntuples}(T) \leq \text{ntuples}(S)
$$
Wenn weder $A$ noch $B$ Schlüssel sind, kann die Kardinalität des Ergebnisses wie folgt abgeschätzt werden.
$$
\text{ntuples}(T) = \text{SC}_A(R) \cdot \text{ntuples}(S) = \text{SC}_B(S) \cdot \text{ntuples}(R)
$$
Für jedes Tupel $s$ aus $S$ werden im Durchschnitt $\text{SC}_A(R)$ Tupel für das gegebene Attribut $A$ angenommen.
Die zweite Formel begründet sich analog.

## Block Nested Loop-Verbund
Ist der einfachste Algorithmus um einen Verbund zu implementieren.
Es wird in zwei verschachtelten Schleifen jede Kombination von Tupeln auf die Bedingung geprüft und ggf. zum Ergebnis hinzugefügt.

$$
\text{cost}_{\text{BNL}} = \text{nblocks}(R) + (\text{nblocks}(R) \cdot \text{nblocks}(S))
$$
Dabei kann durch Vertauschen der erste Term variiert werden.

Im Code sind vier Schleifen vorhanden da jeweils die Daten aus den Blöcken gelesen werden müssen.
``` Java
for iblock = 1 to nblocks(R){
	Rblock = read_block(R,iblock);
	
	for jblock = 1 to nblocks(S){ 
		Sblock = read_block(S,jblock);
		
		for i = 1 to ntuples(Rblock){
		
			for j = 1 to ntuples(Sblock){
			if (Join(Rblock.tuple[i].A,Sblock.tuple[j].B)){ 
				T := T ∪ (Rblock.tuple[i],Sblock.tuple[j]);
				}
			}
		}
	}
}
```

Durch Pufferung der Blöcke von $R$ können die Kosten optimiert werden. Im besten Fall ergibt sich ein Aufwand von 
$$
\text{cost}_{\text{BNL}} = \text{nblocks}(R) + \text{nblocks}(S)
$$
Falls mit Schlüsselattributen gearbeitet wird kann ggf. früher abgebrochen werden.

## Indexed Nested Loop-Verbund
Voraussetzung ist ein Index $I$ über das Verbundattribut in der inneren Relation.
Somit kann dieser Index statt der inneren Schleife verwendet werden um die passenden Tupel schneller zu finden.

```Java
 for iblock = 1 to nblocks(R){ 
	 Rblock = read_block(R,iblock); 
	 
	 for i = 1 to ntuples(Rblock){ 
		 for j = 1 to m{
		 if (Rblock.tuple[i].A = I[j]){
			 T := T ∪ Rblock.tuple[i];
			 }
		 }
	 }
 }
```

Auch hier kann analog zum [Block-nested-Join](#Block%20Nested%20Loop-Verbund) optimiert werden indem möglichst große Teile von $R$ gepuffert werden und bei Schlüsselattributen die Berechnung früher beendet werden kann.

Falls das Verbundattribut $B$ in der inneren Relation $S$ ein Primärschlüssel ist, gelten folgende Kosten:
$$
\text{cost}_{\text{INL}} = \text{nlbocks}(R) + \text{ntuples}(R) \cdot (\text{nlevels}_{B}(I)+1)
$$

Wenn für das Attribut $B$ ein [Clusterindex](02%20Dateiorganisation.md#Clusterindex) definiert ist, so bleibt:
$$
\text{cost}_{\text{INL}} = \text{nlbocks}(R) + \text{ntuples}(R) \cdot \left(\text{nlevels}_{B}(I) + \left \lceil \frac{\text{SC}_B(S)}{\text{bfactor}(S)} \right \rceil \right)
$$

## Sort Merge Join
Voraussetzung ist, dass die Dateien (oder Zwischenresultate) nach den beiden Verbundattributen sortiert sind. In diesem Fall kann das Resultat durch Mischen ermittelt werden.
![](SortMergeJoin.png)

```Java
sort(R);
sort(S);
// Führe Mischen aus
nextR = 1;
nextS = 1;
while(nextR <= ntuples(R) and nextS <= ntuples(S)){ 
	join_value = R.tuples[nextR].A;
	// Scanne S bis Wert kleiner als aktueller
	// Verbundwert gefunden wird
	while( S.tuples[nextS].A < join_value and nextS <= ntuples(S)){
		nextS = nextS + 1;
		}
	// Eventuell übereinstimmendes Tupel von R und S gefunden
	// Jedes Tupel aus S mit join_value muss mit jedem 
	// Tupel aus R mit join_value zusammengeführt werden 
	while( S.tuples[nextS].A = join_value and nextS <= ntuples(S)){
		m = nextR;
		while( R.tuples[m].A = join_value and m <= ntuples(R)){
			T := T ∪ S.tuples[nextS]+R.tuples[m] 
			m = m + 1;
			}
		nextS = nextS + 1; 
		}
	// Jetzt sind alle matchende Paare in R und S 
	// gefunden. Jetzt muss nächstes Tupel in R mit 
	// nächstem Verbundwert gesucht werden
	while( R.tuples[nextR].A = join_value
	and nextR <= ntuples(R)){
	nextR = nextR + 1;
	}
}
```

Die Kosten bei bestehender Sortierung belaufen sich auf:
$$
\text{cost}_{\text{SMJ}} = \text{nblocks}(R) + \text{nblocks}(S)
$$

Falls die Relation unsortiert ist kommen die Kosten hierzu als Vorverarbeitungsschritt dazu.
$$
\text{cost}_\text{sorting} = \text{nblocks}(R) \cdot \left \lceil \log_2(\text{nblocks}(R)) \right \rceil + \text{nblocks}(S) \cdot \left \lceil \log_2(\text{nblocks}(S)) \right \rceil
$$


## Hash-Join
In zwei Phasen werden die Relationen $R$ und $S$ erst Partitioniert und anschließend gematched.
Gemäß einer [Hashfunktion](Hashing.md) $h()$ entstehen die Partitionen $R_1, R_2, \dots, R_m$ und $S_1, S_2, \dots, S_m$.
Die Entsprechenden Partitionen enthalten die möglichen Matches und können verglichen werden. So ist die Anzahl an negativer Vergleiche deutlich reduziert.

``` Java
// Partitionierung-Phase 
for i = 1 to ntuples(R){ 
	hash_value = h(R.tuple[i].A);
	Füge Tupel R.tuple[i].A zur Partition Rj mit 
	hash_value = Rj hinzu
}
for j = 1 to ntuples(S){
	hash_value = h(S.tuple[j].B);
	Füge Tupel S.tuple[j].A zur Partition Sj mit 
	hash_value = Sj hinzu
}
// Matching-Phase
for ihash = 1 to number_partitions{
	Lese die R-Partition zum Hash-Wert ihash;
	RP = Rpartition[ihash];
	for i = 1 to max_tuples_in_R_partition(RP){
		// Baue im Speicher Hash-Index unter Verwendung 
		// von Hashfunktion h2(), verschieden h() 
		new_hash = h2(RP.tuple[i].A);
		Füge new_hash zu neuem Hash-Index hinzu;
	}
	// Scan Partition von S nach matchenden Tupeln von R 
	SP = Spartition[ihash];
	for j = 1 to max_tuples_in_S_partition(SP){
		Lese SP und sondiere Hash-Tabelle unter Verwendung 
		von h2(SP.tuple[j].B);
		Füge alle matchenden Tupel zum Resultat hinzu; 
	}
	Lösche Hash-Tabelle für nächste Partition; 
}
```

Die Kosten hierfür belaufen sich auf die dreifache Summe der Blöcke.
$$
\text{cost}_{\text{HashJ}} = 3 \cdot \left( \text{nblocks}(R) + \text{nblocks}(S) \right)
$$
Grund dafür sind die drei Folgen an Plattenzugriffen:
1. Lesen der Relationen zum Partitionieren
2. Schreiben der Partitionen
3. Nochmaliges Lesen bei der Matching-Phase

## Vergleich der Verbundimplementierungen
![](JoinImplementationComparisonExample1.png)

![](JoinImplementationComparisonExample2.png)

Generell gibt es keinen der drei Algorithmen der immer zu bevorzugen ist. In unterschiedlichen Situationen haben verschiedene Algorithmen einen großen Vorteil.

# Weitere Operationen
## Projektion
$$
S = \Pi_{A_1, A_2, \dots, A_n}(R)
$$
Im ersten von zwei Teilschritten werden die nicht benötigten Attribute entfernt.
Eventuell sind durch diese Operation unterscheidende Merkmale gelöscht worden, so dass nun Duplikate verbleiben. 

Diese Duplikate können durch Hashing oder Sortierung entfernt werden.

Falls die Projektion Schlüsselattribute enthält ist das Entfernen von Duplikaten nicht notwendig.
$$
\text{ntuples}(S) = \text{ntuples}(R)
$$

### Duplikatseliminierung
Bei einer Projektion auf ein einzelnes Nicht-Schlüsselattribut
$$
(S = \Pi_A(R)) \Rightarrow \text{ntuples}(S) = \text{ndistinct}_A(R)
$$


Beim Sortieren werden Duplikate in benachbarten Plätzen positioniert. 
Kosten dazu sind also
$$
\text{nblocks}(R) + \text{nblocks}(R) \cdot \left \lceil \log_2 (\text{nblocks}(R)) \right \rceil
$$


--- 

Beim Einsatz von Hashing werden kleine Partitionen erzeugt in denen nur wenige Elemente eingeordnet sind. Diese Partitionen können leicht auf Duplikate überprüft werden.
Dazu kann jeder Wert mit einer zweiten Hashfunktion $h_2$ verarbeitet werden. Falls es hier zu Kollisionen kommt handelt es sich mit hoher Wahrscheinlichkeit um ein Duplikat das entfernt werden kann.

Mit diesem Verfahren werden nur sehr wenige Paare verglichen die keine echten Duplikate sind.


## Aggregationen
Wie auch bei der [Duplikatseliminierung](#Duplikatseliminierung) kann der große Datensatz mit Hashing in kleinere Gruppen aufgeteilt werden.

Die Aggregatfunktion kann auf alle Gruppen einzeln angewendet werden, für Mittelwertbestimmungen kann die Summe aller Gruppen durch den Count geteilt werden, so ist es nicht notwendig den Mittelwert der Daten $0$ bis $i$ für jeden einzelnen Wert zu bestimmen.

## Mengenoperationen
Bei Mengenoperationen werden die Relationen zunächst nach dem gleichen Attribut sortiert. Dann werden die Relationen gescannt und dabei die Attribute verglichen.
Für alle drei Operationen (Vereinigung, Schnitt, Differenz) kann der Algorithmus auf Basis des [Sort-Merge](Sortieralgorithmen.md#Externes%20Sort-Merge)-Verbund Algorithmus realisiert werden.

In allen drei Fällen belaufen sich die geschätzten Kosten auf 
$$
\text{nblocks}(R) + \text{nblocks}(S) + \text{nblocks}(R) \cdot \left \lceil \log_2(\text{nblocks}(R)) \right \rceil + \text{nblocks}(S) \cdot \left \lceil \log_2(\text{nblocks}(S)) \right \rceil
$$

Die Abschätzung der Resultatsgröße ist schwierig. Es können folgende Obere und untere Schranke angegeben werden:
$$
\max(\text{ntuples}(R), \text{ntuples(S)}) \leq \text{ntuples}(T) \leq \text{ntuples}(R) + \text{ntuples(S)}
$$

Für Differenzoperationen gilt:
$$
0 \leq \text{ntuples}(T) \leq \text{ntuples}(R)
$$