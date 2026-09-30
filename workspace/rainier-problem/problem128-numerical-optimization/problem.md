# Normalized Math Problem

## LaTeX (Normalized)

Let $H$ be a real symmetric positive definite matrix whose spectrum is contained in
$$
E=[1,2]\cup[5,6].
$$
Consider the heavy-ball iteration
$$
x_{k+1}=x_k-\alpha_{k+1}Hx_k+\beta(x_k-x_{k-1}),
$$
where $0\leq\beta<1$, the two positive step sizes $\alpha_1,\alpha_2$ are chosen in advance, and $\alpha_{k+2}=\alpha_k$.

For a scalar eigenvalue $\lambda$, define
$$
A_\alpha(\lambda)=
\begin{pmatrix}
1+\beta-\alpha\lambda & -\beta\\
1 & 0
\end{pmatrix},
\qquad
M(\lambda)=A_{\alpha_2}(\lambda)A_{\alpha_1}(\lambda),
$$
and let $r(B)$ denote the spectral radius of a matrix $B$.

Define the best two-step contraction factor
$$
\rho_2=
\inf_{\substack{0\leq\beta<1\\ \alpha_1,\alpha_2>0}}
\max_{\lambda\in E} r(M(\lambda)).
$$
Also define the stepwise-stable optimum
$$
\widehat\rho_2=
\inf_{\substack{0\leq\beta<1,\ \alpha_1,\alpha_2>0\\
\max_{\lambda\in E}r(A_{\alpha_i}(\lambda))\leq1\ (i=1,2)}}
\max_{\lambda\in E} r(M(\lambda)).
$$
Determine the ordered pair $(\rho_2,\widehat\rho_2)$ exactly.

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

The problem asks for exact worst-case convergence factors of a two-periodic heavy-ball method on quadratic objectives with a disconnected spectral set, both without and with per-step stability. The main task is to design iteration parameters that minimize the spectral radius of the two-step error propagator, so the primary sub-domain is Numerical optimization.
