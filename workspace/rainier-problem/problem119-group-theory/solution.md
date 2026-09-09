## Steps

Step 1: Reduce the problem to a Burnside count on symmetric matrices

Let
$$
U=\mathbb F_p^3,\qquad Z=Z(G)=\{(0,0,t):t\in\mathbb F_p\}.
$$
The commutator is
$$
[(u,v,t),(u',v',t')]=(0,0,u\cdot v'-u'\cdot v).
$$
Hence every admissible subgroup is uniquely
$$
A_T=\{(u,Tu,t):u\in U,\ t\in\mathbb F_p\},
$$
where $T$ is symmetric and invertible. The diagonal intersection has order $p^{1+\dim\ker(T-I)}$, so admissibility is equivalent to
$$
T=T^T,\qquad \det T\ne0,\qquad \dim\ker(T-I)=1.
$$
Let $X$ be this set of matrices. Since
$$
Q\cdot A_T=A_{QTQ^{-1}},
$$
ordered subgroup pairs correspond to $X\times X$ with diagonal conjugation. Conjugation by $-Q$ equals conjugation by $Q$, so the orbit set is unchanged if $\mathcal O$ is replaced by $SO_3(\mathbb F_p)$. Put
$$
F(Q)=\#\{T\in X:QT=TQ\}.
$$
Burnside's lemma gives
$$
\#(X\times X)/\mathcal O
=\frac1{|SO_3(\mathbb F_p)|}\sum_{Q\in SO_3(\mathbb F_p)}F(Q)^2.
$$

Step 2: Count the element types in $SO_3(\mathbb F_p)$

For $q(x)=x\cdot x$, choose a Witt basis with Gram matrix
$$
J=\begin{pmatrix}0&1&0\\1&0&0\\0&0&d\end{pmatrix},\qquad d\ne0.
$$
Such a basis exists because the two sets of squares $\{a^2\}$ and $\{-1-b^2\}$, each of size $(p+1)/2$, intersect. An isotropic line with first coordinate nonzero has a unique representative $e+yf+zh$ with $2y+dz^2=0$, giving $p$ lines, and $\langle f\rangle$ gives one more. Thus there are $p+1$ isotropic lines and $p^2$ nonisotropic lines.

Let $n_+$ count nonisotropic lines $L$ for which $L^{\perp}$ is split and $n_-$ those for which it is anisotropic. Counting incidences $(\ell,L)$ with $\ell$ isotropic and $L\perp\ell$ gives
$$
2n_+=p(p+1),
$$
because each isotropic $\ell$ is perpendicular to $p$ nonisotropic lines, while a split plane contains two isotropic lines and an anisotropic plane none. Hence
$$
n_+=\frac{p(p+1)}2,\qquad n_-=\frac{p(p-1)}2.
$$

A nonidentity semisimple $Q\in SO_3$ has a unique nonisotropic axis $L$ and is $1_L\oplus R$. On a split plane, $SO_2$ has order $p-1$; on an anisotropic plane, identified with $\mathbb F_{p^2}$ with its norm form, the norm-one rotations have order $p+1$. Each axis has one involution $R=-I$. Therefore there are $n_+$ split-axis involutions, $n_-$ anisotropic-axis involutions, and
$$
n_+(p-3)+n_-(p-1)=p(p^2-2p-1)
$$
other semisimple elements.

For an isotropic axis $\langle e\rangle$, the nonidentity unipotents are
$$
Q_c=\begin{pmatrix}1&-dc^2/2&-dc\\0&1&0\\0&c&1\end{pmatrix},\qquad c\ne0.
$$
Thus each isotropic line supports $p-1$ of them, giving $p^2-1$ unipotents. Consequently
$$
|SO_3(\mathbb F_p)|
=1+n_+(p-2)+n_-p+(p^2-1)
=p(p^2-1).
$$

Step 3: Compute the fixed-point numbers $F(Q)$

Set
$$
M=p(p-1)^2.
$$
On a split plane, a self-adjoint map has form
$$
B=\begin{pmatrix}a&b\\c&a\end{pmatrix}.
$$
Each equation $\det B=0$ and $\det(B-I)=0$ has $p^2$ solutions, and both hold exactly when $a=1/2$ and $bc=1/4$, giving $p-1$ solutions. Hence
$$
S_+=\#\{B:\det B\det(B-I)\ne0\}=M-1.
$$
If $C=B-I$ has rank one, then $C=\begin{pmatrix}x&b\\c&x\end{pmatrix}$ with $x^2=bc$, while $I+C$ is invertible exactly when $1+2x\ne0$. The case $x=0$ gives $2(p-1)$ nonzero pairs $(b,c)$, and the $p-2$ allowed nonzero values of $x$ each give $p-1$ pairs. Thus
$$
R_+=p(p-1).
$$

On an anisotropic plane, every self-adjoint map is uniquely
$$
B(z)=az+b\overline z,\qquad a\in\mathbb F_p,\ b\in\mathbb F_{p^2},
$$
with
$$
\det B=a^2-N(b),\qquad \det(B-I)=(a-1)^2-N(b).
$$
A nonzero norm fiber has $p+1$ elements, so the same inclusion-exclusion gives
$$
S_-=M+1.
$$
For $C=B-I$, rank one requires $x^2=N(b)$. The case $x=0$ gives only $C=0$, while each nonzero $x\ne-1/2$ gives $p+1$ choices of $b$. Hence
$$
R_-=(p-2)(p+1).
$$

For a fixed isotropic $1$-eigenline, write
$$
T=\begin{pmatrix}1&a&dr\\0&1&0\\0&r&j\end{pmatrix}.
$$
Here $j\ne0$ and the fixed space is exactly the chosen line iff $a(j-1)-dr^2\ne0$. For each of the $p-1$ nonzero $j$, there are $p(p-1)$ allowed pairs $(a,r)$, so an isotropic line contributes $M$ matrices. Therefore
$$
F(I)=|X|=(p+1)M+n_+S_++n_-S_-=p^5-p^4-p^2.
$$

If $Q$ is semisimple and not an involution, write $Q=1_L\oplus R$ with $R\ne\pm I$. The centralizer of $R$ on its plane is $\mathbb F_p[R]$. Since $R^*=R^{-1}$, a commuting self-adjoint map $aI+bR$ has $b=0$. Thus an admissible commuting $T$ is $1_L\oplus sI$ with $s\in\mathbb F_p^\times\setminus\{1\}$, so
$$
F(Q)=p-2.
$$

For an involution $Q=1_L\oplus(-I)$, a commuting $T$ is $t\oplus B$. If $t=1$, the plane block contributes $S_+$ or $S_-$; if $t\ne1$, there are $p-2$ choices of $t$ and the plane block contributes $R_+$ or $R_-$. Hence
$$
F_+=S_++(p-2)R_+=2p^3-5p^2+3p-1,
$$
$$
F_-=S_-+(p-2)R_-=2p^3-5p^2+p+5.
$$

If $Q$ is nonidentity unipotent and $N=Q-I$, then $N$ is one Jordan block of size three, so every commuting endomorphism is $aI+bN+cN^2$. Since
$$
N^*=-N+N^2,
$$
self-adjointness forces $b=0$. For $T=aI+cN^2$, the kernel of $T-I$ has dimension $0$, $2$, or $3$, never $1$. Thus
$$
F(Q)=0.
$$

Step 4: Evaluate Burnside's sum

Using the element counts from Step 2 and the fixed-point counts from Step 3 gives
$$
\frac{F(I)^2+n_+F_+^2+n_-F_-^2+p(p^2-2p-1)(p-2)^2}{p(p^2-1)}.
$$
The numerator expands to
$$
p^{10}-2p^9+5p^8-22p^7+35p^6-7p^5-42p^4+47p^3+p^2-16p
$$
and factors as
$$
p(p-1)(p+1)\left(p^7-2p^6+6p^5-24p^4+41p^3-31p^2-p+16\right).
$$
After division by $p(p^2-1)$, the required number is
$$
p^7-2p^6+6p^5-24p^4+41p^3-31p^2-p+16.
$$

Final Answer: $\boxed{p^7-2p^6+6p^5-24p^4+41p^3-31p^2-p+16}$

---

## Answer

$p^7-2p^6+6p^5-24p^4+41p^3-31p^2-p+16$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- extraspecial finite group
- orthogonal group actions
- Burnside lemma
- self-adjoint operators
- finite quadratic geometry

---

## Black-Box Audit — no issues found