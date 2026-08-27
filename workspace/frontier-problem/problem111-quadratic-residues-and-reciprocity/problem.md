# Normalized Math Problem

## LaTeX (Normalized)

Let $\ell$ be a prime with $\ell\equiv1\pmod4$, and put
$$
V=\mathbb F_\ell^2,\qquad m=\ell^2,\qquad q=7^m.
$$
Fix an $\mathbb F_7$-basis $(\beta_v)_{v\in V}$ of $\mathbb F_q$ satisfying
$$
\sum_{v\in V}\beta_v=1.
$$
Thus every $a\in\mathbb F_q$ has unique coordinates
$$
a=\sum_{v\in V}a_v\beta_v,\qquad a_v\in\mathbb F_7.
$$
Let $\chi$ be the quadratic character of $\mathbb F_\ell$, extended by $\chi(0)=0$. Let $\mathscr H$ be the set of three-element subsets $\{u,v,w\}\subset V$ satisfying
$$
\chi\bigl(\det(v-u,w-u)\bigr)=1.
$$
This is independent of the ordering because $\chi(-1)=1$.

For variables $z_1,z_2,z_3$, define
$$
\Psi(z_1,z_2,z_3)
=
\sum_{\{i,j,k\}=\{1,2,3\}}
(z_j-z_i)^2(z_k-z_i)^4,
$$
where the sum is over the six ordered triples of distinct indices. For $a\in\mathbb F_q$, define
$$
\mathcal A(a)=\sum_{v\in V}a_v^4,
\qquad
\mathcal C(a)=\sum_{\{u,v,w\}\in\mathscr H}\Psi(a_u,a_v,a_w).
$$

Call $F\in\mathbb F_q[X]$ translation-admissible if
$$
\prod_{a\in\mathbb F_q}
\left(Z-F(X+a)+F(X)\right)=Z^q-Z
\quad\text{in }\mathbb F_q(X)[Z].
$$
For any $F\in\mathbb F_q[X]$, put
$$
\nu(F)=
\left|
\left\{v\in V:F(X+\beta_v)-F(X)=\beta_v\right\}
\right|.
$$
Let $\mathscr S$ be the set of translation-admissible polynomials satisfying
$$
F(1)=1,
$$
$$
\mathcal A(F(a))=\mathcal A(a),
\qquad
\mathcal C(F(a))=\mathcal C(a)
\qquad(a\in\mathbb F_q),
$$
and the coupled degree condition
$$
\deg F<q^2\quad\text{if }\nu(F)>0,
\qquad
\deg F<q\quad\text{if }\nu(F)=0.
$$
Determine $|\mathscr S|$.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Number Theory |
| **Sub-domain** | Quadratic residues and reciprocity |
| **Problem Type** | Symbolic derivation |
| **Answer Type** | Exact symbolic expression |

---

## Domain Explanation

This problem involves quadratic characters over prime fields and square classes of determinants, which are part of Number Theory and Quadratic residues and reciprocity.
The problem also involves finite field polynomials, affine maps, and hypergraph automorphisms, which are part of algebra and combinatorics.
However, those structures organize the counting argument, while the quadratic residue condition defines the central incidence relation.
