## Steps

Step 1: Encode the environment by local odds ratios

Let \(\omega=(\omega_x)_{x\in\mathbb Z}\) be i.i.d. with
\[
\mathbb P(\omega_x=3/4)=\theta,
\qquad
\mathbb P(\omega_x=1/4)=1-\theta,
\qquad 0<\theta<1.
\]
Given \(\omega\), let \(X_n\) be the nearest-neighbor walk with
\[
P_\omega(X_{n+1}=x+1\mid X_n=x)=\omega_x,
\]
\[
P_\omega(X_{n+1}=x-1\mid X_n=x)=1-\omega_x.
\]
Put
\[
\rho_x:=\frac{1-\omega_x}{\omega_x}.
\]
Then
\[
\rho_x=
\begin{cases}
1/3,&\omega_x=3/4,\\
3,&\omega_x=1/4.
\end{cases}
\tag{1}
\]
The two quantities governing direction and speed are different:
\[
\mathbb E\log\rho_0
=(1-2\theta)\log3,
\tag{2}
\]
while
\[
m_+:=\mathbb E\rho_0
=\frac\theta3+3(1-\theta)
=\frac{9-8\theta}{3}.
\tag{3}
\]
For the reflected walk we will also need
\[
m_-:=\mathbb E\rho_0^{-1}
=3\theta+\frac{1-\theta}{3}
=\frac{1+8\theta}{3}.
\tag{4}
\]

Step 2: Direction of transience and recurrence

Define the potential on the positive half-line by
\[
V(n)=\sum_{j=1}^n\log\rho_j.
\]
The standard one-dimensional hitting-probability formula is obtained by solving the harmonic difference equation
\[
h(x)=\omega_xh(x+1)+(1-\omega_x)h(x-1).
\]
Indeed, if \(h\) is harmonic then
\[
h(x+1)-h(x)=\rho_x\bigl(h(x)-h(x-1)\bigr),
\]
so successive increments are proportional to products of the \(\rho_j\). Thus the convergence or divergence of the corresponding scale sums is controlled by the asymptotic behavior of \(V(n)\).

By the strong law,
\[
\frac{V(n)}n\longrightarrow \mathbb E\log\rho_0
=(1-2\theta)\log3
\qquad\text{a.s.}
\tag{5}
\]
Hence:

- if \(\theta>1/2\), then \(V(n)\to-\infty\) linearly and the walk is transient to \(+\infty\);
- if \(\theta<1/2\), the reflected potential has negative drift and the walk is transient to \(-\infty\);
- if \(\theta=1/2\), then \(\log\rho_x=\pm\log3\) symmetrically, so the potential oscillates to both \(+\infty\) and \(-\infty\), and the scale sums diverge in both directions. The walk is recurrent.

Therefore the exact directional transition is
\[
\boxed{\theta_{\rm dir}=\frac12.}
\tag{6}
\]

Step 3: The right-transient crossing-time series

Assume \(\theta>1/2\), so the walk is transient to the right. Let
\[
T_1=\inf\{n\ge0:X_n=1\}
\]
when the walk starts at \(0\). The quenched expected crossing time has the standard series representation
\[
E_\omega^0T_1
=1+2\sum_{k=0}^\infty
\rho_0\rho_{-1}\cdots\rho_{-k}.
\tag{7}
\]
For completeness, this follows by writing the first-step recursion for the expected number of left excursions before the first crossing of the edge \((0,1)\): every left excursion contributes two steps, and the expected number of excursions reaching successively farther left produces the products in (7).

Taking annealed expectation and using independence,
\[
\mathbb E E_\omega^0T_1
=1+2\sum_{k=0}^\infty m_+^{k+1}.
\tag{8}
\]
Thus the mean crossing time is finite exactly when
\[
m_+<1
\iff
\frac{9-8\theta}{3}<1
\iff
\boxed{\theta>\frac34.}
\tag{9}
\]
In that regime,
\[
\mathbb E T_1
=1+\frac{2m_+}{1-m_+}
=\frac{1+m_+}{1-m_+}
=\boxed{\frac{6-4\theta}{4\theta-3}}.
\tag{10}
\]
For \(1/2<\theta\le3/4\), the walk still goes to \(+\infty\), but the annealed mean time to advance one level is infinite.

The one-dimensional RWRE law of large numbers can be read from these crossing times: in the right-transient regime,
\[
v(\theta):=\lim_{n\to\infty}\frac{X_n}{n}
=\begin{cases}
\displaystyle \frac1{\mathbb ET_1},&\mathbb ET_1<\infty,\\[2mm]
0,&\mathbb ET_1=\infty,
\end{cases}
\qquad\text{a.s. under the annealed law.}
\tag{11}
\]
Hence
\[
\boxed{
v(\theta)=\frac{4\theta-3}{6-4\theta}
\qquad\left(\frac34<\theta<1\right),
}
\tag{12}
\]
and
\[
\boxed{
v(\theta)=0
\qquad\left(\frac12<\theta\le\frac34\right).
}
\tag{13}
\]

Step 4: The left-transient regime by reflection

Reflect space by replacing \(X_n\) with \(-X_n\). The reflected walk has right-jump probability \(1-\omega_{-x}\), so its odds ratio is \(\rho_x^{-1}\). Therefore the leftward crossing time has finite annealed mean exactly when
\[
m_-<1
\iff
\frac{1+8\theta}{3}<1
\iff
\boxed{\theta<\frac14.}
\tag{14}
\]
In that regime,
\[
\mathbb ET_{-1}
=\frac{1+m_-}{1-m_-}
=\boxed{\frac{2+4\theta}{1-4\theta}}.
\tag{15}
\]
Consequently
\[
\boxed{
v(\theta)
=-\frac1{\mathbb ET_{-1}}
=\frac{4\theta-1}{2+4\theta}
\qquad\left(0<\theta<\frac14\right).
}
\tag{16}
\]
For
\[
\frac14\le\theta<\frac12,
\]
the walk is transient to \(-\infty\) but has zero limiting speed.

At \(\theta=1/2\), recurrence also gives \(v(1/2)=0\). Thus the two ballistic thresholds are
\[
\boxed{\theta_-=\frac14,
\qquad
\theta_+=\frac34.}
\tag{17}
\]
Both threshold points themselves have zero speed because the relevant geometric series in (8) or its reflected analogue is then critical and diverges.

Step 5: Collect the complete phase diagram

The almost-sure annealed velocity exists for every \(0<\theta<1\) and is
\[
\boxed{
v(\theta)=
\begin{cases}
\displaystyle \frac{4\theta-1}{2+4\theta},
&0<\theta<\frac14,\\[3mm]
0,
&\frac14\le\theta\le\frac34,\\[3mm]
\displaystyle \frac{4\theta-3}{6-4\theta},
&\frac34<\theta<1.
\end{cases}
}
\tag{18}
\]
The directional behavior is finer than the velocity:
\[
\boxed{
\begin{array}{c|c|c}
\theta&\text{direction}&v(\theta)\\ \hline
(0,1/4)&X_n\to-\infty&<0\\
[1/4,1/2)&X_n\to-\infty&0\\
\{1/2\}&\text{recurrent}&0\\
(1/2,3/4]&X_n\to+\infty&0\\
(3/4,1)&X_n\to+\infty&>0
\end{array}
}
\tag{19}
\]
In particular, there are genuine transient zero-speed regimes on both sides of recurrence.

The first-passage means are
\[
\boxed{
\mathbb ET_1<\infty
\iff \theta>\frac34,
\qquad
\mathbb ET_1=\frac{6-4\theta}{4\theta-3},
}
\tag{20}
\]
and
\[
\boxed{
\mathbb ET_{-1}<\infty
\iff \theta<\frac14,
\qquad
\mathbb ET_{-1}=\frac{2+4\theta}{1-4\theta}.
}
\tag{21}
\]
Outside those respective parameter ranges, the corresponding annealed expectation is infinite.

---

## Answer

The three exact transition parameters are
\[
\boxed{
(\theta_-,\theta_{\rm dir},\theta_+)
=\left(\frac14,\frac12,\frac34\right),
}
\]
and the annealed almost-sure velocity is
\[
\boxed{
v(\theta)=
\begin{cases}
\displaystyle \frac{4\theta-1}{2+4\theta},&0<\theta<1/4,\\[2mm]
0,&1/4\le\theta\le3/4,\\[2mm]
\displaystyle \frac{4\theta-3}{6-4\theta},&3/4<\theta<1.
\end{cases}
}
\]
The walk is transient to \(-\infty\) for \(\theta<1/2\), recurrent at \(\theta=1/2\), and transient to \(+\infty\) for \(\theta>1/2\). The transient regimes \([1/4,1/2)\) and \((1/2,3/4]\) have zero speed.

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- one-dimensional random walk in random environment
- logarithmic potential and recurrence/transience
- random crossing-time series
- ballistic versus zero-speed transience
- regeneration/renewal law of large numbers
