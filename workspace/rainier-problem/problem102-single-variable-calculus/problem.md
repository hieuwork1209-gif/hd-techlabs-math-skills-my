# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
\mathbb F=\mathbb F_{2^{11}},
$$
and let
$$
\operatorname{Tr}(a)=a+a^2+a^{2^2}+\cdots+a^{2^{10}}\in\mathbb F_2
$$
be the absolute trace. Evaluate exactly
$$
K=\sum_{x\in\mathbb F^\times}(-1)^{\operatorname{Tr}(x+x^{-1})}.
$$
For grading, write the final answer as $K=\cdots$.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Number Theory |
| **Sub-domain** | Modular arithmetic and congruences |
| **Problem Type** | Exact computation |
| **Answer Type** | Exact symbolic expression |

---

## Domain Explanation

The problem asks for an exact binary Kloosterman character sum over a finite field. The trace condition converts the sum into the point count of an elliptic curve over $\mathbb F_{2^{11}}$, and the required exact value follows from the Frobenius recurrence determined by the curve over $\mathbb F_2$. The essential arithmetic is finite-field and characteristic-two in nature, so the closest available classification is Number Theory with sub-domain Modular arithmetic and congruences.
