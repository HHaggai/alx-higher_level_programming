#!/usr/bin/python3
"""Defynes a Rectangl subclass Squar."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Reprsnt a squar."""

    def __init__(self, size):
        """Initializ a new squar.

        Args:
            size (int): The size of new squar.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
