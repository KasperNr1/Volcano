# Design

## Start Screens
### Home Screen
![](IconAndName.png)

### App Launch Screen
![](AppLaunchScreen.png)

Ermöglicht die Erstellung einer [Skitour](#Skitour).

### EHB Screen
Hier können [EHB](#EHB) erstellt werden.
![](EhbStartScreen.png)

Bei der Auswahl bestehender [EHB](#EHB)s kann nichts verändert werden. Alle Daten und Antworten auf die Fragen sind fest.

![](EhbViewing.png)

Das eigentliche Ergebnis steht ganz unten und ist nur nach einigem Scrollen erreichbar.

![](EhbViewScrolledDown.png)

### Lawinenlageberichte
Nicht wirklich implementiert
![](LawinenlageScreen.png)

### Komponenten
Hier sind einige Werkzeuge untergebracht. Darunter ein Kompass, Neigungsmesser und eine interaktive Karte.

![](Components.png)

#### Kompass
Funktioniert vielleicht?
Im Simulator nicht gut zu testen

![](Compass.png)

#### Hangneigung
Kann evtl. mit Kamerazugriff funktionieren? Ebenfalls nicht (gut) im Simulator testbar

![](Hangneigung.png)

#### Karten
Apple Maps 

![](MapIntegration.png)

### Informationen
Diese Seite soll als Zentrum für relevante Informationen dienen. Sie ist nicht interaktiv
![](InfoPage.png)


![](InfoPageDetailed.png)
# Features
## Skitour
Können erstellt und gelöscht werden, sie enthalten einige wenige Informationen wie Name, Ziel, Datum und eine Schwierigkeitsstufe.
![](TourCreation.png)

Erst nach der Erstellung kann ihr durch Auswahl auf der Startseite eine bereits bestehende [EHB](#EHB) zugewiesen werden.


> [!error]- Flow
> Nutzer kann nach dem Start der App auf der [Hauptseite](#App%20Launch%20Screen) nicht wirklich arbeiten.
> Es ist nicht ersichtlich, dass er die Bewertung hinzufügen muss. Selbst um es zu tun muss erst auf die [zweite Seite](#EHB%20Screen) navigiert werden, bevor die Daten abgespeichert und zugewiesen werden können


![](HomeScreenWithExampleTour.png)

![](AddingEhbToTour.png)

Nachdem eine EHB separat erstellt und hier zugewiesen wurde, kann sie angesehen werden. Dabei wird dieselbe Ansicht präsentiert, die auch im [EHB Screen](#EHB%20Screen) nach der Auswahl einer bestehenden Bewertung zu sehen ist.

Es ist möglich mehrere Bewertungen zuzuweisen
![](TourWithMultiEhb.png)

## EHB
"Einzelhangbewertungen" sollen das Key-Feature der App sein.
![](EhbCreation.png)

![](ProblemSelection.png)
Warum ist die Anzahl der Probleme begrenzt?

![](EhbProblemQuestions.png)

![](ProblemQuestionaireProblems.png)
Es können (Falls sie existieren würden) Erklärungen zu den Fragen eingeblendet werden.

Teilweise ist die Beschriftung der Buttons abgeschnitten und nicht lesbar.

![](EhbProblemQuestionaireQuestionSelection.png)
Hier kann zu einer "allgemeinen Frage" gewechselt werden (Warum??)


![](EhbQuestionsLastQuestion.png)

![](EhbResultDuringQuestionaire.png)