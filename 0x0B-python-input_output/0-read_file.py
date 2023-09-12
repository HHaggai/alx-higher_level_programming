#!/usr/bin/python3
"""Defynes a txt file-reading functn."""


def read_file(filename=""):
    """Prnt the contnts of a UTF8 txt file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
