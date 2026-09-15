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
\rho(q)=\lambda_{\max}\!\left(A^{-1/2}\Bigl(\sum_\pi q_\pi M_\pi\Bigr)A^{-1/2}\right).
$$

The matrix $A$ is invariant under swapping coordinates $1$ and $2$. Swapping those coordinates sends any distribution $q$ to another distribution with the same value of $\rho$, while $\lambda_{\max}$ is convex in the averaged energy matrix. Therefore averaging $q$ with its swapped copy cannot increase $\rho$. We may restrict to swap-symmetric distributions.

Let $a,b,c$ be the total masses of the three swap-orbits: coordinate $3$ last, middle, and first, respectively. Thus $a,b,c\geq0$ and $a+b+c=1$. Multiplying the displayed $T_i$ matrices and averaging the two permutations in each orbit gives
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

For the symmetric $2\times2$ block on $\operatorname{span}\{u,e_3\}$, nonnegative determinant is necessary. After clearing the positive factor $7/10368$, that determinant condition is
$$
\Delta(a,b,r)\geq0,
$$
where
$$
\begin{aligned}
\Delta(a,b,r)={}&-1071a^2-1519ab-216ar+1287a-532b^2\\
&+1872br+676b+20736r^2-5616r.
\end{aligned}
$$

Step 3: Prove the sharp global lower bound
Define
$$
p(t)=182016t^2-66080t+5997
$$
and let
$$
r_*=\frac{2065-\sqrt{358}}{11376},
$$
the smaller root of $p$. Since
$$
p\left(\frac{17}{96}\right)=\frac{37}{12}>0,
\qquad
p\left(\frac9{50}\right)=-\frac{51}{625}<0,
$$
we have
$$
\frac{17}{96}<r_*<\frac9{50}.
$$

Suppose that some symmetric distribution satisfies $\rho(a,b)<r_*$. Put $r=\rho(a,b)$. From the antisymmetric condition,
$$
a\geq a_0:=18+\frac{22}{3}b-96r.
$$
For $a\geq a_0$,
$$
\frac{\partial\Delta}{\partial a}
=-2142a-1519b-216r+1287
\leq -17227b+205416r-37269.
$$
Because $r<r_*<9/50$,
$$
-17227b+205416r-37269
<-17227b-\frac{7353}{25}<0.
$$
Hence $\Delta(a,b,r)\leq\Delta(a_0,b,r)$. Substituting $a_0$ gives
$$
\Delta(a_0,b,r)
=-54p(r)+(1654080r-299972)b-\frac{207802}{3}b^2.
$$
Again using $r<9/50$,
$$
1654080r-299972<-\frac{11188}{5}<0,
$$
so
$$
\Delta(a,b,r)\leq-54p(r).
$$
But Step 2 gives $r\geq17/96$, and on the interval $[17/96,r_*)$ the quadratic $p$ is positive because $r_*$ is its smaller root. Therefore $\Delta(a,b,r)<0$, contradicting the necessary determinant condition. Thus every distribution satisfies
$$
\rho(q)\geq r_*.
$$

Step 4: Construct a distribution attaining the lower bound
Set
$$
r=r_*,
\qquad
b=0,
\qquad
a=18-96r,
\qquad
c=1-a.
$$
The bounds $17/96<r<9/50$ imply $0<a<1$. Assign probability $a/2$ to each of the permutations $123,213$, probability $c/2$ to each of $312,321$, and probability $0$ to $132,231$.

For this distribution the antisymmetric block is exactly tight because
$$
\frac{54-3a}{288}=r.
$$
For the symmetric block, substituting $a=18-96r$ and $b=0$ gives
$$
\Delta(a,0,r)=-54p(r)=0.
$$
Its two diagonal entries are
$$
\frac{4(34-183r)}9,
\qquad
\frac{3(184r-33)}8.
$$
The first is positive because $r<9/50<34/183$. Also
$$
p\left(\frac{33}{184}\right)=\frac{189}{529}>0
$$
while $p(9/50)<0$, so the smaller root satisfies $r_*>33/184$ and the second diagonal entry is positive. Hence the symmetric $2\times2$ slack matrix is positive semidefinite with determinant zero. The antisymmetric slack is zero, so altogether
$$
r_*A-M(a,0)\succeq0.
$$
Therefore this distribution has $\rho(q)\leq r_*$. Combined with Step 3,
$$
\rho_*=r_*.
$$

Step 5: State the optimal one-epoch contraction
The sharp worst-case expected energy contraction over all distributions on the six coordinate orders is the smaller root found in Step 3.

Final Answer: $\boxed{\frac{2065-\sqrt{358}}{11376}}$

---

## Answer

$\frac{2065-\sqrt{358}}{11376}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

---

## Solution Concepts

- randomized Gauss-Seidel sweeps
- generalized Rayleigh quotient
- symmetry reduction
- semidefinite matrix inequality
- sharp minimax lower bound
