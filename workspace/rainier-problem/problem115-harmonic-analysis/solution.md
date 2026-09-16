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

To count nondegenerate alternating forms on a $2m$-space, choose symplectic pairs successively. When the remaining dimension is $2j$, there are $(2^{2j}-1)2^{2j-1}$ choices for the next ordered pair. Therefore
$$
\alpha_{2m}=\frac{|\operatorname{GL}(2m,2)|}{\prod_{j=1}^{m}(2^{2j}-1)2^{2j-1}},
$$
so
$$
\alpha_8=2^{12}\cdot7\cdot31\cdot127.
$$
The number of admissible positive quadratic phases is consequently
$$
N_+=136\alpha_8=2^{15}\cdot7\cdot17\cdot31\cdot127.
$$
All such forms are split and are equivalent under $\operatorname{GL}(8,2)$, so their preserving involutions have the same structure. Fix one split form $q$ with polar form $B$.

Step 2: Convert the ambiguity trace into a signed fixed-vector sum
For the vertical ambiguity spectrum from the prompt,
$$
\mathcal A_h(b,\xi)=2^{-8}\sum_{x\in E}h(x,0)\overline{h(x,b)}(-1)^{\xi\cdot x},
$$
we have $f_{M,g}(x,0)=1$ and
$$
f_{M,g}(x,b)=(-1)^{x\cdot Mb+g(b)}.
$$
Hence character orthogonality gives the exact point-mass identity
$$
\mathcal A_{f_{M,g}}(b,\xi)
=(-1)^{g(b)}\mathbf 1_{\{\xi=Mb\}}.
$$
Therefore the nonzero diagonal ambiguity mass is
$$
\mathscr T(f_{M,g})
=\sum_{0\ne b\in E}\mathcal A_{f_{M,g}}(b,b)
=\sum_{\substack{0\ne b\in E\\Mb=b}}(-1)^{g(b)}.
$$
For a self-dual function, Step 1 shows that $M$ is an involution preserving $g$. Thus for a fixed split $q$ it remains to sum $(-1)^{q(b)}$ over the nonzero fixed vectors of every involution in $O(q)$.

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
$$
\omega(u,v)=B(x,v)\qquad(v\in R).
$$
This is well-defined, symmetric, and nondegenerate. Since $q(x+Nx)=q(x)$,
$$
\omega(Nx,Nx)=B(x,Nx)=q(Nx),
$$
so the diagonal of $\omega$ is $q|_R$.

Conversely, let $R$ be $B$-isotropic and let $\omega$ be nondegenerate symmetric on $R$ with $\omega(r,r)=q(r)$. The perfect pairing identifies $E/R^\perp$ with $R^*$, so there is a unique $N:E\to R$ satisfying
$$
\omega(Nx,r)=B(x,r).
$$
Because $R$ is isotropic, $N|_R=0$, hence $N^2=0$; taking $r=Nx$ gives $q(x+Nx)=q(x)$. Thus $T=I+N$ is a preserving involution. This establishes a bijection between such involutions and residual pairs $(R,\omega)$.

Step 4: Count the two residual types and evaluate their fixed-space Gauss sums
Let $I_r$ be the number of $r$-dimensional $B$-isotropic subspaces. Counting ordered isotropic bases gives
$$
I_r=\frac{\prod_{k=0}^{r-1}(2^{8-k}-2^k)}{\prod_{k=0}^{r-1}(2^r-2^k)},
$$
so
$$
(I_1,I_2,I_3,I_4)=(255,5355,11475,2295).
$$
Let $S_r$ count totally $q$-singular $r$-spaces. If $U$ is a singular $k$-space, then $U^\perp/U$ is split of dimension $2(4-k)$ and has $(2^{3-k}+1)(2^{4-k}-1)$ nonzero singular vectors. Hence
$$
S_r=\frac{\prod_{k=0}^{r-1}2^k(2^{3-k}+1)(2^{4-k}-1)}{\prod_{k=0}^{r-1}(2^r-2^k)},
$$
which yields
$$
(S_1,S_2,S_3,S_4)=(135,1575,2025,270).
$$

Because $B|_R=0$, the restriction $q|_R$ is linear. If $q|_R=0$, admissible $\omega$ are nondegenerate alternating forms, so there are $\alpha_r$ choices for even $r$ and none for odd $r$. The total number of involutions of this residual type is therefore
$$
C_0=1+S_2\alpha_2+S_4\alpha_4
=1+1575+270\cdot28=9136.
$$
If $q|_R\ne0$, choose a basis with $q|_R=x_1$ and write
$$
[\omega]=\begin{pmatrix}1&b^T\\ b&A\end{pmatrix},
$$
where $A$ is alternating. For odd $r$, nondegeneracy is equivalent to nondegeneracy of $A$, giving $2^{r-1}\alpha_{r-1}$ choices. For even $r$, $A$ must have a one-dimensional radical and $b$ must be nonzero on it; the count is
$$
(2^{r-1}-1)\alpha_{r-2}2^{r-2}=\alpha_r.
$$
Thus the total number of involutions with $q|_R\ne0$ is
$$
C_1=(I_1-S_1)+ (I_2-S_2)+4(I_3-S_3)+28(I_4-S_4)=98400.
$$

Now $\operatorname{Fix}(T)=R^\perp$. If $q|_R=0$, then $q$ descends to a split nondegenerate form on $R^\perp/R$. Its zero-frequency Walsh sum is $2^{4-r}$, and each coset lifts through $2^r$ elements on which $q$ is constant. Hence
$$
\sum_{x\in\operatorname{Fix}(T)}(-1)^{q(x)}=2^r2^{4-r}=16,
$$
so the nonzero fixed vectors contribute $15$ to $\mathscr T$.

If $q|_R\ne0$, choose $r_0\in R$ with $q(r_0)=1$. Translation by $r_0$ preserves $R^\perp$ and flips the sign of $(-1)^{q(x)}$, because $B(x,r_0)=0$ on $R^\perp$. Hence the full fixed-space sum is $0$, and after removing $x=0$ the nonzero fixed vectors contribute $-1$.

Therefore the total diagonal ambiguity mass over all preserving involutions of the fixed split form is
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
