# Snippets
Sind die Vorschläge die beim Tippen gegeben werden. Sie sind ein mächtiges Tool das auch über komplexere Features als nur benutzerdefinierte Vervollständigungen bieten.

[Snippets in Visual Studio Code](https://code.visualstudio.com/docs/editing/userdefinedsnippets)


# Extensions
## Veröffentlichung
Extensions können direkt auf den öffentlichen Marketplace hochgeladen werden oder als Pakete offline verteilt werden.
[Die Dokumentation](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) beschreibt detailliert wie die einzelnen Schritte zu durchlaufen sind, jedoch ist der Weg nicht besonders lang.

Mit dem Tool `vsce` kann die Verteilung von VSC Extensions verarbeitet werden. 
Es kann über NPM installiert werden.

``` Terminal
npm install -g @vscode/vsce
```
### Packaging
Kompiliert eine Extension in eine einzelne `.vsix` Datei die manuell verteilt und installiert werden kann.

Um eine Extension zu verpacken muss in ihrem Root-Verzeichnis nur ein einzelner Befehl ausgeführt werden.

``` Terminal
vsce package
```

### Publishing
Es muss ein PAT und ein Publisher erstellt werden. 
Das PAT kann wie [hier beschrieben](https://code.visualstudio.com/api/working-with-extensions/publishing-extension#publishing-extensions) in wenigen Schritten erstellt werden und wird verwendet um sich bei `vsce` zu authentifizieren.

Der Publisher wird auf der Seite der Extension angezeigt.

![](VscePublisher.png)

Als Publisher muss man sich [erst registrieren](https://code.visualstudio.com/api/working-with-extensions/publishing-extension#publishing-extensions) und anschließend den verwendeten Name in der `package.json` Datei der Extension eintragen.

``` JSON filename="package.json"
{
	"name" : "example-name",
	"publisher" : "myPublisherName",
	"description" : "good Description"
}
```

Nachdem die Datei korrekt ausgefüllt ist kann man sich mit 

``` Terminal
vsce login
```

erst authentifizieren und die Extension anschließend mit 

``` Terminal
vsce publish
```

veröffentlichen