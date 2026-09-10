## Steps

Step 1: Characterize self-duality inside the affine Maiorana--McFarland family

For an affine permutation $\pi(y)=My+c$ and $g:E\to\mathbb F_2$ with $g(0)=0$, put
$$
f_{\pi,g}(x,y)=(-1)^{x\cdot\pi(y)+g(y)}.
$$
For $(u,v)\in E\times E$,
$$
(\mathcal Ff_{\pi,g})(u,v)
=2^{-8}\sum_{y\in E}(-1)^{g(y)+y\cdot u}
\sum_{x\in E}(-1)^{x\cdot(\pi(y)+v)}.
$$
The inner sum is $2^8$ exactly when $\pi(y)=v$, and is $0$ otherwise. Since $\pi$ is a permutation,
$$
(\mathcal Ff_{\pi,g})(u,v)
=(-1)^{u\cdot\pi^{-1}(v)+g(\pi^{-1}(v))}.
$$
Comparing this with
$$
f_{\pi,g}(u,v)=(-1)^{u\cdot\pi(v)+g(v)}
$$
for every $u,v$ shows that
$$
\mathcal Ff_{\pi,g}=f_{\pi,g}
$$
if and only if
$$
\pi^2=\operatorname{id}_E
\qquad\text{and}\qquad
g\circ\pi=g.
$$
Indeed, equality for every $u$ first forces $\pi^{-1}(v)=\pi(v)$, and then the constant terms force $g(\pi(v))=g(v)$.

The parametrization is injective: for fixed $y$, the character in the $x$-variable recovers $\pi(y)$, while $f_{\pi,g}(0,y)=(-1)^{g(y)}$ recovers $g(y)$. Thus it remains to count affine involutions $\pi$, weighting each by the number of $\pi$-invariant functions $g$ with $g(0)=0$.

Step 2: Parametrize affine involutions by square-zero linear maps

Write
$$
\pi(v)=Mv+c,
\qquad M\in\operatorname{GL}(8,2),\ c\in E,
$$
and put
$$
N=M+I.
$$
Because the characteristic is $2$,
$$
M^2=I\iff N^2=0.
$$
Also
$$
\pi^2(v)=M^2v+(M+I)c,
$$
so $\pi^2=\operatorname{id}$ exactly when
$$
N^2=0,
\qquad Nc=0.
$$
Conversely, if $N^2=0$, then $M=I+N$ is automatically invertible with inverse $I+N$.

Let
$$
r=\operatorname{rank}N.
$$
Since $\operatorname{im}N\subseteq\ker N$, we have $0\le r\le4$. Put
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

Step 3: Count square-zero maps of each rank

For fixed rank $r$, choose $U=\operatorname{im}N$, then choose $K=\ker N$ containing $U$, and finally choose the induced isomorphism
$$
E/K\longrightarrow U.
$$
Hence the number $A_r$ of square-zero endomorphisms of rank $r$ is
$$
A_r=inom{8}{r}_2\binom{8-r}{r}_2\,|\operatorname{GL}(r,2)|,
$$
where
$$
\binom{n}{r}_2
=\prod_{j=0}^{r-1}\frac{2^{n-j}-1}{2^{r-j}-1}.
$$
Evaluating gives
$$
A_0=1,
\quad A_1=32385,
\quad A_2=42165270,
$$
$$
A_3=2529916200,
\quad A_4=4047865920.
$$

Step 4: Count invariant Boolean functions for each affine involution

The translation vector must satisfy $c\in K$. The fixed-point equation for $\pi$ is
$$
Nv=c.
$$
If $c\in U$, this equation has exactly $|K|=2^{8-r}$ solutions; there are $2^r$ such translation vectors. If $c\in K\setminus U$, there are no fixed points; there are
$$
2^{8-r}-2^r
$$
such translations.

An involution of the $256$-element set $E$ having $F$ fixed points has
$$
\frac{256+F}{2}
$$
orbits. Therefore:

- if $c\in U$, then $\pi$ has $128+2^{7-r}$ orbits;
- if $c\in K\setminus U$, then $\pi$ has $128$ orbits.

A function $g:E\to\mathbb F_2$ satisfying $g\circ\pi=g$ is constant on every orbit of $\pi$. The condition $g(0)=0$ fixes the value on the unique orbit containing $0$, so an involution with $o$ orbits contributes exactly $2^{o-1}$ possible functions $g$.

Thus for each fixed square-zero $N$ of rank $r$, the total contribution from all allowed translations is
$$
W_r
=2^r2^{127+2^{7-r}}
+\left(2^{8-r}-2^r\right)2^{127}.
$$
Equivalently,
$$
W_r
=2^{127}\left(2^{r+2^{7-r}}+2^{8-r}-2^r\right).
$$

Step 5: Sum over the possible ranks

The required number is therefore
$$
\sum_{r=0}^4 A_rW_r
=2^{127}\sum_{r=0}^4
A_r\left(2^{r+2^{7-r}}+2^{8-r}-2^r\right).
$$
For $r=0,1,2,3,4$, the factors in parentheses are respectively
$$
340282366920938463463374607431768211711,
$$
$$
36893488147419103358,
\qquad
17179869244,
\qquad
524312,
\qquad
4096.
$$
Substituting the values of $A_r$ from Step 3 gives
$$
\sum_{r=0}^4
A_r\left(2^{r+2^{7-r}}+2^{8-r}-2^r\right)
=340282366920939658259713998470149879141.
$$
Hence the number of self-dual functions is
$$
2^{127}\cdot340282366920939658259713998470149879141.
$$

Final Answer: $\boxed{2^{127}\cdot340282366920939658259713998470149879141}$

---

## Answer

$2^{127}\cdot340282366920939658259713998470149879141$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact scalar

---

## Solution Concepts

- Walsh--Fourier self-duality
- Maiorana--McFarland bent functions
- affine involutions over $\mathbb F_2$
- square-zero linear endomorphisms
- Gaussian binomial coefficients

---

## Black-Box Audit — no issues found
