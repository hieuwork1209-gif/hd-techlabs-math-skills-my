# Normalized Math Problem

## LaTeX (Normalized)

For a parameter $\gamma\in[3,\frac{21}{4}]$, define
$$
E_\gamma=[1,2]\cup[\gamma,6].
$$
Consider four successive Richardson steps for a real symmetric positive-definite system,
$$
x^{(j)}=(I-\alpha_jA)x^{(j-1)},\qquad j=1,2,3,4,
$$
with
$$
\alpha_j>0,\qquad
\sum_{j=1}^4\alpha_j=2,
\qquad
\sum_{1\le i<j<k\le4}\alpha_i\alpha_j\alpha_k=\frac14.
$$
Their worst-case four-step Euclidean contraction factor over spectra contained in $E_\gamma$ is
$$
\mathcal C_\gamma(\alpha_1,\alpha_2,\alpha_3,\alpha_4)
=\max_{\lambda\in E_\gamma}
\left|\prod_{j=1}^4(1-\alpha_j\lambda)\right|.
$$
Let $\mathcal C_\gamma^*$ be the minimum under these constraints, let $p_\gamma^*$ be the unique minimizing quartic, and define
$$
\mathcal A_\gamma
=\{\lambda\in E_\gamma:|p_\gamma^*(\lambda)|=\mathcal C_\gamma^*\}.
$$

As $\gamma$ increases from $3$ to $\frac{21}{4}$, there are exactly two interior values
$$
3<\gamma_1<\gamma_2<\frac{21}{4}
$$
at which the active-set pattern changes. Determine $\gamma_1$ and $\gamma_2$ exactly. Your reasoning must also identify $\mathcal A_\gamma$ on each of the three open regimes and describe the active set at each transition.

For a polynomial $f$ having a unique real zero in $(a,b)$, write $\operatorname{root}_{(a,b)}(f)$ for that zero. Give the final answer as $(\gamma_1,\gamma_2)$.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Optimization and Numerical Mathematics |
| **Sub-domain** | Numerical optimization |
| **Problem Type** | Optimization |
| **Answer Type** | Tuple or ordered list |

---

## Domain Explanation

This problem asks for exact minimax tuning of a four-step nonstationary Richardson schedule under two symmetric step-invariant constraints and a moving spectral gap. The primary task is constrained algorithmic parameter optimization in Optimization and Numerical Mathematics and Numerical optimization; coefficient-constrained polynomial approximation is the proof mechanism.
