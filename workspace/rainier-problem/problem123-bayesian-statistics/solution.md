## Steps

Step 1: Express the posterior predictive probability as a ratio of moments
Let $\Theta$ have prior law $\mu$ on $[0,1]$, and conditional on $\Theta=\theta$ let the observations be i.i.d. Bernoulli$(\theta)$. Write
$$
m_k=\mathbb E_\mu[\Theta^k].
$$
The calibration assumptions give
$$
m_1=\frac{1}{2},\qquad m_2=\frac{1}{3},\qquad m_3=\frac{1}{4}.
$$
After four observed successes, Bayes' rule weights the prior by $\theta^4$. Therefore the posterior predictive success probability is
$$
p_\mu=\frac{m_5}{m_4}.
$$
By Cauchy-Schwarz applied to $\Theta^2$ and $1$,
$$
m_4=\mathbb E[\Theta^4]\geq\mathbb E[\Theta^2]^2=m_2^2=\frac{1}{9},
$$
so the denominator is always positive.

Step 2: Derive the two canonical feasible priors and their candidate endpoint values
The fixed moments imply, for $Y=\Theta-\frac{1}{2}$,
$$
\mathbb E[Y]=0,\qquad \mathbb E[Y^2]=\frac{1}{12},\qquad \mathbb E[Y^3]=0.
$$
A symmetric two-point law matching these central moments is forced to place mass $\frac{1}{2}$ at
$$
a=\frac{1}{2}-\frac{1}{2\sqrt{3}},\qquad b=\frac{1}{2}+\frac{1}{2\sqrt{3}}.
$$
Call this prior $\mu_-$. Since $a,b$ are the roots of
$$
x^2-x+\frac{1}{6}=0,
$$
the power sums $s_k=a^k+b^k$ satisfy
$$
s_k=s_{k-1}-\frac{1}{6}s_{k-2},\qquad s_0=2,\quad s_1=1.
$$
Hence
$$
s_2=\frac{2}{3},\quad s_3=\frac{1}{2},\quad s_4=\frac{7}{18},\quad s_5=\frac{11}{36}.
$$
Thus $\mu_-$ has the required first three moments and
$$
m_4=\frac{7}{36},\qquad m_5=\frac{11}{72},\qquad p_{\mu_-}=\frac{11}{14}.
$$

A second symmetric law matching the same three central moments is obtained by using the endpoints and midpoint. If the endpoint masses are both $w$, the variance condition gives
$$
2w\left(\frac{1}{2}\right)^2=\frac{1}{12},
$$
so $w=\frac{1}{6}$. Therefore
$$
\mu_+=\frac{1}{6}\delta_0+\frac{2}{3}\delta_{1/2}+\frac{1}{6}\delta_1.
$$
It also satisfies the three calibration moments, and
$$
m_4=\frac{5}{24},\qquad m_5=\frac{3}{16},\qquad p_{\mu_+}=\frac{9}{10}.
$$
These give candidate lower and upper endpoints.

Step 3: Prove the sharp lower bound by a moment certificate
To prove $p_\mu\geq\frac{11}{14}$, it is enough to prove
$$
m_5-\frac{11}{14}m_4\geq0.
$$
Only moments through degree $3$ are fixed, so a useful certificate is a cubic polynomial whose expectation is determined by the calibration data. The candidate extremizer $\mu_-$ is supported at the two interior roots of $x^2-x+\frac{1}{6}$. Equality at an interior support point of a nonnegative pointwise gap must have even multiplicity, so require the gap to contain
$$
\left(x^2-x+\frac{1}{6}\right)^2.
$$
For
$$
g_-(x)=x^5-\frac{11}{14}x^4,
$$
matching the degree-$5$ and degree-$4$ coefficients forces
$$
g_-(x)-h_-(x)=\left(x^2-x+\frac{1}{6}\right)^2\left(x+\frac{17}{14}\right),
$$
where the remaining part is the cubic
$$
h_-(x)=\frac{23}{21}x^3-\frac{9}{7}x^2+\frac{95}{252}x-\frac{17}{504}.
$$
Equivalently,
$$
g_-(x)-h_-(x)=\frac{(14x+17)(6x^2-6x+1)^2}{504}\geq0
$$
for $0\leq x\leq1$. The expectation of the cubic is fixed and equals
$$
\mathbb E[h_-(\Theta)]
=\frac{23}{21}\frac{1}{4}-\frac{9}{7}\frac{1}{3}+\frac{95}{252}\frac{1}{2}-\frac{17}{504}
=0.
$$
Therefore
$$
m_5-\frac{11}{14}m_4=\mathbb E[g_-(\Theta)]\geq\mathbb E[h_-(\Theta)]=0.
$$
Thus $p_\mu\geq\frac{11}{14}$. Equality forces the nonnegative gap to vanish almost surely. Since $14x+17>0$ on $[0,1]$, the support must lie in the two roots of $6x^2-6x+1$, and the first moment then forces equal weights. Hence equality occurs exactly at $\mu_-$.

Step 4: Prove the sharp upper bound by the endpoint-midpoint certificate
To prove $p_\mu\leq\frac{9}{10}$, it is enough to prove
$$
m_5-\frac{9}{10}m_4\leq0.
$$
The candidate extremizer $\mu_+$ is supported at $0,\frac{1}{2},1$. Endpoint contacts may be simple, while the interior contact at $\frac{1}{2}$ must be double for a nonnegative pointwise majorant. Thus, for
$$
g_+(x)=x^5-\frac{9}{10}x^4,
$$
require the gap $h_+(x)-g_+(x)$ to contain $x(1-x)(2x-1)^2$. Matching the two highest coefficients determines the final linear factor and yields
$$
h_+(x)-g_+(x)
=\frac{x(1-x)(2x-1)^2(10x+11)}{40}\geq0
$$
for $0\leq x\leq1$, where
$$
h_+(x)=\frac{19}{20}x^3-\frac{9}{8}x^2+\frac{11}{40}x.
$$
The expectation of the cubic is fixed:
$$
\mathbb E[h_+(\Theta)]
=\frac{19}{20}\frac{1}{4}-\frac{9}{8}\frac{1}{3}+\frac{11}{40}\frac{1}{2}
=0.
$$
Hence
$$
m_5-\frac{9}{10}m_4=\mathbb E[g_+(\Theta)]\leq\mathbb E[h_+(\Theta)]=0,
$$
so $p_\mu\leq\frac{9}{10}$. Equality forces the support to lie in $\left\{0,\frac{1}{2},1\right\}$, and the first two moment equations uniquely give masses $\frac{1}{6},\frac{2}{3},\frac{1}{6}$. Thus equality occurs exactly at $\mu_+$.

Step 5: Show that every intermediate value is attainable
For $0\leq t\leq1$, let
$$
\mu_t=(1-t)\mu_-+t\mu_+.
$$
Each $\mu_t$ satisfies the same three calibration moments. Its posterior predictive probability is
$$
p_{\mu_t}
=\frac{(1-t)m_5^-+tm_5^+}{(1-t)m_4^-+tm_4^+},
$$
whose denominator is positive. This is continuous in $t$, with endpoint values
$$
p_{\mu_0}=\frac{11}{14},\qquad p_{\mu_1}=\frac{9}{10}.
$$
Therefore every value between the two sharp endpoints is attained.

Final Answer: $\boxed{[\frac{11}{14},\frac{9}{10}]}$

---

## Answer

$[\frac{11}{14},\frac{9}{10}]$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Interval or region description

---

## Solution Concepts

- posterior predictive distributions
- truncated moment problems
- polynomial dual certificates
- extremal atomic priors
- sharp moment inequalities
