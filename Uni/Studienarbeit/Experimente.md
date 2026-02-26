# Handschuhmodus
Entwickelt wird eine Einstellungsseite in der verschiedene Eigenschaften des UI zentral festgelegt werden können.
Dabei soll beispielsweise auch die Größe von Schaltflächen für den Gebrauch mit Handschuhen angepasst werden.
Eine weitere Idee ist die Auswahl eines alternativen Farbschemas um Kontraste zu erhöhen und auch bei schlechter Sicht (bei Schnee und Wind) in der Benutzung zu unterstützen.

> [!Info] Ziel
> Ziel ist die Bedienbarkeit auch bei schlechten Bedingungen zu gewährleisten
> - Benutzung mit Handschuhen
> - Fehlendes Feingefühl bei Kälte

## Kommunikation in der App
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

## Smarte Modifier
Ziel war es, einen Modifier `foo` zu erstellen, sodass `Button.foo` im Normalen Modus regulär aussieht und im Glovemode eine alternative Darstellung erhält.

Modifier können selbst definiert werden und auch Logik enthalten um bestimmte Formatierungen nur bedingt anzuwenden.
``` Swift
private struct ThemeButtonSizing : ViewModifier {
	@Environment(Theme.self) private var theme // lädt die Umgebungsvariable
	
	func body(content: Content) -> some View{
		switch theme.buttonSizeMode {
		case .normal:
			content.controlSize(baseline)
		case .glove:
			content.controlSize(.extraLarge)
		}
	}
}
```

Diese Funktion ist ein Wrapper um den selbst definierten Modifikator mit der `.notation`  erreichbar zu machen.
``` Swift
public extension View {
	func themedButtonSize(baseline: ControlSize) -> some View {
		modifier(ThemeButtonSizing(baseline: baseline))
	}
}
```


# Buttons
## Controll-Sizes
[Swift stellt 5 unterschiedliche Größen bereit](https://developer.apple.com/documentation/appkit/nscontrol/controlsize-swift.enum), jedoch werden bei der Anwendung auf IOS Buttons nur drei verschiedene Varianten tatsächlich angezeigt.

![](IosButtonSizes.png)

## Whitespace
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

## Padding
Der Parameter setzt einen Abstand um den äußeren Rand des Elements
``` Swift
 Button {...}
	.buttonStyle(.borderedProminent)
	.controlSize(.regular)
 Button {...}
	.buttonStyle(.borderedProminent)
	.controlSize(.large)
	.padding(50)
Button {...}
	.buttonStyle(.borderedProminent)
	.controlSize(.extraLarge)
	.padding(.vertical, 50)
```

![](PaddedButtons.png)