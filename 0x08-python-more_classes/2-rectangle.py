#!/usr/bin/python3
"""Defynes a Rectangl class."""


class Rectangle:
    """Reprsnt a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializ new Rectangl.

        Args:
            width (int):  width of new rectangl.
            height (int): height of new rectangl.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets/sets the width of Rectangl."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an intgr")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets/sets height of Rectangl."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an intgr")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Retrns area of the Rectangl."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Retrn the permetr of the Rectangl."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
