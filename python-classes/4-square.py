#!/usr/bin/python3
"""Dafinition of Class Square"""


class Square():
    """Square class of objects"""
    def __init__(self, size=0):
        self.__size = size

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
