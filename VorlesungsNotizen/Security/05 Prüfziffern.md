Bei der Datenübertragung zwischen [unterschiedlichen Geräten](01.md#ISO/OSI-Referenzmodell) sind die [Layer 2](01.md#2%20Sicherungsschicht) bis [Layer 4](01.md#4%20Transportschicht) für die [Fehlererkennung- und Korrektur](Codes.md#Fehlerumgang) zuständig. 

Eine Einfache Form der Fehlererkennung ist die Verwendung von [Parity-Bits](DigitaltechnischeBegriffe.md#Parity). Dabei berechnet der Sender die Parität und sendet sein Ergebnis mit der Nachricht zusammen. Der Empfänger berechnet ebenfalls die Prüfziffer und vergleicht seine Antwort mit der empfangenen Prüfziffer. Wenn sie übereinstimmen kann er sich sicher sein, dass kein Fehler vorliegt bei dem ein Bit getauscht wurde.

> [!Info] Sonderfall
> Wenn mehrere Bits getauscht werden scheitert dieses Verfahren. Beispielsweise kann nur erkannt werden, ob eine ungerade Anzahl an Flips vorliegt. Tauscht man exakt 2 Bits, stimmt die Prüfsumme überein.
> Um mehr Fehler zu erkennen gibt es [komplexere Verfahren](Codes.md#Zweidimensionale%20Parität).


# EAN

> [!Example] Klausuraufgabe
> 12 Stellige Zahl + eine Prüfziffer
> Wert-Ziffern werden abwechselnd x3 und x1 gewichtet, Prüfziffer wird gewählt so dass die gesamte gewichtete Summe (Inklusive PZ) =0 Mod 10 ist
> 
> Korrekte Prüfziffer berechnen und Fehlerfreiheit einer Eingabe bestimmen
> 
