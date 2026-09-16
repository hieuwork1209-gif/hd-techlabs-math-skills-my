## Steps

Step 1: Force every maximizer to be a circulant completion.
Let $\mathcal F$ be the set of real symmetric positive semidefinite $6\times6$ matrices $G=(g_{ij})$ with
$$
g_{ii}=1,
\qquad
g_{12}=g_{23}=g_{34}=g_{45}=g_{56}=g_{61}=\frac12.
$$
Every entry of a matrix in $\mathcal F$ has absolute value at most $1$, by the $2\times2$ principal minors, so $\mathcal F$ is compact. The matrix with diagonal entries $1$ and every off-diagonal entry $1/2$ equals
$$
\frac12 I+\frac12 J,
$$
where $J$ is the all-ones matrix. Its eigenvalues are $7/2$ once and $1/2$ five times, so it is positive definite and belongs to $\mathcal F$. Hence the maximum determinant on $\mathcal F$ is positive, and every maximizer is positive definite.

Let $P$ be the permutation matrix for the cyclic shift of the six coordinates. If $G$ is a maximizer, then every $P^jG(P^j)^T$ is also feasible and has the same determinant. Their average is feasible. On the positive definite cone, along a nonzero symmetric direction $H$,
$$
\frac{d^2}{ds^2}\log\det(G+sH)
=-\operatorname{tr}\left((G+sH)^{-1}H(G+sH)^{-1}H\right)<0
$$
whenever the segment is positive definite. Thus $\log\det$ is strictly concave. The cyclic average would therefore have strictly larger determinant unless all six rotated matrices were equal. Hence every maximizer is invariant under cyclic shifts. Since it is also symmetric, it must be the matrix $C(a,b)$ from the prompt for some real $a,b$.

Step 2: Use first-order optimality to reconstruct the inverse matrix.
Let $G=C(a,b)$ be a maximizer and put $K=G^{-1}$. For any nonedge pair $i\ne j$, the entry $g_{ij}$ is free in the affine constraint set. Because $G$ is positive definite, sufficiently small symmetric perturbations in that entry remain positive definite. If $E_{ij}$ denotes the matrix unit, Jacobi's formula gives
$$
\left.\frac{d}{d\varepsilon}\log\det\left(G+\varepsilon(E_{ij}+E_{ji})\right)\right|_{\varepsilon=0}
=2K_{ij}.
$$
At the maximum this derivative is zero. Hence $K_{ij}=0$ for every nonedge. Since the inverse of a circulant matrix is circulant, the first row of $K$ has the form
$$
(d,e,0,0,0,e).
$$
Because $K$ is positive definite, $d>0$. Write $t=-e/d$. Multiplying $GK=I$ and comparing the four cyclic distances gives
$$
d+e=1,
$$
$$
\frac d2+e(1+a)=0,
$$
$$
ad+e\left(\frac12+b\right)=0,
$$
$$
bd+2ae=0.
$$
Thus
$$
d(1-t)=1,
\qquad
\frac12=t(1+a),
\qquad
a=t\left(\frac12+b\right),
\qquad
b=2at.
$$
The second relation gives $a=1/(2t)-1$, while the last two give
$$
a(1-2t^2)=\frac t2.
$$
Eliminating $a$ yields
$$
(t-1)(4t^2+t-1)=0.
$$
Let $\omega=e^{2\pi i/6}$. For the circulant matrix $K/d$, the vector
$$
(1,\omega^k,\omega^{2k},\ldots,\omega^{5k})
$$
has eigenvalue
$$
1-t(\omega^k+\omega^{-k})=1-2t\cos\left(\frac{k\pi}{3}\right).
$$
Hence the six eigenvalues are
$$
1-2t,\quad 1-t,\quad 1-t,\quad 1+t,\quad 1+t,\quad 1+2t.
$$
Positive definiteness therefore requires $|t|<1/2$. Among the three roots above, the unique admissible one is
$$
t=\frac{\sqrt{17}-1}{8}.
$$
Consequently
$$
a=\frac{1}{2t}-1=\frac{\sqrt{17}-3}{4},
\qquad
b=2at=\frac{5-\sqrt{17}}{4}.
$$

Step 3: Evaluate the determinant and state the unique optimizer.
The eigenvalues derived in Step 2 give
$$
\det K=d^6(1-4t^2)(1-t^2)^2.
$$
Since $d=1/(1-t)$,
$$
\det G=\frac{(1-t)^6}{(1-4t^2)(1-t^2)^2}
=\frac{(1-t)^4}{(1-4t^2)(1+t)^2}.
$$
The relation $4t^2+t-1=0$ gives $1-4t^2=t$. Repeatedly replacing $t^2$ by $(1-t)/4$ gives
$$
(1-t)^4=\frac{181-441t}{64},
\qquad
t(1+t)^2=\frac{7+13t}{16}.
$$
Using $4t^2+t-1=0$ once more in the quotient gives
$$
\det G=85t-33=\frac{85\sqrt{17}-349}{8}.
$$
Existence of a maximizer was established in Step 1, while Steps 1 and 2 show that every maximizer must have exactly these values of $a$ and $b$. Hence the maximizing matrix is unique.

Final Answer: $\boxed{\left(\frac{85\sqrt{17}-349}{8},\frac{\sqrt{17}-3}{4},\frac{5-\sqrt{17}}{4}\right)}$

---

## Answer

$\left(\frac{85\sqrt{17}-349}{8},\frac{\sqrt{17}-3}{4},\frac{5-\sqrt{17}}{4}\right)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- maximum determinant matrix completion
- strict concavity of log determinant
- first-order optimality conditions
- circulant matrices
- spectral determinant evaluation
