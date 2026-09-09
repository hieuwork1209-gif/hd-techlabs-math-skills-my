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

Step 2: Construct the critical eigenspace and compute its shell eigenvalue

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
Thus
$$
W=\left\{c_u:\sum_Qu(Q)=0\right\}
$$
has dimension $14$, and every vector in $W$ has coordinate sum $0$.

It remains to compute the scalar by which each distance shell acts on $W$. Fix the base flag $F=(P,L,H)$ and a point $Q_0\not\subset H$. For the Bruhat cell $C_w$ of relative position $w$, define
$$
b_w(Q)
=\#\{F'=(P',L',H')\in C_w:P'=Q\}
-\frac12\#\{F'\in C_w:Q\subset H'\}.
$$
This is exactly the coefficient of $u(Q)$ in $(T_wc_u)(F)$. Put
$$
k(w)=2\bigl(b_w(P)-b_w(Q_0)\bigr).
$$
Each cell has $|C_w|=2^{\ell(w)}$. Writing permutations in one-line notation, the complete $24$-position calculation is
$$
\begin{array}{c|l|r}
 r& w:k(w)&k_r:=\sum_{\ell(w)=r}k(w)\\
\hline
0&1234:1&1\\
1&1243:3,\ 1324:2,\ 2134:-2&3\\
2&1342:6,\ 1423:6,\ 2143:-2,\ 2314:-4,\ 3124:-4&2\\
3&1432:12,\ 2341:-6,\ 2413:-4,\ 3142:-4,\ 3214:-8,\ 4123:4&-6\\
4&2431:-12,\ 3241:-12,\ 3412:-8,\ 4132:8,\ 4213:8&-16\\
5&3421:-24,\ 4231:8,\ 4312:16&0\\
6&4321:16&16
\end{array}
$$
The $r=0$ row is the identity and does not occur in $D_p$. If
$$
B_r(Q)=\sum_{\ell(w)=r}b_w(Q),
$$
then the same shell count gives, for every $R\subset H$ with $R\ne P$,
$$
2\bigl(B_r(R)-B_r(Q_0)\bigr)=-k_r,
$$
while all points outside $H$ have the same coefficient $B_r(Q_0)$. Since $\sum_Qu(Q)=0$, that common outside coefficient contributes nothing. Also
$$
c_u(F)=\frac12\left(u(P)-\sum_{\substack{R\subset H\\R\ne P}}u(R)\right).
$$
Consequently the distance-$r$ shell $A_r=\sum_{\ell(w)=r}T_w$ satisfies
$$
A_rc_u=k_rc_u.
$$
Therefore
$$
D_pc_u=L(p)c_u,
$$
where
$$
L(p)=3+2\cdot2^p-6\cdot3^p-16\cdot4^p+16\cdot6^p.
$$

Step 3: Display and bound every remaining Hecke mode

Write $x_r=r^p$ for $2\le r\le6$. Since $q=2$, the Hecke algebra $H_2(S_4)$ is semisimple and its irreducible modules are the five Specht modules indexed by the partitions of $4$:
$$
S^{(4)},\quad S^{(31)},\quad S^{(22)},\quad S^{(211)},\quad S^{(1111)},
$$
of dimensions $1,3,2,3,1$, respectively. The three small induced modules used below decompose as
$$
\operatorname{Ind}_{H_2(S_3)}^{H_2(S_4)}\mathbf 1
\cong S^{(4)}\oplus S^{(31)},
$$
$$
\operatorname{Ind}_{H_2(S_3)}^{H_2(S_4)}\operatorname{sgn}
\cong S^{(1111)}\oplus S^{(211)},
$$
$$
\operatorname{Ind}_{H_2(S_2\times S_2)}^{H_2(S_4)}\mathbf 1
\cong S^{(4)}\oplus S^{(31)}\oplus S^{(22)}.
$$
Thus these induced modules contain every irreducible Hecke type. The $S^{(4)}$ type is the constant mode. Step 2 identifies the critical eigenline inside the $S^{(31)}$ type; it has eigenvalue $L(p)$. Hence it only remains to check the residual two-dimensional part of $S^{(31)}$, all of $S^{(211)}$, all of $S^{(22)}$, and the sign mode.

Using
$$
T_wT_i=
\begin{cases}
T_{ws_i},&\ell(ws_i)=\ell(w)+1,\\
2T_{ws_i}+T_w,&\ell(ws_i)=\ell(w)-1,
\end{cases}
$$
on the minimal-coset bases gives the following explicit factors.

For $S^{(31)}$, after removing the eigenvalue $L(p)$, the other two eigenvalues are the roots of the characteristic polynomial of
$$
Q_{31}(p)=
\begin{pmatrix}
8x_2+10x_3+8x_4-16x_5-16x_6+5&4x_2+4x_3-8x_4\\
11x_2+14x_3-4x_4-24x_5+3&-2x_2-4x_3+4x_4+16x_5-16x_6+1
\end{pmatrix}.
$$
Its trace is
$$
\tau_{31}=6+6x_2+6x_3+12x_4-32x_6,
$$
and put $\Delta_{31}=\det Q_{31}$.

For $S^{(211)}$, one eigenvalue is
$$
L_{211}=-4x_2+3x_3+2x_4-6x_5+4x_6,
$$
and the other two are the roots of the characteristic polynomial of
$$
Q_{211}(p)=
\begin{pmatrix}
7x_3-12x_4+10x_5-4x_6-2&2x_2+2x_3-4x_4\\
-2x_3+3x_4-2x_5+1&-3x_2-4x_3+6x_4+2x_5-4x_6+2
\end{pmatrix}.
$$
Here
$$
\tau_{211}=-3x_2+3x_3-6x_4+12x_5-8x_6,
\qquad
\Delta_{211}=\det Q_{211}.
$$

For $S^{(22)}$ one may use
$$
T_1=T_3=\begin{pmatrix}2&0\\0&-1\end{pmatrix},
\qquad
T_2=\begin{pmatrix}-1/3&14/9\\1&4/3\end{pmatrix},
$$
which satisfy the Hecke quadratic and braid relations. They give
$$
Q_{22}(p)=
\begin{pmatrix}
\frac43x_2-8x_3-\frac{26}3x_4+\frac83x_5+8x_6+\frac{11}3&
\frac{28}9x_2-\frac{14}3x_3-\frac{56}9x_4+\frac{56}9x_5+\frac{14}9\\
2x_2-3x_3-4x_4+4x_5+1&
-\frac{13}3x_2+8x_3+\frac83x_4-\frac{44}3x_5+8x_6-\frac23
\end{pmatrix},
$$
so
$$
\tau_{22}=3-3x_2-6x_4-12x_5+16x_6,
\qquad
\Delta_{22}=\det Q_{22}.
$$
Finally, on $S^{(1111)}$ the scalar is
$$
S(p)=-3+5x_2-6x_3+5x_4-3x_5+x_6.
$$

Now let $I=[1/4,1/3]$. All quantities above are explicit exponential polynomials. Differentiate them directly; for a determinant $\Delta=ad-bc$ use
$$
\Delta'=a'd+ad'-b'c-bc'.
$$
Using $r^p=e^{p\log r}$ in the displayed formulas gives the following conservative derivative enclosures on $I$:
$$
\begin{array}{c|c}
f&f'(I)\\
\hline
\tau_{31}&[-63.1,-52.5]\\
\Delta_{31}&[62,93]\\
L_{211}&[1.7,2.2]\\
\tau_{211}&[-4.1,-3.4]\\
\Delta_{211}&[0.7,1.9]\\
\tau_{22}&[1.7,3.3]\\
\Delta_{22}&[-4.7,-1.6]\\
S&[0.8,0.9]
\end{array}
$$
Thus the relevant extrema occur at endpoints. Direct substitution gives
$$
\begin{array}{c|c|c}
f&\text{controlling endpoint value}&\text{consequence on }I\\
\hline
\tau_{31}&\tau_{31}(1/4)=-12.080457\ldots&\tau_{31}<-12\\
\Delta_{31}&\Delta_{31}(1/4)=11.873409\ldots&\Delta_{31}>11\\
L_{211}&L_{211}(1/3)=-0.529506\ldots&L_{211}<-1/2\\
\tau_{211}&\tau_{211}(1/4)=-2.681171\ldots&\tau_{211}<-2\\
\Delta_{211}&\Delta_{211}(1/4)=1.475441\ldots&\Delta_{211}>1\\
\tau_{22}&\tau_{22}(1/3)=-1.749951\ldots&\tau_{22}<-1\\
\Delta_{22}&\Delta_{22}(1/3)=0.609126\ldots&\Delta_{22}>1/2\\
S&S(1/3)=-0.729694\ldots&S<-1/2
\end{array}
$$
The Hecke action comes from self-adjoint operators on the chamber space, so the roots of each quadratic factor are real. A negative trace and positive determinant therefore force both roots to be negative. Hence every nonconstant eigenvalue outside the $L(p)$-eigenline in the $S^{(31)}$ mode is strictly negative for every $p\in I$. In particular,
$$
D_p\big|_{\mathbf 1^\perp\cap W^\perp}<0
\qquad\left(\frac14\le p\le\frac13\right).
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
Therefore there is a unique $\alpha\in(\frac{1}{4},\frac{1}{3})$ with $L(\alpha)=0$. Numerically,
$$
\alpha\approx0.2655412194.
$$

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
