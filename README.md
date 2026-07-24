# 🌋 Obsidian Main Vault 🌋
Heimat von Bildung, Ideen und sonstigen gedanklichen Feuerwerken.

# Vault-Qualität
Die letzte strukturelle Prüfung am 23.07.2026 umfasste 218 Markdown-Dateien. Der Prüfer verändert keine Dateien und benötigt nur Python:

```powershell
python scripts/audit_vault.py
```

Mit `--portability` werden zusätzlich Links gemeldet, die nur durch Obsidian anhand eines global eindeutigen Dateinamens aufgelöst werden. Mit `--strict` endet der Befehl bei Befunden mit Exit-Code 1 und kann dadurch später in einer CI-Prüfung verwendet werden.

Der Prüfer findet interne Link- und Ankerfehler, leere oder sehr kurze Notizen, offene Marker, doppelte Überschriften und Kapitelnummern sowie nicht geschlossene Code- oder Mathematikblöcke. Fachliche Widersprüche, veraltete Quellen und Grammatik müssen weiterhin inhaltlich geprüft werden.

## Tag-System
Tags werden kleingeschrieben, enthalten keine Leerzeichen und verwenden `/` als Hierarchie. Review-Tags stehen direkt an Aufgaben, damit sie über die Obsidian-Suche `tag:#review` gemeinsam oder mit ihrem vollständigen Tag gezielt gefunden werden können.

- `#review/content` - fachliche Aussage, Formel oder Widerspruch prüfen
- `#review/completeness` - fehlenden oder unvollständigen Inhalt ergänzen
- `#review/link` - Linkziel anlegen oder Verweis fachlich zuordnen
- `#review/structure` - Benennung, Gliederung, Dublette oder Weiterleitung klären
- `#review/source` - Quelle ergänzen oder zeitabhängige Aussage aktualisieren

Für den Zustand einer ganzen Notiz sind optional genau ein `#status/entwurf`, `#status/pruefen`, `#status/geprueft` oder `#status/veraltet` im YAML-Feld `tags` vorgesehen. Ein Status wird erst nach einer manuellen Prüfung gesetzt; deshalb wurden die bestehenden Notizen nicht pauschal als geprüft markiert.

## Review-Aufgaben

### Fachliche Prüfung
- [ ] In der [Embedding-Matrix](VorlesungsNotizen/KiAnwendung/08%20Transformer.md#Embedding%20Matrix) widersprechen sich die angegebene Dimension $|V| \times d$, die Zuordnung der Wortvektoren zu Spalten und die Multiplikation $e_t=E\cdot x_t$. Orientierung und Formeln vereinheitlichen. #review/content
- [ ] In der [GRU-Berechnung](VorlesungsNotizen/KiAnwendung/08%20Transformer.md#Gated%20Recurrent%20Unit%20%28GRU%29) wird der neue Zustand erst als $\tilde{t}_t$, danach aber als $\tilde{h}_t$ bezeichnet. Notation mit der Quelle abgleichen. #review/content
- [ ] Die [Self-Attention-Beschreibung](VorlesungsNotizen/KiAnwendung/08%20Transformer.md#Self-Attention) fachlich prüfen: Der Value-Vektor entsteht vor der Aggregation, und bei den Attention-Scores sollte die notwendige Transposition von $K$ eindeutig beschrieben werden. #review/content
- [ ] Die markierte Rechnung zur [Varianz einer stetigen Zufallsvariablen](Mathe/Stochastik/Wahrscheinlichkeitsrechnung/Stetige%20Zufallsvariablen.md#Varianz) neu herleiten; der lokale Hinweis nennt $50/9$ statt $6$ und ein fehlendes Quadrat. #review/content
- [ ] Angaben zu Rentenpflicht, Grenzen und Rückwirkung unter [Sozialversicherung](Didaris/Fragerunde.md#Sozialversicherung) anhand einer aktuellen Primärquelle prüfen und mit Prüfdatum versehen. #review/source

### Offene Verweise
- [ ] Für den Verweis aus [Diffie-Hellman](VorlesungsNotizen/Security/04%20Authentification.md#Diffie-Hellman%20Key-Exchange) eine Notiz oder einen vorhandenen Abschnitt zu symmetrischen Verschlüsselungsverfahren zuordnen. #review/link

### Markierte Lücken
- [ ] [Pipelining](Architektur/Pipelining.md) ausarbeiten oder den Platzhalter entfernen. #review/completeness
- [ ] Den offenen Punkt unter [Fehlerkorrektur](Digitaltechnik/Basics/Codes.md#Fehlerkorrektur) konkretisieren und ergänzen. #review/completeness
- [ ] Den [Satz von Schwarz](Mathe/Calculus/Funktionen%20von%20Mehreren%20Variablen.md#Satz%20von%20Schwarz) aus den vorhandenen OneNote-Aufzeichnungen vervollständigen. #review/completeness
- [ ] [Komplexe Zahlen](Mathe/Calculus/Komplexe%20Zahlen.md) aus den vorhandenen OneNote-Aufzeichnungen vervollständigen. #review/completeness
- [ ] Den unspezifizierten Marker im Abschnitt [Stetig](Mathe/Stochastik/Wahrscheinlichkeitsrechnung/Stetige%20Zufallsvariablen.md#Stetig) konkretisieren oder erledigen. #review/completeness
- [ ] Den fehlenden Inhalt zu [gRPC](Programmieren/Programmiermodelle.md#gRPC) ergänzen. #review/completeness
- [ ] Im [Compiler-Überblick](Theo/Compiler.md#Compiler%20Überblick) die fehlende Abbildung der Compilerphasen ergänzen. #review/completeness
- [ ] Die fehlende Beschreibung der [Marktformen](VorlesungsNotizen/Consulting/Themenabgrenzung.md#Marktformen) ergänzen. #review/completeness
- [ ] Den Abschnitt [Rangfunktionen](VorlesungsNotizen/Datenbanken2/DataWarehouse/09%20Analytische%20Funktionen.md#Rangfunktionen) vervollständigen. #review/completeness
- [ ] Den fehlenden Inhalt zu [Information Retrieval](VorlesungsNotizen/KiAnwendung/11%20Chatbots.md#Information%20Retrieval) ergänzen. #review/completeness
- [ ] Unter [Bewertung von Entscheidungsbäumen](VorlesungsNotizen/KiGrundlagen/03%20Entscheidungsbäume.md#Bewertung) den fehlenden Text und die Hyperparameter für Baumhöhe oder Knotenzahl ergänzen. #review/completeness

### Leere und sehr kurze Notizen
- [ ] [Entity-Relationship](Datenbanken/Entity-Relationship.md) befüllen oder mit der bestehenden Datenbank-Modellierung zusammenführen. #review/completeness
- [ ] [Kompressionsalgorithmen](Theo/Algorithmen/Kompressionsalgorithmen.md) befüllen oder entfernen. #review/completeness
- [ ] [Big O](Theo/Berechenbarkeit/Big%20O.md) befüllen oder mit Komplexität zusammenführen. #review/completeness
- [ ] [Graphen](Theo/Daten/Graphen.md) befüllen oder entfernen. #review/completeness
- [ ] [Aussagenlogik](Theo/Formale%20Logik/Aussagenlogik.md) befüllen oder entfernen. #review/completeness
- [ ] [Prädikatenlogik](Theo/Formale%20Logik/Prädikatenlogik.md) befüllen oder entfernen. #review/completeness
- [ ] [Parser](Theo/Formale%20Sprachen/Parser.md) befüllen oder entfernen. #review/completeness
- [ ] [Sprachen](Theo/Formale%20Sprachen/Sprachen.md) befüllen oder entfernen. #review/completeness
- [ ] [Hashing](Theo/Hashing.md) befüllen oder auf eine vorhandene Hashing-Notiz weiterleiten. #review/completeness
- [ ] Die leere Netztechnik-Notiz [06](VorlesungsNotizen/Netztechnik/06.md) benennen und befüllen oder entfernen. #review/completeness
- [ ] Die leere [Netztechnik-Fragerunde](VorlesungsNotizen/Netztechnik/09%20Fragerunde.md) befüllen oder entfernen. #review/completeness
- [ ] Die Stichworte in [KI-Vortrag](RandomNotes/KiVortrag.md), [Manim](Tech%20Stuf/Manim.md), [Bäume](Theo/Daten/Bäume.md), [Prozessmanagement](VorlesungsNotizen/Betriebssysteme/03%20Prozessmanagement.md) und [Softwarequalität-Aufgabe](VorlesungsNotizen/SoftwareQualität/Aufgabe.md) zu vollständigen Notizen ausbauen oder bewusst als Platzhalter kennzeichnen. #review/completeness

### Struktur
- [ ] Die mehrfach vergebenen Nummern `00` in [KI-Anwendung](VorlesungsNotizen/KiAnwendung/00%20Spickzettel.md) und [Verteilte Systeme](VorlesungsNotizen/VerteilteSysteme/00%20Einführung.md) sowie `05` in [Security](VorlesungsNotizen/Security/05%20Prüfziffern.md) anhand einer dokumentierten Benennungsregel prüfen. #review/structure
- [ ] Die einzeiligen Weiterleitungen in [Verteilte Systeme](VorlesungsNotizen/VerteilteSysteme/01%20Grundlagen.md) prüfen. Mehrere Kapitel zeigen nur auf allgemeine Notizen, und `04 Prozessmanagement` sowie `05 Logische Uhren` sind inhaltlich identisch. Beibehalten, zu echten Indexnotizen ausbauen oder zusammenführen. #review/structure
- [ ] Die 80 mehrfach verwendeten Überschriften in 35 Dateien prüfen und bei verlinkbaren Abschnitten eindeutig benennen. Beginnen mit [Vertragsrecht](Recht/Vertragsrecht.md), [IT-Recht](Recht/ItRecht.md), [Recht-Einleitung](Recht/Einleitung.md) und [Dateiorganisation](VorlesungsNotizen/Datenbanken2/02%20Dateiorganisation.md). #review/structure
- [ ] Tippfehler in Dateinamen kontrolliert über Obsidian umbenennen, damit Links mitgezogen werden: [Authentification](VorlesungsNotizen/Security/04%20Authentification.md), [Bitübertragunsschicht](VorlesungsNotizen/Netztechnik/02%20Bitübertragunsschicht.md) und [Wahrscheinlichtkeit](Mathe/Stochastik/Wahrscheinlichkeitsrechnung/Bedingte%20Wahrscheinlichtkeit.md). #review/structure

### Bestehende Themenplanung
- [ ] [Suchalgorithmen](Theo/Algorithmen/Suchalgorithmen.md) vervollständigen. #review/completeness
- [ ] [Sortieralgorithmen](Theo/Algorithmen/Sortieralgorithmen.md) vervollständigen. #review/completeness
- [ ] [Komplexität](Theo/Berechenbarkeit/Komplexität.md) vervollständigen. #review/completeness
- [ ] [Elementare Datentypen](Theo/Daten/Elementare%20Datentypen.md) vervollständigen. #review/completeness
- [ ] [Automaten](Theo/Automaten.md) vervollständigen. #review/completeness
- [ ] [Implizite Ableitungen](Mathe/Calculus/Funktionen%20von%20Mehreren%20Variablen.md#Implizite%20Ableitungen) vervollständigen. #review/completeness
- [ ] [Integrale von mehreren Variablen](Mathe/Calculus/Funktionen%20von%20Mehreren%20Variablen.md#Integrale%20von%20mehreren%20Variablen) vervollständigen. #review/completeness
- [ ] [Polarintegrale](Mathe/Calculus/Funktionen%20von%20Mehreren%20Variablen.md#Polarintegrale) vervollständigen. #review/completeness
- [ ] Die [Normalisierung](Datenbanken/Datenbank-Modellierung.md#Normalisierung) vervollständigen. #review/completeness

# How2Markdown
Markdown ist ein Format das mit wenigen Zeichen die meisten Formatierungsarten möglich macht.

Diese Datei soll als Zusammenfassung und Ausstellung verwendeter Blöcke dienen.

## (Unter-)Überschriften

### Überschriften Lvl 3
#### Überschriften Lvl 4
##### Überschriften Lvl 5
###### Überschriften Lvl 6

Normaler Text

## Links
Über links kann auf Webseiten, Dateien oder Bilder verwiesen werden.
Sie folgen dem Schema `[anzuzeigender Text](Link.Destination)`
- [Google](https://www.Google.com)
- [Überschriften](#🌋Obsidian🌋Main-Vault🌋)
- Andere Dateien [Obsidian on Mobile](Obsidian.md)
Wenn direkt vor dem Link ein Ausrufezeichen `!` eingefügt wird, so versucht Obsidian eine Vorschau des Ziels einzublenden.
Besonders häufig wird diese Funktion verwendet um [Bilder](#Bilder) einzufügen.

## Bilder
Werden als [Links](#Links) mit Vorschau verwendet.
Sie können außerdem mit einer definierten Breite gerendert werden indem sie folgendermaßen eingebettet werden.
`![AltText |200](image.png)`
Das Bild würde so mit einer Breite von 200 angezeigt werden.

## Aufzählungen
Entweder unsortiert
- so
- dies
- das
- Ananas
	- Unterpunkte
	- Sind
	- wichtig

Oder nummeriert
1. Eins
2. Zwei
3. Auch mit Unterpunkten
	1. So
	2. oder so
## Gleichungen
Beginnen und enden mit einem \$ wenn sie im Text stehen sollen.
Meine Lieblingsgleichung ist $1 + 1 = 2$. Ich mag sie sehr.
Oder mit \$\$ wenn die Gleichung als eigenständiger Block angezeigt werden soll.
$$
e = mc^2
$$
Verfügbar sind alle [Mathjax-Befehle](https://math.meta.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference)

## Code
Kann ähnlich wie [Gleichungen](#Gleichungen) inline oder als Block gezeigt werden.
Dafür wird ` `` ` oder die Blockschreibweise verwendet.
Bei Blöcken kann die Sprache angegeben werden um Syntax-Highlighting zu verwenden.

``` Python
def example():
	print("hello Nerd!")
```

## Callouts

> [!NOTE] Notiz
> Here is a Link to the official [Doku](https://help.obsidian.md/callouts)


> [!Warning]- Warnung
> Contents


> [!Error] Error
> Contents

## Tabellen

| Heading | Head 2       | Überschrift der Mathe-Spalte |
| ------- | ------------ | ---------------------------- |
| Content | More Content | $\pi \approx e$              |
