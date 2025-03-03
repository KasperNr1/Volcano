# Eigenschaften des [Integrals](Integrale%20&%20Rotationskörper.md)
## Linearität
$$
\int_a^br*f(x) \, dx = r*\int_a^bf(x)\, dx
$$
## Additivität
$$
\int_a^bf(x) \, dx + \int_a^bg(x) \, dx = \int_a^bf(x)+g(x)\, dx
$$
# Integration durch Substitution
Bekannt: Lineare Substitution
$$
\int_a^bf(r*x+s) \, dx = \frac{1}{r} * [F(r*x+s)]_a^b 
$$
Neu: Logarithmische Integration
$$
\int_a^b \frac{g'(x)}{g(x)} \, dx = [\ln(|g(x)|)]_a^b
$$
Denn
$$
f(x) = \ln(|g(x)|) \rightarrow f'(x) = \frac{1}{g(x)} * g'(x) = \frac{g'(x)}{g(x)}
$$
Beispielsweise die [Tangensfunktion](Funktionen.md#Tangens) lässt sich mit anhand dieser Regel integrieren.
$$
\begin{array}{c}
f(x) = \tan(x) = \dfrac{\sin(x)}{\cos(x)} = - \dfrac{-\sin(x)}{\cos(x)} \\\\
\rightarrow F(x) = -\ln(|\cos(x)|)
\end{array}
$$
## Substitution
Grundlage ist die [Verkettung](Differentialrechnung.md#Kettenregel) beim Ableiten.
Sei $U$ eine [Stammfunktion](Integrale%20&%20Rotationskörper.md#Stammfunktion) von $u$ und $v$ eine [differenzierbare Funktion](Differentialrechnung.md#Ableitung).
Betrachtet wird die Verkettung $H$ mit $H(x) = U(v(x))$
$H'(x) = U'(v(x)) * v'(x)$
$= u(v(x)) * v'(x) \leftarrow$ Kettenregel

$H$ ist eine Stammfunktion von $h$ mit $h(x) = u(v(x)) * v'(x)$ 

$$
\int_a^b u(v(x)) * v'(x) \, dx = \left[ U(v(x)) \right]_a^b = U(v(b)) - U(v(a)) = \left[ U(z) \right]_{v(a)}^{v(b)} = \int_{v(a)}^{v(b)} u(z)  \, dz
$$
### Strategie
- Innere Funktion $v$ so wählen, dass $v'$ im Integranden als Faktor vorkommt
- Äußere Funktion $u$ so wählen, dass eine Stammfunktion $U$ bekannt ist.

### Beispiele
$$
\begin{array}{l}
\displaystyle\int_0^2{\dfrac{4x}{\sqrt{1 + 2x^2}} \, dx} 
& \begin{array}{l} 
v(x) = 1+2x^2 &\rightarrow v'(x)=4x \\
u(z) = \dfrac{1}{\sqrt{z}} &\rightarrow U(z) = 2 \sqrt{z}
\end{array}
\\\\
\displaystyle\int_0^2{\dfrac{1}{\sqrt{1 + 2x^2}}4x \, dx}
\\\\
\displaystyle\int_0^2{u(v(x)) * v'(x) \, dx} 
\\\\
\displaystyle\int_{v(0)}^{v(2)}{u(z) \, dz}
\\\\
\displaystyle\int_1^9{\dfrac{1}{\sqrt{z}} \, dz} = \left[2\sqrt{z}\right]_1^9 
\\\\
=2\sqrt{9}-2\sqrt{1} \\
=6-2 \\
=4
\end{array}
$$

Aufgrund der [Linearität](#Linearität) von Integralen ist es möglich auch aus dieser Art verketteter Integrale konstante Faktoren auszuklammern.
$$
\int_0^2{\dfrac{8x}{\sqrt{1 + 2x^2}} \, dx} = \int_0^2{2*\dfrac{4x}{\sqrt{1 + 2x^2}} \, dx} = 2 * \int_0^2{\dfrac{4x}{\sqrt{1 + 2x^2}} \, dx} = 2 * 4 = 8 
$$
---
Gegeben ist $h$ mit $h(x) = \dfrac{2x}{(1+3x)^3}$ 
Gesucht ist die Stammfunktion $H$ von $h$ 
$$
\begin{array}{l}
\displaystyle\int_a^b{\dfrac{2x}{(1 + 2x)^3} \, dx} 
& \begin{array}{l} 
v(x) = 1+x^2 &\rightarrow v'(x)=2x \\
u(z) = z^{-3} &\rightarrow U(z) = -\dfrac{1}{2z^2}
\end{array}
\\\\
\displaystyle\int_a^b{\dfrac{1}{(1 + 2x)^3} * 2x \, dx}
\\\\
= \displaystyle\int_{v(a)}^{v(b)} \dfrac{1}{z^3} \, dz
\\\\
= \left[-\dfrac{1}{2z^2}\right]_{v(a)}^{v(b)}
\\\\
= \left[-\dfrac{1}{2\left( 1+x^2 \right)^2}\right]_{v(a)}^{v(b)}
\\\\
H(x) = -\dfrac{1}{2\left( 1+x^2 \right)^2}
\end{array}
$$

# Integration durch Parzialbruchzerlegung
Bekannt:
$$
f(x) = \frac{1}{x^n} = x^{-n} \rightarrow \left\{\begin{array}{l}n=1 & \rightarrow F(x) = \ln(|x|) \\ n>1 & \rightarrow F(x) = \dfrac{1}{1-n}*x^{1-n} = -\dfrac{1}{n-1}*\dfrac{1}{x^{n-1}} 
\end{array} \right.
$$

## Grundintegrale
$$
\int_u^v{\frac{A}{x-a} \, dx} = A * [\ln(|x-a|)]_u^v
$$
Und
$$
\int_u^v{\frac{A}{x-a} \, dx} = \left[ -\frac{1}{n-1} * \frac{A}{(x-a)^{n-1}} \right]_u^v
$$
