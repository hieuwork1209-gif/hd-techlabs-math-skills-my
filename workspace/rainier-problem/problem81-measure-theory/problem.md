# Normalized Math Problem

## LaTeX (Normalized)

Let
\[
\Omega=\{0,1\}^{\mathbb N}
\]
with its product Borel $\sigma$-algebra. For every integer $k\ge3$, define
\[
a_k=\frac1{k^2(\log k)^2},
\qquad
b_k=\frac1{k^4},
\qquad
c_k=\frac1{k^5},
\qquad
d_k=\frac1{k^2},
\qquad
e_k=\frac1{k^4}.
\]
Let $\mu,\nu,\lambda$ be Bernoulli product probability measures on $\Omega$ with coordinate laws
\[
\begin{array}{c|ccc}
\text{coordinate}&\mu(X_n=1)&\nu(X_n=1)&\lambda(X_n=1)\\ \hline
4k&a_k&b_k&b_k\\
4k+1&c_k&c_k&d_k\\
4k+2&e_k&d_k&e_k
\end{array}
\qquad(k\ge3),
\]
and suppose that at every remaining coordinate all three measures are fair Bernoulli:
\[
\mu(X_n=1)=\nu(X_n=1)=\lambda(X_n=1)=\frac12.
\]

Determine whether $\mu,\nu,\lambda$ are pairwise equivalent or whether some pair is mutually singular. In the pairwise equivalent case, put
\[
Z=\frac{d\mu}{d\nu},
\qquad
W=\frac{d\lambda}{d\nu},
\]
and define the joint Mellin transform
\[
M(s,t)=\int_\Omega Z^sW^t\,d\nu
\qquad(s,t\in\mathbb R).
\]

Determine exactly the real joint-moment domain
\[
\mathcal D
=\{(s,t)\in\mathbb R^2:M(s,t)<\infty\}.
\]
Your answer must specify which critical boundary faces are included and which are excluded.

Also determine the maximal open tube domain in $\mathbb C^2$ on which
\[
M(z,w)=\int_\Omega Z^zW^w\,d\nu
\]
is represented by a locally uniformly convergent coordinate product and is holomorphic.

Finally determine exactly
\[
\mathcal P_Z=\{p>0:Z\in L^p(\nu)\},
\qquad
\mathcal P_W=\{p>0:W\in L^p(\nu)\},
\]
\[
\mathcal R_\mu
=\left\{p>0:\frac{d\nu}{d\mu}\in L^p(\mu)\right\},
\qquad
\mathcal R_\lambda
=\left\{p>0:\frac{d\nu}{d\lambda}\in L^p(\lambda)\right\},
\]
and state exactly for which $p>0$ one has
\[
Z^{-1}W^{-1}\in L^p(\nu).
\]

Your derivation must exhibit the coordinatewise joint Mellin product and justify every critical face, including endpoint attainment or failure.

Return the exact tuple
\[
(\mathcal D,\mathcal P_Z,\mathcal P_W,\mathcal R_\mu,\mathcal R_\lambda).
\]

---

## Domain Classification

| Field | Value |
|---|---|
| Domain | Analysis |
| Sub-domain | Measure theory |
| Problem Type | Symbolic derivation |
| Answer Type | Tuple or ordered list |

---

## Domain Explanation

The problem concerns equivalence of infinite Bernoulli product measures, two Radon-Nikodym derivatives relative to a common reference measure, and the exact joint Mellin-integrability region of those densities. The main work is to combine Kakutani's criterion with coordinate likelihood products, identify three distinct critical faces with different endpoint behavior, and determine the maximal holomorphic tube domain. Thus Analysis -> Measure theory is primary.
