#!/usr/bin/python3
"""A function that returns the dictionary description"""


def class_to_json(obj):
    """Converts a class into Jason format"""

    result = {}
    for key, value in obj.__dict__.items():
        result[key] = value
    return result
 