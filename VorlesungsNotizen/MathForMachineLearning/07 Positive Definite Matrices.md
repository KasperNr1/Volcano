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

# Gram Matrices
A matrix $A$ is called a `Gram Matrix` if there exists a set of vectors $v_1, v_2, \dots v_n$ such that:
$$
a_{ij} = \left<v_i, v_j\right>
$$

> [!NOTE] Additional Properties
> On $\mathbb{C}^{n\times n}$ Gram matrices are [Hermitian](06%20Orthogonal%20basis%20and%20projections.md#Symmetric%20matrices)
> On $\mathbb{R}^{n\times n}$ Gram matrices are [Symmetric](06%20Orthogonal%20basis%20and%20projections.md#Symmetric%20matrices)



$$
\frac{e^x - e^{-x}}{e^{x} + e^{-x}} = R
$$




















