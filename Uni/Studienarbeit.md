# Meeting
## Schriftliche Ausarbeitung
- Viele Bilder
- Seitenzahl quasi egal
- Als Doku für Nachfolger
- Chat ist erlaubt, Kontrollieren. Verweis in der Eigenständigkeitserklärung
- Wissenschaftlichkeit primär im Kerngebiet 

# Ideen
- Sprachauswahl
- Dark Mode
- Custom Farben
- Menüleiste weniger eng (Lieber wie bei Apple News)
- 4 Felder bei EHB wenig intuitiv (Bewertung in Algo ist nicht Linear?)
  lieber Slider (Mit diskreten Werten wie Maus-Sensi?)

# Themen
- ⁠Einzelhangbewertung für IOS (Siemens)
- Automatische Einarbeitung in Lawinenbericht
- Handschuhbedienbarkeit
- Icon Erstellung
- ⁠Funktionen der Android App übernehmen
- ⁠Bedienvideo / Bedienertutorial
- CI / CD Pipline



# Notizen
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


TODO
Zu vergrößernde App-Elemente auswählen und Optionen zur Vergrößerung von Schaltflächen vergleichena
