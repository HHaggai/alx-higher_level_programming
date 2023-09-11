#!/usr/bin/python3
"""Defynes a class Rectangl that inhrits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Reprsnt a rectangl using BaseGeometry."""

    def __init__(self, width, height):
        """Intializ a new Rectangl.

        Args:
            width (int): Width of the new Rectangl.
            height (int): Height of the new Rectangl.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Retrn the area of the rectangl."""
        return self.__width * self.__height

    def __str__(self):
        """Retrn the prnt() and str() reprsntatn of a Rectangl."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
