## Steps

Step 1: Express the powered distance matrix through projective incidence

Fix $d\geq2$, and write
$$
v=2^{d+1}-1,\qquad k=2^d-1,\qquad s=2^{(d-1)/2}.
$$
Over $\mathbb{F}_2$, every nonzero vector determines a distinct projective point, so $|\mathcal{P}_d|=v$; duality gives $|\mathcal{H}_d|=v$. A point lies in $k$ hyperplanes because the nonzero linear functionals vanishing on it form a $d$-dimensional vector space. Two distinct points lie in $2^{d-1}-1$ common hyperplanes because the functionals vanishing on both form a $(d-1)$-dimensional vector space.

Let $B$ be the $v\times v$ point-hyperplane incidence matrix. The preceding counts give
$$
BB^T=2^{d-1}I+(2^{d-1}-1)J=s^2I+(s^2-1)J.
$$
Two distinct points have distance $2$, as do two distinct hyperplanes. If $P$ and $H$ are nonincident, choose $Q\in H$ and a hyperplane $K$ containing $P$ and $Q$; then $P-K-Q-H$ is a path of length $3$, so a point and a hyperplane have distance $1$ when incident and $3$ otherwise. Hence, with $a=2^p$ and $b=3^p$, the powered distance matrix is
$$
D_p=
\begin{pmatrix}
a(J-I)&bJ+(1-b)B\\
bJ+(1-b)B^T&a(J-I)
\end{pmatrix}.
$$

Step 2: Reduce conditional negative type to two scalar obstructions

Let $U=\mathbf{1}^{\perp}\subset\mathbb{R}^{v}$. Since $B^T\mathbf{1}=k\mathbf{1}$, the map $B^T$ preserves $U$. On $U$, Step 1 gives $BB^T=s^2I$, so
$$
Q=s^{-1}B^T:U\to U
$$
is orthogonal. For $u\in U$, the vectors $(u,Qu)$ and $(u,-Qu)$ are eigenvectors of $D_p$ with eigenvalues
$$
\lambda_{-}(p)=-2^p-(3^p-1)s<0,
$$
$$
\lambda_{+}(p)=-2^p+(3^p-1)s,
$$
respectively, each with multiplicity $v-1$.

The only remaining direction in the total-sum-zero subspace is
$$
z=(\mathbf{1},-\mathbf{1}).
$$
Because each point is incident with $k$ hyperplanes and nonincident with $v-k=2^d$ hyperplanes,
$$
D_pz=h_d(p)z,
$$
where
$$
h_d(p)=(2^{d+1}-2)2^p-(2^d-1)-2^d3^p.
$$
The decomposition
$$
\mathbf{1}_{X_d}^{\perp}=(U\oplus U)\oplus\mathbb{R}z
$$
has dimension $2v-1$, so these are all eigenvalues relevant to negative type. Therefore $(X_d,\rho_d)$ has $p$-negative type exactly when
$$
\lambda_{+}(p)\leq0\qquad\text{and}\qquad h_d(p)\leq0.
$$
At any exponent where these eigenvalues are nonpositive, the restriction of $D_p$ to $\mathbf{1}_{X_d}^{\perp}$ is symmetric negative semidefinite. Its quadratic form vanishes exactly on its kernel, so $\dim E_d$ is the zero-eigenvalue multiplicity at $p=\wp_d$.

Step 3: Locate the zero of the incidence mode

Put
$$
g_d(p)=s(3^p-1)-2^p=\lambda_{+}(p).
$$
We have $g_d(0)=-1$, while
$$
g_d'(p)=s3^p\log3-2^p\log2>0
$$
for $p\geq0$, because $s\geq\sqrt{2}$ and $(\frac{3}{2})^p\geq1$. Also $g_d(p)\to\infty$ as $p\to\infty$. Thus $g_d$ has a unique positive zero $\alpha_d$, and
$$
\lambda_{+}(p)\leq0\quad\Longleftrightarrow\quad p\leq\alpha_d.
$$
If this mode reaches zero before the imbalance mode, then the equality space has dimension $v-1=2^{d+1}-2$.

Step 4: Prove the phase transition between dimensions four and five

Set $m=2^d$. Rewrite the imbalance eigenvalue as
$$
h_d(p)=mA(p)+1-2^{p+1},
\qquad
A(p)=2^{p+1}-3^p-1.
$$
For $0<p<1$, strict concavity of $x^p$ and $2=\frac{1+3}{2}$ give $A(p)>0$. For $p>1$, strict convexity gives $A(p)<0$, while $A(1)=0$. Hence $h_d(p)<0$ for $p\geq1$, and on $0<p<1$ the function $h_d(p)$ increases with $d$.

For $d\leq4$ it is enough to consider $d=4$. Write $u=2^p\in(1,2)$ and $r=\log_{2}3$. Since $3^7>2^{11}$, we have $r>\frac{11}{7}$, so
$$
h_4(p)=-16u^r+30u-15<-16u^{\frac{11}{7}}+30u-15=:q(u).
$$
The concave function $q$ has its unique maximum at
$$
u_0=\left(\frac{105}{88}\right)^{\frac{7}{4}}<\frac{11}{8},
$$
where the last inequality is equivalent to the rational inequality $(\frac{105}{88})^7<(\frac{11}{8})^4$. Using $u_0^{\frac{4}{7}}=\frac{105}{88}$,
$$
q(u_0)=\frac{120}{11}u_0-15<\frac{120}{11}\frac{11}{8}-15=0.
$$
Thus $h_d(p)<0$ for every $p>0$ when $d\leq4$.

For $d\geq5$, monotonicity in $d$ on $(0,1)$ and
$$
h_5\left(\frac{1}{2}\right)=62\sqrt{2}-32\sqrt{3}-31>0
$$
show that $h_d$ has a first positive zero $\beta_d<\frac{1}{2}$, since $h_d(0)=-1$. The displayed inequality is exact: after squaring twice it reduces to $13{,}359{,}025>11{,}808{,}768$. As a function of $u=2^p$,
$$
h_d=-mu^r+2(m-1)u-(m-1),
$$
which is strictly concave because $r>1$. Hence it has at most two zeros and is positive between its first and second zeros.

It remains to compare $\beta_d$ with $\alpha_d$. At $p=\alpha_d$, let $u=2^{\alpha_d}$ and keep $s=2^{(d-1)/2}$. Since $s(3^{\alpha_d}-1)=u$ and $2^d=2s^2$, substitution gives
$$
h_d(\alpha_d)=(2s+1)\left(2u(s-1)-(2s-1)\right).
$$
Set
$$
t=1+\frac{1}{2(s-1)},\qquad r=\log_{2}3.
$$
The equation for $u$ is $G_s(u)=0$, where
$$
G_s(x)=s(x^r-1)-x.
$$
Since $G_s'(x)>0$ for $x\geq1$, it is enough to prove $G_s(t)<0$. Write $\delta=\frac{1}{2(s-1)}$. For $d\geq5$, $s\geq4$ and $0<\delta\leq\frac{1}{6}$, while
$$
G_s(t)=F(\delta)=\left(1+\frac{1}{2\delta}\right)\left((1+\delta)^r-1\right)-(1+\delta).
$$
Differentiation gives
$$
F'(\delta)=\frac{\delta r(1+\delta)^{r-1}-((1+\delta)^r-1)}{2\delta^2}+r(1+\delta)^{r-1}-1>0.
$$
The first numerator is positive by convexity of $x^r$, and the second term is positive because $r>1$. Hence $F(\delta)\leq F(\frac{1}{6})$. Also $r<\frac{8}{5}$ because $3^5<2^8$. Taylor's theorem, using the bound on the second derivative of $(1+x)^{\frac{8}{5}}$, gives
$$
\left(\frac{7}{6}\right)^r<\left(\frac{7}{6}\right)^{\frac{8}{5}}\leq1+\frac{4}{15}+\frac{1}{75}=\frac{32}{25}.
$$
Therefore
$$
F(\frac{1}{6})<4\left(\frac{32}{25}-1\right)-\frac{7}{6}=-\frac{7}{150}<0.
$$
Thus $h_d(\alpha_d)>0$, so $\beta_d<\alpha_d$ for every $d\geq5$.

At $d\leq4$, the first zero is therefore $\alpha_d$ and the kernel has dimension $v-1>1$. At $d\geq5$, the first zero is $\beta_d$ and only the direction $z$ vanishes, so $\dim E_d=1$. Hence
$$
d_*=5.
$$

Step 5: Compute the asymptotic critical exponent

For $d\geq5$, Step 4 gives $\wp_d=\beta_d$. With $m=2^d$, the equation $h_d(\beta_d)=0$ is
$$
mA(\beta_d)=2^{\beta_d+1}-1,
\qquad
A(p)=2^{p+1}-3^p-1.
$$
Since $0<\beta_d<\frac{1}{2}$, the right-hand side is bounded, so $A(\beta_d)\to0$. Step 4 gives $A(p)>0$ on $(0,1)$. If a subsequence of $\beta_d$ stayed above some $\varepsilon>0$, continuity would give a positive lower bound for $A(\beta_d)$ on $[\varepsilon,\frac{1}{2}]$, a contradiction. Hence $\beta_d\to0$. Dividing the displayed equation by $\beta_d$ gives
$$
2^d\beta_d=\frac{2^{\beta_d+1}-1}{A(\beta_d)/\beta_d}
\longrightarrow\frac{1}{A'(0)}
=\frac{1}{2\log2-\log3}
=\frac{1}{\log\left(\frac{4}{3}\right)}.
$$
Combining this with $d_*=5$ gives the requested pair.

Final Answer: $\boxed{(5,\frac{1}{\log(\frac{4}{3})})}$

---

## Answer

$(5,\frac{1}{\log(\frac{4}{3})})$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- conditional negative type
- incidence graph metrics
- symmetric design incidence matrices
- spectral decomposition
- concavity and phase transitions
