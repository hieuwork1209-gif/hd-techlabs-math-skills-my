# Normalized Math Problem

## LaTeX (Normalized)

For each $c\in\mathbb R$ and $\varepsilon\geq0$, define
$$
\Lambda_c(\varepsilon)=
\min_{\substack{P\in\mathbb R[x]\text{ monic of degree }6\\
\text{the }x^3\text{-coefficient of }P\text{ is }\varepsilon\\
\text{the }x\text{-coefficient of }P\text{ is }\left(-\frac19+c\varepsilon\right)\varepsilon}}
\max_{-1\leq x\leq1}\frac{|P(x)|}{\sqrt{1+120x^2}}.
$$
The right derivative $\Lambda_c'(0+)$ exists, and the limit
$$
G(c)=\lim_{\varepsilon\to0+}
\frac{\Lambda_c(\varepsilon)-\Lambda_c(0)-\Lambda_c'(0+)\varepsilon}{\varepsilon^2}
$$
exists for every real $c$. Determine $G(c)$ exactly for all real $c$.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Optimization and Numerical Mathematics |
| **Sub-domain** | Approximation theory |
| **Problem Type** | Symbolic derivation |
| **Answer Type** | Function or mapping |

---

## Domain Explanation

This problem is a weighted minimax polynomial approximation problem. Its main structure comes from extremal contacts, alternation-type identities, dual certificates, and perturbation of the optimal polynomial, so it belongs to Optimization and Numerical Mathematics, specifically Approximation theory. The second-order sensitivity calculation measures the perturbation of an approximation-theoretic extremal value rather than the stability of a numerical algorithm.
