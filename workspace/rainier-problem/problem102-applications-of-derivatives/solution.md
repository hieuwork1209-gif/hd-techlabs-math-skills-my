## Steps

Step 1: Pass to logarithmic coordinates and resolve the branch signs

Let
$$
g(s)=f(e^s),\qquad H(s)=\int_0^s g(u)\,du,\qquad a(s)=A(e^s)=\frac{H(s)}{s}.
$$
The improper integral assumption makes $H$ finite, while concavity makes $g$ continuous on $(0,\infty)$. Hence $a$ is continuous. The two hypotheses become
$$
\bigl(a(2s)-a(s)\bigr)^2=(\log2)^2,
\qquad
\bigl(a(3s)-a(s)\bigr)^2=(\log3)^2.
$$
Each difference is continuous and takes values only in a two-point set, so on the connected interval $(0,\infty)$ its sign is constant. Thus there are $\varepsilon_2,\varepsilon_3\in\{-1,1\}$ such that
$$
a(2s)-a(s)=\varepsilon_2\log2,
\qquad
a(3s)-a(s)=\varepsilon_3\log3.
$$

Step 2: Couple the two scales to force a single slope

Set $B(u)=a(e^u)$. Then
$$
B(u+\log2)-B(u)=\varepsilon_2\log2,
\qquad
B(u+\log3)-B(u)=\varepsilon_3\log3.
$$
Define
$$
C(u)=B(u)-\varepsilon_2u.
$$
The first relation makes $C$ periodic with period $\log2$, hence bounded. The second gives
$$
C(u+\log3)-C(u)=(\varepsilon_3-\varepsilon_2)\log3.
$$
Iterating this identity would make $C$ unbounded unless $\varepsilon_3=\varepsilon_2$. Therefore
$$
\varepsilon_2=\varepsilon_3=: \varepsilon.
$$
Now $C(u)=B(u)-\varepsilon u$ has both periods $\log2$ and $\log3$. Since $\log2/\log3$ is irrational, integer combinations of these periods are dense in $\mathbb R$. By continuity, $C$ is constant. Hence
$$
B(u)=\varepsilon u+c,
$$
so
$$
a(s)=\varepsilon\log s+c.
$$
The normalization $A(e)=a(1)=-9$ gives $c=-9$.

Step 3: Recover the candidate functions

Since $H(s)=sa(s)$,
$$
H(s)=s(\varepsilon\log s-9).
$$
Differentiating gives
$$
g(s)=H'(s)=\varepsilon\log s+\varepsilon-9.
$$
Thus the two algebraically possible branches are
$$
g(s)=\log s-8
$$
and
$$
g(s)=-\log s-10.
$$

Step 4: Use concavity to select the unique branch and verify it

For the general branch,
$$
g''(s)=-\frac{\varepsilon}{s^2}.
$$
Concavity requires $g''(s)\le0$, so necessarily $\varepsilon=1$. Therefore
$$
g(s)=\log s-8.
$$
The improper integral converges because $\int_0^s\log u\,du$ is finite. Also
$$
H(s)=s\log s-9s,
\qquad
a(s)=\log s-9,
$$
so $a(1)=-9$, while
$$
a(2s)-a(s)=\log2,
\qquad
a(3s)-a(s)=\log3,
$$
which verifies both squared relations. Returning to $s=\log x$ yields the required function.

Final Answer: $\boxed{f(x)=\log(\log x)-8}$

---

## Answer

$f(x)=\log(\log x)-8$

---

## Classification

**Problem Type:** Solve for unknowns

**Answer Type:** Function or mapping

---

## Solution Concepts

- concavity and branch selection
- incommensurate periods
- logarithmic coordinate changes
- differentiation of integral means
