#!/usr/bin/python3
# 4-print_square.py
"""Defynes a square-prntng func."""


def print_square(size):
    """Print a square with the # char.

    Args:
        size (int): The height/width of the squar.
    Raises:
        TypeError: If size is not an intgr.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an intgr")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
