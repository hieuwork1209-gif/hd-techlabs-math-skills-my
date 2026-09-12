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
| **Answer Type** | Exact scalar |

---

## Domain Explanation

The problem asks for the genus of a quotient of a smooth algebraic curve obtained from a fiber product of cyclic covers. Its essential structure is algebraic: normalization, inertia and ramification of the function-field extension, fixed points of an algebraic involution, and the quotient curve. Algebraic geometry is therefore more appropriate than geometric topology, because the decisive data come from valuations and ramification in algebraic function fields rather than from a purely topological classification of surfaces.
