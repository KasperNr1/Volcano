# Vorlage
Für größere Arbeiten wie die [T2000](T2000.md) liegt eine Vorlage unter 
`C:\Users\dh10mbo\OneDrive - Durr Group\Documents\LaTeX`
und bei [Github](https://www.github.com). 

## Verwendung
Das Projekt kann nicht direkt mit `pdflatex main.tex` compiliert werden, für Glossar und Literaturverzeichnis ist weitere Vorbereitung notwendig.

### Glossar
Die Glossar-Datei entspricht folgendem Format:

`fileName: glossar.tex`
``` LaTeX
\newsglossaryentry{Template}
{
    name=Template,
    description={Ein Template ist eine Vorlage}
}
```


> [!tip] Glossar compilieren
> Aufruf von `makeglossaries {filename}`
> Wobei filename der Name des Main Files ist (ohne Extension)
> 
> Für das Glossar des Dokuments in `documentation.tex` wird also
> `makeglossaries documentation`
> aufgerufen


In `main.tex` wird es über einen $\LaTeX$ Befehl eingebunden.
`\printglossary[style=altlist,title=Glossar]`

### Literaturverzeichnis
