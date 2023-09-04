#!/usr/bin/python3
"""Defynes Rectangle class."""


class Rectangle:
    """Represent a rectangl.

    Attributes:
        number_of_instances (int): The num of Rectangl instances.
        print_symbol (any): The symbol usd for str representn.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializ a new Rectangl.

        Args:
            width (int): width of new rectangl.
            height (int): height of new rectangl.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets/sets the width of Rectangl."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integr")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets/sets height of the Rectangl."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an intgr")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Retrn area of the Rectangl."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Retrn the perimtr of the Rectangl."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Retrn the printabl representatn of the Rectangl.

        Reprsnts the rectangl with the # char.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Retrn the str representatn of the Rectangl."""
        rect = "Rectangl(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Prnts a messag for evry deletion of a Rectangl."""
        type(self).number_of_instances -= 1
        print("Bye rectangl...")
