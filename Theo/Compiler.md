# Compiler Überblick
Besteht aus mehreren Schritten mit unterschiedlichen Aufgaben.

TODO Bild Compilerphasen

- Tatsächliche Übersetzung findet zwischen Semantik-Check und Codegenerator statt.
- Programmiersprachen sind (fast) Kontextfrei -> Lineare Komplexität für Parsen mit [Push-Down Automaten](Automaten.md#Push-Down%20Automaten)
- Semantik-Check prüft Kontextsensitiven Anteil ( i = 1 -> erlaubt oder nicht je nach Datentyp der Variable)

# Lexer
# Parser
Linksrekursion vermeiden
`S -> S + smth`

- Terminale bei %Token
- NichtTerminale definiert durch existenz auf linker seite einer Produktion
- Terminalsymbole müssen einem Token-Konstruktor zugewiesen werden

Aufruf
`happy --info Parser.y` generiert `nfo` File

# Typcheck

# Codegenerator
## Class Files

Konstantenpool ist ein Array dessen erstes Element den Index 1 hat. Das 0te Element existiert nicht, wird aber bei der Länge des Arrays mitgezählt.

Code Attribut mit eigenen Namen, statt nur Nummer des Befehls

Mit diesem Befehl wird ein minimales Class file generiert.
`javac -g:none smth.java` 

Packet Namen mit `/` statt der gewöhnlichen Schreibweise mit Punkten `.` 

Befehle bestehen aus 1, 2 oder 3 Bytes, Code_Length summiert die verwendeten Bytes.

## JVM

`aload_0` lädt das aktuelle Objekt

Der erste Buchstabe des Befehlsname sagt aus auf welchen Daten er operiert.
- `aSmth` Attribute
- `iSmth` Integer

`New` fügt 2 Objekte auf dem Stack zu, eines wird nach dem Aufruf des Konstruktors gelöscht.

- `invokeSpecial` ruft Methode des Objekts auf
- `invokeVirtual` beachtet Überschreibungen bei Vererbung