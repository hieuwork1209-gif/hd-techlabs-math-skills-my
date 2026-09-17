## Steps

Step 1: Locate the common entry threshold
Let
$$
f_1=e_1,\qquad f_2=e_2,\qquad f_3=e_3,
$$
$$
f_4(\tau)=\begin{pmatrix}\tau\\1/3\\1/3\end{pmatrix},
\qquad
f_5(\tau)=\begin{pmatrix}1/3\\\tau\\1/3\end{pmatrix},
$$
and let
$$
M_\tau(w)=\sum_{i=1}^5w_if_if_i^T,
\qquad w_i\ge0,
\qquad \sum_{i=1}^5w_i=1.
$$
Put
$$
S(\tau)=\tau^2+\frac29.
$$
Then
$$
\operatorname{tr}M_\tau(w)
=1+(S(\tau)-1)(w_4+w_5). \tag{1}
$$
For a positive-semidefinite $3\times3$ matrix with eigenvalues $\lambda_1,\lambda_2,\lambda_3$,
$$
\det M=\lambda_1\lambda_2\lambda_3
\le\left(\frac{\lambda_1+\lambda_2+\lambda_3}{3}\right)^3.
$$
Hence if $S(\tau)\le1$,
$$
\det M_\tau(w)\le\frac1{27}. \tag{2}
$$
The design
$$
w^0=\left(\frac13,\frac13,\frac13,0,0\right)
$$
attains equality. If $S(\tau)<1$, equality in (1)-(2) forces $w_4=w_5=0$ and then $w_1=w_2=w_3=1/3$. If $S(\tau)=1$, equality in (2) forces $M_\tau(w)=I/3$. But every off-diagonal entry contributed by $w_4f_4f_4^T+w_5f_5f_5^T$ is nonnegative, and its $(1,2)$ entry is
$$
\frac{\tau}{3}(w_4+w_5).
$$
Thus $w_4=w_5=0$ again. Therefore $w^0$ is the unique optimizer whenever $S(\tau)\le1$.

The equality $S(\tau)=1$ gives
$$
\tau_c=\frac{\sqrt7}{3}. \tag{3}
$$
For $\tau>\tau_c$, both fourth and fifth design points have squared norm greater than $1$, so at $w^0$ the directional derivative of $\log\det M$ toward either new point is
$$
3\bigl(S(\tau)-1\bigr)>0.
$$
Hence the optimum exceeds $-3\log3$ for every $\tau>\tau_c$. Thus (3) is exactly the threshold in the problem.

Step 2: Set up the two-dimensional support bifurcation
Let
$$
r=\tau_c=\frac{\sqrt7}{3},
\qquad
\delta=\tau^2-r^2,
$$
and write near $w^0$
$$
w_4=t,\qquad w_5=u,
$$
$$
w_i=\frac13+y_i\quad(1\le i\le3),
\qquad
y_1+y_2+y_3=-(t+u).
$$
At the threshold, the squared-coordinate vectors of $f_4,f_5$ are
$$
a=\left(\frac79,\frac19,\frac19\right),
\qquad
b=\left(\frac19,\frac79,\frac19\right),
$$
and both have coordinate sum $1$. Define
$$
z=y+ta+ub.
$$
Then $z_1+z_2+z_3=0$.

Put
$$
H=M_\tau(w)-\frac13I.
$$
Since $t,u,\|y\|=O(\delta)$ at an optimizer, the Taylor formula
$$
\log\det\left(\frac13I+H\right)
=-3\log3+3\operatorname{tr}H-\frac92\operatorname{tr}(H^2)+O(\|H\|^3) \tag{4}
$$
is uniform in the relevant neighborhood. Moreover
$$
\operatorname{tr}H=\delta(t+u). \tag{5}
$$
At quadratic order the diagonal of $H$ is $z$, while its off-diagonal entries are those of
$$
t f_4(r)f_4(r)^T+u f_5(r)f_5(r)^T.
$$
For fixed $t,u$, the term $\operatorname{tr}(H^2)$ is minimized uniquely at $z=0$. This choice is compatible with the simplex constraint because $\sum z_i=0$.

Step 3: Compute the interaction quadratic form
For $z=0$, the three off-diagonal coordinates contributed by the fourth point are
$$
p=\left(\frac{\sqrt7}{9},\frac{\sqrt7}{9},\frac19\right),
$$
and those contributed by the fifth point are
$$
q=\left(\frac{\sqrt7}{9},\frac19,\frac{\sqrt7}{9}\right).
$$
Therefore
$$
\operatorname{tr}(H^2)
=2\|tp+uq\|^2+o((t+u)^2)
=A(t^2+u^2)+2Ctu+o((t+u)^2), \tag{6}
$$
where
$$
A=2\|p\|^2=\frac{10}{27},
$$
$$
C=2p^Tq=\frac{14+4\sqrt7}{81}. \tag{7}
$$
Since $A>C>0$, the quadratic form is positive definite.

Combining (4)-(7),
$$
\Psi(\tau)+3\log3
=\max_{t,u\ge0}
\left[
3\delta(t+u)-\frac92\bigl(A(t^2+u^2)+2Ctu\bigr)
\right]
+o(\delta^2). \tag{8}
$$
The bracket is strictly concave. Its unique unconstrained maximizer satisfies
$$
3\delta=9(At+Cu),
\qquad
3\delta=9(Ct+Au).
$$
Because $A\ne C$, subtraction gives $t=u$, and hence
$$
t=u=\frac{\delta}{3(A+C)}>0. \tag{9}
$$
Thus for $\tau>\tau_c$ sufficiently close to $\tau_c$, both new design points enter the support. The first three weights remain positive by continuity, so the optimizer has full support.

Uniqueness follows from strict concavity of $\log\det$ in the information matrix together with injectivity of the weight-to-matrix map near $\tau_c$: the off-diagonal entries determine $w_4,w_5$ because $\tau_c\ne1/3$, and then the diagonal entries determine $w_1,w_2,w_3$.

Step 4: Extract the exact second-order optimal-value sensitivity
At the maximizer (9), the quadratic maximum in (8) is
$$
\frac{\delta^2}{A+C}. \tag{10}
$$
From (7),
$$
A+C
=\frac{4(11+\sqrt7)}{81}. \tag{11}
$$
If $\tau=\tau_c+h$, then
$$
\delta=2\tau_ch+h^2,
$$
so
$$
\frac{\delta^2}{h^2}\longrightarrow4\tau_c^2=\frac{28}{9}. \tag{12}
$$
Using (10)-(12),
$$
\lim_{h\downarrow0}
\frac{\Psi(\tau_c+h)-\Psi(\tau_c)}{h^2}
=\frac{28/9}{4(11+\sqrt7)/81}
=\frac{63}{11+\sqrt7}
=\frac{21(11-\sqrt7)}{38}. \tag{13}
$$

Final Answer: $\boxed{(\sqrt7/3,21(11-\sqrt7)/38)}$

---

## Answer

$(\sqrt7/3,21(11-\sqrt7)/38)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- D-optimal experimental design
- simultaneous support bifurcation
- information-matrix log determinant
- interacting entry directions
- second-order optimal-value sensitivity
