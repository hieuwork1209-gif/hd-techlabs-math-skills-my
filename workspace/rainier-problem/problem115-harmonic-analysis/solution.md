## Steps

Step 1: Reduce Fourier self-duality and count the admissible quadratic phases
For
$$
f_{M,g}(x,y)=(-1)^{x\cdot My+g(y)},
$$
summing over $x$ first gives
$$
(\mathcal Ff_{M,g})(u,v)=(-1)^{u\cdot M^{-1}v+g(M^{-1}v)}.
$$
Hence
$$
\mathcal Ff_{M,g}=f_{M,g}
\iff M^2=I\ \text{and}\ g\circ M=g.
$$
Also $f_{M,g}(0,y)$ determines $g(y)$, and then the character in $x$ determines $My$, so distinct pairs $(M,g)$ give distinct functions.

Put
$$
B_g(x,y)=g(x+y)+g(x)+g(y),\qquad
W_g(a)=\sum_{y\in E}(-1)^{g(y)+a\cdot y}.
$$
For quadratic $g$,
$$
W_g(a)^2=\sum_{t\in E}(-1)^{g(t)+a\cdot t}
\sum_{z\in E}(-1)^{B_g(z,t)}.
$$
The inner sum is $2^8$ on $\operatorname{rad}B_g$ and $0$ elsewhere. Thus $|W_g(a)|=16$ for every $a$ exactly when $B_g$ is nondegenerate: if the radical were nonzero, choose $a$ agreeing with the linear function $g$ on the radical to obtain $W_g(a)^2>2^8$.

For a fixed nondegenerate alternating form $B$, every quadratic refinement is $q_a(x)=q(x)+B(a,x)$, and
$$
q(x)+B(a,x)=q(x+a)+q(a)
$$
gives $W_{q_a}(0)=(-1)^{q(a)}W_q(0)$. A positive refinement has $136$ zeros because its zero and one counts have sum $256$ and difference $16$. Hence exactly $136=2^3\cdot17$ refinements have positive Walsh sign.

Every nondegenerate alternating form has a symplectic basis, so $\operatorname{GL}(2m,2)$ acts transitively on them with stabilizer $\operatorname{Sp}(2m,2)$. Orbit-stabilizer and successive choice of symplectic pairs give
$
\alpha_{2m}=\frac{|\operatorname{GL}(2m,2)|}{\prod_{j=1}^{m}(2^{2j}-1)2^{2j-1}}.
$
For $m=4$,
$
|\operatorname{GL}(8,2)|=2^{28}\prod_{i=1}^{8}(2^i-1),
$
hence
$
\alpha_8=2^{12}\frac{(1)(3)(7)(15)(31)(63)(127)(255)}{(3)(15)(63)(255)}
=2^{12}\cdot7\cdot31\cdot127.
$
The number of admissible positive quadratic phases is consequently
$$
N_+=136\alpha_8=2^{15}\cdot7\cdot17\cdot31\cdot127.
$$

It remains to identify their common isometry type. In a symplectic basis, each two-dimensional summand has the form
$$
Q_{a,b}(x,y)=xy+ax+by.
$$
The forms $Q_{0,0},Q_{1,0},Q_{0,1}$ are hyperbolic: respectively $(e,f)$, $(f,e+f)$, and $(e,e+f)$ are singular symplectic pairs. The remaining plane $A=Q_{1,1}$ has value $1$ on every nonzero vector and Walsh sum $-2$. Moreover $A\perp A$ is hyperbolic: for symplectic bases $e_i,f_i$ of the two copies, the vectors
$$
u_1=f_1+f_2,\quad v_1=f_1+e_2,
$$
$$
u_2=e_1+e_2+f_2,\quad v_2=e_1+f_1+e_2+f_2
$$
are singular and satisfy $B(u_i,v_j)=\delta_{ij}$, with all other pairings among them zero. Thus a positive Walsh sign means an even number of $A$-planes, which pair off, so every admissible $g$ is equivalent to the split form $H^{\perp4}$ with $H(x,y)=xy$. Fix one such split form $q$ with polar form $B$.

Step 2: Convert the requested Walsh sum into a signed fixed-vector sum
For a fixed $f_{M,g}$ and $b\in E$, we have $f_{M,g}(x,0)=1$ and
$
f_{M,g}(x,b)=(-1)^{x\cdot Mb+g(b)}.
$
Hence character orthogonality gives
$
2^{-8}\sum_{x\in E}
f_{M,g}(x,0)\overline{f_{M,g}(x,b)}(-1)^{b\cdot x}
=(-1)^{g(b)}\mathbf 1_{\{b=Mb\}}.
$
Therefore the inner sum over nonzero $b$ in the problem equals
$
\sum_{\substack{0\ne b\in E\\Mb=b}}(-1)^{g(b)}.
$
For a self-dual function, Step 1 shows that $M$ is an involution preserving $g$. Thus for the fixed split $q$ it remains to sum $(-1)^{q(b)}$ over the nonzero fixed vectors of every involution in $O(q)$.

Step 3: Parametrize the preserving involutions by residual data
Let $T\in O(q)$ satisfy $T^2=I$, write $T=I+N$, and set $R=\operatorname{im}N$. Then $N^2=0$. Preservation of $B$ gives
$$
B(Nx,y)+B(x,Ny)+B(Nx,Ny)=0.
$$
Replacing $y$ by $Ny$ gives $B(Nx,Ny)=0$, so $R$ is $B$-isotropic and
$$
B(Nx,y)=B(x,Ny),\qquad \ker N=R^\perp.
$$
For $u=Nx\in R$ define
$
\omega(u,v)=B(x,v)\qquad(v\in R).
$
It is well-defined because $\ker N=R^\perp$. For $u=Nx$ and $v=Ny$,
$
\omega(u,v)=B(x,Ny)=B(Nx,y)=\omega(v,u),
$
so it is symmetric. If $\omega(Nx,R)=0$, then $x\in R^\perp=\ker N$, so $Nx=0$; hence it is nondegenerate. Since $q(x+Nx)=q(x)$,
$
\omega(Nx,Nx)=B(x,Nx)=q(Nx),
$
so the diagonal of $\omega$ is $q|_R$.

Conversely, let $R$ be $B$-isotropic and let $\omega$ be nondegenerate symmetric on $R$ with $\omega(r,r)=q(r)$. The perfect pairing identifies $E/R^\perp$ with $R^*$, while nondegeneracy identifies $R$ with $R^*$ through $u\mapsto\omega(u,\cdot)$. Hence there is a unique linear map $N:E\to R$ satisfying
$
\omega(Nx,r)=B(x,r)
$
for every $r\in R$, and this map is onto $R$. Because $R$ is isotropic, $N|_R=0$, hence $N^2=0$; taking $r=Nx$ gives $q(x+Nx)=q(x)$. Thus $T=I+N$ is a preserving involution.

They are inverse: uniqueness recovers the original $N$, while from $(R,\omega)$ the constructed map is onto $R$ and the recovered form satisfies $\omega_N(Nx,r)=B(x,r)=\omega(Nx,r)$.

Step 4: Count the two residual types and evaluate their fixed-space Gauss sums
Let $I_r$ be the number of $r$-dimensional $B$-isotropic subspaces. Counting ordered isotropic bases gives
$$
I_r=\frac{\prod_{k=0}^{r-1}(2^{8-k}-2^k)}{\prod_{k=0}^{r-1}(2^r-2^k)},
$$
so
$$
(I_1,I_2,I_3,I_4)=(255,5355,11475,2295).
$$

Let $S_r$ count totally $q$-singular $r$-spaces. A singular basis $u_1,\ldots,u_k$ can be extended to hyperbolic pairs: choose $v_i$ with $B(u_i,v_i)=1$, orthogonalize against the earlier pairs, and replace $v_i$ by $v_i+q(v_i)u_i$ to make it singular. Hence $U^\perp/U$ is again split. A split $2m$-space has
$$
2^m+(2^m-1)2^{m-1}=2^{2m-1}+2^{m-1}
$$
zeros, since for $q(x,y)=x\cdot y$ there are $2^m$ choices when $x=0$ and $2^{m-1}$ choices of $y$ for each $x\ne0$. Thus it has $(2^{m-1}+1)(2^m-1)$ nonzero singular vectors. If $U$ is a totally singular $k$-space and $z\in U^\perp$, then for every $u\in U$,
$
q(z+u)=q(z)+q(u)+B(z,u)=q(z).
$
Therefore $q$ is constant on each coset of $U$ in $U^\perp$, so every nonzero singular vector of $U^\perp/U$ has exactly $2^k$ singular lifts. This explains the factor $2^k$ at the $k$th extension step. Extending ordered singular bases gives
$
S_r=\frac{\prod_{k=0}^{r-1}2^k(2^{3-k}+1)(2^{4-k}-1)}{\prod_{k=0}^{r-1}(2^r-2^k)},
$
so
$$
(S_1,S_2,S_3,S_4)=(135,1575,2025,270).
$$

Because $B|_R=0$, the restriction $q|_R$ is linear. If $q|_R=0$, admissible $\omega$ are nondegenerate alternating forms, so there are $\alpha_r$ choices for even $r$ and none for odd $r$. The total number of involutions of this residual type is
$$
C_0=1+S_2\alpha_2+S_4\alpha_4
=1+1575+270\cdot28=9136.
$$
If $q|_R\ne0$, choose a basis with $q|_R=x_1$ and write
$
[\omega]=\begin{pmatrix}1&b^T\\ b&A\end{pmatrix},
$
where $A$ is alternating. Put $\alpha_0=1$.

For odd $r$, the matrix $A$ has even size. If $A$ is nondegenerate, then $A^{-1}$ is alternating, so $b^TA^{-1}b=0$ and the Schur complement is $1$; hence the block is nondegenerate. Conversely, if $A$ is degenerate, its rank is even, so its radical has even dimension at least $2$. A linear functional cannot be nonzero on every vector of such a space, so there is some $0\ne w\in\operatorname{rad}A$ with $b^Tw=0$. Then
$
\begin{pmatrix}1&b^T\\ b&A\end{pmatrix}
\binom{0}{w}=0,
$
and the block is degenerate. Thus nondegeneracy is equivalent to nondegeneracy of $A$, giving $2^{r-1}\alpha_{r-1}$ choices.

For even $r$, $A$ has odd size, so $\dim\operatorname{rad}A$ is odd. If it is at least $3$, some $0\ne w$ in the radical satisfies $b^Tw=0$, making $(0,w)$ radical for the block. Hence nondegeneracy requires $\operatorname{rad}A=\langle w\rangle$ and $b^Tw=1$. Conversely, if these hold and $(c,u)$ is radical, then $cb+Au=0$; pairing with $w$ gives $c=0$, then $u\in\langle w\rangle$, and the first row gives $u=0$. Thus the block is nondegenerate.

There are $(2^{r-1}-1)\alpha_{r-2}$ choices for $A$: choose its one-dimensional radical and then a nondegenerate alternating form on the quotient. For each such $A$, exactly $2^{r-2}$ vectors $b$ satisfy $b^Tw=1$. Hence the count is
$
(2^{r-1}-1)\alpha_{r-2}2^{r-2}.
$
Cancelling the factors in the formula from Step 1 gives
$
\alpha_{2m}=2^{m(m-1)}\prod_{j=1}^{m}(2^{2j-1}-1),
$
so for even $r$,
$
\frac{\alpha_r}{\alpha_{r-2}}
=2^{r-2}(2^{r-1}-1).
$
Therefore
$
(2^{r-1}-1)\alpha_{r-2}2^{r-2}=\alpha_r.
$
Therefore
$
\begin{aligned}
C_1
&=(I_1-S_1)+(I_2-S_2)+4(I_3-S_3)+28(I_4-S_4)\\
&=120+3780+4\cdot9450+28\cdot2025\\
&=120+3780+37800+56700=98400
\end{aligned}
$
is the total number of involutions with $q|_R\ne0$.

Now $\operatorname{Fix}(T)=R^\perp$. If $q|_R=0$, then $q$ descends to the split form on $R^\perp/R$. Its zero-frequency Walsh sum is $2^{4-r}$, and each quotient vector has $2^r$ lifts on which $q$ is constant. Hence
$$
\sum_{x\in\operatorname{Fix}(T)}(-1)^{q(x)}=2^r2^{4-r}=16,
$$
so the nonzero fixed vectors contribute $15$ to the requested inner sum.

If $q|_R\ne0$, choose $r_0\in R$ with $q(r_0)=1$. Translation by $r_0$ preserves $R^\perp$ and flips $(-1)^{q(x)}$, because $B(x,r_0)=0$ on $R^\perp$. Hence the full fixed-space sum is $0$, and after removing $x=0$ the nonzero fixed vectors contribute $-1$.

Therefore the total requested contribution over all preserving involutions of the fixed split form is
$$
K=15C_0-C_1=15\cdot9136-98400=38640
=2^4\cdot3\cdot5\cdot7\cdot23.
$$

Step 5: Sum over all self-dual quadratic phases
Every admissible positive quadratic form has the same value $K$, and Step 1 shows that the parametrization by $(M,g)$ is injective. Hence the requested aggregate is
$$
N_+K
=(2^{15}\cdot7\cdot17\cdot31\cdot127)
(2^4\cdot3\cdot5\cdot7\cdot23).
$$
Thus
$$
N_+K=2^{19}\cdot3\cdot5\cdot7^2\cdot17\cdot23\cdot31\cdot127.
$$

Final Answer: $\boxed{2^{19}\cdot3\cdot5\cdot7^2\cdot17\cdot23\cdot31\cdot127}$

---

## Answer

$2^{19}\cdot3\cdot5\cdot7^2\cdot17\cdot23\cdot31\cdot127$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact scalar

---

## Solution Concepts

- Walsh Fourier self-duality
- ambiguity spectrum and character orthogonality
- quadratic forms over finite fields
- orthogonal involutions and residual forms
- fixed-space Gauss sums
