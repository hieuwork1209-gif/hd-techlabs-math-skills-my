# Normalized Math Problem

## LaTeX (Normalized)

Let $r\ge2$, and put
$$
h=\gcd(r,2),
\qquad
\epsilon=
\begin{cases}
1,&4\mid r,\\
0,&4\nmid r.
\end{cases}
$$
Let $C$ be the smooth projective curve whose function field is
$$
\mathbb C(x)(y,z),
$$
where
$$
y^r=x(x-1),
\qquad
z^r=x(x+1).
$$
The rule
$$
\tau(x,y,z)=(-x,z,y)
$$
defines an involution of $C$.

Determine exactly the genus of the quotient curve
$$
C/\langle\tau\rangle.
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Topology and Geometry |
| **Sub-domain** | Algebraic geometry |
| **Problem Type** | Symbolic derivation |
| **Answer Type** | Exact symbolic expression |

---

## Domain Explanation

The problem concerns a finite cover of the projective line, its normalization, an algebraic involution induced by a symmetry of the branch locus, and the genus of the resulting quotient curve. The essential work is to combine ramification data for the Kummer fiber product with a local analysis of fixed points on the normalized curve and then apply Riemann-Hurwitz to the quotient. Thus Algebraic geometry is the primary classification.
