## Steps

Step 1: Derive the quadratic character-sum lemma and the base residue sum.
Let $\chi$ be the quadratic character of $\mathbb F_{\ell}$, extended by $\chi(0)=0$. Since $\ell\equiv3\pmod 4$, we have $\chi(-1)=-1$, so $-1\notin H$ and $\chi(1+x)\in\{\pm1\}$ for every $x\in H$.

We first derive the quadratic character-sum identity needed below. If $d\ne0$, count pairs $(u,v)\in\mathbb F_{\ell}^2$ satisfying
$$
v^2=u^2-d.
$$
Writing $a=u-v$ and $b=u+v$ gives $ab=d$. Every $a\in\mathbb F_{\ell}^{\times}$ determines the unique $b=d/a$, and since $2$ is invertible this determines a unique pair $(u,v)$. Hence there are $\ell-1$ such pairs. On the other hand, for each $u$ the number of $v$ is $1+\chi(u^2-d)$, so
$$
\ell-1=\sum_{u\in\mathbb F_{\ell}}\left(1+\chi(u^2-d)\right),
$$
and therefore
$$
\sum_{u\in\mathbb F_{\ell}}\chi(u^2-d)=-1.
$$
Consequently, if $A\ne0$ and $B^2-4AC\ne0$, completing the square gives
$$
\sum_{t\in\mathbb F_{\ell}}\chi(At^2+Bt+C)=-\chi(A).
$$

Now put
$$
S=\sum_{x\in H}\chi(1+x).
$$
Using the indicator $(1+\chi(x))/2$ of $H$ on $\mathbb F_{\ell}^{\times}$,
$$
S=\frac12\sum_{x\ne0}\chi(1+x)+\frac12\sum_{x\ne0}\chi(x(1+x)).
$$
The first sum is $-1$, because $\sum_x\chi(1+x)=0$ and the omitted term $x=0$ equals $1$. The second sum is also $-1$ by the quadratic identity with $x(1+x)=x^2+x$. Thus
$$
S=-1.
$$

Step 2: Evaluate the same-sign second moment.
For $x\in H$, write $u_x=\chi(1+x)$. For $x,y\in H$, define
$$
K(x,y)=\sum_{a\in\mathbb F_{\ell}^{\times}}\chi(1+ax)\chi(1+ay).
$$
If $x=y$, exactly one nonzero value $a=-x^{-1}$ makes $1+ax=0$, while every other term is $1$. Hence
$$
K(x,x)=\ell-2.
$$
If $x\ne y$, then
$$
(1+ax)(1+ay)=xy\,a^2+(x+y)a+1
$$
has discriminant $(x-y)^2\ne0$. Since $x,y\in H$, we have $\chi(xy)=1$, so the quadratic identity from Step 1 gives
$$
\sum_{a\in\mathbb F_{\ell}}\chi((1+ax)(1+ay))=-1.
$$
The term at $a=0$ is $1$, hence
$$
K(x,y)=-2\qquad(x\ne y).
$$
Therefore
$$
\begin{aligned}
\sum_{a\ne0}C_{+1}(a)^2
&=\sum_{x,y\in H}u_xu_yK(x,y)\\
&=(\ell-2)\sum_{x\in H}u_x^2-2\sum_{\substack{x,y\in H\\x\ne y}}u_xu_y.
\end{aligned}
$$
Because $u_x^2=1$, $|H|=r$, and $\sum_xu_x=S=-1$,
$$
\sum_{\substack{x,y\in H\\x\ne y}}u_xu_y=S^2-r=1-r.
$$
Thus
$$
\sum_{a\ne0}C_{+1}(a)^2=(\ell-2)r-2(1-r)=r\ell-2.
$$

Step 3: Evaluate the opposite-sign mixed moment.
For $x,y\in H$, define
$$
L(x,y)=\sum_{a\in\mathbb F_{\ell}^{\times}}\chi(1+ax)\chi(1-ay).
$$
The polynomial
$$
(1+ax)(1-ay)=-xy\,a^2+(x-y)a+1
$$
has discriminant $(x+y)^2$. This is nonzero: if $x+y=0$, then $y/x=-1$ would lie in $H$, contradicting $\chi(-1)=-1$. Its leading coefficient satisfies
$$
\chi(-xy)=\chi(-1)\chi(x)\chi(y)=-1.
$$
Hence the quadratic identity from Step 1 gives
$$
\sum_{a\in\mathbb F_{\ell}}\chi((1+ax)(1-ay))=1.
$$
Subtracting the $a=0$ term, which equals $1$, yields $L(x,y)=0$ for every $x,y\in H$. Therefore
$$
\sum_{a\ne0}C_{+1}(a)C_{-1}(a)
=\sum_{x,y\in H}u_xu_yL(x,y)=0.
$$
Combining the two moments gives the requested ordered pair.

Final Answer: $\boxed{\left(r\ell-2,0\right)}$

---

## Answer

$\left(r\ell-2,0\right)$

---

## Classification

**Problem Type:** Symbolic derivation

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- quadratic residues and Legendre symbols
- quadratic character sums
- character indicator expansions
- correlation moment expansion
