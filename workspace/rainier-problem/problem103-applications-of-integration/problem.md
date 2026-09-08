# Normalized Math Problem

## LaTeX (Normalized)

For $n\ge1$, define
$$
M_n=\iint_{|x|^{2/3}+|y|^{2/3}\le1}
 e^{-n((x-1)^2+y^2)}\,dx\,dy.
$$
Here
$$
\Gamma(s)=\int_0^\infty t^{s-1}e^{-t}\,dt.
$$
Evaluate
$$
\lim_{n\to\infty}n^{7/4}
\left(M_n-\frac{\sqrt6\,\Gamma(1/4)}{18n^{5/4}}\right).
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Calculus |
| **Sub-domain** | Applications of integration |
| **Problem Type** | Exact computation |
| **Answer Type** | Real number |

---

## Domain Explanation

The Gaussian is centered at the cusp $(1,0)$ of the astroid $|x|^{2/3}+|y|^{2/3}=1$. Near that cusp, horizontal and vertical scales are different: $1-x$ is of order $n^{-1/2}$ while $y$ is of order $n^{-3/4}$. The requested correction comes from the interaction between the next term in the cusp geometry and the vertical Gaussian decay, making this a natural anisotropic asymptotic-integration problem.
