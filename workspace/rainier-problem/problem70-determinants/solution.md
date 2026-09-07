## Steps

Step 1: Recover the two hidden scale variables
Put
$$
L=\log n,\qquad c=aL,\qquad d=c-b,
$$
and
$$
P_n(a,b)=\frac{W_1(n,a,b)}{T_1(n,a,b)}.
$$
For fixed $b$, the identities $T_1'=-T_2$, $T_1''=2T_3$ and their $W$-analogues give
$$
H_n(a,b)=\frac{d}{dc}\log P_n(a,b),\qquad
K_n(a,b)=\frac{d^2}{dc^2}\log P_n(a,b).
$$
Thus the first equation is a stationary determinant-ratio condition, while the second measures its normalized curvature.

Let
$$
A_N(a)=S_1(N,a)=B(a,N+1),\qquad N=n^3,
$$
$$
r_j(a)=\frac{A_{N+m_j}(a)}{A_N(a)},\qquad
h_n(a)=1-\sum_{j=1}^3b_jr_j(a).
$$
Since
$$
W_1=e^{2b}A_Nh_n,
$$
the beta approximation $B(a,n^q+1)=\Gamma(a)n^{-qa}(1+o(1))$ gives, uniformly near $(c,b)=(1,1)$,
$$
P_n(a,b)=\frac{e^{-3d}h_n(a)}{Z(d)}(1+o(1)),
\qquad
Z(d)=e^{-d}+e^{-2d}+e^{-3d}.
$$

Step 2: Identify the singular limiting system
Define
$$
Q(d)=\frac{e^{-d}+2e^{-2d}+3e^{-3d}}{Z(d)},
$$
and let $V(d)$ be the variance of $\{1,2,3\}$ with weights proportional to $e^{-qd}$. Since $h_n(c/L)=c\,C_n(1+o(1))$ for a factor $C_n$ independent of $c$,
$$
H_n(c/L,b)\longrightarrow H_0(c,b)=\frac1c+Q(d)-3,
$$
$$
K_n(c/L,b)\longrightarrow K_0(c,b)=-\frac1{c^2}-V(d).
$$
The elementary three-point expansions are
$$
Q(d)=2-\frac23d+\frac19d^3+O(d^5),
$$
$$
V(d)=\frac23-\frac13d^2+O(d^4).
$$
Write
$$
u=c-1,\qquad v=b-1,
$$
so $d=u-v$. Then
$$
H_0=-u-\frac23d+u^2-u^3+\frac19d^3+O((|u|+|d|)^4),
$$
$$
K_0+\frac53=2u-3u^2+4u^3+\frac13d^2+O((|u|+|d|)^4).
$$
The first limiting equation has nonzero derivative with respect to $u$ at the origin, so it determines a local stationary curve $u=u(d)$.

Step 3: Eliminate the stationary curve and expose the cubic branch
Solving $H_0=0$ recursively gives
$$
u=-\frac23d+\frac49d^2-\frac5{27}d^3+O(d^4),
$$
therefore
$$
v=u-d=-\frac53d+\frac49d^2-\frac5{27}d^3+O(d^4).
$$
Along this curve,
$$
K_0+\frac53=-\frac43d-\frac19d^2+\frac29d^3+O(d^4).
$$
Hence
$$
K_0+\frac53-\frac45v
=-\frac7{15}d^2+\frac{10}{27}d^3+O(d^4).
$$
Also
$$
v^2=\frac{25}{9}d^2-\frac{40}{27}d^3+O(d^4).
$$
Consequently the tuned second invariant satisfies
$$
K_0+\frac53-\frac45v+\frac{21}{125}v^2
=\frac{82}{675}d^3+O(d^4).
$$
Thus the Jacobian of the two-equation limiting system is singular in the relative-scale direction, and both the linear and quadratic terms disappear only after the first determinant equation has been eliminated.

Step 4: Compute the finite-size forcing without destroying the singularity
Let
$$
\pi_1(d)=\frac{e^{-d}}{Z(d)},\qquad s=\frac1{nL}.
$$
Only the $q=1$ beta factor contributes at order $s$:
$$
B(c/L,n+1)=\Gamma(c/L)e^{-c}
\left(1-\frac{c}{2nL}-\frac{c^2}{2nL^2}+O(n^{-2}L^{-1})\right).
$$
Therefore the base-column part of $\log P_n$ contributes
$$
\frac{s}{2}c\pi_1(d)+\frac{s}{2L}c^2\pi_1(d)
$$
up to smaller terms.

For the signed stencil, with
$$
\mu_k=\sum_{j=1}^3b_js_j^k,\qquad
s_j=\sum_{k=1}^{m_j}\frac1{N+k},
$$
the same direct moment expansion gives
$$
\frac{\mu_2}{\mu_1}=\frac{2}{3n}+O(n^{-3/2}),\qquad
\frac{\mu_3}{\mu_1}=-\frac{3}{2n}+O(n^{-3/2}),
$$
so
$$
\log h_n(c/L)=\text{const}+\log c-\frac{sc}{3}-\frac{sc^2}{4L}
+O(n^{-3/2}L^{-1}).
$$
At $(c,b)=(1,1)$,
$$
\pi_1(0)=\frac13,\qquad \pi_1'(0)=\frac13,\qquad \pi_1''(0)=\frac19.
$$
The order-$s$ and order-$s/L$ corrections to the first derivative cancel between the base column and the stencil, while the second derivative retains
$$
K_n(1/L,1)=-\frac53+\frac7{18}s+O\left(\frac{s}{L}+n^{-3/2}L^{-1}\right).
$$
More generally, for $|u|+|d|=o(1)$,
$$
H_n-H_0=O\bigl(s(|u|+|d|)+s/L+n^{-3/2}L^{-1}\bigr),
$$
with the constant term through order $s/L$ cancelling at the origin, and
$$
K_n-K_0=\frac7{18}s+O\bigl(s(|u|+|d|)+s/L+n^{-3/2}L^{-1}\bigr).
$$

Step 5: Extract the coupled cubic displacement
The first equation $H_n=0$ therefore perturbs the stationary curve by $o(s^{1/3})$. On that curve the second equation becomes
$$
0=\frac{82}{675}d_n^3+\frac7{18}s+o(s),
\qquad d_n=a_nL-b_n.
$$
Hence
$$
(nL)d_n^3\longrightarrow
-\frac7{18}\frac{675}{82}=-\frac{525}{164}.
$$
The selected branch has $d_n<0$, and the reduced derivative is
$$
\frac{246}{675}d^2+o(d^2)>0
$$
away from the limiting cusp, giving the claimed local uniqueness for large $n$. Therefore
$$
(n\log n)^{1/3}(b_n-a_n\log n)
\longrightarrow \sqrt[3]{\frac{525}{164}}.
$$

Final Answer: $\boxed{\sqrt[3]{\frac{525}{164}}}$

---

## Answer

$\sqrt[3]{\frac{525}{164}}$

---

## Classification

**Problem Type:** Parameter identification

**Answer Type:** Exact scalar

---

## Solution Concepts

- determinant-ratio stationary curve
- tilted three-scale beta mixture
- singular coupled implicit system
- signed-stencil finite-size cancellation
- cubic relative-scale splitting

---

## Black-Box Audit — no issues found

The hardening keeps the signed three-cutoff stencil but no longer exposes a single preassembled cusp equation. The first determinant condition determines a hidden stationary curve in the two scale variables; only after eliminating that curve do the linear and quadratic terms in the curvature constraint cancel, leaving a cubic relative-scale branch forced by the finite beta correction.