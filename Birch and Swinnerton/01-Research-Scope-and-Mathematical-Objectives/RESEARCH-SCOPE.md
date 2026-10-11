# Research Scope — BSD Part I

**Author:** Philippe Beauchamp  
**ORCID:** [0009-0003-7407-394X](https://orcid.org/0009-0003-7407-394X)  
**Release:** Part I — Research in Progress  
**Canonical archive:** [Zenodo record 23304606](https://zenodo.org/records/23304606)

## 1. Research objective

This research program investigates the Birch and Swinnerton-Dyer (BSD) Conjecture through elliptic-curve arithmetic, analytic rank, real periods, regulators, local factors, rational torsion, the Tate–Shafarevich group, integral-lattice methods, and certificate-based computational protocols. A supplementary Ammonite-inspired geometric model investigates logarithmic-spiral kinematics and a proposed geometry-to-arithmetic connection.

A geometric identity or dynamical derivation does not itself establish a correspondence with an elliptic curve's L-function or arithmetic invariants. Any proposed bridge requires explicitly defined objects and maps, stated hypotheses, and proofs of the relevant properties.

## 2. Evidence labels

- **PROVED:** established under explicit hypotheses and within the stated scope.
- **COMPUTATIONALLY VERIFIED:** supported by a specified computation and its verification conditions.
- **DERIVED:** follows from stated assumptions, definitions, or established results.
- **OPEN:** not established by the current record.

These labels apply to individual claims, not automatically to an entire certificate or research track.

## 3. Main open obligations

1. Recover and bind the original curve-specific input and parameters.
2. Identify the elliptic curve and verify its arithmetic data.
3. Verify rational-point generators, rank, and regulator independently.
4. Complete analytic calculations and real-period normalization under explicit conventions.
5. Verify local factors, torsion, and any Tate–Shafarevich order claims.
6. Establish or reject rigorously the proposed Ammonite-to-arithmetic bridge.
7. Check each theorem and certificate against its full statement, hypotheses, and evidence.

## 4. Conjectural reference formula

Under appropriate hypotheses and normalization conventions, the BSD leading-term formula is conventionally written

\[
\frac{L^{(r)}(E,1)}{r!}=\frac{\Omega_E\,\operatorname{Reg}(E)\,|\Sha(E/\mathbb Q)|\,\prod_{p\mid N}c_p}{|E(\mathbb Q)_{\mathrm{tors}}|^2}.
\]

This is the conjectural reference framework, not a proof of BSD in general and not a curve-specific certification in this release.

## 5. Scientific status and reproducibility

The public Part I archive is research in progress. Curve-specific claims require the exact curve, reproducible inputs, stated conventions, and evidence for every invariant. An identity proved abstractly may still have an open application to the intended elliptic curve.

## 6. Publication

The versioned release and full deposited research files are maintained at [Zenodo DOI 10.5281/zenodo.23304606](https://doi.org/10.5281/zenodo.23304606). The Ammonite records are supplementary geometric investigations, not additional proofs of BSD.