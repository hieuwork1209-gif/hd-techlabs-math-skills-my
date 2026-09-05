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
\mathbf1\in\operatorname{span}\{s,Ps+P^{-1}s\},\qquad \sum_js_j=r,\qquad \prod_j(s_j-1)=2,
$$
and there are subspaces $W\subset U\subset G$ of codimensions $2,1$ with $P^ts\in U\setminus W$ for every $0\le t<r$ and
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

The decisive rigidity comes from Fourier coefficients in the cyclotomic field $\mathbb Q(\zeta)$: inert rational primes force their phases, after which finite-field recurrence and projective incidence determine the count. Thus Field theory is the appropriate sub-domain.
