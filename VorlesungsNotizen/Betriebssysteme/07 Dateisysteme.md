Neben den klassischen Dateisystemen gibt es auch solche, die speziell auf einer Implementierung in [Verteilten Systemen](Verteilte%20Systeme.md) basieren.

# Verteilte Dateisysteme
Ziel ist das gemeinsame Nutzen von Dateien im Netz. Dabei gibt es verschiedene Anforderungen die für den korrekten Betrieb notwendig sind.
- [Verschiedene Transparenzen](../../Architektur/Verteilte%20Systeme.md#Transparenz)
- Konsistenz & Nebenläufigkeit um gleichzeitige Updates zu behandeln
- Replikation und Caching um Latenz und Verfügbarkeit zu verbessern
- Unterstützung verschiedener Betriebssysteme

## Flat File Service
Bietet idempotente Operationen auf Dateien an.
- `read`
- `write`
- `create`
- `move`
- `get / set attributes`

Dateien werden durch UFIDs (Unique File IDs) eindeutig markiert.
Ein Directory Service kann Dateinamen oder Pfade in diese UFIDs übersetzen.

## NFS
![](ArchitekturNfs.png)

Wurde 1984 von SUN eingeführt und arbeitet plattformübergreifend. Die Server sind zustandslos und prüfen daher Zugriffsrechte bei jeder Anfrage neu. Dadurch wurden Spoofing Angriffe möglich.

Über Erweiterungen wie Firewalls, Mount-Optionen und kryptographischer Authentifizierung wird das System sicher. Diese werden ab NFSv4 unterstützt.

Um Anfragen zu beschleunigen wird mit einem Cache gearbeitet, Cache auf Clientseite muss regelmäßig überprüft werden, um nicht mit veralteten Daten zu arbeiten.
Auf Serverseite werden Änderungen teilweise erst im Cache geschrieben, bei einem Ausfall gehen diese jedoch verloren. Ein Write-Trough schreibt direkt auf die Disk, ist jedoch langsamer.

NFS garantiert keine strikte Konsistenz des Client Caches, Anwendungen müssen diese Problematiken selbst erwarten und behandeln.

# Verteilter Shared Memory
Ziel ist die Bereitstellung eines gemeinsamen Speichers über mehrere Knoten hinweg.
Grundtechnik ist die seitengesteuerte (Page based) Speicherverwaltung pro Knoten.

![](DifferentStorageLocations.png)
![](DifferentStorageLocationsExplanation.png)

Der verteilte Speicher kann Byte- oder Objektorientiert sein. 

Um Konsistenz zu wahren wird meist ein 'local write' verwendet. Die beschreibbare Page wird zur schreibenden Instanz migriert. Um zu lesen wird eine Kopie der Daten angefordert.

Die Verwaltung der beschreibbaren Seite wird von ihrem 'Owner' verwaltet. Dazu kann ein Zentraler Manager die Rolle übernehmen oder eine feste Verteilung benutzt werden. Auch Multicasts sind möglich, so wird der Manager ersetzt.
Dynamische Strategien sind möglich, bei der Prozesse einen vermuteten Owner kennen und die Anfragen im Fehlerfall weitergeleitet werden.


> [!Info] Forschung
> Die Thematik ist eher in der Forschung angesiedelt, Shared Memory wird aktuell in keiner größeren Anwendung produktiv eingesetzt
