---
course: Math for Machine Learning
lecture: "8"
source: https://www.tml.cs.uni-tuebingen.de/teaching/2026_maths_for_ml/index.php
date: 2026-11-12
tags:
  - lecture
---

# Pseudo-Inverse
For rectangular matrices $A \in \mathbb{R}^{m\times n}$ a `pseudo-inverse` of $A$ is defined as the matrix $A^\# \in \mathbb{R}^{n \times m}$ which satisfies the following conditions:
1. $AA^\#A =A$ (Nealy inverse)
2. $A^\#AA^\# = A^\#$  (Nearly Inverse)
3. $\left(AA^\#\right)^T = AA^\#$ (Symmetry)
4. $\left(A^\#A\right)^T = A^\#A$ (Symmetry)

> [!NOTE] Possible Invertibility
> If $A$ were invertible, then the pseudo Inverse would be equivalent to its actual [inverse](03%20Linear%20Maps%20as%20Matrices.md#Invers%20of%20linear%20Maps) $A^\# = A^{-1}$ 

An example for a mapping $A$ without an inverse is one that looses a dimension by projecting the input into a lower dimensional space.
$$
A: \mathbb{R}^3 \to \mathbb{R}^2 \qquad A\left(\begin{array}{}x_1 \\ x_2 \\ x_3 \end{array}\right) = \left(\begin{array}{}x_1 \\ x_2 \end{array}\right)
$$
There is no way to reconstruct the third dimension accurately.
However, we can invent one specific reconstruction, such as setting $x_3 = 0$ with the pseudo-inverse.
$$
R: \mathbb{R}^2 \to \mathbb{R}^3 \qquad R\left(\begin{array}{}x_1 \\ x_2 \end{array}\right) = \left(\begin{array}{}x_1 \\ x_2 \\ 0 \end{array}\right)  
$$
A point $\left(\begin{array}{}1 \\ 1 \\ 1\end{array}\right)$ obviously becomes $\left(\begin{array}{}1 \\ 1 \\ 0\end{array}\right)$ after having $AR$ applied, which means $R$ is not an actual inverse of $A$.
However, applying $A$ once more yields the same result $\left(\begin{array}{}1 \\ 1 \end{array}\right)$ as just applying it once and never using the pseudo inverse.

## How to find a Pseudo-Inverse
For [diagonal matrices](Matrizen.md#Bezeichnungen) with shape $\mathbb{R}^{m \times n}$ their pseudo inverse is the matrix $A^\# \in \mathbb{R}^{n \times m}$ that has transposed shape and the values $\frac{1}{\lambda_1} \frac{1}{\lambda_2} \dots$ on its diagonal.

To find a pseudo inverse for all other matrices, the `Moore-Penrose pseudo-inverse` uses [Singular Value Decomposition](07%20Positive%20Definite%20Matrices%20and%20SVD.md#Singular%20Value%20Decomposition).
Let $A \in \mathbb{R}^{m \times n}, A = U \Sigma V^T$ its SVD. Then a pseudo inverse is given by:
$$
A^\# := V\Sigma^\#U^T
$$
With $\Sigma^\# \in \mathbb{R}^{n \times m}$ defined as 
$$
\Sigma_{ii}^{\#} = \left\{ \begin{array}{cl} \dfrac{1}{\Sigma_{ii}} & \text{if} \; \Sigma_{ii} \neq 0 \\ 0 & \text{else}\end{array} \right.
$$

> [!NOTE] Dimensions
> Note that the dimension of $\Sigma^\#$ is the transpose of $\Sigma$ and that $U$ and $V$ are flipped in the SVD.


# Trace
The trace of a `square` matrix $A \in \mathbb{R}^{n \times n}$ is defined as the sum of its diagonal elements.
$$
\text{tr}(A) = \sum_{i=1}^{n} a_{ii}
$$
The trace $\text{tr}: \mathbb{R}^{n \times n} \to \mathbb{R}$ is a [Linear operator](02%20Mappings.md#Linear%20Mappings).
In particular
$$
\text{tr}(A + B) = \text{tr}(A) + \text{tr}(B)
$$
and 
$$
\text{tr}(A \cdot B) = \text{tr}(B \cdot A)
$$
> [!Danger] But not
> $$
> \text{tr}(A \cdot B) = \text{tr}(A) \cdot \text{tr}(B)
> $$

The trace also does not depend on the [Basis](01%20Vectorspaces.md#Basis).


While the [Determinant](04%20Eigenvalues%20and%20Determinant.md#Determinant) $\det(A)$ is the `product` of [Eigenvalues](04%20Eigenvalues%20and%20Determinant.md#Eigenvalues), the Trace is the `sum` of all Eigenvalues.


> [!NOTE] Trace is a real number
> Even though some [Eigenvalues](04%20Eigenvalues%20and%20Determinant.md#Eigenvalues) can be complex for a [Matrix](03%20Linear%20Maps%20as%20Matrices.md#Definition%20of%20a%20Matrix) with only real values, the trace is always a real number.
> 
> This is because the eigenvalues come as the roots of the [Characteristic polynomial](04%20Eigenvalues%20and%20Determinant.md#Characteristic%20polynomial), which can be factored into linear or quadratic terms. While the linear terms only provide real solutions, the quadratic terms may introduce complex solutions.
> Due to the [quadratic formula](Gleichungen.md#Quadratische%20Gleichungen) those complex solutions are of the form $x = a \pm i\cdot b$.
> This way the complex parts cancel each other perfectly when summing over them.
> 


# TODO
Matrix Series 
Page 265 onwards

















