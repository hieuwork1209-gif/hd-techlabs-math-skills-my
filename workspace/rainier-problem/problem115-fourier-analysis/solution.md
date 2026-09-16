## Steps

Step 1: Reduce Fourier self-duality and count the admissible quadratic forms

For
$$
f_{M,g}(x,y)=(-1)^{x\cdot My+g(y)},
$$
summing first over $x$ gives
$$
(\mathcal Ff_{M,g})(u,v)=(-1)^{u\cdot M^{-1}v+g(M^{-1}v)}.
$$
Therefore
$$
\mathcal Ff_{M,g}=f_{M,g}
\iff M^2=I\quad\text{and}\quad g\circ M=g.
$$
The parametrization is injective: $f_{M,g}(0,y)$ determines $g(y)$, and then the character in $x$ determines $My$ for every $y$.

Let
$$
B_g(x,y)=g(x+y)+g(x)+g(y),
\qquad
W_g(a)=\sum_{y\in E}(-1)^{g(y)+a\cdot y}.
$$
For quadratic $g$,
$$
W_g(a)^2
=\sum_{t\in E}(-1)^{g(t)+a\cdot t}
\sum_{z\in E}(-1)^{B_g(z,t)}.
$$
The inner sum equals $2^8$ when $t\in\operatorname{rad}B_g$ and $0$ otherwise. Hence the condition $|W_g(a)|=16$ for every $a$ is equivalent to nondegeneracy of $B_g$: nondegeneracy gives $W_g(a)^2=2^8$, while a nonzero radical lets one choose $a$ agreeing with the linear function $g$ on the radical, which makes $W_g(a)^2>2^8$.

Fix a nondegenerate alternating form $B$ on an $8$-space. Its quadratic refinements are $q_a(x)=q(x)+B(a,x)$. Since
$$
q(x)+B(a,x)=q(x+a)+q(a),
$$
we have
$$
W_{q_a}(0)=(-1)^{q(a)}W_q(0).
$$
For a refinement with positive Walsh sign,
$$
\#q^{-1}(0)-\#q^{-1}(1)=16,
\qquad
\#q^{-1}(0)+\#q^{-1}(1)=256,
$$
so exactly $136=2^3\cdot17$ refinements have $W_q(0)=16$.

It remains to count nondegenerate alternating forms. Choosing a symplectic basis gives
$$
\alpha_{2m}
=\frac{|\operatorname{GL}(2m,2)|}{|\operatorname{Sp}(2m,2)|}
=2^{m(m-1)}\prod_{j=1}^m(2^{2j-1}-1).
$$
Thus
$$
\alpha_8=2^{12}\cdot7\cdot31\cdot127,
$$
and the number of admissible $g$ is
$$
N_+=136\alpha_8
=2^{15}\cdot7\cdot17\cdot31\cdot127.
$$
All such $g$ are split nondegenerate quadratic forms, so their isometry groups are conjugate. We may henceforth fix one split form $q$ and its polar form $B$.

Step 2: Parametrize the preserving involutions by residual data

Let $T\in O(q)$ satisfy $T^2=I$, and write $T=I+N$. Then $N^2=0$. Put
$$
R=\operatorname{im}N.
$$
Since $T$ preserves $B$,
$$
B(Nx,y)+B(x,Ny)+B(Nx,Ny)=0.
$$
Replacing $y$ by $Ny$ gives $B(Nx,Ny)=0$, so $R$ is $B$-isotropic. The same identity then gives
$$
B(Nx,y)=B(x,Ny),
\qquad
\ker N=R^\perp.
$$
For $u=Nx\in R$ and $v\in R$, define
$$
\omega(u,v)=B(x,v).
$$
This is well-defined because $\ker N=R^\perp$, symmetric by the displayed adjointness identity, and nondegenerate. Moreover $q(Tx)=q(x)$ gives
$$
\omega(Nx,Nx)=B(x,Nx)=q(Nx).
$$
Thus the diagonal of $\omega$ is $q|_R$.

Conversely, if $R$ is $B$-isotropic and $\omega$ is a nondegenerate symmetric form on $R$ with $\omega(r,r)=q(r)$, the map $x\mapsto B(x,\cdot)|_R$ identifies $E/R^\perp$ with $R^*$. Since $\omega:R\to R^*$ is an isomorphism, there is a unique $N:E\to R$ satisfying
$$
\omega(Nx,r)=B(x,r)
$$
for every $r\in R$. Then $N|_R=0$, hence $N^2=0$, and taking $r=Nx$ gives $q(x+Nx)=q(x)$. Therefore $T=I+N$ is an isometry with $T^2=I$.

So preserving involutions are in bijection with pairs $(R,\omega)$ of this form.

Step 3: Count residual types and derive the singular fixed-point weight

Let $I_r$ be the number of $r$-dimensional $B$-isotropic subspaces and $S_r$ the number of totally $q$-singular ones. Building ordered isotropic bases gives
$$
I_r=
\frac{\prod_{k=0}^{r-1}(2^{8-k}-2^k)}
{\prod_{k=0}^{r-1}(2^r-2^k)},
$$
so
$$
(I_1,I_2,I_3,I_4)=(255,5355,11475,2295).
$$
For a totally singular $k$-space $U$, the quotient $U^\perp/U$ is split of dimension $2(4-k)$. A split $2m$-space has
$$
(2^{m-1}+1)(2^m-1)
$$
nonzero singular vectors. Extending an ordered singular basis and dividing by the number of ordered bases therefore gives
$$
(S_1,S_2,S_3,S_4)=(135,1575,2025,270).
$$

Because $B|_R=0$, the restriction $q|_R$ is linear. If $q|_R=0$, the admissible $\omega$ are precisely nondegenerate alternating forms, so there are $\alpha_r$ for even $r$ and none for odd $r$. If $q|_R\ne0$, choose a basis in which $q|_R$ is the first coordinate. Writing
$$
[\omega]=\begin{pmatrix}1&b^T\\ b&A\end{pmatrix}
$$
with $A$ alternating shows that for odd $r$ the number is $2^{r-1}\alpha_{r-1}$, while for even $r$ it is $\alpha_r$. With
$$
\alpha_0=1,\qquad \alpha_2=1,\qquad \alpha_4=28,
$$
the numbers of preserving involutions with residual dimension $r$ and residual type $q|_R=0$ or $q|_R\ne0$ are therefore
$$
(1,0),\ (0,120),\ (1575,3780),\ (0,37800),\ (7560,56700)
$$
for $r=0,1,2,3,4$, respectively.

The marked-vector condition requires more than the total involution count. Since
$$
\operatorname{Fix}(T)=\ker N=R^\perp,
$$
we need the number of nonzero singular vectors in $R^\perp$.

If $q|_R\ne0$, then on every coset $x+R\subset R^\perp$ the function
$$
r\longmapsto q(x+r)=q(x)+q(r)
$$
is a nonconstant affine linear function. Exactly half of each coset is singular. Hence the number of singular vectors in $R^\perp$, including $0$, is
$$
2^{7-r},
$$
and the number of nonzero singular fixed vectors is
$$
z_{r,1}=2^{7-r}-1.
$$

If $q|_R=0$, then $q$ descends to a split nondegenerate form on $R^\perp/R$, of dimension $2(4-r)$. Lifting its zeros back through the $2^r$-element fibers gives, including $0$,
$$
2^{7-r}+8
$$
singular vectors in $R^\perp$. Thus
$$
z_{r,0}=2^{7-r}+7.
$$
This formula also gives $15$ when $r=4$, as it should because then $R^\perp=R$ is a $4$-dimensional totally singular space.

Step 4: Double-count the marked singular fixed vector

For the fixed split form $q$, let $H$ be the number of pairs $(T,a)$ such that
$$
T\in O(q),\qquad T^2=I,\qquad a\ne0,\qquad q(a)=0,\qquad Ta=a.
$$
Using the residual counts from Step 3 and the uniform weights $z_{r,0},z_{r,1}$ gives
$$
\begin{aligned}
H={}&135+120\cdot63
+1575\cdot39+3780\cdot31\\
&+37800\cdot15+7560\cdot15+56700\cdot7\\
={}&1263600
=2^4\cdot3^5\cdot5^2\cdot13.
\end{aligned}
$$

Now let $\mathcal T$ be the set of triples $(g,T,a)$ where $g$ is admissible, $T$ preserves $g$ and satisfies $T^2=I$, and $a\ne0$ is both $g$-singular and fixed by $T$. For each admissible $g$, the inner count is $H$, so
$$
|\mathcal T|=N_+H.
$$
The group $\operatorname{GL}(8,2)$ acts transitively on the $255$ nonzero vectors of $E$ and preserves all defining conditions under simultaneous transport of $(g,T,a)$. Therefore every fixed nonzero vector occurs equally often as the marked vector. For the prescribed $e$, the desired count is
$$
\frac{N_+H}{255}.
$$
Since
$$
255=3\cdot5\cdot17,
$$
we obtain
$$
\frac{(2^{15}\cdot7\cdot17\cdot31\cdot127)
(2^4\cdot3^5\cdot5^2\cdot13)}{3\cdot5\cdot17}
=2^{19}\cdot3^4\cdot5\cdot7\cdot13\cdot31\cdot127.
$$

Final Answer: $\boxed{2^{19}\cdot3^4\cdot5\cdot7\cdot13\cdot31\cdot127}$

---

## Answer

$2^{19}\cdot3^4\cdot5\cdot7\cdot13\cdot31\cdot127$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact scalar

---

## Solution Concepts

- Walsh--Fourier self-duality
- quadratic forms over finite fields
- orthogonal involutions and Wall forms
- singular fixed-point incidence
- double counting