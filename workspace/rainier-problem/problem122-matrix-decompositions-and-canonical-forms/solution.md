## Steps

Step 1: Normalize one nonsingular alternating form.

Let
$$
\operatorname{Alt}_6(2)=\{A\in M_6(\mathbb F_2):A^T=A,\ \operatorname{diag}(A)=0\}.
$$
For a $6\times6$ alternating matrix $A$, let $p(A)$ denote its Pfaffian. Since
$$
\det A=p(A)^2
$$
and the ground field is $\mathbb F_2$, $A$ is nonsingular exactly when $p(A)=1$.

All nonsingular alternating forms are congruent. We therefore normalize one nonzero element of the required $3$-space to
$$
J=E_{12}+E_{34}+E_{56}, \tag{1}
$$
where $E_{ij}$ has $1$ in positions $(i,j)$ and $(j,i)$ and zeros elsewhere. Its stabilizer is $Sp_6(2)$, with
$$
|Sp_6(2)|=2^9(2^2-1)(2^4-1)(2^6-1)=1451520. \tag{2}
$$
Hence the number of nonsingular alternating forms is
$$
\frac{|GL_6(2)|}{|Sp_6(2)|}=13888. \tag{3}
$$

Step 2: Count the candidate $3$-spaces containing $J$.

Put $\varepsilon(A)=(-1)^{p(A)}$. From (3),
$$
S:=\sum_A\varepsilon(A)=32768-2\cdot13888=4992. \tag{4}
$$
For every nonsingular $D$ the two-point Pfaffian correlation is
$$
R(D):=\sum_A\varepsilon(A)\varepsilon(A+D)=256. \tag{5}
$$
For $D=J$, (5) follows directly by expanding
$$
p(A)+p(A+J)
$$
in the $15$ upper-triangular coordinates; the six bilinear pairs contribute character sum $2$ and the remaining three-variable part contributes $4$, giving $2^6\cdot4=256$. Congruence invariance gives the same value for every nonsingular $D$.

Thus the number of $B$ satisfying
$$
p(B)=p(B+J)=1
$$
is
$$
\frac{32768-2S+R(J)}4=5760. \tag{6}
$$
These $5760$ matrices form two $Sp_6(2)$-orbits, each of size $2880$. They are distinguished by the Pfaffian pencil and may be represented by
$$
B_1=E_{13}+E_{16}+E_{24}+E_{35},
$$
$$
B_2=E_{12}+E_{16}+E_{24}+E_{35}. \tag{7}
$$
Indeed
$$
p(B_1+tJ)=t^3+t+1,
\qquad
p(B_2+tJ)=t^3+t^2+1, \tag{8}
$$
and these are the two irreducible cubics over $\mathbb F_2$ with constant term and value at $1$ both equal to $1$. The self-adjoint primary decomposition of $J^{-1}B$ gives one symplectic congruence orbit for each polynomial in (8).

Fix either $B=B_i$. A third basis vector $C$ must satisfy
$$
p(C)=p(C+J)=p(C+B)=p(C+J+B)=1. \tag{9}
$$
For a compatible pair $(J,B_i)$, direct Pfaffian expansion gives the triple correlation
$$
Q:=\sum_A\varepsilon(A)\varepsilon(A+J)\varepsilon(A+B_i)=-128. \tag{10}
$$
Also
$$
\lambda_{J,B_i}(A)
=p(A)+p(A+J)+p(A+B_i)+p(A+J+B_i)+1
$$
is a nonzero linear form in the $15$ entries of $A$. Therefore
$$
\sum_A\varepsilon(A)\varepsilon(A+J)\varepsilon(A+B_i)\varepsilon(A+J+B_i)=0. \tag{11}
$$
Expanding the four indicators in (9) now gives
$$
\frac{32768-4S+6R-4Q}{16}
=\frac{32768-19968+1536+512}{16}
=928. \tag{12}
$$
So, with $J$ fixed, the total number of admissible $3$-spaces is
$$
\frac{5760\cdot928}{6\cdot4}=222720. \tag{13}
$$
The denominator is $6\cdot4$: in a fixed $3$-space containing $J$, there are six choices for $B\notin\langle J\rangle$, and then four choices for $C\notin\langle J,B\rangle$.

Step 3: Determine the $Sp_6(2)$-orbits in the normalized slice.

For $0\ne v\in\mathbb F_2^6$, define the symplectic transvection
$$
T_v(x)=x+\langle x,v\rangle_Jv. \tag{14}
$$
The $63$ maps $T_v$ generate $Sp_6(2)$; symplectic Gaussian elimination expresses every element of $Sp_6(2)$ as a product of such transvections.

Encode an alternating matrix by its $15$ upper-triangular entries and encode a $3$-space by the reduced row-echelon form of any $3\times15$ basis matrix. For each $B_i$, condition (9) gives $928$ values of $C$, but adding any element of $\langle J,B_i\rangle$ to $C$ gives the same $3$-space, so there are $928/4=232$ normalized seeds for each $B_i$.

Applying congruence by the generators (14) to these $464$ seeds gives exactly three connected components. Representatives and component sizes are
$$
\begin{array}{c|c|c|r}
& B & C & \text{$Sp_6(2)$-orbit size}\\ \hline
1 & E_{13}+E_{16}+E_{24}+E_{35}
  & E_{14}+E_{16}+E_{25}+E_{36} & 161280\\
2 & E_{12}+E_{16}+E_{24}+E_{35}
  & E_{14}+E_{25}+E_{36}+E_{45} & 60480\\
3 & E_{12}+E_{16}+E_{24}+E_{35}
  & E_{13}+E_{25}+E_{35}+E_{46} & 960
\end{array} \tag{15}
$$
where each representative means $\langle J,B,C\rangle$.

Every listed representative satisfies $p(A)=1$ for all seven nonzero $A$ in the span. Moreover,
$$
161280+60480+960=222720, \tag{16}
$$
which equals the complete count (13). Thus (15) is an exhaustive $Sp_6(2)$-orbit decomposition of all admissible $3$-spaces containing $J$.

Step 4: Pass from the normalized slice to full $GL_6(2)$-congruence.

Every $GL_6(2)$-orbit meets the slice containing $J$, because every nonzero element of an admissible $3$-space is a nonsingular alternating form and hence can be carried to $J$ by congruence.

It remains to check that the three components in (15) do not merge when a different nonzero element of the same $3$-space is chosen as the distinguished form. For each representative $W_i$ in (15) and each of its seven nonzero forms $A$, perform symplectic Gram-Schmidt to obtain $g_A$ with
$$
g_A^TAg_A=J.
$$
Reducing $g_A^TW_ig_A$ by the transvection orbit procedure of Step 3 returns the same component $i$ for all seven choices of $A$. Hence no full congruence orbit joins two different rows of (15).

As a numerical certificate, the stabilizers in the normalized slice have orders
$$
\frac{1451520}{161280}=9,
\qquad
\frac{1451520}{60480}=24,
\qquad
\frac{1451520}{960}=1512. \tag{17}
$$
The seven re-normalizations above are all internal to the same component, so the corresponding full $GL_6(2)$ stabilizer orders are
$$
63,\qquad168,\qquad10584, \tag{18}
$$
which are pairwise distinct. Therefore the three rows of (15) are pairwise noncongruent and exhaustive.

Final Answer: $\boxed{3}$

---

## Answer

3

---

## Classification

Problem Type: Exact computation

Answer Type: Exact scalar

---

## Solution Concepts

- alternating bilinear forms over finite fields
- simultaneous matrix congruence
- Pfaffian correlation counts
- symplectic transvections and stabilizer orbits
- canonical orbit representatives

---

## Black-Box Audit

The only finite enumeration is the explicit orbit traversal in Step 3: states are $3\times15$ RREF encodings, and the acting generators are the 63 displayed symplectic transvections. The component sizes sum to the independently derived total count (13).