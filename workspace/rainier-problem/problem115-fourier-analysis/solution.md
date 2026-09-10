## Steps

Step 1: Reduce Walsh self-duality to invariant quadratic forms

For $M\in\operatorname{GL}(8,2)$ and an admissible quadratic Boolean function $g$, put
$$
f_{M,g}(x,y)=(-1)^{x\cdot My+g(y)}.
$$
For $(u,v)\in E\times E$,
$$
(\mathcal Ff_{M,g})(u,v)
=2^{-8}\sum_{y\in E}(-1)^{g(y)+y\cdot u}
\sum_{x\in E}(-1)^{x\cdot(My+v)}.
$$
The inner sum is $2^8$ exactly when $My=v$, and is $0$ otherwise. Hence
$$
(\mathcal Ff_{M,g})(u,v)
=(-1)^{u\cdot M^{-1}v+g(M^{-1}v)}.
$$
Comparing this with
$$
f_{M,g}(u,v)=(-1)^{u\cdot Mv+g(v)}
$$
for every $u,v$ gives
$$
\mathcal Ff_{M,g}=f_{M,g}
\iff
M^2=I,
\qquad g\circ M=g.
$$
The parametrization $(M,g)\mapsto f_{M,g}$ is injective, since the $x$-character recovers $My$ and $f_{M,g}(0,y)$ recovers $g(y)$.

For a quadratic $g$ with $g(0)=0$, let
$$
B_g(x,y)=g(x+y)+g(x)+g(y).
$$
The usual squared-Walsh calculation shows that
$$
\left|\sum_y(-1)^{g(y)+a\cdot y}\right|=16
\quad\text{for every }a
$$
if and only if $B_g$ is nondegenerate. Moreover
$$
\varepsilon(g):=2^{-4}\sum_y(-1)^{g(y)}\in\{1,-1\},
$$
so the additional condition $\sum_y(-1)^{g(y)}=16$ is exactly $\varepsilon(g)=1$.

Step 2: Count the linear involutions by rank

Write
$$
M=I+N.
$$
In characteristic $2$,
$$
M^2=I\iff N^2=0.
$$
Let $r=\operatorname{rank}N$. Then $0\le r\le4$, with
$$
U=\operatorname{im}N\subseteq K=\ker N,
\qquad
\dim U=r,
\qquad
\dim K=8-r.
$$
For fixed $r$, choose $U$, then $K\supseteq U$, then the induced isomorphism $E/K\to U$. Thus the number $A_r$ of such $N$ is
$$
A_r=\binom{8}{r}_2\binom{8-r}{r}_2|\operatorname{GL}(r,2)|.
$$
Hence
$$
A_0=1,
\quad A_1=32385,
\quad A_2=42165270,
$$
$$
A_3=2529916200,
\quad A_4=4047865920.
$$

Step 3: Count the invariant nondegenerate polar forms

Fix a rank-$r$ map $N$. Choose coordinates
$$
E=U\oplus W\oplus Z,
\qquad
\dim U=\dim W=r,
\qquad
\dim Z=s:=8-2r,
$$
so that
$$
N(u,w,z)=(w,0,0).
$$
An alternating form $B$ is invariant under $M=I+N$ exactly when its matrix has the shape
$$
B=
\begin{pmatrix}
0&R&0\\
R&S&T\\
0&T^T&D
\end{pmatrix},
$$
where $R$ is symmetric $r\times r$, $S$ is alternating, $T$ is arbitrary, and $D$ is alternating $s\times s$. Such a form is nondegenerate exactly when $R$ and $D$ are both nonsingular.

Let $\sigma_r$ be the number of nonsingular symmetric $r\times r$ binary matrices and $\alpha_s$ the number of nondegenerate alternating $s\times s$ matrices. Then
$$
Q_r=\sigma_r\,2^{\binom r2+rs}\alpha_s
$$
is the number of invariant nondegenerate polar forms. Using
$$
\alpha_0=1,\quad \alpha_2=1,\quad \alpha_4=28,
\quad \alpha_6=13888,\quad \alpha_8=112881664
$$
and
$$
\sigma_0=1,\quad \sigma_1=1,\quad \sigma_2=4,
\quad \sigma_3=28,\quad \sigma_4=448,
$$
we obtain
$$
\begin{array}{c|ccccc}
r&0&1&2&3&4\\ \hline
Q_r&112881664&888832&57344&14336&28672.
\end{array}
$$

The later Arf-sign split depends on whether $R$ is alternating. Let $Q_r^{\mathrm{alt}}$ denote the number of the above forms for which $R$ is alternating as well as nonsingular. This is zero for odd $r$, while for even $r$
$$
Q_r^{\mathrm{alt}}
=\alpha_r\,2^{\binom r2+rs}\alpha_s.
$$
Therefore
$$
\begin{array}{c|ccccc}
r&0&1&2&3&4\\ \hline
Q_r^{\mathrm{alt}}&112881664&0&14336&0&1792.
\end{array}
$$

Step 4: Split the invariant quadratic refinements by Walsh sign

Fix one invariant nondegenerate polar form $B$. Since $B$ is nondegenerate, all quadratic refinements are
$$
g_a(x)=g(x)+B(a,x),
\qquad a\in E.
$$
If $g$ is $M$-invariant, then $g_a$ is $M$-invariant exactly when $a\in K=\ker N$. Hence there are $2^{8-r}$ invariant refinements of $B$.

Their Walsh signs satisfy
$$
\varepsilon(g_a)=\varepsilon(g)(-1)^{g(a)},
$$
because
$$
g(x)+B(a,x)=g(x+a)+g(a).
$$
Thus the difference between the numbers of positive- and negative-sign invariant refinements is
$$
\varepsilon(g)\sum_{a\in K}(-1)^{g(a)}.
$$

The radical of $B|_K$ is $U=\operatorname{im}N$. In the coordinates of Step 3, invariance gives, for $u=Nv$,
$$
g(u)=B(v,u),
$$
and this restriction vanishes identically on $U$ exactly when the diagonal of $R$ is zero, that is, exactly when $R$ is alternating.

If $R$ is not alternating, then $g|_U$ is a nonzero linear form, so
$$
\sum_{a\in K}(-1)^{g(a)}=0.
$$
Hence exactly half of the $2^{8-r}$ invariant refinements have positive Walsh sign.

If $R$ is alternating, then $g$ vanishes on $U$ and descends to a nondegenerate quadratic form on $K/U$. Splitting off $r$ hyperbolic pairs shows
$$
\sum_{a\in K}(-1)^{g(a)}=16\varepsilon(g).
$$
Therefore the positive-minus-negative difference is $16$. Consequently the number $P_r$ of invariant refinements satisfying the required positive Walsh sign, summed over all invariant nondegenerate $B$, is
$$
P_r
=2^{7-r}Q_r+8Q_r^{\mathrm{alt}}.
$$
This gives
$$
\begin{array}{c|ccccc}
r&0&1&2&3&4\\ \hline
P_r&15351906304&56885248&1949696&229376&243712.
\end{array}
$$

Step 5: Sum over the involution ranks

For each rank $r$, there are $A_r$ possible linear involutions and $P_r$ admissible positive-sign invariant quadratic functions. Hence the required number is
$$
\sum_{r=0}^4 A_rP_r.
$$
Substituting the values from Steps 2 and 4 yields
$$
1650882596306944.
$$

Final Answer: $\boxed{1650882596306944}$

---

## Answer

$1650882596306944$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact scalar

---

## Solution Concepts

- Walsh--Fourier self-duality
- quadratic bent Boolean functions
- Arf invariant and Walsh sign
- linear involutions over $\mathbb F_2$
- invariant orthogonal geometry

---

## Black-Box Audit — no issues found
