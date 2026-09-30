# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
H_0=
\begin{pmatrix}
1&1\\
1&2
\end{pmatrix},
\qquad
H_1=
\begin{pmatrix}
\frac{1}{2}&1\\
1&4
\end{pmatrix},
\qquad
H_t=(1-t)H_0+tH_1
\quad(0\leq t\leq1).
$$
For a fixed symmetric positive definite preconditioner $P$ and step size $\eta>0$, consider the gradient iteration
$$
x_{k+1}=(I-\eta PH_t)x_k,
$$
where the unknown parameter $t$ is fixed but may be any value in $[0,1]$.

Define
$$
\rho_{\mathrm{full}}
=
\inf_{\substack{P\succ0\\ \eta>0}}
\max_{0\leq t\leq1}r(I-\eta PH_t),
$$
where $r(\cdot)$ denotes spectral radius. Define also
$$
\rho_{\mathrm{diag}}
=
\inf_{\substack{P\succ0\ \mathrm{diagonal}\\ \eta>0}}
\max_{0\leq t\leq1}r(I-\eta PH_t).
$$
Determine the ordered pair $(\rho_{\mathrm{full}},\rho_{\mathrm{diag}})$ exactly.

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

The problem asks for the best worst-case convergence factor of preconditioned gradient descent over a continuous family of quadratic Hessians, first with an unrestricted positive definite preconditioner and then with a diagonal one. The main task is robust preconditioner and step-size design for an iterative optimization method, so the primary sub-domain is Numerical optimization.
