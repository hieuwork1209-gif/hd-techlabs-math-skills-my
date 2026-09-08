## Steps

Step 1: Pass from subgroups to a symplectic quotient

For
$$
x=(u,v,t),\qquad y=(u',v',t'),
$$
the commutator is
$$
[x,y]=(0,0,u\cdot v'-u'\cdot v).
$$
Hence
$$
Z(G)=\{(0,0,t):t\in\mathbb F_p\},
$$
and
$$
G/Z(G)\cong U\oplus U,\qquad U=\mathbb F_p^2,
$$
with alternating form
$$
\omega((u,v),(u',v'))=u\cdot v'-u'\cdot v.
$$
Subgroups containing $Z(G)$ correspond to subspaces of $G/Z(G)$ by taking images and full inverse images. Thus if $A\ge Z(G)$ has order $p^3$, then $L=A/Z(G)$ is a two-dimensional subspace of $U\oplus U$, and $A$ is abelian exactly when $\omega$ vanishes on $L$. Since the ambient symplectic space has dimension four, such a two-dimensional isotropic subspace is Lagrangian.

The images in $G/Z(G)$ of the three subgroups appearing in the intersection conditions are
$$
U\oplus0,\qquad 0\oplus U,\qquad \Delta=\{(u,u):u\in U\}.
$$
Therefore the required subgroups $A$ are in bijection with Lagrangian planes $L$ satisfying
$$
L\cap(U\oplus0)=L\cap(0\oplus U)=0,
$$
and
$$
\dim(L\cap\Delta)=1.
$$

Step 2: Encode every admissible plane by a symmetric matrix

Because $L\cap(0\oplus U)=0$, projection onto the first copy of $U$ is an isomorphism on $L$. Therefore there is a unique linear map $T:U\to U$ such that
$$
L=\{(u,Tu):u\in U\}.
$$
The condition $L\cap(U\oplus0)=0$ says exactly that $T$ is invertible.

For $u,u'\in U$,
$$
\omega((u,Tu),(u',Tu'))=u\cdot Tu'-u'\cdot Tu.
$$
Hence $L$ is isotropic exactly when $T$ is symmetric. Finally,
$$
L\cap\Delta=\{(u,u):(T-I)u=0\},
$$
so the last intersection condition is
$$
\dim\ker(T-I)=1.
$$
Consequently we must count invertible symmetric $2\times2$ matrices $T$ for which $T-I$ has rank one.

Step 3: Shift by the identity and count all rank-one symmetric matrices

Put
$$
S=T-I.
$$
Then $S$ is symmetric, nonzero, and singular, hence has rank one. Conversely every nonzero singular symmetric $S$ gives $\dim\ker S=1$. We only need to impose that $T=I+S$ is invertible.

Write
$$
S=\begin{pmatrix}a&b\\ b&d\end{pmatrix}.
$$
The singularity condition is
$$
ad-b^2=0.
$$
If $a\ne0$, then $d=b^2/a$, giving
$$
(p-1)p
$$
matrices. If $a=0$, then $b=0$, and nonzero rank one requires $d\ne0$, giving $p-1$ more. Thus the total number of nonzero rank-one symmetric matrices is
$$
p(p-1)+(p-1)=p^2-1.
$$

Step 4: Count the rank-one matrices for which $I+S$ is singular

Because $\det S=0$,
$$
\det(I+S)=1+\operatorname{tr}S.
$$
Therefore $I+S$ is singular exactly when
$$
a+d=-1.
$$
Together with $ad=b^2$, this gives
$$
a(-1-a)=b^2.
$$
Set
$$
x=2a+1,\qquad y=2b.
$$
Since $p$ is odd, this change of variables is bijective, and the equation becomes
$$
x^2+y^2=1.
$$
Let $\chi$ be the quadratic character on $\mathbb F_p$, with $\chi(0)=0$. The number $N$ of solutions is
$$
N=\sum_{x\in\mathbb F_p}\bigl(1+\chi(1-x^2)\bigr)
=p+\chi(-1)\sum_{x\in\mathbb F_p}\chi(x^2-1).
$$
To evaluate the remaining sum, count pairs satisfying
$$
y^2=x^2-1.
$$
Equivalently,
$$
(x-y)(x+y)=1.
$$
Choosing $r=x-y\in\mathbb F_p^{\times}$ determines $x+y=r^{-1}$, hence uniquely determines $x$ and $y$. So there are exactly $p-1$ such pairs. On the other hand there are
$$
p+\sum_x\chi(x^2-1)
$$
pairs, hence
$$
\sum_x\chi(x^2-1)=-1.
$$
Therefore
$$
N=p-\chi(-1).
$$
These are exactly the rank-one symmetric $S$ for which $I+S$ is singular.

Step 5: Subtract the forbidden matrices

The desired number is
$$
(p^2-1)-\bigl(p-\chi(-1)\bigr)
=p^2-p-1+\chi(-1).
$$
Euler's criterion gives
$$
\chi(-1)=(-1)^{\frac{p-1}{2}}.
$$

Final Answer: $\boxed{p^2-p-1+(-1)^{\frac{p-1}{2}}}$

---

## Answer

$p^2-p-1+(-1)^{\frac{p-1}{2}}$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- extraspecial finite group
- symplectic quotient
- Lagrangian plane
- symmetric graph map
- quadratic character

---

## Black-Box Audit

No Level 2 or Level 3 black-box issues found.
