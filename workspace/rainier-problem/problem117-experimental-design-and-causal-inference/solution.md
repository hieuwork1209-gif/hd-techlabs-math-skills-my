## Steps

Step 1: Determine exactly when the fourth design point becomes useful
Let
$$
f_1=e_1,
\qquad f_2=e_2,
\qquad f_3=e_3,
\qquad
f_4(\tau)=\begin{pmatrix}\tau\\1/2\\1/3\end{pmatrix},
$$
and for $w=(w_1,w_2,w_3,w_4)$ in the simplex $\Delta_4$ put
$$
M_\tau(w)=\sum_{i=1}^4w_if_if_i^T,
\qquad
D_\tau(w)=\det M_\tau(w).
$$
Write
$$
A=\tau^2,
\qquad B=\frac14,
\qquad C=\frac19,
\qquad S=A+B+C.
$$
Expanding the determinant gives
$$
D_\tau(w)
=w_1w_2w_3
+w_4\left(Aw_2w_3+Bw_1w_3+Cw_1w_2\right). \tag{1}
$$
Also
$$
\operatorname{tr}M_\tau(w)
=w_1+w_2+w_3+Sw_4
=1-(1-S)w_4. \tag{2}
$$
If $S\le1$, the eigenvalues of the positive-semidefinite $3\times3$ matrix $M_\tau(w)$ have product at most the cube of their average, so
$$
D_\tau(w)
\le\left(\frac{\operatorname{tr}M_\tau(w)}3\right)^3
\le\frac1{27}. \tag{3}
$$
The design
$$
w^0=\left(\frac13,\frac13,\frac13,0\right)
$$
attains $D_\tau(w^0)=1/27$. If $S<1$, equality in (2)-(3) forces $w_4=0$ and then $w_1=w_2=w_3=1/3$. If $S=1$, equality in (3) forces $M_\tau(w)=I/3$; since all three coordinates of $f_4(\tau)$ are nonzero, every off-diagonal entry contributed by $w_4f_4f_4^T$ vanishes only when $w_4=0$. Thus $w^0$ is still the unique optimizer.

Now $S=1$ exactly when
$$
\tau^2+\frac14+\frac19=1,
$$
so
$$
\tau_0=\frac{\sqrt{23}}6. \tag{4}
$$
If $\tau>\tau_0$, then $S>1$. At $w^0$, the directional derivative of (1) obtained by introducing a small amount of $w_4$ and removing the same total mass from the first three coordinates is
$$
\frac{S-1}{9}>0.
$$
Hence $\max D_\tau>1/27$ for every $\tau>\tau_0$. Therefore
$$
\tau_c=\tau_0=\frac{\sqrt{23}}6. \tag{5}
$$
Since maximizing $\log\det M$ is equivalent to maximizing $D_\tau$, this also identifies the threshold for the stated objective.

Step 2: Control the optimizer near the support transition
At $\tau=\tau_c$, Step 1 gives the unique optimizer $w^0$. By compactness of the simplex, every sequence of optimizers with $\tau\to\tau_c$ converges to $w^0$: otherwise a convergent subsequence would give a different optimizer at $\tau_c$ by continuity of (1).

Hence for $\tau>\tau_c$ sufficiently close to $\tau_c$, the first three weights remain positive. The fourth weight is also positive, because the face $w_4=0$ has maximum determinant exactly $1/27$, while Step 1 shows the true optimum is larger. Thus the optimizer has full support immediately to the right of the threshold.

It is unique there. Indeed, $\log\det$ is strictly concave as a function of the positive-definite information matrix, and the affine map $w\mapsto M_\tau(w)$ is injective: the off-diagonal entries determine $w_4$ because every product of two coordinates of $f_4(\tau)$ is nonzero, and then the diagonal entries determine $w_1,w_2,w_3$.

Step 3: Derive the quadratic onset of the optimal determinant
Put
$$
\tau=\tau_c+h,
\qquad
\delta=\tau^2-\tau_c^2=2\tau_ch+h^2,
$$
and write the optimizer locally as
$$
w_4=t,
\qquad
w_i=\frac13+y_i\quad(1\le i\le3),
\qquad
y_1+y_2+y_3=-t.
$$
At the threshold define
$$
a_0=\left(\frac{23}{36},\frac14,\frac19\right),
\qquad
R_0=\|a_0\|^2
=\frac{313}{648}. \tag{6}
$$
Set
$$
z=y+t a_0.
$$
Because the coordinates of $a_0$ sum to $1$, we have $z_1+z_2+z_3=0$.

Expanding the exact polynomial (1) at $(\tau_c,w^0)$ gives
$$
D_{\tau_c+h}(w)-\frac1{27}
=rac{\delta t}{9}
-\frac{\|z\|^2}{6}
-\frac{1-R_0}{6}t^2
+O\!\left((|h|+t+\|z\|)^3\right). \tag{7}
$$
For completeness, the quadratic part follows from
$$
\frac13\sum_{i<j}y_iy_j
+\frac t3\left[a_{0,1}(y_2+y_3)+a_{0,2}(y_1+y_3)+a_{0,3}(y_1+y_2)\right]
$$
$$
=-\frac{\|z\|^2}{6}-\frac{1-R_0}{6}t^2,
$$
using $\sum y_i=-t$ and $\sum a_{0,i}=1$.

Since the optimizer has value at least $1/27$, (7) first implies
$$
t+\|z\|=O(h). \tag{8}
$$
Write $t=hT$ and $z=hZ$. Because
$$
\frac\delta h\longrightarrow2\tau_c=\frac{\sqrt{23}}3,
$$
dividing (7) by $h^2$ shows that the limiting optimization problem is
$$
\max_{T\ge0,\ Z_1+Z_2+Z_3=0}
\left[
\frac{\sqrt{23}}{27}T
-\frac{\|Z\|^2}{6}
-\frac{1-R_0}{6}T^2
\right]. \tag{9}
$$
Its unique maximizer has $Z=0$ and
$$
T
=\frac{3(\sqrt{23}/27)}{1-R_0}
=\frac{72\sqrt{23}}{335}. \tag{10}
$$
Thus, in particular,
$$
\frac{w_4(\tau_c+h)}h\longrightarrow\frac{72\sqrt{23}}{335},
$$
which confirms the full-support bifurcation quantitatively.

The maximum value in (9) is
$$
\frac{3}{2(1-R_0)}\left(\frac{\sqrt{23}}{27}\right)^2
=\frac{92}{1005}. \tag{11}
$$
Therefore
$$
\max_w D_{\tau_c+h}(w)
=\frac1{27}+\frac{92}{1005}h^2+o(h^2). \tag{12}
$$

Step 4: Pass from determinant to the D-optimal log criterion
Let
$$
\Psi(\tau)=\max_{w\in\Delta_4}\log\det M_\tau(w).
$$
At the threshold,
$$
\Psi(\tau_c)=\log\frac1{27}=-3\log3.
$$
Using (12) and $\log(1+u)=u+o(u)$,
$$
\Psi(\tau_c+h)-\Psi(\tau_c)
=27\cdot\frac{92}{1005}h^2+o(h^2)
=\frac{828}{335}h^2+o(h^2).
$$
Hence
$$
\lim_{h\downarrow0}
\frac{\Psi(\tau_c+h)-\Psi(\tau_c)}{h^2}
=\frac{828}{335}. \tag{13}
$$

Final Answer: $\boxed{(\sqrt{23}/6,828/335)}$

---

## Answer

$(\sqrt{23}/6,828/335)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- D-optimal experimental design
- information-matrix determinant
- support bifurcation
- local simplex expansion
- second-order optimal-value sensitivity
