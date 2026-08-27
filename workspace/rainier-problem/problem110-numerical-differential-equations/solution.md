## Steps

Step 1: Reduce boundedness to coefficient inequalities

For fixed $s$, write
$$
A_s=1+B_s-s(1-s),
\qquad
p_s(r)=r^{2}-A_s r+B_s.
$$
Every solution of the recurrence is bounded for every starting pair exactly when both roots of $p_s$ lie in the closed unit disk and every unit-modulus root is simple. This follows from the terms $r^{m}$ for a simple root and $m r^{m}$ for a repeated root.

Since $p_s$ is real and monic, the closed Jury criterion puts both roots in the closed unit disk exactly when
$$
1-A_s+B_s\geq0,
\qquad
1+A_s+B_s\geq0,
\qquad
1-B_s\geq0.
$$
For real roots, the first two left sides are $(1-r_1)(1-r_2)$ and $(1+r_1)(1+r_2)$; for nonreal roots, $B_s$ is their squared modulus. The same argument covers the non-strict boundary cases.

Here the three left sides are
$$
s(1-s),
\qquad
2+2B_s-s(1-s),
\qquad
1-B_s.
$$
So the closed-disk condition for every $s\in[0,1]$ is equivalent to
$$
-1+\frac{1}{2}s(1-s)\leq B_s\leq1
\qquad(0\leq s\leq1).
$$

Step 2: Derive the exact quadratic envelopes

For real $x,c$, consider
$$
xs+cs(1-s)\leq1
\qquad(0\leq s\leq1).
$$
The endpoint $s=1$ requires $x\leq1$. Under this condition, put $v=\sqrt{1-x}$. For $0<s<1$, the inequality is equivalent to
$$
c\leq\frac{1-xs}{s(1-s)}=\frac{1}{s}+\frac{v^{2}}{1-s}.
$$
The exact gap identity
$$
\frac{1}{s}+\frac{v^{2}}{1-s}-(1+v)^{2}
=\frac{((1+v)s-1)^{2}}{s(1-s)}
$$
shows that the infimum is $(1+v)^{2}$. It is attained at $s=\frac{1}{1+v}$ when $v>0$ and approached as $s\to1$ when $v=0$. So
$$
xs+cs(1-s)\leq1\quad(0\leq s\leq1)
$$
holds exactly when
$$
x\leq1,
\qquad
c\leq(1+\sqrt{1-x})^{2}.
$$

Apply this envelope to $B_s=as+bs(1-s)\leq1$. It gives
$$
a\leq1,
\qquad
b\leq(1+\sqrt{1-a})^{2}.
$$
The lower stability inequality from Step 1 is equivalent to
$$
(-a)s+\left(\frac{1}{2}-b\right)s(1-s)\leq1.
$$
The same envelope with $x=-a$ and $c=\frac{1}{2}-b$ gives
$$
a\geq-1,
\qquad
b\geq\frac{1}{2}-(1+\sqrt{1+a})^{2}.
$$
So every characteristic root lies in the closed unit disk for every $s\in[0,1]$ exactly on
$$
-1\leq a\leq1,
\qquad
\frac{1}{2}-(1+\sqrt{1+a})^{2}\leq b\leq(1+\sqrt{1-a})^{2}.
$$

Step 3: Remove the defective unit-root edge

A repeated unit root of a real quadratic must be $1$ or $-1$. If $1$ is a root, then $p_s(1)=s(1-s)=0$, so $s=0$ or $s=1$. At $s=0$,
$$
p_0(r)=r(r-1),
$$
whose roots are simple. At $s=1$, since $B_1=a$,
$$
p_1(r)=(r-1)(r-a).
$$
The root $1$ is repeated exactly when $a=1$; the recurrence then has solutions containing the unbounded term $m$.

A repeated root $-1$ would require $B_s=1$ and $A_s=-2$. But $B_s=1$ gives
$$
A_s=2-s(1-s)\geq\frac{7}{4},
$$
so this case is impossible. The closed region from Step 2 loses precisely the edge $a=1$. Every remaining unit-circle root is simple.

Final Answer: $\boxed{\{(a,b):-1\leq a<1,\frac{1}{2}-(1+\sqrt{1+a})^{2}\leq b\leq(1+\sqrt{1-a})^{2}\}}$

---

## Answer

$\{(a,b):-1\leq a<1,\frac{1}{2}-(1+\sqrt{1+a})^{2}\leq b\leq(1+\sqrt{1-a})^{2}\}$

---

## Classification

**Problem Type:** Exhaustive enumeration

**Answer Type:** Interval or region description

---

## Solution Concepts

- quadratic root condition
- uniform stability envelope
- repeated unit root

---

## Black-Box Audit

No issues found.
