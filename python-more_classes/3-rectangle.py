#!/usr/bin/python3
""""This is Class for rectangles"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """Returns rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2*(self.__width + self.__height)

    @property
    def width(self):
        """"Returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def heigth(self):
        """"Returns height"""
        return self.__height

    @heigth.setter
    def height(self, value):
        """Sets the value of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        rec = ""
        for i in range(self.__height):
            rec += "#" * self.__width + "\n"
        return rec
