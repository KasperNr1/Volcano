---
course: Math for Machine Learning
lecture: "7"
source: https://www.tml.cs.uni-tuebingen.de/teaching/2026_maths_for_ml/index.php
date: 2026-11-10
tags:
  - lecture
---
# Positive Definite Matrices
A [Matrix](03%20Linear%20Maps%20as%20Matrices.md#Definition%20of%20a%20Matrix) $A \in \mathbb{R}^{n\times n}$ is called 
- `Positive Definite (pd)` if $x^T Ax > 0$ for all $x \in \mathbb{R}^n \setminus \left\{0\right\}$ 
- `Positive semi-definite (psd)` if $x^T Ax \geq 0$ for all $x \in \mathbb{R}^n$ 

## Gram Matrices
A matrix $A$ is called a `Gram Matrix` if there exists a set of vectors $v_1, v_2, \dots v_n$ such that:
$$
a_{ij} = \left<v_i, v_j\right>
$$

> [!NOTE] Additional Properties
> On $\mathbb{C}^{n\times n}$ Gram matrices are [Hermitian](06%20Orthogonal%20basis%20and%20projections.md#Symmetric%20matrices)
> On $\mathbb{R}^{n\times n}$ Gram matrices are [Symmetric](06%20Orthogonal%20basis%20and%20projections.md#Symmetric%20matrices)


## Characterization of Positive Definite Matrices
For a Matrix $A \in \mathbb{C}^{n \times n}$ that is [hermitian](06%20Orthogonal%20basis%20and%20projections.md#Symmetric%20matrices) the following statements are equivalent:
1. $A$ is [psd](#Positive%20Definite%20Matrices) ([pd](#Positive%20Definite%20Matrices))
2. All [Eigenvalues](04%20Eigenvalues%20and%20Determinant.md#Eigenvalues) of $A$ are $\geq 0$ ($>0$)
3. The Mapping $\left<\cdot , \cdot\right>_A : \mathbb{C}^n \to \mathbb{C}$  defined by
$$
\left<x,y\right>_A := \overline{y}^T Ax
$$
	Satisfies all properties of a scalar product (Except one: if $\left<x,x\right>_A =0$, this does not imply $x=0$)
4. $A$ is a [Gram Matrix](#Gram%20Matrices) of $n$ vectors $a_{ij} = \left< x_i, x_j\right>$ which are not necessarily [linearly independant](01%20Vectorspaces.md#Linear%20Independence) (Which are linearly dependant)


## Roots of PSD Matrices
Let $A \in \mathbb{R}^{n \times n}$ be symmetric and [psd](#Positive%20Definite%20Matrices).
Then there exists a matrix $B \in \mathbb{R}^{n \times n}$ such that
$$
A = B^2
$$
$B$ is sometimes called the `square root` of $A$ and denoted as $B = A^{1/2}$ 


## Important psd Matrices
Consider a `data matrix` $X \in \mathbb{R}^{n \times d}$ with $n$ data points and $d$ dimensions. We assume the data is centered, that is, each column of $X$ has mean $0$.

Then the matrix
$$
X := X^TX \in \mathbb{R}^{d \times d}
$$
is called the `covariance matrix` (up to the factor $1/n$)


The matrix 
$$
K := XX^T \in \mathbb{R}^{n\times n}
$$
is called a `kernel matrix` for the linear [Kernel](02%20Mappings.md#Kernel%20and%20Range) and in this special case, it is also the [Gram Matrix](#Gram%20Matrices) 

All these matrices are [Symmetrical](06%20Orthogonal%20basis%20and%20projections.md#Symmetric%20matrices) and [Positive Semi-Definite](#Positive%20Definite%20Matrices)


# Rayleigh coefficient
Let $A \in \mathbb{R}^{n \times n}$ be a symmetric matrix. The function
$$
R_A : \mathbb{R}^n \setminus \{0\} \to \mathbb{R}, \quad x \mapsto \frac{x^TAx}{x^Tx} = \frac{x^TAx}{\left|\left|x\right|\right|^2}
$$
Is called the `Rayleigh coefficient`. 

The $\min$ and $\max$ of the rayleigh coefficient are attained at the smallest and the largest [Eigenvalues](04%20Eigenvalues%20and%20Determinant.md#Eigenvalues) of $A$.
$$
\min_{x \in \mathbb{R}^n} R_A(x) = \min_{\left|\left|x\right|\right| =1} x^T Ax = \lambda_1, \; \text{attained at} \; x = v_1
$$
$$
\max_{x \in \mathbb{R}^n} R_A(x) = \max_{\left|\left|x\right|\right| =1} x^T Ax = \lambda_1, \; \text{attained at} \; x = v_n
$$

The second eigenvalue can be found by constraining the solution to be orthogonal to the first eigenvalue
$$
\min_{\left|\left|x\right|\right| =1, \; x \bot v_1} R(x) 
$$
This problem is solved by $x = v_2$ and $R(v_2) = \lambda_2$

# Matrix norms
We want to quantify the `similarity` of various matrices. So we define `norms` on the space of all matrices.

> [!Warning] Not all of them are proper [Norms](05%20Diagonalization%20and%20Normed%20Spaces.md#Normed%20Spaces)

## Maximum Norm
Is the entry-wise norm. Its value is the value of the largest element in the matrix
$$
\left|\right| A \left|\right|_\max = \max_{ij} \left|a_{ij}\right|
$$

## Frobenius Norm
$$
\left|\right| A \left|\right|_\text{F} = \sqrt{\sum_{ij}a_{ij}^2} = \sqrt{\text{tr}(A^TA)} = \sqrt{\sum \sigma_i^2}
$$
Where $\sigma_i$ are the [Singular Values](#Singular%20Values) of $A$.

## Spectral Norm
Also called `operator Norm` is defined as the largest [Singular Value](#Singular%20Values) of $A$
$$
\left|\left|A\right|\right|_2 = \sigma_\max(A)
$$

Alternatively it can be defined using the [Euclidian Norm](05%20Diagonalization%20and%20Normed%20Spaces.md#Euclidian%20Norm) $\left|\left|x\right|\right|$ as
$$
\left|\left|A\right|\right|_2 = \max_{x \neq 0} \frac{\left|\left|Ax\right|\right|}{\left|\left|x\right|\right|}
$$

## Induced (operator) Norms
Use the generalized [P-Norm](05%20Diagonalization%20and%20Normed%20Spaces.md#P-Norm) in place of the euclidian norm from the alternate definition of the [Spectral Norm](#Spectral%20Norm).
This makes the spectral norm itself a special case of an induced norm where $p =2$.

## Nuclear Norm
Is the square root of the [Trace](08%20Pseudo%20Invers%20and%20Trace%20of%20a%20Matrix.md#Trace) of the [Gram Matrix](#Gram%20Matrices) of $A$
$$
\left|\left|A\right| \right|_* = \text{tr}\left(\sqrt{A^T A}\right)
$$
> [!NOTE] Note
> Many other norms can be defined


# Singular Value Decomposition
Motivation is the `Netflix Matrix` where each row is a user and each column represents a show. Most users only watch and rate a handful of shows, so the absolute majority of all entries in this matrix is $0$.
To recommend shows to new users based on their previous ratings we want to extract some structure out of this matrix. Because of its enormous size, we want to somehow `compress` it, to get the same patterns represented by a much smaller object.

We can write a Matrix $A \in \mathbb{R}^{m \times n}$ with [Rank](03%20Linear%20Maps%20as%20Matrices.md#Rank%20of%20a%20Matrix) $r$ as:
$$
A = U \cdot \Sigma \cdot V^T
$$
where $U \in \mathbb{R}^{m \times m}$, $V \in \mathbb{R}^{n\times n}$ and $\Sigma \in \mathbb{R}^{m \times n}$ is [“diagonal”](Matrizen.md#Bezeichnungen) 
$$
\Sigma = \left(\begin{array}{}
\sigma_1 & 0 & \dots & 0 \\
0 & \sigma_2 & \dots & 0 \\ 
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \dots & \sigma_r \\ 
0 & 0 & 0 & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \dots & 0 \\
\end{array}\right) \text{or} 
 
 \left(\begin{array}{}
 \sigma_1 & 0 & \dots & 0 & 0 & \dots & 0 \\
 0 & \sigma_2 & \dots & 0 & 0 & \dots & 0 \\
 \vdots & \vdots & \ddots & \vdots & \vdots &  & \vdots \\
 0 & 0 & \dots & \sigma_r & 0 & \dots & 0 \\
 \end{array}\right) 
$$

$\Sigma$ has the same shape as $A$ and exactly the first $r$ of the diagonal values $\sigma_1, \sigma_2 \dots$  are non-zero. 

> [!Warning] Not all values on the diagonal
> Since $r$ depends on the [Rank](03%20Linear%20Maps%20as%20Matrices.md#Rank%20of%20a%20Matrix) and not only on the size of the matrix, the diagonal of $\Sigma$ does not need to be filled until the edge.
> In the general case where $r < n$ and $r<m$ The matrix $\Sigma$ has empty rows and columns


## Singular Values











