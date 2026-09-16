# Normalized Math Problem

## LaTeX (Normalized)

For $\gamma\in[3,\frac{18}{5}]$, define
$$
E_\gamma=[1,2]\cup\left[\gamma,\frac{15}{\gamma}\right].
$$
Consider four successive Richardson steps
$$
x^{(j)}=(I-\alpha_jA)x^{(j-1)},\qquad j=1,2,3,4,
$$
for a real symmetric positive-definite system, with
$$
\alpha_j>0,
\qquad
\alpha_1+\alpha_2+\alpha_3+\alpha_4=2.
$$
Their worst-case four-step contraction factor over spectra contained in $E_\gamma$ is
$$
\mathcal C_\gamma(\alpha_1,\alpha_2,\alpha_3,\alpha_4)
=\max_{\lambda\in E_\gamma}
\left|\prod_{j=1}^4(1-\alpha_j\lambda)\right|.
$$
Let $\mathcal C_\gamma^*$ be the minimum under the positivity and budget constraints, let $p_\gamma^*$ be the unique minimizing quartic, and define
$$
\mathcal A_\gamma
=\{\lambda\in E_\gamma:|p_\gamma^*(\lambda)|=\mathcal C_\gamma^*\}.
$$

As $\gamma$ increases from $3$ to $\frac{18}{5}$, there are exactly two interior values
$$
3<\gamma_1<\gamma_2<\frac{18}{5}
$$
at which the active-set pattern changes. Determine $\gamma_1$ and $\gamma_2$ exactly. Your reasoning must identify $\mathcal A_\gamma$ on each of the three open regimes and describe the active set at each transition.

If an algebraic number is specified as $\operatorname{root}_{(a,b)}(f)$, this means the unique real zero of $f\in\mathbb Z[x]$ in $(a,b)$.

Give the final answer as $(\gamma_1,\gamma_2)$.

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

This problem asks for exact minimax tuning of a budget-constrained four-step nonstationary Richardson iteration when both endpoints of one spectral component move reciprocally. The primary task is constrained algorithmic parameter optimization in Optimization and Numerical Mathematics and Numerical optimization; constrained equioscillation is the proof mechanism.
