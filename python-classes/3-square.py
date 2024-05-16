#!/usr/bin/python3
"""Dafinition of Class Square"""


class Square():
    """Square class of objects"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates Area"""
        return self.__size ** 2
