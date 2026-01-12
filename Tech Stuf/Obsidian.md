# Plugins
## DH-Mac
- Ink
- Slash Commander
- [Zotero Integration](obsidian://show-plugin?id=obsidian-zotero-desktop-connector)
- Pandoc
- Pandoc Reference List

## Laptop
- Code Styler
- Ink
- Slash Commander
- Webpage HTML Export

## Mobile
- Git
- Ink


# Mermaid
Eine Bibliothek die es erlaub Diagramme durch textuelle Beschreibungen zu erstellen und in Markdown einzufügen.

[Mermaid | Diagramming and charting tool](https://mermaid.js.org/)

Neben simplen Pie-Charts sind auch Klassen-/Sequenzdiagramme unterstützt


```mermaid
---
config:
  pie:
    textPosition: 0.5
  themeVariables:
    pieOuterStrokeWidth: "5px"
---
pie showData
    title Key elements in Product X
    "Calcium" : 42.96
    "Potassium" : 50.05
    "Magnesium" : 10.01
    "Iron" :  5
```
Auch seltenere Diagrammtypen wie `GitGraph` sind enthalten
```mermaid
---
config:
  logLevel: 'debug'
  theme: 'base'
  gitGraph:
    showBranches: false
---
      gitGraph
        commit
        branch hotfix
        checkout hotfix
        commit
        branch develop
        checkout develop
        commit id:"ash" tag:"abc"
        branch featureB
        checkout featureB
        commit type:HIGHLIGHT
        checkout main
        checkout hotfix
        commit type:NORMAL
        checkout develop
        commit type:REVERSE
        checkout featureB
        commit
        checkout main
        merge hotfix
        checkout featureB
        commit
        checkout develop
        branch featureA
        commit
        checkout develop
        merge hotfix
        checkout featureA
        commit
        checkout featureB
        commit
        checkout develop
        merge featureA
        branch release
        checkout release
        commit
        checkout main
        commit
        checkout release
        merge main
        checkout develop
        merge release

```


# Committing on Mobile
## Cloning the Repo
### Android
Termux App installieren
Zugriff auf Dateisystem über:
``` Shell
termux-setup-storage
```
Durch CommandLine Repo Klonen, in Obsidian App das geklonte Verzeichnis auswählen.

## Git Plugin
Als Passwort wird ein PAT für das Repo verwendet.
Erstellung: 

## Directory
cd "/data/data/com.termux/files/home/storage/documents/Obsidian Vaults/Volcano"

## Git
Add, commit und Push durch Termux.