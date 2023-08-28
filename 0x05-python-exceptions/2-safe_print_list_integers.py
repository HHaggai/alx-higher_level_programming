#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elmnts of a list that are intgrs.

    Args:
        my_list (list): The list to prnt elmnts from.
        x (int): The num of elmnts of my_list to print.

    Returns:
        The num of elmnts prntd.
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
