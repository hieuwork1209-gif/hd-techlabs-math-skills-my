## Steps

Step 1: Fourier diagonalize the antipodal quotient metric

Let
$$
X=\mathbb F_2^8/\langle\mathbf 1\rangle,
$$
where $\mathbf 1=(1,\ldots,1)$. The quotient has $2^7=128$ points. For a coset $[x]$, put
$$
\delta([x])=\min\{\operatorname{wt}(x),8-\operatorname{wt}(x)\}.
$$
Then the metric is translation invariant:
$$
d([x],[y])=\delta([x-y]).
$$

A character of $X$ is
$$
\chi_a([x])=(-1)^{a\cdot x},
$$
where $a\in\mathbb F_2^8$ has even Hamming weight. Thus the nonconstant characters have weights
$$
2,4,6,8
$$
with multiplicities
$$
\binom82=28,\qquad \binom84=70,\qquad \binom86=28,\qquad \binom88=1.
$$

Because the powered distance matrix is the convolution kernel $\delta^p$, these characters diagonalize it. Hence $p$-negative type is equivalent to requiring every nonconstant Fourier eigenvalue to be nonpositive.

Step 2: Compute the four Fourier eigenvalues

Fix an even-weight character $a$ with $\operatorname{wt}(a)=j$. For $0\le k\le8$, let
$$
K_j(k)=\sum_s(-1)^s\binom js\binom{8-j}{k-s}.
$$
This is exactly the sum of $\chi_a(x)$ over all vectors $x$ of Hamming weight $k$, because $s$ records how many of the $k$ chosen coordinates lie in the support of $a$.

Since $j$ is even,
$$
K_j(8-k)=K_j(k).
$$
Each quotient point consists of the antipodal pair $\{x,x+\mathbf1\}$, so the Fourier eigenvalue is
$$
\lambda_j(p)=K_j(1)+2^pK_j(2)+3^pK_j(3)+\frac{4^p}{2}K_j(4).
$$
Directly from the displayed binomial sum,
$$
\begin{array}{c|rrrr}
j&K_j(1)&K_j(2)&K_j(3)&K_j(4)\\
\hline
2&4&4&-4&-10\\
4&0&-4&0&6\\
6&-4&4&4&-10\\
8&-8&28&-56&70
\end{array}
$$
Therefore, with
$$
x=2^p,\qquad y=3^p,\qquad z=4^p=x^2,
$$
we have
$$
\lambda_2=4+4x-4y-5z,
$$
$$
\lambda_4=-4x+3z,
$$
$$
\lambda_6=-4+4x+4y-5z,
$$
$$
\lambda_8=-8+28x-56y+35z.
$$

Step 3: Locate the unique critical exponent

Define
$$
h(p)=\lambda_8(p)=35\cdot4^p-56\cdot3^p+28\cdot2^p-8.
$$
We have
$$
h(0)=-1.
$$
Let
$$
q=\log_2 3.
$$
Since $3^5<2^8$,
$$
1<q<\frac85.
$$
Writing $x=2^p$, differentiation gives
$$
\frac{h'(p)}{14\log2}
=x\left(2+5x-4q x^{q-1}\right).
$$
Put
$$
G(x)=2+5x-4q x^{q-1}.
$$
For $x\ge1$,
$$
G'(x)=5-4q(q-1)x^{q-2}
>5-4\cdot\frac85\cdot\frac35
=\frac{29}{25}>0,
$$
and
$$
G(1)=7-4q>7-\frac{32}{5}=\frac35>0.
$$
Hence $h$ is strictly increasing for every $p\ge0$.

At $p=1/3$, use
$$
2^{1/3}>\frac54,
\qquad
3^{1/3}<\frac{29}{20}.
$$
Then
$$
h\left(\frac13\right)
>-8+28\cdot\frac54-56\cdot\frac{29}{20}+35\cdot\frac{25}{16}
=\frac{39}{80}>0.
$$
Thus there is a unique
$$
\alpha\in\left(0,\frac13\right)
$$
with
$$
35\cdot4^\alpha-56\cdot3^\alpha+28\cdot2^\alpha-8=0.
$$
Numerically,
$$
\alpha\approx0.1353727236.
$$

Step 4: Show that no other Fourier mode reaches zero first

For $0<p\le\alpha$, we have
$$
x=2^p<2^{1/3}<\frac43.
$$
Also
$$
x<y<z.
$$
Therefore
$$
\lambda_2
=4+4x-4y-5z
<4-5x<0,
$$
while
$$
\lambda_4=x(3x-4)<0.
$$
Finally,
$$
\lambda_6
=-4+4x+4y-5z
<-4+4x-z
=-(x-2)^2<0.
$$
Thus the first and only boundary occurs when the weight-$8$ mode satisfies
$$
\lambda_8=0.
$$
Because $h$ is strictly increasing, $\lambda_8>0$ for every $p>\alpha$. Hence
$$
\wp=\alpha.
$$

Step 5: Compute the equality-space dimension

At $p=\alpha$, the weight-$2$, weight-$4$, and weight-$6$ Fourier eigenvalues are strictly negative. The weight-$8$ eigenvalue is zero.

There is exactly one weight-$8$ character, corresponding to
$$
a=\mathbf1.
$$
Hence the kernel inside the zero-sum subspace is one-dimensional, and
$$
\dim E=1.
$$

Final Answer: $\boxed{(\alpha,1),\quad35\cdot4^\alpha-56\cdot3^\alpha+28\cdot2^\alpha-8=0,\quad0<\alpha<\frac13}$

---

## Answer

$(\alpha,1),\quad35\cdot4^\alpha-56\cdot3^\alpha+28\cdot2^\alpha-8=0,\quad0<\alpha<\frac13$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- antipodal quotient of the Hamming cube
- Fourier characters on finite binary groups
- Krawtchouk shell sums
- negative type of finite metric spaces
- spectral multiplicities
