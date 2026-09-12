# Normalized Math Problem

## LaTeX (Normalized)

Let $\Theta$ have an arbitrary Borel prior probability measure $\mu$ on $[0,1]$. Conditional on $\Theta=\theta$, let $X_1,X_2,\ldots$ be i.i.d. Bernoulli$(\theta)$.

Assume
$$
\mathbb P(X_1=1)=\frac{1}{2},\qquad
\mathbb P(X_1=X_2=1)=\frac{1}{3},\qquad
\mathbb P(X_1=X_2=X_3=1)=\frac{1}{4},
$$
and
$$
\mathbb P(X_1=X_2=X_3=X_4=1)=r,
$$
where at least one prior satisfying these four conditions exists.

After observing $X_1=X_2=X_3=X_4=1$, define
$$
p_\mu=\mathbb P(X_5=1\mid X_1=X_2=X_3=X_4=1).
$$
Determine exactly, in terms of $r$, the set of possible values of $p_\mu$ over all such priors.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Probability and Statistics |
| **Sub-domain** | Bayesian statistics |
| **Problem Type** | Optimization |
| **Answer Type** | Interval or region description |

---

## Domain Explanation

The problem asks for a sharp posterior-predictive range under prior-predictive calibration of a Bernoulli model. The unknown object is the prior distribution, and the additional fourth-order calibration parameter constrains the posterior predictive probability, so Bayesian statistics is the natural classification.
