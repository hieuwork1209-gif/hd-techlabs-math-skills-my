# Normalized Math Problem

## LaTeX (Normalized)

For $\tau>0$, define
$$
V(\tau)=\max_{\substack{X\in\mathbb S_+^5\\ X_{11}=\cdots=X_{55}=1}}
\left[
\frac12(1-X_{12})
+\frac12(1-X_{23})
+(1-X_{34})
+(1-X_{45})
+\frac\tau2(1-X_{51})
\right].
$$
Let
$$
\tau_c=\sup\{\tau>0:V(\tau)=6\}.
$$
Determine exactly
$$
\left(\tau_c,
\lim_{h\downarrow0}
\frac{V(\tau_c+h)-V(\tau_c)}{h^2}
\right).
$$

Your reasoning must prove that the limit exists, characterize the optimizer rank at $\tau_c$ and for $\tau>\tau_c$ sufficiently close to $\tau_c$, and justify that no higher-rank feasible Gram matrix can improve the value in that neighborhood.

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

This problem asks for the exact rank transition and second-order onset of the optimal value in a parameterized weighted semidefinite program. The main object is an SDP over correlation matrices, and the proof depends on its Gram geometry and local convex-optimization sensitivity, so the primary classification is Optimization and Numerical Mathematics and Convex optimization.
