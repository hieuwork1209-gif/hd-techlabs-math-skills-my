# Draft Solution

Let $f_+=\max(f,0)$ and $f_-=\max(-f,0)$. Since $f$ is absolutely continuous and $|f'|\leq1$ almost everywhere, $f$ is $1$-Lipschitz, hence so are $f_+$ and $f_-$. The mean-zero condition gives
$$
A:=\int_0^1f_+(x)\,dx=\int_0^1f_-(x)\,dx.
$$

If $(a_i,b_i)$ is a component of $\{f_+>0\}$ and $\ell_i=b_i-a_i$, then $f_+(a_i)=f_+(b_i)=0$ and the Lipschitz bound gives
$$
f_+(x)\leq\min(x-a_i,b_i-x).
$$
Thus the positive area on this component is at most $\ell_i^2/4$. If $L_+=|\{f>0\}|=\sum_i\ell_i$, then
$$
A\leq\frac14\sum_i\ell_i^2\leq\frac{L_+^2}{4},
$$
so $L_+\geq2\sqrt A$. The same argument gives $L_-:=|\{f<0\}|\geq2\sqrt A$. Since the positive and negative sets are disjoint, $L_++L_-\leq1$, hence $A\leq1/16$.

We also need a sharp moment estimate. Let $g\geq0$ be $1$-Lipschitz on $[0,1]$, with $g(0)=g(1)=0$, and write
$$
a=\int_0^1g(x)\,dx,\qquad b=\int_0^1g(x)^2\,dx,\qquad M=\max g.
$$
For $0\leq t<M$ let $m(t)=|\{g>t\}|$. For $0\leq s<t<M$, the left and right extreme points of $\{g>t\}$ have value $t$. The $1$-Lipschitz condition forces intervals of length $t-s$ immediately outside those two extremes to lie in $\{g>s\}$. Therefore
$$
m(s)\geq m(t)+2(t-s),
$$
so $q(t)=m(t)+2t$ is nonincreasing. Put
$$
p=\lim_{t\uparrow M}m(t),\qquad e(t)=m(t)-p-2(M-t).
$$
Then $e\geq0$ and $e$ is nonincreasing. Layer-cake integration gives
$$
a=\int_0^Mm(t)\,dt,
\qquad
b=\int_0^M2t\,m(t)\,dt.
$$
For a nonincreasing $e$, the elementary opposite-monotonicity estimate
$$
\int_0^M t e(t)\,dt\leq\frac M2\int_0^M e(t)\,dt
$$
follows by expanding
$$
\int_0^M\int_0^M(t-s)(e(t)-e(s))\,ds\,dt\leq0.
$$
Writing $E=\int_0^Me(t)\,dt$, we obtain
$$
a=pM+M^2+E
$$
and
$$
\begin{aligned}
b&=pM^2+\frac23M^3+2\int_0^Mt e(t)\,dt\\
&\leq pM^2+\frac23M^3+ME\\
&=Ma-\frac13M^3.
\end{aligned}
$$
Since $a\geq M^2$, one has $M\leq\sqrt a$, and $Ma-M^3/3$ is increasing for $0\leq M\leq\sqrt a$. Consequently
$$
b\leq\frac23a^{3/2}.
$$

Applying this estimate to $f_+$ and $f_-$ yields
$$
\int_0^1f(x)^2\,dx
=\int_0^1f_+(x)^2\,dx+\int_0^1f_-(x)^2\,dx
\leq\frac43A^{3/2}
\leq\frac43\left(\frac1{16}\right)^{3/2}
=\frac1{48}.
$$

Equality is attained by
$$
f_*(x)=
\begin{cases}
x,&0\leq x\leq\frac14,\\
\frac12-x,&\frac14\leq x\leq\frac34,\\
x-1,&\frac34\leq x\leq1.
\end{cases}
$$
It is absolutely continuous, has $f_*(0)=f_*(1)=0$, satisfies $|f_*'|=1$ almost everywhere, and obeys $f_*(1-x)=-f_*(x)$, so its integral is zero. Finally,
$$
\int_0^1f_*(x)^2\,dx
=4\int_0^{1/4}x^2\,dx
=\frac1{48}.
$$
Thus the supremum is $1/48$ and is attained.
