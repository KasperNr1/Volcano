# Vectorspace
## Definition Vectorspace
Let $F$ be a [field](Gruppen%20Ringe%20und%20Körper.md#Feld) with Operations $\bigoplus, \bigodot$.
A vector space over the field $F$ is a set $V$ with two mappings:
- $+:V\times V \to V$ (Vector Addition)
- $\cdot : V \times V \to V$ (Vector Multiplikation)
such that 
1. $(V,+)$ is a [commutative group](Gruppen%20Ringe%20und%20Körper.md#Gruppe) 
2. Multiplicative identity: $\forall v \in V: 1\cdot v = v$
3. Associativity of scalar multiplication: $\forall a,b \in F$ and $\forall v \in V: (a \bigodot b) \cdot v = a \cdot (b \cdot v)$
4. Distributive Properties $\forall a, b \in F$ and $\forall u, v \in V$

Elements of $V$ are called vectors, elements of $F$ are called scalars.


> [!Info] Complex vector spaces
> Some literature uses the word ‘complex vector space’ to refer to vector spaces where $F = \mathbb{C}$

## Subspaces
Let $V$ be a [Vectorspace](#Vectorspace), $U \subset V$ non-empty set.
We call $U$ a subspace of $V$ if it is closed under linear combinations:
$$
\forall \lambda, \mu \in F \quad \forall u,v \in U : \quad\lambda \cdot u + \mu \cdot v \in U
$$
Meaning that all linear combinations of elements of a space are themselves contained by the space. 

> [!Info] Notation
> The notation $A \subset B$ allows for $A=B$ (Usually $A \subseteq B$).
> To denote strictly smaller sets $A \subsetneq B$ is used (usually $A \subset B$)

## Linear Combinations
Let $V$ be a [Vectorspace](#Definition%20Vectorspace) over a [Field](Gruppen%20Ringe%20und%20Körper.md#Feld) $F, u_1, \ldots , u_n \in V$ and $\lambda_1, \ldots, \lambda_n \in F$ 
Then a linear combination is any combination of Vectors and Factors.
$$
\sum_{i=1}^{n} \lambda_i u_i
$$

## Span
The set of all linear combinations is called the Span (linear hull) of $u_1, \ldots, u_n$:
$$
\text{span}(u_1, \ldots, u_n) := \left\{ \sum_{i=1}^{n} \lambda_i u_i \mid \lambda_i \in F \right\}
$$
The [set](Intervalle%20und%20Mengen.md#Mengen) $U := \left\{u_1, \ldots, u_n\right\}$ is called the `generator of` $\text{span}(U)$ 

## Linear Independence
A set of vectors $v_1, \ldots, v_n$ is called `linearly independent` if the following holds:
$$
\sum_{i=1}^{n} \lambda_i u_i = 0 \quad \Rightarrow \quad \lambda_1 = \ldots = \lambda_n = 0 
$$
Meaning that no vector can be expressed as a [linear Combination](#Linear%20Combinations) of any other vectors in the set

- Any set of $d+1$ vectors in $\mathbb{R}^d$ is not linearly independant
- Any set that contains the 0-vector is not linearly independant

## Basis
A subset $B$ of a vector space $V$ is called a (Hamel) basis if:
1. $\text{span}(B) = V$
2. $B$ is [linearly independant](#Linear%20Independence)

As an example:
One basis of $\mathbb{R}^3$ is: $\left(\begin{array}{c} 1 \\ 0 \\ 0 \end{array}\right), \left(\begin{array}{c} 0 \\ 1 \\ 0 \end{array}\right), \left(\begin{array}{c} 0 \\ 0 \\ 1 \end{array}\right)$
