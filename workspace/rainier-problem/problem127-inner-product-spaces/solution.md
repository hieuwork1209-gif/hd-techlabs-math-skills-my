## Steps

Step 1: Normalize the cyclic phases without changing the determinant magnitude
Let $0<\rho<\cos(\pi/5)$ and let $v_1,\ldots,v_5\in\mathbb C^5$ be unit vectors, with indices modulo $5$. Write
$$
c_i=\langle v_i,v_{i+1}\rangle.
$$
The hypotheses give $|c_i|=\rho$ and
$$
\prod_{i=1}^5c_i=-\rho^5.
$$
Set
$$
\alpha=\frac\pi5,
\qquad
q=\rho e^{i\alpha}.
$$
Then $q^5=-\rho^5$. Multiplying each $v_i$ by a complex scalar of modulus $1$ does not change $|\det[v_1\ \cdots\ v_5]|$. Choose these phases successively so that the first four transformed adjacent inner products equal $q$. The transformed phase on the fifth edge is then forced to be $\alpha$ as well, because the product of the five adjacent inner products is invariant and equals $q^5$. Hence we may assume
$$
\langle v_i,v_{i+1}\rangle=q
$$
for every $i$.

Let $G=(\langle v_i,v_j\rangle)_{i,j=1}^5$ be the Gram matrix. Then
$$
|\det[v_1\ \cdots\ v_5]|^2=\det G,
$$
so the problem is to maximize $\det G$ among Hermitian positive semidefinite matrices with diagonal entries $1$ and cyclic adjacent entries $q$.

Step 2: Exhibit an interior feasible family and record its spectrum
Put
$$
A=\cos\frac\pi5=\frac{1+\sqrt5}{4},
\qquad
B=\cos\frac{2\pi}{5}=\frac{\sqrt5-1}{4}.
$$
For real $t$, consider the Hermitian circulant matrix whose first row is
$$
\left(1,q,te^{2i\alpha},te^{-2i\alpha},\overline q\right).
$$
Using the fifth roots of unity as Fourier eigenvectors, its five eigenvalues are
$$
\lambda_A=1+2\rho A+2tB
$$
with multiplicity $2$,
$$
\lambda_B=1-2\rho B-2tA
$$
with multiplicity $2$, and
$$
\lambda_C=1-2\rho+2t
$$
with multiplicity $1$.

Thus this matrix is positive definite whenever
$$
\rho-\frac12<t<\frac{1-2\rho B}{2A}.
$$
The interval is nonempty exactly when $\rho<A=\cos(\pi/5)$. Therefore the stated range of $\rho$ contains positive definite feasible Gram matrices, so the maximum determinant is positive and every maximizing Gram matrix is positive definite.

Step 3: Use cyclic symmetry and the negative holonomy to force a one-parameter maximizer
On the convex set of positive definite feasible Gram matrices, $\log\det$ is strictly concave. Hence the maximizing Gram matrix is unique: two distinct maximizers would have a midpoint with strictly larger log determinant.

Cyclically permuting the five indices preserves all normalized constraints. By uniqueness, the maximizer is fixed by that permutation, hence is circulant. Its first row therefore has the form
$$
(1,q,z,\overline z,\overline q)
$$
for some complex $z$.

There is a second symmetry forced by the cyclic phase. Complex conjugation changes every adjacent entry from $q$ to $\overline q$. To restore $q$, the adjacent rephasing ratio must be
$$
\frac q{\overline q}=e^{2i\alpha}.
$$
Because $5(2\alpha)=2\pi$, this rephasing is consistent around the whole cycle. Explicitly, with
$$
D=\operatorname{diag}(1,e^{2i\alpha},e^{4i\alpha},e^{6i\alpha},e^{8i\alpha}),
$$
the map
$$
G\longmapsto D^*\overline G D
$$
preserves the normalized feasible set and the determinant. Uniqueness forces the maximizer to be fixed by this map. On the distance-two entry this gives
$$
z=e^{4i\alpha}\overline z.
$$
Therefore
$$
z=te^{2i\alpha}
$$
for some real $t$. Thus the unique maximizer lies in the one-parameter family from Step 2.

Step 4: Optimize the remaining parameter exactly
For the maximizing family,
$$
D(t)=\det G
=\lambda_A^2\lambda_B^2\lambda_C.
$$
Inside the positive definite interval,
$$
\frac{D'(t)}{D(t)}
=\frac{4B}{\lambda_A}-\frac{4A}{\lambda_B}+\frac{2}{\lambda_C}.
$$
Clearing the positive denominators and using
$$
A=\frac{1+\sqrt5}{4},
\qquad
B=\frac{\sqrt5-1}{4}
$$
reduces the critical-point equation to
$$
\rho^2-\rho t-t^2-t=0.
$$
Set
$$
\Delta=\sqrt{5\rho^2+2\rho+1}.
$$
The two roots are
$$
t_{\pm}=\frac{-\rho-1\pm\Delta}{2}.
$$
The root $t_-$ lies below $\rho-1/2$, while
$$
t_*=t_+=\frac{\Delta-\rho-1}{2}>0.
$$
Moreover
$$
\lambda_C(t_*)=\Delta-3\rho>0
$$
because
$$
\Delta^2-9\rho^2=1+2\rho-4\rho^2>0
$$
for $0<\rho<\cos(\pi/5)$. Also $\lambda_A(t_*)>0$, and
$$
\lambda_A(t_*)\lambda_B(t_*)
=1+2\rho-\rho^2-\rho\Delta>0,
$$
since
$$
(1+2\rho-\rho^2)^2-\rho^2\Delta^2
=-(\rho+1)^2(4\rho^2-2\rho-1)>0.
$$
Thus $t_*$ lies in the positive definite interval. The determinant tends to $0$ at both endpoints of that interval, and $t_*$ is its only interior critical point, so $t_*$ is the unique global maximizer.

Step 5: Evaluate the maximum and verify attainment
At $t=t_*$,
$$
\lambda_C=\Delta-3\rho.
$$
Multiplying the other two eigenvalues first gives
$$
\lambda_A\lambda_B
=1+\rho-\rho^2-3\rho t_*-t_*^2-t_*.
$$
The critical-point relation
$$
\rho^2=\rho t_*+t_*^2+t_*
$$
and
$$
\rho+t_*=\frac{\Delta+\rho-1}{2}
$$
then yield
$$
\lambda_A\lambda_B
=1+2\rho-\rho^2-\rho\Delta.
$$
Consequently
$$
\det G_{\max}
=(1+2\rho-\rho^2-\rho\Delta)^2(\Delta-3\rho).
$$
The maximizing matrix is positive definite, so it is the Gram matrix of five unit vectors in $\mathbb C^5$. Hence the bound is attained. Taking the positive square root of the Gram determinant and expanding $\Delta$ gives the required maximum.

Final Answer: $\boxed{(1+2\rho-\rho^2-\rho\sqrt{5\rho^2+2\rho+1})\sqrt{\sqrt{5\rho^2+2\rho+1}-3\rho}}$

---

## Answer

$(1+2\rho-\rho^2-\rho\sqrt{5\rho^2+2\rho+1})\sqrt{\sqrt{5\rho^2+2\rho+1}-3\rho}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- Hermitian Gram matrices
- cyclic phase normalization
- strict concavity of log determinant
- twisted conjugation symmetry
- circulant spectral optimization
