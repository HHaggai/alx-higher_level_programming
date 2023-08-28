#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elmnts of a list.

    Args:
        my_list (list): list to prnt elmnts from.
        x (int): The num of elmnts of my_list to print.

    Returns:
        The num of elmnts printd.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
