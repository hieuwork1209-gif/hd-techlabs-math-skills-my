## Steps

Step 1: Reduce the representation problem to horizontal two-strip chains
Let $U=\mathbf{1}\oplus V_m$, the permutation module of $S_m$ on the $m$ matched pairs, inflated to $H_m$. The ordered triples of pair-indices have four orbit types: all three equal, one of the three possible choices of an equal pair, or all three distinct. With
$$
T_1=h_2h_{m-1}[h_2],\qquad T_2=h_2^2h_{m-2}[h_2],\qquad T_3=h_2^3h_{m-3}[h_2],
$$
we have
$$
\operatorname{ch}\operatorname{Ind}_{H_m}^{S_{2m}}U^{\otimes3}=T_1+3T_2+T_3,
$$
while the tensor-square and tensor-first-power analogues are $T_1+T_2$ and $T_1$. Since $V_m=U-\mathbf{1}$ in the representation ring,
$$
\operatorname{ch}M_m=(T_1+3T_2+T_3)-3(T_1+T_2)+3T_1-h_m[h_2]
=T_3+T_1-h_m[h_2].
$$

For every $r\geq0$, the Littlewood decomposition is
$$
h_r[h_2]=\sum_{\alpha\vdash r}s_{2\alpha},
\qquad
2\alpha=(2\alpha_1,2\alpha_2,\ldots).
$$
Thus the coefficient of $s_\mu$ in $h_r[h_2]$ is $1$ exactly when every row length of $\mu$ is even: such a $\mu$ has the unique form $\mu=2\alpha$. In particular, $P_m$ is multiplicity-free on the even-row partitions. Tensoring a Specht module by sign conjugates its diagram,
$$
S^\mu\otimes\operatorname{sgn}\cong S^{\mu'},
$$
so a partition $\lambda$ occurs in both $P_m$ and $N_m$ exactly when both its rows and its columns have even lengths. If all column lengths are even, then the number of rows of each fixed length $j$ is
$$
\lambda'_j-\lambda'_{j+1},
$$
hence is even. Combining this with the even-row condition lets us pair equal rows and divide their lengths by $2$. Therefore every admissible partition has the unique form
$$
\lambda=\Lambda(\delta):=(2\delta_1,2\delta_1,2\delta_2,2\delta_2,\ldots),\qquad \delta\vdash n:=\frac{m}{2},
$$
and conversely every such partition has even rows and columns. Also $\Lambda(\delta)'=\Lambda(\delta')$.

For $k\geq0$, let $c_k(\lambda)$ be the coefficient of $s_\lambda$ in $h_2^kh_{m-k}[h_2]$. Applying Littlewood with $r=m-k$ gives
$$
h_{m-k}[h_2]=\sum_{\alpha\vdash m-k}s_{2\alpha}.
$$
Pieri's rule in the needed case is
$$
s_\mu h_2=
\sum_{\substack{\nu\supseteq\mu\\ \nu/\mu\text{ a horizontal }2\text{-strip}}}s_\nu,
$$
with coefficient $1$ for every allowed $\nu$. Repeating it $k$ times shows that $c_k(\lambda)$ is the number of chains
$$
2\alpha=\mu_0\subset\mu_1\subset\cdots\subset\mu_k=\lambda
$$
in which every $\mu_j/\mu_{j-1}$ is a horizontal $2$-strip. Reversing the chain, $c_k(\lambda)$ therefore counts the successive horizontal $2$-strip removals from $\lambda$ that end at an even-row partition. Hence
$$
a_\lambda=c_3(\lambda)+c_1(\lambda)-1.
$$

Step 2: Count the three-strip chains for an admissible partition
Write the distinct parts of $\delta$ as
$$
q_1>q_2>\cdots>q_t>0
$$
with multiplicities $r_1,\ldots,r_t$, set $q_{t+1}=0$, and put $g_i=q_i-q_{i+1}$. Define
$$
G=\#\{i:g_i\geq2\},\qquad H=\#\{i:g_i\geq3\},\qquad M=\#\{i:r_i\geq2\}.
$$
There are $t$ removable row ends that can lose two boxes and leave every row even, so $c_1(\Lambda(\delta))=t$.

Call a strip of type A if both boxes are removed from one row, and type B if one box is removed from each of two rows. A type A strip preserves all row parities, while a type B strip flips exactly two. Since the initial and final row lengths are even, the only possible three-step type patterns are AAA, ABB, BBA, BAB, and BBB.

For the AAA count, divide all row lengths by $2$. The resulting partition is
$$
\beta=(q_1^{\,2r_1},q_2^{\,2r_2},\ldots,q_t^{\,2r_t}),
$$
and an A-removal is exactly an ordinary corner removal from $\beta$. Put
$$
a_i=\mathbf{1}_{\{g_i\geq2\}},\qquad
h_i=\mathbf{1}_{\{g_i\geq3\}},\qquad
m_i=\mathbf{1}_{\{r_i\geq2\}}.
$$
Initially $\beta$ has $t$ distinct row lengths and hence $t$ corners. Fix the first removal at run $i$. Since its multiplicity is $2r_i\geq2$, the old $q_i$-run remains. The shortened row either merges with the next run when $g_i=1$, or forms a new run when $g_i\geq2$. Thus the number of corners after the first move is
$$
T_i=t+a_i.
$$

For any partition with $T$ runs, removing the corner of a run changes the next corner count by
$$
\mathbf{1}_{\{\text{gap below}\geq2\}}
-\mathbf{1}_{\{\text{run multiplicity}=1\}}:
$$
the first indicator records creation of a new intermediate row length, while the second records disappearance of the old row length. After the first move at $i$, the number of gaps at least $2$ is
$$
A_i=G-a_i+h_i.
$$
Indeed, if $a_i=0$ no qualifying gap changes; if $a_i=1$, the old gap $g_i$ is replaced by gaps $1$ and $g_i-1$, and the latter is at least $2$ exactly when $g_i\geq3$. The number of singleton runs is
$$
B_i=1-m_i+a_i.
$$
Here the surviving $q_i$-run has multiplicity $2r_i-1$, which is $1$ exactly when $r_i=1$, and when $a_i=1$ the new $(q_i-1)$-run is another singleton.

There are $T_i$ choices for the second A-removal. Summing the number of third corners over those choices gives
$$
T_i^2+A_i-B_i.
$$
Therefore
$$
\begin{aligned}
C_{AAA}
&=\sum_{i=1}^t\left((t+a_i)^2+G-a_i+h_i-(1-m_i+a_i)\right)\\
&=\sum_{i=1}^t\left(t^2+G-1+(2t-1)a_i+m_i+h_i\right)\\
&=t^3-t+(3t-1)G+M+H\\
&=t(t-1)(t+1)+(3t-1)G+M+H.
\end{aligned}
$$
This identifies the three correction statistics explicitly: $G$ records a new run opened by a gap of at least $2$, $M$ records whether the old run avoids becoming a singleton after the first removal, and $H$ records whether the residual gap after opening a new run is still at least $2$.

For the other patterns, a B-pair which is used twice is forced on its second use because the same two odd rows must be returned to even parity. If an A removal opens a new row length at run $i$, this happens exactly when $g_i\geq2$. This gives
$$
\begin{aligned}
C_{ABB}&=\sum_{i=1}^t\binom{t+\mathbf{1}_{\{g_i\geq2\}}}{2}
=\frac{t^2(t-1)}{2}+tG,\\
C_{BBA}&=\sum_{1\leq i<j\leq t}\left(t+\mathbf{1}_{\{g_i\geq2\}}+\mathbf{1}_{\{g_j\geq2\}}\right)
=\frac{t^2(t-1)}{2}+(t-1)G,\\
C_{BAB}&=\sum_{1\leq i<j\leq t}\left(t-2+\mathbf{1}_{\{g_i\geq2\}}+\mathbf{1}_{\{g_j\geq2\}}\right)
=\frac{t(t-1)(t-2)}{2}+(t-1)G.
\end{aligned}
$$
For BBB, after the first B-strip chooses an unordered pair of runs, the second B-strip must share exactly one of those two odd rows and introduce one new row; there are $2(t-1)$ choices, and the third strip is forced. This gives
$$
C_{BBB}=\binom{t}{2}\,2(t-1)=t(t-1)^2.
$$
Adding the five pattern counts yields
$$
c_3(\Lambda(\delta))
=\frac{t(t-1)(7t-2)}{2}+(6t-3)G+M+H.
$$
Since $a_\lambda=c_3(\lambda)+t-1$,
$$
a_{\Lambda(\delta)}
=\frac{(t-1)(7t^2-2t+2)}{2}+(6t-3)G+M+H.
$$

Step 3: Add the conjugate multiplicity
Conjugating $\delta$ interchanges its run multiplicities and its successive gaps, up to reversal. In particular,
$$
G(\delta')=M(\delta),\qquad M(\delta')=G(\delta).
$$
If
$$
K=\#\{i:r_i\geq3\},
$$
then $H(\delta')=K(\delta)$. The number $t$ of distinct parts is unchanged by conjugation. Therefore, with
$$
U=G+M,\qquad W=H+K,
$$
we obtain
$$
a_{\Lambda(\delta)}+a_{\Lambda(\delta')}
=(t-1)(7t^2-2t+2)+(6t-2)U+W.
$$

Step 4: Show that a maximizing partition has $d$ distinct parts
A partition of $n=m/2$ with $t$ distinct parts has size at least $1+2+\cdots+t$, so $t(t+1)\leq m$. So $t\leq d$, where $d$ is the integer defined in the problem.

For fixed $t$, both $U$ and $W$ are at most $2t$, so
$$
a_{\Lambda(\delta)}+a_{\Lambda(\delta')}
\leq (t-1)(7t^2-2t+2)+(6t-2)2t+2t
=7t^3+3t^2+2t-2.
$$
On the other hand, the base term for $t+1$ distinct parts is
$$
t(7(t+1)^2-2(t+1)+2)=7t^3+12t^2+7t,
$$
which exceeds the preceding upper bound by $9t^2+5t+2$. Whenever $t+1\leq d$, the staircase partition $(t+1,t,\ldots,1)$ fits inside size $n$, and extra size can be added by repeating the part $1$ without decreasing the objective. So no $t<d$ can maximize, and every maximizer has $t=d$.

Step 5: Optimize the gap and multiplicity bonuses and attain the bound
Set
$$
q=n-\frac{d(d+1)}{2}=\frac{m-d(d+1)}{2}.
$$
Write
$$
x_i=r_i-1\geq0,\qquad y_i=g_i-1\geq0.
$$
The Ferrers diagram decomposes into the rectangles determined by its runs, giving the exact area identity
$$
n=\sum_{1\leq i\leq j\leq d}r_i g_j.
$$
Subtracting the staircase contribution gives
$$
q=\sum_{i=1}^d(d-i+1)x_i+\sum_{j=1}^d j y_j+\sum_{i\leq j}x_i y_j.
$$
The statistic $U$ counts how many of the $2d$ variables $x_i,y_j$ are positive, while $W$ counts how many are at least $2$. The linear weights occur in the order
$$
1,1,2,2,\ldots,d,d.
$$
If $s$ of these variables are positive, their least possible linear cost is
$$
C_s=1+1+2+2+\cdots\text{ through the first }s\text{ terms}
=\left\lfloor\frac{(s+1)^2}{4}\right\rfloor.
$$
The cross term is nonnegative, so
$$
q\geq C_U+C_W.
$$
Because $d$ is maximal, $0\leq q\leq d$. The coefficient $6d-2$ of $U$ is larger than the maximum possible change in $W$, so $U$ is maximized first. The largest integer with $C_U\leq q$ is
$$
U=e=\left\lceil\sqrt{4q+2}\right\rceil-2.
$$
After paying $C_e$, the largest possible $W$ is
$$
W=f=\left\lceil\sqrt{4(q-C_e)+2}\right\rceil-2.
$$
Since $4q+2=2m-2d(d+1)+2$ and $2C_e=\left\lfloor\frac{(e+1)^2}{2}\right\rfloor$, these are exactly the prompt-defined $e$ and $f$.

It remains to see that the bound is attained. Choose the $e$ positive variables among the cheapest weights, taking $x$-variables from the right end and $y$-variables from the left end. Their indices then satisfy $i>j$, so every cross product $x_i y_j$ with $i\leq j$ vanishes. Set those $e$ variables to $1$, raise the $f$ cheapest selected variables by another $1$, and put any remaining budget into an already counted weight-$1$ variable. This realizes the exact value of $q$ with $U=e$ and $W=f$. Therefore
$$
A_m=(d-1)(7d^2-2d+2)+(6d-2)e+f.
$$

Final Answer: $\boxed{(d-1)(7d^2-2d+2)+(6d-2)e+f}$

---

## Answer

$(d-1)(7d^2-2d+2)+(6d-2)e+f$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

---

## Solution Concepts

- frobenius characteristic
- pieri rule
- specht module conjugation
- partition run statistics
- discrete optimization

---

## Black-Box Audit — no issues found
