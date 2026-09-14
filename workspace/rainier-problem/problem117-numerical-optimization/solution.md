## Steps

Step 1: Reduce the sweep norm to a scalar function
Let
$$
S=\begin{bmatrix}1&0\\0&-1\end{bmatrix},\qquad
u=1-\frac52\alpha,\qquad v=\frac32\alpha,
$$
and set $N_k=R_kSR_k^T$. Then
$$
I-\alpha P_k=uI+vN_k.
$$
The three displayed reflections satisfy
$$
N_0+N_1+N_2=0,
$$
$$
N_2N_1+N_2N_0+N_1N_0=-\frac32I+\frac{\sqrt3}{2}J,
\qquad N_2N_1N_0=N_1,
$$
where $J=\begin{bmatrix}0&-1\\1&0\end{bmatrix}$. Hence the sweep matrix is
$$
A=(uI+vN_2)(uI+vN_1)(uI+vN_0)=sI+tJ+v^3N_1,
$$
with
$$
s=u^3-\frac32uv^2,\qquad t=\frac{\sqrt3}{2}uv^2.
$$
Since $J^T=-J$, $N_1^T=N_1$, $N_1^2=I$, and $N_1J=-JN_1$, the squared singular values of $A$ are
$$
\left(\sqrt{s^2+t^2}\pm v^3\right)^2.
$$
Therefore
$$
R(\alpha)=|u|\sqrt{u^4-3u^2v^2+3v^4}+v^3.
$$
For $0<\alpha<2/5$, put $r=v/u$. Then
$$
\alpha=\frac{2r}{3+5r},\qquad u=\frac{3}{3+5r},
$$
so minimizing $R$ is equivalent to minimizing
$$
G(r)=\frac{w(r)+r^3}{(1+5r/3)^3},\qquad
w(r)=\sqrt{1-3r^2+3r^4},\qquad r>0.
$$
The radical is positive because
$$
1-3r^2+3r^4=3\left(r^2-\frac12\right)^2+\frac14.
$$

Step 2: Prove the scalar objective has a unique global minimizer
Define
$$
P(r)=5r^4-6r^3-10r^2+3r+5.
$$
Differentiation gives
$$
G'(r)=-\frac{P(r)-3r^2w(r)}{w(r)(1+5r/3)^4}.
$$
A direct expansion gives
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
\qquad
H''(r)=24r^2+360r+82>0
$$
for $r>0$. Thus $H'$ is strictly increasing. Since $H'(0)<0<H'(1)$, it has one zero $c\in(0,1)$, so $H$ decreases on $(0,c)$ and increases on $(c,\infty)$. Also $H(0)=-25$ and $H(1)=48$, hence $H$ has exactly one positive zero $\rho\in(c,1)$.

If $0<r<\rho$, then $H(r)<0$, so
$$
P(r)^2>9r^4w(r)^2.
$$
Thus $P$ cannot vanish there; since $P(0)=5$, we have $P(r)>3r^2w(r)$ and hence $G'(r)<0$. At $r=\rho$, continuity gives $P(\rho)\ge0$, while the difference-of-squares identity gives
$$
P(\rho)=3\rho^2w(\rho),
$$
so $G'(\rho)=0$. If $r>\rho$ and $r\ne1$, then $H(r)>0$, hence
$$
P(r)^2<9r^4w(r)^2,
$$
so $P(r)-3r^2w(r)<0$ and $G'(r)>0$. At $r=1$, directly $P(1)-3w(1)=-6<0$. Therefore $G$ decreases on $(0,\rho)$ and increases on $(\rho,\infty)$, so $\rho$ is its unique global minimizer.

Step 3: Isolate the minimizer and round both requested values by hand
Substitution gives
$$
H\left(\frac{31}{42}\right)=-\frac{135257}{1555848}<0,
\qquad
H\left(\frac{17}{23}\right)=\frac{13908}{279841}>0.
$$
Thus
$$
\frac{31}{42}<\rho<\frac{17}{23}.
$$
Because $r\mapsto2r/(3+5r)$ is increasing,
$$
\frac{62}{281}<\alpha_*<\frac{17}{77}.
$$
Moreover
$$
\frac{62}{281}>\frac{441}{2000}=0.2205,
\qquad
\frac{17}{77}<\frac{443}{2000}=0.2215,
$$
so $\alpha_*=0.221$ to three decimal places.

For $R_*$, the trial value $\alpha=2/9$ gives
$$
R_*\le R\left(\frac29\right)=\frac{27+4\sqrt{67}}{729}
<\frac{299}{3645}<0.0825,
$$
using $\sqrt{67}<41/5$. For the lower bound, the bracket for $\rho$ gives
$$
u_* =\frac{3}{3+5\rho}>\frac{69}{154}>\frac{56}{125},
\qquad
\rho^3>\left(\frac{31}{42}\right)^3>\frac{201}{500}.
$$
Also $31/42>1/\sqrt2$, and $F(r)=1-3r^2+3r^4$ is increasing for $r>1/\sqrt2$. Hence
$$
w(\rho)^2>F\left(\frac{31}{42}\right)
=\frac{265549}{1037232}>\left(\frac{101}{200}\right)^2,
$$
so $w(\rho)>101/200$. Therefore
$$
R_*=u_*^3\bigl(w(\rho)+\rho^3\bigr)
>\left(\frac{56}{125}\right)^3\frac{907}{1000}
>0.0815.
$$
Thus $R_*=0.082$ to three decimal places.

Finally, for $2/5\le\alpha\le1/2$, the scalar formula from Step 1 gives
$$
R(\alpha)\ge v^3\ge\left(\frac35\right)^3=0.216,
$$
whereas $R(2/9)<0.0825$. Hence the minimizer above is the unique global minimizer on the full allowed interval.

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
