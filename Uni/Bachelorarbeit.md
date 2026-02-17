# Anmeldung
https://www.dhbw-stuttgart.de/studierendenportal/horb/informatik/studienbetrieb/bachelorarbeit/t3-3300-bachelorarbeit/

## Thema
[Klebe-Heizung](#Klebe-Heizung)
### Titel
1. Echtzeit-Temperaturregelung im Kantenanleimen mittels KI-basierter Vorhersagemodelle
2. Entwicklung eines KI-Agenten zur dynamischen Anpassung der Heizleistung beim Kantenanleimen
3. Reinforcement Learning zur dynamischen Heizleistungssteuerung im Kantenanleimprozess
4. Reinforcement-Learning-Gestützte Prädiktive Heizleistungssteuerung im Kantenanleimprozess
5. Reinforcement Learning im Kantenanleimprozess: Ein simulationsgestützter Ansatz


### Beschreibung
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


