# Normalized Math Problem

## LaTeX (Normalized)

Let $\mathcal F$ be the class of all absolutely continuous functions $f:[0,1]\to\mathbb R$ such that
$$
f(0)=f(1)=0,\qquad |f'(x)|\leq1\ \text{for almost every }x\in[0,1],
$$
and the two local cancellation conditions
$$
\int_0^{1/3}f(x)\,dx=0,\qquad \int_{1/3}^1f(x)\,dx=0.
$$
Determine exactly
$$
\max_{f\in\mathcal F}\int_0^1 f(x)^2\,dx.
$$
A complete proof must also classify all equality cases.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Analysis |
| **Sub-domain** | Real analysis |
| **Problem Type** | Optimization |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

The problem asks for a sharp integral inequality for absolutely continuous Lipschitz functions under two local cancellation constraints, with a complete classification of equality. The main work is the real-variable geometry of positive and negative level sets and sharp endpoint-sensitive integral estimates, so Analysis and Real analysis are the direct classification. Optimization supplies only the extremal framing and is subordinate to the real-analysis argument.
