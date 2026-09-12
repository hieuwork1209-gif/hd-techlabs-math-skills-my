# Normalized Math Problem

## LaTeX (Normalized)

Let $\Theta$ be an unknown Bernoulli success parameter with an arbitrary Borel prior probability measure $\mu$ on $[0,1]$. Conditional on $\Theta=\theta$, let $X_1,X_2,\ldots$ be i.i.d. Bernoulli$(\theta)$.

Assume the prior predictive calibration
$$
\mathbb P(X_1=1)=\frac12,
$$
$$
\mathbb P(X_1=X_2=1)=\frac13,
$$
and
$$
\mathbb P(X_1=X_2=X_3=1)=\frac14.
$$
After observing four successes $X_1=X_2=X_3=X_4=1$, define
$$
p_\mu=\mathbb P(X_5=1\mid X_1=X_2=X_3=X_4=1).
$$
As $\mu$ ranges over all priors satisfying the three calibration conditions, determine exactly the set of possible values of $p_\mu$.

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

The problem asks for a sharp posterior-predictive range under partial prior-predictive calibration. The unknown object is the prior distribution on a Bernoulli parameter, and the requested quantity is a posterior predictive probability after observed data, so Bayesian statistics is the natural classification.
