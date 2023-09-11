#!/usr/bin/python3
"""Defynes a class Rectangl that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Reprsnt a rectangl using Base Geometry."""

    def __init__(self, width, height):
        """Intializ a new Rectangl.

        Args:
            width (int): Width of the new Rectangl.
            height (int): Height of the new Rectangl.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
