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

# Registerarchitekuren
Es werden verschieden Architekturen für Register und Datenfluss zur CPU verwendet. In jedem dieser Beispiele werden die notwendigen Assembler-Befehle gezeigt um die Berechnung $C = A + B$  durchzuführen.

Praktisch alle neu entwickelten RISC Prozessoren verwenden [die Load-Store Variante](#Registerarchitektur%20Load-Store).
Die dort verbauten Universalregister sind sehr schnell verfügbar (Zugriffe  $< 1ns$ ).
Auch können Compiler diese Register sehr effizient ausnutzen. Beispielsweise können die Reihenfolgen einiger Operatoren getauscht werden, was bei der [Stack-Architektur](#Stack-Architektur%20Invers%20Polish%20Notation) nicht möglich ist.
## Stack-Architektur: Invers Polish Notation
![](StackArchitektur.png)
Folge von Befehlen werden auf Stack gespeichert oder verrechnen die letzten $n$ Werte im Stack

$$

(3 + 4) * 5

$$

In klassischer Infix-Notation wird zu

$$

3; 4; +; 5; *

$$

So entfällt der Bedarf für Klammern

### Codesequenz
Die beiden zu verrechnenden Werte werden auf den Stack gespeichert, verrechnet und das Ergebnis wird wieder vom Stack entfernt.
```
Push A
Push B
Add
Pop C
```


## Akkumulator Architektur
![](AkkumulatorArchitektur.png)
Ergebnisse werden immer in Register gelagert, so ist wie bei einem Taschenrechner eine weitere Berechnung mit dem vorherigen Ergebnis möglich.

### Codesequenz
```
Load A
Add B
Store C
```

## Registerarchitektur
![](RegisterArchitekur.png)
Es werden mehrere Universalregister verwendet.
Beispielsweise x86 arbeitet nach diesem Prinzip.

### Codesequenz
Wert $A$ wird im ersten Register gespeichert, dann wird der Inhalt des ersten Registers mit der Variable $B$ addiert und das Ergebnis in Register $R3$ gespeichert. Schließlich wird der Variable C im Speicher der Wert aus dem dritten Register zugewiesen.

```
Load  R1, A
Add   R3, R1, B
Store R3, C
```

## Registerarchitektur Load-Store
![](LoadStore.png)
Ähnlich wie die [Registerarchitektur](#Registerarchitektur), jedoch ohne Speicheroperanden. Jeder Zugriff auf den Speicher erfolgt über einen dedizierten `load` oder `store` Befehl.

Diese Architektur ist die typische RISC Architektur.

### Codesequenz
Die beiden Variablen werden in unterschiedliche Register geladen. Diese beiden Register werden addiert und das Ergebnis in einem dritten Register gespeichert.
Abschließend wird der Wert aus dem Register in den Speicher geschrieben.
```
Load  R1, A
Load  R2, B
Add   R3, R1, R2
Store R3, C
```

