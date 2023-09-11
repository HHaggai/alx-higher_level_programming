#!/usr/bin/python3
"""Defynes a class-checking functn."""


def is_same_class(obj, a_class):
    """Check if an objct is exctly an instanc of a givn class.

    Args:
        obj (any): The objct to chec.
        a_class (type): Class to match the typ of objct to.
    Returns:
        If objct is exctly an instanc of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
