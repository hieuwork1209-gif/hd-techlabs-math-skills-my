## Steps

Step 1: Analyze the zeros of one cyclic block
For an integer $k\ge2$, define
$$
B_{k,t}(w_1,\dots,w_k)
=\bigl(w_1^2+t\overline{w_2},\dots,w_{k-1}^2+t\overline{w_k},w_k^2+t\overline{w_1}\bigr).
$$
Suppose $B_{k,t}(w)=0$. If one coordinate vanishes, the equations force all coordinates to vanish. Thus every nonzero zero has all coordinates nonzero.

Write
$$
\rho_i=|w_i|.
$$
Then
$$
\rho_i^2=t\rho_{i+1}
$$
cyclically. Setting
$$
a_i=\log\frac{\rho_i}{t}
$$
gives $a_{i+1}=2a_i$, hence $a_1=2^ka_1$ and therefore
$$
\rho_1=\cdots=\rho_k=t.
$$

Write $w_i=te^{i\theta_i}$. The phase equations are
$$
\theta_{i+1}\equiv\pi-2\theta_i\pmod{2\pi}.
$$
If $f(\theta)=\pi-2\theta$, then
$$
f^k(\theta)-\theta
=\bigl((-2)^k-1\bigr)\left(\theta-\frac\pi3\right)
\pmod{2\pi}.
$$
Hence the number of nonzero zeros is
$$
N_k=\left|(-2)^k-1\right|=2^k-(-1)^k.
$$
Every such zero has Euclidean norm
$$
\sqrt{k}\,t.
$$

Step 2: Compute the local degree of every zero of a block
At the origin,
$$
DB_{k,t}(0)(\xi_1,\dots,\xi_k)
=t\bigl(\overline{\xi_2},\dots,\overline{\xi_k},\overline{\xi_1}\bigr).
$$
The cyclic permutation of the complex coordinate blocks has positive real determinant, while conjugation on each complex coordinate has determinant $-1$. Thus the local degree at the origin is
$$
(-1)^k.
$$

Now let $w$ be a nonzero zero and write a tangent increment as
$$
\delta w_i=w_i\eta_i.
$$
Using
$$
w_i^2=-t\overline{w_{i+1}},
$$
the derivative becomes
$$
DB_{k,t}(w)(\delta w)_i
=t\overline{w_{i+1}}\bigl(-2\eta_i+\overline{\eta_{i+1}}\bigr).
$$
Multiplying complex input or output coordinates by nonzero complex scalars preserves real orientation, so the sign of the Jacobian equals that of
$$
L(\eta)_i=-2\eta_i+\overline{\eta_{i+1}}.
$$
Let $S$ be the cyclic shift on $\mathbb R^k$. Writing $\eta=x+iy$, the real and imaginary parts of $L$ are
$$
x\longmapsto(-2I_k+S)x,
\qquad
y\longmapsto(-2I_k-S)y.
$$
Since
$$
\det(-2I_k+S)=(-1)^k(2^k-1)
$$
and
$$
\det(-2I_k-S)=(-2)^k-1,
$$
these two determinants have the same sign, so
$$
\det_{\mathbb R}L>0.
$$
Therefore every nonzero zero of $B_{k,t}$ is nondegenerate and has local degree $+1$.

Step 3: Classify the zeros of the two-block map relative to the unit ball
Let
$$
m=r+s
$$
and let $P_t$ be the map from the problem. Because the permutation consists of an $r$-cycle and an $s$-cycle,
$$
P_t=B_{r,t}\oplus B_{s,t}.
$$
Thus every zero is of one of four types:

$$
(0,0),
$$
with local degree $(-1)^{r+s}$;

$$
(u,0),\qquad u\ne0,
$$
with $N_r$ choices, norm $\sqrt r\,t$, and local degree $(-1)^s$;

$$
(0,v),\qquad v\ne0,
$$
with $N_s$ choices, norm $\sqrt s\,t$, and local degree $(-1)^r$;

and
$$
(u,v),\qquad u\ne0,\ v\ne0,
$$
with $N_rN_s$ choices, norm $\sqrt{r+s}\,t$, and local degree $+1$.

The hypothesis
$$
(r+s)^{-1/2}<t<s^{-1/2}
$$
and the inequality $r<s$ imply
$$
\sqrt r\,t<1,
\qquad
\sqrt s\,t<1,
\qquad
\sqrt{r+s}\,t>1.
$$
Hence the first three types lie inside the open unit ball and the fourth lies outside it. In particular, $P_t$ has no zero on the unit sphere, so the normalized map $F_t$ is well-defined.

Step 4: Sum the local degrees inside the ball
For a smooth map with no zero on the unit sphere and only nondegenerate zeros in the ball, the degree of the normalized boundary map is the sum of the local degrees of the interior zeros. Therefore
$$
\deg F_t
=(-1)^{r+s}+N_r(-1)^s+N_s(-1)^r.
$$
Using
$$
N_r=2^r-(-1)^r,
\qquad
N_s=2^s-(-1)^s,
$$
we obtain
$$
\deg F_t
=(-1)^{r+s}
+\bigl(2^r-(-1)^r\bigr)(-1)^s
+\bigl(2^s-(-1)^s\bigr)(-1)^r,
$$
which simplifies to
$$
\deg F_t
=2^r(-1)^s+2^s(-1)^r-(-1)^{r+s}.
$$

Final Answer: $\boxed{2^r(-1)^s+2^s(-1)^r-(-1)^{r+s}}$

---

## Answer

$2^r(-1)^s+2^s(-1)^r-(-1)^{r+s}$

---

## Classification

**Problem Type:** Symbolic derivation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- brouwer degree
- local degree
- cyclic zero classification
- nondegenerate jacobian signs
- direct-sum zero bookkeeping
