# Normalized Math Problem

## LaTeX (Normalized)

Let $p$ be an odd prime and let
$$
G=\mathbb F_p^3\times\mathbb F_p^3\times\mathbb F_p
$$
with multiplication
$$
(u,v,t)(u',v',t')=(u+u',v+v',t+t'+u\cdot v'),
$$
where $u\cdot v'$ is the standard dot product on $\mathbb F_p^3$. Let
$$
\mathcal O=\{Q\in GL_3(\mathbb F_p):Q^TQ=I\}
$$
act on $G$ by
$$
Q\cdot(u,v,t)=(Qu,Qv,t).
$$
Determine the number of $\mathcal O$-orbits of abelian subgroups $A\le G$ of order $p^4$ such that
$$
Z(G)\le A,
$$
$$
A\cap\bigl(\mathbb F_p^3\times\{0\}\times\mathbb F_p\bigr)=Z(G),\qquad
A\cap\bigl(\{0\}\times\mathbb F_p^3\times\mathbb F_p\bigr)=Z(G),
$$
and
$$
\left|A\cap\{(u,u,t):u\in\mathbb F_p^3,\ t\in\mathbb F_p\}\right|=p^2.
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Abstract Algebra |
| **Sub-domain** | Group theory |
| **Problem Type** | Exact computation |
| **Answer Type** | Exact symbolic expression |

---

## Domain Explanation

The problem asks for symmetry classes of maximal abelian subgroups in a finite nonabelian prime-power group under a natural orthogonal automorphism group. Passing to the quotient by the center turns the subgroups into Lagrangian graphs, while orbit counting requires classifying the resulting self-adjoint operators up to orthogonal conjugacy rather than merely counting matrices. The primary objects are subgroups, automorphisms, and their orbits, so Abstract Algebra -> Group theory is the appropriate classification.
