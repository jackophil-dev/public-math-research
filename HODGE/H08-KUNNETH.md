# H08 — Künneth Decomposition and Lattice Compatibility

**Author / Researcher:** Philippe Beauchamp  
**ORCID:** [0009-0003-7407-394X](https://orcid.org/0009-0003-7407-394X)

> **Status:** DERIVED FOR THE SPECIFIED ARITHMETIC COMPONENT + OPEN FOR FULL GEOMETRIC COMPATIBILITY
>
> This record connects the explicit Künneth-graded lattice calculation to the Hodge/Weil lattice framework. It does **not** claim that the displayed rank-two lattice is the complete geometric cycle lattice or that the Künneth decomposition alone proves algebraicity.

## 1. Objective

H08 records the Künneth layer between the cohomological model and the integral lattice calculations.

For an abelian fourfold $A$, the middle cohomology is

$$
H^4(A,\mathbf Z),
$$

which carries its standard Künneth grading arising from tensor products of the cohomology of the factors.

The purpose here is to keep three levels distinct:

1. the formal Künneth decomposition of cohomology;
2. the explicitly selected rational/integral component used in the arithmetic calculation;
3. the still-open question of whether that component has been fully identified with the intended geometric Hodge-cycle lattice.

## 2. Künneth framework

For a product $A=J\times J$, the integral cohomology decomposes through the Künneth theorem as

$$
H^4(J\times J,\mathbf Z)
\cong
\bigoplus_{p+q=4}
H^p(J,\mathbf Z)\otimes H^q(J,\mathbf Z),
$$

up to the standard torsion correction terms, which vanish for the free integral cohomology of an abelian variety.

The decomposition provides a natural bookkeeping structure for separating tensor-degree contributions.

In the present research model, a specified middle-dimensional rank-two lattice is extracted from this broader cohomological setting.

## 3. Explicit arithmetic component

The existing Künneth/SNF certificate records a rank-two integral lattice

$$
L=\mathbf Ze_1\oplus\mathbf Ze_2
$$

with intersection matrix

$$
G=
\begin{pmatrix}
36&12\\
12&0
\end{pmatrix}.
$$

Its determinant is

$$
\det(G)=-144.
$$

The gcd of its entries is $12$, giving

$$
\operatorname{SNF}(G)=\operatorname{diag}(12,12),
$$

and therefore

$$
L^*/L
\cong
\mathbf Z/12\mathbf Z\oplus\mathbf Z/12\mathbf Z.
$$

These statements are explicit arithmetic properties of the selected lattice.

## 4. Künneth-to-lattice interpretation

The intended structural chain is

$$
H^4(A,\mathbf Z)
\supseteq
H^4_{\mathrm{selected}}
\supseteq
L
\subseteq
L_{\mathrm{amb}},
$$

where $H^4_{\mathrm{selected}}$ denotes the specified rational/integral component used by the calculation.

The Künneth decomposition supplies the cohomological grading, while the Gram matrix supplies the integral pairing on the selected lattice.

This gives a reproducible bridge from:

$$
\text{cohomological tensor structure}
\longrightarrow
\text{selected component}
\longrightarrow
\text{integral lattice}
\longrightarrow
\text{discriminant data}.
$$

The arithmetic part of this chain is recorded. The full geometric identification of every arrow is not yet established.

## 5. Compatibility questions

A complete Künneth/lattice compatibility result would require independent verification of:

1. the exact embedding of the selected lattice into the relevant Künneth component;
2. the integral basis used for the selected component;
3. compatibility of the intersection pairing with the Künneth decomposition;
4. compatibility with the $Q(i)$ CM action used elsewhere in the dossier;
5. the saturation of the selected lattice in its intended ambient integral component.

Items 1–3 are partly encoded by the explicit arithmetic certificate, but the public record does not yet contain a complete basis-level embedding and projector calculation establishing all five simultaneously.

## 6. Relation to H06 and H07

H06 establishes the arithmetic of the displayed Gram matrix:

$$
\operatorname{SNF}(G)=\operatorname{diag}(12,12),
\qquad
L^*/L\cong(\mathbf Z/12)^2.
$$

H07 records the separate index-2 extension and saturation checkpoint:

$$
R=\frac{P+Q}{2},
\qquad
[L_1:L_0]=2,
\qquad
\operatorname{SNF}=\operatorname{diag}(1,2).
$$

H08 places those arithmetic objects into the larger structural sequence:

$$
\text{Künneth decomposition}
\rightarrow
\text{selected CM/Hodge component}
\rightarrow
\text{integral lattice}
\rightarrow
\text{saturation}
\rightarrow
\text{geometric realization}.
$$

This prevents the Gram-matrix calculation from being silently promoted into a statement about the entire ambient cohomology.

## 7. What H08 establishes and leaves open

### Established / derived

- The standard Künneth decomposition supplies the tensor-degree structure for $H^4(J\times J,\mathbf Z)$.
- A specified rank-two integral component has an explicit Gram matrix.
- Its determinant, SNF, and discriminant group are explicitly calculable.
- The lattice calculation can therefore be tracked as a concrete component of the broader CM/Weil framework.

### Open

- A complete basis-level identification of the selected lattice with a specific Künneth summand.
- Full projector/orthogonality verification for the selected component.
- Complete compatibility between the Künneth decomposition and the $Q(i)$ CM action at the integral-lattice level.
- Full ambient saturation.
- Identification with the complete geometric algebraic-cycle lattice.
- Any general Hodge realization theorem.

## 8. Research status

**Künneth decomposition:** standard cohomological structure.  
**Selected rank-two arithmetic lattice:** explicit and checkable.  
**SNF/discriminant calculation:** verified for the specified lattice.  
**Full Künneth/CM integral compatibility:** OPEN.  
**Projector/orthogonality audit:** OPEN.  
**Ambient saturation:** OPEN.  
**General geometric realization:** NOT ESTABLISHED.

---

**Source record:** [CERTIFICATE-SNF-KUNNETH.md](../docs/RESEARCH/CERTIFICATE-SNF-KUNNETH.md)  
**Researcher:** Philippe Beauchamp  
**ORCID:** 0009-0003-7407-394X
