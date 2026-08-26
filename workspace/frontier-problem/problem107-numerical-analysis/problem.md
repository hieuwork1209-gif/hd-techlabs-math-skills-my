# Normalized Math Problem

## LaTeX (Normalized)

Fix $h>0$. For real coefficients $c_1,\ldots,c_6$, define the symmetric differentiation rule
$$
(D_h f)(0)=\frac{1}{h}\sum_{j=1}^{6}c_j\bigl(f(jh)-f(-jh)\bigr).
$$

Assume that $D_h$ is exact at the origin for every real polynomial $p$ of degree at most $6$ and also for the Fourier mode
$$
s_h(x)=\sin\left(\frac{\pi x}{2h}\right).
$$
Thus
$$
(D_h p)(0)=p'(0)
$$
for every such polynomial $p$, and
$$
(D_h s_h)(0)=s_h'(0).
$$

Among all coefficient vectors $(c_1,\ldots,c_6)$ satisfying these exactness conditions, determine the exact value of
$$
\min\sum_{j=1}^{6}|c_j|.
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Optimization and Numerical Mathematics |
| **Sub-domain** | Numerical analysis |
| **Problem Type** | Optimization |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

This problem optimizes a symmetric finite-difference differentiation rule under polynomial exactness and Fourier-mode exactness, which are part of Optimization and Numerical Mathematics and Numerical analysis.
The problem also uses absolute-value optimization and a dual certificate, which could resemble linear programming.
However, the primary object is a numerical differentiation stencil and the constraints encode accuracy and frequency response, so Numerical analysis is the best fit.
