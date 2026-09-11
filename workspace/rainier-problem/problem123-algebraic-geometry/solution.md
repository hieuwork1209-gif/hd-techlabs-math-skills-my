## Steps

Step 1: Identify the conjugate branches of the finite projection

Put
$$
x=t^m,
\qquad
y=t^n+t^p,
\qquad
d=\gcd(m,n),
\qquad
a=\frac md.
$$
Because $d$ divides both $m$ and $n$ and $\gcd(d,p)=1$,
$$
\gcd(m,n,p)=1.
\tag{1}
$$

The extension $\mathbb C((t))/\mathbb C((x))$ is cyclic of degree $m$. Its automorphisms are
$$
t\longmapsto \alpha t,
\qquad \alpha^m=1.
$$
If such an automorphism fixes $y$, then equality of the coefficients of the distinct powers $t^n$ and $t^p$ gives
$$
\alpha^n=\alpha^p=1.
$$
Together with $\alpha^m=1$ and (1), this forces $\alpha=1$. Hence the orbit of $y$ has size $m$, so its monic minimal polynomial over $\mathbb C((x))$ has degree $m$ and its roots are
$$
y_\alpha=\alpha^n t^n+\alpha^p t^p,
\qquad \alpha\in\mu_m,
\tag{2}
$$
where $\mu_m$ is the group of $m$th roots of unity.

The element $t$ is integral over $\mathbb C[[x]]$ because it satisfies $T^m-x=0$, so $y$ is integral over $\mathbb C[[x]]$. Since $\mathbb C[[x]]$ is integrally closed, the monic minimal polynomial has coefficients in $\mathbb C[[x]]$. Thus, after replacing $x$ by a formal variable $X$, it defines the polynomial $P(X,Y)\in\mathbb C[[X]][Y]$ from the problem.

Step 2: Express the discriminant through derivatives at the conjugate roots

For a monic degree-$m$ polynomial with distinct roots $r_1,\dots,r_m$,
$$
P'(r_i)=\prod_{j\ne i}(r_i-r_j).
$$
Multiplying over $i$, every unordered pair $\{i,j\}$ contributes
$$
(r_i-r_j)(r_j-r_i)=-(r_i-r_j)^2.
$$
Therefore
$$
\operatorname{Disc}(P)
=(-1)^{m(m-1)/2}\prod_{i=1}^m P'(r_i).
\tag{3}
$$
Applying (3) to the roots (2), it remains to determine the first nonzero term of each
$$
P_Y'(x,y_\alpha)=\prod_{\substack{\beta\in\mu_m\\\beta\ne\alpha}}(y_\alpha-y_\beta).
\tag{4}
$$

Step 3: Derive the two root-of-unity strata and their exact leading products

Fix $\alpha\in\mu_m$ and write $\beta=\alpha\xi$, where $\xi\in\mu_m\setminus\{1\}$. Then
$$
\begin{aligned}
y_\alpha-y_{\alpha\xi}
&=\alpha^n t^n(1-\xi^n)
 +\alpha^p t^p(1-\xi^p).
\end{aligned}
\tag{5}
$$
There are two forced cases.

If $\xi^n\ne1$, the first term in (5) is nonzero, so the $t$-order is $n$ and the leading coefficient is
$$
\alpha^n(1-\xi^n).
$$

If $\xi^n=1$, then $\xi$ lies in the kernel of the map $\mu_m\to\mu_m$, $\xi\mapsto\xi^n$. That kernel has size $d$ and is exactly $\mu_d$. For $\xi\ne1$ in this kernel, $\xi^p\ne1$ because $\gcd(d,p)=1$. Hence the $t$-order in this case is $p$ and the leading coefficient is
$$
\alpha^p(1-\xi^p).
$$

Thus, if
$$
D:=(m-d)n+(d-1)p,
\tag{6}
$$
then (4) has $t$-order $D$. Its leading coefficient is
$$
\alpha^D A B,
\tag{7}
$$
where
$$
A=\prod_{\substack{\xi\in\mu_m\\\xi^n\ne1}}(1-\xi^n),
\qquad
B=\prod_{\substack{\xi\in\mu_d\\\xi\ne1}}(1-\xi^p).
$$

We now evaluate these products exactly. The map
$$
\mu_m\longrightarrow\mu_a,
\qquad \xi\longmapsto\xi^n,
$$
has kernel $\mu_d$ and is onto because $\gcd(n/d,m/d)=1$. Hence every nontrivial element of $\mu_a$ occurs exactly $d$ times among the values $\xi^n$ with $\xi^n\ne1$. Therefore
$$
A=\left(\prod_{\substack{\eta\in\mu_a\\\eta\ne1}}(1-\eta)\right)^d.
$$
Since
$$
\frac{z^a-1}{z-1}=\prod_{\substack{\eta\in\mu_a\\\eta\ne1}}(z-\eta),
$$
evaluating at $z=1$ gives
$$
\prod_{\substack{\eta\in\mu_a\\\eta\ne1}}(1-\eta)=a.
$$
Thus
$$
A=a^d.
\tag{8}
$$

Similarly, exponentiation by $p$ permutes $\mu_d$ because $\gcd(d,p)=1$. Hence
$$
B=\prod_{\substack{\xi\in\mu_d\\\xi\ne1}}(1-\xi)=d.
\tag{9}
$$
Combining (7)-(9),
$$
P_Y'(x,y_\alpha)
=a^d d\,\alpha^D t^D+O(t^{D+1}).
\tag{10}
$$

Step 4: Multiply the conjugates and track the discriminant sign

Multiplying (10) over all $\alpha\in\mu_m$ gives
$$
\prod_{\alpha\in\mu_m}P_Y'(x,y_\alpha)
=(a^d d)^m\left(\prod_{\alpha\in\mu_m}\alpha\right)^D
 t^{mD}+O(t^{mD+1}).
\tag{11}
$$
The product of all roots of $z^m-1$ is
$$
\prod_{\alpha\in\mu_m}\alpha=(-1)^{m+1},
\tag{12}
$$
because the constant term of $z^m-1$ is $-1$.

Substituting (11)-(12) into the discriminant identity (3) yields the nonzero leading term
$$
(-1)^{m(m-1)/2+(m+1)D}(a^d d)^m t^{mD}.
$$
The discriminant belongs to $\mathbb C[[x]]=\mathbb C[[t^m]]$. Since $x=t^m$, the preceding term is exactly
$$
(-1)^{m(m-1)/2+(m+1)D}(a^d d)^m x^D.
$$
All later terms of the discriminant have $t$-orders divisible by $m$, so after the leading order $mD$ the next possible order is at least $m(D+1)$. Therefore
$$
\operatorname{Disc}_Y P(X,Y)
=
(-1)^{m(m-1)/2+(m+1)D}
\left(\left(\frac md\right)^d d\right)^m X^D
+O(X^{D+1}),
$$
where $D$ is given by (6).

## Solution Concepts

- Galois conjugates of a parametrized plane branch under the finite projection $x=t^m$.
- Root-of-unity stratification by the stabilizers of the first and second Puiseux terms.
- Exact discriminant product and leading-unit computation.

Final Answer: $\displaystyle (-1)^{m(m-1)/2+(m+1)D}\left((m/d)^d d\right)^m X^D,\quad D=(m-d)n+(d-1)p$.
