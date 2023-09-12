#!/usr/bin/python3
"""Defynes a txt file insrtn functn."""


def append_after(filename="", search_string="", new_string=""):
    """Insrt txt aftr each line containin a givn str in a file.

    Args:
        filename (str): The nam of the fil.
        search_string (str): The str to search for withn the file.
        new_string (str): The str to insrt.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
