# Normalized Math Problem

## LaTeX (Normalized)

Let $\Omega=(0,\pi)^2$, let $\eta\ge0$, and consider the Neumann problem
$$
-\Delta u=\lambda u+\eta u^2-u^3
\qquad\text{in }\Omega,
$$
$$
\partial_\nu u=0
\qquad\text{on }\partial\Omega.
$$
Study small nonzero solutions bifurcating from
$$
(u,\lambda)=(0,1).
$$
Put
$$
\delta=\lambda-1,
$$
and write the critical-mode part of $u$ as
$$
A\cos x+B\cos y.
$$

Derive the cubic Lyapunov-Schmidt system in the form
$$
0=A\left[-\delta+\alpha(\eta)A^2+\beta(\eta)B^2\right]
+\text{higher-order terms},
$$
$$
0=B\left[-\delta+\beta(\eta)A^2+\alpha(\eta)B^2\right]
+\text{higher-order terms}.
$$

Let $\eta_{\mathrm{ex}}>0$ be the value at which
$$
\alpha(\eta)=\beta(\eta),
$$
so that axial and diagonal branch selection becomes degenerate at cubic order. Let $\eta_{\mathrm{flip}}>0$ be the value at which
$$
\alpha(\eta)+\beta(\eta)=0,
$$
so that the diagonal branch changes the side of $\lambda=1$ on which it bifurcates.

Determine exactly
$$
\bigl(\alpha(\eta),\beta(\eta),\eta_{\mathrm{ex}},\eta_{\mathrm{flip}}\bigr).
$$
Also state, for $0\le\eta<\eta_{\mathrm{flip}}$ and sufficiently small $\delta>0$, whether the axial branches
$$
(A,B)=(r,0),(0,r)
$$
or the diagonal branches
$$
A=\pm B=r
$$
are the strict local minima of the quartic reduced energy on each side of $\eta_{\mathrm{ex}}$.

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

The problem asks for the local bifurcation normal form at a double Neumann eigenvalue, including the nonlinear feedback of slaved modes, the exchange of axial and diagonal branch selection, and the change of criticality of the diagonal branch. The essential work is a Lyapunov-Schmidt reduction and interpretation of the resulting $D_4$-equivariant amplitude equations, so Differential Equations and Dynamical Systems -> Bifurcation theory is primary.
