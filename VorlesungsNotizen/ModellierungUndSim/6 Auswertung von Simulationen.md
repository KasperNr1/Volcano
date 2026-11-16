---
course: "[[Modellierung und Simulation 1]]"
lecture: "6"
source: https://unitc-my.sharepoint.com/personal/iinme01_cloud_uni-tuebingen_de/_layouts/15/stream.aspx?id=%2Fpersonal%2Fiinme01%5Fcloud%5Funi%2Dtuebingen%5Fde%2FDocuments%2FTeaching%2DGITs%2Fmodellierung%5Fund%5Fsimulation%2FOnline%2FVideos%2FMuS%5F5%2D2%5F6%2D1%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2Eedcf2b2c%2Dcd48%2D4748%2Dba61%2Dc991f353795b
date: 2026-11-15
tags:
  - lecture
---
# Transiente Phase 
![](TransientSimulationPhase.png)
Zu Beginn kann eine Simulation mit Werten initialisiert sein, die nicht dem normalen Zustand des Systems entsprechen. Beispielsweise mit einer leeren initialen Warteschlange. So haben frühe Kunden eine geringere durchschnittliche Wartezeit.

Nach einiger Zeit (Aufwärmzeit) stabilisiert sich das System und der Zustand ist nur noch schwach abhängig vom Startzustand.
Erst dann kann für manche Fragestellungen mit der Erhebung der tatsächlichen Ergebnisse begonnen werden.

> [!Question] Woran erkennt man das Ende der Aufwärmphase?
> Das Ende der Transienten Phase zu erkennen ist schwierig.
> 
> Generell sind die Histogramme für aufeinanderfolgende Ereignisse gleich oder sehr ählich. (Siehe obere Abbildung)
> Dabei ist die Länge der Transienten Phase ist sehr stark von den initialen Parametern des Systems abhängig.

## Naive Methode zur Erkennung
Paralleles Simulieren von $n$ Simulationen zur Erkennung von ähnlichen Histogrammen der Zufallsvariablen.

Enormer Rechenaufwand macht diese Methode in der Praxis sehr unbeliebt.

## Graphisches Verfahren
Einfacher als die [Naive Methode zur Erkennung](#Naive%20Methode%20zur%20Erkennung) und schnellere Konvergenz. Dabei beschreibt die Konvergenz nicht das Ende der Transienten Phase sondern die Anzahl der Testläufe um dieses Ende zu bestimmen.

Dabei werden Messwerte aus $n$ parallelen Läufe bestimmt, wobei $X_i^j$ der Wert zum Zeitpunkt $i$ in Lauf $j$ ist.

Die Reihe der gemittelten Messreihen wird gebildet:
$$
\overline{X}_i = \frac{\sum_{j=1}^n X_i^j}{n}
$$
Es wird der Wert $i$ bestimmt, ab dem die Messreihe konvergiert.
Dieses $i$ beschreibt das Ende der initialen Phase.

Mit $l=i$ kann die "Richtige” Simulation berechnen.
Ihr Mittelwert liegt damit bei
$$
\overline{X}(m,l) = \frac{\sum_{j=l+1}^m X_i^j}{m-l}
$$


> [!Missing] Moving Average
> Gleichung 5.7 im Skript
> 
> Bei extrem stark schwankenden Variablen lässt sich nicht immer ein Trend erkennen.
> Mit Gleitendem Durchschnitt kann hier ggf. ein Trend erkannt werden um die Initialisierungsphase zu erkennen.



