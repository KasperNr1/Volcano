# Definition of a Matrix
A Matrix has [rectangular Shape](Matrizen.md#Definition) with $m$ rows and $n$ columns

With a [Linear Map](2%20Mappings.md#Linear%20Mappings) $T \in \mathcal{L}(V,W)$ and $V, W$ being finite-dimensional [Vectorspaces](1%20Vectorspaces.md#Vectorspace) with the [Basis](1%20Vectorspaces.md#Basis) $v_1, \dots, v_n$ and $w_1, \dots, w_m$ respectively.

The Linear Map transforms a vector $v\in V$ into some vector $w \in W$ that can be written as a [Linear Combination](1%20Vectorspaces.md#Linear%20Combinations)  of the basis vectors in $W$.
$$
T(v) = T(\lambda_1v_1 + \ldots + \lambda_nv_n) = \mu_1w_2 + \ldots + \mu_mw_m
$$
Transformed basis vectors $v_i$ have their factors denoted as follows
$$
T(v_i) = a_{1i}w_1 + \ldots + a_{mj}w_m
$$
The resulting factors are written as the columns in the matrix.
$$
M(T) := 
\underbrace{
\left(
\begin{array}{}
a_{11} & \dots & a_{1j} & \dots & a_{1n} \\
\vdots & \vdots & \vdots & \vdots & \vdots \\
a_{m1} & \dots & a_{mj} & \dots & a_{mn} \\
\end{array}
\right)
}_{n\text{ columns, one for each basis Vector of }V}
\left\}
\begin{array}{l}
m\text{ rows, one }\\
\text{for each basis }\\
\text{vector of } W\\
\end{array}
\right. 
$$
This is the matrix of the Mapping $T$ with respect to the bases $v_1, \dots , v_n$ of $V$ and $w_1, \dots , w_n$ of $W$ 

## Using a Matrix to apply linear Maps
The result of $T(v)$ can now be expressed by a [matrix-vector multiplication](Matrizen.md#Multiplikation).
$$
\begin{align}{}
T(v) &= \sum_{j=1}^n \lambda_j T(v_j) \\
&= \sum_{j=1}^n \lambda_j \sum_{i=1}^m a_{ij}w_i \\
&= \sum_{j=1}^n \left(\sum_{i=1}^m a_{ij} \cdot \lambda_j\right)w_i \\
\end{align}
$$

## Notation
Let $T: V \to W$ be linear, let $\mathcal{B}$ be a basis of $V$ and $\mathcal{C}$ a basis of $V$.
$$
M(T, \mathcal{B}, \mathcal{C})
$$
Denotes the matrix corresponding to $T$ with respect to the bases $\mathcal{B}$ and $\mathcal{C}$ 

## Properties of Matrices
Let $U,V,W$ be [Vectorspaces](1%20Vectorspaces.md#Vectorspace) and consider the bases fixed. Let $S,T \in \mathcal{V}, \mathcal{W}$ 
Then:
- $\mathcal{M}(S + T) = \mathcal{M}(S) + \mathcal{M}(T)$ 
- $\mathcal{M}(\lambda S) = \lambda \mathcal{M}(S)$ 
- If $T: U \to V$ and $S: V \to W$ are linear, then
$$
\mathcal{M}(S \circ T) = \mathcal{M}(S) \cdot \mathcal{M}(T)
$$ 
> [!Warning] Order of Operations
> Note that to map $U \to W$ we must apply first $T$ then $S$, but the written notation reverses this order



