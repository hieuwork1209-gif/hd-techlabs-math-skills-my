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

For any positive solution \(u\), define its Dirichlet linearization
\[
\mathcal L_u\phi
=-\phi''-3\lambda(1+u)^2\phi,
\qquad
\phi(0)=\phi(1)=0.
\]
Its Morse index is the number of negative eigenvalues of \(\mathcal L_u\), counted with multiplicity, and its nullity is \(\dim\ker\mathcal L_u\).

For \(0<\lambda<\lambda_*\), there are two positive solutions. Call them \(u_{\rm small}\) and \(u_{\rm large}\) according to their maximum amplitudes. Determine exactly:

1. the Morse index of \(u_{\rm small}\);
2. the Morse index of \(u_{\rm large}\);
3. the Morse index and nullity of the fold solution \(u_*\).

Also determine the exact number of positive solutions for each regime
\[
0<\lambda<\lambda_*,
\qquad
\lambda=\lambda_*,
\qquad
\lambda>\lambda_*.
\]

It is acceptable to specify a transcendental constant as the unique real root of an explicit one-variable integral equation together with an isolating interval.

Your derivation must:

- prove that every positive solution is symmetric about \(x=1/2\);
- reduce all positive solutions to an exact one-parameter branch;
- prove that this branch has exactly one fold;
- prove spectrally, rather than by a turning-point slogan alone, the Morse-index classification on both branches;
- identify the one-dimensional kernel at the fold.

Return the exact tuple
\[
(\lambda_*,A_*,m_{\rm small},m_{\rm large},\nu_*),
\]
where \(m_{\rm small}\), \(m_{\rm large}\) are the two branch Morse indices and \(\nu_*\) is the fold nullity.

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

The problem asks for the complete positive-solution structure of a nonlinear two-point Dirichlet boundary value problem, including the exact fold parameter, critical amplitude, solution multiplicity, and the Dirichlet Morse index of each branch. The phase-plane reduction and boundary conditions determine the global branch, while Sturm-Liouville analysis of the boundary-value linearization provides the spectral classification. Thus Differential Equations and Dynamical Systems -> Boundary value problems is primary; the stability calculation is subordinate to the boundary-value problem itself.
