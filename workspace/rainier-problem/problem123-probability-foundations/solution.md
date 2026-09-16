## Steps

Step 1: Reduce exchangeability to a compact moment problem
By the Bernoulli de Finetti theorem, there is a random variable $\Theta\in[0,1]$ such that, conditional on $\Theta$, the variables $X_i$ are independent Bernoulli$(\Theta)$. Therefore
$$
\mathbb P(X_1=1)=\mathbb E\Theta,
$$
$$
\mathbb P(X_1=X_2=1)=\mathbb E\Theta^2,
$$
$$
\mathbb P(X_1=X_2=X_3=1)=\mathbb E\Theta^3.
$$
The constraints become
$$
m_1=\frac12,\qquad m_2=\frac13,\qquad m_3=\frac14,
$$
where $m_j=\mathbb E\Theta^j$, and
$$
\mathbb P(X_1+\cdots+X_6=2)=\mathbb E f(\Theta),
$$
with
$$
f(x)=15x^2(1-x)^4.
$$
Thus it remains to maximize $\mathbb E f(\Theta)$ over probability measures on $[0,1]$ with the displayed first three moments.

Step 2: Construct matching primal support and dual contact equations
A cubic polynomial $q$ satisfying $q\geq f$ on $[0,1]$ gives an upper bound because $\mathbb E q(\Theta)$ depends only on $m_0,m_1,m_2,m_3$. To build a primal-dual certificate, seek equality at an endpoint $0$ and at two interior points $0<a<b<1$, with the interior contacts doubled. Write
$$
S=a+b,\qquad P=ab,
$$
and set
$$
d(x)=q(x)-f(x)=-15x(x-a)^2(x-b)^2(x-r).
$$
This is a certificate ansatz rather than an assumption about every optimizer; once a feasible measure and a nonnegative $d$ are found, weak duality proves global optimality.

Since
$$
f(x)=15x^6-60x^5+90x^4-60x^3+15x^2,
$$
the top terms of $d$ are
$$
-15x^6+15(2S+r)x^5-15(S^2+2P+2Sr)x^4.
$$
For $q=f+d$ to have degree at most $3$, the $x^5$ and $x^4$ coefficients must vanish, so
$$
2S+r=4,
$$
$$
S^2+2P+2Sr=6.
$$
Hence
$$
r=4-2S,\qquad P=\frac{3S^2-8S+6}{2}.
$$

Now seek a probability measure supported on $\{0,a,b\}$ with the required moments. On this support,
$$
x^3=Sx^2-Px,
$$
so the third moment must satisfy
$$
\frac14=S\cdot\frac13-P\cdot\frac12.
$$
Thus
$$
P=\frac{2S}{3}-\frac12.
$$
Equating the two formulas for $P$ gives
$$
9S^2-28S+21=0.
$$
Therefore
$$
S=\frac{14\pm\sqrt7}{9}.
$$
The plus sign gives $r=4-2S<1$, which would make $d$ change sign on $[0,1]$. Hence the valid branch is
$$
S=\frac{14-\sqrt7}{9},
$$
$$
P=\frac{29-4\sqrt7}{54},\qquad r=\frac{8+2\sqrt7}{9}>1.
$$

Step 3: Verify the feasible extremal measure and the global dual bound
Let $a<b$ be the roots of
$$
t^2-St+P=0.
$$
Their discriminant is
$$
S^2-4P=\frac{29-4\sqrt7}{81}>0.
$$
Also
$$
\left(\frac23\right)^2-S\left(\frac23\right)+P=-\frac1{18}<0,
$$
while
$$
1-S+P=\frac{2\sqrt7-1}{54}>0.
$$
Since $S,P>0$, this proves
$$
0<a<\frac23<b<1.
$$
Define
$$
w_a=\frac{b/2-1/3}{a(b-a)},
$$
$$
w_b=\frac{1/3-a/2}{b(b-a)},
$$
and $w_0=1-w_a-w_b$. The inequalities above give $w_a,w_b>0$. Moreover,
$$
w_0P=\frac13-\frac S2+P=\frac{5-\sqrt7}{54}>0,
$$
so $w_0>0$. By construction the measure
$$
\mu_*=w_0\delta_0+w_a\delta_a+w_b\delta_b
$$
has first and second moments $1/2$ and $1/3$, and the recurrence $x^3=Sx^2-Px$ on its support gives its third moment as $1/4$. Thus $\mu_*$ is feasible.

For the chosen parameters,
$$
d(x)=-15x(x-a)^2(x-b)^2(x-r)\geq0\qquad(0\leq x\leq1),
$$
because $r>1$. Hence $q=f+d$ is a cubic majorant of $f$. Every feasible mixing law therefore satisfies
$$
\mathbb E f(\Theta)\leq\mathbb E q(\Theta).
$$
The right side is fixed by the first three moments. Since $d$ vanishes at $0,a,b$, the measure $\mu_*$ satisfies $\mathbb E_{\mu_*}f=\mathbb E_{\mu_*}q$. Therefore $\mu_*$ attains the global maximum.

Step 4: Evaluate the maximum exactly
For $\mu_*$, the support relation gives
$$
m_n=Sm_{n-1}-Pm_{n-2}\qquad(n\geq3).
$$
Using $m_1=1/2$, $m_2=1/3$, and $P=2S/3-1/2$, one obtains
$$
m_3=\frac14,
$$
$$
m_4=\frac{S+6}{36},
$$
$$
m_5=\frac{2S^2+9}{72},
$$
$$
m_6=\frac{3S^3-2S^2+3S+9}{108}.
$$
Therefore
$$
\max\mathbb P(X_1+\cdots+X_6=2)
=15\left(m_2-4m_3+6m_4-4m_5+m_6\right)
$$
$$
=\frac{5(3S^3-14S^2+21S-9)}{36}.
$$
Using $9S^2-28S+21=0$, this reduces to
$$
\frac{5(51-14S)}{972}.
$$
Substituting $S=(14-\sqrt7)/9$ gives
$$
\frac{1315+70\sqrt7}{8748}.
$$

Final Answer: $\boxed{\frac{1315+70\sqrt7}{8748}}$

---

## Answer

$\frac{1315+70\sqrt7}{8748}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

---

## Solution Concepts

- de Finetti theorem
- truncated moment problems
- polynomial dual certificates
- complementary slackness
- moment recurrences
