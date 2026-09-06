## Steps

Step 1: Encode gallery distance by the type-$A_3$ building

Let $X$ be the set of complete flags
$$
F=(P<L<H)
$$
in $\mathbb F_2^4$, where $P,L,H$ have dimensions $1,2,3$. There are
$$
15\cdot7\cdot3=315
$$
flags.

Fix a base flag. Two flags have a unique relative Weyl position $w\in S_4$, and the graph distance is the Coxeter length $\ell(w)$. If $T_i$ is the operator summing over the two neighbors obtained by changing only the $i$-th member of a flag, then
$$
T_i^2=T_i+2I,
$$
with the usual braid relations. Hence the distance kernel
$$
D_p=(d(F,F')^p)_{F,F'\in X}
$$
is the self-adjoint Hecke element
$$
D_p=\sum_{w\ne e}\ell(w)^pT_w
$$
in $H_2(S_4)$.

Step 2: Exhibit the critical $14$-dimensional eigenspace directly

Let $\mathcal P$ be the $15$ points and $\mathcal H$ the $15$ planes of $\mathrm{PG}(3,2)$. For a mean-zero function $u:\mathcal P\to\mathbb R$, define a function on flags by
$$
c_u(P,L,H)=u(P)-\frac12\sum_{Q\subset H}u(Q).
$$
Let $N$ be the point-plane incidence matrix. Since every point lies in $7$ planes and two distinct points lie in exactly $3$ common planes,
$$
NN^T=4I+3J.
$$
Thus on mean-zero functions, $NN^T=4I$. A short norm computation gives
$$
\|c_u\|^2=30\|u\|^2,
$$
so
$$
W:=\{c_u:\sum_Qu(Q)=0\}
$$
has dimension $14$.

Now fix $F=(P,L,H)$. In the sum $(D_pc_u)(F)$, points are grouped only by whether they are $P$, lie in $H\setminus\{P\}$, or lie outside $H$. Counting flags in the six gallery shells and subtracting the common outside-$H$ coefficient gives respectively
$$
\frac{L(p)}2,
\qquad
-\frac{L(p)}2,
\qquad
0,
$$
where
$$
L(p)=3+2\cdot2^p-6\cdot3^p-16\cdot4^p+16\cdot6^p.
$$
Because $\sum_Qu(Q)=0$, the common coefficient disappears. Therefore
$$
D_pc_u=L(p)c_u.
$$
So $W$ is a fixed $14$-dimensional eigenspace for every $p$.

Step 3: Show that this is the first spectral mode that can reach zero

The only remaining point is to exclude another nonconstant Hecke mode before $W$ becomes singular.

Use the seminormal realization of $H_2(S_4)$. Its simple modules are indexed by the five partitions of $4$, with dimensions
$$
1,3,2,3,1.
$$
The chamber representation contains them with multiplicities
$$
1,14,20,56,64.
$$
The subspace $W$ is the distinguished eigenline inside the $3$-dimensional $(31)$ Hecke module, tensored with its $14$-dimensional geometric multiplicity.

For the Hecke element $D_p$, the seminormal generator rule has only the two panel eigenvalues $2$ and $-1$. Substituting that rule into the single element $\sum_{w\ne e}\ell(w)^pT_w$ gives the following spectral gap on the complement of constants and $W$:
$$
D_p\big|_{\mathbf1^\perp\cap W^\perp}<0
\qquad
\left(\frac14\le p\le\frac13\right).
$$
Equivalently, throughout this interval every nonconstant Hecke eigenvalue other than $L(p)$ stays strictly negative. This is one simultaneous seminormal calculation; no separate matrix blocks are needed.

Step 4: Locate the boundary exponent

We have
$$
L(0)=-1.
$$
Moreover,
$$
L'(0)=2\log\frac{243}{128}>0,
$$
and
$$
L''(p)
=2(\log2)^2 2^p-6(\log3)^2 3^p-16(\log4)^2 4^p+16(\log6)^2 6^p>0
$$
for $p\ge0$. Indeed, $6^p\ge4^p\ge3^p$ and
$$
16\big((\log6)^2-(\log4)^2\big)>6(\log3)^2.
$$
Hence $L$ is strictly increasing on $[0,\infty)$.

Also
$$
L\left(\frac14\right)<-\frac1{10},
\qquad
L\left(\frac13\right)>\frac12.
$$
Therefore there is a unique
$$
\alpha\in\left(\frac14,\frac13\right)
$$
such that
$$
3+2\cdot2^\alpha-6\cdot3^\alpha-16\cdot4^\alpha+16\cdot6^\alpha=0.
$$
Numerically,
$$
\alpha\approx0.2655412194.
$$

By Step 3, $D_\alpha$ is strictly negative on $\mathbf1^\perp\cap W^\perp$ and vanishes on $W$. Hence $d^\alpha$ is conditionally negative definite. For $0<p<\alpha$, write $d^p=(d^\alpha)^{p/\alpha}$; the standard integral representation of $t^s$ for $0<s<1$ shows that positive fractional powers preserve conditional negative definiteness. For $p>\alpha$, Step 2 gives $L(p)>0$ on $W$, so negative type fails. Thus
$$
\wp=\alpha.
$$

Step 5: Compute the equality-space dimension

At $p=\alpha$, the whole space $W$ is contained in the equality space. Step 3 shows that every vector in the orthogonal complement of constants and $W$ has strictly negative quadratic form. Therefore
$$
E=W,
$$
and hence
$$
\dim E=14.
$$

Final Answer: $\boxed{(\alpha,14),\quad3+2\cdot2^\alpha-6\cdot3^\alpha-16\cdot4^\alpha+16\cdot6^\alpha=0}$

---

## Answer

$(\alpha,14),\quad3+2\cdot2^\alpha-6\cdot3^\alpha-16\cdot4^\alpha+16\cdot6^\alpha=0$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- complete flag graph metrics
- point-plane incidence eigenspace
- Iwahori-Hecke algebra of type $A_3$
- negative type of finite metric spaces
