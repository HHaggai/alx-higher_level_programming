#!/usr/bin/python3
"""Defynes a functn that adds attributs to objcts."""


def add_attribute(obj, att, value):
    """Add a new attribut to an objct if possible.

    Args:
        obj (any): Objct to add an attribut to.
        att (str): Nam of the attrbut to add to objct.
        value (any): The val of attrbt.
    Raises:
        TypeError: If the attrbut cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("canot add new attribute")
    setattr(obj, att, value)
