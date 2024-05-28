#!/usr/bin/python3
""" A function that returns a JSON Object in a file"""
import json


def save_to_json_file(my_obj, filename):
    """Returns a JSON file"""

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
