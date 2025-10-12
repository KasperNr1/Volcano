# Darstellung
Ein Entity/Relationship Modell dient zur Konzeptionellen Programmierung einer Datenbank.
Es enthält die notwendigen Informationen über die Entitäten, Attribute und Beziehungen des Systems.

Die verbreitetste Form der Darstellung ist die sogenannte [Chen Notation]([Chen-Notation – Wikipedia](https://de.wikipedia.org/wiki/Chen-Notation)) 

> [!Info] Modellierungswillkür
> Es gibt zu einem realen Sachverhalt nicht immer eine eindeutige, einzig korrekte Art diesen zu modellieren. Diese Existenz verschiedener korrekter Lösungen wird auch als **"Modellierungswillkür"** bezeichnet.

## Entitäten
Eine Entität ist ein durch verschiedene Attribute beschriebenes, von anderen unterscheidbares Objekt.

Beispielsweise die Mitarbeiter "Müller", "Schmid" und "Kaiser".
Der Entitätstyp **"Mitarbeiter"** fasst sie zusammen.

Entitätstypen (Klassen) werden als Rechteck dargestellt.
![](Entities.png)

## Beziehungen
Allgemein werden Beziehungen als Raute zwischen zwei Entitätstypen dargestellt.

Beispiele:
- Mitarbeiter "Frank" betreut Kunde "Steffi"
- Mitarbeiter "Schmid" ist für Kostenstelle 0815 verantwortlich

![](Beziehung.png)

Dabei sind rekursive Beziehungen zwischen Entitäten des selben Typs möglich. Beispielsweise kann ein Mitarbeiter zu einem anderen Mitarbeiter in der Beziehung "Vorgesetzter" stehen.
Auch können mehrere Beziehungen zwischen den selben Entitätstypen bestehen. Eine Person arbeitet in einer Stadt und wohnt in einer Stadt. Dabei müssen die beiden nicht zwingend die selbe Stadt sein.

![](DoubleRelation.png)

Es können auch mehr als zwei Entitäten an einer Beziehung beteiligt sein.
![](MultiRelation.png)
Der Kritiker empfiehlt einen bestimmten Wein nicht allgemein, sondern nur in Kombination mit ausgewählten Gerichten.

## Attribute
Attribute beschreiben eine [Entität](#Entitäten) oder [Beziehung](#Beziehungen) näher aufgebaut ist. Sie werden Oval dargestellt und können selbst aus einer Reihe primitiverer Attribute zusammengesetzt sein. 

Ein doppelt umrandetes Attribut symbolisiert eine Liste von Werten. Im gezeigten Beispiel kann eine Abteilung also mehrere Telefone besitzen. Die Adresse ist ein Zusammengesetzes Attribut, erst die Werte "Straße", "PLZ" und "Ort" sind Atomar.

![](Attribute.png)

## Kardinalität
Manche [Beziehungen](#Beziehungen) sind beschränkt in der Anzahl an teilnehmenden Entitäten beschränkt. Eventuell gelten Ober- oder Untergrenzen aufgrund verschiedener [Integritätsbedingungen](Relationen.md#Integrität). Die Beschränkungen werden auf die Verbindungslinien der Beziehungen notiert.

Um darzustellen, dass ein Mitarbeiter zu beliebig vielen Projekten gehört, definiert man die Untergrenze auf $0$ und die Obergrenze auf $*$ (Unbegrenzt).
Umgekehrt besteht ein Projekt aus höchstens $12$, jedoch nicht weniger als $3$ Mitarbeitern.

![](Kardinalitäten.png)

In der Vereinfachten Notation werden lediglich die Obergrenzen notiert. Ebenfalls ist die Seite auf der die Werte notiert werden im Vergleich zur ausführlichen Variante vertauscht.

Die Selbe Relation zwischen Mitarbeitern und Projekten würde also nun folgendermaßen dargestellt. $N$ und $M$ stehen dabei für eine jeweils unbegrenzte Menge an Zuordnungen, ohne dass von beiden gleich viele existieren müssen.

![](Kardinalitäten2.png)

## Vererbung
Ähnliche Entitätstypen können in einer Vererbungsstruktur zusammengefasst werden, wenn eine Entität eine Verallgemeinerung einer anderen ist.

So wird dargestellt, dass ein Manager eine besondere Art von Mitarbeiter ist, die zusätzlich zu den normalen [Attributen](#Attribute) auch über ein Attribut "Bonus" verfügt.

![](Inheritance.png)

