---
course: Math for Machine Learning
lecture: "6"
source: https://www.tml.cs.uni-tuebingen.de/teaching/2026_maths_for_ml/index.php
date: 2026-11-05
tags:
  - lecture
---
# Orthogonal and normal things
## Orthogonal Vectors and Sets
Consider a [pre-Hilbert Space](05%20Diagonalization%20and%20Normed%20Spaces.md#Banach%20and%20Hilbert%20Spaces) $V$.
- Two vectors $v_1, v_2 \in V$ are called `orthogonal` if their scalar product is $0$: $\left<v_1, v_2 \right> =0$ This can also be written as $v_1 \bot v_2$ 
- Two [sets](Intervalle%20und%20Mengen.md#Mengen) $V_1, V_2 \subseteq V$ are called `orthogonal` if every vector in one set is orthogonal to every vector in the other set
$$
\forall v_1 \in V_1, \forall v_2 \in V_2 : \left<v_1, v_2\right> = 0
$$
- For a set $S \subset V$ we define its `orthogonal complement` $S^\bot$ as the set of all vectors that are orthogonal to every vector in $S$
$$
S^\bot := \left\{v \in V \mid v \bot s \forall s \in S \right\}
$$

## Orthonormal vectors and sets
Two vectors are called `orthonormal` if they are [orthogonal](#Orthogonal%20Vectors%20and%20Sets) and additionally have [norm](05%20Diagonalization%20and%20Normed%20Spaces.md#Definition%20Norm%20on%20a%20Vector%20Space) 1
$$
\left<v_1, v_2\right> = 0, \quad \left|\left|v_1\right|\right| = 1, \; \left|\left|v_2\right|\right| = 1
$$
	A set of vectors $v_1, v_2, \dots v_n$ is called `orthonormal` if any two vectors are orthonormal.

## Orthogonal / Normal Basis
In an orthonormal [Basis](01%20Vectorspaces.md#Basis) $u_1, u_2, \dots u_n$ the representation of a vector $v$ is given as:
$$
v = \sum_{i=1}^n \left<v, u_i\right> u_i, \qquad \text{with} \; v = \sum a_iu_i
$$

> [!INFO] Existance
> Such a basis always exists and can be constructed using the [Gram-Schmidt orthogonalization](https://de.wikipedia.org/wiki/Gram-Schmidtsches_Orthogonalisierungsverfahren)

# Projections
An Operator $A \in \mathcal{L}(V)$ is called a `projection` if $A^2 = A$.
This means that applying the operator more than one time has no result on the outcome.


> [!NOTE] Example
> A Projection generally `removes Information`. For example it could set the first coordinate of a given vector to $0$.
> $$
> \left(\begin{array}{}1 \\ 1 \\ 1 \end{array}\right) \to \left(\begin{array}{}0 \\ 1 \\ 1 \end{array}\right) \to \left(\begin{array}{}0 \\ 1 \\ 1 \end{array}\right)
> $$
> Applying this transformation multiple times does not change the result, hence $A^2 = A$

## Orthogonal Projection
Let $U$ be a finite-dimensional [Subspace](01%20Vectorspaces.md#Subspaces) of a [pre-Hilbert space](05%20Diagonalization%20and%20Normed%20Spaces.md#Banach%20and%20Hilbert%20Spaces) $H$. Then there exists a linear [Projection](#Projections)
$$
P_U: H \to U
$$
with $\ker(P_U) = U^\bot$. $P_U$ is called the `orthogonal projection` of $H$ on $U$.


# Orthogonal Matrices
Let $Q \in \mathbb{R}^{n \times n}$ be a matrix with [orthonormal](#Orthonormal%20vectors%20and%20sets)
 column vectors (with respect to the [euclidian scalar product](05%20Diagonalization%20and%20Normed%20Spaces.md#Scalar%20Product)) Then $Q$ is called an `orthogonal` matrix

> [!Error] Naming
> While the column vectors are orthonormal, the matrix itself is called orthogonal

If $Q \in \mathbb{C}^{n\times n}$ it is called a `unitary matrix` when all its columns are [orthonormal](#Orthonormal%20vectors%20and%20sets)

Examples of orthogonal matrices are:
$$
\left(\begin{array}{}1 & 0 \\ 0 & 1\end{array}\right) \quad
\left(\begin{array}{}1 & 0 \\ 0 & -1\end{array}\right) \quad
\left(\begin{array}{}\cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{array}\right) \quad
$$

## Properties of orthogonal matrices
Let $Q$ be an orthogonal matrix. Then:
- Orthogonal Columns $\Leftrightarrow$ Rows are orthogonal
- $Q$ is always invertible and its invers is equal to its transpose $Q^{-1} = Q^T$
- $Q$ acts as geometry
  $$
  \forall v \in V, \left|\left|Qv\right|\right| = \left|\left|v\right|\right|
  $$
  Meaning that applying the transformation to any vector does not change its length.
- $Q$ preserves Angles
  $$
  \left<Qv, Qu\right> = \left<v, u\right> \quad \forall u,v \in V
  $$
  - $\left|\det Q\right| =1$

# Symmetric matrices
For a matrix $A \in \mathbb{C}^{n \times n}$ it is called `hermitian` if 
$$
A  = \overline{A}^T
$$

A Matrix $A \in \mathbb{R}^{n\times n}$ is symmetric if it is identical to its transpose. This is a special case of the hermitian matrix
$$
A = A^T = \overline{A}^T = \overline{A^T}
$$

> [!NOTE] Eigenvalues of hermitian matrices
> A hermitian matrix has all $n$ [Eigenvalues](04%20Eigenvalues%20and%20Determinant.md#Eigenvalues) live in $\mathbb{R}$ For a complex matrix the eigenvectors might still live in $\mathbb{C}^n$. For a symmetrical matrix the eigenvector always live in $\mathbb{R}^n$.

## Self-Adjoint operators
An Operator $T \in \mathcal{L}(V)$ on a [pre-Hilbert space](05%20Diagonalization%20and%20Normed%20Spaces.md#Banach%20and%20Hilbert%20Spaces) $V$ is called `self-adjoint` if:
$$
\left<Tv, w\right> = \left<v, Tw\right>
$$
Sometimes it is also called a `Hermitian operator` (on $\mathbb{C}^n$) or a `symmetric operator` on $\mathbb{R}^n$.

Self adjoint operators are represented by hermitian or symmetric matrices.
The representing matrix has at least one real-valued [Eigenvalue](04%20Eigenvalues%20and%20Determinant.md#Eigenvalues).

# Spectral Theorem for symmetric matrices
A symmetric matrix $A \in \mathbb{R}^{n\times n}$ is `orthogonally diagonalizable`:
There always exists an [Orthogonal Matrix](#Orthogonal%20Matrices) $Q \in \mathbb{R}^{n \times n}$ such that
$$
A = QDQ^T = \sum_{i=1}^{n} \lambda_i q_i q_i^T
$$

$$
D = \left(\begin{array}{}\lambda_1 & & \\
& \ddots & \\ && \lambda_n\end{array}\right)
\quad
Q = \left(\begin{array}{}| & | & \\ q_1 & q_2 & \dots \\ | & | & \end{array}\right)
$$

This property is very powerful.
Applying the matrix $A$ multiple times becomes easy to compute.
$$
A^{100} = \left(QDQ^T\right)\left(QDQ^T\right)\dots\left(QDQ^T\right) = QD^{100}Q^T
$$
Because of the [Properties of orthogonal matrices](#Properties%20of%20orthogonal%20matrices) all the pairs of $Q^T Q$ cancel out since $Q^T = Q^{-1}$ for orthogonal matrices. 

> [!tip] What is this good for?
> This allows us to compute the product of many applications of $A$ by simply raising $\lambda_i$ to some power. This Operation reduces the amount of computational steps required by orders of magnitude, since it removes the need to multiply all the matrices explicitely.

