Ist ein Sonderfall des [Überwachten Lernens](01%20Grundidee.md#^cf5d0b), die Modelle basieren auf [neuronalen Netzen](07%20Neural%20Nets.md#Neural%20Nets) mit extrem vielen verdeckten Schichten. Diese Anzahl an Schichten ist namensgebend und unterscheidet sie von regulären neuronalen Netzen.

Die Rechenleistung zum Training solcher Modelle ist erst seit dem Jahr ~2000 allgemein verfügbar. Dieses aufwändige Training erfordert enorm viele gelabelte Trainingsdaten.

# Tensoren
Ein Tensor ist eine Struktur um Daten in mehrdimensionalen Arrays zu halten. 
- 0D Tensor oder 'Skalar' ist ein einzelner Zahlenwert 
- 1D Tensor ist ein [Vektor](Vektoren%20und%20Vektorräume.md#Vektoren)
- 2D Tensor ist eine [Matrix](Matrizen.md#Definition)
- Höhere Dimensionen (n-D Tensor)

Sie werden eingesetzt um Datentypen wie Bilder oder Texte darzustellen und Eingabedaten zu organisieren.
Auch die Gewichte der Netze werden als Tensoren dargestellt.

# Keras
Eine Python Library mit der Neuronale Netzte erstellt und trainiert werden können.
In den Präsentationsfolien wird beschrieben wie man die Netze konstruiert und welche Parameter wann gesetzt werden sollten.
Beispielsweise sollte in einem Netz zur Klassifikation in mehrere Kategorien "Softmax" als [Aktivierungsfunktion](07%20Neural%20Nets.md#Aktivierungsfunktion) verwendet werden. So werden die Ausgaben normiert und geben eine Art [Wahrscheinlichkeit](Einführung.md) an.

Ebenfalls wird beschrieben wie die Berechnung durch Einsatz von GPUs oder Google-Cloud-Rechenleistung beschleunigt werden kann.

