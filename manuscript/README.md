# Counterexamples to the three-distinguishability product conjecture

The note refutes the conjecture in Korzekwa, Czachórski, Puchała and Życzkowski,
*Distinguishing classically indistinguishable states and channels* (2019),
Section III.B, Eq. (30), arXiv:1812.09083v3.

## Contents and mathematical coverage

- `note.tex` is the self-contained LaTeX source; `note.pdf` is its readable PDF.
- `verify.py` checks the exact weighted Gram matrix, residual-weight pairing
  differences, all 24 vertex permutations, and strict rational sign bounds.
- `verification.json` is the deterministic checker output.
- `metadata.json` gives authors, license, source, and covered problem identifier.

For each explicit diagonal, the three density matrices are rank-one projectors
onto the displayed orthogonal vectors. Each diagonal lies strictly inside the bounding tetrahedron but
admits no ordering of the conjectured product weights. The rank-one
characterization of the product weights and the total-variation distance bound
have written proofs. The unitary-completion consequence follows by extending
three orthonormal columns to a unitary matrix.

The pinned Lean declaration `result` in
https://github.com/the-omega-institute/trureturing/blob/73ec20a01fc35e0f53bc258c605821728f3c33b6/D5/S3/Quantum/Measurements/ThreeDistinguishabilityProductRefutation.lean
proves the negation of a fixed-order necessary product condition for the
three-distinguishability region. Its proof excludes every ordering for the
sqrt(5) common diagonal. The written rank-one converse and quantitative
distance bound are separate mathematical statements, not additional conclusions
of that declaration.

## Build

Use Tectonic 0.17.0:

```sh
tectonic note.tex
```

For the PDF's fixed creation date and byte-reproducible output, use:

```sh
SOURCE_DATE_EPOCH=1793923200 tectonic note.tex
```

Alternatively, compile twice with a current pdfLaTeX distribution:

```sh
pdflatex -interaction=nonstopmode -halt-on-error note.tex
pdflatex -interaction=nonstopmode -halt-on-error note.tex
```

The bibliography is embedded. No external images, bibliography files, Python
packages, network access, or shell escape are needed once TeX's standard packages
are available. A fresh Tectonic installation may obtain its standard TeX bundle.

## Exact computation

With Python 3.9 or later, using only its standard library:

```sh
python3 verify.py > verification.json
```

The expected SHA256 of `verification.json` is
`e60028db95712eac7a643153b96428bb9ce0c8e43b87edd145889cb9be80a73d`.

The calculation uses fractions in the cyclotomic field defined by
`z^4-z^3+z^2-z+1=0`, with the specified embedding `z=exp(pi*i/5)`.
Positivity uses the rational interval `11/5 < sqrt(5) < 9/4` and the written
identification of the positive radical. No floating-point tolerance is used.

The rational example `(1/6,1/4,7/24,7/24)` uses the biquadratic field
`Q[u,v]/(u^2+3,v^2+6)`, with `u=i*sqrt(3)` and `v=i*sqrt(6)`.
Both complete weighted Gram matrices equal the identity. All 24 vertex
orderings are excluded for each example. The three family pairing identities
are checked coefficient by coefficient with sparse rational polynomials.

The centre-to-edge inclusion is due to Korzekwa et al. (2019), already in
their 21 December 2018 preprint, Appendix B.1 (Appendix C.1 in v3).
The radial subfamily was constructed by Bengtsson et al. (2004 preprint,
2005 publication), Section 4, Eqs. (35)-(40). The note gives short proofs
and identifies their conflict with the proposed necessary product condition;
the earlier inclusion is not a new result. The sqrt(5) example is outside
that family. The proper-face exclusion is reproved with credit to its source.

The note also proves that every point of the dimension-four,
three-distinguishability region has pure witnesses: a possible rank-two
state is replaced by a pure state using conjugation on the complementary
two-dimensional subspace. The earlier negative-ray pure-state exclusion
therefore holds for mixed states as well, with its central Fourier endpoint
excluded from the exclusion interval.

The family, rank-one converse, distance bounds, pure-state reduction,
radial exclusion, exact three-state capacity and channel instances are
written proofs. The pinned Lean declaration
concerns the sqrt(5) diagonal and does not assert these additional results.

## Authors and license

Haobo Ma — ChronoAI Pte Ltd, Singapore.

Wenlin Zhang — National University of Singapore; ChronoAI Pte Ltd, Singapore.

CC BY 4.0 (Creative Commons Attribution 4.0 International).
