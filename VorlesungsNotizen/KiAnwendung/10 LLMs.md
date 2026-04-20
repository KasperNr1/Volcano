Wie auch einfache N-Gramm Modelle werden bei Large Language Models Wahrscheinlichkeiten an Wortsequenzen zugewiesen. Unterschied ist das Training. Bei LLMs wird mit Maskierung gearbeitet um ein Folgewort einer Sequenz vorherzusagen. Bei N-Grammen wird nur mit den Häufigkeitswerten gearbeitet.
Obwohl  nur trainiert wird einzelne Worte vorherzusagen, wird nützliches Sprachwissen erworben.

# Architekturen
![](LlmArchitekturen.png)

## Encoder only
Diese Architektur ist besonders gut geeignet für Aufgaben bei denen keine großen Sequenzen generiert werden müssen. Für Klassifikationsaufgaben ist die Fähigkeit nützlich, große Texte umfassend zu analysieren und zu verstehen.

## Encoder-Decoder
Besteht aus einem [Encoder](#Encoder%20only) und einem Decoder. Eignet sich für Aufgaben bei denen Inputsequenzen in Ausgabesequenzen umgewandelt werden müssen. Beispielsweise in der maschinellen Übersetzung sind diese Modelle beliebt.

Da sie sehr ressourcenintensiv sind, ist es für kleinere Ideen sinnvoll sparsamere Modell zu verwenden.

## Decoder Only
Modelle wie GPT oder auch "Left-To-Right LLMs" oder "Autoregressive LLMs" generieren Text von 'links' nach 'rechts'. Es wird stets die aktuelle Sequenz vervollständigt.

Auch solche Sequenzgenerierungsmodelle können für Klassifikationsaufgaben verwendet werden. Dazu wird die Wahrscheinlichkeit der verschiedenen Optionen verglichen.
![](LlmForClassifikation.png)

### Sampling
Beim Sampling wird zur Erstellung natürlicherer Texte ein Teil der Ausgabetokens zufällig gewählt. Es wird nicht das wahrscheinlichste Wort gewählt sondern eine seltenere Fortsetzung der Sequenz gewählt.
So kann die Ausgabe vielfältiger und lebendiger wirken, opfert aber eventuell Genauigkeit der Ergebnisse.

#### Top-k Sampling
Es wird die Liste der Top $k$ wahrscheinlichsten Worten in eine engere Auswahl genommen. Mit nach einer Normierung der Wahrscheinlichkeiten wird eine gültige Verteilung erreicht, die aber Unterschiede in den Wahrscheinlichkeiten beibehält.

#### Top-p Sampling
Statt einer festen Anzahl Wörter wie bei [Top-k Sampling](#Top-k%20Sampling) soll eine dynamische Zahl Wörter verwendet werden, sodass eine feste Menge der Gesamtwahrscheinlichkeit enthalten ist.

Für eine Verteilung $P(w_t \mid w_{<t})$ ist das Top-p-Vokabular $V(p)$ die kleinste Menge von Wörtern mit 
$$
\sum_{w \in V(p)} P(w \mid w_{<t} \geq p)
$$
#### Temperature Sampling
Statt die Verteilung abzuschneiden wird sie hier umgeformt. Beim Sampling mit 'niedriger' Temperatur $(\tau \leq 1)$ wird die Wahrscheinlichkeit der wahrscheinlichsten Wörter erhöht, während die der seltenen Wörter verringert wird. 

Statt $\text{softmax}(u)$ wird $\text{softmax}\left(\dfrac{u}{\tau}\right)$ berechnet.

> [!Missing] Fehlt
> Seite 585-586

# Pretraining
Zentrale Idee ist das Training in zwei Stufen. Im ersten Schritt werden auf breiter Datenbasis allgemeine Muster und Sprachverständnis erlernt. In einem [zweiten Training](#Finetuning) wird das Modell speziell auf eine Aufgabe vorbereitet.

Es wird erlernt wie semantische Beziehungen in Sprachen funktionieren. Dabei wird auch der Wortschatz des Modells entwickelt.
Kontextuelle Nuancen wie die Ähnlichkeit von 'kalt' und 'eisig' können erlernt werden, wenn die Begriffe oft genug im selben Kontext gesehen werden.
Faktenwissen wie Autorenschaft oder kulturelle Referenzen werden erfasst.
Mathematische und logische Zusammenhänge werden grundlegend erlernt, wobei diese Beziehungen deutliche Schwierigkeiten bei komplexen Aufgaben haben können.


> [!Info] How-To-Mathe
> Wenn Chatbots Berechnungen durchführen sollen, so generieren sie teilweise Pythonprogramme. Diese Programme können die Berechnung ausführen und liefern die Ergebnisse an das Sprachmodell.

## Teacher Forcing
An jeder Position $t$ sind die korrekten Tokens $w_{1:t}$ bekannt. Es wird der loss ($- \log \text{Wahrscheinlichkeit})$ für das nächste Token $w_{t+1}$ berechnet. Nach jeder Vorhersage wird das generierte Token bewertet und verworfen. Nur das bekannte korrekte Token wird angehängt und fortgefahren.

## Quellen 
Große Textsammlungen wie Wikipedia und StackExchange, verschiedene Bücher und wissenschaftliche Publikationen sind in 'The Pile' zusammengefasst. Dieser Datensatz bildet ein breites Spektrum von Themen und Sprachstilen ab.

Dabei ist es wichtig Duplikate zu entfernen und anstößige Inhalte zu filtern. Herausforderung ist der Umgang mit Dialekten, verschiedene Ausdrücke könnten in einem Dialekt verfasst sein und fälschlicherweise als problematischer Inhalt erkannt werden.

# Finetuning
Fine-tuning hat vier verschiedene Bedeutungen. Dabei wird in allen Fällen ein Teil der Parameter an neue Daten angepasst werden.

## Fortgesetztes Pretraining
Alle Parameter des Modells werden mit neuen Daten weiter trainiert.
Unter Verwendung derselben Lossfunktion und Methodik wie im [Pretraining](#Pretraining) wird so gehandelt, als ob der ursprüngliche Datensatz erweitert wurde.

## Parametereffizientes Finetuning (PEFT)
Es werden aufgrund der großen Menge an Parametern nur ein Teil der Gewichte weiter Trainiert. Alle anderen werden 'eingefroren' und beibehalten.

## Low Rank Adaptation LoRA
Sei $W$ eine Matrix der Form $[N \times d]$  die aktualisiert werden muss. Diese wird in zwei Matrizen $A [N \times r]$ und $B [r \times d]$ zerlegt. Da $r$ gewählt wurde um klein zu sein (z.B. 1 oder 2) ist die Berechnung der Optimierung deutlich schneller. 
Der Effekt wird durch das spätere Zusammenführen auf mehrere Gewichte angewendet. So ist das Training weniger präzise, aber deutlich schneller.

# Bewertung von LLMs
## Perplexität
Misst wie 'verwirrt' das Modell ist, wenn es versucht, den nächsten Teil des Textes vorherzusagen. Bei niedrigen Werten ist das Modell in der Lage Vorhersagen zu machen, die sinnvoll sind und gut zueinander passen.
Hohe Werte zeigen, dass der Text für das Modell unverständlich ist. 

Da die Perplexität sensibel gegenüber Länge von Eingaben und Tokens ist, funktioniert sie am besten wenn ähnliche Modelle verwendet werden.

## Andere Faktoren
- Größe: Die verwendete Menge an Speicherplatz und GPU Verbrauch
- Energieverbrauch: Kann in kWh gemessen werden, oder in ausgestoßenem CO2
- Fairness: Prüft das Vorhandensein von Stereotypen


# Skalierung
Die Leistung von großen Modellen hängt von ihrer Größe ab. Mit mehr Parametern und größeren Trainingsdatensätzen steigt die Qualität der Modelle. 


> [!Info] LLM Overfitting
> Die Grenze zum Overfitting ist noch nicht erreicht. Aufgrund der hohen Kosten wird typischerweise das Training bereits beendet, wenn eine Konvergenz annähernd erreicht ist.

