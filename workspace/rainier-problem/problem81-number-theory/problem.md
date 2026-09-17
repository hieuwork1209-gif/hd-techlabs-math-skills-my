# Normalized Math Problem

## LaTeX (Normalized)

Let $p\equiv1\pmod4$ be a prime and let $\alpha\ge2$. Choose the unique integers $u,v$ with
$$
p=u^2+4v^2,
\qquad
u\equiv1\pmod4,
\qquad
v>0,
$$
and put
$$
\Delta_p=(p-9)^2-16v^2.
$$

Let
$$
R_\alpha=\mathbb Z/p^\alpha\mathbb Z.
$$
Call a unit $w\in R_\alpha^\times$ a square unit if
$$
w=z^2
$$
for some $z\in R_\alpha^\times$. Define a graph $G_{p,\alpha}$ with vertex set $R_\alpha$ by joining distinct vertices $x,y$ exactly when $x-y$ is a square unit.

Let $C_{p,\alpha}$ be the number of unordered $4$-element subsets of $R_\alpha$ whose vertices are pairwise adjacent in $G_{p,\alpha}$. Let $Z_{p,\alpha}$ be the number of those $4$-cliques satisfying
$$
\sum_{x\in S}x=0
\qquad\text{in }R_\alpha.
$$

Determine exactly
$$
(C_{p,\alpha},Z_{p,\alpha}).
$$

---

## Domain Classification

| Field | Value |
|---|---|
| Domain | Number Theory |
| Sub-domain | Quadratic residues and reciprocity |
| Problem Type | Exact computation |
| Answer Type | Tuple or ordered list |

---

## Domain Explanation

The graph is defined by quadratic-residue conditions on unit differences modulo an odd prime power. The essential exact count reduces to a Paley-graph $K_4$ character sum whose evaluation uses quartic Jacobi sums and the representation $p=u^2+4v^2$; the prime-power lifting and zero-sum translation orbit are subsequent arithmetic refinements. Thus Number Theory -> Quadratic residues and reciprocity is the primary classification.
