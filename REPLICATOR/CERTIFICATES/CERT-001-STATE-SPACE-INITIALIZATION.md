# CERT-001 — State-Space Initialization

**Class:** Verification specification  
**Status:** SPECIFICATION / OPEN VALIDATION

Define the admissible state space, coordinate conventions, and initial conditions before any transition is executed. For constraints $g_i(s)\le0$, define $D_0=\{s\in\mathbb R^n:g_i(s)\le0,\ i=1,\ldots,m\}$. Initialization is admissible only if $s(0)\in D_0$.

## Evidence required

- State variables and units.
- All constraint functions and parameter values.
- The supplied initial state.
- A reproducible check that every constraint is satisfied.

This certificate defines the test. It does not assert that a physical implementation has passed it.