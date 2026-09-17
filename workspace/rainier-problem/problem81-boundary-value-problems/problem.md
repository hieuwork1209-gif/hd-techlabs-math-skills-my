# Normalized Math Problem

## LaTeX (Normalized)

For \(\lambda>0\), consider the nonlinear Dirichlet boundary value problem
\[
-u''(x)=\lambda(1+u(x))^3,
\qquad 0<x<1,
\]
with
\[
u(0)=u(1)=0,
\qquad
u(x)>0\quad(0<x<1).
\]

Determine exactly the critical parameter \(\lambda_*>0\) for which positive solutions exist precisely when
\[
0<\lambda\le\lambda_*.
\]
Also determine exactly the critical maximum amplitude
\[
A_*=\max_{0\le x\le1}u_*(x)
\]
of the unique positive solution \(u_*\) at \(\lambda=\lambda_*\).

In addition, determine the exact number of positive solutions for each of the three regimes
\[
0<\lambda<\lambda_*,
\qquad
\lambda=\lambda_*,
\qquad
\lambda>\lambda_*.
\]

It is acceptable to specify a transcendental constant as the unique real root of an explicit one-variable integral equation together with an isolating interval.

Your derivation must prove that every positive solution is symmetric about \(x=1/2\), reduce the problem to an exact one-parameter branch, and prove that this branch has exactly one fold.

Return the exact pair
\[
(\lambda_*,A_*).
\]

---

## Domain Classification

| Field | Value |
|---|---|
| Domain | Differential Equations and Dynamical Systems |
| Sub-domain | Boundary value problems |
| Problem Type | Exact computation |
| Answer Type | Tuple or ordered list |

---

## Domain Explanation

The problem asks for the complete positive-solution bifurcation diagram of a nonlinear two-point Dirichlet boundary value problem, including the exact fold parameter, the critical solution amplitude, and the number of solutions on each side of the fold. The essential work is the phase-plane first integral, symmetry of positive solutions, an exact amplitude parameterization, and a global uniqueness proof for the turning point. Thus Differential Equations and Dynamical Systems -> Boundary value problems is primary.
