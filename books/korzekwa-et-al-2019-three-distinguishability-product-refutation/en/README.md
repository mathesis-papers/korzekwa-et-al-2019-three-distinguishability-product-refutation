# One list of probabilities, three orthogonal states

Imagine a device with four lights. For each of three settings, the lights flash in the same proportions: $1/6,1/4,7/24,7/24$. From the flashes alone, you cannot tell the settings apart. Yet in the quantum example here there is another measurement that distinguishes them every time. The trick is that a quantum state has **amplitudes**, not just probabilities. A measurement in the original basis sees the squares of their magnitudes and discards their phases. Phases can still make two vectors orthogonal: their complex inner product can sum to zero.

The question is which lists of four probabilities allow three states to share them while remaining perfectly distinguishable. Call this set $\mathcal A_4^3$. More precisely, the three states are positive semidefinite matrices of trace one with pairwise orthogonal supports. For a pure state, the matrix is $xx^*$ for a unit vector $x$; its diagonal is $(|x_k|^2)_k$. Three orthonormal vectors therefore suffice. Keep these two tests separate: equal squared magnitudes hide the setting in the first measurement; orthogonality reveals it in a different one.

::: {.film src="001-one-diagonal"}
The rational example: the same four probabilities, three orthogonal states, and a two-by-two test that fails in all orderings.
:::

## The proposed shape

Any common diagonal satisfies $p_k\le 1/3$. Indeed, three states with orthogonal supports sum to a matrix bounded above by the identity, so each diagonal entry in that sum is $3p_k\le1$. With $p_k\ge0$ and $\sum_k p_k=1$, these inequalities cut out a tetrahedron. Its vertex $f^j$ has a zero at coordinate $j$ and $1/3$ everywhere else. If you mix the vertices with weights $q_k$, the $k$th coordinate becomes $(1-q_k)/3$. Thus there is only one choice: $q_k=1-3p_k$.

Korzekwa, Czachórski, Puchała and Życzkowski conjectured in §III.B, Eq. (30), that every attainable $p$ comes from two independently weighted binary choices. Indeed, two coins with heads probabilities $a,b$ give the four weights $ab,a(1-b),(1-a)b,(1-a)(1-b)$. Try assigning the four weights to vertices in any order, even a different order for each point. Can every attainable list be obtained that way?

::: {.proposition #rank-one-test mathesis="collected:korzekwa-et-al-2019-three-distinguishability-product-refutation:2:s2" status="written-proof" proof="pf-rank-one-test" doi="10.5281/zenodo.24406607" source="Proposition 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/592"}
**Rank-one test (Ma and Zhang, Proposition 2).** For $0\le p_k\le1/3$ and $\sum_k p_k=1$, arrange the four residual weights $q_k=1-3p_k$ as a table with rows $(u,v)$ and $(w,h)$. This ordering has product form exactly when $uh=vw$. Over all orderings there are precisely three opposite-pair partitions to test.
:::

::: {.proof #pf-rank-one-test}
The two-coin weights give $uh=vw$ by multiplication. Conversely, let $a=u+v$ and $b=u+w$ be the first row and column totals. They lie in $[0,1]$, and $u-ab=uh-vw$ because the table sums to one. If the determinant is zero then $u=ab$; subtract from the totals to recover the other three weights. There was no division, so a zero row or column causes no exception. Across all permutations the index paired with the first index can be any of the other three, and that choice determines both pairs.
:::

## A rational counterexample you can check

::: {.remark #rational-example mathesis="collected:korzekwa-et-al-2019-three-distinguishability-product-refutation:2:s5"}
**Rational example (Corollary 5).** The diagonal $p_*=(1/6,1/4,7/24,7/24)$ is attainable but has no product form for any ordering. Its total-variation distance from the union of product forms is at least $1/192$.
:::

Here are the two independent checks. First, use magnitudes $(\sqrt{1/6},\sqrt{1/4},\sqrt{7/24},\sqrt{7/24})$ in each of three vectors. Multiply those four magnitudes by the phases in one row below. All phases have magnitude one, so each vector has diagonal $p_*$.

| Vector | Phase 1 | Phase 2 | Phase 3 | Phase 4 |
|---|---|---|---|---|
| First | $1$ | $1$ | $1$ | $1$ |
| Second | $1$ | $\omega$ | $v$ | $w$ |
| Third | $1$ | $\omega$ | $w$ | $v$ |

Take $\omega=(-1+i\sqrt3)/2$ and $v,w=-(1+3i\sqrt3)(1\pm i\sqrt6)/14$, respectively. Then $v+w=-(1+3i\sqrt3)/7$. The inner product of the first vector with either other one is $1/6+\omega/4+(7/24)(v+w)=0$. Swapping the phases in the last two positions makes their contribution to the second–third inner product real. Since $\operatorname{Re}(\overline v w)=-5/7$, that inner product is $1/6+1/4+2(7/24)(-5/7)=0$.

Second, forget the phases and compute the unique weights: $(1/2,1/4,1/8,1/8)$. If the $1/2$ is paired with $1/4$ the product difference is $1/8-1/64=7/64$. If it is paired with either $1/8$, the difference is $1/16-1/32=1/32$. All are nonzero. This one calculation rules out **all 24 orderings**. The smallest gap is $1/32$. Changing weights from $q$ to $q'$ can change any pairing difference by at most $\|q-q'\|_1$: expand each product difference and bound each multiplier by one. A product point has a zero pairing, and $\|q-q'\|_1=3\|p-p'\|_1$, so $\tfrac12\|p-p'\|_1\ge1/192$. The failure is not a rounding effect.

::: {.remark #edge-family mathesis="collected:korzekwa-et-al-2019-three-distinguishability-product-refutation:2:s4"}
**Centre-to-edge family (Proposition 4).** Put $c=(1-3t)/4$ and take $p=(c+st,c+(1-s)t,(1+t)/4,(1+t)/4)$ for $0\le s\le1/2$, $0\le t\le1/3$. All these points have pure witnesses (Korzekwa et al., Appendix C.1). If $s<1/2$ and $0<t<1/3$, they all fail the product test.
:::

The rational diagonal uses $s=1/4,t=1/6$. The general construction chooses a phase for the second coordinate so the first two weighted terms sum to a complex number of magnitude $\sqrt{t(1+t)}/2$. The last two terms can cancel it; swapping those phases gives the third orthogonal state. For exclusion, the weights are $(c+3t(1-s),c+3ts,c,c)$. The differences are $3ct+9t^2s(1-s)$ and twice $3ct(1-2s)$, positive in the claimed range. The inclusion still holds at the endpoints; that strict inequality argument does not cover them. The radial subfamily $s=0$ was already obtained by Bengtsson, Ericsson, Kuś, Tadej and Życzkowski.

## A different example and the limits of the result

::: {.remark #interior-example mathesis="collected:korzekwa-et-al-2019-three-distinguishability-product-refutation:2:s1"}
**A counterexample outside that family (Theorem 1).** For $r=\sqrt5$, set $\alpha=(5-r)/10$, $\beta=(5-r)/20$, $\gamma=(r-1)/4$. The point $(\alpha,\beta,\alpha,\gamma)$ lies strictly inside the tetrahedron, has three pure witnesses, and fails for every ordering and every $a,b\in[0,1]$.
:::

Here the repeated coordinates are neither largest nor smallest, unlike the repeated largest coordinates in the centre-to-edge family. The proof uses powers of $z=e^{\pi i/5}$ as phases. The phase rows are $(1,1,1,1)$, $(1,z^2,z^4,z^7)$, and $(-1,z^9,z^3,z^9)$, with the square roots of the same probabilities as magnitudes. To see the cancellation, write $g=(1+\sqrt5)/2$. From $z+\overline z=g$ and $|z|=1$ one gets $z^2=gz-1$; higher powers reduce to a constant plus a multiple of $z$. In the first–second inner product those coefficients are $\alpha-\beta-\alpha g+\gamma$ and $\beta g+\alpha-\gamma g$, both zero. The other inner products vanish using the same identities (Theorem 1). The three pairing differences are $(21-9r)/10,(33-15r)/40,-(21-9r)/10$, all nonzero.

::: {.remark #irrational-distance mathesis="collected:korzekwa-et-al-2019-three-distinguishability-product-refutation:2:s3"}
**Separation for the second example (Corollary 3).** The smallest absolute pairing gap is $(15\sqrt5-33)/40$. The same total-variation estimate gives a lower bound of $(15\sqrt5-33)/240>0$ from the union of product forms.
:::

::: {.remark #state-channel-capacity mathesis="collected:korzekwa-et-al-2019-three-distinguishability-product-refutation:2:s6"}
**States and channels (Corollary 6).** For either example, completing the three vectors to a unitary adds a fourth column of squared magnitudes $1-3p$. So $T(p)=(p\ p\ p\ 1-3p)$ is unistochastic, meaning entrywise squared magnitudes of a unitary. Exactly three states can share either example's diagonal: four orthogonally supported states in dimension four would be four basis vectors, forcing the diagonal to be uniform. Any stochastic matrix with such a column allows at least three distinguishable channels on a fixed unentangled input; for $T(p)$ the number is four. This is about different channels acting on the same input, not four states sharing $p$. The channel constructions specialize Korzekwa et al., Propositions 15 and 19.
:::

::: {.remark #pure-reduction mathesis="collected:korzekwa-et-al-2019-three-distinguishability-product-refutation:2:s8"}
**Pure witnesses suffice in this dimension (Proposition 8).** Every point of $\mathcal A_4^3$ has a pure triple. Hence membership is equivalent to unistochasticity of $(p\ p\ p\ 1-3p)$; its first three columns in a unitary witness also give the converse.
:::

The only ranks other than $(1,1,1)$ are $(2,1,1)$ up to order. The two pure vectors have the same magnitudes, so rotate each coordinate by a common phase to make the vectors conjugates of each other (at zero coordinates the phase is arbitrary). Their orthogonal complement is invariant under conjugation. Average the third density matrix with its conjugate; this keeps the diagonal and gives a real state on the two-dimensional complement. If its orthonormal real eigenvectors are $a,b$ with weights $\lambda,1-\lambda$, the single vector $\sqrt\lambda\,a+i\sqrt{1-\lambda}\,b$ has the same diagonal: the two terms have no real cross term when you square magnitudes. This includes $\lambda=0,1$.

::: {.remark #face-exclusion mathesis="collected:korzekwa-et-al-2019-three-distinguishability-product-refutation:2:s7"}
**Face exclusion (Corollary 7; Korzekwa et al., Appendix C.2).** No point in the relative interior of a two-dimensional face belongs to $\mathcal A_4^3$. This is not an exclusion of the edges or vertices. On such a face one coordinate is $1/3$ while the other three lie strictly between $0$ and $1/3$; the saturated row leaves a two-dimensional row subspace. The phase equations split the three remaining positive weights into two sign classes of equal total. The singleton would have to have half the total weight, forcing a second coordinate to be $1/3$.
:::

::: {.remark #radial-endpoint mathesis="collected:korzekwa-et-al-2019-three-distinguishability-product-refutation:2:s9"}
**Radial endpoint (Corollary 9).** The list $(1-3t,1+t,1+t,1+t)/4$ is excluded for $-1/9\le t<0$. The pure-state phase equations in Bengtsson et al. have no solution when $(1-3t)/(1+t)>1$; the pure-witness reduction extends this to mixed states. At $t=0$, three columns of the Fourier matrix give the uniform diagonal. Thus the centre is not excluded.
:::

## What has and has not been shown

The counterexamples refute **necessity** of Eq. (30), not the converse, and do not characterize the full set or settle its star-shapedness. The public Lean theorem says no *fixed* vertex ordering works on the whole region. Its proof uses the same irrational point for every ordering, but the named statement does not expose the pure/interior witness as its conclusion. The rank-one equivalence and the other claims above have manuscript proofs, not separate verification from that theorem.

::: {.slides src="overview"}
English seminar slides and speaker notes.
:::

**Sources.** Haobo Ma and Wenlin Zhang, [*Counterexamples to Korzekwa et al. (2019)*, version 2](https://doi.org/10.5281/zenodo.24406607). Original conjecture and the centre-to-edge and face results: Korzekwa, Czachórski, Puchała and Życzkowski, [*Distinguishing classically indistinguishable states and channels*](https://doi.org/10.1088/1751-8121/ab30f7), §III.B and Appendix C. Earlier radial construction and phase obstruction: Bengtsson, Ericsson, Kuś, Tadej and Życzkowski, [*Birkhoff's polytope and unistochastic matrices, N = 3 and N = 4*](https://doi.org/10.1007/s00220-005-1392-8), §4 and Appendix C. See the [canonical formalization queue](https://github.com/the-omega-institute/trureturing-requests/issues) and the [upstream contribution guide](https://github.com/the-omega-institute/trureturing/blob/dev/docs/CONTRIBUTING.md) to contribute a focused proof from a fork.
