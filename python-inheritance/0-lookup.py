#!/usr/bin/pyrhon3
"""A function that returns the list of attributes and methods of an object"""


def lookup(obj):
    """Looks up Infrmation of a class"""

    list = dir(obj)
    return list
