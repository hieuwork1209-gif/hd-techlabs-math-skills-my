# Normalized Math Problem

## LaTeX (Normalized)

For a parameter $\gamma\in[\frac92,\frac{28}{5}]$, define
$$
E_\gamma=[1,2]\cup[\gamma,6].
$$
Consider four successive Richardson steps for a real symmetric positive-definite system,
$$
x^{(1)}=(I-\alpha A)x^{(0)},\qquad
x^{(2)}=(I-\beta A)x^{(1)},\qquad
x^{(3)}=(I-\delta A)x^{(2)},\qquad
x^{(4)}=(I-\eta A)x^{(3)},
$$
with $\alpha,\beta,\delta,\eta>0$. Their worst-case four-step Euclidean contraction factor over spectra contained in $E_\gamma$ is
$$
\mathcal C_\gamma(\alpha,\beta,\delta,\eta)
=\max_{\lambda\in E_\gamma}
\left|(1-\alpha\lambda)(1-\beta\lambda)(1-\delta\lambda)(1-\eta\lambda)\right|.
$$
Let $\mathcal C_\gamma^*$ be the minimum over positive $\alpha,\beta,\delta,\eta$, and let $p_\gamma^*$ be the unique minimizing quartic. Define
$$
\mathcal A_\gamma=\{\lambda\in E_\gamma:|p_\gamma^*(\lambda)|=\mathcal C_\gamma^*\}.
$$

As $\gamma$ increases from $\frac92$ to $\frac{28}{5}$, there are exactly two interior values
$$
\frac92<\gamma_1<\gamma_2<\frac{28}{5}
$$
at which the active-set pattern changes. Determine $\gamma_1$ and $\gamma_2$ exactly. Your reasoning must also identify $\mathcal A_\gamma$ on each of the three open regimes and describe the active set at each transition.

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

This problem asks for exact minimax tuning of a four-step nonstationary Richardson iteration under a moving spectral gap and for the phase transitions in the extremal eigenvalues controlling the worst-case contraction. The primary task is algorithmic parameter optimization in Optimization and Numerical Mathematics and Numerical optimization; polynomial equioscillation and Hermite interpolation are proof tools rather than the main classification target.
