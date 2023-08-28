#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """Prnts an intgr with "{:d}".format().

    If ValuError message is caught, corespondin
    message is printd to standrd error.

    Args:
        value (int): The intgr to prnt.

    Returns:
        If TypError or ValuError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
