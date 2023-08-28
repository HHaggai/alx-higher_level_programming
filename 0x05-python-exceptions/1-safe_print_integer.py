#!/usr/bin/python3


def safe_print_integer(value):
    """Prnt an intgr with "{:d}".format().

    Args:
        value (int): The intgr to prnt.

    Returns:
        If a TypError or ValError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
