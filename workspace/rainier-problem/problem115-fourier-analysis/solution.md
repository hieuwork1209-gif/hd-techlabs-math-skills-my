## Steps

Step 1: Reduce self-duality to orthogonal involutions and count the admissible quadratic forms

For
$$
f_{M,g}(x,y)=(-1)^{x\cdot My+g(y)},
$$
we have
$$
(\mathcal Ff_{M,g})(u,v)
=2^{-8}\sum_{y\in E}(-1)^{g(y)+u\cdot y}
\sum_{x\in E}(-1)^{x\cdot(My+v)}.
$$
The inner sum is $2^8$ when $My=v$ and $0$ otherwise, so
$$
(\mathcal Ff_{M,g})(u,v)=(-1)^{u\cdot M^{-1}v+g(M^{-1}v)}.
$$
Hence
$$
\mathcal Ff_{M,g}=f_{M,g}
\iff M^2=I\quad\text{and}\quad g\circ M=g.
$$
The parametrization is injective: for each $y$, the character in $x$ recovers $My$, while $f_{M,g}(0,y)$ recovers $g(y)$.

Let
$$
B_g(x,y)=g(x+y)+g(x)+g(y)
$$
be the polar form. If
$$
W_g(a)=\sum_{y\in E}(-1)^{g(y)+a\cdot y},
$$
then, after writing $t=y+z$,
$$
W_g(a)^2
=\sum_{t\in E}(-1)^{g(t)+a\cdot t}
\sum_{z\in E}(-1)^{B_g(z,t)}.
$$
The inner sum is $2^8$ for $t\in\operatorname{rad}B_g$ and $0$ otherwise. Therefore $|W_g(a)|=16$ for every $a$ exactly when $B_g$ is nondegenerate. The condition $W_g(0)=16$ selects the plus Arf type.

Let $\alpha_{2m}$ be the number of nondegenerate alternating forms on a fixed $2m$-dimensional binary vector space. The general linear group acts transitively on these forms. For one fixed form, an ordered symplectic basis is chosen recursively: after choosing a nonzero first vector in a $2j$-dimensional symplectic space, there are $2^{2j-1}$ choices for its partner, and the remaining vectors form a symplectic basis of a $2j-2$ dimensional complement. Hence
$$
|\operatorname{Sp}(2m,2)|
=\prod_{j=1}^{m}(2^{2j}-1)2^{2j-1}.
$$
Dividing $|\operatorname{GL}(2m,2)|$ by this stabilizer gives
$$
\alpha_{2m}
=2^{m(m-1)}\prod_{i=1}^{m}(2^{2i-1}-1).
$$
Thus $\alpha_8=112881664$. For a fixed nondegenerate $B$, its quadratic refinements are $q_a(x)=q(x)+B(a,x)$, $a\in E$. Taking one plus refinement $q$, translation gives
$$
W_{q_a}(0)=(-1)^{q(a)}W_q(0).
$$
Since $W_q(0)=16$, the number of zeros of $q$ is determined by
$$
\#q^{-1}(0)-\#q^{-1}(1)=16,
\qquad
\#q^{-1}(0)+\#q^{-1}(1)=256,
$$
so exactly $136$ refinements have plus sign. Consequently the number of admissible $g$ is
$$
136\alpha_8=15351906304.
$$
All plus-type forms are linearly equivalent to the split form $x_1x_2+x_3x_4+x_5x_6+x_7x_8$, so it remains to count involutions preserving one fixed plus-type quadratic form $q$.

Step 2: Encode every orthogonal involution by its residual space and Wall form

Fix the plus-type form $q$ and let $B$ be its polar form. For an involution $T$ preserving $q$, write $T=I+N$. Then $N^2=0$. Put
$$
R=\operatorname{im}N.
$$
Because $T$ preserves $B$,
$$
B(Nx,y)+B(x,Ny)+B(Nx,Ny)=0.
$$
Replacing $y$ by $Ny$ and using $N^2=0$ gives $B(Nx,Ny)=0$, so $R$ is $B$-isotropic. The same identity then becomes
$$
B(Nx,y)=B(x,Ny),
$$
which implies
$$
\ker N=R^{\perp}.
$$

For $u=Nx\in R$ and $v\in R$, define
$$
\omega(u,v)=B(x,v).
$$
This is well-defined because changing $x$ by an element of $\ker N=R^{\perp}$ does not change the value. It is nondegenerate: if $\omega(Nx,v)=0$ for every $v\in R$, then $x\in R^{\perp}=\ker N$, hence $Nx=0$. For $u=Nx$ and $v=Ny$,
$$
\omega(u,v)=B(x,Ny)=B(Nx,y)=\omega(v,u),
$$
so $\omega$ is symmetric. Finally, $q(Tx)=q(x)$ gives
$$
q(Nx)=B(x,Nx)=\omega(Nx,Nx).
$$
Thus the diagonal of $\omega$ is exactly $q|_R$.

Conversely, let $R$ be any $B$-isotropic subspace and let $\omega$ be a nondegenerate symmetric form on $R$ satisfying
$$
\omega(r,r)=q(r)\qquad(r\in R).
$$
The map $x\mapsto B(x,\cdot)|_R$ surjects from $E$ onto $R^*$, and $\omega$ identifies $R$ with $R^*$. Hence there is a unique linear map $N:E\to R$ such that
$$
\omega(Nx,r)=B(x,r)\qquad(r\in R).
$$
Since $R$ is $B$-isotropic, $N$ vanishes on $R$, so $N^2=0$. Taking $r=Nx$ gives
$$
B(x,Nx)=\omega(Nx,Nx)=q(Nx),
$$
and therefore
$$
q(x+Nx)=q(x)+q(Nx)+B(x,Nx)=q(x).
$$
So $T=I+N$ is an orthogonal involution with image $R$. This proves a bijection between orthogonal involutions and pairs $(R,\omega)$ of the stated kind.

Step 3: Count the residual data with one parity formula

Let $I_r$ be the number of $r$-dimensional $B$-isotropic subspaces and $S_r$ the number of $r$-dimensional totally $q$-singular subspaces. To count $I_r$, build an ordered basis of an isotropic $r$-space. After $k$ independent isotropic vectors span $U$, the next vector may be any element of $U^{\perp}\setminus U$, so there are $2^{8-k}-2^k$ choices. Dividing by the number $\prod_{k=0}^{r-1}(2^r-2^k)$ of ordered bases of an $r$-space gives
$$
I_r=
\frac{\prod_{k=0}^{r-1}(2^{8-k}-2^k)}
{\prod_{k=0}^{r-1}(2^r-2^k)}.
$$

For $S_r$, suppose $U$ is already totally singular of dimension $k$. Then $U^{\perp}/U$ is again split, now of dimension $2(4-k)$. In a split $2m$-space written as $q(a,b)=a\cdot b$, the number of nonzero singular vectors is
$$
(2^{m-1}+1)(2^m-1).
$$
Indeed, for $a=0$ there are $2^m$ choices of $b$, while for each nonzero $a$ there are $2^{m-1}$ vectors $b$ with $a\cdot b=0$, and then the zero vector is removed. Thus, at stage $k$, there are
$$
2^k(2^{3-k}+1)(2^{4-k}-1)
$$
possible next vectors. Dividing the product of these extension counts by the same ordered-basis denominator gives $S_r$. The values needed here are therefore
$$
I_1=255,\quad S_1=135,\quad I_2=5355,
$$
$$
I_3=11475,\quad S_3=2025,\quad I_4=2295.
$$

Because $B|_R=0$, the restriction $\ell=q|_R$ is linear. The number of nondegenerate symmetric forms $\omega$ with diagonal $\ell$ has a uniform parity description. If $\ell=0$, then $\omega$ is alternating, so there are $\alpha_r$ choices for even $r$ and none for odd $r$. If $\ell\neq0$, choose $e$ with $\ell(e)=1$ and put $H=\ker\ell$. In the decomposition $R=\langle e\rangle\oplus H$,
$$
[\omega]=
\begin{pmatrix}
1&b^T\\
b&A
\end{pmatrix},
$$
where $A$ is alternating. When $r$ is odd, $H$ has even dimension and nondegeneracy is equivalent to $A$ being nondegenerate, giving $2^{r-1}\alpha_{r-1}$ choices. When $r$ is even, $H$ has odd dimension. An alternating form $A$ can then have the required one-dimensional radical in $(2^{r-1}-1)\alpha_{r-2}$ ways: choose its radical line, then a nondegenerate alternating form on the quotient. For each such $A$, exactly $2^{r-2}$ functionals $b$ are nonzero on the radical. Their product equals $\alpha_r$. Thus, for even $r$ every $B$-isotropic $R$ contributes $\alpha_r$ forms, while for odd $r$ only the $I_r-S_r$ subspaces with $q|_R\neq0$ contribute, each with $2^{r-1}\alpha_{r-1}$ forms.

Since $R$ is isotropic, $0\leq r\leq4$. Using $\alpha_0=1$, $\alpha_2=1$, and $\alpha_4=28$, the number $J$ of involutions preserving $q$ is the single sum
$$
J
=1+\sum_{r\in\{2,4\}}I_r\alpha_r
+\sum_{r\in\{1,3\}}(I_r-S_r)2^{r-1}\alpha_{r-1}
$$
$$
=1+(255-135)+5355+4(11475-2025)+28\cdot2295
=107536.
$$

Step 4: Combine the independently checkable factors

There are $136\cdot112881664$ admissible plus-type quadratic forms $g$, and every such form has exactly $107536$ preserving involutions. By the injectivity established in Step 1, the number of distinct self-dual functions is
$$
136\cdot112881664\cdot107536=1650882596306944.
$$
The factored form keeps the three independently meaningful counts visible: plus refinements per polar form, nondegenerate polar forms, and orthogonal involutions.

Final Answer: $\boxed{136\cdot112881664\cdot107536}$

---

## Answer

$136\cdot112881664\cdot107536$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact scalar

---

## Solution Concepts

- Walsh--Fourier self-duality
- quadratic forms over finite fields
- orthogonal involutions
- Wall forms
- isotropic subspace counting
