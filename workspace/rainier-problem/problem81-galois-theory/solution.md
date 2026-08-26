## Steps

Step 1: Determine the radical kernel and all lifts of the fixed permutation
Put $g_i=a+y_i$ and $M=K(\omega)$. The only quadratic subfield of the $S_n$-extension $K/\mathbb Q$ is $\mathbb Q(\sqrt{\Delta})$. Thus $-3\Delta\notin(\mathbb Q^\times)^2$ gives $K\cap\mathbb Q(\omega)=\mathbb Q$, so $\operatorname{Gal}(M/\mathbb Q(\omega))\cong S_n$.

Let $\mathcal R\subset\mathbb F_3^n$ consist of the vectors $e=(e_i)$ for which $\prod_i g_i^{e_i}$ is a cube in $M$. Since $\prod_i g_i=c^3$, the all-ones vector belongs to $\mathcal R$. If $\mathcal R$ contained a nonconstant vector, subtracting its image under a transposition of two unequal coordinates would put some nonzero multiple of $e_i-e_j$ in $\mathcal R$; $S_n$-stability would then put every coordinate difference in $\mathcal R$.

The factorization modulo $p$ gives a prime of $M$ whose residue field contains the two roots reducing to $u,v$ and has degree $n-2$ over $\mathbb F_p$ on the remaining orbit. A noncube $z\in\mathbb F_p^\times$ remains a noncube there, because $p\equiv1\pmod3$ and
$$
1+p+\cdots+p^{n-3}\equiv n-2\equiv2\pmod3.
$$
Hence the quotient of the $g_i$ reducing to $a+u$ by the $g_j$ reducing to $a+v$ is not a cube, contradicting the presence of every coordinate difference. Therefore
$$
\mathcal R=\langle(1,\ldots,1)\rangle.
$$
Also every $g_i$ is a unit at primes above $p$, whereas $v(p)=1$, so the class of $p$ is independent of the classes of the $g_i$.

Choose $\alpha_i^3=g_i$ with $\prod_i\alpha_i=c$, and choose $\eta^3=p$. The ratio classes generate all classes of the $g_i$: since $n\equiv1\pmod3$,
$$
\prod_{j\neq i}\frac{g_i}{g_j}=\frac{g_i^n}{c^3}
$$
has the same cube class as $g_i$. More explicitly, write $n=3h+1$ and choose roots $\gamma_{ij}=\alpha_i/\alpha_j$ of $x^3-B_{ij}$. Then
$$
\frac{c\prod_{j\neq i}\gamma_{ij}}{g_i^h}=\alpha_i.
$$
Thus the roots of $P_0$ generate all $\alpha_i$. Dividing a root $\eta\gamma_{ij}$ of $P_1$ by the corresponding root $\gamma_{ij}$ of $P_0$ recovers $\eta$ up to a power of $\omega$, and
$$
L=M(\alpha_1,\ldots,\alpha_n,\eta).
$$
The verified cube-class relations and the independence of $p$ let Kummer theory identify $\operatorname{Gal}(L/M)$ with the dual of an $n$-dimensional $\mathbb F_3$-space. Consequently every lift of the fixed $\pi$ that fixes $\omega$ is uniquely given by $\xi_1,\ldots,\xi_n,s\in\mathbb F_3$ with
$$
\sum_i\xi_i=0,
$$
through
$$
\sigma(\alpha_i)=\omega^{\xi_i}\alpha_{\pi(i)},
\qquad
\sigma(\eta)=\omega^s\eta.
$$

Step 2: Convert the three cycle types into orbit-phase conditions
The values $B_{ij}$ are distinct. Suppose $g_i/g_j=g_k/g_l$. If $i=k$ or $j=l$, then the other indices also agree. If $i,j,k,l$ are distinct, choose $m$ outside them and apply the transposition $(i\,m)$, which fixes $j,k,l$; comparison with the original equality gives $g_i=g_m$, impossible. If exactly one index is shared in the crossed position, for example $i=l$, move one of the two unshared indices while fixing the other two and compare again. For the reversed pair $(k,l)=(j,i)$, the equality gives $g_i^2=g_j^2$; moving $j$ through three distinct indices would force more than two distinct $g$-values to have the same square, again impossible. Thus $(i,j)=(k,l)$.

A root of $P_k$ has the form
$$
\omega^r\eta^k\frac{\alpha_i}{\alpha_j},
\qquad r\in\mathbb F_3,
\quad i\neq j.
$$
Let an orbit of the ordered pair $(i,j)$ under $\pi$ have length $d$. If $i$ lies in a cycle $C$ of length $r_C$ and $j$ lies in a cycle $D$ of length $r_D$, write
$$
x_C=\sum_{i\in C}\xi_i,
\qquad
x_D=\sum_{j\in D}\xi_j.
$$
For distinct cycles, one turn around the ordered-pair orbit accumulates the phase
$$
T=\frac{d}{r_C}x_C-\frac{d}{r_D}x_D.
$$
For two entries in the same cycle the accumulated phase is $0$. After one turn, the fiber coordinate is translated by $T+kds$. Hence that orbit contributes three $d$-cycles when $T+kds=0$, and one $3d$-cycle otherwise.

Write $C_1,\ldots,C_{2q^2}$ for the $2$-cycles and $D_1,\ldots,D_{15q^2}$ for the $5$-cycles, and set
$$
x_a=\sum_{i\in C_a}\xi_i,
\qquad
y_b=\sum_{i\in D_b}\xi_i.
$$
The ordered-pair orbit lengths are $2$, $5$, and $10$, producing the six distinct root-cycle lengths $2,6,5,15,10,30$. If $s=0$, the three actions are identical. If $s\neq0$, the three cycle types agree exactly when, separately for each base length, the phases $T$ are equally distributed among $0,1,2$.

Step 3: Express equidistribution by two Eisenstein norms and one orthogonality relation
Put
$$
X=\sum_{a=1}^{2q^2}\omega^{x_a},
\qquad
Y=\sum_{b=1}^{15q^2}\omega^{y_b}.
$$
For the length-$2$ class, each $2$-cycle contributes one internal ordered-pair orbit of phase $0$, and every ordered pair of distinct $2$-cycles contributes two orbits of phase $x_a-x_{a'}$. Therefore its nontrivial character sum is
$$
2q^2+2\sum_{a\neq a'}\omega^{x_a-x_{a'}}
=2|X|^2-2q^2.
$$
It vanishes exactly when
$$
|X|^2=q^2.
$$
Similarly, the length-$5$ class has four internal orbits per $5$-cycle and five orbits for every ordered pair of distinct $5$-cycles, so its character sum is
$$
60q^2+5\sum_{b\neq b'}\omega^{y_b-y_{b'}}
=5|Y|^2-15q^2.
$$
Thus
$$
|Y|^2=3q^2.
$$
Between a $2$-cycle and a $5$-cycle there is one orbit in each direction. Their phases are $y_b-x_a$ and $x_a-y_b$, so the length-$10$ character sum is
$$
Y\overline X+X\overline Y=2\operatorname{Re}(X\overline Y).
$$
The nonzero-$s$ condition is therefore equivalent to
$$
|X|^2=q^2,
\qquad
|Y|^2=3q^2,
\qquad
\operatorname{Re}(X\overline Y)=0.
$$

Step 4: Classify the norm solutions and impose the global phase relation
Work in the Euclidean ring $\mathbb Z[\omega]$, whose norm is $N(z)=|z|^2$. Because $q\equiv2\pmod3$, the rational prime $q$ remains prime in $\mathbb Z[\omega]$. The first norm equation therefore gives $X=q\varepsilon$ for a unit $\varepsilon$. Since $X$ is a sum of $2q^2$ powers of $\omega$, reduction modulo $1-\omega$ gives
$$
X\equiv2q^2\equiv q\pmod{1-\omega}.
$$
Only the units $1,\omega,\omega^2$ satisfy this congruence, so
$$
X\in\{q,q\omega,q\omega^2\}.
$$

The norm equation $N(Y)=3q^2$ forces $q\mid Y$: the only prime of $\mathbb Z[\omega]$ above the inert rational prime $q$ is $q$ itself. For a fixed such $X$, put $Z=Y/X$. Then $Z\in\mathbb Z[\omega]$, $N(Z)=3$, and $\operatorname{Re}(Z)=0$. Writing $Z=a+b\omega$, the second condition gives $2a-b=0$, and the norm gives $a^2-ab+b^2=3$. Hence $a=\pm1$, so
$$
Y=\pm X(1+2\omega).
$$

If a multiset of residues has character sum $U=A+B\omega$, then its residue sum is congruent to $B$ modulo $3$: writing its multiplicities as $(m_0,m_1,m_2)$ gives $B=m_1-m_2$ and $m_1+2m_2\equiv B\pmod3$. The relation $\sum_i\xi_i=0$ is therefore the condition that the $\omega$-coefficients of $X$ and $Y$ add to $0$ modulo $3$. If $X=q$, the two signs give coefficient sums $\pm2q$, so neither works. If $X=q\omega$, only the positive sign works, while if $X=q\omega^2$, only the negative sign works. Thus exactly two pairs remain:
$$
(X,Y)=\bigl(q\omega,q\omega(1+2\omega)\bigr)
$$
and
$$
(X,Y)=\bigl(q\omega^2,-q\omega^2(1+2\omega)\bigr).
$$

Step 5: Count the phase assignments
For the first pair, the multiplicities of the $2$-cycle sums $0,1,2$ are
$$
(A_q,A_q+q,A_q),
$$
and for the conjugate pair they are
$$
(A_q,A_q,A_q+q).
$$
Both profiles occur in
$$
\binom{2q^2}{A_q,A_q,A_q+q}
$$
ways. The corresponding multiplicities of the $5$-cycle sums are
$$
(5q^2-q,5q^2,5q^2+q)
$$
and
$$
(5q^2-q,5q^2+q,5q^2),
$$
so each occurs in
$$
\binom{15q^2}{5q^2-q,5q^2,5q^2+q}
$$
ways.

For prescribed sums, a $2$-cycle has $3$ phase assignments and a $5$-cycle has $3^4$ phase assignments. Hence each profile has
$$
3^{2q^2+4\cdot15q^2}=3^{62q^2}
$$
preimages. There are two profiles and two nonzero values of $s$, contributing four times this quantity. When $s=0$, every vector with coordinate sum $0$ works, contributing $3^{n-1}=3^{79q^2-1}$ lifts. For the smallest parameter $q=2$, the two admissible profiles are $(2,4,2)$ with $(18,20,22)$ and $(2,2,4)$ with $(18,22,20)$, which directly checks the boundary case. Adding the two cases gives the required count.

Final Answer: $\boxed{3^{79q^2-1}+4\cdot3^{62q^2}\binom{2q^2}{A_q,A_q,A_q+q}\binom{15q^2}{5q^2-q,5q^2,5q^2+q}}$

---

## Answer

$3^{79q^2-1}+4\cdot3^{62q^2}\binom{2q^2}{A_q,A_q,A_q+q}\binom{15q^2}{5q^2-q,5q^2,5q^2+q}$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- cubic Kummer theory
- permutation orbits on ordered pairs
- character sums over cyclic phases
- norms in the Eisenstein integers
- multinomial counting
