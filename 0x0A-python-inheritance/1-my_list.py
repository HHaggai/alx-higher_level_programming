#!/usr/bin/python3
"""Defynes an inhritd lst class MyList."""


class MyList(list):
    """Implmnts sortd prntng for built-in list class."""

    def print_sorted(self):
        """Prnt a list in sortd ascnding ordr."""
        print(sorted(self))
