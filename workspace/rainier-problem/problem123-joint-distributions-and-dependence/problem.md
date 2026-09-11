# Normalized Math Problem

## LaTeX (Normalized)

Fix $a>0$. Let
$$
(P_1,P_2,P_3,P_4)\sim\operatorname{Dirichlet}(a,1,1,1),
$$
so, writing $P_4=1-P_1-P_2-P_3$, the density of $(P_1,P_2,P_3)$ on
$$
P_j>0,
\qquad
P_1+P_2+P_3<1,
$$
is
$$
\frac{\Gamma(a+3)}{\Gamma(a)}P_1^{a-1}.
$$
Conditional on $(P_1,P_2,P_3,P_4)$, let $(X_i)_{i\ge1}$ and $(Y_i)_{i\ge1}$ be independent iid sequences taking values in $\{1,2,3\}$ with
$$
\begin{aligned}
P(X_i=1\mid P)&=P_1,&
P(X_i=2\mid P)&=P_2,&
P(X_i=3\mid P)&=P_3+P_4,\\
P(Y_i=1\mid P)&=P_1,&
P(Y_i=2\mid P)&=P_3,&
P(Y_i=3\mid P)&=P_2+P_4.
\end{aligned}
$$
Using natural logarithms, determine the exact function of $a$
$$
\lim_{n\to\infty}\left[
I\bigl((X_1,\ldots,X_n);(Y_1,\ldots,Y_n)\bigr)
-\frac12\log n
\right].
$$
You may use
$$
B(x,y)=\frac{\Gamma(x)\Gamma(y)}{\Gamma(x+y)},
\qquad
\psi(x)=\frac{\Gamma'(x)}{\Gamma(x)}.
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Probability and Statistics |
| **Sub-domain** | Joint distributions and dependence |
| **Problem Type** | Symbolic derivation |
| **Answer Type** | Exact symbolic expression |

---

## Domain Explanation

The requested object is the asymptotic mutual information between two dependent categorical sample blocks obtained from different coarsenings of the same random probability vector, so the primary mathematics is joint distributions and dependence. Dirichlet reparameterization and Beta-posterior asymptotics are auxiliary tools used to evaluate that dependence functional.
