## Steps

Step 1: Convert the SDP to an exact weighted angular problem
Let the four light-edge weights be
$$
w_1=w_2=1,\qquad w_3=w_4=2.
$$
Every feasible $X$ is a Gram matrix $X_{ij}=u_i^Tu_j$ of unit vectors. Put
$$
v_1=u_1,\quad v_2=-u_2,\quad v_3=u_3,\quad v_4=-u_4,\quad v_5=u_5,
$$
and define
$$
\alpha_i=d(v_i,v_{i+1})\quad(1\le i\le4),
\qquad
\phi=d(v_5,v_1).
$$
Then
$$
X_{i,i+1}=-\cos\alpha_i\quad(1\le i\le4),
\qquad
X_{5,1}=\cos\phi.
$$
The spherical triangle inequality gives
$$
\phi\le A:=\alpha_1+\alpha_2+\alpha_3+\alpha_4. \tag{1}
$$
Near the rank-one cut, $A<\pi$. Since $1-\cos\phi$ increases with $\phi$ on $[0,\pi]$, every local maximizer must have equality in (1). Conversely, equality is attainable by placing the $v_i$ successively on one great circle with increments $\alpha_i$. Therefore, once the optimizer is known to lie near the cut,
$$
V(\tau)-6=
\max_{\substack{\alpha_i\ge0\\A<\pi}}
\left[
-\frac12\sum_{i=1}^4w_i(1-\cos\alpha_i)
+\frac\tau2(1-\cos A)
\right]. \tag{2}
$$
Any nonzero optimizer of (2) is realized on one great circle, so its Gram matrix has rank $2$.

Step 2: Find the exact threshold and the rank-one side
For arbitrary unit vectors, the chord triangle inequality and weighted Cauchy-Schwarz give
$$
\|v_5-v_1\|
\le\sum_{i=1}^4\|v_{i+1}-v_i\|,
$$
$$
\left(\sum_{i=1}^4\|v_{i+1}-v_i\|\right)^2
\le
\left(\sum_{i=1}^4\frac1{w_i}\right)
\left(\sum_{i=1}^4w_i\|v_{i+1}-v_i\|^2\right).
$$
Here
$$
S_1:=\sum_{i=1}^4\frac1{w_i}=3.
$$
Since $\|p-q\|^2=2(1-p^Tq)$ for unit vectors,
$$
1-\cos\phi\le3\sum_{i=1}^4w_i(1-\cos\alpha_i). \tag{3}
$$
Hence
$$
V(\tau)-6
\le
\frac{3\tau-1}{2}
\sum_{i=1}^4w_i(1-\cos\alpha_i). \tag{4}
$$
Thus $V(\tau)=6$ for $0<\tau\le1/3$, attained by the alternating collinear vectors
$$
u_1=u_3=u_5=v,\qquad u_2=u_4=-v.
$$
At $\tau=1/3$, equality in (4) requires equality in both the chord triangle inequality and weighted Cauchy-Schwarz. The four chord increments must therefore be nonnegative parallel multiples of one vector. Since all five $v_i$ lie on the unit sphere, a line meets that sphere in at most two points; monotone parallel increments cannot visit five unit points unless every increment vanishes. Hence the Gram matrix is rank $1$ and is unique up to the common choice of $v$.

For $\tau=1/3+h$ with $h>0$, choose small angles proportional to $1/w_i$ and place them on a great circle. The quadratic term in (2) is then positive, so $V(1/3+h)>6$. Therefore
$$
\tau_c=\frac13. \tag{5}
$$
By compactness and uniqueness of the rank-one Gram matrix at $\tau_c$, every optimizer converges to that Gram matrix as $\tau\downarrow\tau_c$. Thus (2) applies to all optimizers for $\tau>\tau_c$ sufficiently close to $\tau_c$, and every such optimizer has rank $2$.

Step 3: Compute the weighted quartic onset
For a fixed small total angle $A$, define
$$
L(A)=\min_{\substack{\alpha_i\ge0\\\sum\alpha_i=A}}
\sum_{i=1}^4w_i(1-\cos\alpha_i). \tag{6}
$$
The minimizer is interior for small $A$. Its Lagrange equations are
$$
w_i\sin\alpha_i=\lambda.
$$
Hence $\alpha_i=A/(S_1w_i)+O(A^3)$. Let
$$
S_3:=\sum_{i=1}^4\frac1{w_i^3}
=1+1+\frac18+\frac18
=\frac94.
$$
Using $1-\cos z=z^2/2-z^4/24+O(z^6)$, and noting that the $O(A^3)$ corrections do not change the quartic term because the quadratic minimizer is stationary under the constraint, we obtain
$$
L(A)=\frac{A^2}{2S_1}-\frac{S_3}{24S_1^4}A^4+O(A^6)
=\frac{A^2}{6}-\frac{A^4}{864}+O(A^6). \tag{7}
$$
Now put $\tau=1/3+h$. From (2), after optimizing the light-edge split for fixed $A$,
$$
V\left(\frac13+h\right)-6
=
\max_{A\ge0}
\left[
-\frac12L(A)+\left(\frac16+\frac h2\right)(1-\cos A)
\right]. \tag{8}
$$
Substituting (7) gives
$$
V\left(\frac13+h\right)-6
=
\max_{A\ge0}
\left[
\frac h4A^2-\frac{11}{1728}A^4
+O(hA^4+A^6)
\right]. \tag{9}
$$
The maximizing angle satisfies $A^2=O(h)$; more precisely the leading quadratic-quartic balance gives
$$
\frac{A^2}{h}\longrightarrow\frac{216}{11}. \tag{10}
$$
Using (10) in (9),
$$
\lim_{h\downarrow0}
\frac{V(1/3+h)-V(1/3)}{h^2}
=
\frac{27}{11}. \tag{11}
$$

Step 4: Collect the transition data
The weighted SDP stays at the rank-one cut value $6$ through $\tau=1/3$. Immediately to the right, every optimizer is rank $2$, and the excess optimal value turns on quadratically with coefficient $27/11$.

Final Answer: $\boxed{(1/3,27/11)}$

---

## Answer

$(1/3,27/11)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- weighted semidefinite Gram geometry
- weighted chord inequality
- odd-cycle angular obstruction
- rank bifurcation
- quartic sensitivity analysis
