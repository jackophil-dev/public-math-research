# H11 — Invariant Subspace

**Status:** DERIVED FOR THE EXPLICIT Q(i) MODEL + OPEN INTEGRAL/GEOMETRIC CLOSURE

## 1. Objective

H11 identifies the invariant subspace structure already obtained in the explicit Q(i) Weil calibration and connects it to the lattice/discriminant checkpoints of H06–H10.

The central object is the rational Weil-type subspace
[
W_K=\mathbf Q\alpha_1\oplus\mathbf Q\alpha_2.
]

The purpose of this certificate is to record the explicit invariant action without promoting that calculation into a universal statement about all Weil-type fourfolds or all Hodge classes.

## 2. Explicit Q(i) invariant subspace

For the decomposable model
[
A=J\times J,
qquad K=\mathbf Q(i),
]
the public calibration records
[
W_K=\mathbf Q\alpha_1\oplus\mathbf Q\alpha_2.
]

With the chosen convention, the explicit endomorphism corresponding to
[
k=2+i
]
has
[
k^4=-7+24i
]
and acts on the ordered basis ((\alpha_1,\alpha_2)) by
[
(2+i)^*\alpha_1=-7\alpha_1-48\alpha_2,
]
[
(2+i)^*\alpha_2=12\alpha_1-7\alpha_2,
]
up to the documented sign convention associated with the choice of Weil eigenform.

Thus the displayed matrix is
[
M_K=
\begin{pmatrix}
-7&12\\
-48&-7
\end{pmatrix}.
]

This is the explicit invariant-subspace calculation recorded by the present research program.

## 3. Invariance statement

The matrix (M_K) maps the span of ((\alpha_1,\alpha_2)) to itself. Therefore, within the specified rational model,
[
(2+i)^*(W_K)\subseteq W_K.
]

Since the action is induced by the explicit Q(i) endomorphism, this supplies a concrete algebraic symmetry of the two-dimensional Weil subspace.

The statement is model-specific: it does not assert that every Hodge subspace of every Weil-type abelian fourfold has this same matrix or even this same integral realization.

## 4. Connection to the lattice/discriminant data

H06–H10 concern an explicitly selected integral lattice and its arithmetic invariants:
[
G=
\begin{pmatrix}
36&12\\
12&0
\end{pmatrix},
qquad
\det G=-144,
qquad
\operatorname{SNF}(G)=\operatorname{diag}(12,12),
]
with
[
L^*/L\cong(\mathbf Z/12\mathbf Z)^2.
]

H11 does **not** silently identify the basis ((\alpha_1,\alpha_2)) with the H06/H10 integral lattice basis.

The required bridge is an explicit basis-level map
[
\Phi:
W_K\cap H^4(A,\mathbf Z)
\longrightarrow L
]
or an explicitly justified alternative integral model, together with proof of how the pairing and Q(i) action transform under (Phi).

Without that map, the rational invariant subspace and the selected discriminant lattice remain related research objects, not proven identical objects.

## 5. Invariant vs. integral compatibility

There are therefore two distinct questions.

### Rational invariance

For the explicit Q(i) calibration:
[
(2+i)^*(W_K)\subseteq W_K.
]

**Status: DERIVED / COMPUTATIONALLY CHECKABLE.**

### Integral invariance

For an integral lattice (L_{\mathrm{int}}subset W_K), one must additionally prove
[
(2+i)^*(L_{\mathrm{int}})\subseteq L_{\mathrm{int}}
]
and determine the induced finite action on the discriminant quotient.

That requires an explicit integral basis and its embedding. The present public record does not yet supply a complete proof of this compatibility.

**Status: OPEN.**

## 6. Established vs. open

### Established

- The explicit Q(i) model has a two-dimensional rational Weil subspace (W_K).
- The displayed (2+i) action preserves that rational subspace.
- The matrix entries are explicit and computationally checkable.
- The H06 discriminant invariants remain unchanged.
- The H07 saturation boundary remains unchanged.
- H10's local (2)- and (3)-primary discriminant framework remains applicable.

### Open

- explicit identification of (W_K\cap H^4(A,\mathbf Z));
- an integral basis compatible with the selected discriminant lattice;
- preservation of that integral lattice by the Q(i) action;
- the induced action on the finite discriminant group;
- compatibility with the H09 Lefschetz operator;
- complete ambient saturation and geometric cycle-lattice identification;
- any universal invariant-subspace or Hodge-realization theorem.

Thus H11 establishes a concrete rational symmetry while leaving the integral and geometric closure explicitly open.

## 7. Verification target

A complete H11 closure should provide:

1. an explicit integral basis for the relevant sublattice of (W_K);
2. the embedding into (H^4(A,\mathbf Z));
3. the Gram matrix in that basis;
4. the change-of-basis map relating it to the H06/H10 lattice, if they are the same object;
5. the induced integral Q(i) action;
6. the induced action on the discriminant quotient;
7. compatibility tests against the Lefschetz operator from H09.

Until those data are supplied, the correct status is:

**H11 — RATIONAL Q(i) INVARIANT SUBSPACE ESTABLISHED FOR THE EXPLICIT MODEL; INTEGRAL AND GEOMETRIC CLOSURE OPEN.**

### Source note

The invariant-subspace statement here is a direct consequence of the explicit endomorphism matrix already recorded in the public Q(i) calibration. H11 intentionally does not infer a universal theorem from that model-specific calculation.
