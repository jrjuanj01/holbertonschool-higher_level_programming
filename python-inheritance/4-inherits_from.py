#!/usr/bin/python3
"""A function tthat veryfies inheritance"""


def inherits_from(obj, a_class):
    """Veryfies inheritance"""

    return isinstance(obj, a_class) and not type(obj) is a_class
