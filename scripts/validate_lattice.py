#!/usr/bin/env python3
"""Small reproducible checks for integral Gram matrices.

This script verifies Smith normal form data and, when both Gram matrices
are supplied, the finite-index relation between a lattice and a saturation.
It does not prove geometric saturation without an explicitly specified
ambient lattice and embedding.
"""

import math

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form


def analyze_gram_matrix(matrix_data):
    """Compute SNF invariant factors and determinant of an integral Gram matrix."""
    G = sp.Matrix(matrix_data)

    if any(not value.is_Integer for value in G):
        raise ValueError("Gram matrix entries must be integers.")

    print("--- Gram matrix G ---")
    sp.pprint(G)

    snf = smith_normal_form(G, domain=sp.ZZ)

    print("\n--- Smith normal form ---")
    sp.pprint(snf)

    factors = [
        abs(int(snf[i, i]))
        for i in range(min(snf.rows, snf.cols))
        if snf[i, i] != 0
    ]
    print(f"\nInvariant factors: {factors}")

    det_G = int(G.det())
    print(f"Determinant: {det_G}")

    return factors, det_G


def saturation_index_from_gram_determinants(det_lattice, det_saturation):
    """Return the finite index when Gram determinants describe L and Sat(L)."""
    if det_lattice == 0 or det_saturation == 0:
        raise ValueError("Determinants must be non-zero.")

    ratio = sp.Rational(abs(det_lattice), abs(det_saturation))
    index = sp.sqrt(ratio)

    if index.q != 1:
        raise ValueError(
            "The determinant ratio is not a perfect square; "
            "check that the two Gram matrices describe a finite-index inclusion."
        )

    return int(index)


if __name__ == "__main__":
    # Basic regression example: diag(12, 12).
    test_gram = [
        [12, 0],
        [0, 12],
    ]

    factors, det_G = analyze_gram_matrix(test_gram)

    expected_factors = [12, 12]
    assert factors == expected_factors, (factors, expected_factors)
    assert abs(det_G) == math.prod(expected_factors)

    # Example finite-index relation: det(L) / det(Sat(L)) = 2^2.
    assert saturation_index_from_gram_determinants(48, 12) == 2

    print("\nAll checks passed.")
