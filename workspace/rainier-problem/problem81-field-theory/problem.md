# Normalized Math Problem

## LaTeX (Normalized)

Let $r\ge5$ and $\ell=2r+1$ be primes, with $2$ generating $\mathbb F_\ell^\times$. Put $Q=\ell^r$, and suppose $q,q+2Q,q+4Q$ are prime with $2q\equiv1\pmod Q$. Let $G=\mathbb F_\ell^r$, let $\zeta$ be a primitive $\ell$th root of unity, and for $f:G\to\mathbb Z_{\ge0}$ define
$$
\widehat f(y)=\sum_{x\in G}f(x)\zeta^{x\cdot y}.
$$
Let $P(s_1,\ldots,s_r)=(s_2,\ldots,s_r,s_1)$.

Determine the number of pairs $(s,f)$ with $s\in(\mathbb F_\ell^\times)^r$ and $f:G\to\mathbb Z_{\ge0}$ such that
$$
\sum_x f(x)=2q^2,\qquad \sum_x f(x)x=Ps,
$$
$$
\mathbf1\in\operatorname{span}\{s,Ps+P^{-1}s\},\qquad \sum_js_j=r,
$$
and, with cyclic indices,
$$
\prod_j(s_j-1)=2,\qquad \prod_js_j=4,\qquad
\sum_j(s_j+s_{j+1}-2)^2=-1.
$$
There are also subspaces $W\subset U\subset G$ of codimensions $2,1$ such that for every $0\le t<r$,
$$
P^ts,\quad P^t(Ps-s),\quad P^t(2\mathbf1-s)\in U\setminus W,
$$
and
$$
|\widehat f(y)|=
\begin{cases}
q+4Q,&0\ne y\in U^\perp,\\
q+2Q,&y\in W^\perp\setminus U^\perp,\\
q,&y\notin W^\perp
\end{cases}
\qquad(y\ne0).
$$
Here $U^\perp=\{y\in G:y\cdot U=0\}$. Give a closed formula.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Abstract Algebra |
| **Sub-domain** | Field theory |
| **Problem Type** | Exact computation |
| **Answer Type** | Exact symbolic expression |

---

## Domain Explanation

Cyclotomic phase rigidity fixes the Fourier phases. A cyclic quadratic-energy constraint couples the reciprocal frequency to the two product conditions, while the three incidence orbits form the affine part of a projective conic together with selected secant directions. Thus Field theory is the appropriate sub-domain.
