# Normalized Math Problem

## LaTeX (Normalized)

Let $n\ge2$ be an integer and let $\alpha,\beta\in\mathbb C$. Define the real trigonometric polynomial
$$
P_{\alpha,\beta}(\theta)
=1+2\operatorname{Re}\!\left(\alpha e^{i\theta}+\beta e^{in\theta}\right).
$$
Among all pairs $(\alpha,\beta)$ for which
$$
P_{\alpha,\beta}(\theta)\ge0
$$
for every real $\theta$, determine the largest possible value of $|\alpha|$ and, when this maximum is attained, determine $\beta$ in terms of $\alpha$.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Analysis |
| **Sub-domain** | Harmonic analysis |
| **Problem Type** | Optimization |
| **Answer Type** | Tuple or ordered list |

---

## Domain Explanation

This problem is primarily Analysis and Harmonic analysis: it asks for a sharp extremal Fourier coefficient in a globally nonnegative trigonometric polynomial with frequency support $\{0,\pm1,\pm n\}$. The extremal magnitude is controlled by the zero lattice of the $n$th mode, while equality forces a compatible relative Fourier phase and a global positivity certificate.
