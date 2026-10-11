# BSD Certificate Register — C001–C010

**Author:** Philippe Beauchamp  
**Archive:** [Zenodo record 23304606](https://zenodo.org/records/23304606)  
**Status:** Part I research register

A certificate record identifies a verification task or protocol; its existence does not by itself certify the associated arithmetic result.

| ID | Record | Status in Part I description |
|---|---|---|
| C001 | Parameter-Driven Start State and BSD Input Binding | Partially derived; project-specific parameter values and the BSD arithmetic bridge remain open. |
| C002 | Rational Points, Saturation, Height Pairing, and Regulator Protocol | Open; curve-specific data have not been recovered. |
| C003 | Hasse–Weil L-Function, Functional Equation, and Analytic Rank | Open; protocol documented, curve-specific values not certified. |
| C004 | Real Period and Differential Normalization | Open; curve-specific period remains uncertified. |
| C005 | Tamagawa Factors and Rational Torsion | Open; curve-specific invariants remain uncertified. |
| C006 | Tate–Shafarevich Group and Order Evidence | Open; no curve-specific group order has been certified. |
| C007 | Unified BSD Invariant Ledger and Leading-Term Consistency Gate | Open; reference formula recorded, curve-specific invariant ledger incomplete. |
| C008 | Ammonite Image-to-BSD Certification Map | Open; original construction rule and reproducible map unresolved. |
| C009 | Unified Ammonite-Input BSD Certification Audit (SPNIT-Independent) | Standard BSD reference framework recorded; image-driven certification and curve-specific resolution remain open. |
| C010 | Integral-Lattice Transfer, Mordell–Weil Saturation, and Regulator Audit | Method derived; curve-specific application remains open. |

## Reference formula

Under the appropriate hypotheses and normalization conventions, the BSD leading-term formula is conventionally expressed as

\[
\frac{L^{(r)}(E,1)}{r!}
= \frac{\Omega_E\,\operatorname{Reg}(E)\,|\Sha(E/\mathbb Q)|\,\prod_{p\mid N} c_p}
{|E(\mathbb Q)_{\mathrm{tors}}|^2}.
\]

Here the terms include the analytic rank, real period, regulator, Tate–Shafarevich group, Tamagawa factors, and rational torsion. This is a reference formulation of the conjecture, not a claim that the formula has been proved for the general case or certified for a particular curve in this archive.

## Verification boundary

Curve-specific conclusions require the exact curve, reproducible inputs, appropriate conventions, and sufficient evidence for every invariant. A linear-algebraic identity can be proved in isolation while its application to the intended Mordell–Weil group or regulator remains open.
