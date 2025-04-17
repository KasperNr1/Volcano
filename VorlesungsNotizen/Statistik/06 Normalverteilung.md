# 4.3 Die Gaus'sche  Normalverteilung
Zahlreiche Zufallsvariablen in Naturwissenschaft und Technik, wie z.B. physikalisch-technische Messgrößen genügen einer stetigen Verteilung mit Dichtefunktion.

Definition:
Die Verteilung einer stetigen Zufallsvariablen $X$ mit der Dichtefunktion 
$$
f(x)=\frac{1}{\sigma \sqrt{2\pi}}*e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}
$$  
und der Verteilungsfunktion $F(x)$
$$
F(x) = \frac{1}{\sigma \sqrt{2\pi}} \int_{-\infty}^{x} e^{-\frac{1}{2}\left(\frac{t-\mu}{\sigma}\right)^2} \, dt
$$
heißt Gauß'sche Normalverteilung mit den Parametern $\mu$ und $\sigma$.
Man kann zeigen:
$$
\begin{array}{ll}
E(X) &= \mu \\
Var(X) &= \sigma^2
\end{array}
$$
Man schreibt: $X \sim N(\mu; \sigma)$

```handdrawn-ink
{
	"versionAtEmbed": "0.3.4",
	"filepath": "VorlesungsNotizen/Statistik/attachments/Ink/Drawing/2025.4.17 - 13.25pm.drawing",
	"width": 500,
	"aspectRatio": 1
}
```
Maximum bei $x=\mu$ und Wendestellen bei $x=\mu \pm \sigma$ 

Eigenschaften der Dichtefunktion:
- Die Dichtefunktion ist symmetrisch zur Geraden $x=\mu$ 
- $f(x)$ ist normiert, d.h. die Fläche zwischen Dichtefunktion und $x$-Achse hat den Wert $1$ 
- Die Gestalt der Dichtefunktion $f(x)$ erinnert an eine Glocke.


> [!Info] Form der Kurve
> Der Parameter $\mu$ legt die Position des Maximums fest.
> $\sigma$ bestimmt die horizontale Streckung. Aufgrund der Normierung ist er damit auch für die Höhe der Kurve verantwortlich. Eine kleine Standardabweichung hat eine höhere, schmalere Kurve zur Folge.

# Die Standardnormalverteilung
Die im vorausgegangenen Abschnitt behandelte allgemeine Gauß'sche Normalverteilung mit den Parametern $\mu$ und $\sigma$ lässt sich stets auf die Standardnormalverteilung mit den Parameterwerten $\mu = 0$ und $\sigma = 1$ zurückführen.

$X \sim N(\mu; \sigma)$

Standardtransformation
$$
u = \frac{x-\mu}{\sigma} \sim N(0;1)
$$

Dichtefunktion:
$$
\varphi(u) = \frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2}u^2}
$$

```handdrawn-ink
{
	"versionAtEmbed": "0.3.4",
	"filepath": "VorlesungsNotizen/Statistik/attachments/Ink/Drawing/2025.4.17 - 13.42pm.drawing",
	"width": 1000,
	"aspectRatio": 1.9646365422396856
}
```
Fläche = 1 (In Skizze)

Verteilungsfunktion:
$$
\Phi(u) = P(U\leq u) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{u}e^{-\frac{1}{2}t^2} \, dt
$$
Erläuterung zur tabellierten Verteilungsfunktion der Standardnormalverteilung:
- Integral ist unnötig schwer zu berechnen, Tabelle (moodle: Verteilungstabelle_Standardnormverteilung.pdf) wird in der Klausur gestellt
- Lesen: 
  Zeilen sind erste Kommastellen
  Spalten zur höheren Präzision weitere Nachkommastellen
-


```handdrawn-ink
{
	"versionAtEmbed": "0.3.4",
	"filepath": "VorlesungsNotizen/Statistik/attachments/Ink/Drawing/2025.4.17 - 13.51pm.drawing",
	"width": 870,
	"aspectRatio": 1.8087318087318087
}
```

Beispiel:
1.)
$\Phi(1,58) = 0.9429$
Tabelle ablesen: Reihe 1.5 - Spalte 8

2.)

```handdrawn-ink
{
	"versionAtEmbed": "0.3.4",
	"filepath": "VorlesungsNotizen/Statistik/attachments/Ink/Drawing/2025.4.17 - 13.54pm.drawing",
	"width": 1114,
	"aspectRatio": 2.411255411255411
}
```
$\Phi(-u) = 1-\Phi(u)$
Tabelle kann nur positive Zahlen, durch Symmetrie und Gegenereignis kann der Wert für negative Ergebnisse bestimmt werden

$\Phi(-1.25) = 1-\Phi(1.25) = 1-0.8944 = 0.1056$


> [!Warning] Tabelle nur bei Standardnormalverteilung
> Allgemeine Normalverteilung muss in Standardverteilung umgeformt werden um die Werte aus der Tabelle nutzen zu können

## Berechnung von Wahrscheinlichkeiten
### 1. $P(X\leq x)$
Sei $X \sim N(\mu; \sigma)$ 
$$
P(X \leq x) = F(x) = \frac{1}{\sigma \sqrt{2\pi}}\int_{-\infty}^{x}e^{-\frac{1}{2}\left(\frac{t-\mu}{\sigma}\right)^2} \, dt
$$

```handdrawn-ink
{
	"versionAtEmbed": "0.3.4",
	"filepath": "VorlesungsNotizen/Statistik/attachments/Ink/Drawing/2025.4.17 - 14.05pm.drawing",
	"width": 500,
	"aspectRatio": 1
}
```

Substitution:
$$
u = \frac{t-\mu}{\sigma} \qquad \frac{du}{dt}=\frac{1}{\sigma}\longrightarrow dt = \sigma \cdot du
$$

Untere Grenze:
$$
t \to -\infty \quad \Longrightarrow \quad u \rightarrow -\infty
$$
Obere Grenze:
$$
t = x \quad \Longrightarrow \quad u \rightarrow \frac{x-\mu}{\sigma}
$$

Daher gilt:
$$
\begin{array}{ll}
F(x) &= \displaystyle
\frac{1}{\sigma \sqrt{2\pi}} \int_{-\infty}^{x} e^{-\frac{1}{2}\left(\frac{t-\mu}{\sigma}\right)^2} \, dt \\ 
&= \displaystyle
\frac{1}{\sigma \sqrt{2\pi}} \int_{-\infty}^{\frac{x-\mu}{\sigma}} e^{-\frac{1}{2}u^2} \, dt \\
&= \displaystyle
\frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\frac{x-\mu}{\sigma}}e^{-\frac{1}{2}u^2} \\
&= \displaystyle
\Phi\left(\frac{x-\mu}{\sigma}\right)
\end{array}
$$


> [!Info] Umformung
> $$
> P(X\leq x) = F(x) = \Phi\left(\frac{x-\mu}{\sigma}\right)
> $$

Beispiel:
Sei $X \sim N(6;2)$ 

```handdrawn-ink
{
	"versionAtEmbed": "0.3.4",
	"filepath": "VorlesungsNotizen/Statistik/attachments/Ink/Drawing/2025.4.17 - 14.50pm.drawing",
	"width": 500,
	"aspectRatio": 1
}
```

$$
P(X \leq 10.42) = F(10.42) = \Phi\left( \frac{10.42 - 6}{2} \right) = \Phi(2.21) = 0.9864
$$

### 2. $P(X \geq x)$
Sei $X \sim N(\mu; \sigma)$

```handdrawn-ink
{
	"versionAtEmbed": "0.3.4",
	"filepath": "VorlesungsNotizen/Statistik/attachments/Ink/Drawing/2025.4.17 - 14.57pm.drawing",
	"width": 736,
	"aspectRatio": 1.576017130620985
}
```
$P(X \geq x) = 1-P(X \leq x)$

Also gilt allgemein $P(X \geq x) = 1 - \Phi\left(\frac{x-\mu}{\sigma}\right)$

### 3: $P(a \leq X \leq b)$
$X \sim N(\mu; \sigma)$

```handdrawn-ink
{
	"versionAtEmbed": "0.3.4",
	"filepath": "VorlesungsNotizen/Statistik/attachments/Ink/Drawing/2025.4.17 - 15.02pm.drawing",
	"width": 500,
	"aspectRatio": 1
}
```
$$
P(a \leq X \leq b) = P(X \leq b) - P(X \leq a)
$$
Beispiel
Sei $X \sim N(2; 6)$

```handdrawn-ink
{
	"versionAtEmbed": "0.3.4",
	"filepath": "VorlesungsNotizen/Statistik/attachments/Ink/Drawing/2025.4.17 - 15.05pm.drawing",
	"width": 646,
	"aspectRatio": 1.5528846153846154
}
```
$$
P(0 \leq X \leq 1) = \Phi\left(-\frac{1}{6}\right) - \Phi\left(\frac{1}{3}\right) = 0.0618
$$