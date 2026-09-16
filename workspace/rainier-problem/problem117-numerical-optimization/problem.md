# Normalized Math Problem

## LaTeX (Normalized)

For a parameter $\gamma\in[\frac92,\frac{11}{2}]$, define
$$
E_\gamma=[1,2]\cup[\gamma,6].
$$
Consider four successive Richardson steps for a real symmetric positive-definite system,
$$
x^{(j)}=(I-\alpha_jA)x^{(j-1)},\qquad j=1,2,3,4,
$$
with
$$
\alpha_j>0,
\qquad
\alpha_1+\alpha_2+\alpha_3+\alpha_4=2.
$$
Their worst-case four-step Euclidean contraction factor over spectra contained in $E_\gamma$ is
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

As $\gamma$ increases from $\frac92$ to $\frac{11}{2}$, there are exactly two interior values
$$
\frac92<\gamma_1<\gamma_2<\frac{11}{2}
$$
at which the active-set pattern changes. Determine $\gamma_1$ and $\gamma_2$ exactly, and also determine $\mathcal C_{9/2}^*$. Your reasoning must identify $\mathcal A_\gamma$ on each of the three open regimes and describe the active set at each transition.

At $\gamma=\frac{11}{2}$, let $m_*$ be the unique member of $\mathcal A_{11/2}\cap(1,2)$. Let
$$
Q(t)=q_4t^4+q_3t^3+q_2t^2+q_1t+q_0\in\mathbb Z[t]
$$
be the primitive minimal polynomial of $m_*$ with $q_4>0$. Determine $(q_4,q_3,q_2,q_1,q_0)$ as well.

Give the final answer as $(\gamma_1,\gamma_2,\mathcal C_{9/2}^*;q_4,q_3,q_2,q_1,q_0)$.

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

This problem asks for exact minimax tuning of a budget-constrained four-step nonstationary Richardson iteration under a moving spectral gap, including active-set phase transitions and exact algebraic endpoint data from both non-plateau branches. The primary task is constrained algorithmic parameter optimization in Optimization and Numerical Mathematics and Numerical optimization; coefficient-constrained polynomial approximation is the proof mechanism.