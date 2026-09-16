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
Comparing this with $f_{M,g}(u,v)=(-1)^{u\cdot Mv+g(v)}$ for every $u,v$ gives
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
The inner sum is $2^8$ for $t\in\operatorname{rad}B_g$ and $0$ otherwise. If $B_g$ is nondegenerate, only $t=0$ contributes and $|W_g(a)|=16$ for every $a$. Conversely, on $\operatorname{rad}B_g$ the function $g$ is linear. If the radical were nonzero, choose $a$ whose restriction to the radical equals $g$. Then
$$
W_g(a)^2=2^8|\operatorname{rad}B_g|>2^8,
$$
contradicting $|W_g(a)|=16$. Thus the Walsh condition is equivalent to nondegeneracy of $B_g$.

We now derive the needed classification directly. Let $q$ be any quadratic form on $\mathbb F_2^{2m}$ with nondegenerate polar form $B$. Choose a symplectic basis
$$
e_1,f_1,\ldots,e_m,f_m,
\qquad
B(e_i,f_j)=\delta_{ij},
$$
with all other basis pairings zero. Put $x=\sum_i(x_ie_i+y_if_i)$. The split form
$$
h(x)=\sum_{i=1}^m x_i y_i
$$
has the same polar form as $q$. Hence $q-h$ has zero polar form and vanishes at $0$, so it is linear. Therefore
$$
q(x)=\sum_{i=1}^m\bigl(x_i y_i+a_i x_i+b_i y_i\bigr),
\qquad a_i,b_i\in\mathbb F_2.
$$
Thus $q$ is an orthogonal sum of two-dimensional forms
$$
Q_{a,b}(x,y)=xy+ax+by.
$$
There are only two plane types. If $(a,b)=(0,0)$, then $Q_{a,b}=H:=xy$. If $(a,b)=(1,0)$, the vectors $f,e+f$ are both singular and pair to $1$; if $(a,b)=(0,1)$, the vectors $e,e+f$ have the same property. Hence these two forms are also linearly equivalent to $H$. The remaining form
$$
A(x,y)=xy+x+y
$$
has value $1$ on every nonzero vector, so it is not equivalent to $H$.

Two copies of $A$ cancel. On $A\perp A$ with symplectic coordinates $(e_1,f_1,e_2,f_2)$, set
$$
u_1=f_1+f_2,\qquad v_1=f_1+e_2,
$$
$$
u_2=e_1+e_2+f_2,\qquad
v_2=e_1+f_1+e_2+f_2.
$$
A direct substitution gives
$$
q(u_1)=q(v_1)=q(u_2)=q(v_2)=0,
$$
and the polar pairings satisfy
$$
B(u_i,v_j)=\delta_{ij},
\qquad
B(u_i,u_j)=B(v_i,v_j)=0.
$$
Hence $u_1,v_1,u_2,v_2$ form a hyperbolic basis, proving
$$
A\perp A\cong H\perp H.
$$
Consequently every nondegenerate quadratic form in dimension $2m$ is equivalent to exactly one of
$$
H^{\perp m}
\qquad\text{or}\qquad
A\perp H^{\perp(m-1)}.
$$
To distinguish them, Walsh sums multiply under orthogonal direct sums, while
$$
W_H(0)=\sum_{x,y\in\mathbb F_2}(-1)^{xy}=2,
\qquad
W_A(0)=\sum_{x,y\in\mathbb F_2}(-1)^{xy+x+y}=-2.
$$
Therefore
$$
W_{H^{\perp m}}(0)=2^m,
\qquad
W_{A\perp H^{\perp(m-1)}}(0)=-2^m.
$$
So the sign of $2^{-m}W_q(0)$ determines the class, with positive sign giving the split class. Here $m=4$ and $W_g(0)=16$, hence every admissible $g$ is linearly equivalent to
$$
q_+(x)=x_1x_2+x_3x_4+x_5x_6+x_7x_8.
$$
Moreover, if $g=q_+\circ S$ for some $S\in\operatorname{GL}(8,2)$, then
$$
T\mapsto STS^{-1}
$$
is a bijection from the involutions preserving $g$ to the involutions preserving $q_+$. Thus every admissible $g$ has the same involution count, and it is legitimate to count using this one split model.

It remains to count how many admissible $g$ there are. Let $\alpha_{2m}$ be the number of nondegenerate alternating forms on a fixed $2m$-dimensional binary vector space. Every such form has a symplectic basis, obtained inductively by choosing a nonzero vector, choosing a partner pairing to $1$, and passing to their orthogonal complement. The general linear group is therefore transitive on these forms. For one fixed form, the same induction counts its ordered symplectic bases and gives
$$
|\operatorname{Sp}(2m,2)|
=\prod_{j=1}^{m}(2^{2j}-1)2^{2j-1}.
$$
Dividing $|\operatorname{GL}(2m,2)|$ by this stabilizer gives
$$
\alpha_{2m}
=2^{m(m-1)}\prod_{i=1}^{m}(2^{2i-1}-1).
$$
In dimension $8$ this is $\alpha_8=112881664$. For a fixed nondegenerate $B$, all of its quadratic refinements are
$$
q_a(x)=q(x)+B(a,x),\qquad a\in E,
$$
because the difference of two refinements is linear and nondegeneracy identifies every linear functional with $B(a,\cdot)$ for a unique $a$. Taking one plus refinement $q$, the identity
$$
q(x)+B(a,x)=q(x+a)+q(a)
$$
gives
$$
W_{q_a}(0)=(-1)^{q(a)}W_q(0).
$$
Since $W_q(0)=16$,
$$
\#q^{-1}(0)-\#q^{-1}(1)=16,
\qquad
\#q^{-1}(0)+\#q^{-1}(1)=256,
$$
so exactly $136$ refinements have positive Walsh sign. The number of admissible $g$ is therefore
$$
136\alpha_8=15351906304.
$$

Step 2: Encode every orthogonal involution by its residual space and Wall form

Fix the split form $q=q_+$ from Step 1 and let $B$ be its polar form. For an involution $T$ preserving $q$, write $T=I+N$. Then $N^2=0$. Put
$$
R=\operatorname{im}N.
$$
Because $T$ preserves $B$,
$$
B(Nx,y)+B(x,Ny)+B(Nx,Ny)=0.
$$
Replacing $y$ by $Ny$ and using $N^2=0$ gives $B(Nx,Ny)=0$, so $R$ is $B$-isotropic. The same identity becomes
$$
B(Nx,y)=B(x,Ny).
$$
An element $x$ lies in $\ker N$ exactly when the left side vanishes for every $y$, equivalently when $B(x,R)=0$. Therefore
$$
\ker N=R^{\perp}.
$$

For $u=Nx\in R$ and $v\in R$, define
$$
\omega(u,v)=B(x,v).
$$
This is well-defined because changing $x$ by an element of $\ker N=R^{\perp}$ does not change the value. If $\omega(Nx,v)=0$ for every $v\in R$, then $x\in R^{\perp}=\ker N$, so $Nx=0$, proving that $\omega$ is nondegenerate. For $u=Nx$ and $v=Ny$,
$$
\omega(u,v)=B(x,Ny)=B(Nx,y)=\omega(v,u),
$$
so $\omega$ is symmetric. The identity $q(Tx)=q(x)$ gives
$$
q(Nx)=B(x,Nx)=\omega(Nx,Nx).
$$
The diagonal of $\omega$ is exactly $q|_R$.

Conversely, let $R$ be any $B$-isotropic subspace and let $\omega$ be a nondegenerate symmetric form on $R$ satisfying
$$
\omega(r,r)=q(r)\qquad(r\in R).
$$
The map $x\mapsto B(x,\cdot)|_R$ has kernel $R^{\perp}$, so its image has dimension $\dim R$ and is all of $R^*$. Since $\omega$ identifies $R$ with $R^*$, there is a unique surjective linear map $N:E\to R$ such that
$$
\omega(Nx,r)=B(x,r)
\qquad(r\in R).
$$
Because $R$ is $B$-isotropic, $N$ vanishes on $R$, so $N^2=0$. Taking $r=Nx$ gives
$$
B(x,Nx)=\omega(Nx,Nx)=q(Nx),
$$
and then
$$
q(x+Nx)=q(x)+q(Nx)+B(x,Nx)=q(x).
$$
Therefore $T=I+N$ is an orthogonal involution with $\operatorname{im}N=R$. We have a bijection between orthogonal involutions and pairs $(R,\omega)$ with these properties.

Step 3: Count the residual data with one parity formula

Let $I_r$ be the number of $r$-dimensional $B$-isotropic subspaces and $S_r$ the number of $r$-dimensional totally $q$-singular subspaces. To count $I_r$, build an ordered basis of an isotropic $r$-space. After $k$ independent isotropic vectors span $U$, the next vector can be any element of $U^{\perp}\setminus U$, giving $2^{8-k}-2^k$ choices. Dividing by the number $\prod_{k=0}^{r-1}(2^r-2^k)$ of ordered bases of an $r$-space gives
$$
I_r=
\frac{\prod_{k=0}^{r-1}(2^{8-k}-2^k)}
{\prod_{k=0}^{r-1}(2^r-2^k)}.
$$

For $S_r$, suppose $U$ is already totally singular of dimension $k$. A hyperbolic basis for the split form can be chosen with the first $k$ singular basis vectors spanning $U$. The quotient $U^{\perp}/U$ then retains $4-k$ hyperbolic pairs, so it is split of dimension $2(4-k)$. In a split $2m$-space written as $q(a,b)=a\cdot b$, the number of nonzero singular vectors is
$$
(2^{m-1}+1)(2^m-1).
$$
For $a=0$ there are $2^m$ choices of $b$, while for each nonzero $a$ there are $2^{m-1}$ vectors $b$ with $a\cdot b=0$; removing the zero vector gives the displayed count. Each nonzero singular vector of $U^{\perp}/U$ has $2^k$ singular lifts, so at stage $k$ there are
$$
2^k(2^{3-k}+1)(2^{4-k}-1)
$$
possible next vectors. Dividing the product of these extension counts by the same ordered-basis denominator gives $S_r$. The values needed here are
$$
I_1=255,\quad S_1=135,\quad I_2=5355,
$$
$$
I_3=11475,\quad S_3=2025,\quad I_4=2295.
$$

Because $B|_R=0$, the restriction $\ell=q|_R$ is linear. We now count the nondegenerate symmetric forms $\omega$ with diagonal $\ell$. If $\ell=0$, then $\omega$ is alternating, so there are $\alpha_r$ choices for even $r$ and none for odd $r$. If $\ell\neq0$, choose $e$ with $\ell(e)=1$ and put $H=\ker\ell$. In the decomposition $R=\langle e\rangle\oplus H$,
$$
[\omega]=
\begin{pmatrix}
1&b^T\\
b&A
\end{pmatrix},
$$
where $A$ is alternating.

When $r$ is odd, $H$ has even dimension. If $A$ is nondegenerate, then $A^{-1}$ is alternating, so $b^TA^{-1}b=0$ and the Schur complement has determinant $1$; the full matrix is nondegenerate. If $A$ is singular, its radical has even dimension at least $2$, and one extra row and column cannot remove every radical direction. The full matrix is then singular. This leaves $2^{r-1}\alpha_{r-1}$ choices when $\ell\neq0$ and $r$ is odd.

When $r$ is even, $H$ has odd dimension. The full matrix is nondegenerate exactly when $A$ has a one-dimensional radical and $b$ is nonzero on that radical; if the radical of $A$ were larger, one functional $b$ could not kill all of it. To count such $A$, choose its radical line in $2^{r-1}-1$ ways and then choose a nondegenerate alternating form on the quotient, giving $(2^{r-1}-1)\alpha_{r-2}$ choices. For each $A$, exactly $2^{r-2}$ functionals $b$ are nonzero on the radical. By the formula for $\alpha_r$ in Step 1,
$$
(2^{r-1}-1)\alpha_{r-2}2^{r-2}=\alpha_r.
$$
Every $B$-isotropic $R$ therefore contributes $\alpha_r$ forms when $r$ is even. For odd $r$, only the $I_r-S_r$ subspaces with $q|_R\neq0$ contribute, each with $2^{r-1}\alpha_{r-1}$ forms.

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

Step 1 gives $15351906304$ admissible plus-type quadratic forms $g$, and Step 3 gives $107536$ involutions preserving each one. The injectivity proved in Step 1 now gives
$$
15351906304\cdot107536=1650882596306944.
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
- quadratic forms over finite fields
- orthogonal involutions
- Wall forms
- isotropic subspace counting
