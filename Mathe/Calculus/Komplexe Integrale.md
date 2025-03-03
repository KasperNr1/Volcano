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

## Idee
Funktionsterm wird in eine Summe von Teilbrüchen zerlegt. Anschließend werden die Grundintegrale angewandt.

## Beispiel
$$
\int_3^4{\frac{x-7}{x^2+x-2} \, dx}
$$
Linearfaktorzerlegung der Nennerfunktion 
$$
x^2 + x - 2 = (x+2)(x-1)
$$
$$
\frac{x-7}{x^2+x-2} = \frac{x-7}{(x+2)(x-1)} \overset{!}{=} \frac{A}{x+2} + \frac{B}{x-1}
$$
$$
\begin{array}{l}
x-7 = A *(x-1) + B*(x+2) \\
x-7 = Ax - A +Bx+2B \\
x-7 = (A+B)x + (-A+2B)7
\end{array}
$$
Es muss gelten $A+B=1$ und $2B-A=7$ 
LGS $\rightarrow A=3 \quad B = -2$ 

$$
\begin{array}{l}
\displaystyle \int_3^4{\frac{x-7}{x^2+x-2} \, dx} = \int_3^4{\frac{3}{x+2} + \frac{-2}{x-1} \, dx} = \int_3^4{\frac{3}{x+2} \, dx} + \int_3^4{-\frac{2}{x-1} \, dx} 
\\\\
= \displaystyle 3 * \left[ \ln(|x+2|) \right]_3^4 + (-2) * \left[ \ln(|x-1|) \right]_3^4
\\\\
3 * \left(\ln(6)-\ln(5) \right) - 2 * \left(\ln(3) -\ln(2)\right) \\\\
= -0.26396\ldots \approx -0.264
\end{array}
$$

# Integrieren von Produkten
Grundlage:
[Produktregel](Differentialrechnung.md#Produktregel) beim Ableiten
$$
f = u * v \rightarrow f'= u'v + v'u
$$
Über $f$ integrieren ergibt:
$$
\int_a^b{f'(x) \, dx} = \int_a^b{u'(x)*v(x) \, dx} + \int_a^b{u(x)*v'(x) \, dx}
$$
Wegen
$$
\int_a^b{f'(x) \, dx} = \left[ f(x) \right]_a^b = \left[ u(x) * v(x) \right]_a^b
$$
gilt:
$$
\boxed{\int_a^b{u'(x)*v(x) \, dx} = \left[ u(x) * v(x) \right]_a^b - \int_a^b{u(x)*v'(x) \, dx} =}
$$
## Strategie
$u*v'$ muss einfacher zu integrieren sein als $u'*v$ 

## Beispiel
$$
\begin{array}{l}
\displaystyle \int_0^1{(3x*e^{2x}) \, dx} & \begin{array}{l} 
v(x) = 3x &\rightarrow v'(x)=3 \\
u'(x) = e^{2x} &\rightarrow u(x) = \frac{1}{2}e^{2x}
\end{array}
\\\\
= \displaystyle \int_0^1{(e^{2x}*3x) \, dx} 
\\\\
= \displaystyle\left[ \frac12 e^{2x} *3x \right]_0^1 - \int_0^1{\left(\frac12 e^{2x} -3\right) \, dx}
\\\\
= \displaystyle\left[ \frac32x* e^{2x}\right]_0^1-\left[ \frac43 e^{2x} \right]_0^1
\\\\
= \displaystyle \left( \frac32 e^2 - 0\right) -\left( \frac34 e^2 - \frac34\right)
\\\\
= 6.29179\ldots \approx 6.29
\end{array}
$$
