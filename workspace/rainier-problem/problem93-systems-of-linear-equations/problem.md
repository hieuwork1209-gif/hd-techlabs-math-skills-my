# Normalized Math Problem

## LaTeX (Normalized)

Let $p\geq 7$ be a prime and let $n$ be a positive power of $p$. Put
$$
q=\frac{n}{p},
\qquad
\Gamma=(\mathbb Z/n\mathbb Z)^3,
$$
with all coordinates read modulo $n$.

Let $V_n$ be the vector space over $\mathbb F_p$ of all functions
$$
f:\Gamma\to\mathbb F_p
$$
such that, for every $(x,y,z)\in\Gamma$,
$$
f(x+1,y,z)+f(x,y+1,z)+f(x,y,z+1)=3f(x,y,z),
$$
$$
f(x+1,y+1,z)+f(x,y+1,z+1)+f(x+1,y,z+1)=3f(x,y,z),
$$
and
$$
\begin{aligned}
&4\Bigl(
f(x+(p-1)q,y,z)+f(x,y+(p-1)q,z)+f(x,y,z+(p-1)q)
\Bigr)\\
&\quad-\Bigl(
f(x+(p-2)q,y,z)+f(x,y+(p-2)q,z)+f(x,y,z+(p-2)q)
\Bigr)\\
&=9f(x,y,z).
\end{aligned}
$$

Determine, in closed form as a function of $p$ and $n$,
$$
\boxed{\dim_{\mathbb F_p}V_n}.
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Linear Algebra |
| **Sub-domain** | Systems of linear equations |
| **Problem Type** | Symbolic derivation |
| **Answer Type** | Polynomial or rational function |

---

## Domain Explanation

This problem involves the dimension of a simultaneous solution space for homogeneous translation equations over a finite field, which are part of Linear Algebra and Systems of linear equations.
The problem also involves finite-field polynomial identities and cyclic shifts, which are part of algebra.
However, those identities are tools for reducing the linear system rather than the main classification of the problem.
