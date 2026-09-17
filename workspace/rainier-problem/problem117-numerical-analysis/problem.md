# Normalized Math Problem

## LaTeX (Normalized)

For $\tau>0$, let
$$
d\mu_\tau(x)=(1+\tau x^2)\,dx+\tau(\delta_{-1}+\delta_1)
$$
be the even positive measure on $[-1,1]$. Let
$$
\{-a_\tau,0,a_\tau\}
$$
be the nodes of its three-point Gaussian quadrature rule, i.e. the unique three-node rule exact for every polynomial of degree at most $5$.

Call $\tau$ compatible if there exist
$$
0<b<a_\tau
$$
and positive weights $A,B,C,D$ such that the symmetric seven-node rule
$$
Q(p)=A[p(-1)+p(1)]
+B[p(-b)+p(b)]
+C[p(-a_\tau)+p(a_\tau)]
+Dp(0)
$$
is exact for every polynomial of degree at most $11$.

Define
$$
P(t)=357975t^4+2668650t^3+3550150t^2+120890t-49049,
$$
and write $\operatorname{root}_{(u,v)}P$ for the unique zero of $P$ in $(u,v)$ whenever it exists.

Determine the unique compatible value of $\tau$ exactly.

Your reasoning must also determine $a_\tau$, $b$, and all four positive weights at the compatible parameter, and must prove uniqueness of the nested rule.

Give the final answer as $\tau$.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Optimization and Numerical Mathematics |
| **Sub-domain** | Numerical analysis |
| **Problem Type** | Symbolic derivation |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

This problem asks when a Gaussian quadrature rule for a parameterized positive measure admits a positive nested seven-node extension of degree $11$, and requires exact determination of the compatible nodes and weights. The primary mathematics is Gaussian and nested quadrature construction through parameter-dependent moment equations, which belongs to Optimization and Numerical Mathematics, specifically Numerical analysis.
