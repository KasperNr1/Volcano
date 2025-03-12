# Erstellung
Der primitivste Weg eine Schaltung aus einer Vorgabe an Ein- und Ausgaben zu erstellen ist die Aufstellung der [Konjunktiven](DigitaltechnischeBegriffe.md#Konjunktiv) / [Disjunktiven](DigitaltechnischeBegriffe.md#Disjunktiv) [Normalform](DigitaltechnischeBegriffe.md#Normalform). Beispielhaft ist dieses Vorgehen bei der [Bestimmung der 2-aus-3-Schaltung](Boolsche%20Algebra.md#Bestimmung%20Schaltung) zu erkennen.

Meistens ist es erwünscht die Schaltung möglichst simpel zu gestalten.
Mit Hilfe eines [KV-Diagramms](#KV-Diagramm) kann man schnell Terme erstellen die bereits minimal sind.
So spart man sich Arbeit da ein Vereinfachen der Terme nicht mehr notwendig ist.

## KV-Diagramm
Hier dargestellt ist ein KV-Diagramm (Erfinder Karnaugh & Veitch) für Abhängigkeit von 4 Variablen.
Die geforderten Outputs werden der Reihenfolge entsprechend in die Felder eingetragen. Dabei ist die Nummer gleich der Binärzahl ABCD + 1.
![](KVDiagramm.png)
Zustände die nicht vorkommen können oder deren Ergebnis irrelevant ist, werden mit einem Eintrag 'x' als solche markiert.

Vollständig ausgefüllt könnte es folgendermaßen aussehen:
![](KvDiagramm2.png)
Um aus dieser Matrix nun die Schaltung zu bestimmen, versuch man alle $1$en mit mindestens einem Rechteck abzudecken. Dabei können die Seitenlängen nur 2er-Potenzen sein, bei einem $4\times4$ Diagramm also nur die Werte $1;2;4$. 
Jede $1$ muss abgedeckt sein, während keine $0$ enthalten sein darf.
$X$ ist egal, kann abgedeckt werden wenn dadurch ein größeres Rechteck verwendet werden kann. Die Linken & Rechten, bzw. oberen und unteren Ränder sind "verbunden", wie man am blauen Ramen erkennen kann.

Nach dem Einrahmen lässt sich der Term einfach ablesen.
$$
\overline{A} \vee B \vee \overline{C}
$$

Ein Excel Tool sollte hier [hier](C:\Users\dh10mbo\OneDrive - Durr Group\Documents\Uni\S1\Digitaltechnik\KV_Diagramme.xls) liegen:
```
"C:\Users\dh10mbo\OneDrive - Durr Group\Documents\Uni\S1\Digitaltechnik\KV_Diagramme.xlsx"
```

# Gezielte Umformung
Wenn man eine bestimmte Art elektrotechnischer Bausteine verwenden möchte, kann man logische Ausdrücke gezielt umformen um bestimmte [Verknüpfungen](Boolsche%20Algebra.md#Verknüpfungen) zu verenden.
Dazu können die [De-Morgansche Gesetze](Boolsche%20Algebra.md#De-Morgansche%20Gesetze) und andere [Rechenregeln](Boolsche%20Algebra.md#Rechenregeln) angewandt werden.

Möchte man beispielsweise die [2 aus 3 Schaltung](Boolsche%20Algebra.md#2%20aus%203%20Schaltung) ausschließlich über [NAND-Verknüpfungen](Boolsche%20Algebra.md#NAND) realisieren, so ist folgender Umformungsweg denkbar

Die Gesamte Schaltung wird doppelt negiert, diese Negation kaskadiert dann entsprechend den De-Morganschen Gesetzen weiter nach innen.
Der Prozess wird in diesem Beispiel wiederholt bis jedes ODER durch ein UND ersetzt wurde, jedes UND exakt 2 Variablen verknüpft und von einer Negation umschlossen ist.
Die Resultierende Schaltung lässt sich mit 6 NAND-Gattern realisieren, erkennbar an den insgesamt 6 Negationsstrichen innerhalb des Terms.
$$
\begin{array}{l}
w = ab \vee ac \vee bc \\
w = a(b \vee c) \vee bc \\
w = \overline{\overline{a(b \vee c) \vee bc}} \\
w = \overline{\overline{a(b \vee c)} \; \overline{(bc)}} \\
w = \overline{\overline{a} \vee \overline{(b \vee c)} \; \overline{(bc)}} \\
w = \overline{\overline{a} \vee (\overline{b} \; \overline{c})} \; \overline{\overline{(bc)}} \\
\dots \\
w = \overline{\overline{(a (\overline{\overline{b} \; \overline{c}}))} \overline{(bc)}}
\end{array}
$$
Es ist nicht zwingend notwendig den gesamten Term zu negieren, alternativ kann die Anwendung auch direkt an einzelnen Verknüpfungen stattfinden.


