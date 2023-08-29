#!/usr/bin/python3
"""Defyne a class Square."""


class Square:
    """Reprsnt a squar."""

    def __init__(self, size=0):
        """Initializ a new squar.

        Args:
            size (int): size of the new squar.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integr")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Retrn current area of the squar."""
        return (self.__size * self.__size)
