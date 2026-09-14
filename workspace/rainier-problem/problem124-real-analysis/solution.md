## Steps

Step 1: Bound the common positive and negative area
For $f\in\mathcal F$, absolute continuity and $|f'|\leq1$ almost everywhere give
$$
|f(y)-f(x)|\leq\int_x^y|f'(u)|\,du\leq y-x
$$
for $0\leq x<y\leq1$. Thus $f$ is $1$-Lipschitz. Define
$$
f_+=\max(f,0),\qquad f_-=\max(-f,0).
$$
Both are nonnegative $1$-Lipschitz functions that vanish at $0$ and $1$. Since $\int_0^1f=0$,
$$
A:=\int_0^1f_+(x)\,dx=\int_0^1f_-(x)\,dx.
$$

Write the components of $\{f_+>0\}$ as intervals $(a_i,b_i)$ of lengths $\ell_i=b_i-a_i$. Continuity gives $f_+(a_i)=f_+(b_i)=0$, so for $x\in(a_i,b_i)$ the Lipschitz bound implies
$$
f_+(x)\leq\min(x-a_i,b_i-x).
$$
Hence
$$
\int_{a_i}^{b_i}f_+(x)\,dx\leq\frac{\ell_i^2}{4}.
$$
If $L_+=|\{f>0\}|=\sum_i\ell_i$, then
$$
A\leq\frac14\sum_i\ell_i^2\leq\frac{L_+^2}{4},
$$
so $L_+\geq2\sqrt A$. The same argument for $f_-$ gives $L_-:=|\{f<0\}|\geq2\sqrt A$. The sets $\{f>0\}$ and $\{f<0\}$ are disjoint, hence
$$
4\sqrt A\leq L_++L_-\leq1,
$$
and therefore
$$
A\leq\frac1{16}.
$$

Step 2: Prove a sharp second-moment bound for one nonnegative Lipschitz cap
Let $g\geq0$ be $1$-Lipschitz on $[0,1]$, with $g(0)=g(1)=0$, and set
$$
a=\int_0^1g(x)\,dx,\qquad b=\int_0^1g(x)^2\,dx,\qquad M=\max_{[0,1]}g.
$$
If $M=0$, then $a=b=0$. Assume $M>0$, and for $0\leq t<M$ define
$$
E_t=\{x\in[0,1]:g(x)>t\},\qquad m(t)=|E_t|.
$$
For $0\leq s<t<M$, the set $E_t$ is nonempty. Let $\alpha=\inf E_t$ and $\beta=\sup E_t$. Continuity gives $g(\alpha)=g(\beta)=t$. Since $g(0)=g(1)=0$ and $g$ is $1$-Lipschitz, $\alpha\geq t$ and $1-\beta\geq t$. Moreover, every point within distance $t-s$ immediately to the left of $\alpha$ or to the right of $\beta$ has value greater than $s$. These two intervals are disjoint from $E_t$, so
$$
m(s)\geq m(t)+2(t-s).
$$
Thus $q(t)=m(t)+2t$ is nonincreasing. Put
$$
p=\lim_{t\uparrow M}m(t),\qquad e(t)=m(t)-p-2(M-t).
$$
Then $e(t)=q(t)-(p+2M)$ is nonnegative and nonincreasing.

Using
$$
g(x)=\int_0^M\mathbf 1_{\{g(x)>t\}}\,dt,
\qquad
g(x)^2=\int_0^M2t\mathbf 1_{\{g(x)>t\}}\,dt,
$$
and integrating first in $x$ gives
$$
a=\int_0^Mm(t)\,dt,
\qquad
b=\int_0^M2t\,m(t)\,dt.
$$
For nonincreasing $e$, one has
$$
\int_0^M\int_0^M(t-s)(e(t)-e(s))\,ds\,dt\leq0.
$$
Expanding the double integral yields
$$
2M\int_0^Mte(t)\,dt-M^2\int_0^Me(t)\,dt\leq0,
$$
so
$$
\int_0^Mte(t)\,dt\leq\frac M2\int_0^Me(t)\,dt.
$$
Let $E=\int_0^Me(t)\,dt$. Since $m(t)=p+2(M-t)+e(t)$,
$$
a=pM+M^2+E
$$
and
$$
\begin{aligned}
b&=pM^2+\frac23M^3+2\int_0^Mte(t)\,dt\\
&\leq pM^2+\frac23M^3+ME\\
&=Ma-\frac13M^3.
\end{aligned}
$$
Also $a\geq M^2$, hence $M\leq\sqrt a$. For fixed $a$, the function $aM-M^3/3$ has derivative $a-M^2\geq0$ on $0\leq M\leq\sqrt a$. Consequently
$$
b\leq a\sqrt a-\frac13a^{3/2}=\frac23a^{3/2}.
$$

Step 3: Apply the cap bound to the positive and negative parts
The functions $f_+$ and $f_-$ from Step 1 each satisfy the hypotheses of Step 2 and each has integral $A$. Therefore
$$
\int_0^1f(x)^2\,dx
=\int_0^1f_+(x)^2\,dx+\int_0^1f_-(x)^2\,dx
\leq\frac43A^{3/2}.
$$
Using $A\leq1/16$ from Step 1 gives
$$
\int_0^1f(x)^2\,dx
\leq\frac43\left(\frac1{16}\right)^{3/2}
=\frac1{48}.
$$
Thus $1/48$ is an upper bound for every admissible function.

Step 4: Construct an admissible function attaining the bound
Define
$$
f_*(x)=
\begin{cases}
x,&0\leq x\leq\frac14,\\
\frac12-x,&\frac14\leq x\leq\frac34,\\
x-1,&\frac34\leq x\leq1.
\end{cases}
$$
This function is absolutely continuous, satisfies $f_*(0)=f_*(1)=0$, and has $|f_*'|=1$ almost everywhere. It also obeys $f_*(1-x)=-f_*(x)$, so
$$
\int_0^1f_*(x)\,dx=0.
$$
Hence $f_*\in\mathcal F$. Its four quarter-interval pieces have the same squared profile, and therefore
$$
\int_0^1f_*(x)^2\,dx
=4\int_0^{1/4}x^2\,dx
=\frac1{48}.
$$
Together with the upper bound in Step 3, this proves that the maximum is attained and equals $1/48$.

Final Answer: $\boxed{\frac{1}{48}}$

---

## Answer

$\frac{1}{48}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

---

## Solution Concepts

- Lipschitz functions
- positive and negative parts
- layer-cake representation
- superlevel set geometry
- sharp integral inequalities
