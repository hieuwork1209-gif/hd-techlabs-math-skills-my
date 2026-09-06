## Steps

Step 1: Encode the flag metric by the type-$A_3$ Hecke algebra

Write a flag as $F=(P<L<H)$, with $P,L,H$ of dimensions $1,2,3$. The number of flags is
$$
15\cdot 7\cdot 3=315.
$$
Fix a base flag. Bruhat decomposition assigns to every second flag a unique relative position $w\in S_4$, and a gallery changes the relative position by one simple reflection. So the graph distance is the Coxeter length $\ell(w)$. For the three simple reflections let $T_i$ be the operator summing over the two adjacent flags of type $i$. A panel contains three flags, so
$$
T_i^2=T_i+2I.
$$
The remaining relations are
$$
T_1T_3=T_3T_1,
$$
$$
T_1T_2T_1=T_2T_1T_2,
\qquad
T_2T_3T_2=T_3T_2T_3.
$$
These relations generate $H_2(S_4)$. If $T_w$ denotes the product along a reduced word for $w$, then the distance kernel is
$$
D_p=\sum_{w\ne e}\ell(w)^pT_w.
$$

Step 2: Construct the critical eigenspace from point-plane incidence

Let $\mathcal P$ and $\mathcal H$ be the $15$ points and $15$ planes of $\operatorname{PG}(3,2)$. For a mean-zero function $u:\mathcal P\to\mathbb{R}$, set
$$
c_u(P,L,H)=u(P)-\frac{1}{2}\sum_{Q\subset H}u(Q).
$$
Let $N$ be the point-plane incidence matrix. Every point lies in $7$ planes and two distinct points lie together in exactly $3$ planes, so
$$
NN^T=4I+3J.
$$
It follows that $\|N^Tu\|^2=4\|u\|^2$ whenever $\sum_Qu(Q)=0$. For each incident pair $P\subset H$ there are exactly three lines $L$ with $P<L<H$, so
$$
\begin{aligned}
\|c_u\|^2
&=3\sum_{P\subset H}\left(u(P)-\frac{1}{2}(N^Tu)(H)\right)^2\\
&=3\left(7\|u\|^2-\|N^Tu\|^2+\frac{7}{4}\|N^Tu\|^2\right)\\
&=30\|u\|^2.
\end{aligned}
$$
It follows that
$$
W=\left\{c_u:\sum_Qu(Q)=0\right\}
$$
has dimension $14$, and every vector in $W$ has coordinate sum $0$.

It remains to determine the scalar by which $D_p$ acts on $W$. Fix $F=(P,L,H)$ and compare the coefficient of $u(Q)$ in $(D_pc_u)(F)$ with the coefficient for a point $Q$ outside $H$. For a relative position $w$, the corresponding Bruhat cell contains $2^{\ell(w)}$ flags. Sorting the $24$ positions by length and by the two conditions $P'=Q$ and $Q\subset H'$ gives the shell-coefficient difference
$$
(3,2,-6,-16,0,16)
$$
when $Q=P$, its negative when $Q\subset H$ and $Q\ne P$, and $0$ when $Q\not\subset H$. This gives
$$
D_pc_u=L(p)c_u,
$$
where
$$
L(p)=3+2\cdot 2^p-6\cdot 3^p-16\cdot 4^p+16\cdot 6^p.
$$

Step 3: Certify that every other Hecke mode is strictly negative near the boundary

Only the spectrum on the orthogonal complement of constants and $W$ remains. For a simple reflection $s_i$, the Hecke multiplication rule is
$$
T_wT_i=
\begin{cases}
T_{ws_i},&\ell(ws_i)=\ell(w)+1,\\
2T_{ws_i}+T_w,&\ell(ws_i)=\ell(w)-1.
\end{cases}
$$
Use this rule on three parabolic induced modules. Inducing the trivial character from $H_2(S_3)$ gives the trivial module plus $S^{(31)}$; inducing the sign character from the same parabolic gives the sign module plus $S^{(211)}$; and inducing the trivial character from $H_2(S_2\times S_2)$ gives the trivial module, $S^{(31)}$, and $S^{(22)}$. Their minimal-coset bases have sizes $4$, $4$, and $6$. The calculation uses only these fourteen basis vectors and the displayed two-term rule.

Put $x_r=r^p$. Factoring the characteristic polynomials after removing the constant factor and the eigenline $W$ from Step 2 gives the following basis-independent certificate on $\frac{1}{4}\leq p\leq\frac{1}{3}$. The residual quadratic factor from $S^{(31)}$ has trace less than $-12$ and determinant greater than $11$. In $S^{(211)}$, one linear factor is less than $-\frac{1}{2}$, while the residual quadratic factor has trace less than $-2$ and determinant greater than $1$. The $S^{(22)}$ factor has trace less than $-1$ and determinant greater than $\frac{1}{2}$, and the sign-module scalar is less than $-\frac{1}{2}$. These inequalities are obtained from the same multiplication rule because every characteristic coefficient is an exponential polynomial in $x_2,\ldots,x_6$ with a fixed derivative sign on this interval, so its extremum is at an endpoint.

The Hecke action is self-adjoint, so the quadratic factors have real roots. Negative trace and positive determinant place both roots below $0$. It follows that every nonconstant eigenvalue outside $W$ is strictly negative throughout the interval, so
$$
D_p\big|_{\mathbf{1}^{\perp}\cap W^{\perp}}<0
\qquad
\left(\frac{1}{4}\leq p\leq\frac{1}{3}\right).
$$

Step 4: Locate the unique boundary exponent

The critical scalar satisfies
$$
L(0)=-1
$$
and
$$
L'(0)=2\log\frac{243}{128}>0.
$$
Also,
$$
L''(p)
=2(\log 2)^2 2^p-6(\log 3)^2 3^p-16(\log 4)^2 4^p+16(\log 6)^2 6^p.
$$
For $p\geq0$, use $6^p\geq4^p\geq3^p$ to obtain
$$
L''(p)
\geq 2(\log 2)^2 2^p
+\left(16\big((\log 6)^2-(\log 4)^2\big)-6(\log 3)^2\right)4^p>0.
$$
So $L$ is strictly increasing. For the left endpoint, the elementary bounds
$$
2^{1/4}<1.19,\quad 3^{1/4}>1.316,\quad 4^{1/4}>1.4142,\quad 6^{1/4}<1.5651
$$
follow by raising the four decimal bounds to the fourth power. They give
$$
L\left(\frac{1}{4}\right)<3+2(1.19)-6(1.316)-16(1.4142)+16(1.5651)<-\frac{1}{10}.
$$
For the right endpoint, cubing
$$
2^{1/3}>1.259,\quad 3^{1/3}<1.443,\quad 4^{1/3}<1.588,\quad 6^{1/3}>1.817
$$
gives
$$
L\left(\frac{1}{3}\right)>3+2(1.259)-6(1.443)-16(1.588)+16(1.817)>\frac{1}{2}.
$$
Therefore there is a unique $\alpha\in(\frac{1}{4},\frac{1}{3})$ with $L(\alpha)=0$.

Step 3 shows that $D_\alpha$ is strictly negative on $\mathbf{1}^{\perp}\cap W^{\perp}$, while Step 2 shows that it vanishes on $W$. Therefore $d^\alpha$ is conditionally negative definite. For $0<p<\alpha$, write $d^p=(d^\alpha)^{p/\alpha}$; the integral representation of $t^s$ for $0<s<1$ preserves conditional negative definiteness. For $p>\alpha$, Step 2 gives $L(p)>0$ on $W$, so negative type fails. Therefore
$$
\wp=\alpha.
$$

Step 5: Determine the equality-space dimension

At $p=\wp$, Step 2 gives $W\subseteq E$, while Step 3 gives strict negativity on the orthogonal complement of constants and $W$, so
$$
E=W
$$
and
$$
\dim E=14.
$$

Final Answer: $\boxed{(\min\{p>0:3+2\cdot2^p-6\cdot3^p-16\cdot4^p+16\cdot6^p=0\},14)}$

---

## Answer

$(\min\{p>0:3+2\cdot2^p-6\cdot3^p-16\cdot4^p+16\cdot6^p=0\},14)$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- negative type of finite metric spaces
- complete flag graph metrics
- point-plane incidence operators
- Iwahori-Hecke algebra
