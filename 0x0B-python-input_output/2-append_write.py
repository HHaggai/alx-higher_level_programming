#!/usr/bin/python3
"""Defynes a file-appending functn."""


def append_write(filename="", text=""):
    """Appends a str to the end of UTF8 txt file.

    Args:
        filename (str): The nam of file to append to.
        text (str): The str to append to file.
    Returns:
        The num of chars appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
