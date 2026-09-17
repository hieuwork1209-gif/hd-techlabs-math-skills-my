## Steps

Step 1: Reduce the SDP exactly to an angular cycle problem
For $\tau>0$, write
$$
V(\tau)=\max_{X\succeq0,\ X_{ii}=1}
\left[\frac12\sum_{i=1}^4(1-X_{i,i+1})+\frac\tau2(1-X_{5,1})\right].
$$
Every feasible $X$ is a Gram matrix $X_{ij}=u_i^Tu_j$ of unit vectors. Define
$$
\delta_i=\arccos(-u_i^Tu_{i+1})\quad(1\le i\le4),
\qquad
\delta_5=\arccos(-u_5^Tu_1),
$$
so $0\le\delta_i\le\pi$. Put
$$
v_1=u_1,\quad v_2=-u_2,\quad v_3=u_3,\quad v_4=-u_4,\quad v_5=u_5.
$$
Then the spherical distance from $v_i$ to $v_{i+1}$ is $\delta_i$ for $1\le i\le4$, while
$$
d(v_1,v_5)=\arccos(u_1^Tu_5)=\pi-\delta_5.
$$
The triangle inequality on the unit sphere therefore gives
$$
\delta_1+\delta_2+\delta_3+\delta_4+\delta_5\ge\pi. \tag{1}
$$
The objective is
$$
\frac12\sum_{i=1}^4(1+\cos\delta_i)+\frac\tau2(1+\cos\delta_5). \tag{2}
$$
Because every term decreases as its $\delta_i$ increases, the relaxed angular maximum under (1) occurs with equality in (1). Conversely, every $5$-tuple of nonnegative angles summing to $\pi$ is attainable: place $v_1,\dots,v_5$ consecutively on one great circle with increments $\delta_1,\dots,\delta_4$, then recover the $u_i$ by the alternating signs above. Hence (1)-(2) are an exact reformulation of the SDP.

Fix $b=\delta_5$. The four light-edge angles have total $\pi-b$. For $p,q\ge0$ with $p+q\le\pi$,
$$
\cos p+\cos q
=2\cos\frac{p+q}{2}\cos\frac{p-q}{2}
\le2\cos\frac{p+q}{2}.
$$
Repeated averaging shows that the maximum is attained when
$$
\delta_1=\delta_2=\delta_3=\delta_4=a,
\qquad
\delta_5=\pi-4a,
\qquad 0\le a\le\frac\pi4. \tag{3}
$$
Thus
$$
V(\tau)=\max_{0\le a\le\pi/4}\Phi_\tau(a),
\qquad
\Phi_\tau(a)=2+2\cos a+\frac\tau2(1-\cos4a). \tag{4}
$$
Equality in the spherical triangle inequality and in the averaging step also describes all optimizers. If $a=0$, all $u_i$ are collinear and the Gram matrix has rank $1$. If $a>0$, the equality case lies on one great circle with a nonzero increment, so the optimizer Gram matrix is uniquely determined and has rank $2$.

Step 2: Locate the rank transition
Differentiate (4):
$$
\Phi_\tau'(a)
=-2\sin a+2\tau\sin4a
=2\sin a\bigl(4\tau\cos a\cos2a-1\bigr). \tag{5}
$$
On $(0,\pi/4)$,
$$
g(a):=\cos a\cos2a
$$
is strictly decreasing because
$$
g'(a)=-\sin a\cos2a-2\cos a\sin2a<0,
$$
with $g(0)=1$ and $g(\pi/4)=0$.

If $0<\tau\le1/4$, then $4\tau g(a)<1$ for every $a>0$, so $\Phi_\tau$ is strictly decreasing and its unique maximizer is $a=0$. Hence
$$
V(\tau)=4,\qquad 0<\tau\le\frac14, \tag{6}
$$
and every optimizer has rank $1$.

If $\tau>1/4$, equation
$$
4\tau\cos a\cos2a=1 \tag{7}
$$
has a unique solution $a_\tau\in(0,\pi/4)$. By (5), $\Phi_\tau$ increases before $a_\tau$ and decreases after it, so this is the unique maximizer. Thus the optimizer has rank $2$ for every $\tau>1/4$. Consequently
$$
\tau_c:=\sup\{\tau>0:V(\tau)=4\}=\frac14. \tag{8}
$$

Step 3: Extract the second-order onset at the bifurcation
Let $h>0$ and write
$$
a_h=a_{1/4+h}.
$$
From (7),
$$
\cos a_h\cos2a_h=\frac1{1+4h}. \tag{9}
$$
Hence $a_h\to0$. Since
$$
\cos a\cos2a=1-\frac52a^2+O(a^4),
$$
(9) gives
$$
\frac{a_h^2}{h}\longrightarrow\frac85. \tag{10}
$$
Indeed,
$$
1-\cos a_h\cos2a_h=\frac{4h}{1+4h},
$$
and division by $a_h^2$ followed by $h\downarrow0$ yields (10).

Using (4) and $\tau=1/4+h$,
$$
V\left(\frac14+h\right)-4
=2(\cos a_h-1)+\left(\frac18+\frac h2\right)(1-\cos4a_h).
$$
Taylor expansion at $0$ gives
$$
V\left(\frac14+h\right)-4
=4h\,a_h^2-\frac54a_h^4+O(ha_h^4+a_h^6). \tag{11}
$$
Because $a_h^2=O(h)$ by (10), dividing (11) by $h^2$ gives
$$
\lim_{h\downarrow0}
\frac{V(1/4+h)-V(1/4)}{h^2}
=4\cdot\frac85-\frac54\left(\frac85\right)^2
=\frac{16}{5}. \tag{12}
$$

Step 4: Collect the exact pair
Equations (8) and (12) give the threshold where the SDP leaves the rank-one cut solution and the exact quadratic onset of the optimal value.

Final Answer: $\boxed{(1/4,16/5)}$

---

## Answer

$(1/4,16/5)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- semidefinite Gram representation
- spherical triangle inequality
- odd-cycle angular obstruction
- rank bifurcation
- second-order sensitivity
