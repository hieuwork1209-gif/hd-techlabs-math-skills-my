# Normalized Math Problem

## LaTeX (Normalized)

For $\lambda>0$, consider positive solutions $u\in C^2([0,1])$ of
$$
u''+\lambda e^u=0,\qquad u(0)=u(1)=0,
$$
with $u(x)>0$ for $0<x<1$. For such a solution, let the Dirichlet linearization be
$$
L_{\lambda,u}v=v''+\lambda e^u v,\qquad v(0)=v(1)=0.
$$
Determine exactly the set of parameters $\lambda>0$ for which there exists a positive solution $u$ such that $L_{\lambda,u}$ has a nontrivial kernel.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Differential Equations and Dynamical Systems |
| **Sub-domain** | Bifurcation theory |
| **Problem Type** | Parameter identification |
| **Answer Type** | Set or multiset of objects |

---

## Domain Explanation

The problem asks for the parameter values at which the positive Bratu solution branch becomes degenerate, detected by a nontrivial kernel of the linearized boundary-value operator. Determining that parameter requires constructing the full nonlinear solution branch and locating the singular point of its linearization, which is the standard local mechanism of a fold bifurcation. Thus Differential Equations and Dynamical Systems -> Bifurcation theory is the primary classification.
