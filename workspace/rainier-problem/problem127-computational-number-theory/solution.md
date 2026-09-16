## Steps

Step 1: Reduce the two congruences to a single unit equation
Let $M_n(p)$ be the number of ordered pairs $(x,y)\in(\mathbb Z/p^n\mathbb Z)^2$ satisfying
$$
x^2\equiv y^3\pmod{p^n},
\qquad
x+y\equiv2\pmod{p^n}.
$$
Because $p$ is odd, $2$ is a unit modulo $p$. Hence at least one of $x,y$ is a unit modulo $p$. The congruence $x^2\equiv y^3\pmod p$ then forces both to be units.

For a unit solution define
$$
z=y^2x^{-1}.
$$
Then
$$
z^2=y^4x^{-2}=y,
\qquad
z^3=y^6x^{-3}=x,
$$
using $x^2=y^3$ in the unit group. Conversely, every unit $z$ gives the cusp solution
$$
(x,y)=(z^3,z^2).
$$
Therefore the required pairs are in bijection with the roots modulo $p^n$ of
$$
f(z)=z^3+z^2-2.
$$
Since
$$
f(z)=(z-1)(z^2+2z+2)
=(z-1)\bigl((z+1)^2+1\bigr),
$$
the problem is now a root-lifting problem for this factored cubic.

Step 2: Count the roots when $p\ne5$
Modulo $p$, the root $z=1$ is always present. The quadratic factor has two roots exactly when $-1$ is a quadratic residue modulo $p$. Thus, writing
$$
L_p=\left(\frac{-1}{p}\right),
$$
the quadratic contributes $1+L_p$ roots.

When $p\ne5$, the linear root does not coincide with a quadratic root because
$$
1^2+2\cdot1+2=5\not\equiv0\pmod p.
$$
All these roots are simple. Indeed,
$$
f'(1)=5\not\equiv0\pmod p,
$$
and a root of the quadratic factor cannot satisfy
$$
2z+2\equiv0\pmod p,
$$
because $z\equiv-1$ would make the quadratic equal to $1$.

A simple root lifts uniquely through every higher power of $p$: if $r$ solves $f(r)\equiv0\pmod{p^m}$ and $f'(r)\not\equiv0\pmod p$, then among the $p$ candidates
$$
r+tp^m\qquad(t=0,\dots,p-1),
$$
Taylor expansion modulo $p^{m+1}$ gives
$$
f(r+tp^m)\equiv f(r)+tp^mf'(r)\pmod{p^{m+1}},
$$
so exactly one value of $t$ produces a root modulo $p^{m+1}$.

Hence for every $n\ge1$ and every odd prime $p\ne5$,
$$
M_n(p)=2+L_p.
$$

Step 3: Analyze the singular prime $p=5$
Modulo $5$,
$$
f(z)=(z-1)(z^2+2z+2)
$$
has exactly the two roots
$$
z\equiv1,2\pmod5.
$$
Thus
$$
M_1(5)=2.
$$

Put
$$
t=z-1.
$$
Then
$$
f(z)=t(t^2+4t+5).
$$
The class $t\equiv1\pmod5$, corresponding to $z\equiv2\pmod5$, is simple because
$$
2t+4\equiv1\pmod5.
$$
By the lifting calculation from Step 2, it contributes exactly one root modulo $5^n$ for every $n$.

Now consider the branch $t\equiv0\pmod5$. Write
$$
t=5u.
$$
Then
$$
f(z)=25u(5u^2+4u+1).
$$
For $n=2$, every $u\pmod5$ gives a root, so this branch contributes $5$ roots. Together with the simple branch,
$$
M_2(5)=6.
$$

Assume $n\ge3$ and set
$$
h(u)=5u^2+4u+1.
$$
The condition becomes
$$
5^{n-2}\mid u h(u).
$$
Modulo $5$,
$$
h(u)\equiv4u+1.
$$
Hence a solution must satisfy either
$$
u\equiv0\pmod5
$$
or
$$
u\equiv1\pmod5.
$$

If $u\equiv0\pmod5$, then $h(u)$ is a unit, so we need
$$
u\equiv0\pmod{5^{n-2}}.
$$
Among the residues modulo $5^{n-1}$ there are exactly $5$ such $u$.

If $u\equiv1\pmod5$, then $u$ is a unit and we need
$$
h(u)\equiv0\pmod{5^{n-2}}.
$$
Since
$$
h'(u)=10u+4\equiv4\pmod5,
$$
the same one-step lifting argument shows that the root $u\equiv1\pmod5$ has a unique lift modulo $5^{n-2}$. That single class has exactly $5$ representatives modulo $5^{n-1}$. Thus this branch also contributes $5$ roots.

Therefore the branch $t\equiv0\pmod5$ contributes $10$ roots for every $n\ge3$, and the simple branch contributes one more. Hence
$$
M_n(5)=11
\qquad(n\ge3).
$$

Step 4: Combine the cases
We have shown
$$
M_n(p)=
\begin{cases}
2,&p=5,\ n=1,\\
6,&p=5,\ n=2,\\
11,&p=5,\ n\ge3,\\
2+L_p,&p\ne5.
\end{cases}
$$

Final Answer: $\boxed{\begin{cases}2,&p=5,n=1\\6,&p=5,n=2\\11,&p=5,n\ge3\\2+L_p,&p\ne5.\end{cases}}$

---

## Answer

$\begin{cases}2,&p=5,n=1\\6,&p=5,n=2\\11,&p=5,n\ge3\\2+L_p,&p\ne5.\end{cases}$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- modular cusp parametrization
- simple root lifting
- quadratic residues
- singular prime analysis
- p-adic valuation counting
