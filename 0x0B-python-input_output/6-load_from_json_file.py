#!/usr/bin/python3
"""Defynes a JSON file-reading functn."""
import json


def load_from_json_file(filename):
    """Creat a Python objct frm a JSON file."""
    with open(filename) as f:
        return json.load(f)
