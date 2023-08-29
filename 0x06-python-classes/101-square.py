#!/usr/bin/python3
"""Defynes a class Squar."""


class Square:
    """Reprsnt a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializ a new squar.

        Args:
            size (int): size of the new squar.
            position (int, int): positn of the new squar.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets or sets the current size of the squar."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integr")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets or sets the current positn of the squar."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("positn must be a tuple of 2 positive intgrs")
        self.__position = value

    def area(self):
        """Retrn current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Prnt the square with the # char."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """Defyne the prnt() reprsentatn of a Square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
