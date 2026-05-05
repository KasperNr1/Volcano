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
