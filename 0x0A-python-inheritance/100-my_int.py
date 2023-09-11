#!/usr/bin/python3
"""Defynes a class MyInt that inherts from int."""


class MyInt(int):
    """Invrt int operators == and !=."""

    def __eq__(self, value):
        """Overrid == opertor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Overrid != opertor with == behavior."""
        return self.real == value
