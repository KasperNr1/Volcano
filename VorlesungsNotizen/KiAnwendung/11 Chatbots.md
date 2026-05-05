Es wird unterschieden zwischen reinen Chatbots und (Aufgabenbasierten) Dialogsystemen unterschieden.
Während die Chatbots nur für Unterhaltungen gebraucht werden können, sind die Agenten auch in der Lage mit Schnittstellen von Autos/Robotern oder anderen Smarten Geräten zu kommunizieren.

# Aufgabenbasierte Dialogagenten
Bisherige Systeme verwenden eine Rahmenbasierte Architektur, bei der die Struktur der Aufgabe fest vorgegeben ist und gewisse Slots mit dynamischen Werten gefüllt werden.

![](FrameArchitecture.png)

# Konversationsregeln
Da Konversationen abwechselnde Handlungen der beiden Partner erfordern, ist es wichtig diese Wechselpunkte im Gespräch zu erkennen.

![](LengthOfSpeechTurns.png)

Dabei kann die Länge eines vollständigen "Zugs" stark variieren.
Auch sind Pausen im Satz häufig, wenn ein Teilnehmer innehält um beispielsweise seine nächsten Worte zu wählen.


> [!QUOTE] Sprache als Aktion
> Each turn in a dialogue is a kind of action.


## Sprechakte
- Konstative Akte
  Beschreiben oder informieren über einen Sachverhalt
- Direktive Akte
  Fordern den Hörer zu einer bestimmten Handlung auf.
- Kommissive Akte
  Verpflichten den Sprecher zu einer zukünftigen Handlung
- Expressive Akte
  Äußern Gefühle oder emotionale Zustände
## Grounding
Bezeichnet den Prozess, durch den Gesprächspartner sicherstellen, dass sie ein gemeinsames Verständnis über Inhalt und Verlauf ihres Dialogs haben.

In Gesprächen wird dies durch direkte Bestätigungen ('ja', 'genau' etc.) oder Wiederholungen und Paraphrasen erreicht. 
Auch Nonverbale Signale wie Kopfnicken haben diesen Effekt.

In anderen Mensch-Maschine-Interaktionen wird Grounding auch verwendet. Beispielsweise bei Aufzugknöpfen. Das Leuchten nach der Betätigung dient nur dazu, dem Nutzer die Aktivierung zu bestätigen.

![](ElevatorButton.png)

## Konversationsstruktur
Bestimmte Strukturen sind sehr häufig. Beispielsweise folgt auf eine Frage meist eine Antwort, auf einen Vorschlag eine Akzeptanz oder eine Ablehnung.
Diese Muster helfen Systemen dabei, geeignete Aktionen zu bestimmen.

### Subdialoge
Beide Gesprächspartner können einen Subdialog starten, um Missverständnisse schnell aufzulösen oder fehlenden Kontext zu erfragen damit mit einer ursprünglichen Frage weitergearbeitet werden kann.
![](CorrectionSubdialogue.png)

![](ClaritySubdialogue.png)

### Präsequenzen
Manche Fragen werden durch eine Präsequenz eingeleitet
``` Text
A: Can you make train reservations?
B: Yes I can.
A: Great, please reserve ...
```

### Schlussfolgerungen
Manche Informationen sind implizit im Kontext enthalten. Diese zu extrahieren ist für Maschinen sehr schwierig.

``` Text
A: And what day in May did you want to travel
B: Ugh, I need to be there for a meeting from the 12th to the 15th.
```

Die gewünschte Reisezeit ist vermutlich einen Tag vor dem Termin des Meetings.

# Chatbots
## Regelbasierte Chatbots
### ELIZA
ELIZA basierte auf simplen REGEX, um die Aussagen der Probanten näher zu hinterfragen.
Dabei folgte auf ein `feel like X` stets ein `why do you feel like X`. Durch die Stellung als Psychater ist eine Stellung akzeptabel, bei der kein Weltwissen vorhanden ist und quasi nur mit Fragen gearbeitet wird.

Obwohl nur feste Regeln befolgt werden, verknüpften einige Benutzer menschliche Attribute mit dem System.

### PARRY
Verwendet Variablen um einen internen Zustand für Angst, Wut und Mistrauen zu halten. Alle Werte starten niedrig und werden durch bestimmte Schlüsselworte verändert um einen paranoiden Menschen zu simulieren.

Dieser Chatbot konnte erstmals eine Form des Turing-Test bestehen.

## Korpusbasierte Chatbots
Sie benötigen keine explizite Programmierung der Antwortregeln. 
Aus einem Korpus werden Muster erkannt, um Gespräche zu vervollständigen.

Da die Trainingsprozesse sehr datenintensiv sind, ist es nötig eine große Menge von Gesprächen aus Telefonaten / Filmen / Büchern zu verwenden.

### Information Retrieval

> [!Missing] Fehlt
> Seite 687-693


## Bewertung
Gut für enge, skriptbare Anwendungen. 
Für Nutzer kann die Illusion des Verständnis problematisch sein.
Regelbasierte Chatbots sind sehr aufwändig zu implementieren, [IR](#Information%20Retrieval)-basierte Modelle spiegeln nur ihre Trainingsdaten wieder.

Nächste Schritte sind die Integration der Chatbots in frame-basierte Agenten. Damit können Anfragen frei formuliert werden, die Chatbots formen diese dann in die entsprechende Zielstruktur um.

# Frame-basierte Dialogagenten
Grundlegend in einer von zwei Architekturen:
1. GUS-Architektur
   Auch als "Frame-Basierte Architektur" bekannt.
   Wird in den meisten industriellen Anwendungen verwendet
2. Dialogzustandarchitektur
   Erweiterung von GUS
   Häufiger in Forschungssystemen

Das System stellt dem Benutzer fragen, um die Slots zu füllen. Dabei können aus einer Antwort mehrere Informationen extrahiert werden.

![](GusInference.png)
 Auch einfache Inferenzen sind mit Hilfe von [NLP](VorlesungsNotizen/KiAnwendung/01%20Einführung.md#Natural%20Language%20Processing)möglich.
![](NlpToFillSlots.png)


Problem bei solchen Systemen ist der Recall. Eventuell werden nicht alle relevanten Daten direkt erkannt oder nicht korrekt aus dem Kontext erschlossen.

## Dialogakte
Die Ideen von Sprechakten und Grounding werden in einer einzelnen Repräsentation kombiniert.
![](Dialogakte.png)

### BIO-Tagging
BIO-Tagging ist eine Methode um Slots besser zu füllen. Jedes Wort im Satz erhält eine der folgenden Kategorien:
- B (Beginning) Anfang eines Slot-Fillers
- I (Inside) Teil derselben Slot-Filler-Einheit
- O (Outside) Kein Teil eines Slot-Fillers

Somit soll die Information präzise aus Benutzeräußerungen extrahiert werden.

![](Bio-Tagging.png)

Dieses Tagging kann durch einen eigens dafür trainierten [Klassifikator](01%20Grundidee.md#Klassifikation) erfolgen.

## Erkennung von Korrekturen
Korrekturen in der gesprochenen Sprache werden deutlich häufiger missverstanden als normale Anweisungen. 
Aufgrund der Tendenz zur Hyperartikulation (BAL-TI-MORE statt Baltimore) haben Systeme Schwierigkeiten, da sie auf normaler Aussprache der Worte trainiert wurden.

Typische Merkmale von Korrekturen sind die Einleitung durch spezifische Worte ("NEIN" oder "Ich meinte") oder Wiederholungen.

Um Fehler frühzeitig zu erkennen wird mit verschiedenen Bestätigungen gearbeitet. Aussagen die sehr extrem vom bisherigen Kontext abweichen, können stärker misstraut werden als solche, die sehr ähnlich zur vorherigen Aussage sind.

Diese Bestätigungen können auch implizit geschehen, um den Gesprächsfluss weniger stark zu bremsen.
![](ImpliciteConfirmation.png)

Bei Eingaben in denen kein eindeutiger Inhalt erkannt wird, kann die wahrscheinlichste Möglichkeit bestätigt werden, oder mit einer Ablehnung gearbeitet werden.
"Ich suche nach X" vs. "Das habe ich leider nicht verstanden"

Diese Techniken können auch kombiniert werden, um einen Kompromiss aus Korrektheit und Geschwindigkeit zu erhalten und nicht bei Problemen stecken zu bleiben.
![](FehlerbehandlungsKompromiss.png)

Es kann auch konkret nach den Informationen gefragt werden, falls sie nicht im Text erkannt wurden.
![](PreciseQuestionAfterProblem.png)

Wenn mit einem Konfidenzscore gearbeitet wird, kann dynamisch zwischen den verschiedenen Möglichkeiten der Fehlererkennung gearbeitet werden. So wird bei eindeutigen Aussagen nicht unnötig oft nachgefragt oder bestätigt.

# Bewertung von Chatbots
Um die Qualität eines Systems zu bestimmen, wird bei Chatbots mit direkten Fragen an den Benutzer gearbeitet. 
Anhand verschiedener Metriken wie 
- Wiederholungen
- Flüssigkeit
- Neugier
- Unterhaltsamkeit

Wird die Performance des Systems bewertet.

Für Aufgabenbasierte Systeme kann die Erfolgsrate und Dauer der Bearbeitung einer Aufgabe gemessen und automatisch verglichen werden.

![](TaskSuccessEvaluation.png)