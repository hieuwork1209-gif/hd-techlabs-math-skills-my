# Normalized Math Problem

## LaTeX (Normalized)

For $\tau>0$, define
$$
V(\tau)=\max_{\substack{X\in\mathbb S_+^5\\ X_{11}=\cdots=X_{55}=1}}
\left[
\frac12\sum_{i=1}^4(1-X_{i,i+1})
+\frac\tau2(1-X_{5,1})
\right].
$$
Let
$$
\tau_c=\sup\{\tau>0:V(\tau)=4\}.
$$
Determine exactly
$$
\left(\tau_c,
\lim_{h\downarrow0}
\frac{V(\tau_c+h)-V(\tau_c)}{h^2}
\right).
$$

Your reasoning must prove that the limit exists, characterize the optimizer ranks on both sides of $\tau_c$, and justify that no higher-rank feasible Gram matrix can improve the value.

Give the final answer as an ordered pair.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Optimization and Numerical Mathematics |
| **Sub-domain** | Convex optimization |
| **Problem Type** | Optimization |
| **Answer Type** | Tuple or ordered list |

---

## Domain Explanation

This problem asks for the exact parameter at which a weighted semidefinite optimization problem changes optimizer rank, together with the second-order sensitivity of its optimal value at that transition. The central object is a parameterized SDP and its optimizer geometry, so the primary classification is Optimization and Numerical Mathematics, specifically Convex optimization.
