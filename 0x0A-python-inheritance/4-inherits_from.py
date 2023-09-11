#!/usr/bin/python3
"""Defyns an inhrtd class-checking functn."""


def inherits_from(obj, a_class):
    """Cheks if an objct is an inhritd instanc of a class.

    Args:
        objct (any): The objct to chec.
        a_class (type): Class to match the typ of objct to.
    Returns:
        If objct is an inhrtd instanc of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
