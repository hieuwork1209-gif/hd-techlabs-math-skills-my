# Normalized Math Problem

## LaTeX (Normalized)

Let \(0<\theta<1\). Let \((\omega_x)_{x\in\mathbb Z}\) be an i.i.d. random environment with
\[
\mathbb P(\omega_x=3/4)=\theta,
\qquad
\mathbb P(\omega_x=1/4)=1-\theta.
\]
Conditioned on the environment \(\omega\), let \((X_n)_{n\ge0}\) be the nearest-neighbor random walk on \(\mathbb Z\), started at \(X_0=0\), with
\[
P_\omega(X_{n+1}=x+1\mid X_n=x)=\omega_x,
\]
\[
P_\omega(X_{n+1}=x-1\mid X_n=x)=1-\omega_x.
\]
Let \(\mathbb P_\theta\) denote the annealed law, averaging over both the environment and the walk.

Determine exactly, as a function of \(\theta\):

1. whether the walk is recurrent, transient to \(+\infty\), or transient to \(-\infty\);
2. the almost-sure annealed limiting velocity
   \[
   v(\theta)=\lim_{n\to\infty}\frac{X_n}{n};
   \]
3. all parameter values for which the walk is transient but has zero limiting speed;
4. the exact parameter ranges in which the annealed first-passage means
   \[
   \mathbb E_\theta T_1,
   \qquad
   T_1=\inf\{n\ge0:X_n=1\},
   \]
   and
   \[
   \mathbb E_\theta T_{-1},
   \qquad
   T_{-1}=\inf\{n\ge0:X_n=-1\},
   \]
   are finite, together with their exact values when finite.

Your derivation must distinguish the logarithmic criterion governing recurrence/transience from the moment criterion governing ballisticity. In particular, it must derive the relevant one-dimensional crossing-time product series; simply replacing the environment by its averaged drift is not sufficient.

Return the three exact transition parameters
\[
(\theta_-,\theta_{\rm dir},\theta_+)
\]
and the exact piecewise formula for \(v(\theta)\).

---

## Domain Classification

| Field | Value |
|---|---|
| Domain | Probability and Statistics |
| Sub-domain | Probability foundations |
| Problem Type | Exact computation |
| Answer Type | Tuple or ordered list |

---

## Domain Explanation

The problem asks for the recurrence/transience and ballisticity phase diagram of a one-dimensional random walk in an i.i.d. random environment. The essential probabilistic work is to distinguish the logarithmic potential criterion from the crossing-time moment criterion, derive the first-passage series in the random environment, and obtain the almost-sure limiting velocity. Thus Probability and Statistics -> Probability foundations is primary.
