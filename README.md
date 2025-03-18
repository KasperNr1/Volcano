# 🌋Obsidian🌋Main-Vault🌋
Heimat von Bildung, Ideen und sonstigen gedanklichen Feuerwerken

# TODO
- [2er Komplement](DigitaltechnischeBegriffe.md#2er%20Komplement)
- [Parity](DigitaltechnischeBegriffe.md#Parity)
- Theo alles
- Mathe 3. Semester
- [Codes](Codes.md)

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
- Andere Dateien [Obsidian on Mobile](Obsidian%20Mobile.md)
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
- Aber
	- nicht
- zu
- viele

Oder nummeriert
1. Eins
2. Zwei
3. Drei
4. Auch mit Unterpunkten
	1. So
	2. so
	3. oder so
5. Fünf
18. Unsortiert (Mag Obsidian nicht, geht trotzdem)

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
Dafür wird ` `` ` oder entsprechend 
```
``` ```
```
verwendet.

## Callouts

> [!NOTE] Notiz
> Contents


> [!Warning] Warnung
> Contents


> [!Error] Error
> Contents

## Tabellen

| Heading | Head 2       | Überschrift der Mathe-Spalte |
| ------- | ------------ | ---------------------------- |
| Content | More Content | $\pi \approx e$              |
