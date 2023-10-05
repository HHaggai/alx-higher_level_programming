#!/usr/bin/python3
"""Module to find the max intgr in a list
"""


def max_integer(list=[]):
    """Funct to find and retrn the max intgr in a list of intgrs
        If the list is empty, the funct retrns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
