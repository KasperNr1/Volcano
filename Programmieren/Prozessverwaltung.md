Das Anlegen eines neuen [Prozess](Paraprog-Basics.md#Prozess) ist sehr zeitintensiv (20ms)
Eine Möglichkeit variierende Mengen von Aufgaben zu verwalten ist mit dem Pre-Fork-Modell.

# Pre-Fork Modell
Prozesse werden nicht erst angelegt wenn sie benötigt werden.
Stattdessen wird ein Pool an wartenden Prozessen erzeugt die deutlich schneller mit der Bearbeitung einer Aufgabe beginnen können.
Dabei verwaltet ein einzelner Fater-Prozess die Erstellung und Aufgabenverteilung der Kind-Prozesse.
Er selbst kümmert sich nur darum, die Antworten zurück zu liefern.

## Vorteile
Wenn ein Kind crasht kann seine Aufgabe von einem anderen Kind-Prozess erneut bearbeitet werden. So ist der Fehlschlag einer einzelnen Berechnung nie Grund für den Absturz des Gesamtsystems.
Die Berechtigungen der Kinder können auf ein absolutes Minimum eingeschränkt werden, so dass Beispielsweise nur auf einzelne Dateien zugegriffen werden darf.

## Nachteile
Anzahl der benötigten Kind-Prozesse ist variabel und stets unsicher.
Der Vater muss so regelmäßig neue Prozesse anlegen und alte töten um die Menge wartender Kinder konstant zu halten.