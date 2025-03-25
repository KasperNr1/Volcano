# Optimieren eines Teilsystems
Die Auswirkung auf die Performancegewinne eines Gesamtsystems ist stark abhängig von der Nutzungshäufigkeit des optimierten Teilsystems.

Die Verbesserung wird als "SpeedUp" gemessen
$$
\text{SpeedUp} = \frac{\text{Laufzeit ohne Optimierung}}{\text{Laufzeit mit Optimierung}}
$$
Bei einer Nutzungshäufigkeit $P$ eines Teilsystems mit dem SpeedUp $S$ ergibt sich ein Gesamtspeedup $S_{\text{tot}}$
$$
S_{\text{tot}} = \cfrac{1}{(1-P) + \cfrac{P}{S}}
$$
> [!Warning] Achtung
> Die Nutzungshäufigkeit $P$ muss vor der Optimierung gemessen werden. In der optimierten Version wird der Wert kleiner sein da das Problem nun schneller gelöst wird.

## Obergrenze der Optimierung
Die gegebene [Funktion](#Optimieren%20eines%20Teilsystems) hat für $S \to \infty$ einen [Grenzwert](Funktionen.md#Grenzwert). Damit gibt es ein festes oberes Limit für die Performancegewinne durch Optimierung eines Teilsystems.
$$
\lim_{S \to \infty} S_{\text{tot}} = \cfrac{1}{(1-P)}
$$
![Amdahl](Amdahl.png)
So ist beispielsweise ein System mit $20 \%$ Anteil am Systemfluss selbst bei Weglassen nur in der Lage bis zu $25\%$ Geschwindigkeit zu bringen.
$$
S_{\text{max}} = \cfrac{1}{1-0.2} = 1.25
$$
### Beispiel

> [!Example] Klausuraufgabe
> Es existieren 2 Alternativen zur Optimierung eines Programms.
> - Verbesserung der Laufzeit um Faktor $10$ bei einem Modul das $20\%$ Nutzungshäufigkeit hat
> - Verbesserung um Faktor $2$ bei Modul mit $50\%$ Nutzung
> 
> Welche Alternative ist besser, d.h. bringt den höheren Speedup?

$$
S_1 = \cfrac{1}{(1-P) + \cfrac{P}{S}} = \cfrac{1}{(1-0.2) + \cfrac{0.2}{10}} \approx 1.22
$$
$$
S_2 = \cfrac{1}{(1-0.5) + \cfrac{0.5}{2}} \approx 1.33
$$
Die Optimierung des häufigeren Features hat einen größeren Einfluss.