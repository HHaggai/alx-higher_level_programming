#!/usr/bin/python3
"""Defyne a MagicClass matching exactly a bytecod prov by Holberton."""

import math


class MagicClass:
    """Reprsnt a circle."""

    def __init__(self, radius=0):
        """Initializ a MagicClass.

        Arg:
            radius (float or int): radius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a numb")
        self.__radius = radius

    def area(self):
        """Retrns the area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Retrn The circumfrnce of the MagicClass."""
        return (2 * math.pi * self.__radius)
