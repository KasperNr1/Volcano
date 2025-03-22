# Netzwerk
Ein Netzwerk ist eine Gruppe von (Computer-)Systemen die über Kommunikationsleitungen verbunden sind und gemeinsame Ressourcen und Informationen nutzen.
Es umfasst sowohl die physische Einrichtung als auch die entsprechenden Vermittlungs- und Übertragungsverfahren.
# Netzwerktypen
- PAN
  Personal (Bluetooth)
- LAN
  Local (Heimnetz)
- MAN
  Metropolitan
- WAN
  Wide Area (Mobilfunk)
- GAN
  Global (Internet)

# Netzwerktopologien
Beschreiben verschiedene Varianten Rechner in einem System mit einander zu verbinden. Bei der Entscheidung sind verschiedene Eigenschaften der unterschiedlichen Optionen zu beachten. Beispielsweise die Erweiterbarkeit des Systems oder das Verhalten bei Ausfällen eines Einzelnen relevant.
Übertragungsgeschwindigkeit und tatsächliche physische Anschlussmöglichkeiten spielen ebenfalls eine Rolle.
![](Netztopologien.png)
## Vermascht
Verbindungen werden zwischen Computern gezogen deren Kommunikation besonders hohe Übertragungsraten benötigt.
Wenn jedes Paar an Rechnern eine Verbindung besitzt, so spricht man von einem voll-vermaschten System.
### Vorteile
- Optimale Datenübertragung
- Ausfall eines Computers hat kaum Einfluss auf das restliche Netzwerk
### Nachteile
- Komplex und Teuer
  (Besonders bei weiten Wegen)
- Schlechte Skalierbarkeit
  (Extremer bei Vollvermaschung)

## Bus
Alle Rechner sind an eine Zentrale Datenleitung angebunden. So werden alle Daten von immer von jedem Empfangen und individuell verwendet oder aussortiert.
### Vorteile
- Erweiterung sehr Einfach
### Nachteile
- Kabelprobleme können einen Totalausfall verursachen
- Anteil nicht-relevanter Nachrichten pro Gerät steigt stetig mit Größe des Systems
- Abschlusswiderstände sind notwendig um Probleme der physischen Leitung zu kontern
## Linie / Ring
Jedes Gerät (mit Ausnahme der Linienenden) ist mit exakt zwei Geräten verbunden.
Die Verbindung zwischen erstem und letztem Gerät ist der entscheidende Unterschied zwischen Ring und Linie.
Im Gegensatz zum [Bus](#Bus) gibt es hier kein zentrales Medium
### Vorteile
- Ressourcensparend
- Leicht zu erweitern
### Nachteile
- Ausfall einer Verbindung kann das Netzwerk lahm legen
- Bei großen Systemen weite Wege für Daten
## Stern
Alle Teilnehmer sind mit einem zentralen Hub oder Switch verbunden.
### Vorteile
- Einfach aufzubauen
- Leicht zu erweitern
- Ausfall eines Computers hat keine Wirkung auf restliches Netzwerk
### Nachteile
- Hub kann zum Bottleneck werden
- Totalausfall bei Störung der zentralen Komponente
## Ring mit RLV
RLV ist eine Abkürzung für "Ringverteilungsleiter"
Der Aufbau vereint die physischen Eigenschaften des [Stern](#Stern) und die logischen Eigenschaften eines [Ring](#Linie%20/%20Ring).
![](RLV.png)
### Vorteile
- Hohe Ausfallsicherheit
- Jede Station ist ein Repeater
- Leicht zu erweitern
- Ressourcensparend
### Nachteile
- Störung der zentralen Einheit kann Totalversagen verursachen
- Hub kann zum Bottleneck werden
## Baum
Computer sind in einer hierarchischen Struktur miteinander verbunden.
Ähnlich zur [Stern-Stern](#Stern-Stern) Topologie, hier jedoch strengere Reihenfolge.
### Vorteile
- Ausfall eines Endgeräts hat keinerlei Konsequenz
### Nachteile
- Ausfall eines Verteilers legt Sub-Baum lahm
## Stern-Stern
Router werden [Stern-artig](#Stern) angeordnet, Endgeräte ebenfalls Sternmäßig mit den einzelnen Routern verbunden. Wird in der Praxis häufig für lokale Netzwerke verwendet.
![](StarStar.png)
# Übertragungsarten
## Simplex
Verbindung von $A$ nach $B$ mit Kommunikation in einer festen Richtung

## Halbduplex
Übertragung zwischen $A$ und $B$ abwechselnd in beide Richtungen (Walkie-Talkie)

## Vollduplex
Gleichzeitige Übertragung in beide Richtungen

## Multiplex
Multiplexverfahren sind eine Möglichkeit mehrere Signale zu bündeln um die Effizienz der Kommunikation zu steigern.
Dabei werden verschiedene Arten unterschieden.
### Raummultiplex
Jedes Signal erhält eine eigene Leitung. So kann ohne Interferenz oder Wartezeit gleichzeitig von mehreren Kanälen gesendet werden. Dieser Ansatz ist jedoch besonders bei sehr großen Netzwerken schwer zu skalieren.
## Zeitmultiplex
Jeder Benutzer erhält einen Zeitraum in dem er berechtigt ist Daten zu versenden. Die Kommunikation erfolgt so strikt abwechselnd. Eventuell entstehen kleine Verzögerungen.
Diese Variante ist ähnlich der [Multiplexer](De-Multiplexer.md) Schaltungen, die einen ausgewählten Kanal zur Kommunikation freigeben.
## Frequenzmultiplex
Verschiedene Sender kommunizieren auf individuellen Wellenlängen. Das entstehende Mischsignal kann durch [Fourier Transformation](https://en.wikipedia.org/wiki/Fourier_transform) wieder zerlegt werden.
## Codemultiplex
Verwendung unterschiedlicher Codierungen

# Adressierungsarten
TODO 
Ab Seite 33 Foliensatz 1
