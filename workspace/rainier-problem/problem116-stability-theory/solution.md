## Steps

Step 1: Symmetrize the two subsystem gains
Let
$$
A_1=\begin{pmatrix}-1&a\\0&-1\end{pmatrix},
\qquad
A_2=\begin{pmatrix}-1&0\\b&-1\end{pmatrix},
\qquad a,b>0,
$$
and let the switching mode be the two-state continuous-time Markov chain that jumps from either state to the other at rate $1$.

Put
$$
p=\sqrt{ab},
\qquad
D=\operatorname{diag}(\sqrt b,\sqrt a).
$$
With $y=Dz$, the two matrices become
$$
B_1=DA_1D^{-1}=\begin{pmatrix}-1&p\\0&-1\end{pmatrix},
\qquad
B_2=DA_2D^{-1}=\begin{pmatrix}-1&0\\p&-1\end{pmatrix}.
$$
Since $D$ is fixed and invertible, mean-square exponential stability is unchanged. Thus the problem depends on $(a,b)$ only through $p^2=ab$.

Step 2: Write the closed system for conditional second moments
For $i=1,2$, define
$$
u_i(t)=\mathbb E\bigl[y_1(t)^2\mathbf 1_{\{\sigma(t)=i\}}\bigr],
\quad
v_i(t)=\mathbb E\bigl[y_1(t)y_2(t)\mathbf 1_{\{\sigma(t)=i\}}\bigr],
\quad
w_i(t)=\mathbb E\bigl[y_2(t)^2\mathbf 1_{\{\sigma(t)=i\}}\bigr].
$$
The deterministic dynamics in each mode give
$$
\begin{array}{lll}
\dot u=-2u+2pv,&\dot v=-2v+pw,&\dot w=-2w \qquad (\text{mode }1),\\
\dot u=-2u,&\dot v=-2v+pu,&\dot w=-2w+2pv \qquad (\text{mode }2).
\end{array}
$$
The Markov chain contributes loss at rate $1$ from the current mode and gain at rate $1$ from the other mode. Hence
$$
\frac d{dt}
\begin{pmatrix}u_1\\v_1\\w_1\\u_2\\v_2\\w_2\end{pmatrix}
=L(p)
\begin{pmatrix}u_1\\v_1\\w_1\\u_2\\v_2\\w_2\end{pmatrix},
$$
where
$$
L(p)=
\begin{pmatrix}
-3&2p&0&1&0&0\\
0&-3&p&0&1&0\\
0&0&-3&0&0&1\\
1&0&0&-3&0&0\\
0&1&0&p&-3&0\\
0&0&1&0&2p&-3
\end{pmatrix}.
$$
Moreover
$$
\mathbb E\|y(t)\|^2=u_1+w_1+u_2+w_2.
$$
Therefore the Markov jump system is mean-square exponentially stable exactly when the lifted matrix $L(p)$ is Hurwitz. This follows directly from the closed linear evolution above: if $L(p)$ is Hurwitz all conditional second moments decay exponentially, while if its spectral bound is nonnegative the invariant cone of conditional positive-semidefinite second moments contains initial data whose second moment does not decay exponentially.

Step 3: Split the lift by its reflection symmetry
The lift is invariant under simultaneously interchanging the two modes and swapping the two state coordinates. Thus it decomposes into two three-dimensional invariant subspaces.

On the symmetric subspace
$$
u_1=w_2=x,
\qquad
w_1=u_2=y,
\qquad
v_1=v_2=v,
$$
we obtain
$$
\frac d{dt}\begin{pmatrix}x\\y\\v\end{pmatrix}
=
\begin{pmatrix}
-3&1&2p\\
1&-3&0\\
0&p&-2
\end{pmatrix}
\begin{pmatrix}x\\y\\v\end{pmatrix},
$$
whose characteristic polynomial is
$$
\chi_+(\lambda)
=\lambda^3+8\lambda^2+20\lambda+16-2p^2.
$$

On the antisymmetric subspace
$$
u_1=-w_2=x,
\qquad
w_1=-u_2=y,
\qquad
v_1=-v_2=v,
$$
we obtain
$$
\frac d{dt}\begin{pmatrix}x\\y\\v\end{pmatrix}
=
\begin{pmatrix}
-3&-1&2p\\
-1&-3&0\\
0&p&-4
\end{pmatrix}
\begin{pmatrix}x\\y\\v\end{pmatrix},
$$
with characteristic polynomial
$$
\chi_-(\lambda)
=\lambda^3+10\lambda^2+32\lambda+32+2p^2.
$$
Hence
$$
\det(\lambda I-L(p))=\chi_+(\lambda)\chi_-(\lambda).
$$

Step 4: Apply the cubic Hurwitz criterion
For a real cubic
$$
\lambda^3+c_1\lambda^2+c_2\lambda+c_3,
$$
all roots have negative real part exactly when
$$
c_1>0,\qquad c_2>0,\qquad c_3>0,\qquad c_1c_2>c_3.
$$
For $\chi_+$ this gives
$$
16-2p^2>0,
$$
because once this holds, $8\cdot20>16-2p^2$ is automatic. Thus
$$
\chi_+\text{ is Hurwitz}\iff p^2<8.
$$

For $\chi_-$ all coefficients are positive, and its only nontrivial Hurwitz inequality is
$$
10\cdot32>32+2p^2,
$$
i.e. $p^2<144$. Hence whenever $p^2<8$, the antisymmetric block is automatically Hurwitz as well.

At $p^2=8$, $\chi_+(0)=0$, so the lift has a zero eigenvalue and exponential decay fails. If $p^2>8$, then $\chi_+(0)<0$ while $\chi_+(\lambda)\to+\infty$ as $\lambda\to+\infty$, so $\chi_+$ has a positive real root and mean-square stability fails.

Step 5: State the exact parameter region
Since $p^2=ab$, the origin is uniformly globally mean-square exponentially stable exactly when
$$
a>0,\qquad b>0,\qquad ab<8.
$$
Final Answer: $\boxed{\{(a,b):a>0,\ b>0,\ ab<8\}}$

---

## Answer

$\{(a,b):a>0,\ b>0,\ ab<8\}$

---

## Classification

**Problem Type:** Solve for unknowns

**Answer Type:** Interval or region description

---

## Solution Concepts

- Markov jump linear systems
- mean-square exponential stability
- conditional second moments
- invariant symmetry decomposition
- Routh-Hurwitz criterion

---

## Black-Box Audit — no issues found
