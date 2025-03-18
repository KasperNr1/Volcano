# Multiplexer
Oft als MUX abgekürzt, beschreibt eine Schaltung die mehrere Signale auf wenigen Kanälen verwaltet. Beispielsweise 2 Eingangssignale und 1 Verwaltungssignal. Dabei bestimmt das Verwaltungssignale welches der Eingangssignale auf den einen Ausgabekanal des Multiplexer geschrieben wird.
![](MUX.png)
Die tatsächliche Auswahl des Signals funktioniert, indem jedem Informationssignal eine Binärzahl zugeordnet wird. Wenn die Verwaltungssignale die Zahl symbolisieren wird das entsprechende Informationssignal auf den Ausgang geleitet. Die anderen Signale werden blockiert, da ihr zweiter Eingang des [AND](Boolsche%20Algebra.md#AND) Gatters die Erkennung ihrer Zahl negativ ausfällt.

# De-multiplexer
Auch als DEMUX bezeichnet führt die exakt gegensätzliche Funktion des [Multiplexer](#Multiplexer) aus. Es erhält ein Informationssignal und ein Verwaltungssignal. Anhand des Verwaltungssignals steuert er, auf welchen der vielen Ausgabekanäle die Information weitergeleitet wird.
![](DEMUX.png)
Optimal ausgenutzt sind die Kombinationen dann, wenn insgesamt $n$ Verwaltungssignale und $2^n$ Datensignale in einem (De-)Multiplexer verbaut sind.

