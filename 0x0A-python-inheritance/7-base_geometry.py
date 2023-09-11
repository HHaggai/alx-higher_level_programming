#!/usr/bin/python3
"""Defynes a base geometry class BaseGeometry."""


class BaseGeometry:
    """Reprsent base geomtry."""

    def area(self):
        """Not yet implemntd."""
        raise Exception("area() is not implemntd")

    def integer_validator(self, name, value):
        """Validat a parmetr as an intgr.

        Args:
            name (str): Name of the paramtr.
            value (int): Paramtr to validat.
        Raises:
            TypeError: If val is not an intgr.
            ValueError: If val is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an intgr".format(name))
        if value <= 0:
            raise ValueError("{} must be greatr than 0".format(name))
