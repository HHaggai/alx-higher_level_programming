#!/usr/bin/python3
"""Defyne a class Square."""


class Square:
    """Reprsnt a squar."""

    def __init__(self, size=0):
        """Initializ a new squar.

        Args:
            size (int): size of new square.
        """
        self.size = size

    @property
    def size(self):
        """Get current size of the squar."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integr")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Retrn current area of the squar."""
        return (self.__size * self.__size)
