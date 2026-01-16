# 🌋Obsidian🌋Main-Vault🌋
Heimat von Bildung, Ideen und sonstigen gedanklichen Feuerwerken

# TODO
- [Pipelining](Pipelining.md)
- Theo alles
	- [Suchalgorithmen](Suchalgorithmen.md)
	- [Sortieralgorithmen](Sortieralgorithmen.md)
	- [Kompressionsalgorithmen](Kompressionsalgorithmen.md)
	- [Big O](Big%20O.md)
	- [Komplexität](Komplexität.md)
	- [Bäume](Bäume.md)
	- [Elementare Datentypen](Elementare%20Datentypen.md)
	- [Graphen](Graphen.md)
	- [Aussagenlogik](Aussagenlogik.md)
	- [Prädikatenlogik](Prädikatenlogik.md)
	- [Parser](Parser.md)
	- [Sprachen](Sprachen.md)
	- [Automaten](Automaten.md)
	- [Compiler](Compiler.md)
	- [Hashing](Hashing.md)
- Mathe 3. Semester
	- [Satz von Schwarz](Funktionen%20von%20Mehreren%20Variablen.md#Satz%20von%20Schwarz)
	- [Implizite Ableitungen](Funktionen%20von%20Mehreren%20Variablen.md#Implizite%20Ableitungen)
	- [Integrale von mehreren Variablen](Funktionen%20von%20Mehreren%20Variablen.md#Integrale%20von%20mehreren%20Variablen)
	- [Polarintegrale](Funktionen%20von%20Mehreren%20Variablen.md#Polarintegrale)
	- [Komplexe Zahlen](Komplexe%20Zahlen.md)
- Datenbanken
	- [Entity-Relationship](Entity-Relationship.md)
	- [Normalisierung](Datenbank-Modellierung.md#Normalisierung)

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
