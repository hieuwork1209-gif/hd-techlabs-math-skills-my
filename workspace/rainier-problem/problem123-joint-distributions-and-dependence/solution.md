## Steps

Step 1: Replace the non-identifiable latent variable by the parameter seen by the observations

Fix $a>0$ and let
$$
\Theta\sim\operatorname{Beta}(a,a).
$$
Set
$$
P=4\Theta(1-\Theta).
$$
The observations depend on $\Theta$ only through $P$. For $0<p<1$, the two inverse branches are
$$
\theta_\pm(p)=\frac{1\pm\sqrt{1-p}}2,
\qquad
\left|\frac{d\theta_\pm}{dp}\right|=\frac1{4\sqrt{1-p}}.
$$
At either inverse point,
$$
\theta_\pm(1-\theta_\pm)=\frac p4.
$$
Therefore the density of $P$ is proportional to
$$
p^{a-1}(1-p)^{-1/2},\qquad 0<p<1.
$$
Since this density is normalized, it is exactly the $\operatorname{Beta}(a,1/2)$ density. Equivalently, the normalizing identity is
$$
B\!\left(a,\frac12\right)=2^{2a-1}B(a,a),
$$
which follows directly by the substitution $p=4\theta(1-\theta)$ on $0<\theta<1/2$.

Both inverse values of $\Theta$ give the same Bernoulli success probability $p$. Hence, conditional on $P=p$, the two sequences remain independent and every coordinate is Bernoulli$(p)$. Thus the statistically identifiable latent variable is
$$
P\sim\operatorname{Beta}\!\left(a,\frac12\right).
$$

Step 2: Reduce the two-block mutual information to one parameter-sample quantity

For $m\ge1$, let $Z^{(m)}=(Z_1,\ldots,Z_m)$ be conditionally iid Bernoulli$(P)$ given $P$, and put
$$
J_m=I(P;Z^{(m)}).
$$
Because $X^{(n)}=(X_1,\ldots,X_n)$ and $Y^{(n)}=(Y_1,\ldots,Y_n)$ are conditionally independent given $P$,
$$
I(X^{(n)};Y^{(n)}\mid P)=0.
$$
Expanding the three mutual informations by discrete entropies gives
$$
\begin{aligned}
&I(P;X^{(n)})+I(P;Y^{(n)})-I(P;X^{(n)},Y^{(n)})\\
&=H(X^{(n)})+H(Y^{(n)})-H(X^{(n)},Y^{(n)})
=I(X^{(n)};Y^{(n)}),
\end{aligned}
$$
because conditional independence gives
$$
H(X^{(n)},Y^{(n)}\mid P)
=H(X^{(n)}\mid P)+H(Y^{(n)}\mid P).
$$
The concatenated pair $(X^{(n)},Y^{(n)})$ is, conditional on $P$, a Bernoulli sample of size $2n$. Therefore
$$
I(X^{(n)};Y^{(n)})=2J_n-J_{2n}.
$$

Step 3: Derive the Beta-Bernoulli information asymptotic with boundary control

We first prove a lemma for fixed $r,s>0$. Let $Q\sim\operatorname{Beta}(r,s)$ and, conditional on $Q$, let $Z_1,\ldots,Z_m$ be iid Bernoulli$(Q)$. Write
$$
S_m=\sum_{i=1}^m Z_i,
\qquad
J_m(r,s)=I(Q;Z_1,\ldots,Z_m).
$$
Given $S_m=k$, every binary string with $k$ ones has the same likelihood $Q^k(1-Q)^{m-k}$, so the string carries no information about $Q$ beyond $S_m$. Hence
$$
J_m(r,s)=I(Q;S_m).
$$
Bayes' formula gives
$$
Q\mid S_m=k\sim\operatorname{Beta}(r+k,s+m-k).
$$
Let $h_{u,v}$ denote the differential entropy of $\operatorname{Beta}(u,v)$. Since
$$
E\log Q=\psi(u)-\psi(u+v),
\qquad
E\log(1-Q)=\psi(v)-\psi(u+v),
$$
obtained by differentiating the beta integral, the entropy is
$$
h_{u,v}
=\log B(u,v)-(u-1)\psi(u)-(v-1)\psi(v)+(u+v-2)\psi(u+v).
$$
Consequently
$$
J_m(r,s)=h_{r,s}-E\,h_{r+S_m,s+m-S_m}.
$$

For large $u,v$, substituting
$$
\log\Gamma(t)=\left(t-\frac12\right)\log t-t+\frac12\log(2\pi)+O(t^{-1}),
$$
$$
\psi(t)=\log t-\frac1{2t}+O(t^{-2})
$$
into the displayed entropy formula gives
$$
h_{u,v}
=\frac12\log\!\left(\frac{2\pi e\,uv}{(u+v)^3}\right)
+O(u^{-1}+v^{-1}).
$$
We now justify averaging this expansion even near the beta endpoints. Put
$$
\delta_m=m^{-1/8},\qquad \varepsilon_m=m^{-1/4},
$$
and consider
$$
E_m=\left\{\delta_m\le Q\le1-\delta_m,
\ \left|\frac{S_m}{m}-Q\right|\le\varepsilon_m\right\}.
$$
The beta density gives
$$
P(Q<\delta_m)=O(\delta_m^r),
\qquad
P(Q>1-\delta_m)=O(\delta_m^s),
$$
and conditional Chebyshev, using
$$
\operatorname{Var}(S_m/m\mid Q)=\frac{Q(1-Q)}m\le\frac1{4m},
$$
gives
$$
P\!\left(\left|\frac{S_m}{m}-Q\right|>\varepsilon_m\right)
=O(m^{-1/2}).
$$
On $E_m$, both posterior shape parameters are at least a constant multiple of $m\delta_m$, and
$$
\frac{r+S_m}{m+r+s}=Q+O(\varepsilon_m+m^{-1}).
$$
Since $\varepsilon_m/\delta_m=m^{-1/8}\to0$, the entropy expansion is uniform there and yields
$$
h_{r+S_m,s+m-S_m}
=\frac12\log\frac{2\pi e}{m}
+\frac12\log(Q(1-Q))+o(1).
$$
For fixed $r,s$, the exact beta-entropy formula also gives the uniform bound
$$
|h_{r+k,s+m-k}|\le C_{r,s}(1+\log(m+1)),\qquad 0\le k\le m.
$$
Indeed, if both shape parameters grow, this follows from the preceding asymptotic; if one stays in a fixed compact interval, the other is $m+O(1)$ and the same gamma/digamma expansions give $-\log m+O(1)$. Thus the contribution of $E_m^c$ is $o(1)$. The beta log moments are integrable, and their boundary tails are
$$
O(\!\delta_m^r|\log\delta_m|)+O(\!\delta_m^s|\log\delta_m|)=o(1),
$$
so averaging gives
$$
E\,h_{r+S_m,s+m-S_m}
=\frac12\log\frac{2\pi e}{m}
+\frac12E\log(Q(1-Q))+o(1).
$$
Therefore
$$
J_m(r,s)=\frac12\log m+C(r,s)+o(1),
$$
where
$$
C(r,s)=h_{r,s}-\frac12\log(2\pi e)-\frac12E\log(Q(1-Q)).
$$
Using the displayed beta entropy and log moments,
$$
C(r,s)
=\log B(r,s)-\left(r-\frac12\right)\psi(r)
-\left(s-\frac12\right)\psi(s)
+(r+s-1)\psi(r+s)-\frac12\log(2\pi e).
$$

Step 4: Specialize the asymptotic to the induced latent law

From Step 1, $P\sim\operatorname{Beta}(a,1/2)$. Setting $r=a$ and $s=1/2$ in Step 3 cancels the $\psi(1/2)$ term and gives
$$
J_m
=\frac12\log m+C_a+o(1),
$$
with
$$
C_a
=\log B\!\left(a,\frac12\right)
+\left(a-\frac12\right)
\left[\psi\!\left(a+\frac12\right)-\psi(a)\right]
-\frac12\log(2\pi e).
$$
This holds for every fixed $a>0$; the endpoint estimates in Step 3 require only positivity of the beta shape parameters.

Step 5: Combine the sample sizes $n$ and $2n$

Step 2 and Step 4 give
$$
\begin{aligned}
I(X^{(n)};Y^{(n)})
&=2J_n-J_{2n}\\
&=2\left(\frac12\log n+C_a\right)
-\left(\frac12\log(2n)+C_a\right)+o(1)\\
&=\frac12\log n+C_a-\frac12\log2+o(1).
\end{aligned}
$$
Hence
$$
\lim_{n\to\infty}\left[I(X^{(n)};Y^{(n)})-\frac12\log n\right]
=\log B\!\left(a,\frac12\right)
+\left(a-\frac12\right)
\left[\psi\!\left(a+\frac12\right)-\psi(a)\right]
-\frac12\log(4\pi e).
$$

## Solution Concepts

- Identifiable latent quotient and the induced beta distribution under a two-to-one transformation.
- Conditional-independence decomposition of mutual information across two exchangeable sample blocks.
- Beta-Bernoulli posterior entropy asymptotics with explicit endpoint control.

Final Answer: $\displaystyle \log B(a,\frac12)+(a-\frac12)(\psi(a+\frac12)-\psi(a))-\frac12\log(4\pi e)$.
