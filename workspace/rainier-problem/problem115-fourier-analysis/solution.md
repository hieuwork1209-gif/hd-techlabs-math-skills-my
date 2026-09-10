## Steps

Step 1: Characterize self-duality

Let $g:E\to\mathbb F_2$ have algebraic degree at most $2$ and $g(0)=0$, and let
$$
f_{\pi,g}(x,y)=(-1)^{x\cdot\pi(y)+g(y)}.
$$
For $(u,v)\in E\times E$,
$$
(\mathcal Ff_{\pi,g})(u,v)
=2^{-8}\sum_{y\in E}(-1)^{g(y)+y\cdot u}
\sum_{x\in E}(-1)^{x\cdot(\pi(y)+v)}.
$$
The inner sum is $2^8$ exactly when $\pi(y)=v$, and is $0$ otherwise. Hence
$$
(\mathcal Ff_{\pi,g})(u,v)
=(-1)^{u\cdot\pi^{-1}(v)+g(\pi^{-1}(v))}.
$$
Comparing with
$$
f_{\pi,g}(u,v)=(-1)^{u\cdot\pi(v)+g(v)}
$$
for all $u,v$ shows that
$$
\mathcal Ff_{\pi,g}=f_{\pi,g}
$$
if and only if
$$
\pi^2=\operatorname{id}_E,
\qquad
g\circ\pi=g.
$$
The parametrization $(\pi,g)\mapsto f_{\pi,g}$ is injective, because the $x$-character recovers $\pi(y)$ and $f_{\pi,g}(0,y)$ recovers $g(y)$.

Step 2: Parametrize the affine involutions

Write
$$
\pi(v)=Mv+c,
\qquad M\in\operatorname{GL}(8,2),\ c\in E,
$$
and put $N=M+I$. In characteristic $2$,
$$
\pi^2=\operatorname{id}
\iff
N^2=0,
\qquad Nc=0.
$$
If $r=\operatorname{rank}N$, then $0\le r\le4$. Put
$$
U=\operatorname{im}N,
\qquad K=\ker N.
$$
Then
$$
\dim U=r,
\qquad \dim K=8-r,
\qquad U\subseteq K.
$$
The number $A_r$ of square-zero endomorphisms of rank $r$ is
$$
A_r=\binom{8}{r}_2\binom{8-r}{r}_2|\operatorname{GL}(r,2)|.
$$
Thus
$$
A_0=1,
\quad A_1=32385,
\quad A_2=42165270,
$$
$$
A_3=2529916200,
\quad A_4=4047865920.
$$

Step 3: Count invariant quadratic functions when $c\in U$

Let
$$
D=8+\binom82=36.
$$
Fix a square-zero $N$ of rank $r$. Choose coordinates
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
If $c\in U$, then $c=Nt$ for some $t$, and translation by $t$ conjugates $v\mapsto(I+N)v+c$ to $v\mapsto(I+N)v$. The map
$$
g(v)\longmapsto g(v+t)+g(t)
$$
preserves algebraic degree at most $2$, preserves the condition $g(0)=0$, and gives a bijection between the corresponding invariant functions. Hence it suffices to take $c=0$.

Write a quadratic Boolean polynomial in algebraic normal form in the variables $(u,w,z)$. Invariance under
$$
(u,w,z)\longmapsto(u+w,w,z)
$$
has the following consequences:

- all coefficients of $u_i u_j$ vanish;
- all coefficients of $u_i z_k$ vanish;
- if $R=(R_{ij})$ is the coefficient matrix of the terms $u_iw_j$, then $R$ is symmetric;
- the coefficient of $u_i$ is forced to be $R_{ii}$;
- the part involving only $(w,z)$ is arbitrary of degree at most $2$ with zero constant term.

Therefore the dimension of the invariant $g$-space is
$$
d_r=rac{r(r+1)}2+rac{(8-r)(9-r)}2
=36-r(8-r).
$$
Thus each of the $2^r$ translations $c\in U$ contributes $2^{d_r}$ choices of $g$.

Step 4: Count invariant quadratic functions when $c\in K\setminus U$

Assume $s=8-2r>0$ and $c\in K\setminus U$. First remove the $U$-component of $c$ by a translation as in Step 3. Then a linear change of coordinates commuting with $N$ may send the nonzero class of $c$ in $K/U$ to the first basis vector $z_1$ of $Z$. Hence we may take
$$
\pi(u,w,z_1,z')=(u+w,w,z_1+1,z').
$$
Repeating the algebraic-normal-form comparison from Step 3 gives the same conditions there, together with exactly $s$ further independent constraints:
$$
[z_1]g=0,
\qquad
[z_1z_j]g=0\quad(2\le j\le s).
$$
Indeed, these are respectively the constant and the $z_j$ coefficients created by the substitution $z_1\mapsto z_1+1$; the coefficients of $w_i z_1$ merely change the already-forced linear coefficients of the $u_i$ and create no additional constraint.

Hence the invariant $g$-space now has dimension
$$
d_r-s
=36-r(8-r)-(8-2r).
$$
There are
$$
|K\setminus U|=2^{8-r}-2^r
$$
such translations. Thus for a fixed rank-$r$ map $N$, the total number of allowed pairs $(c,g)$ is
$$
W_r
=2^r2^{d_r}
+\left(2^{8-r}-2^r\right)2^{d_r-(8-2r)}.
$$
For $r=0,1,2,3,4$ this gives
$$
W_0=137170518016,
\quad W_1=2130706432,
\quad W_2=130023424,
$$
$$
W_3=29360128,
\quad W_4=16777216.
$$

Step 5: Sum over the ranks

The required number of distinct self-dual functions is
$$
\sum_{r=0}^4 A_rW_r.
$$
Substituting the values from Steps 2 and 4 gives
$$
147742197217755136.
$$

Final Answer: $\boxed{147742197217755136}$

---

## Answer

$147742197217755136$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact scalar

---

## Solution Concepts

- Walsh--Fourier self-duality
- quadratic Maiorana--McFarland functions
- affine involutions over $\mathbb F_2$
- square-zero endomorphisms
- invariant quadratic Boolean polynomials

---

## Black-Box Audit — no issues found
