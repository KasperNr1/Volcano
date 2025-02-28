# Ableitung
Die Änderungsrate in einem Punkt des Funktionsgraphen ist die sog. Steigung.
Eine [Funktion](Funktionen.md) die die Steigung einer anderen Funktion $f(x)$ in jedem Punkt als Funktionswert besitzt heißt Ableitung von $f(x)$ oder $f'(x)$  

Die durchschnittliche Steigung $m$ zwischen zwei Punkten $(x_1|f(x_1))$ und $(x_2 | f(x_2))$ kann berechnet werden.
$$
m = \frac{f(x_1)-f(x_2)}{x_1-x_2}
$$
Die Änderungsrate in einem Punkt ist der Grenzwert der Steigung für $\lim_{x_1 \to x_2}(m)$ 
Verallgemeinerung dieser Idee liefert die allgemeine Ableitungsfunktion $f'(x)$ die in jedem 
Punkt die Steigung berechnet.

Im Allgemeinen sind nur stetige Funktionen Differenzierbar
# Ableitungsregeln
Beim Ableiten bestimmter Funktionstypen sind einige allgemeine Regeln und Muster bekannt.

## Potenzregel
$$
f(x)=x^n \rightarrow f'(x)=n*x^{n-1}
$$
## Summenregel
$$
f(x)=g(x)+h(x) \rightarrow f'(x)=g'(x)+h'(x)
$$
## Faktorregel
$$
f(x)=c*x^n \rightarrow f'(x)=c*n*x^{n-1} \qquad c\in\Bbb{R}
$$
## Produktregel
$$
f(x)=u(x)*v(x) \rightarrow f'(x)=u'(x)*v(x) + u(x)*v'(x)
$$
## Quotientenregel
$$
f(x)=\frac{u(x)}{v(x)} \rightarrow f'(x)=\frac{u'(x)*v(x) - u(x)*v'(x)}{(v(x))^2}
$$
## Kettenregel
$$
f(x) = u\circ v=u(v(x)) \rightarrow f'(x) = v'(x)*u'(v(x))
$$
## Trigonometrische Funktionen
$$
\begin{array}{lcl}
f(x) = \sin(x) & \rightarrow & f'(x) = \cos(x) \\
f(x) = \cos(x) = \sin(\frac{\pi}{2}-x) & \rightarrow & f'(x) = -1*\sin(x) \\
f(x) = \tan(x) = \frac{\sin(x)}{\cos(x)} & \rightarrow & f'(x) = \frac{1}{\cos^2(x)}
\end{array}
$$
## Exponentialfunktionen
$$
f(x)=b^x \rightarrow f'(x)=b^x*\ln(b)
$$
## Logarithmusfunktionen
$$
f(x)=\log_b(x) \rightarrow f'(x)=\frac{1}{x*\ln(b)}
$$
