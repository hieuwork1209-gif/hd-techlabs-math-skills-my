# Normalized Math Problem

## LaTeX (Normalized)

Let $n\geq12$ satisfy $n\equiv0\pmod{12}$, and let $X$ be the set of all $3$-subsets of $\{1,\ldots,n\}$. Define the integer matrix $L_n=(\ell_{S,T})_{S,T\in X}$ by
$$
\ell_{S,T}=\begin{cases}
3(n-3),&S=T,\\
-1,&|S\cap T|=2,\\
0,&\text{otherwise}.
\end{cases}
$$
Put
$$
m=\binom n2,\qquad q=m-2n+1,\qquad r=\binom n3-2m+n,
$$
and
$$
c=3(n-2),\qquad b=2(n-1)c,\qquad a=\frac n4b.
$$
Determine the Smith normal form of $L_n$ over $\mathbb Z$, with the invariant factors written in divisibility order.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Linear Algebra |
| **Sub-domain** | Matrix decompositions and canonical forms |
| **Problem Type** | Canonicalization or normalization |
| **Answer Type** | Canonical form |

---

## Domain Explanation

The problem asks for the Smith normal form of a canonical integer matrix indexed by 3-subsets. Rational eigenvalues alone do not determine the answer: the integral reduction produces four different small Smith blocks, and their 2- and 3-primary parts must be recombined in divisibility order. The central task is therefore an integral matrix canonical-form computation.
