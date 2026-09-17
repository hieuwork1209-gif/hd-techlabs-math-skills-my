# Normalized Math Problem

## LaTeX (Normalized)

Let \(0<\theta<1\). Let \((S_x)_{x\in\mathbb Z}\) be a two-sided stationary Markov chain with state space \(\{R,L\}\), stationary distribution
\[
\mathbb P(S_x=R)=\theta,
\qquad
\mathbb P(S_x=L)=1-\theta,
\]
and transition matrix
\[
P_\theta=
\begin{pmatrix}
\dfrac{1+4\theta}{5} & \dfrac{4(1-\theta)}5\\[2mm]
\dfrac{4\theta}5 & \dfrac{5-4\theta}{5}
\end{pmatrix}.
\]
Define the random environment
\[
\omega_x=
\begin{cases}
3/4,&S_x=R,\\
1/4,&S_x=L.
\end{cases}
\]
Conditioned on the environment \(\omega\), let \((X_n)_{n\ge0}\) be the nearest-neighbor random walk on \(\mathbb Z\), started at \(X_0=0\), with
\[
P_\omega(X_{n+1}=x+1\mid X_n=x)=\omega_x,
\]
\[
P_\omega(X_{n+1}=x-1\mid X_n=x)=1-\omega_x.
\]
Let \(\mathbb P_\theta\) denote the annealed law, averaging over both the stationary Markov environment and the walk.

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

Your derivation must distinguish the logarithmic criterion governing recurrence/transience from the correlation-sensitive moment criterion governing ballisticity. In particular, it must derive the relevant crossing-time product series for this Markov environment and reduce its annealed expectation to an explicit \(2\times2\) transfer-matrix series. Simply replacing the environment by its stationary averaged drift, or treating successive environment states as independent, is not sufficient.

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

The problem asks for the recurrence/transience and ballisticity phase diagram of a one-dimensional random walk in a stationary correlated random environment. The essential work is to separate the logarithmic potential criterion from the first-passage moment criterion, exploit reversibility of the two-state environment chain, convert correlated products of local odds into a transfer-matrix series, and determine the Perron-Frobenius threshold for nonzero speed. Thus Probability and Statistics -> Probability foundations is primary.
