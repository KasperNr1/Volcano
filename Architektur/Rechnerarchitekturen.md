# Architektur nach von Neumann
Der Rechner besteht aus Funktionseinheiten
- ALU (Arithmetic Control Unit)
  Rechenwerk
- Control Unit
  Steuer- / Leitwerk
- Memory
  Speicherwerk
- I/O Unit
  Ein- / Ausgabewerk

![](vonNeumann.png)

Die Struktur ist unabhängig vom zu bearbeitenden Problem. Der Computer ist speicherprogrammierbar, wobei Daten und Programmcode im selben Speicher liegen.
Die Befehle werden standardmäßig sequentiell ausgeführt, Änderungen im Kontrollfluss werden über (un-)bedingte Sprünge realisiert.
Befehle und Operanden sind durch Binärcodes repräsentiert, die einzelnen Bytes enthalten keine Angaben über den Typ ihres [codierten](Codes.md) Inhalts.

> [!Info] Sicherheit
>Anweisungen, Daten und Zwischenergebnisse liegen im selben Speicher, Eingabedaten können nicht unbedingt vom Programmcode unterschieden werden
>
>`a')´ drop table --` 
>
>Versucht die Trennung zu umgehen

Der streng sequentielle Ablauf ist entscheidender Vorteil dieser Architektur, da deterministische Programmabläufe leichter zu programmieren sind. [Race-Conditions](Parallele%20Probleme.md#Race-Conditions) sind durch Verwendung eines einzelnen Datenbus ausgeschlossen.

# Harvard Architektur
![](HarvardArchitektur.png)
Schaltungskonzept um besonders schnelle Prozessoren zu realisieren.
Daten und Steuerung werden strikt getrennt und auf separaten Leitungen übertragen.
Vorteile gegenüber [von Neumann Architektur](#Architektur%20nach%20von%20Neumann)
- Gleichzeitiges Lesen und Schreiben von Daten
- Einfache Zugriffsrechtesteuerung und Speicherschutz

Durch die parallelisierte Natur des Systems entstehen die [Probleme der Parallelisierung](Parallele%20Probleme.md) auf Rechnerebene. Es gibt keine Garantie für einen deterministischen Ablauf oder eine einfache Vermeidung von Race-Conditions.

