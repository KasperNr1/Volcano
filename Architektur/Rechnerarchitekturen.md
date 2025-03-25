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

# Programmiermodelle
- Desktop -> Viel Integer / Floating Point
- Server -> Integer / Strings
- Embedded -> Codegröße & Stromverbrauch

# Prinzipien des Entwurfs eines Rechners

> [!NOTE] Make The Common Case Fast
> Die Performance eines Systems lässt sich am besten optimieren indem häufige Prozesse perfektioniert werden. Ihnen sollen priorisiert Ressourcen und Entwurfszeit zugeordnet werden.
> Zusätzlich sind häufige Fälle meist simpler als Ausnahmen, was auch ihre Implementierung erleichtert

[Amdahls Law](Amdahls%20Law.md) beschreibt die Mathematik hinter Optimierung von Teilsystemen und deren Einfluss auf das Gesamte.
An diesem [Beispiel](Amdahls%20Law.md#Beispiel) wird gezeigt dass der etwas schnellere Common Case einen deutlich größeren Einfluss hat als die sehr starke Beschleunigung einer selteneren Operation.

1. Simplicity favors Regularity
2. Smaller is faster
3. Make the common Case fast
4. Good design demands compromises