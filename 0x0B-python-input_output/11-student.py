#!/usr/bin/python3
"""Defynes a class Stdnt."""


class Student:
    """Reprsnt a stdnt."""

    def __init__(self, first_name, last_name, age):
        """Initializ new Stdnt.

        Args:
            first_name (str): The first nam of the stdnt.
            last_name (str): The last nam of the stdnt.
            age (int): The age of the studnt.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionry reprsentatn of the Stdnt.

        If attrs is a list of strs, reprsnts only those attrbuts
        inclded in the list.

        Args:
            attrs (list): (Optional) The attrbuts to reprsnt.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replac all attributs of the Studnt.

        Args:
            json (dict): The key or value pairs to replce attributs with.
        """
        for k, v in json.items():
            setattr(self, k, v)
