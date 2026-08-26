# Normalized Math Problem

## LaTeX (Normalized)

All logarithms are natural. Let $f:(1,\infty)\to\mathbb R$, and assume that the improper integral below converges for every $x>1$. Suppose that the function $s\mapsto f(e^s)$ is concave on $(0,\infty)$. Define
$$
A(x)=\frac{1}{\log x}\int_1^x\frac{f(t)}{t}\,dt.
$$
Assume that $A(e)=-9$ and that, for every $x>1$,
$$
\bigl(A(x^2)-A(x)\bigr)^2=(\log 2)^2,
\qquad
\bigl(A(x^3)-A(x)\bigr)^2=(\log 3)^2.
$$
Determine $f(x)$ for all $x>1$.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Calculus |
| **Sub-domain** | Applications of derivatives |
| **Problem Type** | Solve for unknowns |
| **Answer Type** | Function or mapping |

---

## Domain Explanation

The problem uses concavity to select the only admissible branch after two scale relations are resolved, and it recovers the unknown function by differentiating its logarithmic-coordinate integral mean. The decisive rigidity comes from combining the two multiplicative scales with the derivative-based concavity condition, so Applications of derivatives is the primary sub-domain.