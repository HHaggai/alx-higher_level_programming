#!/usr/bin/python3
"""Defyns a class Studnt."""


class Student:
    """Reprsnt a studnt."""

    def __init__(self, first_name, last_name, age):
        """Initializ new Studnt.

        Args:
            first_name (str): The first nam of the studnt.
            last_name (str): The last nam of the studnt.
            age (int): The age of the studnt.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionry reprsntatn of the Studnt."""
        return self.__dict__
