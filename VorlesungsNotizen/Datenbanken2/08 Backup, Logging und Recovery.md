Aufgrund von Stromausfällen oder physischen Fehlern innerhalb des Speichers kann der Inhalt des Hauptspeichers oder der Festplatten (teilweise) verloren gehen.
Auch andere Fehler die aufgrund von Fahrlässigkeit der Benutzer oder durch absichtliche Angreifer ausgelöst wurden, können zu Löschungen von Daten führen.

Prinzipiell können Fehler im System zu jedem beliebigen Zeitpunkt auftreten.
Wenn Fehler zwischen dem Schreiben in den Puffer und dem endgültigen Schreiben auf den Sekundärspeicher auftritt, muss der Recovery Manager unterscheiden, ob die Transaktion bereits ihren `Commit` abgesetzt hat.
- Falls ja, so muss die Transaktion wiederholt werden, um die Dauerhaftigkeit zu gewährleisten. (Globales 'REDO' oder 'ROLLFORWARD')
- Falls der Commit noch nicht gesendet wurde, so wird die Transaktion per Rollback zurückgenommen.

Insgesamt werden verschiedene Konzepte zur Sicherung verwendet, oft auch in Kombination miteinander
- Backup-Mechanismen
- Log-Mechanismus
- Checkpoints
- Recovery-Manager

# Backup
Siehe auch [Datensicherung](02%20Physische%20Sicherheit.md#Datensicherung)

# Log-Mechanismus
Jeder Eintrag im Log umfasst einige Informationen
- Laufende Nummer des Eintrags
- ID der Transaktion
- Art der Operation (`Beginn Transaction`, `Read`, `Write` $\dots$)
- Betroffenes Objekt (Tabelle / Spaltenangabe bzw. Seite oder Datensatz)
- Objektwert vor der Operation (Before Image)
- Objektwert nach der Operation (After Image)
- Log Management Informationen (Z.B. Zeiger auf vorherigen Logeintrag)

In der Praxis werden oft zwei Logdateien gleichzeitig geschrieben, eine für Rückwärtsorientierte Handlungen wie Transaktionsabbrüche und ein Vorwärts-Log zur Wiederherstellung bei z.B. Medienfehlern.

# Checkpoint Mechanismus
Im Fehlerfall wird anhand der Log Datei ein gültiger Zustand wiederhergestellt. Um die korrekte Menge an Operationen zu bestimmen, wird häufig mit Checkpoints gearbeitet, damit DB und Log-Datei zu definierten Zeitpunkten synchronisiert sind.

# Recovery
## Fall 1: Plattenspeicher ist beschädigt
Durch Physische Einflüsse wie Hochwasser / Erdbeben oder Softwareprobleme wurde der Sekundärspeicher zerstört.

Um einen verwendbaren Stand wiederherzustellen wird das letzte Backup der Datenbank wieder eingespielt und mithilfe der [Log-dateien](#Log-Mechanismus) die Transaktionen seit dem Stand nachvollzogen.
Dies setz voraus, dass die Logdateien nicht ebenfalls zerstört sind. Sie sollten physisch getrennt an einem anderen Ort gelagert werden.

## Fall 2: Hauptspeicherverlust
Durch Stromausfälle oder Fehler im Hauptspeicher können diese Probleme auftreten.

Es müssen alle nicht beendete Transaktionen zurückgesetzt werden, Änderungen auf dem Sekundärspeicher müssen zurückgerollt werden (Globales UNDO).
Beendete Transaktionen müssen ggf. wiederholt werden, sowie die erneute Übertragung von Änderungen in den Sekundärspeicher.

## Fall 3: Transaktionsfehler
Ursachen sind Fehler im Anwendungsprogramm, explizite Anweisungen durch `Rollback` oder implizite Anweisungen durch Verletzung von Integritätsbedingungen.

Hier kann mit einem 'lokalen UNDO' im Hauptspeicher recovered werden, vor dem Ende einer Transaktion wird nichts im Sekundärspeicher geschrieben.

## Recovery-Techniken
Für die Fälle [2](#Fall%202%20Hauptspeicherverlust) und [3](#Fall%203%20Transaktionsfehler) gibt es verschiedene Techniken.
Sie unterscheiden sich in der Art und Reihenfolge, wie Aktualisierungen auf den Sekundärspeicher geschrieben werden.
- Deferred Update
- Immediate Update
- Shadow Paging

### Deferred Update
Aktualisierungen werden generell nicht in die DB geschrieben, bis eine `Commit` Anweisung erreicht wird. So muss auch bei einem Abbruch keine Änderung zurückgenommen werden.

Im Log wird entsprechend mit einem 'Transaction Begin' gearbeitet um ein 'REDO' zu ermöglichen.
Falls die Einträge bereits dauernd geschrieben wurden, so hat ein erneutes Schreiben keinen Effekt

### Immediate Update
Bei dieser Strategie werden alle Änderungen direkt in die DB geschrieben. Es wird nicht erst auf ein `Commit` gewartet.
Somit ist es bei Fehlern oft notwendig, diese Änderungen zurückzunehmen.

Im Log wird daher detailliert mitgeschrieben
1. Start der Transaktion wird geloggt.
2. Bei jeder Schreiboperation wird zuerst ins Log protokolliert.
3. Eventuell erreichte Commit-Anweisung wird protokolliert
4. Falls kein Commit erreicht wird, können die Logdateien in umgekehrter Reihenfolge abgearbeitet werden um den alten konsistenten Zustand zu erreichen.

Im Fehlerfall werden alle Transaktionen seit dem letzten Checkpoint analysiert. Gewinner Transaktionen haben ihren Commit bereits erreicht, als Verlierer werden diese Transaktionen bezeichnet, die noch kein Commit erreicht haben.
Alle Gewinner werden erneut ausgeführt, ggf. werden dabei Arbeitsschritte unnötigerweise erneut durchlaufen. Alle Verlierer werden vollständig zurückgerollt.

### Shadow Paging
![](ShadowPaging.png)

Beim Beginn einer Transaktion wird die aktuelle Seitentabelle in eine 'Schattentabelle' kopiert. Diese Schattentabelle bleibt unverändert, bei Änderungen auf den Daten wird eine Kopie der Seite angelegt.
Der Zustand zu Beginn der Transaktion ist durch die Schattentabelle vorhanden.
Beim Commit werden die modifizierten Seiten auf die Platte geschrieben. Alte, von der Schattentabelle referenzierte Seiten werden verworfen und der Speicher freigegeben.

Gegenüber den Log-Basierten Ansätzen werden deutlich weniger Plattenzugriffe benötigt, somit ist die Recovery erheblich schneller.
Durch die vielen Kopien fragmentieren die Daten allerdings, die Leseperformance leidet und es ist eine Garbage-Collection notwendig.
Auch die Skalierbarkeit ist schwierig, besonders das gleichzeitige Schreiben mehrerer paralleler Transaktionen.

## Vergleich
Unterschieden wird der Schreib-Zeitpunkt 
- 'Steal' Das Einbringen von Änderungen ist jederzeit möglich
- 'No-Steal' Änderungen werden erst am Transaktionsende in die DB eingebracht

Auch die Auslagerung ist ein Kriterium anhand dem unterschieden wird
- 'Force' Erzwingt die Auslagerung am Transaktionsende
- 'No-Force' Erlaubt die Auslagerung auch zu einem späteren Zeitpunkt

![](ComparisonRecoveryStrategies.png)

