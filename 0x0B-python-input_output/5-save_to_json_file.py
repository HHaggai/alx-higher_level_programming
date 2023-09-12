#!/usr/bin/python3
"""Defynes a JSON file-writing functn."""
import json


def save_to_json_file(my_obj, filename):
    """Write an objct to a txt file usin JSON represntatn."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
