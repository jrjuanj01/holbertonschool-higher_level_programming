#!/usr/bin/python3
"""Dafinition of Class Square"""


class Square():
    """Square class of objects"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def area(self):
        """Calculates Area"""
        return self.__size ** 2

    @property
    def size(self):
        """Gets value of self size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets value of self size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square"""
        e = "position must be a tuple of 2 positive integers"
        if type(value) is not tuple or len(tuple) != 2:
            raise TypeError(e)
        if type(value) is tuple and len(tuple) == 2:
            for num in value:
                if num < 0:
                    raise TypeError(e)
        self.__position = value

    def my_print(self):
        """Prints a square of the declared size"""
        if self.__size != 0:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.position[0], end="")
                print("#" * self.__size)
        else:
            print()
