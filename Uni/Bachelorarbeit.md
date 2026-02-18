KW 24-40
Abgabe: 31. **August** 2026
[Anmeldeformular](https://www.dhbw-stuttgart.de/studierendenportal/horb/informatik/studienbetrieb/bachelorarbeit/t3-3300-bachelorarbeit/)

# Anmeldung
## Student
Matti
Bos
Informatik \ INF23
9227451

"Entwicklung eines KI-Agenten zur dynamischen Anpassung der Heizleistung beim Kantenanleimen"

## Unternehmen
HOMAG Group AG
Homagstraße 3-5
72296 Schopfloch

## Betreuer
Ruven Weiss
M. Eng.
+49 7443 13-2586
Ruven.Weiss@homag.com

## Beschreibung
Das Kantenanleimen ist ein Prozessschritt in der Möbelfertigung, bei dem ein Kunststoffband (Kantenband) an die Schmalseite einer Holzplatte (meist Spanplatte) geklebt wird.  
Hierfür wird das Kantenband durch eine Heizzone transportiert und erhitzt, bevor es anschließend mit dem Holzwerkstück verklebt wird.  
Für die Qualität der Verklebung spielt die Temperatur des Klebstoffs am Kontaktpunkt mit dem Werkstück (Fügetemperatur) eine entscheidende Rolle.  
Die Regelung dieser Temperatur erfolgt auf der Maschinen-SPS und ist äußerst anspruchsvoll.  
Insbesondere gilt dies auf Stationärmaschinen, wo sich die Bearbeitungsgeschwindigkeit sehr dynamisch ändert.  
Diese Geschwindigkeitsänderungen resultieren aus der CNC-generierten Bahnplanung und können von der Maschinen-SPS nicht gesteuert werden.  
Sie verursachen unweigerlich Schwankungen der Fügetemperatur.

Die Aufgabe einer Temperaturregelung besteht also darin, diese Schwankungen auszuregeln, indem die Heizleistung dynamisch angepasst wird.  
Bisherige Untersuchungen haben bereits gezeigt, dass ein vorausschauender Ansatz für die Regelung die bisher gängigen Methoden schlagen kann.  
Informationen über den Verlauf der Vorschubgeschwindigkeit in einem bestimmten Vorhersagehorizont werden der SPS zur Laufzeit von der CNC zur Verfügung gestellt.

Basierend auf diesen Informationen soll in dieser Arbeit ein KI-basierter Ansatz für eine Temperaturregelung entworfen und untersucht werden.  
Hierfür steht ein Simulationsmodell zur Verfügung, mit dessen Hilfe ein KI-Agent trainiert werden kann.  
Da es sich hierbei um ein dynamisches System in Form eines Markov-Modells handelt, ist ein Reinforcement-Learning basierter Ansatz naheliegend.

## Vorgehen
1. Anforderungsanalyse:
	1.1 Identifikation der relevanten Einflussgrößen auf die Fügetemperatur
	1.2 Definition der Zielkriterien für die Regelung
	1.3 Ermittlung der Verfügbaren Ein- und Ausgabedaten aus CNC und SPS
2. Konzeptentwicklung
	2.1 Definition des Entscheidungsprozesses (Zustände, Aktionen, Belohnungen)
	2.2 Auswahl der RL-Methodik
	2.3 Entwicklung einer Software- und Modellarchitektur 
3. Entwicklung und Training
	3.1 Implementierung des Agenten im Simulationsumfeld
	3.2 Training des Modells
	3.3 Optimierung von Hyperparametern und Belohnungsfunktion
4. Validierung
	4.1 Durchführung von Tests mit realistischen Daten
	4.2 Quantitative Bewertung der Regelungsleistung

Anmerkung: Das Vorgehen findet in Form eines agilen Vorgehens statt, vor allem Punkte 2-4 werden Iterativ mehrmalig durchlaufen.
# Thema
[Klebe-Heizung](#Klebe-Heizung)
## Titel
1. Echtzeit-Temperaturregelung im Kantenanleimen mittels KI-basierter Vorhersagemodelle
2. Entwicklung eines KI-Agenten zur dynamischen Anpassung der Heizleistung beim Kantenanleimen
3. Reinforcement Learning zur dynamischen Steuerung der Heizleistung im Kantenanleimprozess
4. Reinforcement-Learning-Gestützte Prädiktive Steuerung der Heizleistung im Kantenanleimprozess
5. Reinforcement Learning im Kantenanleimprozess: Ein simulationsgestützter Ansatz


## Beschreibung
Das Kantenanleimen ist ein Prozessschritt in der Möbelfertigung, bei dem ein Kunststoffband (Kantenband) an die Schmalseite einer Holzplatte (meist Spanplatte) geklebt wird.  
Hierfür wird das Kantenband durch eine Heizzone transportiert und erhitzt, bevor es anschließend mit dem Holzwerkstück verklebt wird.  
Für die Qualität der Verklebung spielt die Temperatur des Klebstoffs am Kontaktpunkt mit dem Werkstück (Fügetemperatur) eine entscheidende Rolle.  
Die Regelung dieser Temperatur erfolgt auf der Maschinen-SPS und ist äußerst anspruchsvoll.  
Insbesondere gilt dies auf Stationärmaschinen, wo sich die Bearbeitungsgeschwindigkeit sehr dynamisch ändert.  
Diese Geschwindigkeitsänderungen resultieren aus der CNC-generierten Bahnplanung und können von der Maschinen-SPS nicht gesteuert werden.  
Sie verursachen unweigerlich Schwankungen der Fügetemperatur.

Die Aufgabe einer Temperaturregelung besteht also darin, diese Schwankungen auszuregeln, indem die Heizleistung dynamisch angepasst wird.  
Bisherige Untersuchungen haben bereits gezeigt, dass ein vorausschauender Ansatz für die Regelung die bisher gängigen Methoden schlagen kann.  
Informationen über den Verlauf der Vorschubgeschwindigkeit in einem bestimmten Vorhersagehorizont werden der SPS zur Laufzeit von der CNC zur Verfügung gestellt.

Basierend auf diesen Informationen soll in dieser Arbeit ein KI-basierter Ansatz für eine Temperaturregelung entworfen und untersucht werden.  
Hierfür steht ein Simulationsmodell zur Verfügung, mit dessen Hilfe ein KI-Agent trainiert werden kann.  
Da es sich hierbei um ein dynamisches System in Form eines Markov-Modells handelt, ist ein Reinforcement-Learning basierter Ansatz naheliegend.

# Themen
## Digitaler Zwilling
Für das Lagersystem

Mit ISG-Virtuos "zusammenklicken"
Geliefert wird 3D Modell der Maschine und SPS, Nachbauen des Modells und Ausstattung mit logischen Bausteinen (Piston / Förderband) um Funktion abzubilden


## Klebe-Heizung
[Reinforcement-Modell](09%20Reinforcement%20Learning.md#Lernende%20Agenten) trainieren um die Heizung des Klebstoffs auf die variable Geschwindigkeit des Aggregats anzupassen.


## Qualitäts Sensor
Mit Kamera und Abstandsmesser Fehler bei produzierten Werkstücken ermitteln. Welche Fehler können überhaupt erkannt werden?


