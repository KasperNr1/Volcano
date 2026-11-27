---
course: Math for Machine Learning
lecture: "9"
source: https://tml-tuebingen.de/teaching/2026_maths_for_ml/downloads_free/Calculus.pdf
date: 2026-11-17
tags:
  - lecture
---
# Sequences
## Cauchy Sequence
A sequence $\left(x_n\right)_{n \in \mathbb{N}} \subset \mathbb{R}^d$ is called a `Cauchy sequence` if
$$
\forall_{\varepsilon > 0} \exists_{N \in \mathbb{N}} \forall_{n,m>N}: \left|\left|x_n -x_m\right|\right| < \varepsilon
$$
Meaning that for any given difference $\varepsilon$ there exists a border $N$ such that every pair of elements after that border are at most $\varepsilon$ apart from each other.

## Accumulation Point
A point $x \in \mathbb{R}^d$ is called an `accumulation point` of the sequence $(x_n)_n$ if
$$
\forall_{\varepsilon >0} \forall_{N \in \mathbb{N}} \exists_{n > N}: \left|\left|x_n - x\right|\right|< \varepsilon
$$
Meaning that for every distance $\varepsilon$ to a limit $x$ there exists some point $x_n$ that is closer than this distance.
So the sequence has infinitely many points that are arbitrarily close to the limit.

> [!Info] Existance and multiplicity
> A sequence can have many accumulation points.
> Or none at all.
> 
> Even if the sequence has exactly one accumulation point, it is not necessarily a [Cauchy Sequence](#Cauchy%20Sequence)

## Convergence
A sequence $(x_n)_n$ `converges` to $x \in \mathbb{R}^d$ if
$$
\forall_{\varepsilon>0} \exists_{N \in \mathbb{N}} \forall_{n > N} : \left|\left|x_n - x\right|\right| < \varepsilon
$$
Meaning that for every distance $\varepsilon$ there exists an index $N$ such that all point after this index are closer to the value $x$ than the distance.

We also use the following notation
$$
\lim_{n \to \infty} x_n = x \qquad \text{or} \qquad x_n \overset{n \to \infty}{\longrightarrow} x
$$

> [!NOTE] Convergence and Cauchy
> If $(x_n)_n$ converges to $x$, then $x$ is the only [Accumulation Point](#Accumulation%20Point) and the sequence is [Cauchy](#Cauchy%20Sequence)

## Examples
Consider the sequence given by $x_n = \dfrac{1}{n}$
This sequence is [Cauchy](#Cauchy%20Sequence) and also [convergences](#Convergence) to $0$.

![](ExampleSequence01.png)

If we consider the sequence as part of the restricted [interval](Intervalle%20und%20Mengen.md#Intervalle) $(0,1$]$ it is [cauchy](#Cauchy%20Sequence) but does not converge. (Because the convergence-point is not part of the [space](01%20Vectorspaces.md#Vectorspace).

---

Consider the sequence $x_n = \left\{ \begin{array}{}\dfrac{1}{n} & \text{if} \; n \; \text{is even} \\ n & \text{if} \; n \; \text{is odd} \end{array}\right.$ 

![](ExampleSequence02.png)

It has an accumulation point at $0$ but does not [converge](#Convergence) and is also not [cauchy](#Cauchy%20Sequence).


# Minima and Maxima
Assume we are on $\mathbb{R}$ or more generally, on a space that has total ordering.
Let $U \subset \mathbb{R}$ be a subset.

- $x \in \mathbb{R}$ is called a `maximum element` of $U$ if $x\in U$ and $\forall_{u \in U}: u \leq x$ 
- $x$ is called an `upper bound` of $U$ if $\forall_{u\in U }: u\leq x$ 
> [!Warning] Intervalls
> Note that the upper bound $x$ itself does not need to be contained in the set $U$ 
- $x$ is called `supremum` of $U$ if it is the smallest upper bound

The terms `minimum`, `lower bound` and `infimum` are defined analogously.

## Examples
- $1$ is the maximum of $[0,1]$. It is also the supremum of $[0,1]$
- The [open intervall](Intervalle%20und%20Mengen.md#Intervalle) $(0,1)$ does not have a maximum element.
- $5$ is an upper bound of $(0,1)$
- $1$ is also an upper bound of $(0,1)$
- $1$ is the smallest upper bound and thus the supremum of $(0,1)$


# Bounded Sequences
A sequence $(x_n)_{n\in \mathbb{N}}$ is called `bounded` if there exists $a,b \in \mathbb{R}$ such that $\forall_{n\in \mathbb{N}} : x_n \in [a,b]$ 
Meaning that all elements of a sequence land in an interval of finite size.

Any bounded sequence in $\mathbb{R}$ has at least one [Accumulation Point](#Accumulation%20Point).


# Limsup and Liminf
For a sequence $(x_n)_n \subset \mathbb{R}$ we define:
$$
\liminf_{n\to \infty} := \lim_{n \to \infty}\left(\inf_{m \geq n} x_m \right)
$$
and 
$$
\limsup_{n\to \infty} := \lim_{n \to \infty}\left(\sup_{m \geq n} x_m \right)
$$

For a bounded sequence $(x_n)_n$ the $\limsup$ is the largest [Accumulation Point](#Accumulation%20Point) of the sequence and $\liminf$ its smallest.

The $\liminf$ is the largest $y \in \mathbb{R}$ such that
$$
\forall_{\varepsilon>0}\exists_{N}\forall_{n>N} : x_n > y-\varepsilon
$$


# Continuity
A function $f: X \to Y$ between two metric spaces $(X,d), (Y,d)$ is called `continuous at` $x_0 \in X$ if 
$$
\forall_{\varepsilon>0}\exists_{\delta>0} \forall_{x \in X} : d(x,x_0) < \delta \Rightarrow d(f(x), f(x_0)) < \varepsilon
$$
A function $f: X \to Y$ is called `continuous` if it is continuous for every $x_0 \in X$
$$
\boxed{\forall_{x_0 \in X}}\,\forall_{\varepsilon>0}\exists_{\delta>0} \forall_{x \in X} : d(x,x_0) < \delta \Rightarrow d(f(x), f(x_0)) < \varepsilon
$$


One alternate definition says that $f: X \to Y$ is continuous at $x_0$ if for every sequence $(x_n)_n \subset X$ we have 
$$
x_n \to x_0 \Longrightarrow f(x_n) \to f(x_0)
$$
Meaning that for any two very close input values the output values are also very close.

## Uniform Continuity
A function $f: X \to Y$ is called `uniformly continous` if
$$
\forall_{\varepsilon > 0} \exists_{\delta >0} \forall_{x_0, x \in X}:d(x,x_0) < \delta \Rightarrow d(f(x), f(x_0)) < \epsilon
$$
Meaning that any finite interval on the function does not have infinite height gain.
This allows for unbounded derivatives at infinitesimally narrow points.
An example is the function $f(x) = \sqrt{x}$ from $[0,\infty)$. While it has infinite steepness at $x=0$, it does not gain infinite height.
So the function is uniformly continuous.

Functions like $f(x) = \dfrac{1}{n}$ or $f(x) = x^2$ are not uniformly continuous because their height gain can become infinite.
For $1/x$ this is at $x=0$ and for $x^2$ it is as $x \to \infty$.

> [!Info] Rectangle intuition
> For any given $\varepsilon$ one can find a $\delta$ such that the rectangle with height $\varepsilon$ and width $\delta$ can be placed on any point of the function graph such the graph passes through its left and right side, without piercing the top or bottom edge. 


If $f: [a,b] \to \mathbb{R}$ is continuous and defined only on a finite [Interval](Intervalle%20und%20Mengen.md#Intervalle), it is automatically uniformly continuous.


## Libschitz 
A function $f: X\to Y$ is called `libschitz continuous` with Libschitz constant $L$ if:
$$
\forall_{x,y \in X} : d(f(x), f(y)) \leq L \cdot d(x,y)
$$
Meaning that the value of the derivative of $f$ does not become infinitely large and is bounded at every point.

Libschitz continuity implies [Uniform Continuity](#Uniform%20Continuity) but not the other way around.

## Intermediate Value Theorem
If $f: [a,b] \to \mathbb{R}$ is [continuous](#Continuity), then it attains all values between $f(a)$ and $f(b)$.
$$
\forall_{y \in [f(a), f(b)]} \exists_{x \in [a,b]} : f(x) = y
$$

> [!NOTE] Application
> One Application of this theorem is finding zeros.
> If $f(a) < 0$ and $f(b)>0$ then there must exist a value $x \in [a,b]$ with $f(x) =0$ 


# Inverse Functions
Let $f: A \to B$ be a function, denote by $f(A) \subset B$ the [range](02%20Mappings.md#Kernel%20and%20Range) of $f$.
A mapping $g: f(A) \to A$ is called the `inverse` of $f$, denoted as $f^{-1}$ if:
$$
g \circ f = \text{id} \qquad f \circ g = \text{id}
$$

Not every function has an inverse.
Some literature also uses the notation $f^{-1}$ to denote the [Pre-Image](02%20Mappings.md#Pre-Image) (which does not need to be unique).

## Invertible Functions
Let $D \subset \mathbb{R}$, $f: D \to \mathbb{R}$ be continuous and strictly monotone, that is $a<b \Leftrightarrow f(a) < f(b)$ or $a>b \Leftrightarrow f(a) > f(b)$.

Then $f$ is invertible, and the inverse is both, monotone and [continuous](#Continuity).


> [!INFO] Intuition
> The inverse of a function can be thought of as its mirror image along the main Diagonal with $y=x$.
> ![](InverseOfAFunction.png)

