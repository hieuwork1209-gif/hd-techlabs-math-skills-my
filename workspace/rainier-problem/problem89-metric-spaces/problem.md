# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
E=\{x\in\mathbb F_2^8:\operatorname{wt}(x)\text{ is even}\},
\qquad \mathbf1=(1,\ldots,1),
$$
and let $Y=E\cup\{\ast\}$. Define $d$ on $Y$ as follows. For distinct $x,y\in E$,
$$
d(x,y)=
\begin{cases}
24,&x+y=\mathbf1,\\
20,&x+y\ne\mathbf1,
\end{cases}
$$
while
$$
d(\ast,x)=
\begin{cases}
13,&\operatorname{wt}(x)\equiv0\pmod4,\\
15,&\operatorname{wt}(x)\equiv2\pmod4,
\end{cases}
\qquad d(\ast,\ast)=0.
$$
(These values define a metric on $Y$.)

For $p>0$, say that $(Y,d)$ has $p$-negative type if, for every family of real numbers $(a_z)_{z\in Y}$ with $\sum_{z\in Y}a_z=0$,
$$
\sum_{z,w\in Y}a_za_w\,d(z,w)^p\le0.
$$
Determine
$$
\wp=\sup\{p>0:(Y,d)\text{ has }p\text{-negative type}\}.
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Analysis |
| **Sub-domain** | Metric spaces |
| **Problem Type** | Exact computation |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

The target $\wp$ is the supremal negative-type exponent of a finite metric space, so the core question is conditional negative definiteness of powers of the metric. The binary-vector description supplies a compact antipodal symmetry and a two-radius one-point extension, but the object being determined is intrinsically a metric-space invariant rather than a coding-theory or finite-group classification.