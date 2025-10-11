# Begriffe
## Datenbank
Eine Datenbank ist immer dann sinnvoll, wenn größere Mengen an Daten über längere Zeit gespeichert werden sollen. 

> [!Info] Lebensdauer
> Wenn alle Informationen in Variablen gespeichert werden, spricht man von einer *transienten* Datenhaltung. Ein dauerhaftes Speichern über das Programmende hinaus wird als *Persistent* bezeichnet.

Eine Datenbank ist charakterisiert durch verschieden Eigenschaften
- Zusammengehörende Daten
- Dauerhafte Verfügbarkeit
- Integration
- Mehrfachbenutzbar
- [Datenintegrität](Relationen.md#Integrität)
- Sicherheit

Simples Speichern in Dateien führt bei Gleichzeitigem Zugriff von mehreren Benutzern oder Programmen leicht zu [Problemen](Parallele%20Probleme.md).

Ebenfalls ist bei der manuellen Verwaltung von Redundanzen die Gefahr für Inkonsistente Zustände groß.

## DBMS
Ein Datenbank-Management-System nimmt diese Aufgaben ab. Es bildet eine Zwischenschicht zwischen gespeicherten Dateien und Anwendern ab.

![](DBMS.png)

Ein DBMS ist eine Software zur Verwaltung einer Datenbank. Sie nimmt dabei die Verantwortung über die Verteilung von Zugriffsrechten, Datensicherung und Mehrbenutzerfähigkeit. Außerdem ist es für die Sicherung der Konsistenz und [Transaktionen](Transaktionen.md) zuständig.

Insgesamt ist es für die folgenden Funktionen zuständig:
- Datenverwaltung
- Katalog (Metadaten)
- Concurrency Control
- Transaktionen
- Recovery
- Verwaltung von Zugriffsrechten
- Kommunikationsunterstützung
- Integritätsunterstützung
- Datenunabhängigkeit

Elementarste Funktion ist dabei das Speichern, Lesen, Ändern und Löschen von Daten. Dem Benutzer sollen hier die Implementierungen verborgen bleiben.

## Informationssystem
Ist ein Werkzeug zur Erfassung und Verwaltung von Informationen. Es beinhaltet alle Elemente die zur Verwendung benötigt werden.
Dies sind allgemein:
- Die Daten
- Datenbank / [DBMS](#DBMS) Software
- Die Hardware
- Personen, die die Daten benutzen und Verwalten


## Schema & Instanz
Ähnlich wie bei Klassen und Objekten aus der Objektorientieren Programmierung wird auch bei [Datenbanken](#Datenbank) zwischen Istanzen (Objekten) und Schemen (Klassen) unterschieden. Die Instanzen enthalten konkrete Werte die sich mit der Zeit ändern können, während die Schemen starr sind und nur die Art der Daten beschreiben.


# Datenmodell
Sind Konzepte zur abstrakten Darstellung eines Ausschnitts der Welt. Diese sogenannte 'Miniwelt' spiegelt nur einige Ausgewählte Eigenschaften wieder.
Sie kann Strukturen, Operatoren, Abfragen und Constraints enthalten.

**Beispiele**
- Struktur
  Eine Abteilung hat Mitarbeiter
- Operation
  Ändere die Adresse des Mitarbeiters mit Personalnummer 12
- Abfrage
  Welche Mitarbeiter gehören zu Abteilung 3
- Constraint
  Das Alter eines Mitarbeiters muss immer $>0$ sein

Datenmodelle werden meist mit UML oder als [ER](Entity-Relationship.md) Modell dargestellt.
Aktueller Stand der Technik ist der Einsatz von *Relationellen Datenmodellen*
![](RelativeDataModel.png)

# Sichten

Eine [Relation](Relationen.md#Relation) die in der [Datenbank](#Datenbank) tatsächlich existiert heißt **"Basisrelation"**.
Sichten sind virtuelle Relationen, die aus beliebigen anderen Sichten oder Basisrelationen abgeleitet werden.
So könne Nutzer nur die jeweils relevanten Daten betrachten

Ebenfalls erleichtern sie den Umgang mit komplexeren Strukturen. Wenn eine Sicht als Grundlage für eine Abfrage verwendet wird, muss der Benutzer sich nicht mit den Verbundoperationen zum Erstellen der Sicht befassen.

![](Sichten.png)