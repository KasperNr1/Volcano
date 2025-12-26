## Handschuhmodus
Entwickelt wird eine Einstellungsseite in der verschiedene Eigenschaften des UI zentral festgelegt werden können.
Dabei soll beispielsweise auch die Größe von Schaltflächen für den Gebrauch mit Handschuhen angepasst werden.
Eine weitere Idee ist die Auswahl eines alternativen Farbschemas um Kontraste zu erhöhen und auch bei schlechter Sicht (bei Schnee und Wind) in der Benutzung zu unterstützen.

> [!Info] Ziel
> Ziel ist die Bedienbarkeit auch bei schlechten Bedingungen zu gewährleisten
> - Benutzung mit Handschuhen
> - Fehlendes Feingefühl bei Kälte

Um die Einstellungen innerhalb der gesamten App zu erreichen wird eine Globale Instanz der `Theme`Klasse erstellt, die alle zu verwaltenden Einstellungen als Member enthält.

``` Swift
@main
struct Analyst_IOSApp: App {
    @State private var theme = Theme()
    
    var body: some Scene {
        WindowGroup {
            ContentView()
                .environment(theme)
        }
    }
}
```

In den inneren Elementen wird die Verbindung folgendermaßen hergestellt.

``` Swift
struct ContentView: View {
    @Environment(Theme.self) var theme
    
	var body : some View{
		theme.attributes // ist hier erreichbar
	    // ... 
    }
}
```


> [!Tip] Sichtbarkeit
> Da die Variable als Environment einer äußeren Schicht gesetzt wurde, ist sie in allen Unterelementen  erreichbar. Die Zeile
> `@Environment(Theme.self) var theme`
> Definiert die lokale Variable theme auf Basis der Umgebungsvariable vom Typ ´Theme´. Es kann nur eine Env-Variablen von jedem Datentyp exisitieren.



### Button Sizes
[Swift stellt 5 unterschiedliche Größen bereit](https://developer.apple.com/documentation/appkit/nscontrol/controlsize-swift.enum), jedoch werden bei der Anwendung auf IOS Buttons nur drei verschiedene Varianten tatsächlich angezeigt.

![](IosButtonSizes.png)

Durch hinzufügen von längeren Texten kann der Button noch größer angezeigt werden, auch von leeren Zeilen wird die Größe angepasst.

![](MegaButton.png)

``` Swift
Button {
	// Do smth with Button Press
} label: {
	Text("\n\nXtra button\n\n")
}
.buttonStyle(.borderedProminent)
.controlSize(.extraLarge)
```

