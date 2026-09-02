# Entity-Relationship-Modell
Ein Entity/Relationship Modell dient zur Konzeptionellen Programmierung einer Datenbank.
Es enthält die notwendigen Informationen über die Entitäten, Attribute und Beziehungen des Systems.

Die verbreitetste Form der Darstellung ist die sogenannte [Chen-Notation](https://de.wikipedia.org/wiki/Chen-Notation).

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

# Relationenmodell
Nach der Entwicklung des [Entity-Relationship-Modells](#Entity-Relationship-Modell) wird mit dem Relationenmodell zur logischen Ebene des Entwurfs übergegangen. Dabei wir bereits ein konkretes Datenmodell festgelegt um die unterschiedlichen [Beziehungen](#Beziehungen) zu strukturieren.

Alle Elemente werden systematisch übertragen.

## Entitäten & Attribute
Jeder (Nicht an einer Generalisierung beteiligte) Entitätstyp wird auf eine [Relation](Relationen.md#Relation) abgebildet.

Alle [Attribute](#Attribute) werden dabei übernommen, wobei Verschachtelungen aufgelöst werden, sodass nur atomare Werte bestehen.

![](EntityToRelation.png)

## Beziehungen
Bei der Übertragung von Beziehungen ist die Kardinalität wichtig. Es werden 3 wesentliche Fälle unterschieden:
- 1 zu 1
  Der simpelste Fall bei dem $A$ und $B$ immer als Pärchen auftreten
  (Farbe und Komplementärfarbe)
- 1 zu $n$
  Wenn ein Objekt $A$ mehrere Objekte $B$ enthalten kann, jedes Objekt $B$ jedoch höchstens zu einem Objekt $A$ in der Beziehung steht
  (Person und Elternteil)
- $m$ zu $n$
  Wenn Zwei verschieden Entitätstypen beliebig oft miteinander auftreten können
  (Personen und Lieblingsfarben)

### 1 zu 1
In diesem Fall ist es möglich, die beiden Entitätstypen zusammenzufassen.

![](1To1PhoneNumber.png)

Da jeder Mitarbeiter in diesem Beispiel exakt eine Telefon hat und kein Gerät geteilt wird, ist es möglich die Attribute des Telefons mit den [Attributen](#Attribute) des Mitarbeiters zu kombinieren.

![](1To1Result.png)

Falls jeder Mitarbeiter "Höchstens" 1 Telefon besitzt, er also auch keines besitzen kann, so ist eine weitere Variante eventuell besser geeignet.
Hier wird das Telefon als eigene Entität eingeführt und eine **"Telefon-ID"** als Attribut der Mitarbeiter eingeführt.
Das Telefon erhält analog ein neues Attribut **"Mitarbeiter-ID"**
Bei leeren Werten wird so verhindert, dass die Attribute des Telefons nur halb gefüllt sind und ungültige Konfigurationen entstehen.

Die erste Lösung ist für Abfragen schneller, da keine [Verbund-Operation](Relationenalgebra.md#Verbund%20(Join)) notwendig ist.
In der zweiten Variante ist die Überprüfung von [Integritätsbedingungen](Relationen.md#Integrität) eventuell simpler.

### 1 zu $n$
Wie bei der zweiten Variante der Auflösung von [1 zu 1 Beziehungen](#1%20zu%201) wird ein neues Attribut eingeführt. In der mehrfach vorkommenden Entität wird die ID des eindeutigen Elements eingetragen.

![](1ToNRelation.png)

Beispielsweise kann eine Person verschiedene Email-Adressen besitzen, jede einzelne Adresse aber nur von einer Person verwendet werden.
Zu jeder Email wird die "Person-ID" eingetragen. Die Person erhält keine direkte Referenz zu den Adressen.

### $m$ zu $n$
Da für jedes Attribut immer nur ein einzelner Wert eingetragen werden kann, ist es nicht direkt möglich diese Beziehung durch hinzufügen einer einzelnen ID zu modellieren.
Die Relationen Mitarbeiter und Projekt werden nicht verändert.
Es wird eine neue [Relation](Relationen.md#Relation) eingeführt, um die Kombinationen abzubilden.  

![](nToM.png)

### N-äre Beziehungen
Beziehungen zwischen mehr als 2 Beteiligten werden analog zu [$m$ zu $n$](#$m$%20zu%20$n$) Beziehungen aufgelöst.
Es wird eine neue Relation erstellt, in der die entsprechenden Kombinationen festgehalten werden.

![](multiRelationTransformation.png)

### Selbstreferenz
#### Selbstreferenz mit 1 zu 1
Wie bei [1 zu 1](#1%20zu%201) kann die Beziehung durch Erweiterung um ein Attribut dargestellt werden. Ebenfalls kann eine neue Relation erstellt werden, mit den oben beschriebenen Vor- und Nachteilen.

#### Selbstreferenz mit $n$ zu $m$
Ähnlich wie bei einer Beziehung zwischen unterschiedlichen Entitätstypen wird eine neue Relation eingeführt. Sie stellt die Kombinationsmöglichkeiten dar und bietet Platz zum Einfügen weiterer Attribute

![](SelfReferenceNToM.png)



> [!Info] Löschverhalten
> Beim Löschen von Relationen die eine Beziehung darstellen, muss ein Verhalten für alle betroffenen Objekte definiert sein. Verbreitet sind typischerweise drei Optionen:
> - Den entsprechenden Wert auf `<Null>` setzen
> - Die Datensätze (kaskadierend) gänzlich zu löschen
> - Ersetzen mit einem Standardwert

# Normalisierung
Die Normalisierung einer Datenbank ist ein Prozess mit dem Ziel die Datenintegrität zu erhöhen, Redundanzen zu vermeiden und einige [Anomalien](05%20Transaktionssteuerung.md#Mehrbenutzerprobleme) zu vermeiden.

Dabei gibt es verschiedene Normalisierungslevel, die jeweils zusätzliche Eigenschaften gewährleisten.
Praktisch relevant sind meist nur die Normalformen 1 bis 3.

## 1. Normalform
Alle Attribute müssen atomare Werte enthalten. 

| ID   | Name           |
| ---- | -------------- |
| 0815 | Max Mustermann |
wird zu

| ID   | Vorname | Nachname   |
| ---- | ------- | ---------- |
| 0815 | Max     | Mustermann |

## 2. Normalform
Die Daten befinden sich in der [1. Normalform](#1.%20Normalform). Zusätzlich ist in jeder Relation jedes Nicht-Schlüsselattribut vom gesamten [Primärschlüssel](Relationen.md#Primärschlüssel) abhängig.

| BuchungsNr | KursNr | KursName                |
| ---------- | ------ | ----------------------- |
| 123        | 0815   | Informatik-Für-Anfänger |

> [!NOTE]- Anmerkung
> Der Primärschlüssel besteht in diesem Beispiel aus der Buchungsnummer und der KursNr

Wird zu

| BuchungsNr | KursNr |
| ---------- | ------ |
| 123        | 0815   |
und 

| KursNr | KursName                |
| ------ | ----------------------- |
| 0815   | Informatik-Für-Anfänger |

## 3. Normalform
Bei der dritten Normalform muss zusätzlich zu den Bedingungen der [2. Normalform](#2.%20Normalform) auch keine transitive Abhängigkeit von einem Nicht-Schlüsselattribut zum Primärschlüssel besteht. 


> [!NOTE]- Anmerkung
> Der Primärschlüssel besteht in diesem Beispiel aus der Buchungsnummer und der KursNr

| Buchung | KursNr | KundenNr | KundenName |
| ------- | ------ | -------- | ---------- |
| 123     | 0815   | 67       | Bodobert   |

Wird zu 

| Buchung | KursNr | KundenNr |
| ------- | ------ | -------- |
| 123     | 0815   | 67       |
und 

| KundenNr | KundenName |
| -------- | ---------- |
| 67       | Bodobert   |

## Boyce-Codd Normalform
Berücksichtigt zusätzlich zu den Eigenschaften der [3. Normalform](#3.%20Normalform) auch die Transitiven Abhängigkeiten zwischen allen [Schlüsselkandidaten](Relationen.md#Schlüsselkandidat) und nicht nur die der Primärschlüssel.

Diese Normalform befindet sich zwischen der [3. Normalform](#3.%20Normalform) und der [Vierten Normalform](#Weitere%20Normalformen)

## Weitere Normalformen
Durch entfernen Nicht-Trivialer mehrwertiger Abhängigkeiten aus der [Boyce-Codd Normalform](#Boyce-Codd%20Normalform) wird die vierte Normalform erreicht.

Die fünfte Normalform kann erreicht werden, wenn auch Verbundabhängigkeiten beseitigt werden.