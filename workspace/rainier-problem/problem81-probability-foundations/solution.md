## Steps

Step 1: Define the stationary Markov environment and its local odds

Let \((S_x)_{x\in\mathbb Z}\) be a two-sided stationary Markov chain with state space \(\{R,L\}\), stationary law
\[
\pi=(\theta,1-\theta),
\qquad 0<\theta<1,
\]
and transition matrix
\[
P_\theta=
\begin{pmatrix}
\dfrac{1+4\theta}{5} & \dfrac{4(1-\theta)}5\\[2mm]
\dfrac{4\theta}5 & \dfrac{5-4\theta}{5}
\end{pmatrix}.
\tag{1}
\]
The detailed-balance identity
\[
\theta\frac{4(1-\theta)}5
=(1-\theta)\frac{4\theta}5
\]
shows that the chain is reversible.

Set
\[
\omega_x=
\begin{cases}
3/4,&S_x=R,\\
1/4,&S_x=L,
\end{cases}
\]
and define the nearest-neighbor random walk in this environment by
\[
P_\omega(X_{n+1}=x+1\mid X_n=x)=\omega_x.
\]
Put
\[
\rho_x=\frac{1-\omega_x}{\omega_x}
=
\begin{cases}
1/3,&S_x=R,\\
3,&S_x=L.
\end{cases}
\tag{2}
\]
Let
\[
D=\operatorname{diag}(1/3,3),
\qquad
D^{-1}=\operatorname{diag}(3,1/3).
\tag{3}
\]

Step 2: Direction is governed by the logarithmic potential

The potential increments are \(\log\rho_x\). Since the environment chain is stationary and ergodic,
\[
\frac1n\sum_{j=1}^n\log\rho_j
\longrightarrow
\mathbb E_\pi\log\rho_0
\qquad\text{a.s.}
\]
Now
\[
\mathbb E_\pi\log\rho_0
=\theta\log(1/3)+(1-\theta)\log3
=(1-2\theta)\log3.
\tag{4}
\]
The one-dimensional scale-function formula for RWRE expresses hitting probabilities through products of the \(\rho_j\), hence through exponentials of this potential. Therefore

- if \(\theta>1/2\), the potential drifts to \(-\infty\) and the walk is transient to \(+\infty\);
- if \(\theta<1/2\), it is transient to \(-\infty\);
- if \(\theta=1/2\), the centered finite-state Markov additive process oscillates to both signs, so the two scale sums diverge and the walk is recurrent.

Thus
\[
\boxed{\theta_{\rm dir}=\frac12.}
\tag{5}
\]

Step 3: Rightward crossing times become a matrix product series

Assume first \(\theta>1/2\), so the walk is right-transient. The quenched expected time to cross from \(0\) to \(1\) is
\[
E_\omega^0T_1
=1+2\sum_{k=0}^\infty
\rho_0\rho_{-1}\cdots\rho_{-k}.
\tag{6}
\]
This is the same one-dimensional left-excursion expansion as in the i.i.d. case; the difference is that the environment products are now correlated.

Because the stationary chain is reversible, the backward state chain has the same transition matrix \(P_\theta\). Hence
\[
\mathbb E_\theta
\bigl[\rho_0\rho_{-1}\cdots\rho_{-k}\bigr]
=\pi D(P_\theta D)^k\mathbf 1,
\tag{7}
\]
where \(\mathbf 1=(1,1)^T\). Therefore
\[
\mathbb E_\theta T_1
=1+2\sum_{k=0}^\infty
\pi D(P_\theta D)^k\mathbf 1.
\tag{8}
\]
The series converges exactly when
\[
\rho(P_\theta D)<1,
\tag{9}
\]
with \(\rho(\cdot)\) denoting the Perron spectral radius.

A direct computation gives
\[
P_\theta D=
\begin{pmatrix}
\dfrac{1+4\theta}{15} & \dfrac{12(1-\theta)}5\\[2mm]
\dfrac{4\theta}{15} & \dfrac{3(5-4\theta)}5
\end{pmatrix},
\]
\[
\det(P_\theta D)=\frac15,
\qquad
\det(I-P_\theta D)=\frac{4(8\theta-7)}{15}.
\tag{10}
\]
At \(\theta=7/8\) the Perron eigenvalue is exactly \(1\); for larger \(\theta\) the trace decreases while the determinant stays \(1/5\), so the Perron eigenvalue is strictly below \(1\). Thus
\[
\boxed{
\mathbb E_\theta T_1<\infty
\iff \theta>\frac78.
}
\tag{11}
\]
When \(\theta>7/8\), summing the geometric matrix series gives
\[
\begin{aligned}
\mathbb E_\theta T_1
&=1+2\pi D(I-P_\theta D)^{-1}\mathbf 1\\
&=\boxed{\frac{2(7-6\theta)}{8\theta-7}}.
\end{aligned}
\tag{12}
\]

The one-dimensional RWRE law of large numbers identifies the asymptotic speed in the right-transient regime as the reciprocal of the mean crossing time when that mean is finite, and as \(0\) when it is infinite. Hence
\[
\boxed{
v(\theta)=\frac{8\theta-7}{2(7-6\theta)}
\qquad\left(\frac78<\theta<1\right),
}
\tag{13}
\]
and
\[
\boxed{
v(\theta)=0
\qquad\left(\frac12<\theta\le\frac78\right).
}
\tag{14}
\]

Step 4: Leftward crossing times by reflection

For the reflected walk, the relevant local odds are \(\rho_x^{-1}\). The same reversible-Markov calculation gives
\[
\mathbb E_\theta T_{-1}
=1+2\sum_{k=0}^\infty
\pi D^{-1}(P_\theta D^{-1})^k\mathbf 1.
\tag{15}
\]
Now
\[
\det(P_\theta D^{-1})=\frac15,
\qquad
\det(I-P_\theta D^{-1})=\frac{4(1-8\theta)}{15}.
\tag{16}
\]
Thus the Perron radius is below \(1\) exactly when
\[
\boxed{\theta<\frac18.}
\tag{17}
\]
In that range,
\[
\begin{aligned}
\mathbb E_\theta T_{-1}
&=1+2\pi D^{-1}(I-P_\theta D^{-1})^{-1}\mathbf 1\\
&=\boxed{\frac{2(1+6\theta)}{1-8\theta}}.
\end{aligned}
\tag{18}
\]
Therefore
\[
\boxed{
v(\theta)
=-\frac1{\mathbb E_\theta T_{-1}}
=\frac{8\theta-1}{2(1+6\theta)}
\qquad\left(0<\theta<\frac18\right).
}
\tag{19}
\]
For
\[
\frac18\le\theta<\frac12,
\]
the walk is still transient to \(-\infty\), but its speed is zero.

Step 5: Complete phase diagram

Combining the directional criterion with the two transfer-matrix moment criteria,
\[
\boxed{
(\theta_-,\theta_{\rm dir},\theta_+)
=\left(\frac18,\frac12,\frac78\right).
}
\tag{20}
\]
The limiting velocity exists almost surely under the annealed law and is
\[
\boxed{
v(\theta)=
\begin{cases}
\displaystyle \frac{8\theta-1}{2(1+6\theta)},
&0<\theta<\frac18,\\[3mm]
0,
&\frac18\le\theta\le\frac78,\\[3mm]
\displaystyle \frac{8\theta-7}{2(7-6\theta)},
&\frac78<\theta<1.
\end{cases}
}
\tag{21}
\]
The directional behavior is
\[
\boxed{
\begin{array}{c|c|c}
\theta&\text{direction}&v(\theta)\\ \hline
(0,1/8)&X_n\to-\infty&<0\\
[1/8,1/2)&X_n\to-\infty&0\\
\{1/2\}&\text{recurrent}&0\\
(1/2,7/8]&X_n\to+\infty&0\\
(7/8,1)&X_n\to+\infty&>0.
\end{array}
}
\tag{22}
\]
Hence the transient zero-speed set is exactly
\[
\boxed{
\left[\frac18,\frac12\right)
\cup
\left(\frac12,\frac78\right].
}
\tag{23}
\]
The threshold points \(1/8\) and \(7/8\) are included because at those values the corresponding Perron eigenvalue equals \(1\), so the matrix series diverges.

Finally,
\[
\boxed{
\mathbb E_\theta T_1<\infty
\iff \theta>\frac78,
\qquad
\mathbb E_\theta T_1
=\frac{2(7-6\theta)}{8\theta-7},
}
\tag{24}
\]
and
\[
\boxed{
\mathbb E_\theta T_{-1}<\infty
\iff \theta<\frac18,
\qquad
\mathbb E_\theta T_{-1}
=\frac{2(1+6\theta)}{1-8\theta}.
}
\tag{25}
\]
Outside those respective ranges, the corresponding annealed first-passage expectation is infinite.

---

## Answer

\[
\boxed{
(\theta_-,\theta_{\rm dir},\theta_+)
=\left(\frac18,\frac12,\frac78\right),
}
\]
and
\[
\boxed{
v(\theta)=
\begin{cases}
\displaystyle \frac{8\theta-1}{2(1+6\theta)},&0<\theta<1/8,\\[2mm]
0,&1/8\le\theta\le7/8,\\[2mm]
\displaystyle \frac{8\theta-7}{2(7-6\theta)},&7/8<\theta<1.
\end{cases}
}
\]
The walk is transient to \(-\infty\) for \(\theta<1/2\), recurrent for \(\theta=1/2\), and transient to \(+\infty\) for \(\theta>1/2\). The transient zero-speed regime is
\[
\left[\frac18,\frac12\right)\cup\left(\frac12,\frac78\right].
\]

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- one-dimensional random walk in stationary Markov random environment
- logarithmic potential criterion
- reversible two-state environment chain
- matrix transfer products for crossing times
- Perron-Frobenius ballisticity threshold
- zero-speed transience and annealed law of large numbers
