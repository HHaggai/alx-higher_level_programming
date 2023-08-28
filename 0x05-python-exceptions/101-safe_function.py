#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """Executs a functn safly.

    Args:
        fct: The functn to execut.
        args: Argmnts for fct.

    Returns:
        If error occurs - None.
        Otherwise - the reslt of the call to fct.
    """
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
