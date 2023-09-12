#!/usr/bin/python3
"""Defynes a file-writing functn."""


def write_file(filename="", text=""):
    """Write a str to a UTF8 txt file.

    Args:
        filename (str): The nam of the file to wrte.
        text (str): The txt to writ to the file.
    Returns:
        The numr of chars writtn.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
