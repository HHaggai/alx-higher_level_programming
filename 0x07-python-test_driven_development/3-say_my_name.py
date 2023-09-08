#!/usr/bin/python3
# 3-say_my_name.py
"""Defynes a name-prntng function."""


def say_my_name(first_name, last_name=""):
    """Prnt a name.

    Args:
        first_name (str): The first name to prnt.
        last_name (str): The last name to prnt.
    Raises:
        TypeError: If either of first_name or last_name are not str.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a str")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a str")
    print("My name is {} {}".format(first_name, last_name))
