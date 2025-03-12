Eine Variable kann sich nur in einem der Zustände $0$ oder $1$ befinden. Es gibt keine Zwischenschritte oder sonstigen Werte.
Durch diese starke Einschränkung lässt sich dieses System sehr gut auf elektrische Schaltungen übertragen.
Auch die [Menge](Intervalle%20und%20Mengen.md) an verfügbaren Operationen ist entsprechend kleiner.

# Verknüpfungen
Die Zeichnungen wurden mit folgendem Latex-Code generiert:
```
\documentclass{standalone}
\usepackage{circuitikz}

\begin{document}
	\begin{circuitikz}
		\node[european xnor port] {};
	\end{circuitikz}
\end{document}
```
Und anschließend mit einem Python Skript zu als Bilder gerendert.
```
import os
import fitz  # PyMuPDF

def convert_pdfs_to_images(directory, zoom=2.0):
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            file_path = os.path.join(directory, filename)
            pdf_document = fitz.open(file_path)
            for page_number in range(pdf_document.page_count):
                page = pdf_document.load_page(page_number)
                zoom_matrix = fitz.Matrix(zoom, zoom)
                pix = page.get_pixmap(matrix=zoom_matrix)
                image_filename = f"{os.path.splitext(filename)[0]}_page{page_number + 1}.png"
                image_path = os.path.join(directory, image_filename)
                pix.save(image_path)
                print(f"Saved {image_path}")

directory = os.getcwd()
convert_pdfs_to_images(directory, zoom=20.0)
```
## AND
Schreibweise: $Y = A \wedge B$ 
Resultiert nur in $1$ wenn beide Eingänge mit $1$ belegt sind. 
![](AndGate.png)

| A   | B   | $A\wedge B$ |
| --- | --- | ----------- |
| 0   | 0   | 0           |
| 0   | 1   | 0           |
| 1   | 0   | 0           |
| 1   | 1   | 1           |

## OR
Liefert $1$ wenn mindestens ein Wert $1$ ist
![](OrGate.png)

| A   | B   | $A \vee B$ |
| --- | --- | ---------- |
| 0   | 0   | 0          |
| 0   | 1   | 1          |
| 1   | 0   | 1          |
| 1   | 1   | 1          |

## NOT
Negiert die Eingabe
![](NotGate.png)

| A   | $\neg A$ |
| --- | -------- |
| 0   | 1        |
| 1   | 0        |

# Weitere Gatter
Durch Kombination von [UND](#AND), [ODER](#OR) und [NOT](#NOT) können alle logischen Aussagen abgebildet werden. Man spricht auch von einem vollständigen "Vollständigen Boolschen System"

Es gibt noch weitere Gatter. Diese erfüllen zwar keine bisher unmöglichen Funktionen, bieten aber den Vorteil, dass sie in einer Schaltung nicht als Kombination von kleineren Teilen gebaut werden müssen.
Außerdem ist es teilweise möglich, die Grundbausteine mit ihnen abzubilden. So erhält man ein vollständiges Boolsches System das nur eine Art von Gatter benötigt.

## NAND
Ist das direkte Gegenstück zu [AND](#AND). Die Ausgaben sind jeweils negiert, so dass immer das Gegenteil zu AND resultiert.
![](NandGate.png)

| A   | B   | OUT |
| --- | --- | --- |
| 0   | 0   | 1   |
| 0   | 1   | 1   |
| 1   | 0   | 1   |
| 1   | 1   | 0   |

Da mit diesem Baustein die Funktion des [NOT](#NOT) simuliert werden kann, ist das NAND alleine ausreichend um jegliche Schaltung zu [konstruieren](Erstellen%20und%20Umformen%20boolscher%20Ausdrücke.md#Gezielte%20Umformung)
Dies kann eventuell sogar mit weniger Gattern gelingen, als wenn man die Klassischen verwendet. In manchen Fällen ist es jedoch auch deutlich komplexer. Die Entscheidung zur Verwendung der Gatter kann also nicht allgemein getroffen werden.

## NOR
Ist das Gegenteil zu [OR](#OR).
![](NorGate.png)

| A   | B   | OUT |
| --- | --- | --- |
| 0   | 0   | 1   |
| 0   | 1   | 0   |
| 1   | 0   | 0   |
| 1   | 1   | 0   |

NOR ist wie [NAND](#NAND) ebenfalls vollständig.

## XOR
Das exklusive Oder gibt nur dann wahr aus, wenn exakt eine Eingabe wahr ist. 
![](XorGate.png)

| A   | B   | OUT |
| --- | --- | --- |
| 0   | 0   | 0   |
| 0   | 1   | 1   |
| 1   | 0   | 1   |
| 1   | 1   | 0   |

## XNOR
Ist das Gegenteil zu [XOR](#XOR)
Die Schaltung gibt also genau dann $1$ aus, wenn beide Eingaben übereinstimmen.
![](XNorGate.png)

| A   | B   | OUT |
| --- | --- | --- |
| 0   | 0   | 1   |
| 0   | 1   | 0   |
| 1   | 0   | 0   |
| 1   | 1   | 1   |

# Rechenregeln
- [UND](#AND) vor [ODER](#OR) 
- Klammern wie in der herkömmlichen Mathematik
- Kommutativgesetz
  $a \wedge b \wedge c = c \wedge a \wedge b$
  $a \vee b \vee c = c \vee a \vee b$
- Assoziativgesetz
  $a \wedge (b \wedge c) = (a \wedge b) \wedge c$
  $(a \vee b) \vee c = a \vee (b \vee c)$
- Distributivgesetz
  $a \vee (b \vee c) = a \vee b \vee a \vee c$ 
  $a \wedge (b \wedge c) = a \wedge b \wedge a \wedge c$ 
Bemerkenswert ist, dass das Distributivgesetz für beide Rechenoperationen gleichermaßen gilt.

## Schreibweise
Wie die Multiplikation ist bei Boolscher Algebra das UND implizit.
Die Aussagen $a \wedge b \vee c \wedge d$ und $abcd$ sind logisch identisch.

Ebenfalls gibt es mehrere Varianten um Negation darzustellen.
$\neg a = \overline{a}$ 
Sie kann durch Negationssymbol $\neg$ oder Überstrich gekennzeichnet sein.
Zu beachten ist, dass die beiden folgenden Ausdrücke ==NICHT== identisch sind
$$
\overline{a}\overline{b} \neq \overline{ab}
$$
Der Unterschied wird offensichtlich wenn man die implizierten UND-Verknüpfungen explizit schreibt.
$$
\overline{a} \wedge \overline{b} \neq \overline{a \wedge b}
$$

## Erweiterungsregeln
- $a = a \vee a = a \vee a \vee \dots \vee a$
- $a = a \wedge a = a \wedge a \wedge \dots \wedge a$
- $a \wedge \overline{a} = 0$ 
- $a \vee \overline{a} = 1$
- $a \wedge 0 = 0$
- $a \vee 0= a$
- $a \wedge 1= a$
- $a \vee 1= 1$
- $a = \overline{\overline{a}}$ 

## De-Morgansche Gesetze
Diese Regeln beschreiben den Zusammenhang [AND](#AND), [NOT](#NOT) und [OR](#OR).
Sie sind grundlegend um Schaltungen gezielt nach einer Bestimmten [Verknüpfungen umzuformen](Erstellen%20und%20Umformen%20boolscher%20Ausdrücke.md#Gezielte%20Umformung) 

$$
\begin{array}{l}
\overline{(A \vee B)} \Longleftrightarrow \overline{A} \wedge \overline{B} \\
\overline{(A \wedge B)} \Longleftrightarrow \overline{A} \vee \overline{B}
\end{array}
$$
# Anwendung
## 2 aus 3 Schaltung
3 Gäste sitzen an der Bar, der Wirt soll nächstes Bier bringen, wenn mindestens 2 der Gäste ein leeres Glas haben.

### Festlegung
4 Variablen $a;b;c;w$
$a;b;c$ als Eingabe, wobei eine $1$ bedeutet, dass das Glas leer ist.
$w$ als Ausgabe, wobei eine $1$ bedeutet, dass der Wirt die nächste Runde verteilen soll.

### Bestimmung Schaltung

| A   | B   | C   | W   |
| --- | --- | --- | --- |
| 0   | 0   | 0   | 0   |
| 0   | 0   | 1   | 0   |
| 0   | 1   | 0   | 0   |
| 0   | 1   | 1   | 1   |
| 1   | 0   | 0   | 0   |
| 1   | 0   | 1   | 1   |
| 1   | 1   | 0   | 1   |
| 1   | 1   | 1   | 1   |
Die Tabelle wird für jede Kombinationsmöglichkeit der Eingaben ausgefüllt. Anschließend kann man alle Belegungen die zu $1$ führen [disjunktiv](DigitaltechnischeBegriffe.md#Disjunktiv) vereinen.
Man erhält einen Ausdruck der exakt die Tabelle widerspiegelt.
Eventuell kann man diesen zusätzlich noch vereinfachen.

$$
\begin{array}{l}
w = \underline{abc} \vee \overline{a}bc \vee a\overline{b}c \vee ab\overline{c} \\
w = \underline{abc} \vee \overline{a}bc \vee \underline{abc} \vee a\overline{b}c \vee \underline{abc} \vee ab\overline{c} \\
w = ab \vee (c\overline{c}) \vee ac \vee (b\overline{b}) \vee bc \vee (a\overline{a}) \\
w = ab \vee ac \vee bc \\
\end{array}
$$

Die Unterstreichung soll hier darauf hinweisen, dass der Term vervielfacht wurde. Da [Rechenregeln](#Rechenregeln) und [Erweiterungsregeln](#Erweiterungsregeln) 1 gelten, ist die Umformung so erlaubt.

# Benannte Schaltungen (2 Eingaben)

| A   | B   | Y0  | Y1  | Y2  | Y3  | Y4  | Y5  | Y6  | Y7  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $0$ | $0$ | $0$ | $0$ | $0$ | $0$ | $0$ | $0$ | $0$ | $0$ |
| $0$ | $1$ | $0$ | $0$ | $0$ | $0$ | $1$ | $1$ | $1$ | $1$ |
| $1$ | $0$ | $0$ | $0$ | $1$ | $1$ | $0$ | $0$ | $1$ | $1$ |
| $1$ | $1$ | $0$ | $1$ | $0$ | $1$ | $0$ | $1$ | $0$ | $1$ |

| A   | B   | Y8  | Y9  | Y10 | Y11 | Y12 | Y13 | Y14 | Y15 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $0$ | $0$ | $1$ | $1$ | $1$ | $1$ | $1$ | $1$ | $1$ | $1$ |
| $0$ | $1$ | $0$ | $0$ | $0$ | $0$ | $1$ | $1$ | $1$ | $1$ |
| $1$ | $0$ | $0$ | $0$ | $1$ | $1$ | $0$ | $0$ | $1$ | $1$ |
| $1$ | $1$ | $0$ | $1$ | $0$ | $1$ | $0$ | $1$ | $0$ | $1$ |

| Y0  | Nullfunktion           | $=0$                                             |
| --- | ---------------------- | ------------------------------------------------ |
| Y1  | Und-Funktion           | $=a\wedge b$                                     |
| Y2  | Sperr-Und / Inhibition | $=a \wedge \overline{b}$                         |
| Y3  | Identität              | $=a$                                             |
| Y4  | Sperr-Und / Inhibition | $= \overline{a} \wedge b$                        |
| Y5  | Identität              | $=b$                                             |
| Y6  | Antivalenz / XOR       | $=a\neq b; \quad(a\vee b)\wedge \overline{(ab)}$ |
| Y7  | Oder-Funktion          | $=a\vee b$                                       |
| Y8  | NOR-Funktion           | $=\overline{(a\vee b)}$                          |
| Y9  | Equivalenz             | $=ab \vee \overline{a}\overline{b}$              |
| Y10 | Negation               | $=\overline{b}$                                  |
| Y11 | Implikation            | $=a \vee \overline{b}$                           |
| Y12 | Negation               | $= \overline{a}$                                 |
| Y13 | Implikation            | $=\overline{a} \vee b$                           |
| Y14 | NAND-Funktion          | $=\overline{ab}$                                 |
| Y15 | Einsfunktion           | $=1$                                             |
