# Replicator — Theorems and Proofs

## Theorem 1 — Invariant-set preservation
Assume \(s_0\in K\) and \(T(s,u)\in K\) for every \(s\in K\), admissible \(u\). Then every trajectory state remains in \(K\).

**Proof.** Base case is \(s_0\in K\). If \(s_t\in K\), the premise gives \(s_{t+1}=T(s_t,u_t)\in K\). Induction proves the result for every \(t\ge0\). \(\square\)

The theorem is conditional: the system-specific preservation premise must be proved.

## Theorem 2 — Safety-gate logic
If execution is authorized only when every required predicate is true, a false required predicate blocks authorization.

**Proof.** Authorization is the conjunction of all required predicates; a conjunction with a false constituent is false. This proves the logic of the gate, not correctness or completeness of its certificates. \(\square\)

Lyapunov convergence claims require a defined error system, positive-definite candidate, verified derivative bound, and applicable domain/regularity conditions. Those implementation-specific premises remain separate obligations.