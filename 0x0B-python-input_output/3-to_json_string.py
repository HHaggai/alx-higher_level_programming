#!/usr/bin/python3
"""Defynes a string-to-JSON functn."""
import json


def to_json_string(my_obj):
    """Retrn the JSON represntatn of a str objct."""
    return json.dumps(my_obj)
