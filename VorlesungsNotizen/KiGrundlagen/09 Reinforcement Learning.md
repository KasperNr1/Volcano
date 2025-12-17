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
Es wird ein Dictionary erstellt in dem zu jedem Zustand für jede Aktion einen Qualitätswert $Q$ zuordnet. Dieser Wert $Q$ berechnet sich aus dem Reward für die aktuelle Aktion und dem maximalen Reward der folgenden Aktionen.
$$
Q(s_t, a_t) = r_t + \gamma\
$$