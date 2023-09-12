#!/usr/bin/python3
# 6-from_json_string.py
"""Defynes a JSON-to-object functn."""
import json


def from_json_string(my_str):
    """Retrn the Python objct represntatn of a JSON str."""
    return json.loads(my_str)
