#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Prevents user from instantiating new LockedClass attrbutes
    for anything but attrbutes called 'first_name'.
    """

    __slots__ = ["first_name"]
