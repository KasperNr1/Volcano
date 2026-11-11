---
course: Math for Machine Learning
lecture: "4"
source: https://www.tml.cs.uni-tuebingen.de/teaching/2026_maths_for_ml/index.php
date: 2026-10-29
tags:
  - lecture
---
# Determinant
With the standard basis of $\mathbb{R}^3:$ $e_1 = \left( \begin{array}{}1 \\ 0 \\ 0\end{array}\right)$ $e_2 = \left( \begin{array}{}0 \\ 1 \\ 0\end{array}\right)$ $e_3 = \left( \begin{array}{}0 \\ 0 \\ 1\end{array}\right)$ the linear mapping $T =  \left( \begin{array}{}\lambda_1 & 0 & 0 \\ 0 & \lambda_2 & 0 \\ 0 & 0 & \lambda_3 \end{array}\right)$ stretches each of the basis vector by a constant factor.

Let $U$ be the Unit Cube and $P = T(U)$ its image under $T$.
The volume of $P$ is then $\lambda_1 \cdot \lambda_2 \cdot \lambda_3$  
![](UnitCubeTransformation.png)
The derterminant describes this change of the unit volume. 
If the [Linear Map](2%20Mappings.md#Linear%20Mappings) does not have [full Rank](3%20Linear%20Maps%20as%20Matrices.md#Rank%20of%20a%20Matrix), (the image of $T$ is not fully dimensional) the unit cube gets mapped into a plane / line / lower dimensional cube. Therefore its volume in 3D Space becomes $0$.


> [!Note] Linear Dependency
> If the matrix has [Linear dependencies](1%20Vectorspaces.md#Linear%20Independence) columns, it cannot also have full [Rank](3%20Linear%20Maps%20as%20Matrices.md#Rank%20of%20a%20Matrix). So the determinant becomes $0$

## Important Properties of the Determinant
1. It always exists and is unique
2. The determinant of a mapping $T$ does `not` depend on the basis
3. $\det(c\cdot A) = c^n \det(A)$ with $n$ being the dimension of the [Vectorspace](1%20Vectorspaces.md#Vectorspace).
4. $\det(A \cdot B) = \det(A) \cdot \det(B)$
5. $A$ is invertible $\Leftrightarrow \det(A) \neq 0$ 
6. If $A$ is invertible, then $\det(A^{-1}) = \frac{1}{\det(A)}$ 

For Upper / Lower [triangular matrices](Matrizen.md#Dreiecksmatrizen) the determinant is the product of all the values on the diagonal.


> [!Tip] Alternative Definition
> The Determinant of a matrix is the product of all its [Eigenvalues](Matrizen.md#Eigenwerte%20&%20Eigenvektoren).
> 
> If $V$ is a [Vectorspace](1%20Vectorspaces.md#Vectorspace) over $\mathbb{R}$ and $T: V\to V$, then $\det(T)$ is the product of all eigenvalues `over` $\mathbb{C}$, repeated according to multiplicity.
> 

# Eigenvalues
Also see [Eigenwerte & Eigenvektoren](Matrizen.md#Eigenwerte%20&%20Eigenvektoren).

Eigenvectors are vectors, that only get scaled by a transformation $T$. 
$$
T(v) = A \cdot v= \lambda \cdot v
$$
The scaling factor is the eigenvalue $\lambda$ to this eigenvector.
Not all mappings have eigenvalues, for example the rotation matrix does not have any real eigenvectors.

> [!INFO] Existance of Eigenvalues
> Every Operator $T: V \to V$ on a finite-dimensional, [complex Vectorspace](1%20Vectorspaces.md#^6855be) has at least one eigenvalue.

Eigenvalues are not unique, when $v$ is an eigenvector, $u = a\cdot v$ is also an eigenvector.

The set of all eigenvectors of $\lambda$, together with the zero vector ist called the `eigenspace` $E(\lambda,T )$  ^84d480

Because $Tv = \lambda  v \Leftrightarrow Tv - \lambda v = 0 \Leftrightarrow Tv - \lambda I v \Leftrightarrow \left(T - \lambda I\right)v = 0$ the eigenspace can also be written as $E(\lambda, T) = \ker(T- \lambda I)$. 


> [!INFO] Properties
> Eigenvectors corresponding to different Eigenvalues are always [linearly independent](1%20Vectorspaces.md#Linear%20Independence).
> 
> The Eigenspace $E(\lambda, T)$ is always a linear [Subspace](1%20Vectorspaces.md#Subspaces) of $V$.

## Characteristic polynomial
The characteristic polynomial of an $n\times n$-matrix $A$ is defined as 
$$
p_a: \mathbb{R} \to \mathbb{R} \qquad p_A(t) := \det(A - t \cdot I)
$$
The roots of this characteristic polynomial correspond exactly to the eigenvalues of $A$.

The polynomial is independant of the basis and has $n$ roots over $\mathbb{C}$. Not all of them must be unique.

## Multiplicities
For an Operator $A$ with eigenvalue $\lambda$ we define:
- `Geometric multiplicity` the dimension of the corresponding [eigenspace](#^84d480).
- `Algebraic multiplicity` the multiplicity of the root $\lambda$ in the [characteristic polynomial](#Characteristic%20polynomial)

In general, these two do `not` coincide