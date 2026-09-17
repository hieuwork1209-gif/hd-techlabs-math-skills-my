# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
\Omega=(0,\pi)^2,
$$
and fix
$$
\eta=\frac3{\sqrt{22}}.
$$
Consider the Neumann problem
$$
-\Delta u=\lambda u+\eta u^2-u^3
\qquad\text{in }\Omega,
$$
$$
\partial_\nu u=0
\qquad\text{on }\partial\Omega.
$$
Put
$$
\delta=\lambda-1,
$$
and write the critical-mode part of a small solution as
$$
A\cos x+B\cos y.
$$
Assign weighted degrees
$$
\operatorname{wt}(A)=\operatorname{wt}(B)=1,
\qquad
\operatorname{wt}(\delta)=2.
$$
At this value of $\eta$, the cubic Lyapunov-Schmidt system is radially degenerate:
$$
0=A\left[-\delta+\frac{12}{11}(A^2+B^2)\right]+O_{\mathrm w}(5),
$$
$$
0=B\left[-\delta+\frac{12}{11}(A^2+B^2)\right]+O_{\mathrm w}(5).
$$

Carry the Lyapunov-Schmidt reduction through weighted degree $5$ and write it in the form
$$
0=A\Bigl[
-\delta+\frac{12}{11}(A^2+B^2)
-\delta(pA^2+qB^2)
+rA^4+sA^2B^2+tB^4
\Bigr]
+O_{\mathrm w}(7),
$$
$$
0=B\Bigl[
-\delta+\frac{12}{11}(A^2+B^2)
-\delta(qA^2+pB^2)
+tA^4+sA^2B^2+rB^4
\Bigr]
+O_{\mathrm w}(7).
$$
Determine exactly
$$
(p,q,r,s,t).
$$

Let $V(A,B)$ be the normalized reduced potential whose gradient is the displayed amplitude system. For
$$
A=\rho\cos\theta,
\qquad
B=\rho\sin\theta,
$$
minimize $V$ with respect to $\rho$ for each fixed $\theta$ and sufficiently small $\delta>0$. Write the resulting angular energy as
$$
V_{\min}(\theta)
=-\frac{11}{48}\delta^2
+\delta^3\left(
C_0+C_1\cos^2\theta\sin^2\theta
\right)
+O(\delta^4).
$$
Determine exactly
$$
(C_0,C_1),
$$
and state whether the higher-order reduction selects the axial directions
$$
(A,B)=(r,0),(0,r)
$$
or the diagonal directions
$$
A=\pm B=r.
$$

Return the exact tuple
$$
(p,q,r,s,t,C_0,C_1).
$$

---

## Domain Classification

| Field | Value |
|---|---|
| Domain | Differential Equations and Dynamical Systems |
| Sub-domain | Bifurcation theory |
| Problem Type | Symbolic derivation |
| Answer Type | Tuple or ordered list |

---

## Domain Explanation

The problem sits exactly at a cubic degeneracy of a bifurcation from a double Neumann eigenvalue. The cubic normal form no longer selects a branch direction, so one must perform a weighted fifth-order Lyapunov-Schmidt reduction, including parameter-dependent slaved-mode feedback, and then compare the higher-order reduced energy along the $D_4$-symmetric axial and diagonal directions. Thus Differential Equations and Dynamical Systems -> Bifurcation theory is primary.
