# Normalized Math Problem

## LaTeX (Normalized)

Let $r\ge3$ and $\ell=2r+1$ be primes, with $2$ generating $\mathbb F_\ell^\times$. Put $Q=\ell^r$, and suppose $q,q+2Q,q+4Q$ are prime with $2q\equiv1\pmod Q$. Put $n=4q^2$. Let $K/\mathbb Q$ be Galois with group $S_n$, let $\zeta$ be a primitive $\ell$th root, assume $K\cap\mathbb Q(\zeta)=\mathbb Q$, and set $M=K(\zeta)$.

For $1\le j\le r$, choose $g_i^{(j)}\in K^\times$ equivariantly and $p_j\in\mathbb Q^\times$. With cyclic indices assume $\prod_i g_i^{(j)}=p_{j+1}$ and that in $M^\times/(M^\times)^\ell$ the only relations among their classes are $\sum_i[g_i^{(j)}]=[p_{j+1}]$. Choose $(\alpha_i^{(j)})^\ell=g_i^{(j)}$, $\rho_j^\ell=p_j$ with $\prod_i\alpha_i^{(j)}=\rho_{j+1}$. Set $L=M(\alpha_i^{(j)},\rho_j)$, $\Gamma=\operatorname{Gal}(L/\mathbb Q(\zeta))$, and $\pi_\sigma=\sigma|_M$.

Fix $\pi\in S_n$ consisting of $2q^2$ transpositions and put $\widetilde C_\pi=\{\tau\in\Gamma:\pi_\tau\in C_{S_n}(\pi)\}$. For $k\in\mathbb F_\ell^r$, let
$$
\Omega_k=\left\{\left(\zeta^{u_j}\rho_j^{k_j}\frac{\alpha_i^{(j)}}{\alpha_h^{(j)}}\right)_{j=1}^r:i\ne h,\ u\in\mathbb F_\ell^r\right\}.
$$

Determine the number of $\widetilde C_\pi$-conjugacy orbits of $\sigma\in\Gamma$ with $\pi_\sigma=\pi$ and $\sigma(\rho_j)\ne\rho_j$ for all $j$ such that for some flag $W\subset U\subset\mathbb F_\ell^r$ with codimensions $2,1$, the cycle type on $\Omega_k$ is constant on $W$, $U\setminus W$, and its complement. If the corresponding $2$-cycle counts are $C_W,C_U,C_O$, require
$$
C_W-C_U=8\ell^2Q(q+Q),\qquad C_U-C_O=8\ell Q(q+3Q).
$$
Writing $\sigma(\rho_j)=\zeta^{s_j}\rho_j$, let $P$ cyclically shift coordinates and set $c_s^{(t)}=(s_{1+t}/s_1,\ldots,s_{r+t}/s_r)$. Also require
$$
\mathbf1\in\operatorname{span}\{s,Ps+P^{-1}s\},\qquad \sum_js_j=r,\qquad \prod_j(s_j-1)=2,
$$
and $c_s^{(t)}\in U\setminus W$ for every $0\le t<r$. Give a closed formula.

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

Cyclic Kummer relations couple the block-label moment to the radical phases. The hidden Fourier flag is further constrained by a reciprocal-mode phase recurrence, a quadratic-character nonvanishing condition, and projective conic incidence, so Field theory remains the appropriate sub-domain.
