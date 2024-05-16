#!/usr/bin/python3
"""Documentation"""


class Square():
    """Documentation"""
    def __init__(self, size=0):
        if size is not int:
            raise TypeError
        if size < 0:
            raise ValueError
        else:
            self.__size = size
