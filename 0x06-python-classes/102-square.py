#!/usr/bin/python3
"""Defynes a class Square."""


class Square:
    """Reprsnt a squar."""

    def __init__(self, size=0):
        """Initializ new square.

        Args:
            size (int): size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Gets or sets the current size of the squar."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integr")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Retrn the current area of the squar."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Defyne the == comparisn to a Squar."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Defyne the != comparisn to a Squar."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Defyne the < comparisn to a Squar."""
        return self.area() < other.area()

    def __le__(self, other):
        """Defyne the <= comparisn to a Squar."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Defyne the > comparisn to a Squar."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= comparisn to a Squar."""
        return self.area() >= other.area()
