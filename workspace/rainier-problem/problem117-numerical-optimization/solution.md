## Steps

Step 1: Write each randomized sweep as a quadratic energy operator and reduce by symmetry
Let
$$
A=\begin{bmatrix}
2&1&1\\
1&2&1\\
1&1&3
\end{bmatrix},
\qquad
f(x)=\frac12x^TAx.
$$
The leading principal minors of $A$ are $2$, $3$, and $7$, so $A$ is positive definite. An exact coordinate minimization in coordinate $i$ is linear:
$$
x\longmapsto T_i x,
\qquad
T_i=I-\frac1{A_{ii}}e_i e_i^T A.
$$
Thus
$$
T_1=\begin{bmatrix}0&-1/2&-1/2\\0&1&0\\0&0&1\end{bmatrix},
\quad
T_2=\begin{bmatrix}1&0&0\\-1/2&0&-1/2\\0&0&1\end{bmatrix},
\quad
T_3=\begin{bmatrix}1&0&0\\0&1&0\\-1/3&-1/3&0\end{bmatrix}.
$$
For a permutation $\pi=(\pi_1,\pi_2,\pi_3)$, one sweep has operator
$$
T_\pi=T_{\pi_3}T_{\pi_2}T_{\pi_1},
$$
and its final energy is
$$
2f(T_\pi x)=x^TM_\pi x,
\qquad
M_\pi=T_\pi^TAT_\pi.
$$
Hence for a distribution $q$ on the six permutations,
$$
\rho(q)=\lambda_{\max}\left(A^{-1/2}\Bigl(\sum_\pi q_\pi M_\pi\Bigr)A^{-1/2}\right).
$$

The matrix $A$ is invariant under swapping coordinates $1$ and $2$. Swapping those coordinates sends any distribution $q$ to another distribution with the same value of $\rho$, while $\lambda_{\max}$ is convex in the averaged energy matrix. Therefore averaging $q$ with its swapped copy cannot increase $\rho$. We may restrict to swap-symmetric distributions when computing the optimal value.

Let $a,b,c$ be the total masses of the three swap-orbits: coordinate $3$ last, middle, and first, respectively. Thus $a,b,c\geq0$ and $a+b+c=1$. From the displayed $T_i$ matrices,
$$
M_{123}=\begin{bmatrix}0&0&0\\0&17/48&5/16\\0&5/16&11/16\end{bmatrix},
\quad
M_{132}=\begin{bmatrix}0&0&0\\0&19/36&11/36\\0&11/36&13/36\end{bmatrix},
$$
$$
M_{312}=\begin{bmatrix}19/72&2/9&0\\2/9&5/9&0\\0&0&0\end{bmatrix}.
$$
The partners $M_{213},M_{231},M_{321}$ are obtained by swapping the first two rows and columns. Therefore the three orbit averages are
$$
L=\frac{M_{123}+M_{213}}2
=\begin{bmatrix}
17/96&0&5/32\\
0&17/96&5/32\\
5/32&5/32&11/16
\end{bmatrix},
$$
$$
N=\frac{M_{132}+M_{231}}2
=\begin{bmatrix}
19/72&0&11/72\\
0&19/72&11/72\\
11/72&11/72&13/36
\end{bmatrix},
$$
$$
F=\frac{M_{312}+M_{321}}2
=\begin{bmatrix}
59/144&2/9&0\\
2/9&59/144&0\\
0&0&0
\end{bmatrix}.
$$
So the expected energy matrix is
$$
M(a,b)=aL+bN+(1-a-b)F.
$$

Step 2: Separate the antisymmetric mode from the symmetric two-dimensional mode
Use the basis
$$
u=(1,1,0)^T,
\qquad
v=(1,-1,0)^T,
\qquad
e_3=(0,0,1)^T.
$$
With $P=[u\ v\ e_3]$,
$$
P^TAP=
\begin{bmatrix}
6&0&2\\
0&2&0\\
2&0&3
\end{bmatrix},
$$
and
$$
P^TM(a,b)P=
\begin{bmatrix}
\frac{91}{72}-\frac{131a}{144}-\frac{53b}{72}&0&\frac{5a}{16}+\frac{11b}{36}\\
0&\frac38-\frac{a}{48}+\frac{11b}{72}&0\\
\frac{5a}{16}+\frac{11b}{36}&0&\frac{11a}{16}+\frac{13b}{36}
\end{bmatrix}.
$$
Thus $\rho(a,b)\leq r$ is equivalent to
$$
rP^TAP-P^TM(a,b)P\succeq0.
$$
The antisymmetric one-dimensional block gives the necessary condition
$$
r\geq\frac{54-3a+22b}{288}.
$$
Since $a\leq1-b$, every feasible $r$ obeys
$$
r\geq\frac{51+25b}{288}\geq\frac{17}{96}.
$$

For the symmetric $2\times2$ block on $\operatorname{span}\{u,e_3\}$, nonnegative determinant is necessary. Expanding that determinant gives
$$
\det\left(rA_{\mathrm{sym}}-M_{\mathrm{sym}}(a,b)\right)
=\frac7{10368}\Delta(a,b,r),
$$
where
$$
\begin{aligned}
\Delta(a,b,r)={}&-1071a^2-1519ab-216ar+1287a-532b^2\\
&+1872br+676b+20736r^2-5616r.
\end{aligned}
$$
Thus every feasible triple satisfies $\Delta(a,b,r)\geq0$.

Step 3: Derive the sharp lower bound and its equality conditions
From the antisymmetric condition in Step 2,
$$
a\geq a_0:=18+\frac{22}{3}b-96r.
$$
Assume $r<9/50$. For $a\geq a_0$,
$$
\frac{\partial\Delta}{\partial a}
=-2142a-1519b-216r+1287
\leq -17227b+205416r-37269
<-17227b-\frac{7353}{25}<0.
$$
Hence $\Delta(a,b,r)\leq\Delta(a_0,b,r)$. Substitution gives
$$
\Delta(a_0,b,r)
=-54p(r)+(1654080r-299972)b-\frac{207802}{3}b^2,
$$
where the $b$-independent obstruction is
$$
p(t)=182016t^2-66080t+5997.
$$
For $r<9/50$,
$$
1654080r-299972<-\frac{11188}{5}<0,
$$
so every feasible triple with $r<9/50$ must satisfy
$$
0\leq\Delta(a,b,r)\leq-54p(r).
$$
Thus the first possible threshold above the universal bound $17/96$ is the smaller root of $p$. Its discriminant is
$$
66080^2-4\cdot182016\cdot5997=366592=1024\cdot358,
$$
so define
$$
r_*:=\frac{2065-\sqrt{358}}{11376}.
$$
Since
$$
p\left(\frac{17}{96}\right)=\frac{37}{12}>0,
\qquad
p\left(\frac9{50}\right)=-\frac{51}{625}<0,
$$
we have
$$
\frac{17}{96}<r_*<\frac9{50}.
$$
If a symmetric distribution had contraction $r<r_*$, then Step 2 would give $r\geq17/96$, while the displayed inequality would give $p(r)\leq0$. But $p>0$ on $[17/96,r_*)$, a contradiction. Therefore every swap-symmetric distribution has contraction at least $r_*$. By Step 1, symmetrizing an arbitrary distribution cannot increase its contraction, so every distribution satisfies
$$
\rho(q)\geq r_*.
$$

The same chain determines equality among swap-symmetric distributions. Set $r=r_*$. Then
$$
\Delta(a_0,b,r_*)
=(1654080r_*-299972)b-\frac{207802}{3}b^2\leq0,
$$
and the coefficient of $b$ is strictly negative because $r_*<9/50$. Feasibility requires $\Delta\geq0$, so $b=0$. The derivative bound is then strictly negative for $a\geq18-96r_*$, while
$$
\Delta(18-96r_*,0,r_*)=-54p(r_*)=0.
$$
Hence equality forces
$$
b=0,
\qquad
a=18-96r_*,
\qquad c=1-a.
$$
Thus there is a unique optimal swap-symmetric distribution.

Step 4: Construct the optimal swap-symmetric distribution and record its slack rank
Set
$$
a=18-96r_*,
\qquad
c=1-a.
$$
The bounds $17/96<r_*<9/50$ imply $0<a<1$. Assign probability $a/2$ to each of $123,213$, probability $c/2$ to each of $312,321$, and probability $0$ to $132,231$. Call this distribution $q^*$.

For $q^*$ the antisymmetric block is exactly tight because
$$
\frac{54-3a}{288}=r_*.
$$
For the symmetric block,
$$
\Delta(a,0,r_*)=-54p(r_*)=0.
$$
Its two diagonal entries are
$$
\frac{4(34-183r_*)}9,
\qquad
\frac{3(184r_*-33)}8.
$$
The first is positive because $r_*<9/50<34/183$. Also
$$
p\left(\frac{33}{184}\right)=\frac{189}{529}>0
$$
while $p(9/50)<0$, so $r_*>33/184$ and the second diagonal entry is positive. Hence the symmetric $2\times2$ slack matrix is positive semidefinite with determinant zero, while the antisymmetric slack is zero. Therefore
$$
S_*:=r_*A-\sum_\pi q^*_\pi M_\pi\succeq0
$$
has rank one, and its range lies in the swap-symmetric subspace. Thus $q^*$ attains $\rho_*$.

Step 5: Prove the minimizing distribution is unique
Let $q$ be any minimizing distribution, and let $J$ be the matrix swapping coordinates $1$ and $2$. Let $q^J$ be the distribution obtained by applying this swap to every permutation. Then $q^J$ is also minimizing. Their average $\bar q=(q+q^J)/2$ is swap-symmetric and minimizing, so Step 3 gives
$$
\bar q=q^*.
$$
Define
$$
S(q)=r_*A-\sum_\pi q_\pi M_\pi,
\qquad
S(q^J)=J S(q)J.
$$
Both matrices are positive semidefinite, and
$$
\frac{S(q)+S(q^J)}2=S_*.
$$
For any $z\in\ker S_*$,
$$
0=z^TS_*z=\frac12z^TS(q)z+\frac12z^TS(q^J)z.
$$
Both terms are nonnegative, so both vanish. Since $z^TSz=\|S^{1/2}z\|^2$ for $S\succeq0$, this implies $S(q)z=S(q^J)z=0$. Hence $\ker S_*$ is contained in the kernels of both matrices. Since $S_*$ has rank one, both $S(q)$ and $S(q^J)$ have range contained in $\operatorname{range}S_*$. This range is fixed pointwise by $J$, so $J S(q)J=S(q)$. Therefore $S(q^J)=S(q)$, and their average being $S_*$ yields
$$
S(q)=S_*.
$$
Thus $\sum q_\pi M_\pi=\sum q^*_\pi M_\pi$.

Because $\bar q=q^*$, write
$$
q_{123}=\frac a2+s,
\quad q_{213}=\frac a2-s,
\quad q_{312}=\frac c2+t,
\quad q_{321}=\frac c2-t,
$$
with $q_{132}=q_{231}=0$. Equality of the expected energy matrices gives
$$
s(M_{123}-M_{213})+t(M_{312}-M_{321})=0.
$$
The $(1,3)$ entry is $-5s/16$, so $s=0$. Then the $(1,1)$ entry is $-7t/24$, so $t=0$. Hence $q=q^*$, proving uniqueness.

Finally,
$$
q^*_{123}=q^*_{213}=\frac a2
=9-48r_*
=\frac{68+\sqrt{358}}{237},
$$
and
$$
q^*_{132}=q^*_{231}=0,
\qquad
q^*_{312}=q^*_{321}=\frac{101-2\sqrt{358}}{474}.
$$

Step 6: State the optimum and the reported component of the unique optimizer
The exact contraction and the requested probability under the unique minimizing distribution are now determined.

Final Answer: $\boxed{\left(\frac{2065-\sqrt{358}}{11376},\frac{68+\sqrt{358}}{237}\right)}$

---

## Answer

$\left(\frac{2065-\sqrt{358}}{11376},\frac{68+\sqrt{358}}{237}\right)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- randomized Gauss-Seidel sweeps
- generalized Rayleigh quotient
- symmetry reduction
- semidefinite equality cases
- optimizer uniqueness
