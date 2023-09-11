#!/usr/bin/python3
"""Defynes an objct attribt lookup functn."""


def lookup(obj):
    """Retrn a list of an object's availbl attrbuts."""
    return (dir(obj))
