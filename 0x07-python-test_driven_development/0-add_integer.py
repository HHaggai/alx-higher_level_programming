#!/usr/bin/python3
# 0-add_integer.py
"""Defynes an intgr additn funct."""


def add_integer(a, b=98):
    """Retrn the intgr additn of a and b.

    Float argts are typecasted to ints before additn is performd.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
