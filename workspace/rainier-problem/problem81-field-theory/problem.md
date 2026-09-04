# Normalized Math Problem

## LaTeX (Normalized)

Let $\ell$ be an odd prime such that $2$ generates $\mathbb F_\ell^\times$, let $r\ge2$, and let $q$ be a prime satisfying
$$
2q\equiv1\pmod{\ell^r}.
$$
Put $n=4q^2$. Let $K/\mathbb Q$ be Galois with $\operatorname{Gal}(K/\mathbb Q)\cong S_n$ acting on $[n]$. Let $\zeta$ be a primitive $\ell$th root of unity, assume
$$
K\cap\mathbb Q(\zeta)=\mathbb Q,
$$
and put $M=K(\zeta)$.

For $1\le j\le r$, choose $g_i^{(j)}\in K^\times$ $(1\le i\le n)$ such that
$$
\tau(g_i^{(j)})=g_{\tau(i)}^{(j)}
$$
for every $\tau\in S_n$, and choose $p_j\in\mathbb Q^\times$. Assume
$$
\prod_{j=1}^r p_j^{s_j}
\prod_{i=1}^n\prod_{j=1}^r(g_i^{(j)})^{a_i^{(j)}}\in(M^\times)^\ell
$$
for $a_i^{(j)},s_j\in\mathbb F_\ell$ if and only if every $s_j=0$ and, for each $j$, the values $a_i^{(j)}$ are constant in $i$.

Choose
$$
(\alpha_i^{(j)})^\ell=g_i^{(j)},\qquad \rho_j^\ell=p_j,
$$
with $\prod_i\alpha_i^{(j)}\in M$ for every $j$, and let
$$
L=M\left(\alpha_i^{(j)},\rho_j:1\le i\le n,\ 1\le j\le r\right).
$$
For $\sigma\in\operatorname{Gal}(L/\mathbb Q(\zeta))$, let $\pi_\sigma\in S_n$ be its restriction to $M$.

Fix $\pi\in S_n$ consisting of $2q^2$ transpositions. For
$$
k=(k_1,\ldots,k_r)\in\mathbb F_\ell^r,
$$
let
$$
\Omega_k=
\left\{
\left(
\zeta^{u_j}\rho_j^{k_j}
\frac{\alpha_i^{(j)}}{\alpha_h^{(j)}}
\right)_{j=1}^r
:
i\ne h,\ u=(u_1,\ldots,u_r)\in\mathbb F_\ell^r
\right\}.
$$
The relation hypothesis implies these elements are distinct.

Determine the number of $\sigma\in\operatorname{Gal}(L/\mathbb Q(\zeta))$ such that
$$
\pi_\sigma=\pi,
\qquad
\sigma(\rho_j)\ne\rho_j\quad(1\le j\le r),
$$
and the $\ell^r$ induced permutations on the sets $\Omega_k$ all have the same cycle type. Give a closed formula in $\ell,r,q$.

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

The problem asks for the number of lifts of a fixed permutation through prime-degree Kummer extensions over a cyclotomic field. The cube-specific Eisenstein argument is replaced by a cyclotomic norm and inert-prime analysis in $\mathbb Q(\zeta_\ell)$ before the resulting phase profile can be classified by finite Fourier and affine-hyperplane methods, so Field theory is the appropriate sub-domain.