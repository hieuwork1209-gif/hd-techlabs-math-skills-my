## Steps

Step 1: Derive the total-progeny generating-function system
Let $T$ be the total number of individuals ever born, including the initial ancestor, and define
$$
G_A(z)=\mathbb E_A[z^T],
\qquad
G_B(z)=\mathbb E_B[z^T],
\qquad
0\leq z<1.
$$
The offspring generating functions are
$$
F_A(s,t)
=
\frac{1}{2}
+
\frac{3}{8}s^2
+
\frac{1}{8}t^2
$$
and
$$
F_B(s,t)
=
\frac{1}{2}
+
\frac{1}{4}s
+
\frac{1}{4}t^3.
$$
Conditioning on the first generation gives
$$
G_A(z)=zF_A(G_A(z),G_B(z)),
\qquad
G_B(z)=zF_B(G_A(z),G_B(z)).
$$

Because every individual has finitely many children, extinction is equivalent to $T<\infty$. The extinction-probability vector is the increasing limit of the probabilities of extinction by generation $n$, so it is a fixed point of $(F_A,F_B)$. To identify that fixed point directly, suppose $(u,v)\in[0,1]^2$ satisfies $(F_A(u,v),F_B(u,v))=(u,v)$ and put
$$
p=1-u,
\qquad
q=1-v.
$$
The fixed-point equations become
$$
2(p-q)+3p^2+q^2=0
$$
and
$$
q-p+3q^2-q^3=0.
$$
The first equation gives $p\leq q$, while the second gives
$$
p=q+3q^2-q^3\geq q.
$$
Thus $p=q$, and then the first equation forces $p=q=0$. Hence $(1,1)$ is the only fixed point in $[0,1]^2$, so
$$
G_A(z)\to1,
\qquad
G_B(z)\to1
$$
as $z\uparrow1$.

Step 2: Identify the critical and stable scales near the singular point
Write
$$
z=1-t^2,
\qquad
p=1-G_A(z),
\qquad
q=1-G_B(z),
$$
where $t\downarrow0$, and set
$$
x=\frac{p+q}{2},
\qquad
y=\frac{p-q}{2}.
$$
Adding the two fixed-point equations gives the exact identity
$$
t^2(1-x)
=
(1-t^2)
\left(
\frac{3}{16}p^2
+
\frac{7}{16}q^2
-
\frac{1}{8}q^3
\right).
$$
Since $0\leq p,q\leq1$, the bracket is bounded below by
$$
\frac{3}{16}p^2+\frac{5}{16}q^2
\geq
\frac{3}{8}x^2
$$
and above by a constant multiple of $x^2$. Therefore
$$
x=\Theta(t).
$$

Subtracting the two fixed-point equations gives
$$
(1+t^2)y
=
(1-t^2)
\left(
-\frac{3}{8}p^2
+
\frac{5}{8}q^2
-
\frac{1}{4}q^3
\right).
$$
Hence
$$
y=O(x^2)=O(t^2).
$$
This determines the natural rescaling
$$
x=tX,
\qquad
y=t^2Y.
$$

After substituting $p=tX+t^2Y$ and $q=tX-t^2Y$ into the two fixed-point equations, take their average and difference and divide by $t^2$. Because the original residuals are polynomials and every term has a factor $t^2$ under this scaling, the quotients extend to exact polynomial functions $H_1(X,Y,t)$ and $H_2(X,Y,t)$. Their Taylor expansions are
$$
0
=
1-\frac{5}{8}X^2
+
\frac{tX}{8}(X^2+4Y-8)
+
O(t^2)
$$
and
$$
0
=
\frac{X^2-4Y}{8}
-
\frac{tX}{8}(X^2+8Y)
+
O(t^2).
$$
At $t=0$, the positive solution is
$$
X_0=\frac{2\sqrt{10}}{5},
\qquad
Y_0=\frac{2}{5}.
$$

Step 3: Justify and compute the first correction by the implicit function theorem
Let $H_1(X,Y,t)$ and $H_2(X,Y,t)$ denote the two analytic left-hand sides from Step 2. At $(X_0,Y_0,0)$,
$$
\frac{\partial(H_1,H_2)}{\partial(X,Y)}
=
\begin{pmatrix}
-\frac{5X_0}{4}&0\\
\frac{X_0}{4}&-\frac{1}{2}
\end{pmatrix},
$$
whose determinant is
$$
\frac{5X_0}{8}
=
\frac{\sqrt{10}}{4}
\neq0.
$$
Thus the implicit function theorem gives unique analytic functions $X(t),Y(t)$ near $t=0$ corresponding to the physical branch.

Write
$$
X(t)=X_0+X_1t+O(t^2),
\qquad
Y(t)=Y_0+Y_1t+O(t^2).
$$
The coefficient of $t$ in the first equation from Step 2 gives
$$
-\frac{5X_0}{4}X_1
+
\frac{X_0}{8}(X_0^2+4Y_0-8)
=
0.
$$
Since
$$
X_0^2=\frac{8}{5},
\qquad
Y_0=\frac{2}{5},
$$
this becomes
$$
-\frac{5X_0}{4}X_1
-
\frac{3X_0}{5}
=
0,
$$
so
$$
X_1=-\frac{12}{25}.
$$

The coefficient of $t$ in the second equation gives
$$
\frac{X_0}{4}X_1
-
\frac{1}{2}Y_1
-
\frac{X_0}{8}(X_0^2+8Y_0)
=
0.
$$
Substituting $X_1=-\frac{12}{25}$, $X_0^2=\frac{8}{5}$, and $Y_0=\frac{2}{5}$ yields
$$
Y_1=-\frac{72\sqrt{10}}{125}.
$$

Step 4: Read off the two singular expansions
Because
$$
p=x+y=tX(t)+t^2Y(t),
$$
we have
$$
1-G_A(z)
=
\frac{2\sqrt{10}}{5}\sqrt{1-z}
+
O(1-z).
$$
Thus
$$
\kappa=\frac{2\sqrt{10}}{5}.
$$

Also
$$
G_A(z)-G_B(z)
=
q-p
=
-2y
=
-2t^2Y(t).
$$
Using the expansion of $Y(t)$,
$$
G_A(z)-G_B(z)
=
-\frac{4}{5}(1-z)
+
\frac{144\sqrt{10}}{125}(1-z)^{\frac{3}{2}}
+
O((1-z)^2).
$$
Therefore
$$
\alpha=\frac{4}{5},
\qquad
\beta=\frac{144\sqrt{10}}{125}.
$$

Step 5: Assemble the requested coefficient triple
The leading square-root singularity of $G_A$ has coefficient $\frac{2\sqrt{10}}{5}$, while the type-asymmetry expansion has coefficients $\frac{4}{5}$ and $\frac{144\sqrt{10}}{125}$ in the normalization stated in the problem.
Final Answer: $\boxed{\left(\frac{2\sqrt{10}}{5},\frac{4}{5},\frac{144\sqrt{10}}{125}\right)}$

---

## Answer

$\left(\frac{2\sqrt{10}}{5},\frac{4}{5},\frac{144\sqrt{10}}{125}\right)$

---

## Classification

**Problem Type:** Parameter identification

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- multitype branching processes
- total progeny generating functions
- critical singularity scaling
- implicit function theorem
- stable mode asymptotics
