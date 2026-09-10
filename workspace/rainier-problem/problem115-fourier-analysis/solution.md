## Steps

Step 1: Characterize Walsh self-duality

For an affine permutation $\pi$ and an admissible quadratic Boolean function $g$, put
$$
f_{\pi,g}(x,y)=(-1)^{x\cdot\pi(y)+g(y)}.
$$
For $(u,v)\in E\times E$,
$$
(\mathcal Ff_{\pi,g})(u,v)
=2^{-8}\sum_{y\in E}(-1)^{g(y)+y\cdot u}
\sum_{x\in E}(-1)^{x\cdot(\pi(y)+v)}.
$$
The inner sum is $2^8$ exactly when $\pi(y)=v$, and otherwise it is $0$. Hence
$$
(\mathcal Ff_{\pi,g})(u,v)
=(-1)^{u\cdot\pi^{-1}(v)+g(\pi^{-1}(v))}.
$$
Comparing with
$$
f_{\pi,g}(u,v)=(-1)^{u\cdot\pi(v)+g(v)}
$$
for every $u,v$ shows that
$$
\mathcal Ff_{\pi,g}=f_{\pi,g}
\iff
\pi^2=\operatorname{id}_E,
\qquad g\circ\pi=g.
$$
The parametrization is injective: for fixed $y$, the character in $x$ recovers $\pi(y)$, while $f_{\pi,g}(0,y)=(-1)^{g(y)}$ recovers $g(y)$.

Step 2: Parametrize the affine involutions

Write
$$
\pi(v)=Mv+c,
\qquad M\in\operatorname{GL}(8,2),\ c\in E,
$$
and put $N=M+I$. Since the characteristic is $2$,
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
For fixed $r$, choose $U$, then $K\supseteq U$, then the induced isomorphism $E/K\to U$. Thus the number $A_r$ of square-zero endomorphisms of rank $r$ is
$$
A_r=\binom{8}{r}_2\binom{8-r}{r}_2|\operatorname{GL}(r,2)|.
$$
Therefore
$$
A_0=1,
\quad A_1=32385,
\quad A_2=42165270,
$$
$$
A_3=2529916200,
\quad A_4=4047865920.
$$

Step 3: Use the bent condition to eliminate fixed-point-free translations

For a quadratic $g$ with $g(0)=0$, define its polar form
$$
B_g(x,y)=g(x+y)+g(x)+g(y).
$$
This is alternating bilinear. If
$$
W_g(a)=\sum_{x\in E}(-1)^{g(x)+a\cdot x},
$$
then, after writing the second summation variable as $x+h$,
$$
W_g(a)^2
=\sum_{h\in E}(-1)^{g(h)+a\cdot h}
\sum_{x\in E}(-1)^{B_g(x,h)}.
$$
The inner sum is $2^8$ exactly for $h$ in the radical of $B_g$ and is $0$ otherwise. Hence $|W_g(a)|=16$ for every $a$ exactly when $B_g$ is nondegenerate. Thus the stated Walsh condition is equivalent to $g$ being a nonsingular quadratic form.

Assume now that $g\circ\pi=g$. Polarizing this identity shows that $M$ preserves $B_g$. Also $g(c)=g(\pi(0))=g(0)=0$. If $x\in K=\ker N$, then $Mx=x$, so
$$
0=g(x+c)+g(x)=B_g(x,c).
$$
Therefore
$$
c\in K^{\perp_{B_g}}.
$$
For $y=Nv\in U$ and $x\in K$, the $B_g$-invariance of $M$ gives
$$
B_g(v+Nv,x)=B_g(Mv,Mx)=B_g(v,x),
$$
so $B_g(Nv,x)=0$. Hence $U\subseteq K^{\perp_{B_g}}$. Since $B_g$ is nondegenerate, both spaces have dimension $r$, and therefore
$$
K^{\perp_{B_g}}=U.
$$
Thus every admissible affine involution must actually satisfy
$$
c\in U=\operatorname{im}N.
$$
There are $2^r$ such translations. If $c=Nt$, translation by $t$ conjugates $v\mapsto(I+N)v+c$ to $v\mapsto(I+N)v$, and
$$
g(v)\longmapsto g(v+t)+g(t)
$$
preserves degree, bentness, the condition $g(0)=0$, and invariance. Hence each $c\in U$ contributes the same number as $c=0$.

Step 4: Count the invariant nondegenerate polar forms

Fix a rank-$r$ map $N$. Choose coordinates
$$
E=U\oplus W\oplus Z,
\qquad \dim U=\dim W=r,
\qquad \dim Z=s:=8-2r,
$$
so that
$$
N(u,w,z)=(w,0,0),
\qquad
M(u,w,z)=(u+w,w,z).
$$
Write the matrix of an alternating form $B$ in these coordinates. The identity
$$
B(Mx,My)=B(x,y)
$$
is equivalent to
$$
B=
\begin{pmatrix}
0&R&0\\
R&S&T\\
0&T^T&D
\end{pmatrix},
$$
where $R$ is symmetric $r\times r$, $S$ is alternating $r\times r$, $T$ is arbitrary $r\times s$, and $D$ is alternating $s\times s$.

Such a matrix is nondegenerate exactly when both $R$ and $D$ are nondegenerate. Indeed, singular $R$ gives a radical vector in $U$, while for invertible $R$ block elimination gives
$$
\det B=\det(R)^2\det(D).
$$
Let $\sigma_r$ be the number of invertible symmetric $r\times r$ binary matrices, and let $\alpha_s$ be the number of nondegenerate alternating $s\times s$ binary matrices. Then the number $Q_r$ of possible nondegenerate invariant polar forms is
$$
Q_r=\sigma_r\,2^{\binom r2+rs}\alpha_s.
$$
For alternating forms, all nondegenerate forms are one congruence orbit, so
$$
\alpha_{2m}=\frac{|\operatorname{GL}(2m,2)|}{|\operatorname{Sp}(2m,2)|},
$$
where
$$
|\operatorname{GL}(k,2)|=\prod_{j=0}^{k-1}(2^k-2^j),
\qquad
|\operatorname{Sp}(2m,2)|=2^{m^2}\prod_{i=1}^m(2^{2i}-1).
$$
Thus
$$
\alpha_0=1,\quad \alpha_2=1,\quad \alpha_4=28,
\quad \alpha_6=13888,\quad \alpha_8=112881664.
$$
For symmetric forms, a nonsingular form in odd dimension $2m+1$ is necessarily nonalternating and has one congruence class; its stabilizer is $\operatorname{Sp}(2m,2)$. In even dimension $2m$, there is the alternating class plus one nonalternating class. For a nonalternating form, the canonical vector $w$ defined by $B(x,x)=B(x,w)$ is fixed by every isometry, and the induced action on $w^\perp/\langle w\rangle$ is symplectic; the kernel has size $2^{2m-1}$. Hence
$$
\sigma_{2m+1}=\frac{|\operatorname{GL}(2m+1,2)|}{|\operatorname{Sp}(2m,2)|},
$$
$$
\sigma_{2m}=\alpha_{2m}
+\frac{|\operatorname{GL}(2m,2)|}{2^{2m-1}|\operatorname{Sp}(2m-2,2)|}
\qquad(m\ge1).
$$
Together with $\sigma_0=1$, this gives
$$
\sigma_0=1,\quad \sigma_1=1,\quad \sigma_2=4,
\quad \sigma_3=28,\quad \sigma_4=448.
$$
Consequently
$$
\begin{array}{c|ccccc}
r&0&1&2&3&4\\ \hline
Q_r&112881664&888832&57344&14336&28672
\end{array}
$$

For a fixed invariant polar form, the quadratic polynomial itself is determined up to a linear form. In the above coordinates, invariance under $(u,w,z)\mapsto(u+w,w,z)$ forces the $r$ linear coefficients on $U$ and leaves the $r+s=8-r$ coefficients on $W\oplus Z$ free. Hence each polar form lifts to exactly
$$
2^{8-r}
$$
invariant quadratic functions $g$ with $g(0)=0$.

Step 5: Sum over all ranks

For each square-zero $N$ of rank $r$, there are $2^r$ admissible translations $c\in U$, and for each such $c$ there are
$$
Q_r2^{8-r}
$$
admissible bent quadratic functions. Thus the contribution of rank $r$ is
$$
A_r\,2^r\,Q_r\,2^{8-r}=256A_rQ_r.
$$
Therefore the required number is
$$
256\sum_{r=0}^4 A_rQ_r.
$$
Using the values above,
$$
\sum_{r=0}^4 A_rQ_r
=154776113250304,
$$
so
$$
256\cdot154776113250304
=39622684992077824.
$$

Final Answer: $\boxed{39622684992077824}$

---

## Answer

$39622684992077824$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact scalar

---

## Solution Concepts

- Walsh--Fourier self-duality
- quadratic bent Boolean functions
- affine involutions over $\mathbb F_2$
- symplectic polar forms
- invariant bilinear-form counting

---

## Black-Box Audit — no issues found
