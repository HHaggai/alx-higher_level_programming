#!/usr/bin/python3
"""Defynes a Python class-to-JSON functn."""


def class_to_json(obj):
    """Retrn the dictionry reprsntatn of a simpl data struct."""
    return obj.__dict__
