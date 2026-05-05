# ETL
[Extraktion](#Extraktion), [Transformation](#Transformation) und [Laden](#Laden) sind die drei großen Schritte die von Daten auf dem Weg von ihrer Quelle in das DWH durchlaufen.
Dazu gehören die Überwachung von Datenquellen und das Entdecken von Änderungen, sowie auch das Anpassen von Einheiten und Codierungen und das Laden ins DWH.

Dieser Prozess läuft typischerweise nicht komplett im Hauptspeicher ab, es werden einer oder mehrere Zwischenspeicher (Data Staging Area) verwendet.

![](EtlFlowChart.png)

## Extraktion
Lieferzeitpunkt der Daten kann Periodisch sein, auch synchron (In Echtzeit mit Änderung der Daten in der Quelle) oder Ereignisgesteuert.

Beim Nachladen können Snapshots oder nur Änderungen geliefert werden. Hier wird Datenmenge gegen Aufwand aufgewogen.

## Transformation
### Selektion
Es können Daten gefiltert werden, sodass nur die Datensätze gespeichert werden, bei denen eine bestimmte Bedingung erfüllt ist.

### Projektion
Auch Projektionen sind häufig, wenn nicht alle Attribute der Quelldaten relevant sind.

### Pivotisierung
Bei einer Pivotisierung werden Zeilen in Spalten verwandelt. So können neue Erkenntnisse visualisiert werden, die eventuell nicht Ziel der Analyse in der Datenquelle waren.
![](Pivotisierung.png)

### Korrektur
Automatisches Erkennen und Korrigieren ist möglich, wenn gewisse Eigenschaften festen bekannten Mustern folgen. Die Korrektheit der Daten kann überprüft werden, bevor diese blind kopiert werden.

### Formatieren
Felder des selben Datentyps können in unterschiedlichen Quellen in verschiedenen Formaten existieren. Es ist sinnvoll beispielsweise Namen einheitlich in Vor- Nach- und Namenszusätze zu teilen.
### Aggregation
![](AggregationForTransformation.png)
Wenn die Daten detaillierter vorliegen als sie im Ziel benötigt werden können sie zusammengefasst und vereinfacht werden.

### Disaggregation
Bei großen Objekten kann es sinnvoll sein einige Attribute in eine separate Detailtabelle auszulagern. So werden alle Informationen beibehalten, ohne Benutzer zu stören während diese Daten nicht genutzt werden.
![](Disaggregation.png)

### Konvertieren
Konvertieren von Einheiten ist wichtig, insbesondere wenn verschiedene Formate oder Einheiten in den Quellen üblich sind.
Besonders bei Uhrzeiten kann diese Umwandlung Probleme bereiten, aufgrund von verschiedener Zeitzonen und Winter- Sommerzeitverschiebung ist die Erkennung einer eindeutigen Reihenfolge schwierig.
Währungen sind ebenfalls problematisch, da hier die Umrechnungskurse teilweise minütlich schwanken können.
Typischerweise werden solche Umrechnungen vom Nutzen der konkreten Anwendung abhängig gemacht, häufig wird der Wert in der ursprünglichen Währung und einer umgewandelten Form als Referenz gespeichert.

### Matching
Daten können in unterschiedlichen Daten doppelt vorliegen. Um mehrfache Speicherung von z.B. Kundendaten zu vermeiden können diese anhand bestimmter Kriterien als identisch erkannt und zusammengefasst werden.

### Konsistenzprüfung
Manche Daten dürfen nur bestimmte Werte enthalten. Solche Einträge bei denen die Bedingung verletzt sind, können zur manuellen Überprüfung zurückgehalten werden oder automatisiert behandelt / verworfen werden.

### Codierung vereinheitlichen
Z.B. könnte der Eintrag für Geschlecht in einer Quelle als M/F und in einer anderen als 1 und 0 gespeichert sein.

### Berechnung abgeleiteter Werte
![](DerivedValuesInTransformation.png)
Falls für den Anwendungsfall abgeleitete Werte relevant sind können diese direkt berechnet werden.

### Abgleich
Vergleich von Quelle und Ziel (z.B. Anzahl aktiver Kunden) um Vollständigkeit der Datensätze zu überprüfen.
Dieser Schritt kann in belieber Granularität ausgeführt werden um auch feinere Fehler zu erkennen.

## Laden
Bringt Daten ins Warehouse, mit verschiedenen Strategien abhängig von den Anforderungen und dem Zeitfenster.
Die Aktualisierung kann auch in verschiedenen Intervallen erfolgen und an den Erfolg der [vorherigen Transformationen](#Transformation) gekoppelt sein.

# ETL Architekturen
Können in zwei Teilkomponenten unterteilt werden.
- Datenquelle zu Staging Area
- Staging Area zu DWH

![](EtlSourceToStaging.png)

![](EtlStagingToDwh.png)
Beide Teilkomponenten existieren in verschiedenen Realisierungsformen.
- Individuallösungen
- Teil einer Suite (Oracle / Microsoft)
- Werkzeuge für spezielle Operationen
	- DataCleanser von EDD: Speziell zur Duplikateliminierung

Dabei ist das ETL-Tool im Idealfall die einzige Komponente die mit dem DWH kommuniziert, so kann zentral gearbeitet und überwacht werden. Es sind verschiedene Arten des Monitoring und Loggin möglich, auch Fehler können sauber erkannt und behandelt werden. 

## Individuallösungen
Können mit verschiedensten Tools implementiert sein, von Shell- und Skriptsprachen, höherer Programmiersprachen wie C/C++ oder im [DBS](VorlesungsNotizen/Datenbanken2/01%20Grundlagen.md#Datenbanksystem%20(DBS)) integrierte Sprachen wie PL/SQL.

Die Prozesse sind nicht unbedingt gut dokumentiert und somit schlecht nachvollziehbar. Der Einsatz verschiedenster Technologien und Tools macht die Systeme unübersichtlich und somit schlecht wart-oder erweiterbar.


# Datenbankerweiterungen
## Externe Tabellen
Außerhalb der eigentlichen Datenbank können weitere Tabellen angelegt werden. So kann auch mit Dateien gearbeitet werden, die nicht vom [DBMS](VorlesungsNotizen/Datenbanken2/01%20Grundlagen.md#Datenbankmanagementsystem%20(DBMS)) verwaltet werden.

Um eine solche Tabelle anzulegen wird analog zur Erstellung von internen Tabellen gearbeitet.
```SQL
CREATE TABLE <Externer Tabellenname>(
<Attribut 1> <Datentyp 1>,
<Attribut 2> <Datentyp 2>,
...)
ORGANIZATION EXTERNAL
(TYPE oracle_loader
DEFAULT DIRECTORY <Verzeichnis>
ACCESS PARAMETERS
(<Zugriffsparameter>)
LOCATION (<Name der Datei>)
REJECT LIMIT (<Parameter>);
```
Dabei ist die Arbeit mit Constraints nicht möglich.

Das angegebene Format wird erst beim Stellen einer Anfrage überprüft. Falls es korrekt ist, kann nun wie auf eine interne Tabelle zugegriffen werden.
Dabei ist der Zugriff allerdings nur lesend möglich.

Im Allgemeinen ist der Zugriff auf CSV Dateien größer als der auf Dateien fester Größe, Grund dafür ist der zusätzliche Aufwand beim Parsen.

### Beispiel
Sei folgende `CSV`Datei mit Kundendaten gegeben
``` csv
0000000001#Rupp#Talke# 1500,11
0000000002#Hamann#Judith# 2540,81
0000000003#Novincak#Ute# 2313,92
0000000004#Riemann#Bettina# 1208,06
0000000005#Meier#Ottilie# 2886,08
...
```

oder mit festen Feldgrößen:
```
0000000001 Rupp     Talke   1500,11
0000000002 Hamann   Judith  2540,81
0000000003 Novincak Ute     2313,92
0000000004 Riemann  Bettina 1208,06
0000000005 Meier    Ottilie 2886,08
...
```

Um ihren Inhalt auszulesen würde folgender Code verwendet werden
``` SQL
CREATE OR REPLACE DIRECTORY Quellverzeichnis AS 'C:/DWH/';

CREATE TABLE Kunden_Extern( -- Definition der Attribute
	ID      NUMBER(10),
	NAME    VARCHAR2(50),
	VORNAME VARCHAR2(50),
	UMSATZ  NUMBER(10,2))
	
	ORGANIZATION EXTERNAL -- Externe Tabelle
		(TYPE oracle_loader -- Ladewerkzeug
		DEFAULT DIRECTORY Quellverzeichnis --Verzeichnis
		ACCESS PARAMETERS -- Beschreibung der Datei
			(RECORDS DELIMITED BY NEWLINE
			FIELDS TERMINATED BY '#'
			OPTIONALLY ENLCOSED BY '"'
			)
		LOCATION ('KUNDEN.txt') -- Quelldatei
	)
REJECT LIMIT UNLIMITED;
```


Um die Datei fester Größe zu verwenden muss nur die Beschreibung der Quelldatei angepasst werden.
``` SQL
ACCESS PARAMETERS
	(RECORDS DELIMITED BY NEWLINE
	FIELDS(
		ID      CHAR(10),
		NAME    CHAR(20),
		VORNAME CHAR(20),
		UMSATZ  CHAR(10)
	)
```

## Multiple Insert
Standard SQL erlaubt mit einer `INSERT` Anweisung nur das Einfügen in eine Tabelle.
Mit `INSERT ALL` und `INSERT FIRST` kann auch in mehrere Tabellen eingefügt werden.

Dabei wird mit `WHEN <Bedingung> THEN`gearbeitet.

``` SQL
INSERT FIRST
	WHEN Umsatz>4000 THEN INTO Kunde_Kat_I
	WHEN Umsatz>3500 THEN INTO Kunde_Kat_II
	WHEN Umsatz>3000 THEN INTO Kunde_Kat_III
	SELECT * FROM Kunden_Extern_Fest;
```

Das `FIRST` sorgt für Einfügen in der ersten passenden Tabelle, somit ist die Reihenfolge der Abfragen relevant.

Der selbe Effekt mit Standard SQL bedarf mehrerer einzelner Anfragen.
``` SQL
INSERT
INTO Kunde_Kat_I
SELECT *
FROM Kunden_Extern
WHERE Umsatz > 4000;

INSERT
INTO Kunde_Kat_II
SELECT *
FROM Kunden_Extern
WHERE Umsatz BETWEEN 3499 AND 4000;

INSERT
INTO Kunde_Kat_III
SELECT *
FROM Kunden_Extern
WHERE Umsatz BETWEEN 3000 AND 3499;
```

Die Erweiterung bietet entsprechend signifikante Zeitersparnisse bei der Berechnung.

## Merge Into
Standard SQL erlaubt nur Aktualisierungs- oder Einfügeoperationen. Mit `MERGE INTO` ist eine kombinierte Anweisung möglich.
Falls ein Datensatz nicht existiert, so soll er erstellt werden. Alle bereits existierenden Werte sollen angepasst werden.

![](MergeIntoRawData.png)

``` SQL
MERGE INTO F
	USING NeueDaten N
	ON (F.ID1=N.ID1
		AND F.ID2=N.ID2 
		AND F.ID3=N.ID3)
	WHEN MATCHED THEN
		UPDATE SET F.VALUE = F.VALUE + N.VALUE
	WHEN NOT MATCHED THEN
		INSERT VALUES (N.ID1,N.ID2,N.ID3,N.VALUE);
```

![](MergeIntoResult.png)

## Bulk Loader
![](BulkLoaderArchitecture.png)

Um bei großen Einfügeoperationen Performance zu gewinnen, wird der klassische Weg durch das DBMS umgangen. 
Die Konsistenz und Korrektheit wird extern geprüft und direkt in die Datenbankdatei geschrieben. So wird die Verwaltung von mehreren Benutzern oder das Sichern von Rückrollbaren Transaktionszuständen vermieden um kürzere Ladezeiten zu erreichen.

Dieser Weg ist bei Datenbankmigrationen sinnvoll, wenn extreme Mengen von Informationen verarbeitet werden sollen, die im Allgemeinen bereits Korrekt und Vollständig sind.

