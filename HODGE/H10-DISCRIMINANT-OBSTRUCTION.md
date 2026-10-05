# H10 — Discriminant Obstruction

**Status:** VERIFIED ARITHMETIC BOUNDARY + OPEN GEOMETRIC OBSTRUCTION

## 1. Objective

H10 packages the discriminant data already established in H06 and H07 as a precise obstruction boundary.

The purpose is not to claim that the discriminant (-144) proves a universal obstruction, nor that the discriminant group ((\mathbf Z/12\mathbf Z)^2) by itself prevents algebraic realization. The invariant becomes an obstruction only after the relevant ambient lattice, embedding, pairing, and candidate cycle lattice have been identified.

## 2. Arithmetic input

For the selected rank-two lattice
[
L=\mathbf Z e_1\oplus\mathbf Z e_2,
]
the recorded Gram matrix is
[
G=
\begin{pmatrix}
36&12\\
12&0
\end{pmatrix}.
]

Its determinant is
[
\det(G)=-144.
]

The Smith normal form is
[
\operatorname{SNF}(G)=\operatorname{diag}(12,12),
]
hence the associated discriminant quotient is
[
L^*/L\cong(\mathbf Z/12\mathbf Z)^2.
]

These are exact arithmetic invariants of the specified lattice.

## 3. What the discriminant can obstruct

Suppose a larger ambient integral lattice (L_{\mathrm{amb}}) and a geometrically defined target lattice (L_{\mathrm{geom}}) are explicitly identified.

Then the discriminant data can be compared through:

- the index of (L) in its saturation;
- the induced finite discriminant group and quadratic/bilinear form;
- compatibility of the pairing with the ambient lattice;
- elementary divisors required by a proposed geometric cycle lattice;
- local-primary data at primes dividing (144), namely (2) and (3).

A mismatch between the required discriminant data and the invariants of a candidate geometric lattice would constitute a concrete obstruction to that particular realization.

This is a **localized obstruction statement**, not a universal Hodge obstruction.

## 4. Relation to H06 and H07

H06 establishes the arithmetic invariants of the selected lattice.

H07 establishes the explicit index-2 extension
[
R=(P+Q)/2,
qquad
[L_1:L_0]=2,
]
and records the candidate determinant/discriminant data after that extension.

H10 therefore does not introduce a new numerical invariant. It changes the role of the existing invariants: they become tests that a proposed ambient or geometric realization must pass.

The boundary is:

[
\text{arithmetic discriminant}
\longrightarrow
\text{candidate realization test}
\longrightarrow
\text{obstruction only if incompatibility is proved}.
]

## 5. Localized analysis at 2 and 3

Because
[
|\det G|=144=2^4\,3^2,
]
only the primes (2) and (3) occur in the discriminant group.

The public record therefore identifies the relevant primary decomposition
[
(\mathbf Z/12\mathbf Z)^2
\cong
(\mathbf Z/4\mathbf Z)^2
\oplus
(\mathbf Z/3\mathbf Z)^2.
]

This gives two concrete local checkpoints:

### At (p=2)

Any proposed integral realization must reproduce the required (2)-primary elementary-divisor structure after the correct ambient embedding and saturation are fixed.

### At (p=3)

The corresponding (3)-primary component must likewise be compatible with the proposed geometric lattice and its pairing.

These local checks are necessary consistency tests for a proposed realization. They are not, by themselves, proofs that no realization exists.

## 6. Established vs. open

### Established

- (G) is explicitly recorded.
- (det(G)=-144).
- (operatorname{SNF}(G)=\operatorname{diag}(12,12)).
- (L^*/L\cong(\mathbf Z/12\mathbf Z)^2).
- The only discriminant primes are (2) and (3).
- The index-2 extension recorded in H07 is explicit.

### Open

- the complete ambient integral lattice (L_{\mathrm{amb}});
- proof that the selected lattice is fully saturated in that ambient lattice;
- geometric identification of the selected lattice with a complete algebraic-cycle lattice;
- comparison of discriminant quadratic forms, not merely group orders;
- a basis-level geometric realization that would turn a mismatch into an actual obstruction;
- any universal obstruction to the Hodge Conjecture or to general Weil-type realization.

Therefore H10 does **not** claim that (-144) is itself a universal obstruction.

## 7. Verification target

A fully realized H10 obstruction would require:

1. an explicit ambient lattice;
2. an explicit embedding of (L);
3. the saturated lattice and its index;
4. its Gram matrix and discriminant form;
5. the corresponding geometric cycle lattice;
6. an exact comparison of finite discriminant data, including the (2)- and (3)-primary parts;
7. a proof that any proposed realization must satisfy the compared invariants.

Until those data exist, the correct status is:

**H10 — DISCRIMINANT INVARIANTS VERIFIED; LOCAL OBSTRUCTION FRAMEWORK ESTABLISHED; GEOMETRIC OBSTRUCTION OPEN.**

### Source note

Discriminant/elementary-divisor comparisons are standard tools in integral Hodge-cycle computations; for example, explicit algorithms for comparing lattices of algebraic cycles and Hodge cycles use elementary divisors as a criterion for matching the corresponding integral lattices. citeturn0academia0

This certificate deliberately distinguishes that general methodology from the unresolved geometric identification in the present research record.
