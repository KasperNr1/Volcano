# Motivation
Verschiedene Personen innerhalb eines Unternehmen haben Aufgaben unterschiedlicher Arten. Während Sachbearbeiter viele kleinere Transaktionen im Detail verwalten sind im Management Entscheidungen zu treffen, die auf größerer Weitsicht basieren.
![](AufgabenSachbearbeiterUndManagement.png)

Die Entscheidungen des Management werden deutlich seltener getroffen, haben aber größeren Einfluss auf das Unternehmen.

Die Daten die als Grundlage für die jeweiligen Entscheidungen dienen, haben verschiedene Anforderungen.
Operative Datenbanken dienen einem spezifischen Ziel. Sie sollen für täglich aktuelle Anwendungsfälle benutzt werden und hierfür schnell reagieren.
Bei komplexeren Analysen die vom Management gewünscht sind, sind andere Eigenschaften vorteilhaft. Ergebnisse sollen akkurat und reproduzierbar sein, Berechnungsgeschwindigkeit ist weniger relevant. Es sollen außerdem die Daten aus verschiedenen Quellen gesammelt analysiert werden können.
Auch sind prinzipiell längere Zeithorizonte für die Entscheidungsgrundlage relevant. 

# Architektur
Ohne DWH (DataWareHouse) sind die Informationssysteme typischerweise verstreut.
![](KlassischeDatenBankLandschaft.png)
Für unterschiedliche Operative Aufgaben sind unterschiedliche OLTP-Tools (Online Transaction Processing) von verschiedenen Herstellern im Einsatz, meist mit einem jeweils eigenen Export in ein Tabellenformat (Excel o.Ä.) für höheres Management.
Es gibt separate MIS (Management Information Systems) Anwendungen die Tools zu Analyse bereitstellen.

Mit dieser Struktur liegen viele Daten redundant vor. Sie sind schlecht nachvollziehbar in verschiedenen Formaten und Orten gespeichert. Auch eine Einbindung externer Datenquellen (Internet / weitere Tools) ist nicht gegeben. Identische Analysen können auf verschiedenen Systemen unterschiedliche Ergebnisse liefern da die Datenmenge- und Qualität nicht unbedingt identisch ist.

![](DataWareHouseReferenzArchitektur.png)

## Datenquellen
- Interne Quellen
  Sind verschiedene ERP-/CRM-Systeme
- Externe Quellen
  Internet
  Social Media
Diese Daten sind in ihrer Gesamtheit meist sehr heterogen. Unterschiedliche Formate (Datenanken / XML / Freitext) oder Codierungen. 

### Monitoring
Ist für die Aktualisierung der Daten zuständig. Neuerungen werden erkannt und mitgeteilt, entweder mit neuem Inhalt oder nur als Benachrichtigung über die Verfügbarkeit einer neuen Version.

Es wird unterschieden in
- Polling (Anfragen ob Änderungen existieren)
- Benachrichtigungen (Sobald Änderungen anfallen)

und die Art der Aktualisierungen
- Fein (Jede Änderung wird separat behandelt)
- Netto-Effekt ($1\to 3 \to 8$  kann als $1 \to 8$ betrachtet werden)

Es gibt unterschiedliche Strategien zur Entdeckung von Änderungen
- Triggerbasiert (Quelle meldet an Monitor)
- Zeitstempel (Es kann erkannt werden was seit letzter Übertragung entstanden ist)
- Log-Basiert (Alle Aktionen in Log Datei fixiert, log kann durchsucht werden)
- Snapshot-Basiert (Quelle wird periodisch kopiert. Mehrere Kopien können nach Unterschieden untersucht werden)

## Back End-Werkzeuge
### Extraktionskomponente
Überträgt Daten aus Primärquelle in Zwischenspeicher (Operational Data Storage).
Wann wird das getan?
- Periodisch in festen Abständen
- Anfragebasiert
- Ereignisgesteuert (z.B. nach fester Anzahl Änderungen)
- Sofort bei Änderung

### Transformationskomponente
Migriert Daten in geeignetes Format
- Anpassung von Datentypen
- Dateiformate
- Codierungen
- Umrechnung von Maßeinheiten
- Kombination oder Trennung von Attributen
- $\dots$

### Bereinigungskomponente
"Data Cleansing" um Qualitätsmerkmale zu erreichen.
Unreinheiten können verschieden definiert sein.
- Dubletten
- Unvollständige Einträge
- Ausreißer
- Alte Daten
- $\dots$

### Ladekomponente
Übertragung der Daten von Zwischenspeicher zu DWH.
- Online-Ladevorgang (DWH ist während Laden verfügbar)
- Offline-Ladevorgang (Nicht verfügbar während Aktualisierung)

Initiales Laden und Aktualisierungen werden von dieser Komponente behandelt. Aufgrund der Masse an Daten in einem DWH wird typisch nicht mit den Standardtechniken gearbeitet, man setzt sog. "Bulk-Loader" ein.

### Operational Data Storage (ODS)
Physischer Zwischenspeicher im Back-end.
Speichert Daten feingranular und wird für Ad-Hoc-Auswertungen eingesetzt.
Daten liegen meist in der [dritten Normalform](Datenbank-Modellierung.md#Normalisierung) vor.

Alternativ liegen hier die Daten bereits für das DWH aufbereitet vor. Das ODS stellt in diesem Fall nur ein Basis-Layer dar.

## Datenbank
## Applikationen
