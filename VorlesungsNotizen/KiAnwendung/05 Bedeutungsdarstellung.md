# Definition
Bedeutung ist die Botschaft, die durch Wörter und Sätze vermittelt wird.

Dabei ist die Bedeutung oft eine andere als die bloße Summe der einzelnen Wörter.
"Jemandem einen Bären aufbinden"

# Typen von Bedeutungsrepräsentation
Es gibt fünf Typen von Bedeutung
1. Kategorien
   Spezifische Objekte oder Entitäten
   Firmennamen, Standorte oder Gegenstände
2. Ereignisse
   Handlungen oder erlebte Phänomene
   'einen Film ansehen'
3. Zeit
   Genaue oder Referenzzeitpunkte
   Nächste Woche, 9:30 Uhr
4. Aspekte
   Darstellen von Fakten oder Beschreiben von Aktionen
   'Jane läuft', 'Das Buch ist interessant'
5. Überzeugungen / Wünsche und Absichten
   'Ich halte deine Aussage für realistisch'

# Semantische Verarbeitung
Unterschiedliche Fragen benötigen für eine sinnvolle Antwort eine große Menge an Semantischer Verarbeitung.
Bei korrekter Umsetzung kann ein System auch Schlussfolgerungen aus Wissen ziehen um unbekannte Aussagen zu bewerten.
`If John is in the classroom, and Mary is sitting next to him, then Mary is also in the Classroom`

## Kenntnis eines Konzepts
"What is the Meaning of NLP"

## Hintergrundwissen eines Konzepts
"How does the N-gram model work"

## Kenntnis eines Konzepts und unterschiedliche Relevanz zu verschiedenen Zeitpunkten
"Does the Turing Test still exist"

## Einbindung von Weltwissen neben Informationen zum Subjekt
"Why do we need to study self-awareness in AI"

## Wissen um Umstände des Nutzers neben Welt- und Faktenwissen
"Should I study AI"

# Darstellung von Bedeutung
Um eine effektive Repräsentation zu gewährleisten müsse drei Faktoren erfüllt sein.
- Verifizierbarkeit
  Aussagen können durch Vergleiche mit anderem Weltwissen oder durch logische Schlussfolgerungen als Wahr oder Falsch erkannt werden.
- Umgang mit Mehrdeutigkeit
  Die Fähigkeit die richtige der möglichen Bedeutungen zu erkennen.
- Vagheitsüberlegungen
  Manche Begriffe wie 'groß' haben keine klaren Grenzen. In unterschiedlichen Situationen kann die selbe Länge groß und klein sein.

Es gibt vier gängige Ansätze um Semantik formell darzustellen:
## FOPL
Die Aussage "Jack fährt einen Mercedes" lässt sich mittels Prädikatenlogik wie folgt darstellen
$$\exists y (Person(Jack) \wedge Fährt(Jack, y) \wedge Auto(y) \wedge Marke(y, Mercedes)) $$


## Semantische Netzwerke
![](SemanticNetwork.png)

## Konzeptuelles Abhängigkeitsdiagramm
![](ConceptualDependencyDiagram.png)

## Frame-Based Representation
![](FrameBasedRepresentation.png)


# Kanonische Form
Eine kanonische Form bezieht sich auf eindeutig identifizierbare Objekte, die auf mehr als eine Weise dargestellt werden können. 
Eine dieser Möglichkeiten wird als die bevorzugte (kanonische) Standard-Form (wie bei [digitaltechnischen Schaltungen](DigitaltechnischeBegriffe.md#Normalform)) bezeichnet.

Auch [Polynome](Gleichungen.md#Größere%20Polynome) oder Dateipfade haben eine Standard-Darstellungsform. Für Pfade die Darstellung als absolute Pfade vom Wurzelknoten, bei Polynomen die Schreibweise mit nach Größe sortierten Exponenten.

In der Sprachverarbeitung können verschiedene Sätze mit identischer Bedeutung somit auch in einer Standardform gespeichert werden.
- Jack eats KitKat
- KitKat is what Jack eats
- What Jack eats is KitKat
Bis auf geringfügige Variationen in Ton sind diese Aussagen gleichwertig.

Wenn mehrere Aussagen in der selben Kanonischen Form vorliegen, erleichtert dies die Erkennung von Mustern zur Ableitung von Wissen und erhöht die Effizienz der Speichernutzung. Weil für mehrere Varianten dieselben Inferenzregeln verwendet werden können, ist es nicht notwendig für jede dieser Varianten eine eigene Regel zu definieren.
Allerdings besteht so die Gefahr von Missverständnissen, wenn Phrasen fälschlicherweise zusammengefasst werden.

# Schlussfolgerungen
## Inferenz
Das Ableiten von neuen Erkenntnissen aus vorhandenen Informationen.

Teilt sich in [Deduktion](#Deduktion) und [Induktion](#Induktion).

Eine Inferenz ist im Allgemeinen gültig, wenn sie durch korrekte Schlussfolgerungen logisch aus Beweisen abgeleitet wird.
### Deduktion
Aus allgemeinen Prämissen werden spezifische Schlussfolgerungen abgeleitet.

- Alle Menschen sind sterblich
- Sokrates ist ein Mensch
Führt zur Erkenntnis
- Sokrates ist sterblich

### Induktion
Bei der Induktion werden aus spezifischen Beobachtungen Schlussfolgerungen über die Allgemeinheit gebildet.
$$
\begin{array}{}
\text{Die Sonne ist in den letzten 30 Jahren jeden Tag aufgegangen} \\
\downarrow \\
\text{Die Sonne geht jeden Tag auf}
\end{array}
$$

> [!Info] Wichtig
> Diese Schlussfolgerungen sind nicht immer zwingend korrekt.
> 
> Um mit dieser Technik allgemeine Beweise zu führen, muss ein Basisfall existieren. Auch ist ein Schritt notwendig um von einem Zustand allgemein in den nachfolgenden überzugehen.
> Wenn diese Kriterien erfüllt sind spricht man von einer [Vollständigen Induktion](Vollständige%20Induktion.md)

# Kasusgrammatik
Die gleiche Bedeutung kann in unterschiedlichen Sprachen mit verschieden Strukturen und Wörtern codiert werden.
Die Kasusgrammatik ist ein System das die Beziehungen zwischen Subjekten, Objekten und der [Valenz](#Valenz) von Verben analysiert.

Die Grundlegenden Rollen einer Aussage bleiben gleich, unabhängig von der Sprache die verwendet wird um diese Information auszudrücken. Man spricht auch von [Semantischen Rollen](#Semantische%20Rollen).

## Valenz
Verben verlangen eine unterschiedliche Anzahl von Argumenten oder Satzteilen.

| Intransitive Verben | Transitive Verben           | Ditransitive Verben          |
| ------------------- | --------------------------- | ---------------------------- |
| Die Sonne scheint   | Der Hund frisst den Knochen | Er gibt der Frau einen Apfel |
| Valenz von eins     | Valenz von zwei             | Valenz von drei              |

## Semantische Rollen
Beschreiben die Funktionen die ein Satzteil im Bezug der Handlung einnimmt.
- Agent: Der Handelnde (z.B. "Der Lehrer" in "Der Lehrer unterrichtet die Schüler")
- Patient: Der von der Handlung betroffene (z.B. "die Schüler" im obigen Beispiel)
- Instrument: Ein Hilfsmittel zum Erfolg der Handlung

Die Anordnung der Satzteile kann deren Bedeutung beeinflussen.
"Der Hund jagt die Katze" vs. "Die Katze jagt den Hund"

## Kasusrollen
Laut Fillmores Theorie gibt es sechs Hauptrollen
- Agent: Absichtlich Handelnder
- Experiencer: Der Handelnde ohne Absicht
- Theme: Das Objekt, das eine Veränderung erfährt
- Instrument: Das Werkzeug mit dem die Handlung ausgeführt wird
- Beneficiary: Person oder Objekt für die eine Handlung ausgeführt wird
- To/At/From Loc/Poss/Time: Bezieht sich auf den Besitz von Dingen, Orten oder Zeiten

### Komplikationen
Eine Syntaxeinheit kann mehrere Rollen annehmen
"Jack cut the Fish" mit 'Jack' als Agent vs. "A Knife cut the Fish" mit 'A Knife' als Instrument.

Ebenfalls können unterschiedliche Strukturen die selbe Rollenverteilung behalten.

### Regeln der Kasusrollen
- Es gibt Ausnahmen
- Eine Kasusrolle pro Konstituente (Pro Subjekt / Objekt nur eine Rolle)
- Keine doppelten Rollen.
  Innerhalb einer Regel darf keine Rolle mehrfach erscheinen
- Koordinierung von [NPs](04%20Syntax.md#Nominalphrasen): Nur NPs derselben Kasusrolle können kombiniert werden. In "Der Lehrer und die Schüler sind hier" sind beide Subjekte Agenten

### Auswahlbeschränkungen
Sind Regeln die festlegen, welche Kasusrollen in bestimmten Kontexten verwendet werden dürfen.
- Agenten:
  Müssen animiert sein, also lebendige Wesen darstellen
- Instrumente:
  Müssen unbelebte Objekte sein die zur Ausführung einer Handlung verwendet werden
- etc.

# Semantische Analyse
Ist der Prozess um Bedeutung und Informationen aus Texten und Äußerungen zu identifizieren.

Beispielsweise die automatische Analyse von Kunden-Emails oder die Auswertung von Gesprächen um die Interaktionen mit dem Kundendienst zu bewerten.

## Wortfrequenz
Allein durch die Häufigkeit von Begriffen in einem Text kann eine erste Information zu Inhalt und Stimmung erkannt werden.

## Kontext
Um Missverständnisse zu vermeiden muss der Kontext der Unterhaltung / des Textes beachtet werden.

## Notwendigkeit
Wenn Wörter ohne Kontext analysiert werden, sind Antworten häufig irrelevant oder falsch.

Wörter können falsch interpretiert werden, dadurch wird die Verarbeitung deutlich erschwert.
Im Englischen gibt es für jedes Substantiv ca. 5-8 Synonyme.
