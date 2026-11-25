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
## Singular Values
The singular values of a matrix $A$ are the non-negative roots of the [Eigenvalues](04%20Eigenvalues%20and%20Determinant.md#Eigenvalues) of $A^TA$ or $AA^T$

## Motivation SVD
The Singular values are always real and non-negative
They apply to square and rectangular matrices.
The [Rank of a Matrix](03%20Linear%20Maps%20as%20Matrices.md#Rank%20of%20a%20Matrix) determines the amount of singular values it has.
Motivation is the `Netflix Matrix` where each row is a user and each column represents a show. Most users only watch and rate a handful of shows, so the absolute majority of all entries in this matrix is $0$.
To recommend shows to new users based on their previous ratings we want to extract some structure out of this matrix. Because of its enormous size, we want to somehow `compress` it, to get the same patterns represented by a much smaller object.

## Definition SVD
We can write a Matrix $A \in \mathbb{R}^{m \times n}$ with [Rank](03%20Linear%20Maps%20as%20Matrices.md#Rank%20of%20a%20Matrix) $r$ as:
$$
A = U \cdot \Sigma \cdot V^T
$$
where $U \in \mathbb{R}^{m \times m}$, $V \in \mathbb{R}^{n\times n}$ are [Orthogonal Matrices](06%20Orthogonal%20basis%20and%20projections.md#Orthogonal%20Matrices) and $\Sigma \in \mathbb{R}^{m \times n}$ is [“diagonal”](Matrizen.md#Bezeichnungen) 
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

> [!Warning]+ Not all values on the diagonal
> Since $r$ depends on the [Rank](03%20Linear%20Maps%20as%20Matrices.md#Rank%20of%20a%20Matrix) and not only on the size of the matrix, the diagonal of $\Sigma$ does not need to be filled until the edge.
> In the general case where $r < n$ and $r<m$ The matrix $\Sigma$ has empty rows and columns

The values $\sigma_i$ are called the [Singular Values](#Singular%20Values) of $A$.

The `left singular vectors` are the [eigenvectors](Matrizen.md#Eigenwerte%20&%20Eigenvektoren) of $A^TA$ and the eigenvectors of $AA^T$ are called the `right singular vectors`.

The main idea is that we can represent the matrix as a product of its left singular vectors, its singular values and its right singular values.

![](SingularVectorDecomposition.png)

## Example SVD
$$
A = \left(
\begin{array}{}
0 & 1 & 0 \\
1 & 0 & 1 \\
\end{array}
\right)
$$

Because $A$ is of shape $2 \times 3$ the decomposition $A = U \cdot \Sigma \cdot V^T$ will have $U$ with shape $2 \times 2$, $\Sigma$ with $2 \times 3$ and $V$ with $3 \times 3$.

### Step 1: Find V and $\Sigma$ 
We compute the $3\times 3$ [Symmetric matrix](06%20Orthogonal%20basis%20and%20projections.md#Symmetric%20matrices) $A^TA$:
$$
A^TA = 
\left(\begin{array}{}
0 & 1 \\
1 & 0 \\
0 & 1 \\
\end{array}\right) 
\cdot 
\left(\begin{array}{}
0 & 1 & 0 \\
1 & 0 & 1 \\
\end{array}\right)
=
\left(\begin{array}{}
1 & 0 & 1 \\
0 & 1 & 0 \\
1 & 0 & 1 \\
\end{array}\right)
$$
The [Characteristic polynomial](04%20Eigenvalues%20and%20Determinant.md#Characteristic%20polynomial) of this matrix is 
$$
\lambda(\lambda -1)(\lambda - 2) = 0
$$
Giving the eigenvalues $\lambda_1 = 2$, $\lambda_2 =1$, $\lambda_3 = 0$

Now take the square root of those eigenvalues and construct $\Sigma$.
$$
\Sigma = 
\left(\begin{array}{}
\sqrt{2} & 0 & 0 \\
0 & \sqrt{1} & 0 \\
\end{array}\right)
= 
\left(\begin{array}{}
\sqrt{2} & 0 & 0 \\
0 & 1 & 0 \\
\end{array}\right)
$$

Calculating the corresponding [eigenvectors](Matrizen.md#Eigenwerte%20&%20Eigenvektoren) yields:
$$
\lambda_1 = 2 \to v_1 = \left(\begin{array}{}1 \\ 0 \\ 1 \end{array}\right) \\
\lambda_2 = 1 \to v_2 = \left(\begin{array}{}0 \\ 1 \\ 1\end{array}\right) \\
\lambda_3 = 0 \to v_3 = \left(\begin{array}{}1 \\ 0 \\ -1 \end{array}\right)
$$
After normalizing each vector, we use them as the columns for the matrix $V$.
$$
V = \left(\begin{array}{}
\frac{1}{\sqrt2} & 0 & \frac{1}{\sqrt2} \\
0 & 1 & 0 \\
\frac{1}{\sqrt2} & 0 & -\frac{1}{\sqrt2} \\
\end{array}\right)
$$

### Step 2: Find U
Since $U$ is a $2\times 2$ matrix and the [Rank](03%20Linear%20Maps%20as%20Matrices.md#Rank%20of%20a%20Matrix) of $A$ is $2$, both columns of $U$ come directly from 
$$
u_i = \frac{1}{\sigma_i} Av_i
$$
Giving
$$
u_1 = \frac{1}{\sqrt2} \left(\begin{array}{}0 & 1 & 0 \\ 1 & 0 & 1\end{array}\right) \cdot 
\left(\frac{1}{\sqrt2}\left(\begin{array}{} 1 \\ 0 \\ 1\end{array}\right)\right) 
= \frac{1}{2} \left(\begin{array}{}0 \\ 2 \end{array}\right) = \left(\begin{array}{}0 \\ 1 \end{array}\right)
$$
and 
$$
u_2 = \frac11 \left(\begin{array}{}0 & 1 & 0 \\ 1& 0 & 1 \end{array}\right) \cdot \left(\begin{array}{} 0 \\1 \\ 1 \end{array}\right) = \left(\begin{array}{}1 \\ 0 \end{array}\right)
$$
Combining them yields the matrix $U$ with
$$
U = \left(\begin{array}{} 0 & 1 \\ 1 & 0 \end{array}\right)
$$

> [!Tip] Faster calculation
> If $A$ is not square, we can save some time by using either $A^TA$ to find V and then calculate $U$ like in this example.
> Or if $AA^T$ happens to be smaller we can use it to calculate $U$ and then find $V$.
> 
> In this example, we had some extra work because we took the longer way.

### Step 3: Assemble result
Remember to [Transpose](Matrizen.md#Transponieren%20einer%20Matrix) $V$ before writing down the final result.
$$
A = U\Sigma V^T =
\underbrace{\left(\begin{array}{}
0 & 1 \\
1 & 0
\end{array}\right)}_\text{U}
\cdot
\underbrace{
\left(\begin{array}{}
\sqrt2 & 0 & 0 \\
0 & 1 & 0 
\end{array}\right)}_\Sigma
\cdot
\underbrace{
\left(\begin{array}{}
\frac{1}{\sqrt2} & 0 & \frac{1}{\sqrt2} \\
0 & 1 & 0 \\
\frac{1}{\sqrt2} & 0 & -\frac{1}{\sqrt2} \\
\end{array}\right)}_{\text{V}^T}
$$

## Rank-$k$-Approximation
Given the [SVD](#Singular%20Value%20Decomposition) $A = U \Sigma V^T$ where the entries $\sigma_1, \sigma_2 \dots$ are sorted in decreasing order, let $k \leq r$. 
We define a Matrix $A_k$ by the following procedure:

To build $A_k$:
- Take the first $k$ columns of $U$
- Take the first $k$ entries of $\Sigma$ 
- Take the first $k$ rows of $V^T$ 

![](RankKApproximation.png)

This results in a Matrix $A_k$ that uses fewer numbers than $A$ but keeps most of the patterns.
$A_k$ can also be written as
$$
A_k = \sum_{i=1}^{k} \sigma_i u_i v_i^T
$$
The resulting matrix has $\text{rank}(A_k) = k$

