# NPM
Der [Node Package Manager]([npm | Home](https://www.npmjs.com/)) kann nicht verwendet werden. Um die Verwendung gefährlicher Pakete auszuschließen wird ein Homag-eigener Proxy genutzt.

Unter [https://nexus.durr.com/](https://nexus.durr.com/ "https://nexus.durr.com/") kann im Menü "Browse" eine Liste von Repositories angezeigt werden. (Eventuell muss man sich zuerst einloggen, das funktioniert im Login Menü oben rechts über SingleSignOn)

![](NexusBrowse.png)

Unter `homag.npm-proxy` ist ein Link zu finden der als Paketquelle referenziert werden kann.

``` Terminal
npm config set registry https://nexus.durr.com/repository/homag.npm-proxy/
```

Mit einem weiteren Befehl kann man sich authentifizieren
``` Terminal
npm config set //nexus.durr.com/repository/homag.npm-proxy/:_auth <BASE64_CREDENTIALS>
```

![](NexusUserToken.png)

Im Menü findet sich eine Reihe von Tokens, etwas weiter unten auch die Base64 Variante die hier gebraucht wird.
