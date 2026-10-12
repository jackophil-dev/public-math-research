# Replicator — Mathematical Overview

**Milestone:** v0.50-RC1, 50% architecture release. [Selected Zenodo record](https://doi.org/10.5281/zenodo.23204583).

This is a formal control-and-verification architecture, not evidence of a working universal matter-replication device.

Pipeline: **Measurement → Comparison → Correction → Invariant/Safety Checks → Execution Decision**.

Let \(s_t\in S\), \(u_t\in\mathcal U\), and \(s_{t+1}=T(s_t,u_t)\). If \(s_0\in K\) and \(T(K,\mathcal U_{adm})\subseteq K\), then all admissible states remain in \(K\). The proof is conditional; a concrete system must establish the premise.

- [01 Definitions and hypotheses](01-DEFINITIONS-AND-HYPOTHESES.md)
- [02 Core equations and derivations](02-CORE-EQUATIONS-AND-DERIVATIONS.md)
- [03 Theorems and proofs](03-THEOREMS-AND-PROOFS.md)
- [04 Computational verification](04-COMPUTATIONAL-VERIFICATION.md)
- [05 Open problems](05-OPEN-PROBLEMS.md)
- [Framework](../MATHEMATICAL-FRAMEWORK.md), [certificates](../CERTIFICATES/), [theorems](../THEOREMS/)

Formal specification, simulated behavior, and experimental validation are distinct evidence classes.