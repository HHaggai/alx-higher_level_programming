#!/usr/bin/python3
# 101-lazy_matrix_mul.py
"""Defynes a matrix multiplicatn functn using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Retrn the multiplicatn of two matrices.

    Args:
        m_a (list of lists of ints/floats): The frst matrix.
        m_b (list of lists of ints/floats): The secnd matrix.
    """

    return (np.matmul(m_a, m_b))
