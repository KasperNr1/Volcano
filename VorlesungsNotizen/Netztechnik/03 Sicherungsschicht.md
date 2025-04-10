# Aufgaben
Sender: Pakete in Frames verpacken
Empfänger: Frames aus dem Bitstrom erkennen und auslesen

Mac Adressen bereitstellen
Zugriff auf Übertragungsmedium

# MAC
Adressierung
Fehlererkennung
Einteilung in Frames

# Geräte
## Bridge
Mehr als 2 Ports -> Heißt Layer-2-Switch oder Multiport-Switch
Hat keine eigene Adresse

### Transparente Bridges
Nicht Sinnvoll alle Frames an alle Geräte zu senden
## WLAN-Bridge
Verbindet Kabelanschlüsse mit WLAN

# WLAN
Lokales Funknetz
Beschreibt nur die beiden unteren Schichten 
Wi-Fi ist eine spezielle Zertifizierung

## Ad-Hoc
Weniger Teilnehmer (Max. 8) tauschen in einer gewissen Reichweite Daten aus, schnell und einfaches Setup
Nintendo Mulitplayer

## Infrastruktur
"Normaler" Modus eines Routers

## WDS

## TSN
Garantiert bestimmte Latenzzeiten und Bandbreiten für kritische Daten


# Rahmenbildung
## Längenangabe im Header
- Zeichenstopfen
- Bitstopfen
- Verstöße gegen Regeln des Leitungscodes werden nicht behandelt

Längenangabe im Header ist Schwachstelle, falscher Wert zerstört lesende Möglichkeit

## Zeichenstopfen
Bestimmte Symbole als Start und End-Zeichen
Enge Anlehnung an ASCII Codierung

EOF-Character darf nicht im Inhalt vorkommen
-> Escaping mit besonderem Symbol
-> Dieses darf auch nicht vorkommen, Existenz in den Daten wird als EscEsc codiert und vom Leser entfernt

## Bitstopfen
Spezielle Bitfolge als Anfangs und End-Sequenz "01111110"
Darf Ebenfalls nicht im Content enthalten sein.
-> Sender fügt nach 5 1er eine 0 ein, Empfänger ignoriert 0er die nach 5 benachbarten 1ern gesendet werden

---
Bei Wlan wird nicht jede Nachricht immer von jedem empfangen, Kollisionen müssen eher vermieden als behandelt werden

