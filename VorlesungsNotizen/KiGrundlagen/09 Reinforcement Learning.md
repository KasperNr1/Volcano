# Software Agenten
Ein Agent ist ein Stück Software, die autonomes Verhalten zeigt.
Es ist also nach dem Start kein menschliches Eingreifen erforderlich.

- Einfache reaktive Agenten:
  Definition: Reagieren direkt auf aktuelle Zustände mit festgelegten Regeln.
  Beispiel: Ein Thermostat, der die Heizung bei Unterschreitung einer bestimmten Temperatur einschaltet.
- Beobachtende Agenten:
  Definition: Nutzen ein internes Modell, um Entscheidungen basierend auf aktuellen und früheren Zuständen zu treffen.
  Beispiel: Ein Roboterstaubsauger, der Möbel erkennt und seine Reinigungsrouten optimiert.
- Zielbasierte Agenten:
  Definition: Treffen Entscheidungen, um spezifische Ziele zu erreichen. 
  Beispiel: Ein Navigationssystem, das alternative Routen vorschlägt, um Staus zu umgehen.
- Nutzenbasierte Agenten:
  Definition: Bewerten Optionen anhand eines Nutzenmaßes und wählen die beste aus.
  Beispiel: Ein Online-Shop, der Produktempfehlungen basierend auf Nutzerpräferenzen und Preisen gibt.
- Lernende Agenten:
  Definition: Lernen aus Erfahrungen und verbessern ihre Leistung kontinuierlich.
  Beispiel: Ein selbstfahrendes Auto, das seine Fahrstrategien anpasst, um sicherer zu fahren.

## Lernende Agenten
Der Agent versucht immer wieder dasselbe Problem zu lösen. Für (Teil-)Erfolg erhält er eine Belohnung, die er zu maximieren versucht.
Kennzeichnend ist, dass der Agent ohne "Vorwissen" startet. Er muss alle Verfahren und Strategien selbst entwickeln.

![](ReinforcementLearning.png)

Der Agent befindet sich in einem Zustand im Environment. Er entscheidet sich für eine nächste Aktion. Diese Aktion hat Konsequenzen, er wird in einen neuen Zustand versetzt und erhält Feedback (Reward) je nach Qualität der letzten Aktion. Mit diesem Feedback kann er seine Entscheidungsfindung anpassen und so lernen die Entscheidungen zu treffen, bei denen er viele Rewards erhält.

> [!Important] Machbarkeit
> Damit das Training funktionieren kann, muss es in einer Umgebung trainiert werden, in der keine Schäden entstehen können.
> Daher ist fast immer eine Simulation notwendig.


### Rewards
Manche sehr gute Entscheidungen benötigen eine Abfolge von weniger guten Entscheidungen. Damit der Agent diese Wege auch erforscht wird der maximale Rewards der nachfolgenden Knoten weitergereicht. Dabei wird die Belohnung jedoch in jedem Schritt um einen Konstanten Wert oder Faktor verringert.

![](ReinforcementRewards.png)

### Q-Learning
Es wird ein Dictionary erstellt in dem zu jedem Zustand für jede Aktion einen Qualitätswert $Q$ zuordnet. Zu Beginn ist dieses mit "leeren Werten" initialisiert - ohne Erfahrung scheinen alle Möglichkeiten gleich gut. 
Nach jeder Entscheidung wird dieser Wert $Q$ neu berechnet. Er setzt sich aus dem Reward für die aktuelle Aktion und dem maximalen Reward der folgenden Aktionen zusammen.
$\gamma$ beschreibt den "Abzinsfaktor", also das Ausmaß mit dem Belohnungen für Vorbereitungsschritte verliehen werden.
$$
Q(s_t, a_t) = r_t + \gamma \cdot \max_{a}Q(s_{t+1},a)
$$
Oft ist die Umgebung nicht deterministisch. Die selbe Aktion $a$ kann im selben Zustand $s$ abhängig von der Ausführungszeit zu verschiedenen Ergebnissen führen, abhängig von anderen zufälligen Ereignissen in der Umgebung.

Durch die Lernrate $\alpha$ wird dies auch in der Berechnung von $Q$ beachtet. Der Wert wird nicht jedes Mal ersetzt, sondern nur in eine bestimmte Richtung verändert. Für Aktionen die zu unterschiedlichen Resultaten führen, bildet sich so eine Art Mittelwert.
$$
Q(s_{s_t}, a_t) = (1-\alpha) \cdot Q(s_{t}, a_t) + \alpha \cdot (r_t + \gamma \cdot \max_{a}Q(s_{t+1}, a))
$$
Eine Lernrate von $0$ führt dazu, dass nicht gelernt wird, während der Wert $1$ zur Folge hätte, dass die Funktion zur oben genannten simpleren Form degeneriert und jede Belohnung nur von der letzten Erfahrung abhängt.

#### Algorithmus
- $S$ ist die Menge der Zustände $s$ jeweils ein spezifischer
- $A$ ist die Menge der Möglichen Aktionen, $a$ jeweils eine

``` 
# Initialize Rewards
For all 's' in 'S', 'a' in 'A'
	Q(s,a) = 0 # Or random Values
	
# Training
Repeat
	Select Start-state s (randomly)
	
	Repeat
		Perform an Action 'a'
		save reward 'r' and new state 's*'
		Calculate new total reward for Q(s,a)
		's' = 's*'
	Until 's' is end-state or timelimit is reached
Until Q converges	
```

Bei der Auswahl der Aktion $a$ kann das Lernverhalten gesteuert werden. Es können gleichmäßig alle Pfade versucht werden, oder mit Fokus auf vielversprechende Aktionen trainiert werden.
Der gezeigte Algorithmus ist theoretisch vollständig. In echten Anwendungen gibt es oft auch für die äußere Schleife ein Iterationslimit. Wirklich ausgelernt ist das Modell jedoch erst, sobald sich die Belohnungen nicht mehr verändern.

> [!important] Explore vs. Exploit
> Beim Lernen auf zufällige Aktionen zu setzten kann neue Strategien entdecken und "lokale Maxima" vermeiden. 
> Das erforschen bekannter Pfade führt schneller zu besseren Ergebnissen und verfeinert diese. Hier bleiben viele Zustände unbesucht.
> 
> Oft wird eine Mischung der beiden Strategien verwendet, zu beginn wird mehr zufällig gewählt und mit fortschreitendem Training immer stärker auf bekannte Ansätze gesetzt.

