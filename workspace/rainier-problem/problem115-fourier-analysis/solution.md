## Steps

Step 1: Reduce self-duality and count the admissible quadratic forms
For
$$
f_{M,g}(x,y)=(-1)^{x\cdot My+g(y)},
$$
summing over $x$ first gives
$$
(\mathcal Ff_{M,g})(u,v)=(-1)^{u\cdot M^{-1}v+g(M^{-1}v)}.
$$
Thus
$$
\mathcal Ff_{M,g}=f_{M,g}
\iff M^2=I\ \text{and}\ g\circ M=g.
$$
Also $f_{M,g}(0,y)$ determines $g(y)$ and then the character in $x$ determines $My$, so distinct pairs $(M,g)$ give distinct functions.

Put
$$
B_g(x,y)=g(x+y)+g(x)+g(y),\qquad
W_g(a)=\sum_y(-1)^{g(y)+a\cdot y}.
$$
For quadratic $g$,
$$
W_g(a)^2=\sum_t(-1)^{g(t)+a\cdot t}\sum_z(-1)^{B_g(z,t)}.
$$
The inner sum is $2^8$ on $\operatorname{rad}B_g$ and $0$ elsewhere. Hence $|W_g(a)|=16$ for every $a$ exactly when $B_g$ is nondegenerate: if the radical were nonzero, choosing $a$ to agree with the linear function $g$ on it would give $W_g(a)^2>2^8$.

For a fixed nondegenerate alternating form $B$, its quadratic refinements are $q_a(x)=q(x)+B(a,x)$, and
$$
q(x)+B(a,x)=q(x+a)+q(a)
$$
implies $W_{q_a}(0)=(-1)^{q(a)}W_q(0)$. A positive refinement has $136$ zeros because its zero and one counts have sum $256$ and difference $16$. Thus exactly $136=2^3\cdot17$ refinements have positive Walsh sign. The number of nondegenerate alternating forms on an $8$-space is
$$
\alpha_8=\frac{|\operatorname{GL}(8,2)|}{|\operatorname{Sp}(8,2)|}
=2^{12}\cdot7\cdot31\cdot127,
$$
from the usual symplectic-basis count. Therefore the number of admissible $g$ is
$$
N_+=136\alpha_8=2^{15}\cdot7\cdot17\cdot31\cdot127.
$$
The positive sign is the split quadratic type, so all admissible $g$ have conjugate isometry groups. Fix one split form $q$ with polar form $B$.

Step 2: Parametrize the preserving involutions
Let $T\in O(q)$ satisfy $T^2=I$, write $T=I+N$, and put $R=\operatorname{im}N$. Then $N^2=0$. Preservation of $B$ gives
$$
B(Nx,y)+B(x,Ny)+B(Nx,Ny)=0.
$$
Replacing $y$ by $Ny$ gives $B(Nx,Ny)=0$, so $R$ is $B$-isotropic; hence
$$
B(Nx,y)=B(x,Ny),\qquad \ker N=R^\perp.
$$
For $u=Nx\in R$ define
$$
\omega(u,v)=B(x,v)\qquad(v\in R).
$$
This is well-defined, symmetric, and nondegenerate, and $q(x+Nx)=q(x)$ gives
$$
\omega(Nx,Nx)=B(x,Nx)=q(Nx).
$$
Thus the diagonal of $\omega$ is $q|_R$.

Conversely, given a $B$-isotropic $R$ and a nondegenerate symmetric $\omega$ on $R$ with $\omega(r,r)=q(r)$, the perfect pairing identifies $E/R^\perp$ with $R^*$. Hence there is a unique $N:E\to R$ satisfying
$$
\omega(Nx,r)=B(x,r).
$$
Since $R$ is isotropic, $N|_R=0$, so $N^2=0$; taking $r=Nx$ gives $q(x+Nx)=q(x)$. Therefore $T=I+N$ is a preserving involution. This proves a bijection between such $T$ and residual pairs $(R,\omega)$.

Step 3: Count residual pairs and singular fixed vectors
Let $I_r$ count $r$-dimensional $B$-isotropic subspaces. Counting ordered isotropic bases gives
$$
I_r=\frac{\prod_{k=0}^{r-1}(2^{8-k}-2^k)}{\prod_{k=0}^{r-1}(2^r-2^k)},
$$
so
$$
(I_1,I_2,I_3,I_4)=(255,5355,11475,2295).
$$
Let $S_r$ count totally $q$-singular $r$-spaces. If $U$ is a singular $k$-space, then $U^\perp/U$ is split of dimension $2(4-k)$ and has $(2^{3-k}+1)(2^{4-k}-1)$ nonzero singular vectors. Extending an ordered singular basis therefore gives
$$
(S_1,S_2,S_3,S_4)=(135,1575,2025,270).
$$

Because $B|_R=0$, $q|_R$ is linear. If $q|_R=0$, admissible $\omega$ are nondegenerate alternating forms, so the counts for $r=0,2,4$ are $1,1,28$. If $q|_R\ne0$, choose a basis with $q|_R=x_1$ and write
$$
[\omega]=\begin{pmatrix}1&b^T\\ b&A\end{pmatrix},
$$
where $A$ is alternating. For odd $r$, nondegeneracy is equivalent to nondegeneracy of $A$, giving $2^{r-1}\alpha_{r-1}$ choices; for even $r$, the count is $\alpha_r$. Thus the numbers of involutions of residual type $q|_R=0$ or $q|_R\ne0$, for $r=0,1,2,3,4$, are
$$
(1,0),\ (0,120),\ (1575,3780),\ (0,37800),\ (7560,56700).
$$

Now $\operatorname{Fix}(T)=\ker N=R^\perp$. If $q|_R\ne0$, $q$ is a nonconstant affine function on every coset of $R$ in $R^\perp$, so exactly half of each coset is singular. Hence the number of nonzero singular fixed vectors is
$$
z_{r,1}=2^{7-r}-1.
$$
If $q|_R=0$, $q$ descends to a split nondegenerate form on $R^\perp/R$. Lifting its zeros through the $2^r$-element fibers gives $2^{7-r}+8$ singular vectors including $0$, hence
$$
z_{r,0}=2^{7-r}+7.
$$
For $r=4$ this gives $15$, consistent with $R^\perp=R$ being totally singular.

Step 4: Double-count the marked singular fixed vector
For the fixed split form $q$, let $H$ count pairs $(T,a)$ with $T^2=I$, $T\in O(q)$, and $a\ne0$ satisfying $q(a)=0$ and $Ta=a$. Using the residual counts and the weights from Step 3,
$$
\begin{aligned}
H={}&135+120\cdot63+1575\cdot39+3780\cdot31\\
&+37800\cdot15+7560\cdot15+56700\cdot7\\
={}&1263600=2^4\cdot3^5\cdot5^2\cdot13.
\end{aligned}
$$
Across all admissible $g$, the number of triples $(g,T,a)$ with $a\ne0$, $g(a)=0$, $Ta=a$, and $T$ preserving $g$ is $N_+H$. Simultaneous change of basis by $\operatorname{GL}(8,2)$ preserves these conditions and is transitive on the $255$ nonzero vectors, so each prescribed nonzero $e$ occurs equally often. Therefore the desired count is
$$
\frac{N_+H}{255}
=\frac{(2^{15}\cdot7\cdot17\cdot31\cdot127)(2^4\cdot3^5\cdot5^2\cdot13)}{3\cdot5\cdot17}
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