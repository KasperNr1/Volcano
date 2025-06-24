# Vorlage
Für größere Arbeiten wie die [T2000](T2000.md) liegt eine Vorlage unter 
`C:\Users\dh10mbo\OneDrive - Durr Group\Documents\LaTeX`
und bei [Github](https://www.github.com). 

## Verwendung
Das Projekt kann nicht direkt mit `pdflatex main.tex` compiliert werden, für Glossar und Literaturverzeichnis ist weitere Vorbereitung notwendig.

Das Gesamte Dokument wird durch 6 Befehle vollständig generiert.
``` Terminal
pdflatex main           // Wird Sauer sein wegen fehlender Einträge
						// Mit "CTRL + C" Fehlermeldungen skippen

makeglossaries main     // Glossar generieren

pdflatex main           // Mit korrektem Glossar kann Hilfsdatei für Biber 
						// erstellt werden

biber main              // Biblatex Datei verarbeiten

pdflatex main           // Literaturverweise verwenden

pdflatex main           // Zweiter Durchlauf um Seitenzahlen zu korrigieren
```
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

In der Präambel muss das Glossar etwas vorbereitet werden:
``` Latex
% Glossar
\usepackage[nonumberlist,toc]{glossaries}
\makeglossaries
\input{ads/glossaries.tex}
\glsaddall
```


In `main.tex` wird es über einen $\LaTeX$ Befehl eingebunden.
`\printglossary[style=altlist,title=Glossar]`

### Literaturverzeichnis
Im Hauptdokument wird das Literaturverzeichnis mit dem Befehl `\printbibliography` eingefügt.
In der Präambel müssen dafür Konfigurationen gesetzt werden. Die Vorlage verwendet diese:
```
% Literaturverweise
\usepackage[
    backend=biber,      % empfohlen. Falls biber Probleme macht: bibtex
    bibwarn=true,
    bibencoding=utf8,   % wenn .bib in utf8, sonst ascii
    sortlocale=de-DE,
    style=\zitierstil,  % ist eine Variable mit Wert: "alphabetic"
]{biblatex}
\addbibresource{bibliographie.bib}
```

### Bibliographie
Die Quellen selbst stehen in einem Biblatex File mit folgendem Format:

``` Biblatex
@book{martin_clean_nodate,
    title = {Clean Code},
    isbn = {978-0-13-235088-4},
    series = {Robert C. Martin Series},
    author = {Martin, Robert C.},
}

@online{authorlastname_how_2012,
    title = {How to quit {VIM}},
    rights = {No Rights},
    url = {https://stackoverflow.com/questions/11828270/how-do-i-exit-vim},
    shorttitle = {Short Title},
    abstract = {Tells the guy to type :q},
    titleaddon = {{StackOverflow}},
    author = {{AuthorLastName}, {AuthorFirstname}},
    urldate = {2000-01-01},
    date = {2012-04-20},
}
```

Zotero kann eine Sammlung in diesem Format exportieren.
`Datei / Ordner wählen -> Rechtsklick -> Exportieren`
