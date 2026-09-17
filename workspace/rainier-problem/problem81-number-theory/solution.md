## Steps

Step 1: Reduce square units modulo $p^\alpha$ to quadratic residues modulo $p$

Let
$$
R_\alpha=\mathbb Z/p^\alpha\mathbb Z,
$$
and let $\rho:R_\alpha\to\mathbb F_p$ be reduction modulo $p$. A unit $w\in R_\alpha^\times$ is a square unit if and only if $\rho(w)$ is a nonzero square in $\mathbb F_p$. The forward implication is immediate. Conversely, if $\rho(w)=z_0^2$ with $z_0\ne0$, then Hensel lifting applied to $z^2-w$ works because $2z_0\not\equiv0\pmod p$.

Hence a $4$-subset of $R_\alpha$ is a clique in the square-unit graph exactly when its four reductions are distinct and form a $K_4$ in the Paley graph $P_p$. For each fixed $K_4$ downstairs, each of its four vertices has $p^{\alpha-1}$ independent lifts, so the number of lifted cliques is
$$
p^{4(\alpha-1)}.
$$
Thus if $k_4(P_p)$ denotes the number of $K_4$'s in the Paley graph,
$$
C_{p,\alpha}=p^{4\alpha-4}k_4(P_p).
$$

Step 2: Count $K_4$'s in the Paley graph

Let $\chi$ be the quadratic character of $\mathbb F_p$, extended by $\chi(0)=0$, and let
$$
\eta(t)=\begin{cases}
1,&t\ne0\text{ and }\chi(t)=1,\\
0,&\text{otherwise}.
\end{cases}
$$
Since $p\equiv1\pmod4$, one has $\chi(-1)=1$. The affine maps
$$
x\longmapsto sx+t,
\qquad \chi(s)=1,
$$
act transitively on the edges of $P_p$. Fix the edge $\{0,1\}$, and let $\kappa$ be the number of $K_4$'s containing it. Then $\kappa$ is the number of edges inside the common neighborhood of $0$ and $1$, so
$$
2\kappa
=
\sum_{x,y\in\mathbb F_p}
\eta(x)\eta(1-x)\eta(y)\eta(1-y)\eta(x-y).
$$
Write $\delta(t)=1$ for $t=0$ and $0$ otherwise. Then
$$
\eta(t)=\frac{1+\chi(t)-\delta(t)}2.
$$
Expanding the product and using
$$
\sum_t\chi(t)=0,
\qquad
\sum_t\chi((t-a)(t-b))=-1\quad(a\ne b),
$$
together with the terms forced by the delta functions, gives
$$
64\kappa=p^2-20p+81+H_p,
$$
where the only genuinely non-elementary term is
$$
H_p=
\sum_{x,y\in\mathbb F_p}
\chi\bigl(xy(1-x)(1-y)(x-y)\bigr).
$$

We now evaluate $H_p$. Let $\psi$ be a quartic character with $\psi^2=\chi$, and let
$$
J(\psi,\psi)=\sum_{t\in\mathbb F_p}\psi(t)\psi(1-t).
$$
The finite-field Clausen identity at $1$ is obtained by expanding the defining character sums and applying multiplicative-character orthogonality; in this specialization it reads
$$
H_p=J(\psi,\psi)^2+\overline{J(\psi,\psi)}^{\,2}.
$$
For completeness, the usual Gauss-Jacobi calculation gives
$$
J(\psi,\psi)\overline{J(\psi,\psi)}=p,
$$
and the primary quartic Jacobi sum satisfies
$$
J(\psi,\psi)\equiv1\pmod{2+2i}.
$$
Therefore, after replacing $\psi$ by its conjugate if necessary,
$$
J(\psi,\psi)=u+2vi
$$
up to an overall sign, where
$$
p=u^2+4v^2,
\qquad
u\equiv1\pmod4,
\qquad
v>0.
$$
The overall sign disappears after squaring. Consequently
$$
H_p
=2(u^2-4v^2)
=2p-16v^2.
$$
Substituting into the formula for $\kappa$ gives
$$
64\kappa
=p^2-18p+81-16v^2
=(p-9)^2-16v^2.
$$
Put
$$
\Delta_p=(p-9)^2-16v^2.
$$
Then
$$
\kappa=\frac{\Delta_p}{64}.
$$

The Paley graph has
$$
\frac{p(p-1)}4
$$
edges, and every $K_4$ contains $6$ edges. Double-counting pairs consisting of an edge and a $K_4$ containing it gives
$$
k_4(P_p)
=\frac1{6}\cdot\frac{p(p-1)}4\cdot\kappa
=\frac{p(p-1)\Delta_p}{1536}.
$$

Step 3: Lift the total clique count to $R_\alpha$

By Step 1,
$$
C_{p,\alpha}
=p^{4\alpha-4}\,k_4(P_p)
=\frac{p^{4\alpha-3}(p-1)\Delta_p}{1536}.
$$

Step 4: Impose the zero-sum condition by translation

The additive group of $R_\alpha$ acts on its $4$-subsets by translation. This action is free on $4$-subsets: if a nonzero translation fixed such a subset, that subset would be a union of cycles whose common length is the additive order of the translation, a positive power of the odd prime $p$ and therefore at least $5$, impossible for a set of size $4$.

Translation preserves the clique property. If a clique $S$ has vertex sum $\sigma(S)$, then
$$
\sigma(S+t)=\sigma(S)+4t.
$$
Because $4$ is invertible modulo $p^\alpha$, every translation orbit contains exactly one clique with vertex sum $0$, namely the translate by
$$
t=-\frac{\sigma(S)}4.
$$
Every orbit has $p^\alpha$ elements, so
$$
Z_{p,\alpha}=\frac{C_{p,\alpha}}{p^\alpha}
=\frac{p^{3\alpha-3}(p-1)\Delta_p}{1536}.
$$

Final Answer: $\boxed{\left(\frac{p^{4\alpha-3}(p-1)\Delta_p}{1536},\frac{p^{3\alpha-3}(p-1)\Delta_p}{1536}\right)}$

---

## Answer

$\left(\frac{p^{4\alpha-3}(p-1)\Delta_p}{1536},\frac{p^{3\alpha-3}(p-1)\Delta_p}{1536}\right)$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- quadratic residues modulo prime powers
- Paley graph clique counting
- quartic Jacobi sums
- finite-field Clausen identity
- translation orbits
