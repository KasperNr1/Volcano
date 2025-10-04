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