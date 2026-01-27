# Subtrees

> [!Summary] Einsatz
> Erlaubt es, eigenständige Repositories als Unterordner in einem anderen Repo zu speichern und zu verwalten.
> 
> Beispiel:
> Verwaltung der T3000 Dokumentation als eigenständiges Repository und Speichern des gesamten Projekts (Quellcode + Dokumentation) in einem Firmen-Repo

## Setup
1. Erstellung des Unter-Repo (Remote + Befüllen mit Inhalt)
2. Erstellung des Main-Repo
3. `cd Main-Repo`
4. `git subtree add --prefix <sub-Dir-Name> <sub-Repo-URL> <sub-Repo-Branch> --squash`

Der Name des Unterordners nach `--prefix` bestimmt, wohin der Inhalt des Unter-Repos gespeichert wird.
Der Branch des Unter-Repos bestimmt welcher Stand eingefügt werden soll. Für alle aktuellen Daten ist der Wert meist `main` oder `master`.
Die Option `--squash` sorgt dafür, dass nicht die gesamte Historie des Unter-Repos mit eingebunden wird. Mit diesem Flag werden nur die Dateien in ihrem aktuellen Zustand übertragen.

## Updates
### Pull
Wenn neue Änderungen aus dem Unter-Repo verwendet werden sollen, muss ein Befehl ausgeführt werden, der sehr ähnlich ist wie beim [Setup](#Setup).
1. `cd Main-Repo`
2. `git subtree pull --prefix <sub-Dir-Name> <sub-Repo-URL> <sub-Repo-Branch> --squash`

Es wird der Befehl `add` durch `pull` ersetzt, die Parameter und ihre Bedeutung bleiben unverändert.

### Push
Änderungen werden standartmäßig nur im Main-Repo getrackt. Wenn ein aktualisierter Stand auch ins Unter-Repo gepusht werden soll, muss dies explizit geschehen.
1. `cd Main-Repo`
2. `git subtree push --prefix <sub-Dir-Name> <sub-Repo-URL> <sub-Repo-Branch>`

`Add` wird durch `push` ersetzt, die Option `--squash` entfällt. 
Die entsprechenden Änderungen werden (zusammen mit ihren Commit-Nachrichten als Liste aus Commits?) aktualisiert
