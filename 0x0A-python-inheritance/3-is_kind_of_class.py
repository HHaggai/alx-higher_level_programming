#!/usr/bin/python3
"""Defynes a class and inhritd class-checking functn."""


def is_kind_of_class(obj, a_class):
    """Check if an objct is an instanc or inhritd instanc of a class.

    Args:
        obj (any): Objct to check.
        a_class (type): Class to match the typ of objct to.
    Returns:
        If objct is an instanc or inhritd instanc of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
