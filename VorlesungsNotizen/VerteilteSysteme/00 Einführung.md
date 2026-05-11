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