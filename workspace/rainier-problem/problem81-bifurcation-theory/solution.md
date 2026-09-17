## Steps

Step 1: Use weighted Lyapunov-Schmidt order at the cubic-degenerate parameter

Fix
$$
\eta=\eta_*:=\frac3{\sqrt{22}},
$$
let
$$
\delta=\lambda-1,
\qquad
L=-\Delta-1,
$$
and write
$$
u=v+w,
\qquad
v=A\cos x+B\cos y,
\qquad
w\perp\operatorname{span}\{\cos x,\cos y\}.
$$
Assign weighted degrees
$$
\operatorname{wt}(A)=\operatorname{wt}(B)=1,
\qquad
\operatorname{wt}(\delta)=2.
$$
Write
$$
w=w_2+w_3+w_4+O_{\mathrm w}(5),
$$
where $w_j$ is homogeneous of weighted degree $j$.

The range equation for
$$
F(u,\lambda)=Lu-\delta u-\eta u^2+u^3=0
$$
gives successively
$$
Lw_2=\eta_* v^2,
\tag{1}
$$
$$
Lw_3=2\eta_*Q(vw_2)-Q(v^3),
\tag{2}
$$
$$
Lw_4=\delta w_2+\eta_*Q(w_2^2+2vw_3)-3Q(v^2w_2),
\tag{3}
$$
where $Q$ denotes projection onto the range of $L$.

Step 2: Compute the quadratic and cubic range corrections

Using
$$
\cos^2x=\frac{1+\cos2x}{2},
\qquad
\cos^2y=\frac{1+\cos2y}{2},
$$
and the $L$-eigenvalues $-1,3,3,1$ on the modes
$$
1,\quad \cos2x,\quad \cos2y,\quad \cos x\cos y,
$$
respectively, (1) gives
$$
w_2=\frac3{\sqrt{22}}\left(
-\frac{A^2+B^2}{2}
+\frac{A^2}{6}\cos2x
+\frac{B^2}{6}\cos2y
+2AB\cos x\cos y
\right).
\tag{4}
$$

Substituting (4) into (2) and using product-to-sum identities gives the compact cubic correction
$$
w_3
=-\frac1{44}\left(A^3\cos3x+B^3\cos3y\right)
-\frac3{22}\left(
A^2B\cos2x\cos y
+AB^2\cos x\cos2y
\right).
\tag{5}
$$

Step 3: Recover the radial cubic normal form

Let $P$ denote projection onto the kernel. The weighted-degree-$3$ kernel equation is
$$
P\left(-\delta v-2\eta_*vw_2+v^3\right)=0.
$$
A direct projection onto $\cos x$ gives
$$
A\left[-\delta+\frac{12}{11}(A^2+B^2)\right],
$$
and the $\cos y$ equation is obtained by symmetry. Thus the cubic truncation is exactly radial at $\eta=\eta_*$.

Step 4: Compute all weighted-degree-$5$ kernel terms

At weighted degree $5$, the kernel contribution is
$$
P\left(
-2\eta_*vw_4
-2\eta_*w_2w_3
+3v^2w_3
+3vw_2^2
\right).
\tag{6}
$$
Equation (3) determines $w_4$. Rather than list every fourth-order Fourier mode, it is enough to retain the modes that can feed back to $\cos x$ after multiplication by $v$. Product-to-sum gives the four $\cos x$ projections in (6):
$$
P_x(-2\eta_*vw_4)
=\frac{A}{1936}\left(
1053A^4+1434A^2B^2+3393B^4
-836\delta A^2-2376\delta B^2
\right),
\tag{7}
$$
$$
P_x(-2\eta_*w_2w_3)
=\frac{3A}{1936}\left(A^4+36A^2B^2+6B^4\right),
\tag{8}
$$
$$
P_x(3v^2w_3)
=-\frac{3A}{176}\left(A^4+12A^2B^2+6B^4\right),
\tag{9}
$$
$$
P_x(3vw_2^2)
=\frac{3A}{176}\left(13A^4+78A^2B^2-41B^4\right).
\tag{10}
$$
The $\cos y$ projections are obtained by swapping $A$ and $B$.

Summing (7)--(10) yields
$$
0=A\Biggl[
-\delta+\frac{12}{11}(A^2+B^2)
-\frac{\delta}{44}(19A^2+54B^2)
+\frac34A^4
+\frac{465}{242}A^2B^2
+\frac{465}{484}B^4
\Biggr]
+O_{\mathrm w}(7),
\tag{11}
$$
$$
0=B\Biggl[
-\delta+\frac{12}{11}(A^2+B^2)
-\frac{\delta}{44}(54A^2+19B^2)
+\frac{465}{484}A^4
+\frac{465}{242}A^2B^2
+\frac34B^4
\Biggr]
+O_{\mathrm w}(7).
\tag{12}
$$
Hence
$$
\boxed{
(p,q,r,s,t)
=
\left(
\frac{19}{44},
\frac{27}{22},
\frac34,
\frac{465}{242},
\frac{465}{484}
\right).
}
\tag{13}
$$

Step 5: Integrate to the normalized reduced energy

Normalize the reduced potential so that its gradient is the displayed amplitude system. Integrating (11)--(12) gives
$$
V(A,B)
=-\frac\delta2(A^2+B^2)
+\frac3{11}(A^2+B^2)^2
$$
$$
\qquad
-\delta\left[
\frac{19}{176}(A^4+B^4)
+\frac{27}{44}A^2B^2
\right]
+\frac18(A^6+B^6)
+\frac{465}{968}(A^4B^2+A^2B^4)
+O_{\mathrm w}(8).
\tag{14}
$$

Put
$$
A=\rho\cos\theta,
\qquad
B=\rho\sin\theta,
\qquad
h=\cos^2\theta\sin^2\theta.
$$
Then
$$
A^4+B^4=\rho^4(1-2h),
$$
$$
A^6+B^6=\rho^6(1-3h),
$$
and
$$
A^4B^2+A^2B^4=\rho^6h.
$$
Therefore
$$
V
=-\frac\delta2\rho^2
+\frac3{11}\rho^4
-\delta\rho^4\left(\frac{19}{176}+\frac{35}{88}h\right)
+\rho^6\left(\frac18+\frac{51}{484}h\right)
+O_{\mathrm w}(8).
\tag{15}
$$

Step 6: Minimize radially and resolve the cubic degeneracy

For fixed $\theta$ and sufficiently small $\delta>0$, the radial critical point satisfies
$$
\rho^2=\frac{11}{12}\delta+O(\delta^2).
\tag{16}
$$
Because the leading radial part is already stationary at (16), substituting only the leading term of $\rho^2$ into the weighted-degree-$6$ corrections determines the energy through order $\delta^3$. One obtains
$$
V_{\min}(\theta)
=-\frac{11}{48}\delta^2
+\delta^3\left(
\frac{77}{13824}
-\frac{583}{2304}\cos^2\theta\sin^2\theta
\right)
+O(\delta^4).
\tag{17}
$$
Thus
$$
\boxed{
C_0=\frac{77}{13824},
\qquad
C_1=-\frac{583}{2304}.
}
\tag{18}
$$

Since
$$
0\le \cos^2\theta\sin^2\theta\le\frac14,
$$
and $C_1<0$, the energy is minimized when
$$
\cos^2\theta\sin^2\theta=\frac14,
$$
i.e. along the diagonal directions
$$
A=\pm B.
$$
The axial directions have $h=0$ and are higher in energy at order $\delta^3$.

So, exactly at the cubic exchange parameter $\eta=3/\sqrt{22}$, the weighted fifth-order reduction resolves the degeneracy in favor of the diagonal branches for sufficiently small $\delta>0$.

Final Answer:
$$
\boxed{
\left(
\frac{19}{44},
\frac{27}{22},
\frac34,
\frac{465}{242},
\frac{465}{484},
\frac{77}{13824},
-\frac{583}{2304}
\right)
}.
$$

---

## Answer

$\left(\frac{19}{44},\frac{27}{22},\frac34,\frac{465}{242},\frac{465}{484},\frac{77}{13824},-\frac{583}{2304}\right)$

---

## Classification

**Problem Type:** Symbolic derivation

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- weighted Lyapunov-Schmidt reduction
- fifth-order mode slaving
- multiple Neumann eigenvalue bifurcation
- $D_4$-equivariant normal forms
- higher-order energy branch selection
