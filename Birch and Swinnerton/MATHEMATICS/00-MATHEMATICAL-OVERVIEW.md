# Birch–Swinnerton-Dyer — Mathematical Overview

**Public scope:** Part I research framework, computational certificates, and open problems. [Zenodo record](https://doi.org/10.5281/zenodo.23304606).

For an elliptic curve \(E/\mathbb Q\), BSD relates the order of vanishing of \(L(E,s)\) at \(s=1\) to the Mordell–Weil rank and predicts a leading-term formula involving the real period, regulator, Tamagawa factors, torsion, and the Tate–Shafarevich group.

A commonly used form, subject to normalization conventions, is
\[
\frac{L^{(r)}(E,1)}{r!}
=\frac{\Omega_E\,\operatorname{Reg}(E)\,|\Sha(E/\mathbb Q)|\prod_{p\mid N}c_p}
{|E(\mathbb Q)_{\rm tors}|^2}.
\]
This is a **conjectural formula**, not a proved result here.

- [01 Definitions and hypotheses](01-DEFINITIONS-AND-HYPOTHESES.md)
- [02 Core equations and derivations](02-CORE-EQUATIONS-AND-DERIVATIONS.md)
- [03 Theorems and proofs](03-THEOREMS-AND-PROOFS.md)
- [04 Computational verification](04-COMPUTATIONAL-VERIFICATION.md)
- [05 Open problems](05-OPEN-PROBLEMS.md)
- Existing [research scope](../Research%20Scope.md), [certificate register](../BSD%20Certificate%20Register.md), and theorem register.

No unrecovered curve or original parameter is guessed. Public Part I is not a proof of general BSD.