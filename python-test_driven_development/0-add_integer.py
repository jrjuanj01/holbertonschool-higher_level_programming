#!/usr/bin/python3
"""Script that adds two integers"""


def add_integer(a, b=98):
    """Function that adds"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if a is None or b is None:
        raise TypeError("You must have two integers")
    return int(a) + int(b)
