# Normalized Math Problem

## LaTeX (Normalized)

An urn initially contains one red ball and one blue ball. At each step, one ball is drawn uniformly from the urn and replaced. Then:

- if the drawn ball is red, add one red ball and one blue ball;
- if the drawn ball is blue, add two blue balls.

Let $R_n$ be the number of red balls after $n$ draws. For each integer $m\ge2$, define the first hitting time
$$
\tau_m=\inf\{n\ge0:R_n=m\}.
$$
For $t\ge0$, determine exactly
$$
\lim_{m\to\infty}
E\exp\!\left(-t\frac{m^2}{\tau_m}\right).
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Probability and Statistics |
| **Sub-domain** | Stochastic processes |
| **Problem Type** | Symbolic derivation |
| **Answer Type** | Exact symbolic expression |

---

## Domain Explanation

The requested quantity is a scaling limit of first hitting times for a reinforced urn Markov process, so the primary mathematics is stochastic processes. Martingale normalization and moment calculations are tools used to identify the process limit and invert it at the stopping times.
