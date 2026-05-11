# Klausur
Keine Hilfsmittel (?)
2 Blatt Papier

## Nicht Relevant
[Verteilte Dateisysteme](08%20Fehlertoleranz.md#Verteilte%20Dateisysteme) und [Verteilter Shared Memory](08%20Fehlertoleranz.md#Verteilter%20Shared%20Memory)

# Fragen
## Verteilter Algorithmus für Mutexe
Im [Beispiel (Skript Seite 374)](06%20Verteilte%20Mutexe.md#Verteilter%20Algorithmus) werden die Zeitstempel $8,1$ und $12,3$ verwendet.
Sind das jeweils eine Zahl oder jeweils zwei, ähnlich einer [Vektor Uhr](05%20Logische%20Uhren.md#Vektor%20Uhren)?

Eine einzelne Zahl ist zum Rechnen deutlich simpler, wie wird das in echten Systemen verwaltet wenn keine eindeutige Zeit gegeben ist?
Verschiedene Vektorzeitstempel sind auch nur manchmal in totaler Ordnung.

## Write-Write Konflikte
Bei [Quorum basierte Protokollen](07%20Replikation%20und%20Konsistenz.md#Quorum%20basierte%20Protokolle) wird in den Folien auf Seite 489 die Bedingung $N_W > \dfrac{N}{2}$  genannt um Write-Write-Konflikte zu vermeiden.

Weil die aktuellste Versionsnummer nur lokal gespeichert ist?

## Two Army
[Two Army Problem](08%20Fehlertoleranz.md#Two%20Army%20Problem)

Ist lösbar wenn eine gemeinsame Uhr existiert? (Bedingung ist in der [Problembeschreibung](https://en.wikipedia.org/wiki/Two_Generals%27_Problem) implizit gegeben da ein kommendes Datum verwendet wird)

Annahme dass fehlgeschlagene Nachrichten wiederholt werden können bevor Zeitpunkt X eintritt. Bzw. Wiederholung mit neuem X

| t   | A über B          | Wissen A          | Wissen B          | B über A          | Neue Nachricht | M an |
| --- | ----------------- | ----------------- | ----------------- | ----------------- | -------------- | ---- |
| 0   | Null              | Vorschlag: Zeit X | Null              | Null              | Vorschlag um X | B    |
| 1   | Null              | Vorschlag: Zeit X | Vorschlag: Zeit X | Vorschlag: Zeit X | Ok um X        | A    |
| 2   | Vorschlag: Zeit X | Zeit X            | Vorschlag: Zeit X | Vorschlag: Zeit X | Ok Bestätigen  | B    |
| 3   | Vorschlag: Zeit X | Zeit X            | Zeit X            | Zeit X            | Ok_3           | A    |
| 4   | Zeit X            | Zeit X            | Zeit X            | Zeit X            | Ok_4           | B    |
| 5   | Zeit X            | Zeit X            | Zeit X            | Zeit X            | Ok_5           | A    |
| 6   | Zeit X            | Zeit X            | Zeit X            | Zeit X            | Ok_6           | B    |

Zum Zeitpunk $t_{n+2}$ ist einer Seite bewusst, dass $t_{n}$ erreicht wurde.
Beiden Seiten sind zu $t_{n+4}$ sicher dass bewusst dass der Zustand $t_{n}$ erreicht wurde
Ab $t_4$ ist Einigkeit erreicht, mit $t_6$ ist diese für A sicher und mit $t_7$ für B. Ab $t_8$ weiß A dass B Sicherheit hat. Mit $t_9$ wird B darüber informiert, mit $t_{10}$ wird abgeschlossen und ausreichend bestätigt. 

