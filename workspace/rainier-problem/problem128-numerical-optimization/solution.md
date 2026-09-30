## Steps

Step 1: Write one random-reshuffling epoch as an expected quadratic form
Set
$$
G=\frac{H}{2}=
\begin{pmatrix}
1&\frac{1}{2}&0\\
\frac{1}{2}&1&\frac{1}{2}\\
0&\frac{1}{2}&1
\end{pmatrix},
$$
so $f(x)=x^TGx$. Exact minimization in coordinate $i$ has update matrix
$$
T_i=I-e_ie_i^TG.
$$
Therefore
$
T_1=
\begin{pmatrix}
0&-\frac{1}{2}&0\\
0&1&0\\
0&0&1
\end{pmatrix},
\quad
T_2=
\begin{pmatrix}
1&0&0\\
-\frac{1}{2}&0&-\frac{1}{2}\\
0&0&1
\end{pmatrix},
\quad
T_3=
\begin{pmatrix}
1&0&0\\
0&1&0\\
0&-\frac{1}{2}&0
\end{pmatrix}.
$$
For a permutation $\pi=(\pi_1,\pi_2,\pi_3)$, one full epoch is
$$
T_\pi=T_{\pi_3}T_{\pi_2}T_{\pi_1}.
$$
If the permutation law is $\nu$, then
$$
\mathbb E[f(x_3)]
=
x_0^TN_\nu x_0,
\qquad
N_\nu=\sum_{\pi}\nu(\pi)T_\pi^TGT_\pi.
$$
Therefore
$
\rho(\nu)
=
\max_{x\neq0}\frac{x^TN_\nu x}{x^TGx},
$$
the largest generalized eigenvalue of $(N_\nu,G)$.

Step 2: Reduce the six permutation weights to three reflection orbits
Let $R$ exchange coordinates $1$ and $3$. Since $R^TGR=G$, reflecting a permutation preserves the value of $\rho$. The map
$$
N\longmapsto
\max_{x\neq0}\frac{x^TNx}{x^TGx}
$$
is convex in $N$, being a maximum of linear functions of $N$. Therefore averaging any law with its reflected law cannot increase $\rho$. It is enough to use reflection-invariant laws.

There are three reflection orbits:
$$
\mathcal O_0=\{123,321\},
\qquad
\mathcal O_1=\{132,312\},
\qquad
\mathcal O_2=\{213,231\}.
$$
Let their total probabilities be $x,y,z$, with $x+y+z=1$.

Multiplying the displayed coordinate-update matrices gives the orbit-average epoch energy matrices
$$
A_0=
\begin{pmatrix}
\frac{3}{32}&\frac{1}{64}&0\\
\frac{1}{64}&\frac{11}{64}&\frac{1}{64}\\
0&\frac{1}{64}&\frac{3}{32}
\end{pmatrix},
$$
$$
A_1=
\begin{pmatrix}
0&0&0\\
0&\frac{1}{4}&0\\
0&0&0
\end{pmatrix},
\qquad
A_2=
\begin{pmatrix}
\frac{1}{8}&0&\frac{1}{8}\\
0&0&0\\
\frac{1}{8}&0&\frac{1}{8}
\end{pmatrix}.
$$
For example,
$$
T_{123}=
\begin{pmatrix}
0&-\frac{1}{2}&0\\
0&\frac{1}{4}&-\frac{1}{2}\\
0&-\frac{1}{8}&\frac{1}{4}
\end{pmatrix},
$$
and
$$
T_{123}^TGT_{123}=
\begin{pmatrix}
0&0&0\\
0&\frac{11}{64}&\frac{1}{32}\\
0&\frac{1}{32}&\frac{3}{16}
\end{pmatrix};
$$
averaging this with its reflected partner $321$ gives $A_0$. The other two orbit matrices follow from
$$
T_{132}=T_{312}=
\begin{pmatrix}
0&-\frac{1}{2}&0\\
0&\frac{1}{2}&0\\
0&-\frac{1}{2}&0
\end{pmatrix},
$$
and
$$
T_{213}=T_{231}=
\begin{pmatrix}
\frac{1}{4}&0&\frac{1}{4}\\
-\frac{1}{2}&0&-\frac{1}{2}\\
\frac{1}{4}&0&\frac{1}{4}
\end{pmatrix}.
$$
Every reflected law therefore has
$$
N=xA_0+yA_1+zA_2.
$$

Step 3: Build a sharp Rayleigh-quotient lower-bound certificate
For a symmetric test vector
$$
u_q=(1,q,1)^T,
$$
one has
$$
u_q^TGu_q=q^2+2q+2.
$$
The three orbit Rayleigh quotients are
$$
r_0(q)=
\frac{11q^2+4q+12}{64(q^2+2q+2)},
$$
$$
r_1(q)=
\frac{q^2}{4(q^2+2q+2)},
\qquad
r_2(q)=
\frac{1}{2(q^2+2q+2)}.
$$
To make one test vector certify a common lower bound for the two orbit families that will be used at equality, impose
$$
r_0(q)=r_2(q).
$$
This gives
$$
11q^2+4q-20=0.
$$
Choose the negative root
$$
q_*=-\frac{2+4\sqrt{14}}{11}.
$$
For this root,
$$
r_0(q_*)=r_2(q_*)
=
\frac{71}{300}+\frac{\sqrt{14}}{25}
=: \rho_*,
$$
while
$$
r_1(q_*)
=
\frac{13}{50}+\frac{4\sqrt{14}}{75}
=
\rho_*+\frac{7}{300}+\frac{\sqrt{14}}{75}
>
\rho_*.
$$

Therefore, for every reflected law,
$$
\frac{u_{q_*}^TNu_{q_*}}{u_{q_*}^TGu_{q_*}}
=
xr_0(q_*)+yr_1(q_*)+zr_2(q_*)
\geq
\rho_*.
$$
Since the largest generalized eigenvalue is at least every Rayleigh quotient,
$$
\rho(\nu)\geq\rho_*
$$
for every reflected law, and therefore for every permutation law.

Step 4: Construct a reshuffling law that attains the lower bound
Equality in the certificate requires $y=0$. Set
$$
x_*=
\frac{64}{75}+\frac{2\sqrt{14}}{175},
\qquad
z_*=1-x_*.
$$
Choose the law that gives total mass $x_*$ to $\mathcal O_0$, total mass $z_*$ to $\mathcal O_2$, and zero mass to $\mathcal O_1$, split equally inside each reflection pair.

Let
$$
N_*=x_*A_0+z_*A_2.
$$
Substituting $q_*$, $\rho_*$, and $x_*$ into
$$
(N_*-\rho_*G)u_{q_*}
$$
gives zero. For instance, the second coordinate is
$$
-\frac{\sqrt{14}}{16}x_*
+\frac{1}{100}
+\frac{4\sqrt{14}}{75}=0,
$$
which is exactly the equation that yields the displayed value of $x_*$. Therefore $\rho_*$ is a generalized eigenvalue of $(N_*,G)$.

It remains to show that it is the largest one. Reflection symmetry splits the generalized eigenproblem into the antisymmetric line and the symmetric plane. On the antisymmetric line the eigenvalue is
$$
\lambda_{\mathrm a}
=
\frac{3x_*}{32}
=
\frac{2}{25}+\frac{3\sqrt{14}}{2800}.
$$
On the symmetric plane, besides $\rho_*$ the other generalized eigenvalue is
$$
\lambda_{\mathrm s}
=
\frac{71}{300}-\frac{113\sqrt{14}}{2800}.
$$
Their gaps from $\rho_*$ are
$$
\rho_*-\lambda_{\mathrm a}
=
\frac{1316+327\sqrt{14}}{8400}>0,
$$
and
$$
\rho_*-\lambda_{\mathrm s}
=
\frac{9\sqrt{14}}{112}>0.
$$
Therefore
$
\rho(\nu_*)=\rho_*.
$$

Step 5: Evaluate the best one-epoch factor
Step 3 gives the universal lower bound $\rho(\nu)\geq\rho_*$, while Step 4 constructs a permutation law attaining it. Therefore
$$
\inf_\nu \rho(\nu)
=
\frac{71}{300}+\frac{\sqrt{14}}{25}.
$$
Final Answer: $\boxed{\frac{71}{300}+\frac{\sqrt{14}}{25}}$

---

## Answer

$\frac{71}{300}+\frac{\sqrt{14}}{25}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

---

## Solution Concepts

- randomized coordinate descent
- random reshuffling
- generalized eigenvalues
- symmetry averaging
- Rayleigh quotient certificate
