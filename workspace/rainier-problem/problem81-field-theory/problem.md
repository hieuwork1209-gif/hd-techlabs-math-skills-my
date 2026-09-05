# Normalized Math Problem

## LaTeX (Normalized)

Let $\ell\ge5$ be prime with $2$ generating $\mathbb F_\ell^\times$, let $r\ge2$, put $Q=\ell^r$, and let $q$ be prime such that $2q\equiv1\pmod Q$ and $q+2Q$ is prime. Put $n=4q^2$. Let $K/\mathbb Q$ be Galois with group $S_n$ on $[n]$, let $\zeta$ be a primitive $\ell$th root of unity, assume $K\cap\mathbb Q(\zeta)=\mathbb Q$, and set $M=K(\zeta)$.

For $1\le j\le r$, choose $g_i^{(j)}\in K^\times$ with $\tau(g_i^{(j)})=g_{\tau(i)}^{(j)}$ and $p_j\in\mathbb Q^\times$. Assume
$$
\prod_jp_j^{s_j}\prod_{i,j}(g_i^{(j)})^{a_i^{(j)}}\in(M^\times)^\ell
$$
iff every $s_j=0$ and, for each $j$, the $a_i^{(j)}$ are constant in $i$. Choose $(\alpha_i^{(j)})^\ell=g_i^{(j)}$, $\rho_j^\ell=p_j$, with $\prod_i\alpha_i^{(j)}\in M$, and set $L=M(\alpha_i^{(j)},\rho_j)$. For $\sigma\in\operatorname{Gal}(L/\mathbb Q(\zeta))$, let $\pi_\sigma$ be its restriction to $M$.

Fix $\pi\in S_n$ consisting of $2q^2$ transpositions. For $k\in\mathbb F_\ell^r$, let
$$
\Omega_k=\left\{\left(\zeta^{u_j}\rho_j^{k_j}\frac{\alpha_i^{(j)}}{\alpha_h^{(j)}}\right)_{j=1}^r:i\ne h,\ u\in\mathbb F_\ell^r\right\}.
$$
These elements are distinct by the relation hypothesis.

Determine the number of $\sigma$ with $\pi_\sigma=\pi$ and $\sigma(\rho_j)\ne\rho_j$ for all $j$ for which there exists a codimension-one $\mathbb F_\ell$-subspace $U\subset\mathbb F_\ell^r$ such that all $\Omega_k$ with $k\in U$ have one cycle type, all $\Omega_k$ with $k\notin U$ have a second cycle type, and the first type has exactly $8\ell Q(Q+q)$ more $2$-cycles than the second. Give a closed formula in $\ell,r,q$.

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

The Kummer lift parameters reduce the cycle condition to a two-level autocorrelation spectrum. Two inert rational primes control the two Fourier magnitudes, while affine-hyperplane incidence is needed to align their phases and recover the integral label profile, so Field theory is the appropriate sub-domain.
