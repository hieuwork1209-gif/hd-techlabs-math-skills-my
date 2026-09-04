# Normalized Math Problem

## LaTeX (Normalized)

Let $r\ge3$, let $q$ be a prime satisfying $2q\equiv1\pmod{3^r}$, and put $n=4q^2$. Let $K/\mathbb Q$ be Galois with $\operatorname{Gal}(K/\mathbb Q)\cong S_n$ acting on $[n]$, let $\omega\notin K$ be a primitive cube root of unity, and put $M=K(\omega)$.

For $1\le j\le r$, choose $g_i^{(j)}\in K^\times$ $(1\le i\le n)$ such that $\tau(g_i^{(j)})=g_{\tau(i)}^{(j)}$ for every $\tau\in S_n$, and choose $p_j\in\mathbb Q^\times$. Assume
$$
\prod_{j=1}^r p_j^{s_j}\prod_{i=1}^n\prod_{j=1}^r(g_i^{(j)})^{a_i^{(j)}}\in(M^\times)^3
$$
for $a_i^{(j)},s_j\in\mathbb F_3$ if and only if every $s_j=0$ and, for each $j$, the values $a_i^{(j)}$ are constant in $i$.

Choose $(\alpha_i^{(j)})^3=g_i^{(j)}$ and $\rho_j^3=p_j$, with $\prod_i\alpha_i^{(j)}\in M$ for every $j$, and let
$$
L=M\left(\alpha_i^{(j)},\rho_j:1\le i\le n,\ 1\le j\le r\right).
$$
For $\sigma\in\operatorname{Gal}(L/\mathbb Q(\omega))$, let $\pi_\sigma\in S_n$ be its restriction to $M$.

Fix $\pi\in S_n$ consisting of $2q^2$ transpositions. For $k=(k_1,\ldots,k_r)\in\mathbb F_3^r$, let
$$
\Omega_k=\left\{\left(\omega^{u_j}\rho_j^{k_j}\frac{\alpha_i^{(j)}}{\alpha_\ell^{(j)}}\right)_{j=1}^r:i\ne\ell,\ u=(u_1,\ldots,u_r)\in\mathbb F_3^r\right\}.
$$
The relation hypothesis implies these elements are distinct.

Determine the number of $\sigma\in\operatorname{Gal}(L/\mathbb Q(\omega))$ such that $\pi_\sigma=\pi$, $\sigma(\rho_j)\ne\rho_j$ for every $j$, and the $3^r$ induced permutations on the sets $\Omega_k$ all have the same cycle type. Give a closed formula in $r$ and $q$.

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

The problem asks for the number of lifts of a fixed permutation through a family of cubic Kummer extensions. The cube-class relation space determines the Kummer Galois kernel and the admissible lifts; the higher-dimensional finite Fourier and affine-hyperplane incidence arguments classify their phase profile only after this field-theoretic reduction, so Field theory is the appropriate sub-domain.