Auch auf einer höheren Architekturebene gibt es unterschiedliche Ansätze zur Parallelisierung. Grundlegendster Unterschied ist dabei die Trennung zwischen [Daten und Aufgabenteilung](Paraprog-Basics.md#Arten%20der%20Aufgabenteilung)
# Map-Reduce
Google verwendet die Strategie um schnell relativ gute Suchergebnisse zu liefern.
Eine Suchanfrage trifft ein und wird an verschiedene Server weitergeleitet. Jeder Server hat seinen eigenen Datensatz den er, mit einer individuellen Strategie, nach Treffern durchsucht. Nach kurzer Zeit werden die besten 5 Ergebnisse jedes Servers zusammengefasst und als Gesamtergebnis zurück geliefert.

Der Prozess ist ähnlich wie das Beispiel zur [Aufgabenteilung](Paraprog-Basics.md#Aufgabenparallelismus) mit den Burgern.

1. Anfrage
   5 Burger
2. Aufteilen (Map)
   Dem Koch jeder Zutat wird der Auftrag übergeben jeweils 5 Stück bereitzustellen
3. Zusammenfassen (Reduce)
   Die vorbereiteten Zutaten werden kombiniert und das Ergebnis abgeliefert

# Aktorensystem
Jeder Beteiligte ist ein Aktor. Diese Aktoren haben jeweils eine Liste eingegangener Nachrichten, ähnlich zu einem Briefkasten. Jeder Aktor bearbeitet die an ihn zugestellten Nachrichten und kommuniziert mit Anderen ausschließlich indem er ihnen Nachrichten in ihr Postfach schickt.
Dadurch ist eine extrem hohe Robustheit gegeben, da die Existenz aller Aktoren für die Arbeit eines einzelnen irrelevant ist. 
In jedem Schritt kann ein Aktor 3 verschiedene Dinge tun. Er kann eine Nachricht verschicken, einen neuen Aktor erzeugen oder sein eigenes Verhalten ändern.
Jede Nachricht wird exakt 1 mal verschickt und höchstens 1 Mal empfangen. Verlorene Nachrichten fallen also nicht unbedingt auf.

Angewandt wird diese Strategie beispielsweise bei Online-Multiplayer Spielen wenn ein schnelles Fortsetzen für die Masse wichtiger ist als das perfekte Antworten auf jede einzelne Nachricht.