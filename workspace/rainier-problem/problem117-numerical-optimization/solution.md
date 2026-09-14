## Steps

Step 1: Rewrite the three sweep factors using reflections
Let
$$
S=\begin{bmatrix}1&0\\0&-1\end{bmatrix},
\qquad
u=1-\frac{5}{2}\alpha,
\qquad
v=\frac{3}{2}\alpha.
$$
Since
$$
\operatorname{diag}(1-\alpha,1-4\alpha)=uI+vS,
$$
we have
$$
I-\alpha P_k=uI+vN_k,
\qquad
N_k=R_kSR_k^T.
$$
The three reflection matrices are
$$
N_0=\begin{bmatrix}1&0\\0&-1\end{bmatrix},
\quad
N_1=\frac12\begin{bmatrix}-1&\sqrt3\\\sqrt3&1\end{bmatrix},
\quad
N_2=\frac12\begin{bmatrix}-1&-\sqrt3\\-\sqrt3&1\end{bmatrix}.
$$
With
$$
J=\begin{bmatrix}0&-1\\1&0\end{bmatrix},
$$
direct multiplication of these three displayed matrices gives
$$
N_0+N_1+N_2=0,
$$
$$
N_2N_1+N_2N_0+N_1N_0=-\frac32I+\frac{\sqrt3}{2}J,
\qquad
N_2N_1N_0=N_1.
$$
Therefore the three-stage update matrix
$$
A=(uI+vN_2)(uI+vN_1)(uI+vN_0)
$$
reduces to
$$
A=sI+tJ+v^3N_1,
$$
where
$$
s=u^3-\frac32uv^2,
\qquad
t=\frac{\sqrt3}{2}uv^2.
$$

Step 2: Obtain a scalar formula for the worst-case contraction
Write $c=v^3$. The identities
$$
J^T=-J,
\qquad
N_1^T=N_1,
\qquad
N_1^2=I,
\qquad
N_1J=-JN_1
$$
give
$$
A^TA=(s^2+t^2+c^2)I+2cK,
\qquad
K=sN_1-tJN_1.
$$
Moreover $K$ is symmetric, $\operatorname{tr}K=0$, and
$$
K^2=(s^2+t^2)I.
$$
Hence the eigenvalues of $K$ are $\pm\sqrt{s^2+t^2}$, so the two squared singular values of $A$ are
$$
\left(\sqrt{s^2+t^2}\pm c\right)^2.
$$
Because $v>0$, the larger singular value is
$$
R(\alpha)=\sqrt{s^2+t^2}+v^3.
$$
Using the formulas for $s$ and $t$,
$$
s^2+t^2=u^2\left(u^4-3u^2v^2+3v^4\right),
$$
and therefore
$$
R(\alpha)=|u|\sqrt{u^4-3u^2v^2+3v^4}+v^3.
$$
For $0<\alpha<2/5$, we have $u>0$. Put
$$
r=\frac vu>0.
$$
Solving for $\alpha$ and $u$ gives
$$
\alpha=\frac{2r}{3+5r},
\qquad
u=\frac{3}{3+5r}=\frac{1}{1+5r/3}.
$$
Thus minimizing on $0<\alpha<2/5$ is equivalent to minimizing, for $r>0$,
$$
G(r)=\frac{w(r)+r^3}{(1+5r/3)^3},
\qquad
w(r)=\sqrt{1-3r^2+3r^4}.
$$
The radical is always positive because
$$
1-3r^2+3r^4=3\left(r^2-\frac12\right)^2+\frac14>0.
$$

Step 3: Prove that the scalar objective has one and only one minimizer
Define
$$
P(r)=5r^4-6r^3-10r^2+3r+5.
$$
Differentiating the displayed formula for $G$ and using
$$
w'(r)=\frac{3r(2r^2-1)}{w(r)}
$$
gives, after collecting terms,
$$
G'(r)=-\frac{P(r)-3r^2w(r)}{w(r)(1+5r/3)^4}.
$$
The denominator is positive. To determine the numerator sign without numerically solving the stationary equation, expand the difference of squares:
$$
P(r)^2-9r^4w(r)^2=-(r^2-1)^2H(r),
$$
where
$$
H(r)=2r^4+60r^3+41r^2-30r-25.
$$
Now
$$
H'(r)=8r^3+180r^2+82r-30,
$$
$$
H''(r)=24r^2+360r+82>0\qquad(r>0).
$$
Thus $H'$ is strictly increasing. Since $H'(0)=-30$ and $H'(1)=240$, there is exactly one $c\in(0,1)$ with $H'(c)=0$. Hence $H$ decreases on $(0,c)$ and increases on $(c,\infty)$. Because
$$
H(0)=-25,
\qquad
H(1)=48,
$$
there is exactly one positive zero $\rho\in(c,1)$ of $H$.

For $0<r<\rho$, we have $H(r)<0$ and $r\ne1$, so
$$
P(r)^2>9r^4w(r)^2.
$$
Thus $P$ cannot vanish there. Since $P(0)=5$, continuity gives $P(r)>0$, and hence
$$
P(r)>3r^2w(r).
$$
Therefore $G'(r)<0$ for $0<r<\rho$. Taking $r\to\rho^-$ shows $P(\rho)\ge0$; the difference-of-squares identity at $\rho$ then gives
$$
P(\rho)=3\rho^2w(\rho),
$$
so $G'(\rho)=0$. For $r>\rho$ with $r\ne1$, $H(r)>0$, hence
$$
P(r)^2<9r^4w(r)^2,
$$
which implies $P(r)-3r^2w(r)<0$ and therefore $G'(r)>0$. At $r=1$ directly,
$$
P(1)-3w(1)=-6<0,
$$
so $G'(1)>0$ as well. Consequently $G$ decreases up to $\rho$ and increases afterwards, and $r=\rho$ is its unique global minimizer on $(0,\infty)$.

Step 4: Isolate the minimizer and round the two requested values by hand
Simple rational substitutions give
$$
H\left(\frac{31}{42}\right)=-\frac{135257}{1555848}<0,
\qquad
H\left(\frac{17}{23}\right)=\frac{13908}{279841}>0.
$$
Since $H$ has only one positive zero,
$$
\frac{31}{42}<\rho<\frac{17}{23}.
$$
The map $r\mapsto 2r/(3+5r)$ is strictly increasing, so
$$
\frac{62}{281}<\alpha_*<\frac{17}{77}.
$$
Furthermore
$$
\frac{62}{281}-\frac{441}{2000}=\frac{79}{562000}>0,
\qquad
\frac{443}{2000}-\frac{17}{77}=\frac{111}{154000}>0.
$$
Hence
$$
0.2205<\alpha_*<0.2215,
$$
so $\alpha_*$ rounds to $0.221$.

It remains to justify the rounding of $R_*$. First, the trial value $\alpha=2/9$ gives $u=4/9$, $v=1/3$, and $r=3/4$, so
$$
R_*\leq R\left(\frac29\right)=\frac{27+4\sqrt{67}}{729}.
$$
Since $\sqrt{67}<41/5$,
$$
R_*<\frac{299}{3645}<\frac{33}{400}=0.0825,
$$
where
$$
\frac{33}{400}-\frac{299}{3645}=\frac{137}{291600}>0.
$$
For the lower bound, write
$$
u_*=\frac{3}{3+5\rho}.
$$
The bracket for $\rho$ gives
$$
u_*>\frac{69}{154}>\frac{56}{125},
\qquad
\rho^3>\left(\frac{31}{42}\right)^3>\frac{201}{500}.
$$
Also
$$
\left(\frac{31}{42}\right)^2=\frac{961}{1764}>\frac12,
$$
so $31/42>1/\sqrt2$. The polynomial
$$
F(r)=1-3r^2+3r^4
$$
has derivative $F'(r)=6r(2r^2-1)>0$ for $r>1/\sqrt2$. Therefore
$$
w(\rho)^2>F\left(\frac{31}{42}\right)=\frac{265549}{1037232}>\left(\frac{101}{200}\right)^2,
$$
so $w(\rho)>101/200$. It follows that
$$
R_*=u_*^3\left(w(\rho)+\rho^3\right)
>\left(\frac{56}{125}\right)^3\frac{907}{1000}
>\frac{163}{2000}=0.0815,
$$
with the last inequality certified by
$$
\left(\frac{56}{125}\right)^3\frac{907}{1000}-\frac{163}{2000}
=\frac{208049}{3906250000}>0.
$$
Thus $R_*$ rounds to $0.082$.

Finally, for $2/5\leq\alpha\leq1/2$, the scalar norm formula from Step 2 gives
$$
R(\alpha)\geq v^3\geq\left(\frac35\right)^3=\frac{27}{125}=0.216,
$$
whereas the trial value $\alpha=2/9$ has contraction below $0.0825$. Hence no point in $[2/5,1/2]$ can be optimal, and the minimizer found above is the unique global minimizer on the full allowed interval.

Final Answer: $\boxed{\left(0.082,0.221\right)}$

---

## Answer

$\left(0.082,0.221\right)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- cyclic preconditioned gradient descent
- products of planar reflections
- singular-value optimization
- derivative sign analysis
- rational root isolation
