---
course: Math for Machine Learning
lecture: "2"
source: https://www.tml.cs.uni-tuebingen.de/teaching/2026_maths_for_ml/index.php
date: 2026-10-15
tags:
  - lecture
---
# Linear Mappings
## Definition
Let $U,V$ be a [Vectorspace](1%20Vectorspaces.md#Vectorspace) over $F$. A mapping $f: U \to V$ is called `linear` if $\forall u_1, u_2 \in U, \forall \lambda \in F:$
$$
\begin{align}{}
f(u_1 + u_2) &= f(u_1) + f(u_2) \\
f(\lambda u_1) &= \lambda f(u_1)
\end{align}
$$
The set of all linear mappings from $U$ to $V$ is denoted $\mathcal{L}(U,V)$. If $U=V$ we write $\mathcal{L}(U)$

## Kernel and Range
$T \in \mathcal{L}(U,V)$ then the `kernel` or `null space` of the mapping $T$ is defined as:
$$
\text{ker}(T) := \text{null}(T) := \left\{ u \in U \mid T(u) = 0 \right\} \subset U
$$
This means that every element that gets mapped into the origin is part of the kernel.

![](KernelAndRange.png)

The `range` or `image` of $T$ is defined as:
$$
\text{range}(T) := \text{Im}(T) := \left\{ Tu \mid u \in U \right\} \subset V
$$
Every element of $V$ that can be reached by applying the mapping $T$ to any element of $U$ is part of the range.

Both, the $\text{kernel}(T)$ and the $\text{range}(T)$ are [subspaces](1%20Vectorspaces.md#Subspaces) of $V$.
- $T$ is [injective](Gruppen%20Ringe%20und%20Körper.md#Injektiv) $\Leftrightarrow \text{ker}(T)=0$ 
- $T$ is [surjective](Gruppen%20Ringe%20und%20Körper.md#Surjektiv) $\Leftrightarrow \text{range}(T)=V$ 

## Pre-Image
The pre-image of a set $V^\prime$ , is the set of elements $T^{-1}(V^\prime)$ that map to the elements of $V^{\prime}$.
$$
T^{-1}(V^\prime) := \left\{u \in U \mid T(u) \in V^\prime \right\}
$$
![](PreImage.png)

## Fundamental theorem for linear mappings
Let $V$ be finite-dimensional, $W$ any [VS](1%20Vectorspaces.md#Vectorspace) $T \in \mathcal{L}(V,W)$
Let $u_1, \dots, u_n$ be a basis of the [Kernel](#Kernel%20and%20Range) $\text{ker}(T) \subset V$
Let $w_1, \dots, w_m$ be a basis of $\text{range}(T) \subset W$
Let $z_1 \in T^{-1}(w_1), \dots, z_m \in T^{-1}(w_m)$ 

Then $u_1, \dots, u_n, z_1, \dots, z_m \subset V$ form a [basis](1%20Vectorspaces.md#Basis) of $V$.

In particular:
$$
\dim(V) = \dim(\ker(T)) + \dim(\text{range}(T))
$$

> [!NOTE] Equivalent statements
> $T \in \mathcal{L}(V,V)$ with $V$ finite-dimensional. Then the following three statements are equivalent:
> 1. $T$ is injective
> 2. $T$ is surjective
> 3. $T$ is bijective
