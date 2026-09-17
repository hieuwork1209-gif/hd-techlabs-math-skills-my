## Steps

Step 1: Determine the Gaussian node
Let
$$
d\mu_\tau(x)=(1+\tau x^2)\,dx+\tau(\delta_{-1}+\delta_1),\qquad \tau>0,
$$
and write
$$
m_k=\int_{-1}^1x^k\,d\mu_\tau(x).
$$
The measure is even, so $m_{2j+1}=0$, and
$$
m_{2j}=\frac{2}{2j+1}+\frac{2\tau}{2j+3}+2\tau. \tag{1}
$$
In particular,
$$
m_2=\frac{2(18\tau+5)}{15},\qquad
m_4=\frac{2(40\tau+7)}{35}.
$$
The monic cubic orthogonal polynomial is odd, hence is
$$
g_3(x)=x(x^2-r),
$$
where $r=a_\tau^2$. Orthogonality to $x$ gives
$$
0=\int xg_3(x)\,d\mu_\tau=m_4-rm_2,
$$
so
$$
r=\frac{3(40\tau+7)}{7(18\tau+5)}. \tag{2}
$$
For every $\tau>0$, $0<r<1$.

Step 2: Force compatibility from the two missing moments
Assume a nested symmetric seven-node rule exists and put
$$
q=b^2,
\qquad
\Pi(x)=x(x^2-1)(x^2-r)(x^2-q).
$$
Because $\Pi$ vanishes at all seven nodes, exactness through degree $11$ forces
$$
\int \Pi(x)x\,d\mu_\tau(x)=0,
\qquad
\int \Pi(x)x^3\,d\mu_\tau(x)=0. \tag{3}
$$
Unlike the endpoint-mass-only family, the density $1+\tau x^2$ keeps the parameter in these two conditions. Expanding (3) gives
$$
m_8-(1+r+q)m_6+(r+q+rq)m_4-rqm_2=0, \tag{4}
$$
$$
m_{10}-(1+r+q)m_8+(r+q+rq)m_6-rqm_4=0. \tag{5}
$$
Substitute (1) and the Gaussian relation (2). Solving (4) for $q$ gives
$$
q=\frac{1095\tau^2+2440\tau+77}
{11(225\tau^2+700\tau+63)}, \tag{6}
$$
whereas (5) gives
$$
q=\frac{5(1491\tau^2+2700\tau-91)}
{13(1095\tau^2+2440\tau+77)}. \tag{7}
$$
Thus compatibility forces
$$
P(\tau):=
357975\tau^4+2668650\tau^3+3550150\tau^2+120890\tau-49049=0. \tag{8}
$$
For $\tau>0$,
$$
P'(\tau)=1431900\tau^3+8005950\tau^2+7100300\tau+120890>0,
$$
so $P$ has at most one positive zero. Moreover
$$
P\!\left(\frac9{100}\right)<0,
\qquad
P\!\left(\frac1{10}\right)=\frac{498379}{400}>0.
$$
Hence there is exactly one positive candidate
$$
t:=\operatorname{root}_{(9/100,1/10)}P. \tag{9}
$$

At $\tau=t$, define
$$
r=\frac{3(40t+7)}{7(18t+5)},
\qquad
q=\frac{1095t^2+2440t+77}{11(225t^2+700t+63)}. \tag{10}
$$
Both are positive, and
$$
r-q=
\frac{2(79515t^3+315105t^2+74879t+5929)}
{77(18t+5)(225t^2+700t+63)}>0. \tag{11}
$$
Together with $r<1$, this gives
$$
0<q<r<1,
$$
so
$$
b=\sqrt q,\qquad a_t=\sqrt r
$$
indeed satisfy $0<b<a_t<1$.

Step 3: Construct the positive degree-$11$ rule
Match the even moments of degrees $0,2,4,6$ with
$$
Q(p)=A[p(-1)+p(1)]
+B[p(-\sqrt q)+p(\sqrt q)]
+C[p(-\sqrt r)+p(\sqrt r)]
+Dp(0).
$$
The degree-$2,4,6$ equations form a Vandermonde system because $1,q,r$ are distinct, so $A,B,C$ are unique, and the mass equation then fixes $D$. Solving and factoring gives
$$
A=
\frac{11(225t^2+700t+63)^2}
{630(3t+7)(345t^2+1315t+154)}, \tag{12}
$$
$$
B=
\frac{1331(225t^2+700t+63)^4}
{630(345t^2+1315t+154)(1095t^2+2440t+77)
(79515t^3+315105t^2+74879t+5929)}, \tag{13}
$$
$$
C=
\frac{686(18t+5)^4(5t^2+30t+33)}
{135(3t+7)(40t+7)(79515t^3+315105t^2+74879t+5929)}, \tag{14}
$$
$$
D=
\frac{64(25245t^4+468090t^3+931742t^2+151410t+1617)}
{945(40t+7)(1095t^2+2440t+77)}. \tag{15}
$$
Every factor in (12)-(15) is positive because $t>0$, so all four weights are positive.

The rule now matches degrees $0,2,4,6$. Equation (4) is exactly the vanishing of the degree-$8$ error on $\Pi x$, so degree $8$ also matches. With degree $8$ established, (5) is exactly the vanishing of the degree-$10$ error on $\Pi x^3$, so degree $10$ matches as well. Symmetry handles every odd degree. Therefore the rule is exact for all polynomials of degree at most $11$.

Step 4: Prove uniqueness
Conversely, every compatible nested rule must satisfy the Gaussian relation (2) and both annihilation identities (3). Hence its $q$ must satisfy both (6) and (7), so its parameter must satisfy $P(\tau)=0$. By Step 2, the only positive possibility is $\tau=t$. Then (10) fixes both nontrivial interior nodes, and the distinct-node moment system fixes $A,B,C,D$ uniquely. Thus the compatible parameter and the entire positive nested rule are unique.

Final Answer: $\boxed{\operatorname{root}_{(9/100,1/10)}P}$

---

## Answer

$\operatorname{root}_{(9/100,1/10)}P$

---

## Classification

**Problem Type:** Symbolic derivation

**Answer Type:** Exact scalar

---

## Solution Concepts

- Gaussian quadrature nodes
- nested quadrature compatibility
- parameterized moment equations
- node-polynomial annihilation
- positive quadrature weights
