---
course: Math for Machine Learning
lecture: "5"
source: https://www.tml.cs.uni-tuebingen.de/teaching/2026_maths_for_ml/index.php
date: 2026-11-03
tags:
  - lecture
---
# Diagnonalizable Matrices
An Operator $T\in \mathcal{L}(V)$ is diagonalizable if there exists a Basis $\mathcal{B}$ of $V$ such that the corresponding matrix is diagonal:
$$
M(T,\mathcal{B},\mathcal{B}) = \left(\begin{array}{}\lambda_1 & \dots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \dots & \lambda_n \end{array}\right)
$$
This is not always the case.

$T$ is diagonalizable if any one of these equivalent statements is true
1. $V$ has a basis consisting of [Eigenvectors](4%20Eigenvalues%20and%20Determinant.md#Eigenvalues) of $T$.
2. $\dim V = \dim(\text{eigenspace}(\lambda_1)) + \dots + \dim(\text{eigenspace}(\lambda_m))$
3. $V$ has $n$ eigenvalues (if counted with multiplicity) and for all of them, the [algebraic and geometric multiplicities](4%20Eigenvalues%20and%20Determinant.md#Multiplicities) are the same.

# Triangular matrices
Let $T\in \mathcal{L}(V), \mathcal{B} = \{v_1, v_2, \dots v_n \}$  a basis. Then the following two statements are equivalent:
1. $M(T, \mathcal{B})$ is upper triangular
2. $\forall j = 1, \dots, n: Tv_j \in \text{span} \{v_1, \dots , v_j\}$ 


> [!NOTE] Triangularization over $\mathcal{C}$
> For each complex Vectorspace $V$ there exists a Basis $\mathcal{B}$ such that $\mathcal{M}(T, \mathcal{B},\mathcal{B})$ has upper triangular form
> 
> This does not hold over $\mathbb{R}$


## Invertability of triangular matrices
An upper triangular matrix with all $0$ for values below the diagonal is invertible if all values on the diagonal are non-zero.
$$
M(T,\mathcal{B},\mathcal{B}) = \left(\begin{array}{}\lambda_1 & \dots & * \\ \vdots & \ddots & \vdots \\ 0 & \dots & \lambda_n \end{array}\right)
$$
Since a matrix is invertable if the [Determinant](4%20Eigenvalues%20and%20Determinant.md#Important%20Properties%20of%20the%20Determinant) is non-zero and the determinant of a triangular matrix is the product of the value on its diagonal, only the values on the diagonal are relevant for this property.


# Normed Spaces
## Definition Metric Space
Let $X$ be a [set](Intervalle%20und%20Mengen.md#Mengen). A function $d: X \times X \to \mathbb{R}$ is called a `metric` if the following conditions hold for all $x, y, z \in X$
1. $d(x,x) = 0$ 
2. $d(x,y) > 0$ if $x \neq y$
3. $d(x,y) = d(y,x)$ (Symmetry)
4. $d(x, z) \leq d(d,y) + d(y,z)$ (Triangle Inequality)
![](TriangleInequality.png)

## Definition Norm on a Vector Space
Let $V$ be a [Vectorspace](1%20Vectorspaces.md#Vectorspace). A `norm` on $V$ is a function $\left|\left|\cdot\right|\right| : V \to \mathbb{R}$ such that for all $x,y \in V, \quad \lambda \in \mathbb{F}$ where $\mathbb{F}$ is the field of the vectorspace.
1. $\left|\left|\lambda x\right|\right| = \left|\lambda \right| \cdot \left|\left|x\right|\right|$ (Homogeneous)
2. $\left|\left|x + y\right|\right| \leq \left| \left| x \right| \right| + \left|\left|y\right|\right|$ (Triangle Inequality)
3. $\left|\left|x\right|\right| = 0 \Longleftarrow x = 0$ (Definiteness)
4. $\left|\left|x\right|\right| = 0 \Longrightarrow x = 0$ (Definiteness)

$\left|\left|\cdot\right|\right|$ is called a `semi-norm` if only conditions 1-3 are satisfied.


## Euclidian Norm
The Euclidian Norm is defined as the square-root of the sum of the squared values inside a vector.
$$
\left|\left|x\right|\right| = \left(\sum_{i=1}^d x_i^2\right)^{\frac{1}{2}}
$$
This corresponds to repeated application of the pythagorean theorem and describes the length of the vector in $d$-dimensional euclidian space.

This norm induces a metric:
$$
d(x,y) = \left|\left|x-y\right|\right|
$$
To describe the distance between two vectors.

## P-Norm
Is a more general case of the [Euclidian Norm](#Euclidian%20Norm) where power and root $p$ are used, instead of fixing its value to $2$.
$$
\left|\left|x\right|\right| = \left(\sum_{i=1}^d x_i^p\right)^{\frac{1}{p}} \qquad \text{for} \; 0<p<\infty
$$


> [!NOTE] Which $p$-Norm is a norm?
> The [Conditions](#Definition%20Norm%20on%20a%20Vector%20Space) are satisfied for all $p \geq 1$.
> If $p<1$ the triangle inequality can break


## Unit ball of a norm
The `unit ball` of a Norm is the set of all points such that their norm is $\leq 1$
$$
B_p := \left\{x \in \mathbb{R}^d \mid \left|\left|x\right|\right|_p \leq 1 \right\}
$$

The `unit sphere` of a Norm is the set of all points such that their norm is exactly $1$
$$
S_p := \left\{x \in \mathbb{R}^d \mid \left|\left|x\right|\right|_p = 1 \right\}
$$

For [p>1](#P-Norm) the unit balls are convex
![](ConvexUnitBalls.png)
If $p<1$ they become concave and converge to the axies as $p$ approaches $0$
![](ConcaveUnitBalls.png)

# Scalar Product
Consider a [Vectorspace](1%20Vectorspaces.md#Vectorspace) $V$. A Mapping $\left< \cdot, \cdot \right> : V \times V \to \mathbb{R}$ is called a `scalar Product` if:
1. Linearity
   $\left<x_1 +x_2, y\right> = \left<x_1, y\right> + \left<x_2, y\right>$
   $\left<\lambda x ,y\right> = \lambda \left<x,y\right>$ 
2. Symmetry
   $\left<x,y\right> = \overline{\left<y,x\right>}$ (where $\overline{a}$ is the complex conjugate of a complex number and $a = \overline{a}$ if $a$ is $a \in \mathbb{R}$) 
3. Positive Definiteness
   $\left<x,x\right> \geq 0$
   $\left<x,x\right> = 0 \Longleftrightarrow x=0$ 

The scalar product is related to [norms](#P-Norm) through angles in triangles.
$$
\left<v, w\right> = \left|\left|v\right|\right| \cdot \left|\left|w\right|\right| \cdot \cos(\alpha)
$$
![](ScalarProductWithAngles.png)

## Banach and Hilbert Spaces
- A [Vectorspace](1%20Vectorspaces.md) with a norm is called a `normed space`
- If a normed space is complete (meaning that every [Cauchy Sequence](https://de.wikipedia.org/wiki/Cauchy-Folge) converges) then it is called a `Banach Space`
- A vector space with a [Scalar Product](#Scalar%20Product) is called a `pre-Hilbert Space`
- If it is additionally complete, it is called a `Hilbert Space`

## Relationship to norms
The existence of a scalar product implies the existence of a [Norm](#P-Norm). The reverse is not true.
This is, because generally the norm can be defined through the scalar product like this:
$$
\left|\left|x\right|\right| := \sqrt{\left<x,x\right>}
$$
Then $\left|\left|\cdot\right|\right|$ is a norm induced by $\left<\cdot, \cdot\right>$ 


The existence of a norm implies the existence of a [metric](#Definition%20Metric%20Space) 
This is, because the metric can generally be defined through the norm like this:
$$
d(x,y) = \left|\left|x-y\right|\right|
$$
Then $d$ is a metric induced by the norm.

# Important inequalities
Consider $u,v \in \mathbb{R}^d$ and denote by $\left|\left|\cdot\right|\right|_p$ the [P-Norm](#P-Norm).

## Cauchy-Schwarz inequality
$$
\left|\left<u,v\right>\right| \leq \left|\left|u\right|\right|_2 \cdot \left|\left|v\right|\right|_2
$$

## Hölder inequality
Let $p, q \geq 1$ with $\frac{1}{p} + \frac{1}{q} = 1$. Then:
$$
\left|\left<u,v\right>\right| \leq \sum_{i=1}^{d} \left|u_i \cdot v_i\right| \leq \left|\left|u\right|\right|_p \cdot \left|\left|v\right|\right|_q
$$

