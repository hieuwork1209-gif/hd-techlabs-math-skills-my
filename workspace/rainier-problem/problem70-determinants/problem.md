# Normalized Math Problem

## LaTeX (Normalized)

For integers $n\ge2$, real $a>0$ and $\lambda\in\mathbb R$, define
$$
T_r(n,a,\lambda)=\sum_{q=1}^3 e^{q-1+\lambda(q-2)^2}
\sum_{k=0}^{n^q}\frac{(-1)^k\binom{n^q}{k}}{(k+a)^r},\qquad 1\le r\le5.
$$
Put $L=\log n$ and, with all $T_r$ evaluated at $(n,a,\lambda)$, set
$$
\Delta_n=\det\!\left[(i+j)!T_{i+j+1}\right]_{i,j=0}^2,
\qquad \Lambda_n=2T_1T_3-T_2^2,
$$
$$
\Omega_n=-6T_1^2T_4+6T_1T_2T_3-2T_2^3,
$$
$$
\Psi_n=24T_1^3T_5-24T_1^2T_2T_4-12T_1^2T_3^2
+24T_1T_2^2T_3-6T_2^4.
$$
For all sufficiently large $n$, let $(a_n,\lambda_n)$ be the unique pair satisfying
$$
|a_nL-1|<L^{-1},\qquad |\lambda_n|<L^{-1},
$$
$$
60L^2T_1^2\Lambda_n+144LT_1\Omega_n+27\Psi_n+44L^4T_1^4=0,
$$
$$
81T_1\Delta_n+2238L^4T_1^2\Lambda_n-324L^3T_1\Omega_n-135L^2\Psi_n
-1206L^2\Lambda_n^2-1454L^6T_1^4=0.
$$
Determine
$$
\lim_{n\to\infty}L^{4/3}(a_nL-1).
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Linear Algebra |
| **Sub-domain** | Determinants |
| **Problem Type** | Parameter identification |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

The Hankel determinant is coupled to a deformation of the three Beta weights. The two invariant equations have a singular Jacobian at the limiting point, so the parameter deformation and the Gamma correction must be resolved together before the fractional root scale appears.
