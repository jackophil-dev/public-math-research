# Professor Review — Part II
## Open Questions and Verification Targets

**Author:** Philippe Beauchamp  
**Research area:** Hodge theory / algebraic geometry / CM-Weil structures  
**Status:** Public review document — open questions and verification targets

---

## 1. Purpose and scope

Part I records explicit calculations and arithmetic consequences that can be checked directly from the displayed data.

Part II deliberately does **not** add new theorem claims. Its purpose is to identify the precise mathematical steps that should be independently verified, completed, or reformulated before any stronger interpretation is made.

The central principle is:

> **Arithmetic compatibility is not, by itself, geometric realization.**

In particular, compatibility of a displayed lattice, discriminant group, or invariant signature with a proposed Hodge-theoretic model does not establish that the corresponding classes are realized by algebraic cycles, nor does it establish a general proof of the Hodge Conjecture.

---

## 2. Verification Target I — Smith normal form

### Question

For
\[
G_{\mathrm{sat}}=
\begin{pmatrix}
36&12\\
12&0
\end{pmatrix},
\qquad
\det(G_{\mathrm{sat}})=-144,
\]
the arithmetic calculation gives
\[
\operatorname{SNF}(G_{\mathrm{sat}})=\operatorname{diag}(12,12).
\]

The remaining presentation-level target is to exhibit explicit unimodular matrices
\[
P,Q\in GL_2(\mathbb Z)
\]
such that
\[
P G_{\mathrm{sat}} Q=
\begin{pmatrix}
12&0\\
0&12
\end{pmatrix}.
\]

### Verification target

Provide an explicit integer row/column reduction, or explicit \(P,Q\), and verify
\[
\det P=\det Q=\pm1.
\]

### Important distinction

The SNF statement is an arithmetic statement about the displayed integer matrix. Its interpretation as a geometric discriminant or as the discriminant group of a particular realized cycle lattice requires the corresponding lattice identification to be proved separately.

---

## 3. Verification Target II — Exact lattice hierarchy

The current public framework distinguishes three levels:
\[
\Lambda\subseteq\Lambda'\subseteq\Lambda_{\mathrm{sat}}.
\]

Here:

- \(\Lambda\) denotes the initial explicitly generated lattice;
- \(\Lambda'\) denotes the intermediate index-extension step;
- \(\Lambda_{\mathrm{sat}}\) denotes the ambient saturation under consideration.

### Questions

1. What are the exact generators of each lattice?
2. Which inclusion indices are actually computed?
3. Is \([\Lambda':\Lambda]=2\) the only established index, or are further indices known?
4. What is the exact relation between the intermediate extension and ambient saturation?
5. Which quotient groups are explicitly identified?

### Verification target

State each inclusion and quotient independently. Do not infer an index merely from the existence of an inclusion, and do not identify an index-2 extension with the full ambient saturation without proof.

---

## 4. Verification Target III — Discriminant group and quadratic data

For the displayed Gram matrix, the arithmetic Smith data imply an abstract finite abelian group of the form
\[
A\cong(\mathbb Z/12\mathbb Z)^2.
\]

### Questions

1. What is the precise discriminant pairing or quadratic form induced by the lattice?
2. What are its primary components?
3. How does the decomposition into 2-primary and 3-primary parts behave?
4. Which component is relevant to the recorded
\[
q_3(a,b)=\frac{2ab}{3}\pmod{2\mathbb Z}?
\]
5. Is every stated discriminant form derived from the same lattice and coordinate convention?

### Verification target

Separate clearly:

- the abstract group obtained from SNF;
- the bilinear discriminant pairing;
- the quadratic refinement, when defined;
- any geometric interpretation attached to those finite quadratic data.

A group isomorphism alone does not determine the full quadratic structure.

---

## 5. Verification Target IV — S-N-P-I-T formalization

The research framework uses the five-path signature
\[
F(X)=(S,N,P,I,T).
\]

The current status treats this as a research framework rather than an established general theorem.

### Questions

1. What are the exact mathematical definitions of \(S,N,P,I,T\)?
2. Which of the five components are intrinsic invariants?
3. Which depend on choices of coordinates, normalization, basis, or model?
4. What transformations preserve the five-component signature?
5. What information is lost when passing from the original object to \(F(X)\)?
6. Is there a well-defined reconstruction map, or only a proposed reconstruction procedure?

### The parameter \(D=2p=4\)

The recorded certificate #12 uses
\[
D=2p=4
\]
for the degree-4 situation under consideration.

The verification target is **not** to assume that this equality resolves a Hodge obstruction. Rather, the question is:

> What mathematical property, if any, follows formally from the relation \(D=2p\) within the S-N-P-I-T construction?

This should be answered by a definition/proposition with hypotheses, or else retained explicitly as a consistency condition of the model.

---

## 6. Verification Target V — From lattice compatibility to algebraic cycles

This is the principal logical boundary of the dossier.

A chain of implications of the following general shape must not be silently collapsed:
\[
\text{explicit lattice calculation}
\Rightarrow
\text{discriminant compatibility}
\Rightarrow
\text{Hodge-theoretic identification}
\Rightarrow
\text{algebraic-cycle realization}.
\]

Each arrow requires its own hypotheses and proof.

### Questions

1. What is the exact map from the constructed lattice to the relevant Hodge classes?
2. Is the map injective, surjective, or merely a correspondence on a chosen subspace?
3. What theorem establishes that the relevant rational Hodge classes lie in the image of algebraic cycle classes?
4. If an explicit algebraic cycle is constructed, which individual class does it realize?
5. Which conclusions are specific to the decomposable \(J\times J\) model?
6. Which conclusions, if any, extend beyond that model?

### Verification target

Identify the precise **bridge statement** required to pass from arithmetic/lattice compatibility to geometric realization. If that bridge is not proved, it remains an open target.

---

## 7. Verification Target VI — CM/Weil action

The public Part I records the proposed action for \(k=2+i\), with
\[
k^4=-7+24i,
\]
and the corresponding matrix on the chosen basis, subject to the stated sign convention.

### Questions

1. Can the action be independently derived by exterior-power calculation?
2. Which basis and pullback convention are being used?
3. Does the sign convention change under the alternative convention for the CM action?
4. Is the coefficient of magnitude \(48\) invariant under the permitted convention changes?
5. How does the calculation reconcile with the independently described \(T_1/T_2\) coordinates?

### Verification target

Provide the exterior-algebra computation explicitly enough that a reader can reproduce the matrix without relying on the claimed result.

---

## 8. Verification Target VII — Model separation

Two related but distinct settings occur in the dossier:

- the decomposable \(J\times J\) model;
- the separate \(E^4\), \(\mathbb Q(i)\)-Weil lattice with
  \[
  M_W=8I_2.
  \]

### Question

What explicit integral/rational transformation, if any, relates the coordinates used in these two models?

### Verification target

Until such a transformation is established, calculations in one model should not be silently transferred to the other. In particular, the matrix \(8I_2\) should not be identified with the \(J\times J\) coordinate Gram data without an explicit change of basis and proof of compatibility.

---

## 9. What would constitute a publishable standalone result?

A useful next milestone is to isolate a statement whose hypotheses, calculation, and conclusion are completely self-contained.

Candidate categories include:

- a fully explicit lattice/SNF proposition for the displayed matrix;
- a complete calculation of a CM action on the chosen Weil basis;
- a precisely stated algebraic-cycle identity in the decomposable model;
- a formal proposition concerning the invariance or limitations of the S-N-P-I-T construction.

The strongest candidate should be selected only after all required hypotheses and coordinate conventions are made explicit.

---

## 10. Reviewer checklist

A reviewer should be able to answer the following without reconstructing hidden material:

- [ ] Is the SNF calculation correct over \(\mathbb Z\)?
- [ ] Can explicit unimodular reductions be supplied?
- [ ] Are all lattice inclusions and indices stated exactly?
- [ ] Are saturation and index-extension steps distinguished?
- [ ] Is the discriminant group separated from its quadratic/bilinear structure?
- [ ] Are the 2-primary and 3-primary components derived from the displayed data?
- [ ] Are \(S,N,P,I,T\) mathematically defined?
- [ ] Is the meaning of \(D=2p=4\) stated as a theorem, definition, or consistency condition?
- [ ] Is the CM action independently reproducible?
- [ ] Are the \(J\times J\) and \(E^4\) models kept distinct?
- [ ] Is the bridge from lattice compatibility to algebraic-cycle realization explicitly identified?
- [ ] Are model-specific conclusions kept separate from any general Hodge-theoretic claim?

---

## 11. Current status

**Part II is intentionally open-ended.** It records verification targets rather than asserting that those targets have already been solved.

No statement in this document should be read as a proof of the general Hodge Conjecture, a proof of general cycle-class surjectivity, or a proof that the displayed lattice is globally realized by the intended geometric cycle lattice.

The purpose of this document is to make the remaining work precise enough that an independent mathematical reader can verify, reject, strengthen, or complete each step.
