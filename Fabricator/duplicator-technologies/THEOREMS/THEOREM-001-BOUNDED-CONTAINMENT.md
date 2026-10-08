# THEOREM-001 — Bounded Containment (Conditional)

## Statement

Let \(S\subset\mathbb R^n\) be an admissible state space. If the transition law satisfies the explicit positive-invariance condition

\[
T(S\times\mathcal U)\subseteq S
\]

for all admissible controls, and \(s_0\in S\), then the trajectory remains in \(S\) over the declared finite horizon.

## Status

**DERIVED / CONDITIONAL**

The conclusion follows from the stated invariant-set hypothesis. The certificate must independently establish that the actual implementation satisfies that hypothesis.

## Limitation

The earlier informal statement that feedback and resource bounds alone guarantee containment is not retained as an unconditional theorem.
