## Steps

Step 1: Reduce the extremal atom problem to a sharp quartic norm minimization
Let $q$ be any real polynomial of degree at most $4$ with $q(0)=1$. Since $q(X)^2=1$ on the event $\{X=0\}$ and $q(X)^2\geq0$ everywhere,
$$
\mathbb P(X=0)\leq \mathbb E[q(X)^2].
$$
The moment conditions through degree $8$ imply
$$
\mathbb E[q(X)^2]=\frac12\int_{-1}^1q(t)^2\,dt.
$$
Write $q=e+o$, where $e$ and $o$ are the even and odd parts. Then $e(0)=1$, and symmetry of the integral gives
$$
\frac12\int_{-1}^1q(t)^2\,dt
=\frac12\int_{-1}^1e(t)^2\,dt+\frac12\int_{-1}^1o(t)^2\,dt.
$$
Hence the unique minimizer has no odd part and may be written
$$
q(t)=bt^4+at^2+1.
$$
Its squared norm is
$$
F(a,b)=1+\frac{2a}{3}+\frac{a^2+2b}{5}+\frac{2ab}{7}+\frac{b^2}{9}.
$$
The quadratic part of $F$ is positive definite because it is the integral of $(at^2+bt^4)^2$ and vanishes only when $a=b=0$. Thus the critical point is the unique global minimizer. The equations
$$
\frac13+\frac a5+\frac b7=0,
\qquad
\frac15+\frac a7+\frac b9=0
$$
give
$$
a=-\frac{14}{3},\qquad b=\frac{21}{5}.
$$
Therefore
$$
q_*(t)=\frac{21}{5}t^4-\frac{14}{3}t^2+1
=\frac{63t^4-70t^2+15}{15},
$$
and substitution into $F$ gives
$$
\frac12\int_{-1}^1q_*(t)^2\,dt=\frac{64}{225}.
$$
Consequently
$$
\mathbb P(X=0)\leq\frac{64}{225}.
$$

Step 2: Determine the support forced by equality
Let
$$
\nu_-=\frac{35-2\sqrt{70}}{63},
\qquad
\nu_+=\frac{35+2\sqrt{70}}{63},
\qquad
\alpha=\sqrt{\nu_-},
\qquad
\beta=\sqrt{\nu_+}.
$$
The inequalities $0<\nu_-<\nu_+<1$ follow from $2\sqrt{70}<35$ and $2\sqrt{70}<28$. Since
$$
63t^4-70t^2+15=63(t^2-\nu_-)(t^2-\nu_+),
$$
the zeros of $q_*$ in $[-1,1]$ are exactly $\pm\alpha$ and $\pm\beta$.

Moreover,
$$
\mathbb E[q_*(X)^2]-\mathbb P(X=0)
=\mathbb E\left[q_*(X)^2\mathbf 1_{\{X\ne0\}}\right].
$$
Thus equality in the upper bound holds if and only if $q_*(X)=0$ almost surely whenever $X\ne0$. Every maximizing law is therefore supported on
$$
\{0,\pm\alpha,\pm\beta\}.
$$

Step 3: Reconstruct the only possible equality distribution
Write
$$
p_+=\mathbb P(X=\alpha),\quad p_-=\mathbb P(X=-\alpha),
\quad r_+=\mathbb P(X=\beta),\quad r_-=\mathbb P(X=-\beta).
$$
The first and third moment conditions give
$$
\alpha(p_+-p_-)+\beta(r_+-r_-)=0,
$$
$$
\alpha^3(p_+-p_-)+\beta^3(r_+-r_-)=0.
$$
The determinant $\alpha\beta(\beta^2-\alpha^2)$ is nonzero, so
$$
p_+=p_-,\qquad r_+=r_-.
$$
Set
$$
w_\alpha=p_++p_-,\qquad w_\beta=r_++r_-.
$$
At equality the mass at $0$ is $64/225$, hence
$$
w_\alpha+w_\beta=\frac{161}{225}.
$$
The second and fourth moments require
$$
\nu_-w_\alpha+\nu_+w_\beta=\frac13,
\qquad
\nu_-^2w_\alpha+\nu_+^2w_\beta=\frac15.
$$
Since $\nu_-\nu_+(\nu_+-\nu_-)\ne0$, this system has a unique solution. Substituting the displayed values of $\nu_\pm$ gives
$$
w_\alpha=\frac{322+13\sqrt{70}}{900},
\qquad
w_\beta=\frac{322-13\sqrt{70}}{900}.
$$
Hence the only possible maximizing law is
$$
\mathbb P(X=0)=\frac{64}{225},
$$
$$
\mathbb P(X=\alpha)=\mathbb P(X=-\alpha)
=\frac{322+13\sqrt{70}}{1800},
$$
$$
\mathbb P(X=\beta)=\mathbb P(X=-\beta)
=\frac{322-13\sqrt{70}}{1800}.
$$
All five masses are positive and sum to $1$.

Step 4: Verify the remaining moments and finish the equality classification
The numbers $\nu_-$ and $\nu_+$ are the roots of
$$
\nu^2-\frac{10}{9}\nu+\frac{5}{21}=0.
$$
For
$$
M_j=w_\alpha\nu_-^j+w_\beta\nu_+^j,
$$
this identity gives the recurrence
$$
M_{j+2}=\frac{10}{9}M_{j+1}-\frac{5}{21}M_j.
$$
The construction in Step 3 gives $M_1=1/3$ and $M_2=1/5$, so
$$
M_3=\frac{10}{9}\cdot\frac15-\frac{5}{21}\cdot\frac13=\frac17,
$$
$$
M_4=\frac{10}{9}\cdot\frac17-\frac{5}{21}\cdot\frac15=\frac19.
$$
Thus the sixth and eighth moments are also the required uniform moments. Symmetry gives all odd moments through degree $7$ equal to $0$, and the masses sum to $1$, so this law satisfies every stated moment condition. It attains mass $64/225$ at $0$.

Conversely, Step 2 forces every equality case onto the same five support points, and Step 3 then forces all five masses uniquely. Therefore the displayed distribution is the unique maximizer.

Final Answer: $\boxed{\frac{64}{225}}$

---

## Answer

$\frac{64}{225}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

---

## Solution Concepts

- truncated moment problem
- polynomial extremal certificate
- orthogonal polynomial decomposition
- equality-case support reconstruction
- finite quadrature measure
