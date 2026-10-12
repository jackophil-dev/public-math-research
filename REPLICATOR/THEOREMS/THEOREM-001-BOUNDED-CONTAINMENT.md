# Theorem 001 — Bounded Containment (Conditional)

Let $S\subseteq\mathbb R^n$ be the admissible state space, $\mathcal U$ the admissible controls, and $T$ the transition map. If $T(S\times\mathcal U)\subseteq S$ for every admissible control and $s_0\in S$, then repeated transitions remain in $S$ over the horizon for which the condition holds.

## Proof

By induction on the transition index. The base case is $s_0\in S$. If $s_k\in S$, then for any admissible $u_k\in\mathcal U$, the invariant-set hypothesis gives $s_{k+1}=T(s_k,u_k)\in S$. Therefore every state in the specified finite sequence remains in $S$.

**Status:** DERIVED / CONDITIONAL. The proof is elementary once the invariant-set hypothesis is granted. Establishing that a concrete implementation satisfies that hypothesis is a separate certificate obligation. Feedback and resource bounds alone do not imply containment.