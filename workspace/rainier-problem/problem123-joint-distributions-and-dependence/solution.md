## Steps

Step 1: Separate the shared mass from the residual composition

Let
$$
(P_1,P_2,P_3,P_4)\sim\operatorname{Dirichlet}(a,1,1,1),
\qquad a>0.
$$
Thus on the simplex $p_j>0$, $p_1+p_2+p_3+p_4=1$, the density with respect to $dp_1\,dp_2\,dp_3$ is
$$
\frac{\Gamma(a+3)}{\Gamma(a)}p_1^{a-1}.
$$
Set
$$
S=P_1,
\qquad
U=\frac{P_2}{1-P_1},
\qquad
V=\frac{P_3}{1-P_1}.
$$
Then
$$
P_2=(1-S)U,
\quad
P_3=(1-S)V,
\quad
P_4=(1-S)(1-U-V),
$$
where $0<S<1$, $U>0$, $V>0$, and $U+V<1$. The Jacobian of $(S,U,V)\mapsto(P_1,P_2,P_3)$ is $(1-S)^2$. Hence the joint density of $(S,U,V)$ is
$$
\frac{\Gamma(a+3)}{\Gamma(a)}S^{a-1}(1-S)^2
=
\frac{S^{a-1}(1-S)^2}{B(a,3)}\,2.
$$
Therefore
$$
S\sim\operatorname{Beta}(a,3),
$$
and $S$ is independent of $(U,V)$, while $(U,V)$ is uniform with density $2$ on
$$
\{(u,v):u>0,\ v>0,\ u+v<1\}.
$$

Step 2: Split the mutual information into a shared layer and a residual layer

For the $X$-sample define
$$
A_i=\mathbf 1_{\{X_i=1\}},
$$
and for the $Y$-sample define
$$
B_i=\mathbf 1_{\{Y_i=1\}}.
$$
Given $S$, both $(A_i)$ and $(B_i)$ are iid Bernoulli$(S)$ sequences, and the two sequences are conditionally independent.

Whenever $A_i=0$, the residual label records whether $X_i=2$ or $X_i=3$. Conditional on $(S,U,V)$, these residual labels are iid Bernoulli$(U)$. Similarly, conditional on $(S,U,V)$, the residual labels of the $Y$-sample are iid Bernoulli$(V)$.

Let
$$
M_X=\sum_{i=1}^n(1-A_i),
\qquad
M_Y=\sum_{i=1}^n(1-B_i),
$$
and let $R_X^{(M_X)}$ and $R_Y^{(M_Y)}$ denote the two residual binary strings. Because $S$ is independent of $(U,V)$, conditional on $(A^{(n)},B^{(n)})$ the residual pair depends on the indicator strings only through the lengths $(M_X,M_Y)$. Hence the likelihood ratio factors into an indicator part and a residual part, giving the exact identity
$$
I(X^{(n)};Y^{(n)})
=
I(A^{(n)};B^{(n)})
+E\,R_{M_X,M_Y},
$$
where
$$
R_{m,\ell}
=I(R_X^{(m)};R_Y^{(\ell)})
$$
for Bernoulli samples generated from the latent pair $(U,V)$.

Step 3: Evaluate the residual dependence limit

For fixed $m,\ell$, the Markov structure
$$
R_X^{(m)}\longrightarrow U\longrightarrow V\longrightarrow R_Y^{(\ell)}
$$
gives by data processing
$$
0\le R_{m,\ell}\le I(U;V).
$$
As $m,\ell\to\infty$, the strong law gives
$$
\frac1m\sum_{j=1}^m R_{X,j}\to U,
\qquad
\frac1\ell\sum_{j=1}^\ell R_{Y,j}\to V
$$
almost surely. Thus $U$ is measurable from the infinite $X$-residual sequence and $V$ from the infinite $Y$-residual sequence. Mutual information of increasing finite prefixes converges to the mutual information of the full infinite sequences; data processing in both directions then gives
$$
\lim_{m,\ell\to\infty}R_{m,\ell}=I(U;V).
$$
Also, conditional on $S<1$,
$$
\frac{M_X}{n}\to1-S,
\qquad
\frac{M_Y}{n}\to1-S
$$
almost surely, so $M_X,M_Y\to\infty$ almost surely. Since $R_{m,\ell}\le I(U;V)$, bounded convergence yields
$$
E\,R_{M_X,M_Y}\to I(U;V).
$$

Now $(U,V)$ has density $2$ on a triangle of area $1/2$, so
$$
h(U,V)=-\log2.
$$
The marginal density is
$$
f_U(u)=2(1-u),\qquad 0<u<1,
$$
and therefore
$$
\begin{aligned}
h(U)
&=-\int_0^1 2(1-u)\log\bigl(2(1-u)\bigr)\,du\\
&=\frac12-\log2.
\end{aligned}
$$
The same holds for $V$, hence
$$
I(U;V)=h(U)+h(V)-h(U,V)=1-\log2.
$$
Consequently
$$
E\,R_{M_X,M_Y}=1-\log2+o(1).
$$

Step 4: Derive the shared Beta-Bernoulli asymptotic

We need the mutual information between two Bernoulli samples sharing
$$
S\sim\operatorname{Beta}(r,s),
\qquad r,s>0.
$$
For one sample $Z^{(m)}=(Z_1,\ldots,Z_m)$, let
$$
J_m(r,s)=I(S;Z^{(m)}),
\qquad
K_m=\sum_{i=1}^m Z_i.
$$
The sufficient statistic $K_m$ gives
$$
S\mid K_m=k\sim\operatorname{Beta}(r+k,s+m-k).
$$
For $Q\sim\operatorname{Beta}(u,v)$,
$$
E\log Q=\psi(u)-\psi(u+v),
\qquad
E\log(1-Q)=\psi(v)-\psi(u+v),
$$
so its differential entropy is
$$
h_{u,v}
=\log B(u,v)-(u-1)\psi(u)-(v-1)\psi(v)+(u+v-2)\psi(u+v).
$$
Thus
$$
J_m(r,s)=h_{r,s}-E\,h_{r+K_m,s+m-K_m}.
$$

Using
$$
\log\Gamma(t)=\left(t-\frac12\right)\log t-t+\frac12\log(2\pi)+O(t^{-1}),
$$
$$
\psi(t)=\log t-\frac1{2t}+O(t^{-2}),
$$
we obtain, when both $u,v\to\infty$,
$$
h_{u,v}
=
\frac12\log\!\left(\frac{2\pi e\,uv}{(u+v)^3}\right)
+O(u^{-1}+v^{-1}).
$$
To average this uniformly, take
$$
\delta_m=m^{-1/8},
\qquad
\varepsilon_m=m^{-1/4}.
$$
On the event
$$
\delta_m\le S\le1-\delta_m,
\qquad
\left|\frac{K_m}{m}-S\right|\le\varepsilon_m,
$$
both posterior shape parameters are $\gg m\delta_m$, and the displayed entropy expansion gives uniformly
$$
h_{r+K_m,s+m-K_m}
=
\frac12\log\frac{2\pi e}{m}
+\frac12\log(S(1-S))+o(1).
$$
The beta endpoint probabilities are
$$
P(S<\delta_m)=O(\delta_m^r),
\qquad
P(S>1-\delta_m)=O(\delta_m^s),
$$
while conditional Chebyshev gives
$$
P\!\left(\left|\frac{K_m}{m}-S\right|>\varepsilon_m\right)=O(m^{-1/2}).
$$
The exact beta-entropy formula gives the uniform bound
$$
|h_{r+k,s+m-k}|\le C_{r,s}(1+\log(m+1)),
$$
and the beta log moments are integrable, so the complement contributes $o(1)$. Therefore
$$
E\,h_{r+K_m,s+m-K_m}
=
\frac12\log\frac{2\pi e}{m}
+\frac12E\log(S(1-S))+o(1).
$$
It follows that
$$
J_m(r,s)
=
\frac12\log m+C(r,s)+o(1),
$$
where
$$
C(r,s)
=
\log B(r,s)
-\left(r-\frac12\right)\psi(r)
-\left(s-\frac12\right)\psi(s)
+(r+s-1)\psi(r+s)
-\frac12\log(2\pi e).
$$

For two conditionally independent size-$n$ Bernoulli samples $A^{(n)},B^{(n)}$ sharing $S$,
$$
I(A^{(n)};B^{(n)})
=2J_n(r,s)-J_{2n}(r,s).
$$
Hence
$$
I(A^{(n)};B^{(n)})
=
\frac12\log n+D(r,s)+o(1),
$$
with
$$
D(r,s)=C(r,s)-\frac12\log2.
$$
For $(r,s)=(a,3)$,
$$
D(a,3)
=
\log B(a,3)
-\left(a-\frac12\right)\psi(a)
-\frac52\psi(3)
+(a+2)\psi(a+3)
-\frac12\log(4\pi e).
$$

Step 5: Combine the shared and residual layers

By Steps 2--4,
$$
\begin{aligned}
I(X^{(n)};Y^{(n)})
&=\frac12\log n+D(a,3)+1-\log2+o(1).
\end{aligned}
$$
Since
$$
-\frac12\log(4\pi e)-\log2
=-\frac12\log(16\pi e),
$$
we obtain
$$
\lim_{n\to\infty}\left[I(X^{(n)};Y^{(n)})-\frac12\log n\right]
=
\log B(a,3)
-\left(a-\frac12\right)\psi(a)
-\frac52\psi(3)
+(a+2)\psi(a+3)
+1
-\frac12\log(16\pi e).
$$

## Solution Concepts

- Reparameterization of a Dirichlet composition into an independent shared mass and residual simplex coordinates.
- Exact decomposition of block mutual information into a divergent shared layer and a finite residual dependence layer.
- Beta-Bernoulli posterior entropy asymptotics with endpoint control.

Final Answer: $\displaystyle \log B(a,3)-(a-\frac12)\psi(a)-\frac52\psi(3)+(a+2)\psi(a+3)+1-\frac12\log(16\pi e)$.
