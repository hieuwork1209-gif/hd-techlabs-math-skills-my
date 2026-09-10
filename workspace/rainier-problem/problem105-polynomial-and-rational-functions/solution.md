## Steps

Step 1: Encode Eulerian orientations and the automorphism action.

Let the two parts of $K_{6,6}$ be
$$
L=\{u_1,\ldots,u_6\},\qquad R=\{v_1,\ldots,v_6\}.
$$
Encode an orientation by a binary matrix $M=(m_{ij})$ with
$$
m_{ij}=1\iff u_i\to v_j.
$$
Since every vertex has degree $6$, the orientation is Eulerian exactly when every row and every column of $M$ has sum $3$.

Let
$$
H=S_6\times S_6
$$
be the subgroup of $\operatorname{Aut}(K_{6,6})$ preserving the two parts. It acts by independent row and column permutations. The full automorphism group is
$$
G=\operatorname{Aut}(K_{6,6})\cong (S_6\times S_6)\rtimes C_2.
$$
If $\sigma$ exchanges the two parts, then on matrices
$$
\sigma(M)=J_6-M^T, \tag{1}
$$
where $J_6$ is the all-ones matrix. Thus we first classify the row-column permutation orbits under $H$, then apply the involution (1).

Step 2: Classify the $H$-orbits.

Identify a row of $M$ with its support, a $3$-subset of
$$
\Omega=\{1,2,3,4,5,6\}.
$$
Thus $M$ determines a multiset of six $3$-subsets $E_1,\ldots,E_6$ in which every point of $\Omega$ occurs exactly three times. Row permutations forget the ordering of the six sets, while column permutations relabel $\Omega$.

First suppose a support is repeated. No support can occur more than three times. If a support $E$ occurs three times, then its three points already have full degree, so the remaining three supports must all be $E^c$. This gives one type.

If two distinct supports are each repeated, they must be disjoint, since otherwise a common point would occur at least four times. Hence they are complements. The remaining two supports must also be complementary; excluding the preceding triple-multiplicity case leaves one type up to relabeling.

Finally suppose exactly one support $E$ is repeated twice. Across the remaining four supports, the total number of incidences with $E$ is $3$. Since only $E^c$ is disjoint from $E$ and no second support is repeated, the intersection sizes with $E$ must be
$$
1,1,1,0.
$$
Thus $E^c$ occurs once, the other three supports meet $E$ in one point each, and the degree conditions force a unique type up to relabeling.

Now suppose all six supports are distinct. Two disjoint $3$-subsets of $\Omega$ are complementary. Let $n_0$ be the number of complementary pairs among the six supports, and define a graph $\Gamma$ on the six supports by joining two supports when their intersection has size $2$.

For a fixed support $E_i$, the other five supports meet the three points of $E_i$ a total of $6$ times. If $d_i$ is $1$ when $E_i^c$ is present and $0$ otherwise, and $t_i$ is the number of supports meeting $E_i$ in two points, then
$$
t_i-d_i=1. \tag{2}
$$
Hence every vertex of $\Gamma$ has degree $1$ or $2$, with degree $2$ exactly when its complementary support is present.

The value $n_0=2$ is impossible: two complementary pairs already cover every point twice, so the last two supports must themselves be complementary, giving $n_0=3$. Therefore
$$
n_0\in\{0,1,3\}.
$$
If $n_0=0$, equation (2) gives $\Gamma=3K_2$. If $n_0=1$, the two degree-$2$ vertices are the complementary pair and are not adjacent, so $\Gamma=2P_3$. If $n_0=3$, every vertex has degree $2$, so $\Gamma$ is either $C_6$ or $2C_3$. In each case the support family is forced up to relabeling once one support is taken to be $123$.

Writing $123$ for $\{1,2,3\}$ and using exponents for multiplicity, representatives of the seven $H$-orbits are therefore
$$
\begin{array}{c|l}
i&\text{row-support multiset }\mathcal F_i\\ \hline
1&123^3,456^3\\
2&123^2,124,356,456^2\\
3&123^2,145,246,356,456\\
4&123,124,134,256,356,456\\
5&123,124,135,246,356,456\\
6&123,124,135,346,256,456\\
7&123,124,345,346,156,256
\end{array} \tag{3}
$$
For the four all-distinct families, the corresponding $\Gamma$-types are respectively $2C_3,C_6,2P_3,3K_2$ for $i=4,5,6,7$.

Step 3: Compute the seven part-preserving orbit sizes.

For $\mathcal F_i$, let $a_i$ be the number of permutations of $\Omega$ preserving the displayed multiset, and let $\rho_i$ be the product of the factorials of the support multiplicities. Once a column permutation preserves the support multiset, there are exactly $\rho_i$ compatible row permutations. Hence
$$
|\operatorname{Stab}_H(M_i)|=a_i\rho_i. \tag{4}
$$
From the explicit families in (3), their point-automorphism orders and row-multiplicity factors are
$$
\begin{array}{c|r|r|r|r}
i&a_i&\rho_i&|\operatorname{Stab}_H(M_i)|&|H\cdot M_i|\\ \hline
1&72&36&2592&200\\
2&8&4&32&16200\\
3&6&2&12&43200\\
4&12&1&12&43200\\
5&12&1&12&43200\\
6&4&1&4&129600\\
7&24&1&24&21600
\end{array} \tag{5}
$$
because $|H|=(6!)^2=518400$. As a check, the seven orbit sizes sum to
$$
200+16200+3\cdot43200+129600+21600=297200, \tag{6}
$$
the total number of Eulerian orientations.

Step 4: Add the automorphisms exchanging the two parts.

Apply the involution $M\mapsto J_6-M^T$ from (1) to the seven representatives. Directly from the support families in (3), one obtains
$$
1\mapsto1,\qquad
2\mapsto2,\qquad
3\leftrightarrow4,\qquad
5\mapsto5,\qquad
6\mapsto6,\qquad
7\mapsto7. \tag{7}
$$
Thus five $H$-orbits remain single $G$-orbits, while the two $43200$-element orbits numbered $3$ and $4$ merge into one $86400$-element orbit.

Therefore the $G$-orbit sizes, in increasing order, are
$$
200,\quad16200,\quad21600,\quad43200,\quad86400,\quad129600.
$$

Final Answer: $\boxed{(200,16200,21600,43200,86400,129600)}$

---

## Answer

(200,16200,21600,43200,86400,129600)

---

## Classification

Problem Type: Exhaustive enumeration

Answer Type: Tuple or ordered list

---

## Solution Concepts

- Eulerian orientations and regular binary matrices
- automorphism actions on complete bipartite graphs
- regular 3-uniform multihypergraphs
- orbit-stabilizer
- complement-transpose symmetry

---

## Black-Box Audit

No issues found.
