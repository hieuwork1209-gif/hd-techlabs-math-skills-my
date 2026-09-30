# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
A=
\begin{pmatrix}
1&0\\
0&4
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
\frac{11}{2}&-\frac{7}{2}\\
-\frac{7}{2}&\frac{11}{2}
\end{pmatrix},
$$
and consider
$$
f(x)=\frac{1}{2}x^TAx,
\qquad
g(x)=\frac{1}{2}x^TBx.
$$
For $\gamma>0$, define the reflected proximal maps
$$
R_A(\gamma)=(I-\gamma A)(I+\gamma A)^{-1},
\qquad
R_B(\gamma)=(I-\gamma B)(I+\gamma B)^{-1},
$$
and the standard Douglas-Rachford iteration matrix
$$
T_\gamma=
\frac{1}{2}\left(I+R_B(\gamma)R_A(\gamma)\right).
$$
Let $r(\cdot)$ denote spectral radius.

For a real polynomial $F$ having exactly one zero in $(u,v)$, write
$$
\operatorname{root}(F;u,v)
$$
for that zero.

Determine the unique value of $\gamma>0$ minimizing $r(T_\gamma)$.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Optimization and Numerical Mathematics |
| **Sub-domain** | Numerical optimization |
| **Problem Type** | Optimization |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

The problem asks for the stepsize that gives the fastest asymptotic linear convergence of standard Douglas-Rachford splitting applied to two strongly convex quadratic terms with noncommuting Hessians. The requested object is an algorithm parameter obtained by minimizing the spectral radius of the iteration matrix, so the primary sub-domain is Numerical optimization.
