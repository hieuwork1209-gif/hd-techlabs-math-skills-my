# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
R=\mathbb Z/4096\mathbb Z,
$$
and let $G=GL_2(R)$ act on $M_2(R)$ by conjugation. Define
$$
\mathcal I=\{A\in M_2(R):A^2=I\}.
$$
Determine the number of $G$-orbits in $\mathcal I$.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Number Theory |
| **Sub-domain** | Modular arithmetic and congruences |
| **Problem Type** | Exact computation |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

The problem classifies solutions of the matrix congruence $A^2\equiv I\pmod{2^{12}}$ up to change of basis. The essential difficulty is the ramified lifting behavior at the prime $2$: reduction modulo $2$, idempotents over local rings, and conjugacy lifting through powers of $2$. Hence Number Theory -> Modular arithmetic and congruences is the primary classification.
