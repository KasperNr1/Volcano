![](Relationen.png)
# Begriffe
## Relation
Eine Relation ist eine Gruppe von Tupeln. Jedes Tupel ist anhand eines [Primärschlüssel](#Primärschlüssel) eindeutig identifizierbar. Somit gibt es keine doppelten Einträge.

## Attribut
Ist eine Eigenschaft eines Tupels. Sie stellen die Spalten einer [Relation](#Relation) dar.

## Domäne
Die Menge der für ein [Attribut](#Attribut) zulässigen Werte.


# Schlüssel
Ein Schlüssel ist eine Reihe von Attributen die in der Lage sind einen Eintrag einer Relation eindeutig zu kennzeichnen.
![](Keys.png)

## Superschlüssel
Ist eine [Menge](Intervalle%20und%20Mengen.md#Mengen) an [Attributen](#Attribut), die einen Datensatz innerhalb einer Relation eindeutig identifiziert.

## Schlüsselkandidat
Ist ein [Superschlüssel](#Superschlüssel) der keine Teilmenge besitzt, die ebenfalls Superschlüssel ist. 
Man spricht auch von einem 'Minimalen Superschlüssel'

## Primärschlüssel
Ist die Menge an [Attributen](#Attribut) in einer [Relation](#Relation), durch die jeder Eintrag eindeutig identifiziert werden kann. Häufig wird hierfür eine eigene `ID` geführt, dies ist jedoch nicht notwendig. Der Primary Key kann auch eine Kombination aus mehreren Attributen darstellen.

Primärschlüssel ist einer der [Schlüsselkandidaten](#Schlüsselkandidat) der zur Verwendung ausgewählt wurde.

In Abbildungen von Relationen werden die als Primärschlüssel verwendeten Attribute unterstrichen dargestellt.

## Sekundärschlüssel
Sind [Schlüsselkandidaten](#Schlüsselkandidat), die nicht als [Primärschlüssel](#Primärschlüssel) ausgewählt wurden.

## Fremdschlüssel
Sind [Attribut](#Attribut)(-Mengen) innerhalb einer [Relation](Relationen.md#Relation), die in einer anderen Relation [Schlüsselkandidaten](#Schlüsselkandidat) sind.

![](ForeignKeys.png)

# Beziehungen
Eine Relation kann auch sich selbst referenzieren. Beispielsweise bei `Person` unter dem Attribut `Vorgesetzter` 
![](SelfReference.png)

Es ist auch erlaubt den leeren Wert `Null` für Felder einzutragen, die Fremdschlüssel sind.
![](EmptyForeignKey.png)

# Integrität
Datenmodelle müssen eventuell eine Reihe von Bedingungen erfüllen um sinnvoll zu sein.
Integritätsbedingungen sind Bedingungen, die die Korrektheit der Daten beschreiben. Sie werden bei der Erstellung einer Datenbank vom Benutzer definiert.

Das [DBMS](Grundlagen.md#DBMS) muss sicherstellen, dass alle Bedingungen jederzeit eingehalten werden. Nur so kann ein konsistenter und korrekter Zustand gewährleistet werden.

## Inhärente Integrität
Datensätze müssen eindeutig sein.

## Entitätsintegrität
[Primärschlüssel](#Primärschlüssel) dürfen für keinen Eintrag `NULL` sein. Jeder Primärschlüssel muss einen eindeutigen Wert haben.

![](EntityIntegrity.png)

## Referentielle Integrität
Fremdschlüssel dürfen keine Werte enthalten die nie als Primärschlüssel vorkommen.
Ebenfalls dürfen zusammengesetzte Fremdschlüssel nie teilweise ausgefüllt sein.

![](RelationalIntegrity.png)


## Relationale Integrität
Hierrunter fallen beliebige weitere, vom Anwender definierte Regeln.
Beispiele sind:
- Das Alter muss einen Wert zwischen 18 und 99 annehmen
- Einkommen muss positiv sein
- Es muss eine Hausnummer angegeben werden

## Datenscopes
Dabei können verschiedene Scopes miteinbegriffen werden. Man unterscheidet die Bedingungen anhand ihrer Reichweite.
- **Attributlokal** deckt einzelne Attribute ab (Körpergröße muss positiv sein)
- **Attributübergreifend** Bezug auf mehrere Attribute innerhalb eines Datensatz (Anfangszeit muss vor Endzeit liegen)
- **Tupellokal** Bezieht sich auf einen Datensatz (Personalnummer muss vorhanden sein)
- **Tupelübergreifend** Bezug auf mehrere Datensätze innerhalb einer Relation (Summe aller Einkommen muss geringer als 50.000 sein)
- **Intrarelational** Bezug auf eine einzelne Relation (Alle bisherigen Beispiele sind intrarelational)
- **Interrelational** Bezug auf mehrere Relationen (Vergleiche [[Relationen.md#Kardinalitätsbedingung]]) TODO Link anpassen


## Zeitliche Scopes

- **Statisch**
  Bedingungen beziehen sich auf einzelne Zustände der Datenbank.
  Beispielsweise die einzelnen Werte der Attribute
- **Transitional** Die Integritätsbedingungen beziehen sich auf Übergänge zwischen Zuständen.
  Beispielsweise darf der Status eines Projekts nicht von "Beendet" auf "Geplant" versetzt werden. 
- **Temporal** Einschränkungen beziehen sich auf ganze Folgen von Zuständen
  Jeder Wert darf maximal 10% über dem bisherigen Maximum liegen

Es ist ebenfalls möglich die Zeitpunkte der Auswertungen zu klassifizieren.

- Unmittelbar nach einer Änderung
- Nach jeder Operation
- Am Ende einer Transaktion
- Zu einem bestimmten Zeitpunkt

Nach einem Negativen Ergebnis kann die Operation abgelehnt werden (Reject) oder korrigierende Maßnahmen getroffen werden (Repair)

TODO Fortsetzung ab Folie 2-23